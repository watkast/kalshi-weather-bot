"""Lag tracker for Kalshi's 15-minute crypto up/down markets (paper money).

Question: when a coin's price moves on the big exchanges, how long does
Kalshi's price take to follow, and is the gap big enough to trade?

  * Coinbase and Kraken prices arrive live over websockets (no polling delay).
  * Kalshi's prices are polled every 0.5 seconds.
  * Every 0.25 seconds the bot turns the live coin price into a fair chance of UP
    (same random-walk model as the 15-minute study). When that fair chance moves
    5¢+ within 3 seconds, it logs an "event" and watches how Kalshi's price reacts.
  * Paper trade: at the first Kalshi price seen after the event, if the favored
    side's ask is still 3¢+ below fair value after fees, buy 10 contracts.
    Three exits are scored on the same buy: sell 10 seconds later, sell 30
    seconds later, or hold to the close.

Files (under lag/): events.csv, status.json. Dashboard: LAG.md
"""
import json
import math
import os
import statistics
import subprocess
import sys
import threading
import time
from collections import deque
from datetime import datetime, timezone

import requests
import websocket

from common import HERE, fee_per_contract, get_markets, kalshi_get, load_rows
from fifteen_bot import asset_of, iso, models, parse_ts, side_quote, write_csv

DIR = os.path.join(HERE, "lag")
EVENTS = os.path.join(DIR, "events.csv")
STATUS = os.path.join(DIR, "status.json")
PAGE = os.path.join(HERE, "LAG.md")

KALSHI_POLL = 0.5         # seconds between Kalshi price checks
TICK = 0.25               # seconds between fair-value checks
MOVE = 0.05               # fair chance must move this much...
WINDOW = 3.0              # ...within this many seconds to count as an event
COOLDOWN = 15.0           # seconds before the same market can fire again
MIN_SECS_LEFT, MAX_SECS_LEFT = 75, 870
FAIR_RANGE = (0.03, 0.97)
MIN_EDGE = 0.03           # paper buy only if ask is this far below fair after fees
MAX_SPREAD = 0.05
CONTRACTS = 10
EXITS = (10, 30)          # seconds after the buy
FOLLOW = (1, 2, 5, 10, 30)
SAVE_MINUTES = 10
RUN_MINUTES = float(os.environ.get("RUN_MINUTES", "330"))

CANDLES = "https://api.exchange.coinbase.com/products/{}-USD/candles"
COINBASE_WS = "wss://ws-feed.exchange.coinbase.com"
KRAKEN_WS = "wss://ws.kraken.com/v2"

FIELDS = ["time", "ticker", "asset", "secs_left", "direction", "source", "spot_before", "spot_after",
          "fair_before", "fair_after", "kalshi_before", "kalshi_at_entry", "entry_delay",
          "already_moved", "react_secs"] + [f"kalshi_{s}s" for s in FOLLOW] + [
          "side", "fair_side", "ask", "fee", "edge", "traded",
          "exit10_bid", "pnl10", "exit30_bid", "pnl30", "result", "pnl_close", "status"]


def now_ts():
    return time.time()


def utc(ts):
    return datetime.fromtimestamp(ts, timezone.utc)


def mid(q):
    """Kalshi YES mid from a quote tuple (t, yes_bid, yes_ask)."""
    if q is None or q[1] is None or q[2] is None:
        return None
    return (q[1] + q[2]) / 2


