"""15-minute 1-cent study.

Watches every Kalshi 15-minute up/down market (crypto, FX, commodities,
indices). The moment either side (UP = YES or DOWN = NO) can be bought
for 1 cent it logs a paper buy of 14 contracts, then records that side's
bid and ask every ~2 seconds until the 15-minute window closes.

After each window it downloads Kalshi's trade records for the market to
measure how fast we spotted the 1-cent price and how much traded there.

Files (all under fifteen/):
  bets.csv            one row per bet with every metric
  snaps/<date>.csv    our ~2-second bid/ask snapshots for open bets
  ticks/<date>.csv    every Kalshi trade in the market from 1 min before
                      our buy to the close
  status.json         health info for the dashboard
"""
import csv
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone

import requests

from common import HERE, fee_per_contract, get_markets, kalshi_get, price

DIR = os.path.join(HERE, "fifteen")
BETS_FILE = os.path.join(DIR, "bets.csv")
ENTRY = 0.01
CONTRACTS = 14
POLL_SECONDS = 2
REFRESH_SECONDS = 60
SAVE_MINUTES = 10
RUN_MINUTES = float(os.environ.get("RUN_MINUTES", "350"))
TARGETS = [2, 3, 5, 10, 25, 50]
SKIP = ("TEST", "CRYPTOLEAD", "CRYPTOCOMP")   # not up/down markets

# Spot prices for crypto come from Coinbase (close to Kalshi's CF Benchmarks index).
COINBASE = "https://api.exchange.coinbase.com/products/{}-USD/ticker"

BET_FIELDS = [
    "detected_at", "series", "asset", "category", "ticker", "side", "window_close",
    "secs_left", "strike", "spot", "gap_pct", "entry_price", "contracts", "entry_fee",
    "status", "result", "pnl_hold", "peak_bid", "peak_at_s",
    *[f"s_to_{t}c" for t in TARGETS], "bid_at_close", "snapshots",
    "first_1c_trade_at", "detect_lag_s", "contracts_at_1c_after", "trades_in_window",
]
SNAP_FIELDS = ["time", "ticker", "side", "secs_left", "bid", "ask"]
TICK_FIELDS = ["time", "ticker", "yes_price", "contracts", "taker"]


def now_utc():
    return datetime.now(timezone.utc)


def iso(dt, ms=False):
    if not dt:
        return ""
    return dt.isoformat(timespec="milliseconds" if ms else "seconds")


def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00")) if s else None


