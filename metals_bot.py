"""Fair-value bot for Kalshi's 15-minute GOLD and SILVER up/down markets (paper money).

Kalshi settles these on Pyth's metal index: UP wins if the 1-minute close at
the end of the window is at least the 1-minute close at the start (the
market's floor_strike). Pyth's live feed now needs a paid key, so we price
from Hyperliquid's gold/silver markets instead and only use *moves*:

    fair chance of UP = P( price at close / price at window start >= 1 )

so any constant gap between Hyperliquid and Pyth cancels out. We also log
the "direct" reading (Hyperliquid price vs Kalshi's strike) to see which
one predicts better.

Every ~2 seconds: if either side's real order-book price is at least EDGE
below fair value after Kalshi's fee, paper-buy CONTRACTS and hold to the
close (one trade per market per window). Every 30 seconds the model and
Kalshi's price are logged for every market ("shadow log") so other edge
thresholds can be replayed later.

Files (under metals/): trades.csv, obs/<date>.csv, results.csv, status.json
"""
import json
import math
import os
import subprocess
import sys
import time
from collections import deque
from datetime import datetime, timedelta, timezone

import requests

from common import HERE, fee_per_contract, get_markets, kalshi_get, price
from fifteen_bot import append_csv, iso, norm_cdf, parse_ts, write_csv
from fv_bot import book_fill, load

DIR = os.path.join(HERE, "metals")
TRADES = os.path.join(DIR, "trades.csv")
RESULTS = os.path.join(DIR, "results.csv")

SERIES = {"KXSILVER15M": "SILVER", "KXGOLD15M": "GOLD"}
HL = "https://api.hyperliquid.xyz/info"
HL_DEX = "xyz"                          # Hyperliquid's builder dex with metals
PAXG = "https://api.exchange.coinbase.com/products/PAXG-USD/ticker"   # gold backup

CONTRACTS = 10
EDGE = 0.04
MIN_PRICE, MAX_PRICE = 0.05, 0.95
MIN_SECS, MAX_SECS = 30, 840
BASIS_SD = 0.00012        # Hyperliquid move vs Pyth move over one window (log units)
VOL_MULT = 1.25           # widen volatility: metals jump on news more than a normal curve says
SIGMA_FLOOR = 0.00005     # per-minute volatility floor (0.005%)
STALE_SECONDS = 20
POLL_SECONDS = 2
OBS_SECONDS = 30
SAVE_MINUTES = 10
RUN_MINUTES = float(os.environ.get("RUN_MINUTES", "330"))

TRADE_FIELDS = ["time", "ticker", "asset", "side", "secs_left", "feed", "feed_start", "strike",
                "move_pct", "sigma_pct", "model_p", "model_direct", "price", "best_price",
                "fee", "edge", "contracts", "depth", "status", "result", "pnl"]
OBS_FIELDS = ["time", "ticker", "asset", "secs_left", "feed", "feed_start", "strike",
              "sigma_pct", "model_up", "model_direct", "yes_bid", "yes_ask", "source"]
RESULT_FIELDS = ["ticker", "result", "close_time"]


def now_utc():
    return datetime.now(timezone.utc)


def hl_post(body):
    r = requests.post(HL, json=body, timeout=5)
    r.raise_for_status()
    return r.json()


def fair_up(log_move, secs_left, sigma):
    """Chance the settlement price ends at or above the start price, given the
    move so far (log units) and per-minute volatility."""
    tau = max(secs_left, 0.5) / 60
    var = (sigma * VOL_MULT) ** 2 * tau + BASIS_SD ** 2
    return min(max(norm_cdf(log_move / math.sqrt(var)), 0.001), 0.999)