class Feeds:
    """Live coin prices from Coinbase and Kraken websockets."""

    def __init__(self, assets, errors):
        self.assets = sorted(assets)
        self.errors = errors
        self.last = {}            # (source, asset) -> (recv_ts, price)
        self.delays = deque(maxlen=2000)   # Coinbase exchange-time -> receive delay, seconds
        self.msgs = {"coinbase": 0, "kraken": 0}

    def start(self):
        threading.Thread(target=self._run, args=("coinbase",), daemon=True).start()
        threading.Thread(target=self._run, args=("kraken",), daemon=True).start()

    def price(self, asset, max_age=15.0):
        """Freshest price, Coinbase first. Returns (price, source) or (None, None)."""
        t = now_ts()
        for src in ("coinbase", "kraken"):
            v = self.last.get((src, asset))
            if v and t - v[0] <= max_age:
                return v[1], src
        return None, None

    def _run(self, src):
        while True:
            try:
                url = COINBASE_WS if src == "coinbase" else KRAKEN_WS
                ws = websocket.WebSocketApp(url, on_open=lambda w: self._subscribe(w, src),
                                            on_message=lambda w, m: self._on(src, m))
                ws.run_forever(ping_interval=20, ping_timeout=10)
            except Exception as exc:
                self.errors.append(f"{iso(datetime.now(timezone.utc))} {src} ws: {exc}")
            time.sleep(3)

    def _subscribe(self, ws, src):
        if src == "coinbase":
            ws.send(json.dumps({"type": "subscribe", "channels": ["ticker"],
                                "product_ids": [f"{a}-USD" for a in self.assets]}))
        else:
            for a in self.assets:     # one at a time, so an unlisted coin can't block the rest
                ws.send(json.dumps({"method": "subscribe",
                                    "params": {"channel": "ticker", "symbol": [f"{a}/USD"]}}))

    def _on(self, src, raw):
        t = now_ts()
        try:
            m = json.loads(raw)
        except ValueError:
            return
        if src == "coinbase":
            if m.get("type") != "ticker" or "price" not in m:
                return
            asset = m["product_id"].split("-")[0]
            self.last[("coinbase", asset)] = (t, float(m["price"]))
            self.msgs["coinbase"] += 1
            if m.get("time"):
                try:
                    self.delays.append(t - parse_ts(m["time"]).timestamp())
                except ValueError:
                    pass
        else:
            if m.get("channel") != "ticker":
                return
            for d in m.get("data") or []:
                if d.get("last"):
                    self.last[("kraken", d["symbol"].split("/")[0])] = (t, float(d["last"]))
                    self.msgs["kraken"] += 1


