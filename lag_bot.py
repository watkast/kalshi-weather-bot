"""Lag tracker for Kalshi's 15-minute crypto up/down markets (paper money).

Question: when a coin's price moves on the big exchanges, how long does
Kalshi's price take to follow, and is the gap big enough to trade?

  * Coinbase and Kraken prices arrive live over websockets (no polling delay).
  * Kalshi's quoted prices are polled every 0.5 seconds (used to time the lag).
  * Every 0.25 seconds the bot turns the live coin price into a fair chance of UP
    (same random-walk model as the 15-minute study). When that fair chance moves
    5¢+ within 3 seconds -- using one exchange's price throughout, so switching
    feeds can't fake a jump -- it logs an "event" and watches how Kalshi reacts.
  * Paper trade (since Oct 4): the moment an event fires, the bot pulls Kalshi's
    live order book and prices 10 contracts by walking it, exactly as a real order
    would fill. It decides with only what it knew at that instant (coin price at
    the time of the book snapshot). It buys only if the fill is 3¢+ below fair
    value after fees. Exits are also priced on the live book: sell 10 seconds
    later, sell 30 seconds later, or hold to the close.
  * Each event also records the gap between the quoted price and the real order
    book, so we can see whether the "lag" is real or just a stale quote.

Rows before Oct 4 were priced at the quoted price; the dashboard keeps them apart.

Files (under lag/): events.csv, status.json. Dashboard: LAG.md
"""
import json
import os
import statistics
import subprocess
import sys
import threading
import time
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

import requests
import websocket

from common import HERE, KALSHI, fee_per_contract, get_markets, kalshi_get, load_rows
from fifteen_bot import asset_of, iso, models, parse_ts, side_quote, write_csv

DIR = os.path.join(HERE, "lag")
EVENTS = os.path.join(DIR, "events.csv")
STATUS = os.path.join(DIR, "status.json")
PAGE = os.path.join(HERE, "LAG.md")

KALSHI_POLL = 0.5         # seconds between Kalshi quote checks
TICK = 0.25               # seconds between fair-value checks
MOVE = 0.05               # fair chance must move this much...
WINDOW = 3.0              # ...within this many seconds to count as an event
COOLDOWN = 15.0           # seconds before the same market can fire again
MIN_SECS_LEFT, MAX_SECS_LEFT = 75, 870
FAIR_RANGE = (0.03, 0.97)
MIN_EDGE = 0.03           # buy only if the order-book fill is this far below fair after fees
STRICT_EDGE = 0.10        # dashboard also scores a stricter 10¢ rule on the same trades
MAX_SPREAD = 0.05
PRICE_RANGE = (0.05, 0.95)
CONTRACTS = 10
EXITS = (10, 30)          # seconds after the buy
FOLLOW = (1, 2, 5, 10, 30)
SPOT_MAX_AGE = 3.0        # a coin price older than this is too stale to trade a lag on
BOOK_TIMEOUT = 3.0
SAVE_MINUTES = 10
MAX_ERRORS = 200
RUN_MINUTES = float(os.environ.get("RUN_MINUTES", "330"))

CANDLES = "https://api.exchange.coinbase.com/products/{}-USD/candles"
COINBASE_WS = "wss://ws-feed.exchange.coinbase.com"
KRAKEN_WS = "wss://ws.kraken.com/v2"

FIELDS = ["time", "ticker", "asset", "secs_left", "direction", "source", "spot_before", "spot_after",
          "fair_before", "fair_after", "kalshi_before", "kalshi_at_entry", "entry_delay",
          "already_moved", "react_secs"] + [f"kalshi_{s}s" for s in FOLLOW] + [
          "side", "fair_side", "ask", "fee", "edge", "traded",
          "exit10_bid", "pnl10", "exit30_bid", "pnl30", "result", "pnl_close", "status",
          # order-book fields (Oct 4 on)
          "fill", "book_secs", "book_rtt", "quote_ask", "book_best", "book_depth", "skip"]

_local = threading.local()


def session():
    """One keep-alive HTTP session per thread (saves a TLS handshake per call)."""
    s = getattr(_local, "s", None)
    if s is None:
        s = _local.s = requests.Session()
    return s