class Metals:
    def __init__(self):
        self.trades = load(TRADES)
        self.traded = {t["ticker"] for t in self.trades}
        self.results = {r["ticker"]: r for r in load(RESULTS)}
        self.coins = {}           # asset -> Hyperliquid coin name
        self.markets = {}         # ticker -> meta
        self.samples = {a: deque(maxlen=900) for a in SERIES.values()}   # (time, price)
        self.last = {}            # asset -> (time, price, source)
        self.sigma = {}           # asset -> (fetched_at, sigma)
        self.anchor = {}          # (asset, window start iso) -> price
        self.obs, self.last_obs = [], {}
        self.errors = []
        self.last_refresh = 0.0
        self.last_coins = 0.0
        self.accept_new = True
        self.seen = {}            # ticker -> close time, for every market we watched

    # ---------- prices ----------
    def find_coins(self):
        try:
            mids = hl_post({"type": "allMids", "dex": HL_DEX})
            for a in SERIES.values():
                hits = [k for k in mids if k.upper().split(":")[-1] == a]
                if hits:
                    self.coins[a] = hits[0]
        except Exception as exc:
            self.errors.append(f"{iso(now_utc())} hl coins: {exc}")
        self.last_coins = time.time()

    def spots(self):
        t = time.time()
        if self.coins:
            try:
                mids = hl_post({"type": "allMids", "dex": HL_DEX})
                for a, c in self.coins.items():
                    if c in mids:
                        p = float(mids[c])
                        self.last[a] = (t, p, "hyperliquid")
                        self.samples[a].append((t, p))
            except Exception as exc:
                self.errors.append(f"{iso(now_utc())} hl mids: {exc}")
        if "GOLD" not in self.coins or t - self.last.get("GOLD", (0,))[0] > STALE_SECONDS:
            try:
                p = float(requests.get(PAXG, timeout=5).json()["price"])
                if self.last.get("GOLD", (0, 0, ""))[2] == "hyperliquid":
                    self.samples["GOLD"].clear()      # never mix two feeds in one series
                self.last["GOLD"] = (t, p, "paxg")
                self.samples["GOLD"].append((t, p))
            except Exception as exc:
                self.errors.append(f"{iso(now_utc())} paxg: {exc}")

    def candles(self, asset, start_ms, end_ms):
        coin = self.coins.get(asset)
        if not coin or self.last.get(asset, (0, 0, ""))[2] != "hyperliquid":
            return []
        try:
            return hl_post({"type": "candleSnapshot",
                            "req": {"coin": coin, "interval": "1m", "startTime": start_ms, "endTime": end_ms}})
        except Exception as exc:
            self.errors.append(f"{iso(now_utc())} hl candles {asset}: {exc}")
            return []

    def vol(self, asset):
        hit = self.sigma.get(asset)
        if hit and time.time() - hit[0] < 120:
            return hit[1]
        end = int(time.time() * 1000)
        closes = [float(c["c"]) for c in self.candles(asset, end - 65 * 60_000, end)]
        if len(closes) < 10:
            # Fall back to our own samples, one per minute.
            s, closes, nxt = list(self.samples[asset]), [], 0
            for ts, p in s:
                if ts >= nxt:
                    closes.append(p)
                    nxt = ts + 60
        rets = [math.log(b / a) for a, b in zip(closes, closes[1:]) if a > 0 and b > 0]
        if len(rets) < 5:
            return None
        sig = max(math.sqrt(sum(r * r for r in rets) / len(rets)), SIGMA_FLOOR)
        self.sigma[asset] = (time.time(), sig)
        return sig

    def start_price(self, asset, start):
        """Our feed's price at the window start (close of the minute ending then)."""
        key = (asset, iso(start))
        if key in self.anchor:
            return self.anchor[key]
        ts = start.timestamp()
        near = [(abs(t - ts), p) for t, p in self.samples[asset] if abs(t - ts) <= 5]
        if near:
            p = min(near)[1]
        else:
            ms = int(ts * 1000)
            got = [c for c in self.candles(asset, ms - 120_000, ms) if int(c["t"]) == ms - 60_000]
            if not got:
                return None
            p = float(got[0]["c"])
        self.anchor[key] = p
        return p

    # ---------- markets ----------
    def refresh(self):
        found = {}
        for st, a in SERIES.items():
            try:
                for m in get_markets(max_pages=2, series_ticker=st, status="open"):
                    if m.get("floor_strike") in (None, ""):
                        continue
                    close = parse_ts(m["close_time"])
                    found[m["ticker"]] = {"asset": a, "strike": float(m["floor_strike"]), "close": close,
                                          "start": close - timedelta(minutes=15), "m": m}
            except Exception as exc:
                self.errors.append(f"{iso(now_utc())} markets {st}: {exc}")
        self.markets = found
        for t, meta in found.items():
            self.seen.setdefault(t, meta["close"])
        self.last_refresh = time.time()

    def quote(self, ticker):
        try:
            return kalshi_get(f"/markets/{ticker}")["market"]
        except Exception:
            return self.markets[ticker]["m"]

    def poll(self):
        if time.time() - self.last_coins > 1800:
            self.find_coins()
        self.spots()
        now = now_utc()
        for ticker, meta in list(self.markets.items()):
            a = meta["asset"]
            secs = (meta["close"] - now).total_seconds()
            if secs <= 0 or now < meta["start"] or a not in self.last:
                continue
            t_last, spot, source = self.last[a]
            if time.time() - t_last > STALE_SECONDS:
                continue
            start_p = self.start_price(a, meta["start"])
            sigma = self.vol(a)
            if not start_p or not sigma:
                continue
            p_up = fair_up(math.log(spot / start_p), secs, sigma)
            p_direct = fair_up(math.log(spot / meta["strike"]), secs, sigma)

            want_obs = time.time() - self.last_obs.get(ticker, 0) >= OBS_SECONDS
            could_trade = (self.accept_new and ticker not in self.traded and MIN_SECS <= secs <= MAX_SECS)
            if not (want_obs or could_trade):
                continue
            m = self.quote(ticker)
            ybid, yask = price(m, "yes_bid"), price(m, "yes_ask")
            if want_obs:
                self.obs.append({"time": iso(now), "ticker": ticker, "asset": a, "secs_left": round(secs),
                                 "feed": spot, "feed_start": start_p, "strike": meta["strike"],
                                 "sigma_pct": round(sigma * 100, 5), "model_up": round(p_up, 4),
                                 "model_direct": round(p_direct, 4), "yes_bid": ybid, "yes_ask": yask,
                                 "source": source})
                self.last_obs[ticker] = time.time()
            if not could_trade:
                continue
            for side, p_side, ask in (("yes", p_up, yask), ("no", 1 - p_up, price(m, "no_ask"))):
                if ask is None or not (MIN_PRICE <= ask <= MAX_PRICE):
                    continue
                if p_side - ask - fee_per_contract(ask, CONTRACTS) < EDGE:
                    continue
                fill = book_fill(ticker, side, CONTRACTS)     # real order-book price
                if not fill:
                    continue
                avg, best, depth = fill
                fee = fee_per_contract(avg, CONTRACTS)
                edge = p_side - avg - fee
                if edge < EDGE or not (MIN_PRICE <= avg <= MAX_PRICE):
                    continue
                self.trades.append({
                    "time": iso(now), "ticker": ticker, "asset": a, "side": side, "secs_left": round(secs),
                    "feed": spot, "feed_start": start_p, "strike": meta["strike"],
                    "move_pct": round(math.log(spot / start_p) * 100, 4), "sigma_pct": round(sigma * 100, 5),
                    "model_p": round(p_side, 4),
                    "model_direct": round(p_direct if side == "yes" else 1 - p_direct, 4),
                    "price": avg, "best_price": best, "fee": round(fee, 4), "edge": round(edge, 4),
                    "contracts": CONTRACTS, "depth": round(depth), "status": "open", "result": "", "pnl": ""})
                self.traded.add(ticker)
                print(f"{iso(now)} BUY {ticker} {side.upper()} @ {avg:.2f} model {p_side:.0%} edge {edge*100:.1f}c")
                break

    def settle(self):
        now = now_utc()
        pending = {t["ticker"] for t in self.trades if t["status"] == "open"} | set(self.seen)
        for ticker in pending - set(self.results):
            close = self.seen.get(ticker)
            if close and now < close + timedelta(seconds=30):
                continue
            try:
                m = kalshi_get(f"/markets/{ticker}")["market"]
            except Exception as exc:
                self.errors.append(f"{iso(now)} settle {ticker}: {exc}")
                continue
            if m.get("result") in ("yes", "no"):
                self.results[ticker] = {"ticker": ticker, "result": m["result"], "close_time": m.get("close_time", "")}
                self.seen.pop(ticker, None)
            time.sleep(0.1)
        for t in self.trades:
            r = self.results.get(t["ticker"])
            if t["status"] == "open" and r:
                n = int(t["contracts"])
                cost = n * (float(t["price"]) + float(t["fee"]))
                payout = n if r["result"] == t["side"] else 0
                t.update(status="settled", result=r["result"], pnl=f"{payout - cost:.2f}")

    def save(self):
        by_day = {}
        for o in self.obs:
            by_day.setdefault(o["time"][:10], []).append(o)
        for day, rows in by_day.items():
            append_csv(os.path.join(DIR, "obs", f"{day}.csv"), rows, OBS_FIELDS)
        self.obs = []
        write_csv(TRADES, self.trades, TRADE_FIELDS)
        write_csv(RESULTS, list(self.results.values()), RESULT_FIELDS)
        with open(os.path.join(DIR, "status.json"), "w") as fh:
            json.dump({"saved_at": iso(now_utc()), "coins": self.coins,
                       "feeds": {a: {"source": s, "price": p, "age_s": round(time.time() - t)}
                                 for a, (t, p, s) in self.last.items()},
                       "markets": len(self.markets), "trades": len(self.trades),
                       "open": sum(1 for t in self.trades if t["status"] == "open"),
                       "results_known": len(self.results),
                       "sigma_pct": {a: round(s * 100, 5) for a, (_, s) in self.sigma.items()},
                       "errors": self.errors[-15:]}, fh, indent=1)