class Lag:
    def __init__(self):
        self.events = load_rows(EVENTS)
        self.errors = []
        self.lock = threading.Lock()
        self.series = []
        self.markets = {}        # ticker -> {"close": ts, "strike": float, "asset": str}
        self.quotes = {}         # ticker -> deque of (t, yes_bid, yes_ask)
        self.rtts = deque(maxlen=2000)
        self.closes = {}         # asset -> recent 1-minute closes
        self.fair = {}           # ticker -> deque of (t, fair, spot)
        self.cool = {}           # ticker -> last event ts
        self.pending = []        # events still being followed (live dicts in self.events)
        self.last_series = self.last_refresh = self.last_candles = 0.0
        self.feeds = None

    # ---- slow work: series, markets, volatility, results ----
    def load_series(self):
        found = []
        for s in kalshi_get("/series", {}).get("series", []):
            t = s["ticker"]
            if s.get("category") == "Crypto" and (s.get("frequency") == "fifteen_min" or t.endswith("15M")) \
                    and not any(k in t for k in ("TEST", "CRYPTOLEAD", "CRYPTOCOMP")):
                found.append(t)
        self.series = found
        self.last_series = now_ts()
        print(f"watching {len(found)} series: {sorted(asset_of(s) for s in found)}")

    def refresh(self):
        out = {}
        for st in self.series:
            try:
                for m in get_markets(max_pages=1, series_ticker=st, status="open"):
                    if m.get("floor_strike") in (None, ""):
                        continue
                    out[m["ticker"]] = {"close": parse_ts(m["close_time"]).timestamp(),
                                        "strike": float(m["floor_strike"]), "asset": asset_of(st)}
            except Exception as exc:
                self.errors.append(f"{iso(datetime.now(timezone.utc))} refresh {st}: {exc}")
        with self.lock:
            self.markets = out
        self.last_refresh = now_ts()

    def candles(self):
        for a in {m["asset"] for m in self.markets.values()}:
            try:
                r = requests.get(CANDLES.format(a), params={"granularity": 60}, timeout=5)
                rows = sorted(r.json(), key=lambda c: c[0])[-61:]
                self.closes[a] = [float(c[4]) for c in rows]
            except Exception as exc:
                self.errors.append(f"{iso(datetime.now(timezone.utc))} candles {a}: {exc}")
        self.last_candles = now_ts()

    def settle(self):
        t = now_ts()
        for e in self.events:
            if e["status"] != "awaiting result":
                continue
            close = self.markets.get(e["ticker"], {}).get("close")
            if close and close > t:
                continue
            try:
                m = kalshi_get(f"/markets/{e['ticker']}")["market"]
            except Exception:
                continue
            res = m.get("result")
            if res not in ("yes", "no", "void") or m.get("status") not in ("settled", "finalized", "determined"):
                continue
            e["result"] = res
            if e["traded"] == "yes":
                cost = float(e["ask"]) + float(e["fee"])
                won = 1.0 if res == e["side"] else 0.0
                e["pnl_close"] = f"{0.0 if res == 'void' else CONTRACTS * (won - cost):.2f}"
            e["status"] = "done"

    def slow_loop(self):
        while True:
            try:
                if now_ts() - self.last_series > 3600:
                    self.load_series()
                if now_ts() - self.last_refresh > 60:
                    self.refresh()
                    self.settle()
                if now_ts() - self.last_candles > 60:
                    self.candles()
            except Exception as exc:
                self.errors.append(f"{iso(datetime.now(timezone.utc))} slow: {exc}")
            time.sleep(5)

    # ---- Kalshi prices every 0.5 s ----
    def kalshi_loop(self):
        while True:
            start = now_ts()
            live = [tk for tk, m in self.markets.items() if m["close"] > start]
            try:
                for i in range(0, len(live), 50):
                    t0 = now_ts()
                    data = kalshi_get("/markets", {"tickers": ",".join(live[i:i + 50]), "limit": 1000})
                    t1 = now_ts()
                    self.rtts.append(t1 - t0)
                    stamp = (t0 + t1) / 2
                    with self.lock:
                        for m in data.get("markets", []):
                            bid, ask = side_quote(m, "yes")
                            self.quotes.setdefault(m["ticker"], deque(maxlen=400)).append((stamp, bid, ask))
            except Exception as exc:
                self.errors.append(f"{iso(datetime.now(timezone.utc))} kalshi: {exc}")
                time.sleep(2)
            time.sleep(max(0.05, KALSHI_POLL - (now_ts() - start)))

    def quote_at(self, tk, ts, after=False):
        """Last Kalshi quote at or before ts, or (after=True) the first one after ts."""
        q = self.quotes.get(tk)
        if not q:
            return None
        if after:
            return next((x for x in q if x[0] > ts), None)
        best = None
        for x in q:
            if x[0] <= ts:
                best = x
            else:
                break
        return best

    # ---- fair value every 0.25 s ----
    def tick(self):
        t = now_ts()
        with self.lock:
            markets = dict(self.markets)
        for tk, m in markets.items():
            secs_left = m["close"] - t
            if secs_left <= 0:
                continue
            spot, src = self.feeds.price(m["asset"])
            closes = self.closes.get(m["asset"])
            if spot is None or not closes:
                continue
            mod = models(spot, m["strike"], secs_left, closes + [spot])
            if not mod:
                continue
            fair = mod["vol"]
            hist = self.fair.setdefault(tk, deque(maxlen=int(WINDOW / TICK) + 4))
            hist.append((t, fair, spot))
            if not (MIN_SECS_LEFT <= secs_left <= MAX_SECS_LEFT) or t - self.cool.get(tk, 0) < COOLDOWN:
                continue
            old = [h for h in hist if t - h[0] <= WINDOW]
            lo, hi = min(old, key=lambda h: h[1]), max(old, key=lambda h: h[1])
            if fair - lo[1] >= MOVE and lo[0] < t:
                base, direction = lo, "up"
            elif hi[1] - fair >= MOVE and hi[0] < t:
                base, direction = hi, "down"
            else:
                continue
            if not (FAIR_RANGE[0] <= fair <= FAIR_RANGE[1]):
                continue
            with self.lock:
                before = self.quote_at(tk, base[0])
            self.cool[tk] = t
            e = {"time": iso(utc(t), ms=True), "ticker": tk, "asset": m["asset"], "secs_left": int(secs_left),
                 "direction": direction, "source": src, "spot_before": base[2], "spot_after": spot,
                 "fair_before": f"{base[1]:.4f}", "fair_after": f"{fair:.4f}",
                 "kalshi_before": f"{mid(before):.4f}" if mid(before) is not None else "",
                 "traded": "no", "status": "following", "_t": t, "_close": m["close"],
                 "_strike": m["strike"], "_closes": closes}
            self.events.append(e)
            self.pending.append(e)
            print(f"EVENT {tk} {direction} fair {base[1]:.2f}->{fair:.2f} ({src})")

    def follow(self):
        t = now_ts()
        keep = []
        for e in self.pending:
            t0, tk = e["_t"], e["ticker"]
            with self.lock:
                entry = self.quote_at(tk, t0, after=True)
            if entry is None:
                keep.append(e)
                continue
            fb, fa = float(e["fair_before"]), float(e["fair_after"])
            need = abs(fa - fb) / 2
            sign = 1 if e["direction"] == "up" else -1
            kb = float(e["kalshi_before"]) if e["kalshi_before"] else None
            if not e.get("kalshi_at_entry"):
                e["kalshi_at_entry"] = f"{mid(entry):.4f}" if mid(entry) is not None else ""
                e["entry_delay"] = f"{entry[0] - t0:.2f}"
                if kb is not None and mid(entry) is not None:
                    e["already_moved"] = "yes" if sign * (mid(entry) - kb) >= need else "no"
                self.paper_buy(e, entry)
            with self.lock:
                q = list(self.quotes.get(tk, []))
            if kb is not None and not e.get("react_secs"):
                hit = next((x for x in q if x[0] > t0 and mid(x) is not None and sign * (mid(x) - kb) >= need), None)
                if hit:
                    e["react_secs"] = f"{hit[0] - t0:.2f}"
            for s in FOLLOW:
                key = f"kalshi_{s}s"
                if not e.get(key) and t - t0 >= s:
                    x = self.quote_at(tk, t0 + s)
                    e[key] = f"{mid(x):.4f}" if mid(x) is not None else ""
            if e["traded"] == "yes":
                for s in EXITS:
                    if not e.get(f"exit{s}_bid") and t - entry[0] >= s:
                        x = self.quote_at(tk, entry[0] + s)
                        bid = None
                        if x and x[1] is not None and x[2] is not None:
                            bid = x[1] if e["side"] == "yes" else 1 - x[2]
                        if bid is not None and bid > 0:
                            xfee = fee_per_contract(bid, CONTRACTS)
                            pnl = CONTRACTS * (bid - xfee - float(e["ask"]) - float(e["fee"]))
                        else:
                            bid, pnl = 0.0, None   # no bid: count as still holding, scored at close
                        e[f"exit{s}_bid"] = f"{bid:.4f}"
                        e[f"pnl{s}"] = f"{pnl:.2f}" if pnl is not None else ""
            done = t - t0 >= max(FOLLOW) + 1 and (e["traded"] == "no" or all(e.get(f"exit{s}_bid") for s in EXITS))
            if done:
                e["status"] = "awaiting result"   # record the outcome for every event, traded or not
            else:
                keep.append(e)
        self.pending = keep

    def paper_buy(self, e, entry):
        _, bid, ask = entry
        if bid is None or ask is None or ask - bid > MAX_SPREAD:
            return
        secs_left = e["_close"] - entry[0]
        spot, _ = self.feeds.price(e["asset"])
        mod = models(spot, e["_strike"], secs_left, e["_closes"] + [spot]) if spot else None
        if not mod:
            return
        up = mod["vol"]
        side = "yes" if e["direction"] == "up" else "no"
        fair_side = up if side == "yes" else 1 - up
        price = ask if side == "yes" else 1 - bid
        fee = fee_per_contract(price, CONTRACTS)
        edge = fair_side - price - fee
        e.update(side=side, fair_side=f"{fair_side:.4f}", ask=f"{price:.4f}", fee=f"{fee:.4f}", edge=f"{edge:.4f}")
        if edge >= MIN_EDGE and 0.05 <= price <= 0.95:
            e["traded"] = "yes"
            print(f"  BUY {e['ticker']} {side} @ {price:.2f} fair {fair_side:.2f} edge {edge:+.2f}")

    # ---- saving ----
    def save(self):
        write_csv(EVENTS, self.events, FIELDS)
        rtt = statistics.median(self.rtts) if self.rtts else None
        cb = statistics.median(self.feeds.delays) if self.feeds and self.feeds.delays else None
        with open(STATUS, "w") as fh:
            json.dump({"saved_at": iso(datetime.now(timezone.utc)), "windows_watched": len(self.markets),
                       "events": len(self.events),
                       "trades": sum(1 for e in self.events if e.get("traded") == "yes"),
                       "kalshi_poll_rtt_s": round(rtt, 3) if rtt else None,
                       "coinbase_delay_s": round(cb, 3) if cb is not None else None,
                       "ws_messages": self.feeds.msgs if self.feeds else {},
                       "errors": self.errors[-20:]}, fh, indent=1)
        write_page(self.events, rtt, cb)
        subprocess.run(["git", "add", "lag", "LAG.md"], cwd=HERE, capture_output=True)
        if subprocess.run(["git", "commit", "-q", "-m", "lag tracker update"], cwd=HERE,
                          capture_output=True).returncode != 0:
            return
        for _ in range(3):
            if subprocess.run(["git", "pull", "-q", "--rebase", "-X", "theirs"], cwd=HERE,
                              capture_output=True).returncode != 0:
                subprocess.run(["git", "rebase", "--abort"], cwd=HERE, capture_output=True)
            if subprocess.run(["git", "push", "-q"], cwd=HERE, capture_output=True).returncode == 0:
                return
            time.sleep(3)