def now_ts():
    return time.time()


def utc(ts):
    return datetime.fromtimestamp(ts, timezone.utc)


def mid(q):
    """Kalshi YES mid from a quote tuple (t, yes_bid, yes_ask)."""
    if q is None or q[1] is None or q[2] is None:
        return None
    return (q[1] + q[2]) / 2


def fetch_book(ticker):
    """Live order book -> ({"yes": [(price, qty)], "no": [...]} bids, round-trip secs)."""
    t0 = now_ts()
    r = session().get(f"{KALSHI}/markets/{ticker}/orderbook", timeout=BOOK_TIMEOUT)
    r.raise_for_status()
    rtt = now_ts() - t0
    book = r.json().get("orderbook_fp") or {}
    out = {}
    for side in ("yes", "no"):
        out[side] = [(float(p), float(q)) for p, q in (book.get(f"{side}_dollars") or []) if float(q) > 0]
    return out, rtt


def walk(levels, contracts):
    """Fill `contracts` against price levels listed best-first.
    Returns (average price, best price, contracts on the book) or None if too thin."""
    if not levels:
        return None
    need, cost = contracts, 0.0
    for px, qty in levels:
        take = min(need, qty)
        cost += take * px
        need -= take
        if need <= 1e-9:
            return round(cost / contracts, 4), levels[0][0], sum(q for _, q in levels)
    return None


def buy_levels(book, side):
    """Prices to BUY `side`: matching the other side's bids at 1 - their price, cheapest first."""
    other = "no" if side == "yes" else "yes"
    return sorted((round(1 - p, 4), q) for p, q in book[other])


def sell_levels(book, side):
    """Prices to SELL `side`: its own bids, highest first."""
    return sorted(book[side], key=lambda x: -x[0])


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

    def price(self, asset, max_age=SPOT_MAX_AGE, source=None):
        """Freshest price, Coinbase first (or only `source`). Returns (price, source) or (None, None)."""
        t = now_ts()
        for src in ((source,) if source else ("coinbase", "kraken")):
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
        try:
            if src == "coinbase":
                if m.get("type") != "ticker" or "price" not in m:
                    return
                asset = m["product_id"].split("-")[0]
                self.last[("coinbase", asset)] = (t, float(m["price"]))
                self.msgs["coinbase"] += 1
                if m.get("time"):
                    self.delays.append(t - parse_ts(m["time"]).timestamp())
            else:
                if m.get("channel") != "ticker":
                    return
                for d in m.get("data") or []:
                    if d.get("last"):
                        self.last[("kraken", d["symbol"].split("/")[0])] = (t, float(d["last"]))
                        self.msgs["kraken"] += 1
        except (ValueError, KeyError, TypeError):
            pass