def append_csv(path, rows, fields):
    if not rows:
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    new = not os.path.exists(path)
    with open(path, "a", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        if new:
            w.writeheader()
        w.writerows(rows)


def write_csv(path, rows, fields):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def load_bets():
    if not os.path.exists(BETS_FILE):
        return []
    with open(BETS_FILE, newline="") as fh:
        return list(csv.DictReader(fh))


def git_save():
    subprocess.run(["git", "add", "fifteen"], cwd=HERE, capture_output=True)
    if subprocess.run(["git", "commit", "-q", "-m", "15-min study update"],
                      cwd=HERE, capture_output=True).returncode != 0:
        return
    for _ in range(3):
        subprocess.run(["git", "pull", "-q", "--rebase"], cwd=HERE, capture_output=True)
        if subprocess.run(["git", "push", "-q"], cwd=HERE, capture_output=True).returncode == 0:
            return
        time.sleep(3)


def asset_of(series):
    return series.removeprefix("KX").removesuffix("15M")


def side_quote(m, side):
    """(bid, ask) in dollars for the side we hold."""
    if side == "yes":
        return price(m, "yes_bid"), price(m, "yes_ask")
    return price(m, "no_bid"), price(m, "no_ask")


class Fifteen:
    def __init__(self):
        self.bets = load_bets()
        self.held = {(b["ticker"], b["side"]) for b in self.bets}
        self.series = {}          # ticker -> (title, category)
        self.markets = {}         # ticker -> market meta for the current windows
        self.last_series = 0.0
        self.last_refresh = 0.0
        self.snaps = []           # buffered snapshot rows
        self.path = {}            # (ticker, side) -> list of (secs_after_entry, bid)
        self.errors = []
        self.spot_ok = {}
        self.batch_ok = True
        self.accept_new = True

    # ---------------------------------------------------------- discovery
    def load_series(self):
        data = kalshi_get("/series", {})
        found = {}
        for s in data.get("series", []):
            t = s["ticker"]
            if (s.get("frequency") == "fifteen_min" or t.endswith("15M")) and not any(k in t for k in SKIP):
                found[t] = (s.get("title", t), s.get("category", ""))
        self.series = found
        self.last_series = time.time()
        print(f"{len(found)} fifteen-minute series")

    def refresh(self):
        markets = {}
        for st in self.series:
            try:
                for m in get_markets(max_pages=1, series_ticker=st, status="open"):
                    if m.get("strike_type") not in ("greater_or_equal", "greater", "less", "less_or_equal"):
                        continue
                    markets[m["ticker"]] = {"series": st, "close": parse_ts(m.get("close_time")),
                                            "open": parse_ts(m.get("open_time")),
                                            "strike": m.get("floor_strike") or m.get("cap_strike")}
            except Exception as exc:
                self.errors.append(f"{iso(now_utc())} refresh {st}: {exc}")
            time.sleep(0.05)
        self.markets = markets
        self.last_refresh = time.time()

    def quotes(self):
        tickers = [t for t, m in self.markets.items() if m["close"] and m["close"] > now_utc()]
        out = {}
        if self.batch_ok:
            try:
                for i in range(0, len(tickers), 50):
                    data = kalshi_get("/markets", {"tickers": ",".join(tickers[i:i + 50]), "limit": 1000})
                    out.update({m["ticker"]: m for m in data.get("markets", [])})
                if tickers and not out:
                    raise ValueError("batch lookup returned nothing")
                return out
            except Exception as exc:
                self.errors.append(f"{iso(now_utc())} batch off: {exc}")
                self.batch_ok = False
        for st in {self.markets[t]["series"] for t in tickers}:
            try:
                for m in get_markets(max_pages=1, series_ticker=st, status="open"):
                    out[m["ticker"]] = m
            except Exception as exc:
                self.errors.append(f"{iso(now_utc())} quotes {st}: {exc}")
        return out

    def spot(self, asset):
        if self.spot_ok.get(asset) is False:
            return None
        try:
            r = requests.get(COINBASE.format(asset), timeout=3)
            if r.status_code != 200:
                self.spot_ok[asset] = False
                return None
            self.spot_ok[asset] = True
            return float(r.json()["price"])
        except Exception:
            return None

    # ---------------------------------------------------------- main loop
    def poll(self):
        now = now_utc()
        q = self.quotes()
        stamp = iso(now, ms=True)
        for ticker, m in q.items():
            meta = self.markets.get(ticker)
            if not meta or m.get("status") not in ("active", "open"):
                continue
            secs_left = (meta["close"] - now).total_seconds()
            if secs_left <= 0:
                continue
            for side in ("yes", "no"):
                bid, ask = side_quote(m, side)
                key = (ticker, side)
                if key in self.held:
                    if key in self.path:
                        t0 = self.path[key][0]
                        self.path[key][1].append(((now - t0).total_seconds(), bid or 0.0))
                        self.snaps.append({"time": stamp, "ticker": ticker, "side": side,
                                           "secs_left": f"{secs_left:.1f}",
                                           "bid": f"{bid or 0:.2f}", "ask": f"{ask or 0:.2f}"})
                    continue
                if not self.accept_new or ask is None or not (0 < ask <= ENTRY):
                    continue
                st = meta["series"]
                title, cat = self.series.get(st, (st, ""))
                strike = meta["strike"]
                spot = self.spot(asset_of(st)) if cat == "Crypto" else None
                gap = ((spot - strike) / strike * 100) if spot and strike else None
                fee = fee_per_contract(ask, CONTRACTS) * CONTRACTS
                bet = {"detected_at": stamp, "series": st, "asset": asset_of(st), "category": cat,
                       "ticker": ticker, "side": side, "window_close": iso(meta["close"]),
                       "secs_left": f"{secs_left:.0f}", "strike": strike or "",
                       "spot": f"{spot:g}" if spot else "", "gap_pct": f"{gap:.4f}" if gap is not None else "",
                       "entry_price": f"{ask:.2f}", "contracts": CONTRACTS, "entry_fee": f"{fee:.2f}",
                       "status": "open"}
                self.bets.append(bet)
                self.held.add(key)
                self.path[key] = (now, [(0.0, bid or 0.0)])
                self.snaps.append({"time": stamp, "ticker": ticker, "side": side,
                                   "secs_left": f"{secs_left:.1f}", "bid": f"{bid or 0:.2f}",
                                   "ask": f"{ask:.2f}"})
                print(f"BUY {CONTRACTS} {'UP' if side == 'yes' else 'DOWN'} {ticker} @ {ask:.2f} "
                      f"with {secs_left:.0f}s left" + (f", gap {gap:+.3f}%" if gap is not None else ""))

    def close_out(self):
        """Once a window has closed: lock in the price-path metrics, pull Kalshi's
        trade tape, and settle when Kalshi posts the result."""
        now = now_utc()
        for b in self.bets:
            key = (b["ticker"], b["side"])
            close = parse_ts(b["window_close"])
            if b["status"] == "open" and close and now > close + timedelta(seconds=5):
                if key not in self.path:
                    # bought in an earlier run that ended before the window closed
                    b.update(status="closed", snapshots=0)
                    continue
                path = self.path.pop(key, (None, []))[1]
                if path:
                    peak = max(bid for _, bid in path)
                    peak_at = next(s for s, bid in path if bid == peak)
                    b.update(peak_bid=f"{peak:.2f}", peak_at_s=f"{peak_at:.0f}",
                             bid_at_close=f"{path[-1][1]:.2f}", snapshots=len(path))
                    for t in TARGETS:
                        hit = next((s for s, bid in path if s > 0 and bid >= t / 100 - 1e-9), None)
                        b[f"s_to_{t}c"] = f"{hit:.0f}" if hit is not None else ""
                else:
                    b.update(snapshots=0)
                b["status"] = "closed"
                try:
                    self.tape(b)
                except Exception as exc:
                    self.errors.append(f"{iso(now)} tape {b['ticker']}: {exc}")
            if b["status"] == "closed":
                if b.get("_checked") and time.time() - b["_checked"] < 60:
                    continue
                b["_checked"] = time.time()
                try:
                    m = kalshi_get(f"/markets/{b['ticker']}")["market"]
                except Exception as exc:
                    self.errors.append(f"{iso(now)} settle {b['ticker']}: {exc}")
                    continue
                res = m.get("result")
                if res not in ("yes", "no", "void"):
                    continue
                n = int(b["contracts"])
                cost = float(b["entry_price"]) * n + float(b["entry_fee"])
                payout = n * float(b["entry_price"]) if res == "void" else (n if res == b["side"] else 0)
                b.update(status="settled", result=res, pnl_hold=f"{payout - cost:.2f}")
                won = "WON" if res == b["side"] else "lost"
                print(f"SETTLED {b['ticker']} {b['side']}: {won}")

    def tape(self, b):
        det = parse_ts(b["detected_at"])
        close = parse_ts(b["window_close"])
        trades, cursor = [], None
        for _ in range(20):
            qp = {"ticker": b["ticker"], "limit": 1000,
                  "min_ts": int((det - timedelta(minutes=1)).timestamp()),
                  "max_ts": int(close.timestamp()) + 5}
            if cursor:
                qp["cursor"] = cursor
            data = kalshi_get("/markets/trades", qp)
            trades += data.get("trades", [])
            cursor = data.get("cursor")
            if not cursor:
                break
        trades.sort(key=lambda t: t["created_time"])

        def side_price(t):
            y = float(t.get("yes_price_dollars") or 0)
            return y if b["side"] == "yes" else 1 - y

        cheap = [t for t in trades if side_price(t) <= ENTRY + 1e-9]
        first = next((t for t in cheap if parse_ts(t["created_time"]) <= det + timedelta(seconds=5)), None)
        after = [t for t in cheap if parse_ts(t["created_time"]) >= det]
        b.update(first_1c_trade_at=first["created_time"] if first else "",
                 detect_lag_s=f"{(det - parse_ts(first['created_time'])).total_seconds():.1f}" if first else "",
                 contracts_at_1c_after=f"{sum(float(t.get('count_fp') or t.get('count') or 0) for t in after):.0f}",
                 trades_in_window=len(trades))
        day = det.strftime("%Y-%m-%d")
        append_csv(os.path.join(DIR, "ticks", f"{day}.csv"),
                   [{"time": t["created_time"], "ticker": b["ticker"],
                     "yes_price": t.get("yes_price_dollars"),
                     "contracts": t.get("count_fp", t.get("count")), "taker": t.get("taker_side")}
                    for t in trades], TICK_FIELDS)

    def save(self):
        by_day = {}
        for r in self.snaps:
            by_day.setdefault(r["time"][:10], []).append(r)
        for day, rows in by_day.items():
            append_csv(os.path.join(DIR, "snaps", f"{day}.csv"), rows, SNAP_FIELDS)
        self.snaps = []
        write_csv(BETS_FILE, self.bets, BET_FIELDS)
        status = {"saved_at": iso(now_utc()), "series": len(self.series),
                  "markets_watched": len(self.markets), "batch_lookup": self.batch_ok,
                  "bets": len(self.bets),
                  "open": sum(1 for b in self.bets if b["status"] != "settled"),
                  "coinbase_spot": {k: v for k, v in self.spot_ok.items()},
                  "errors": self.errors[-15:]}
        with open(os.path.join(DIR, "status.json"), "w") as fh:
            json.dump(status, fh, indent=1)


def main():
    f = Fifteen()
    end = time.time() + RUN_MINUTES * 60
    last_save = time.time()
    while time.time() < end:
        loop_start = time.time()
        try:
            if time.time() - f.last_series > 3600:
                f.load_series()
            # Refresh the market list every minute and right after each quarter hour.
            n = now_utc()
            fresh_window = n.minute % 15 == 0 and n.second < 10 and time.time() - f.last_refresh > 8
            if time.time() - f.last_refresh > REFRESH_SECONDS or fresh_window:
                f.refresh()
            f.poll()
            f.close_out()
        except Exception as exc:
            print(f"loop error: {exc}")
            f.errors.append(f"{iso(now_utc())} loop: {exc}")
        if time.time() - last_save >= SAVE_MINUTES * 60:
            f.save()
            git_save()
            last_save = time.time()
        time.sleep(max(0.2, POLL_SECONDS - (time.time() - loop_start)))
    # finish: stop buying, keep tracking open bets until their windows close
    f.accept_new = False
    deadline = time.time() + 17 * 60
    while any(b["status"] == "open" for b in f.bets) and time.time() < deadline:
        try:
            f.poll()
            f.close_out()
        except Exception as exc:
            print(f"wind-down error: {exc}")
        time.sleep(POLL_SECONDS)
    f.close_out()
    f.save()
    print(f"15-min study: {len(f.bets)} bets")
    return 0


if __name__ == "__main__":
    sys.exit(main())
