"""Fair-value bot for Kalshi's 15-minute crypto up/down markets (paper money).

Every ~2 seconds, for each market with a Coinbase price feed:
  1. Fair chance of UP = random-walk model using the live Coinbase price,
     the window's target price, time left and recent volatility, with
     Kalshi's 60-second settlement average handled exactly in the final
     minute (we average our own price samples, like Kalshi's index does).
  2. If either side's ask is at least EDGE cheaper than that fair chance
     after Kalshi's fee, paper-buy CONTRACTS of it and hold to the close.

It also logs the model next to the market every 30 seconds for every
market ("shadow log"), so we can check whether the model beats the
market even when it isn't trading.

Files (under fv/): trades.csv, obs/<date>.csv, results.csv, status.json
"""
import csv
import json
import math
import os
import statistics
import subprocess
import sys
import time
from collections import deque
from datetime import datetime, timedelta, timezone

import requests

from common import HERE, fee_per_contract, get_markets, kalshi_get, price
from fifteen_bot import append_csv, asset_of, iso, norm_cdf, parse_ts, side_quote, write_csv

DIR = os.path.join(HERE, "fv")
TRADES = os.path.join(DIR, "trades.csv")
RESULTS = os.path.join(DIR, "results.csv")

CONTRACTS = 10
EDGE = 0.04               # model chance must beat ask + fee by 4 cents
MIN_PRICE, MAX_PRICE = 0.05, 0.95
MIN_SECS, MAX_SECS = 30, 840
BASIS_SD = 0.00015        # Coinbase vs Kalshi's CF Benchmarks index (log units)
SIGMA_FLOOR = 0.0002      # per-minute volatility floor (0.02%)
POLL_SECONDS = 2
OBS_SECONDS = 30
SAVE_MINUTES = 10
RUN_MINUTES = float(os.environ.get("RUN_MINUTES", "330"))

SPOT = "https://api.exchange.coinbase.com/products/{}-USD/ticker"
CANDLES = "https://api.exchange.coinbase.com/products/{}-USD/candles"

TRADE_FIELDS = ["time", "ticker", "asset", "side", "secs_left", "spot", "strike", "gap_pct",
                "sigma_pct", "model_p", "price", "fee", "edge", "contracts", "status", "result",
                "pnl", "mid_at_60s", "clv", "depth_at_ask"]
OBS_FIELDS = ["time", "ticker", "asset", "secs_left", "spot", "strike", "sigma_pct",
              "model_up", "yes_bid", "yes_ask"]
RESULT_FIELDS = ["ticker", "result", "close_time"]


def now_utc():
    return datetime.now(timezone.utc)


def load(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="") as fh:
        return list(csv.DictReader(fh))


def fair_up(spot, strike, secs_left, sigma, window_samples):
    """Chance the settlement average ends at or above the strike."""
    tau = max(secs_left, 0.5) / 60                      # minutes
    if tau >= 1:
        var = sigma ** 2 * (tau - 2 / 3) + BASIS_SD ** 2
        x = math.log(spot / strike)
    else:
        # Inside the final minute: part of the average is already known.
        known = statistics.fmean(window_samples) if window_samples else spot
        elapsed = 1 - tau
        expected = elapsed * known + tau * spot
        var = sigma ** 2 * tau ** 3 / 3 + BASIS_SD ** 2
        x = math.log(expected / strike)
    return min(max(norm_cdf(x / math.sqrt(var)), 0.001), 0.999)


def git_save():
    """Commit this bot's data and rebuild its own dashboard page (files no
    other bot writes, so parallel runs never conflict)."""
    subprocess.run([sys.executable, "fv_dashboard.py"], cwd=HERE, capture_output=True)
    subprocess.run(["git", "add", "fv", 'FAIRVALUE.md', 'fv/charts'], cwd=HERE, capture_output=True)
    if subprocess.run(["git", "commit", "-q", "-m", "fv update"],
                      cwd=HERE, capture_output=True).returncode != 0:
        return
    for _ in range(3):
        # This bot is the only writer of its files, so on a clash keep our copy.
        if subprocess.run(["git", "pull", "-q", "--rebase", "-X", "theirs"], cwd=HERE,
                          capture_output=True).returncode != 0:
            subprocess.run(["git", "rebase", "--abort"], cwd=HERE, capture_output=True)
        if subprocess.run(["git", "push", "-q"], cwd=HERE, capture_output=True).returncode == 0:
            return
        time.sleep(3)

def depth_at_ask(ticker, side, ask):
    """Contracts actually available at or better than our price. Buying YES at
    `ask` means matching NO bids priced at 1-ask or higher (and vice versa)."""
    try:
        book = kalshi_get(f"/markets/{ticker}/orderbook").get("orderbook_fp") or {}
    except Exception:
        return None
    other = book.get("no_dollars" if side == "yes" else "yes_dollars") or []
    need = 1 - ask - 1e-9
    return sum(float(q) for p, q in other if float(p) >= need)