def git_save():
    subprocess.run([sys.executable, "metals_dashboard.py"], cwd=HERE, capture_output=True)
    subprocess.run(["git", "add", "metals", "METALS.md"], cwd=HERE, capture_output=True)
    if subprocess.run(["git", "commit", "-q", "-m", "metals update"], cwd=HERE,
                      capture_output=True).returncode != 0:
        return
    for _ in range(3):
        if subprocess.run(["git", "pull", "-q", "--rebase", "-X", "theirs"], cwd=HERE,
                          capture_output=True).returncode != 0:
            subprocess.run(["git", "rebase", "--abort"], cwd=HERE, capture_output=True)
        if subprocess.run(["git", "push", "-q"], cwd=HERE, capture_output=True).returncode == 0:
            return
        time.sleep(3)


def main():
    os.makedirs(os.path.join(DIR, "obs"), exist_ok=True)
    mb = Metals()
    mb.find_coins()
    print(f"metals: Hyperliquid coins {mb.coins}")
    end = time.time() + RUN_MINUTES * 60
    last_save, last_settle, first_save = time.time(), 0.0, True
    while time.time() < end:
        start = time.time()
        try:
            n = now_utc()
            if time.time() - mb.last_refresh > 60 or (n.minute % 15 == 0 and n.second < 10
                                                       and time.time() - mb.last_refresh > 8):
                mb.refresh()
            mb.poll()
            if time.time() - last_settle > 30:
                mb.settle()
                last_settle = time.time()
        except Exception as exc:
            print(f"loop error: {exc}")
            mb.errors.append(f"{iso(now_utc())} loop: {exc}")
        # First save after 3 minutes so a broken feed shows up fast.
        if time.time() - last_save >= (180 if first_save else SAVE_MINUTES * 60):
            mb.save()
            git_save()
            last_save, first_save = time.time(), False
        time.sleep(max(0.2, POLL_SECONDS - (time.time() - start)))
    mb.accept_new = False
    deadline = time.time() + 20 * 60
    while (any(t["status"] == "open" for t in mb.trades) or mb.seen) and time.time() < deadline:
        try:
            mb.settle()
        except Exception as exc:
            print(f"wind-down error: {exc}")
        time.sleep(20)
    mb.save()
    print(f"metals: {len(mb.trades)} trades")
    return 0


if __name__ == "__main__":
    sys.exit(main())