def _f(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def summarize(rows):
    """Lag stats for a group of events."""
    react = [_f(e.get("react_secs")) for e in rows if _f(e.get("react_secs")) is not None]
    moved = [e for e in rows if e.get("already_moved") in ("yes", "no")]
    caught = []
    for e in rows:
        kb, k2, fb, fa = (_f(e.get("kalshi_before")), _f(e.get("kalshi_2s")),
                          _f(e.get("fair_before")), _f(e.get("fair_after")))
        if None not in (kb, k2, fb, fa) and fa != fb:
            caught.append((k2 - kb) / (fa - fb))
    return {
        "n": len(rows),
        "react": statistics.median(react) if react else None,
        "never": len(rows) - len(react),
        "ahead": (sum(1 for e in moved if e["already_moved"] == "yes") / len(moved)) if moved else None,
        "caught2": statistics.median(caught) if caught else None,
    }


def trade_stats(trades, key):
    done = [t for t in trades if _f(t.get(key)) is not None]
    if key != "pnl_close":
        # a timed exit with no bid falls back to the close result
        done = [t for t in trades if _f(t.get(key)) is not None or _f(t.get("pnl_close")) is not None]
    pnls = [(_f(t.get(key)) if _f(t.get(key)) is not None else _f(t.get("pnl_close"))) for t in done]
    risked = sum(CONTRACTS * (float(t["ask"]) + float(t["fee"])) for t in done)
    half = len(pnls) // 2
    return {"n": len(pnls), "won": sum(1 for p in pnls if p > 0), "pnl": sum(pnls),
            "ret": sum(pnls) / risked if risked else 0.0,
            "h1": sum(pnls[:half]), "h2": sum(pnls[half:])}


def write_page(events, rtt=None, cb=None):
    seen = [e for e in events if e.get("kalshi_at_entry")]
    trades = [e for e in events if e.get("traded") == "yes"]
    allstats = summarize(seen)
    exits = {"Sell after 10 sec": "pnl10", "Sell after 30 sec": "pnl30", "Hold to the close": "pnl_close"}
    ts = {label: trade_stats(trades, key) for label, key in exits.items()}
    best_label, best = max(ts.items(), key=lambda kv: kv[1]["pnl"]) if trades else (None, None)

    if len(seen) < 50:
        verdict = "🟡 **Too early.** Collecting data — needs at least 50 events."
    elif best and best["n"] >= 30 and best["pnl"] > 0 and best["h1"] > 0 and best["h2"] > 0:
        verdict = (f"🟢 **There's a tradable gap.** Buying right after a price jump made money in both "
                   f"halves of the data ({best_label.lower()}).")
    elif allstats["ahead"] is not None and allstats["ahead"] >= 0.7:
        verdict = ("🔴 **Kalshi is too fast.** Most of the time Kalshi's price has already moved by the "
                   "time we can see it, so there's no gap to trade.")
    else:
        verdict = "🔴 **No profitable gap yet.** Kalshi sometimes lags, but not by enough to beat the fees."

    def fmt(v, pct=False, secs=False):
        if v is None:
            return "—"
        if pct:
            return f"{v:.0%}"
        return f"{v:.1f}s" if secs else f"{v:.2f}"

    lines = [
        "# Lag Tracker", "",
        f"*Updated {datetime.now(timezone.utc):%a %b %d %H:%M} UTC. Paper money. Coin prices arrive live from "
        "Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move "
        "shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and "
        "paper-buy the favored side if it's still 3¢+ cheap after fees.*", "",
        "[← Back to all bots](README.md)", "",
        "## Verdict", "", verdict, "",
        "## How fast does Kalshi follow?", "",
        "| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |",
        "|---|---|---|---|---|",
    ]
    for a in sorted({e["asset"] for e in seen}):
        s = summarize([e for e in seen if e["asset"] == a])
        lines.append(f"| {a} | {s['n']} | {fmt(s['react'], secs=True)} | {fmt(s['ahead'], pct=True)} | "
                     f"{fmt(s['caught2'], pct=True)} |")
    lines.append(f"| **All** | **{allstats['n']}** | **{fmt(allstats['react'], secs=True)}** | "
                 f"**{fmt(allstats['ahead'], pct=True)}** | **{fmt(allstats['caught2'], pct=True)}** |")
    lines += ["",
        "*\"Catches up\" = Kalshi's price moved at least half as far as our fair value did. "
        "\"Already moved\" = that had happened by the first Kalshi price we saw after the jump — those are "
        "moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*", "",
        "## Paper trades on the gap", "",
        "| Exit | Trades | Won | P&L | Return | Earlier / later half |",
        "|---|---|---|---|---|---|",
    ]
    for label, s in ts.items():
        lines.append(f"| {label} | {s['n']} | {s['won']} | ${s['pnl']:.2f} | {s['ret']:+.1%} | "
                     f"${s['h1']:.2f} / ${s['h2']:.2f} |")
    lines += ["", "*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — "
              "order-book depth isn't checked).*", ""]
    if rtt is not None or cb is not None:
        lines += ["## Feed speed", "",
                  f"Kalshi price check round trip: **{fmt(rtt, secs=True) if rtt is None else f'{rtt * 1000:.0f} ms'}** · "
                  f"Coinbase price delay: **{'—' if cb is None else f'{cb * 1000:.0f} ms'}**", ""]
    lines += ["## Latest events", "",
              "| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |",
              "|---|---|---|---|---|---|---|---|"]
    for e in seen[-30:][::-1]:
        trade = (f"{'UP' if e['side'] == 'yes' else 'DOWN'} @ {float(e['ask']):.2f}"
                 if e.get("traded") == "yes" else "—")
        pnl = " / ".join(e.get(k) or "·" for k in ("pnl10", "pnl30", "pnl_close")) if e.get("traded") == "yes" else ""
        lines.append(f"| {e['time'][5:19].replace('T', ' ')} | {e['asset']} | {e['direction']} | "
                     f"{float(e['fair_before']):.2f}→{float(e['fair_after']):.2f} | "
                     f"{e.get('kalshi_before') and f'{float(e['kalshi_before']):.2f}' or '—'} → "
                     f"{e.get('kalshi_at_entry') and f'{float(e['kalshi_at_entry']):.2f}' or '—'} → "
                     f"{e.get('kalshi_5s') and f'{float(e['kalshi_5s']):.2f}' or '—'} | "
                     f"{e.get('react_secs') and e['react_secs'] + 's' or 'no'} | {trade} | {pnl} |")
    with open(PAGE, "w") as fh:
        fh.write("\n".join(lines) + "\n")


def main():
    os.makedirs(DIR, exist_ok=True)
    bot = Lag()
    for e in bot.events:     # unfinished rows from an earlier run can't be followed any more
        if e["status"] == "following":
            e["status"] = "awaiting result" if e.get("traded") == "yes" else "done"
    bot.load_series()
    bot.refresh()
    bot.candles()
    bot.feeds = Feeds({m["asset"] for m in bot.markets.values()} or {asset_of(s) for s in bot.series}, bot.errors)
    bot.feeds.start()
    threading.Thread(target=bot.kalshi_loop, daemon=True).start()
    threading.Thread(target=bot.slow_loop, daemon=True).start()
    time.sleep(5)
    end = now_ts() + RUN_MINUTES * 60
    last_save = now_ts()
    while now_ts() < end:
        start = now_ts()
        try:
            bot.tick()
            bot.follow()
        except Exception as exc:
            bot.errors.append(f"{iso(datetime.now(timezone.utc))} {exc}")
            print("error:", exc)
        if now_ts() - last_save > SAVE_MINUTES * 60:
            bot.save()
            last_save = now_ts()
        time.sleep(max(0.01, TICK - (now_ts() - start)))
    time.sleep(max(FOLLOW) + 2)
    bot.follow()
    bot.settle()
    bot.save()


if __name__ == "__main__":
    sys.exit(main())