class FairValue:
    def __init__(self):
        self.trades = load(TRADES)
        self.traded = {t["ticker"] for t in self.trades}
        self.results = {r["ticker"]: r for r in load(RESULTS)}
        self.assets = {}          # series -> asset (with Coinbase feed)
        self.markets = {}         # ticker -> meta
        self.samples = {}         # asset -> deque of (time, price)
        self.sigma = {}           # asset -> (fetched_at, sigma)
        self.obs, self.errors = [], []
        self.last_obs = {}
        self.last_refresh = self.last_series = 0.0
        self.accept_new = True
        self.signals = 0
        self.seen = {}            # ticker -> close time, for everything in the shadow log

    def load_series(self):
        found = {}
        for s in kalshi_get("/series", {}).get("series", []):
            t = s["ticker"]
            if s.get("category") == "Crypto" and (s.get("frequency") == "fifteen_min" or t.endswith("15M")) \
                    and not any(k in t for k in ("TEST", "CRYPTOLEAD", "CRYPTOCOMP")):
                a = asset_of(t)
                try:
                    ok = requests.get(SPOT.format(a), timeout=4).status_code == 200
                except Exception:
                    ok = False
                if ok:
                    found[t] = a
        self.assets = found
        self.last_series = time.time()
        print(f"watching {len(found)} crypto series with Coinbase prices: {sorted(found.values())}")

    def refresh(self):
        markets = {}
        for st, a in self.assets.items():
            try:
                for m in get_markets(max_pages=1, series_ticker=st, status="open"):
                    if m.get("strike_type") != "greater_or_equal" or not m.get("floor_strike"):
                        continue
                    markets[m["ticker"]] = {"series": st, "asset": a, "strike": float(m["floor_strike"]),
                                            "close": parse_ts(m["close_time"])}
            except Exception as exc:
                self.errors.append(f"{iso(now_utc())} refresh {st}: {exc}")
        self.markets = markets
        self.last_refresh = time.time()

    def vol(self, asset):
        hit = self.sigma.get(asset)
        if hit and time.time() - hit[0] < 60:
            return hit[1]
        try:
            r = requests.get(CANDLES.format(asset), params={"granularity": 60}, timeout=5)
            rows = sorted(r.json(), key=lambda c: c[0])[-61:]
            closes = [float(c[4]) for c in rows]
            rets = [math.log(b / a) for a, b in zip(closes, closes[1:]) if a > 0 and b > 0]
            s60 = statistics.pstdev(rets) if len(rets) > 20 else None
            s15 = statistics.pstdev(rets[-15:]) if len(rets) >= 15 else s60
            sig = math.sqrt(0.5 * s60 ** 2 + 0.5 * s15 ** 2) if s60 else None
        except Exception as exc:
            self.errors.append(f"{iso(now_utc())} candles {asset}: {exc}")
            sig = hit[1] if hit else None
        if sig:
            sig = max(sig, SIGMA_FLOOR)
            self.sigma[asset] = (time.time(), sig)
        return sig

    def spots(self):
        out, now = {}, now_utc()
        for a in set(self.assets.values()):
            try:
                r = requests.get(SPOT.format(a), timeout=3)
                if r.status_code == 200:
                    p = float(r.json()["price"])
                    out[a] = p
                    dq = self.samples.setdefault(a, deque(maxlen=120))
                    dq.append((now, p))
            except Exception:
                pass
        return out

    def quotes(self):
        tickers = [t for t, m in self.markets.items() if m["close"] > now_utc()]
        out = {}
        for i in range(0, len(tickers), 50):
            data = kalshi_get("/markets", {"tickers": ",".join(tickers[i:i + 50]), "limit": 1000})
            out.update({m["ticker"]: m for m in data.get("markets", [])})
        return out

    def poll(self):
        spot = self.spots()
        q = self.quotes()
        now = now_utc()
        for ticker, m in q.items():
            meta = self.markets.get(ticker)
            a = meta and meta["asset"]
            if not meta or a not in spot or m.get("status") not in ("active", "open"):
                continue
            secs_left = (meta["close"] - now).total_seconds()
            if secs_left <= 0:
                continue
            sig = self.vol(a)
            if not sig:
                continue
            window = [p for t, p in self.samples.get(a, []) if t >= meta["close"] - timedelta(seconds=60)]
            p_up = fair_up(spot[a], meta["strike"], secs_left, sig, window)

            # Shadow log for model-vs-market accuracy.
            if time.time() - self.last_obs.get(ticker, 0) >= OBS_SECONDS:
                self.obs.append({"time": iso(now), "ticker": ticker, "asset": a,
                                 "secs_left": f"{secs_left:.0f}", "spot": f"{spot[a]:g}",
                                 "strike": meta["strike"], "sigma_pct": f"{sig * 100:.4f}",
                                 "model_up": f"{p_up:.4f}",
                                 "yes_bid": f"{price(m, 'yes_bid') or 0:.2f}",
                                 "yes_ask": f"{price(m, 'yes_ask') or 0:.2f}"})
                self.last_obs[ticker] = time.time()
                self.seen[ticker] = meta["close"]

            # Early skill check: our side's mid 3 minutes after buying (or 60s before close).
            for t in self.trades:
                bought = parse_ts(t["time"]) if t["ticker"] == ticker else None
                if bought and t["status"] == "open" and not t.get("mid_at_60s") and \
                        ((now - bought).total_seconds() >= 180 or secs_left <= 60):
                    bid, ask = side_quote(m, t["side"])
                    if bid is not None and ask is not None:
                        mid = (bid + ask) / 2
                        t["mid_at_60s"] = f"{mid:.3f}"
                        t["clv"] = f"{mid - float(t['price']):.3f}"

            if not self.accept_new or ticker in self.traded or not (MIN_SECS <= secs_left <= MAX_SECS):
                continue
            for side, p in (("yes", p_up), ("no", 1 - p_up)):
                _, ask = side_quote(m, side)
                if ask is None or not (MIN_PRICE <= ask <= MAX_PRICE):
                    continue
                fee = fee_per_contract(ask, CONTRACTS)
                edge = p - ask - fee
                if edge < EDGE:
                    continue
                self.signals += 1
                depth = depth_at_ask(ticker, side, ask)
                gap = (spot[a] - meta["strike"]) / meta["strike"] * 100
                self.trades.append({
                    "time": iso(now), "ticker": ticker, "asset": a, "side": side,
                    "secs_left": f"{secs_left:.0f}", "spot": f"{spot[a]:g}", "strike": meta["strike"],
                    "gap_pct": f"{gap:.4f}", "sigma_pct": f"{sig * 100:.4f}", "model_p": f"{p:.4f}",
                    "price": f"{ask:.2f}", "fee": f"{fee:.4f}", "edge": f"{edge:.4f}",
                    "contracts": CONTRACTS, "status": "open",
                    "depth_at_ask": f"{depth:.0f}" if depth is not None else ""})
                self.traded.add(ticker)
                print(f"BUY {CONTRACTS} {'UP' if side == 'yes' else 'DOWN'} {ticker} @ {ask:.2f} "
                      f"model {p:.1%} edge {edge * 100:.1f}c, {secs_left:.0f}s left")
                break

    def settle(self):
        now = now_utc()
        pending = {t["ticker"] for t in self.trades if t["status"] == "open"} | set(self.seen)
        for ticker in list(pending):
            if ticker in self.results:
                self.seen.pop(ticker, None)
                continue
            meta = self.markets.get(ticker)
            close = meta["close"] if meta else self.seen.get(ticker)
            if close is None:
                t = next((t for t in self.trades if t["ticker"] == ticker), None)
                if not t:
                    continue
                close = parse_ts(t["time"]) + timedelta(seconds=float(t["secs_left"]))
            if now < close + timedelta(seconds=30):
                continue
            try:
                m = kalshi_get(f"/markets/{ticker}")["market"]
            except Exception as exc:
                self.errors.append(f"{iso(now)} settle {ticker}: {exc}")
                continue
            if m.get("result") in ("yes", "no"):
                self.results[ticker] = {"ticker": ticker, "result": m["result"], "close_time": iso(close)}
        for t in self.trades:
            r = self.results.get(t["ticker"])
            if t["status"] == "open" and r:
                n = int(t["contracts"])
                cost = n * (float(t["price"]) + float(t["fee"]))
                t.update(status="settled", result=r["result"],
                         pnl=f"{(n if r['result'] == t['side'] else 0) - cost:.2f}")

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
            json.dump({"saved_at": iso(now_utc()), "assets": sorted(set(self.assets.values())),
                       "markets": len(self.markets), "trades": len(self.trades),
                       "open": sum(1 for t in self.trades if t["status"] == "open"),
                       "results_known": len(self.results),
                       "sigma_pct": {a: round(s * 100, 4) for a, (_, s) in self.sigma.items()},
                       "errors": self.errors[-15:]}, fh, indent=1)