class Lag:
    def __init__(self):
        self.events = load_rows(EVENTS)
        self.errors = []
        self.lock = threading.RLock()
        self.series = []
        self.markets = {}        # ticker -> {"close": ts, "strike": float, "asset": str}
        self.quotes = {}         # ticker -> deque of (t, yes_bid, yes_ask)
        self.rtts = deque(maxlen=2000)
        self.book_rtts = deque(maxlen=2000)
        self.closes = {}         # asset -> recent 1-minute closes
        self.fair = {}           # ticker -> deque of (t, fair, spot, source)
        self.cool = {}           # ticker -> last event ts
        self.pending = []        # events still being followed (live dicts in self.events)
        self.pool = ThreadPoolExecutor(max_workers=4)
        self.last_series = self.last_refresh = self.last_candles = 0.0
        self.feeds = None

    def err(self, msg):
        self.errors.append(f"{iso(datetime.now(timezone.utc))} {msg}")
        del self.errors[:-MAX_ERRORS]

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
                self.err(f"refresh {st}: {exc}")
        with self.lock:
            self.markets = out
            live = set(out)
            for tk in [tk for tk in self.quotes if tk not in live]:
                del self.quotes[tk]
            for tk in [tk for tk in self.fair if tk not in live]:
                del self.fair[tk]
        self.last_refresh = now_ts()

    def candles(self):
        for a in {m["asset"] for m in self.markets.values()}:
            try:
                r = session().get(CANDLES.format(a), params={"granularity": 60}, timeout=5)
                rows = sorted(r.json(), key=lambda c: c[0])[-61:]
                if len(rows) >= 21:
                    self.closes[a] = [float(c[4]) for c in rows]
            except Exception as exc:
                self.err(f"candles {a}: {exc}")
        self.last_candles = now_ts()

    def settle(self):
        t = now_ts()
        with self.lock:
            waiting = [e for e in self.events if e["status"] == "awaiting result"]
        for e in waiting:
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
            with self.lock:
                e["result"] = res
                if e.get("traded") == "yes":
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
                self.err(f"slow: {exc}")
            time.sleep(5)

    # ---- Kalshi quotes every 0.5 s ----
    def kalshi_loop(self):
        while True:
            start = now_ts()
            with self.lock:
                live = [tk for tk, m in self.markets.items() if m["close"] > start]
            try:
                for i in range(0, len(live), 50):
                    t0 = now_ts()
                    r = session().get(f"{KALSHI}/markets", timeout=5,
                                      params={"tickers": ",".join(live[i:i + 50]), "limit": 1000})
                    t1 = now_ts()
                    if r.status_code == 429:
                        time.sleep(1)
                        continue
                    r.raise_for_status()
                    self.rtts.append(t1 - t0)
                    stamp = (t0 + t1) / 2
                    with self.lock:
                        for m in r.json().get("markets", []):
                            bid, ask = side_quote(m, "yes")
                            self.quotes.setdefault(m["ticker"], deque(maxlen=400)).append((stamp, bid, ask))
            except Exception as exc:
                self.err(f"kalshi: {exc}")
                time.sleep(2)
            time.sleep(max(0.05, KALSHI_POLL - (now_ts() - start)))

    def quote_at(self, tk, ts, after=False):
        """Last Kalshi quote at or before ts, or (after=True) the first one after ts."""
        with self.lock:
            q = list(self.quotes.get(tk, ()))
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
    def fair_now(self, m, secs_left, source=None):
        spot, src = self.feeds.price(m["asset"], source=source)
        closes = self.closes.get(m["asset"])
        if spot is None or not closes:
            return None, None, None
        mod = models(spot, m["strike"], secs_left, closes + [spot])
        return (mod["vol"] if mod else None), spot, src

    def tick(self):
        t = now_ts()
        with self.lock:
            markets = dict(self.markets)
        for tk, m in markets.items():
            secs_left = m["close"] - t
            if secs_left <= 0:
                continue
            fair, spot, src = self.fair_now(m, secs_left)
            if fair is None:
                continue
            hist = self.fair.setdefault(tk, deque(maxlen=int(WINDOW / TICK) + 4))
            hist.append((t, fair, spot, src))
            if not (MIN_SECS_LEFT <= secs_left <= MAX_SECS_LEFT) or t - self.cool.get(tk, 0) < COOLDOWN:
                continue
            old = [h for h in hist if t - h[0] <= WINDOW and h[3] == src]   # same exchange only
            if len(old) < 2:
                continue
            lo, hi = min(old, key=lambda h: h[1]), max(old, key=lambda h: h[1])
            if fair - lo[1] >= MOVE and lo[0] < t:
                base, direction = lo, "up"
            elif hi[1] - fair >= MOVE and hi[0] < t:
                base, direction = hi, "down"
            else:
                continue
            if not (FAIR_RANGE[0] <= fair <= FAIR_RANGE[1]):
                continue
            before = self.quote_at(tk, base[0])
            self.cool[tk] = t
            e = {"time": iso(utc(t), ms=True), "ticker": tk, "asset": m["asset"], "secs_left": int(secs_left),
                 "direction": direction, "source": src, "spot_before": base[2], "spot_after": spot,
                 "fair_before": f"{base[1]:.4f}", "fair_after": f"{fair:.4f}",
                 "kalshi_before": f"{mid(before):.4f}" if mid(before) is not None else "",
                 "traded": "no", "fill": "book", "status": "following", "_t": t, "_m": m,
                 "_entry": "queued", "_exits": {}}
            with self.lock:
                self.events.append(e)
                self.pending.append(e)
            self.pool.submit(self.enter, e)
            print(f"EVENT {tk} {direction} fair {base[1]:.2f}->{fair:.2f} ({src})")

    # ---- order-book entry and exits (worker threads) ----
    def enter(self, e):
        tk, m = e["ticker"], e["_m"]
        side = "yes" if e["direction"] == "up" else "no"
        upd = {"side": side}
        try:
            try:
                book, rtt = fetch_book(tk)
            except Exception as exc:
                upd["skip"] = "book error"
                self.err(f"book {tk}: {exc}")
                return
            tb = now_ts()
            self.book_rtts.append(rtt)
            upd.update(book_secs=f"{tb - e['_t']:.2f}", book_rtt=f"{rtt:.3f}")
            q = self.quote_at(tk, tb)           # what the quote feed was showing at that moment
            if q and q[1] is not None and q[2] is not None:
                upd["quote_ask"] = f"{(q[2] if side == 'yes' else 1 - q[1]):.4f}"
            fill = walk(buy_levels(book, side), CONTRACTS)
            if fill is None:
                upd["skip"] = "book too thin"
                return
            avg, best, depth = fill
            upd.update(book_best=f"{best:.4f}", book_depth=f"{depth:.0f}")
            bid_side = walk(sell_levels(book, side), 1)
            fair, _, _ = self.fair_now(m, m["close"] - tb, source=e["source"])   # only what we knew then
            if fair is None:
                upd["skip"] = "coin price stale"
                return
            fair_side = fair if side == "yes" else 1 - fair
            fee = fee_per_contract(avg, CONTRACTS)
            edge = fair_side - avg - fee
            upd.update(fair_side=f"{fair_side:.4f}", ask=f"{avg:.4f}", fee=f"{fee:.4f}", edge=f"{edge:.4f}")
            if bid_side is None or best - bid_side[1] > MAX_SPREAD:
                upd["skip"] = "spread too wide"
            elif not (PRICE_RANGE[0] <= avg <= PRICE_RANGE[1]):
                upd["skip"] = "price out of range"
            elif edge < MIN_EDGE:
                upd["skip"] = "edge gone"
            else:
                upd["traded"] = "yes"
                upd["_entry_t"] = tb
                print(f"  BUY {tk} {side} @ {avg:.3f} (best {best:.2f}, depth {depth:.0f}) "
                      f"fair {fair_side:.2f} edge {edge:+.2f}")
        except Exception as exc:
            upd["skip"] = "error"
            self.err(f"enter {tk}: {exc}")
        finally:
            with self.lock:
                e.update(upd)
                e["_entry"] = "done"

    def exit_at(self, e, s):
        tk, side = e["ticker"], e["side"]
        bid, pnl = 0.0, None
        try:
            book, rtt = fetch_book(tk)
            self.book_rtts.append(rtt)
            fill = walk(sell_levels(book, side), CONTRACTS)
            if fill:
                bid = fill[0]
                pnl = CONTRACTS * (bid - fee_per_contract(bid, CONTRACTS) - float(e["ask"]) - float(e["fee"]))
        except Exception as exc:
            self.err(f"exit book {tk}: {exc}")
        with self.lock:
            # no buyers for 10 contracts: we'd still be holding, so it's scored at the close
            e[f"exit{s}_bid"] = f"{bid:.4f}"
            e[f"pnl{s}"] = f"{pnl:.2f}" if pnl is not None else ""
            e["_exits"][s] = "done"

    # ---- lag measurement from the quote feed ----
    def follow(self):
        t = now_ts()
        keep = []
        for e in list(self.pending):
            t0, tk = e["_t"], e["ticker"]
            with self.lock:
                traded, et, entry_state = e.get("traded") == "yes", e.get("_entry_t"), e["_entry"]
            if traded:
                for s in EXITS:
                    if s not in e["_exits"] and t - et >= s:
                        e["_exits"][s] = "queued"
                        self.pool.submit(self.exit_at, e, s)
            exits_done = all(e["_exits"].get(s) == "done" for s in EXITS)
            entry = self.quote_at(tk, t0, after=True)
            if entry is None:   # quote feed hiccup: give it a minute, then just score the outcome
                if t - t0 >= 60 and entry_state == "done" and (not traded or exits_done):
                    e["status"] = "awaiting result"
                else:
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
            if kb is not None and not e.get("react_secs"):
                with self.lock:
                    q = list(self.quotes.get(tk, ()))
                hit = next((x for x in q if x[0] > t0 and mid(x) is not None and sign * (mid(x) - kb) >= need), None)
                if hit:
                    e["react_secs"] = f"{hit[0] - t0:.2f}"
            for s in FOLLOW:
                key = f"kalshi_{s}s"
                if not e.get(key) and t - t0 >= s:
                    x = self.quote_at(tk, t0 + s)
                    e[key] = f"{mid(x):.4f}" if mid(x) is not None else ""
            done = (t - t0 >= max(FOLLOW) + 1 and entry_state == "done" and (not traded or exits_done))
            if done:
                e["status"] = "awaiting result"   # record the outcome for every event, traded or not
            else:
                keep.append(e)
        self.pending = keep

    # ---- saving ----
    def save(self):
        with self.lock:
            rows = [dict(e) for e in self.events]
        write_csv(EVENTS, rows, FIELDS)
        rtt = statistics.median(self.rtts) if self.rtts else None
        brtt = statistics.median(self.book_rtts) if self.book_rtts else None
        cb = statistics.median(self.feeds.delays) if self.feeds and self.feeds.delays else None
        with open(STATUS, "w") as fh:
            json.dump({"saved_at": iso(datetime.now(timezone.utc)), "windows_watched": len(self.markets),
                       "events": len(rows),
                       "trades": sum(1 for e in rows if e.get("traded") == "yes"),
                       "kalshi_poll_rtt_s": round(rtt, 3) if rtt else None,
                       "book_rtt_s": round(brtt, 3) if brtt else None,
                       "coinbase_delay_s": round(cb, 3) if cb is not None else None,
                       "ws_messages": self.feeds.msgs if self.feeds else {},
                       "errors": self.errors[-20:]}, fh, indent=1)
        write_page(rows, rtt, cb, brtt)
        subprocess.run(["git", "add", "lag", "LAG.md"], cwd=HERE, capture_output=True)
        if subprocess.run(["git", "commit", "-q", "-m", "lag tracker update"], cwd=HERE,
                          capture_output=True).returncode != 0:
            return
        for _ in range(3):
            # This bot is the only writer of lag/ and LAG.md, so on a clash keep our copy.
            if subprocess.run(["git", "pull", "-q", "--rebase", "-X", "theirs"], cwd=HERE,
                              capture_output=True).returncode != 0:
                subprocess.run(["git", "rebase", "--abort"], cwd=HERE, capture_output=True)
            if subprocess.run(["git", "push", "-q"], cwd=HERE, capture_output=True).returncode == 0:
                return
            time.sleep(3)