def main():
    fv = FairValue()
    end = time.time() + RUN_MINUTES * 60
    last_save = time.time()
    last_settle = 0.0
    while time.time() < end:
        start = time.time()
        try:
            if time.time() - fv.last_series > 3600:
                fv.load_series()
            n = now_utc()
            if time.time() - fv.last_refresh > 60 or (n.minute % 15 == 0 and n.second < 10
                                                       and time.time() - fv.last_refresh > 8):
                fv.refresh()
            fv.poll()
            if time.time() - last_settle > 20:
                fv.settle()
                last_settle = time.time()
        except Exception as exc:
            print(f"loop error: {exc}")
            fv.errors.append(f"{iso(now_utc())} loop: {exc}")
        if time.time() - last_save >= SAVE_MINUTES * 60:
            fv.save()
            git_save()
            last_save = time.time()
        time.sleep(max(0.2, POLL_SECONDS - (time.time() - start)))
    fv.accept_new = False
    deadline = time.time() + 20 * 60
    while any(t["status"] == "open" for t in fv.trades) and time.time() < deadline:
        try:
            fv.poll()
            fv.settle()
        except Exception as exc:
            print(f"wind-down error: {exc}")
        time.sleep(POLL_SECONDS)
    fv.save()
    print(f"fair-value: {len(fv.trades)} trades")
    return 0


if __name__ == "__main__":
    sys.exit(main())