# ---------------- dashboard ----------------

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
        "ahead": (sum(1 for e in moved if e["already_moved"] == "yes") / len(moved)) if moved else None,
        "caught2": statistics.median(caught) if caught else None,
    }


def trade_stats(trades, key):
    """P&L for one exit rule. A timed exit with nobody to sell to falls back to the close."""
    pnls, risked = [], 0.0
    for t in trades:
        p = _f(t.get(key))
        if p is None:
            p = _f(t.get("pnl_close"))
        if p is None:
            continue
        pnls.append(p)
        risked += CONTRACTS * (float(t["ask"]) + float(t["fee"]))
    half = len(pnls) // 2
    return {"n": len(pnls), "won": sum(1 for p in pnls if p > 0), "pnl": sum(pnls),
            "ret": sum(pnls) / risked if risked else 0.0,
            "h1": sum(pnls[:half]), "h2": sum(pnls[half:])}


def first_per_window(trades):
    seen, out = set(), []
    for t in trades:
        if t["ticker"] not in seen:
            seen.add(t["ticker"])
            out.append(t)
    return out


def write_page(events, rtt=None, cb=None, brtt=None):
    seen = [e for e in events if e.get("kalshi_at_entry")]
    booked = [e for e in events if e.get("fill") == "book"]
    legacy = [e for e in events if e.get("fill") != "book" and e.get("traded") == "yes"]
    trades = [e for e in booked if e.get("traded") == "yes"]
    closed = [t for t in trades if _f(t.get("pnl_close")) is not None]
    allstats = summarize(seen)
    exits = {"Sell after 10 sec": "pnl10", "Sell after 30 sec": "pnl30", "Hold to the close": "pnl_close"}
    ts = {label: trade_stats(trades, key) for label, key in exits.items()}
    best_label, best = max(ts.items(), key=lambda kv: kv[1]["pnl"]) if closed else (None, None)

    checked = [e for e in booked if _f(e.get("book_best")) is not None]
    vs = [(_f(e["book_best"]) - _f(e["quote_ask"])) for e in checked if _f(e.get("quote_ask")) is not None]
    slip = [_f(e["ask"]) - _f(e["book_best"]) for e in checked if _f(e.get("ask")) is not None]
    skips = {}
    for e in booked:
        if e.get("skip"):
            skips[e["skip"]] = skips.get(e["skip"], 0) + 1
    worse = sum(1 for v in vs if v >= 0.02)

    if not best or best["n"] < 150:
        verdict = (f"🟡 **Testing with real order-book fills.** {len(closed)} of 150 settled trades needed "
                   "before calling it. The earlier results below used quoted prices, which may not have been "
                   "fillable.")
    elif best["pnl"] > 0 and best["h1"] > 0 and best["h2"] > 0:
        verdict = (f"🟢 **The gap is real and tradable.** Priced on the live order book, buying right after a "
                   f"jump made money in both halves of the data ({best_label.lower()}).")
    elif vs and worse / len(vs) >= 0.5:
        verdict = ("🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already "
                   "moved, so the earlier paper profits weren't fillable.")
    else:
        verdict = "🔴 **No profitable gap on real fills.** Kalshi sometimes lags, but not by enough after fees."

    def fmt(v, pct=False, secs=False):
        if v is None:
            return "—"
        if pct:
            return f"{abs(v) if abs(v) < 0.005 else v:.0%}"
        return f"{v:.1f}s" if secs else f"{v:.2f}"

    def money(v):
        return f"-${-v:,.2f}" if v < 0 else f"${v:,.2f}"

    lines = [
        "# Lag Tracker", "",
        f"*Updated {datetime.now(timezone.utc):%a %b %d %H:%M} UTC. Paper money. Coin prices arrive live from "
        "Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move "
        "shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 "
        "contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*", "",
        "[← Back to all bots](README.md)", "",
        "## Verdict", "", verdict, "",
        "## Paper trades on real order-book prices", "",
        "| Exit | Trades | Won | P&L | Return | Earlier / later half |",
        "|---|---|---|---|---|---|",
    ]
    for label, s in ts.items():
        lines.append(f"| {label} | {s['n']} | {s['won']} | {money(s['pnl'])} | {s['ret']:+.1%} | "
                     f"{money(s['h1'])} / {money(s['h2'])} |")
    strict = [t for t in trades if (_f(t.get("edge")) or 0) >= STRICT_EDGE]
    for label, group in ((f"Hold, only edge {STRICT_EDGE * 100:.0f}¢+", strict),
                         ("Hold, first trade per window only", first_per_window(trades))):
        s = trade_stats(group, "pnl_close")
        lines.append(f"| {label} | {s['n']} | {s['won']} | {money(s['pnl'])} | {s['ret']:+.1%} | "
                     f"{money(s['h1'])} / {money(s['h2'])} |")
    lines += ["", "*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only "
              "what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last "
              "two rows re-score the same trades with stricter rules, as a robustness check.*", ""]

    lines += ["## Was the quoted price real?", ""]
    if vs:
        lines += [
            "| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | "
            "Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |",
            "|---|---|---|---|---|---|",
            f"| {len(checked)} | {sum(1 for v in vs if abs(v) <= 0.01) / len(vs):.0%} | {worse / len(vs):.0%} | "
            f"{statistics.median(vs) * 100:+.1f}¢ | {(statistics.mean(slip) if slip else 0) * 100:.1f}¢ | "
            + (", ".join(f"{k} {v}" for k, v in sorted(skips.items(), key=lambda kv: -kv[1])) or "—") + " |",
            "", "*If the book usually matches the quote, the lag is real. If the book is usually worse, the "
            "\"lag\" was just a slow price display and the old paper profits weren't fillable.*", ""]
    else:
        lines += ["*Starts with the next run.*", ""]

    if legacy:
        s = trade_stats(legacy, "pnl_close")
        lines += ["## Before the order-book check (quoted prices)", "",
                  "| Exit | Trades | Won | P&L | Return |", "|---|---|---|---|---|",
                  f"| Hold to the close | {s['n']} | {s['won']} | {money(s['pnl'])} | {s['ret']:+.1%} |", "",
                  "*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*",
                  ""]

    lines += ["## How fast does Kalshi follow?", "",
              "| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | "
              "Share of the move Kalshi made within 2 sec |", "|---|---|---|---|---|"]
    for a in sorted({e["asset"] for e in seen}):
        s = summarize([e for e in seen if e["asset"] == a])
        lines.append(f"| {a} | {s['n']} | {fmt(s['react'], secs=True)} | {fmt(s['ahead'], pct=True)} | "
                     f"{fmt(s['caught2'], pct=True)} |")
    lines.append(f"| **All** | **{allstats['n']}** | **{fmt(allstats['react'], secs=True)}** | "
                 f"**{fmt(allstats['ahead'], pct=True)}** | **{fmt(allstats['caught2'], pct=True)}** |")
    lines += ["",
        "*\"Catches up\" = Kalshi's quoted price moved at least half as far as our fair value did. "
        "\"Already moved\" = that had happened by the first Kalshi price we saw after the jump. "
        "Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*", ""]
    if rtt is not None or cb is not None or brtt is not None:
        part = []
        if rtt is not None:
            part.append(f"Kalshi quote check: **{rtt * 1000:.0f} ms**")
        if brtt is not None:
            part.append(f"Order book check: **{brtt * 1000:.0f} ms**")
        if cb is not None:
            part.append(f"Coinbase price delay: **{cb * 1000:.0f} ms**")
        lines += ["## Feed speed", "", " · ".join(part), ""]
    lines += ["## Latest events", "",
              "| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |",
              "|---|---|---|---|---|---|---|---|"]
    for e in seen[-30:][::-1]:
        trade = (f"{'UP' if e['side'] == 'yes' else 'DOWN'} @ {float(e['ask']):.2f}"
                 if e.get("traded") == "yes" else (e.get("skip") or "—"))
        pnl = " / ".join(e.get(k) or "·" for k in ("pnl10", "pnl30", "pnl_close")) if e.get("traded") == "yes" else ""
        qb = (f"{float(e['quote_ask']):.2f} → {float(e['book_best']):.2f}"
              if _f(e.get("quote_ask")) is not None and _f(e.get("book_best")) is not None else "—")
        lines.append(f"| {e['time'][5:19].replace('T', ' ')} | {e['asset']} | {e['direction']} | "
                     f"{float(e['fair_before']):.2f}→{float(e['fair_after']):.2f} | {qb} | "
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
            bot.err(str(exc))
            print("error:", exc)
        if now_ts() - last_save > SAVE_MINUTES * 60:
            try:
                bot.save()
            except Exception as exc:
                bot.err(f"save: {exc}")
            last_save = now_ts()
        time.sleep(max(0.01, TICK - (now_ts() - start)))
    # stop opening new trades; let open ones finish their timed exits
    deadline = now_ts() + max(FOLLOW) + max(EXITS) + 10
    while bot.pending and now_ts() < deadline:
        bot.follow()
        time.sleep(0.5)
    bot.pool.shutdown(wait=True)
    bot.follow()
    bot.settle()
    bot.save()


if __name__ == "__main__":
    sys.exit(main())
