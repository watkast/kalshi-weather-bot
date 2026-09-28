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

import hourly
import risk
from common import HERE, fee_per_contract, get_markets, kalshi_get, price
from fifteen_bot import append_csv, asset_of, iso, norm_cdf, parse_ts, side_quote, write_csv

DIR = os.path.join(HERE, "fv")
TRADES = os.path.join(DIR, "trades.csv")
TRADES_V2 = os.path.join(DIR, "trades_v2.csv")

# Version 2 (added Sep 28): trend-aware and less overconfident.
V2_VOL_MULT = 1.25        # widen volatility 25% (crypto has fatter tails than a normal curve)
V2_MARKET_WEIGHT = 0.5    # average our number 50/50 with Kalshi's own price
V2_TREND_MINUTES = 30     # recent trend we assume partly continues
V2_TREND_KEEP = 0.5       # keep half of that trend's pace for the rest of the window
V2_TREND_CAP = 0.0005     # cap the assumed trend at 0.05% per minute
RESULTS = os.path.join(DIR, "results.csv")
TRADES_V3 = os.path.join(DIR, "trades_v3.csv")
TRADES_V4 = os.path.join(DIR, "trades_v4.csv")
TRADES_V5 = os.path.join(DIR, "trades_v5.csv")
TRADES_V6 = os.path.join(DIR, "trades_v6.csv")
TRADES_V7 = os.path.join(DIR, "trades_v7.csv")
TRADES_V8 = os.path.join(DIR, "trades_v8.csv")   # Trend Sniper on 1-hour markets   # V5 rules traded through the risk-managed account

# V5 "Trend Sniper" and V6 "60s Harvester" (added Sep 28, from the user's earlier dashboard).
V5_MIN_SECS, V5_MAX_SECS = 360, 720      # 6-12 minutes left
V5_MIN_PRICE, V5_MAX_PRICE = 0.25, 0.55  # only cheap-to-middling contracts
V5_EDGE = 0.06
V5_TAKE_PROFIT = 0.85                    # sell if our side's bid reaches 85c
V6_MIN_SECS, V6_MAX_SECS = 15, 60        # final minute
V6_MIN_PRICE, V6_MAX_PRICE = 0.75, 0.90
V6_MIN_PROB = 0.98                       # model must be at least 98% sure

# Versions 3 and 4 (added Sep 28). Both use a multi-exchange price and cap
# trades per 15-minute window so one market move can't swing every bet.
MAX_PER_WINDOW = 2
V3_EDGE = 0.08            # V3: only 5-10 min left, and only big (8c+) edges
V3_MIN_SECS, V3_MAX_SECS = 300, 600
V4_BELOW_ASK = 0.02       # V4: bid 2c under the ask instead of paying it
V4_ORDER_SECONDS = 180    # cancel if not filled within 3 minutes
MAKER_RATE = 0.0175       # Kalshi's fee for resting (maker) orders, where charged

# Extra exchanges averaged with Coinbase to approximate Kalshi's settlement index.
EXTRA_SECONDS = 6
KRAKEN = {"BTC": ("XBTUSD", "XXBTZUSD"), "ETH": ("ETHUSD", "XETHZUSD"), "SOL": ("SOLUSD", "SOLUSD"),
          "XRP": ("XRPUSD", "XXRPZUSD"), "DOGE": ("XDGUSD", "XDGUSD")}

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
                "pnl", "mid_at_60s", "clv", "depth_at_ask", "quoted", "window", "sources",
                "placed_at", "filled_at", "trend_aligned", "exit_price", "exit_at"]
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


def fair_up_v2(spot, strike, secs_left, sigma, window_samples, trend, market_mid):
    """V2: add the recent trend as drift, widen volatility, then blend with
    Kalshi's price. The trend fixes V1's habit of leaning DOWN in rising markets."""
    tau = max(secs_left, 0.5) / 60
    drift = max(-V2_TREND_CAP, min(V2_TREND_CAP, trend)) * V2_TREND_KEEP * tau
    sig = sigma * V2_VOL_MULT
    if tau >= 1:
        var = sig ** 2 * (tau - 2 / 3) + BASIS_SD ** 2
        x = math.log(spot / strike) + drift
    else:
        known = statistics.fmean(window_samples) if window_samples else spot
        expected = (1 - tau) * known + tau * spot * math.exp(drift)
        var = sig ** 2 * tau ** 3 / 3 + BASIS_SD ** 2
        x = math.log(expected / strike)
    p = norm_cdf(x / math.sqrt(var))
    if market_mid is not None and 0 < market_mid < 1:
        p = V2_MARKET_WEIGHT * market_mid + (1 - V2_MARKET_WEIGHT) * p
    return min(max(p, 0.001), 0.999)


def maker_fee(p, n):
    return math.ceil(MAKER_RATE * n * p * (1 - p) * 100 - 1e-9) / 100 / n


def window_of(ticker):
    return ticker.split("-")[1] if "-" in ticker else ticker


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

def book_fill(ticker, side, contracts):
    """Real price to buy `contracts` of `side` right now, walking Kalshi's order
    book. Buying YES means matching NO bids at (1 - their price), and vice versa.
    Returns (average price, best price, contracts available) or None."""
    try:
        book = kalshi_get(f"/markets/{ticker}/orderbook").get("orderbook_fp") or {}
    except Exception:
        return None
    levels = sorted(((1 - float(p), float(q)) for p, q in
                     (book.get("no_dollars" if side == "yes" else "yes_dollars") or []) if float(q) > 0))
    if not levels:
        return None
    need, cost = contracts, 0.0
    for px, qty in levels:
        take = min(need, qty)
        cost += take * px
        need -= take
        if need <= 1e-9:
            break
    if need > 1e-9:
        return None
    return round(cost / contracts, 4), levels[0][0], sum(q for _, q in levels)


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
        self.trades_v2 = load(TRADES_V2)
        self.traded_v2 = {t["ticker"] for t in self.trades_v2}
        self.trend = {}           # asset -> recent per-minute trend
        self.trades_v3 = load(TRADES_V3)
        self.trades_v4 = load(TRADES_V4)
        self.trades_v5 = load(TRADES_V5)
        self.trades_v6 = load(TRADES_V6)
        self.trades_v7 = load(TRADES_V7)
        self.acct = risk.PaperAccount(DIR)
        self.trades_v8 = load(TRADES_V8)
        self.hourly = hourly.Hourly(self)
        self.last_spot = {}
        self.basis = {}           # asset -> {exchange: (fetched_at, price / coinbase)}
        self.dead = {}            # (exchange, asset) -> consecutive failures
        self.last_extra = 0.0
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
            if len(rets) >= V2_TREND_MINUTES:
                self.trend[asset] = sum(rets[-V2_TREND_MINUTES:]) / V2_TREND_MINUTES
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

    def extra_prices(self, cb):
        """Every few seconds, read Kraken, Bitstamp and Gemini and store each one's
        ratio to Coinbase. Exchanges that keep failing for a coin are skipped."""
        if time.time() - self.last_extra < EXTRA_SECONDS or not cb:
            return
        self.last_extra = time.time()
        got = {}
        pairs = [KRAKEN[a][0] for a in cb if a in KRAKEN and self.dead.get(("kraken", a), 0) < 3]
        if pairs:
            try:
                r = requests.get("https://api.kraken.com/0/public/Ticker",
                                 params={"pair": ",".join(pairs)}, timeout=4)
                res = r.json().get("result", {}) if r.status_code == 200 else {}
                for a in cb:
                    if a in KRAKEN:
                        row = res.get(KRAKEN[a][1]) or res.get(KRAKEN[a][0])
                        if row:
                            got[("kraken", a)] = float(row["c"][0])
            except Exception:
                pass
        for a in cb:
            for ex, url, key in (("bitstamp", f"https://www.bitstamp.net/api/v2/ticker/{a.lower()}usd/", "last"),
                                 ("gemini", f"https://api.gemini.com/v1/pubticker/{a.lower()}usd", "last")):
                if self.dead.get((ex, a), 0) >= 3:
                    continue
                try:
                    r = requests.get(url, timeout=3)
                    if r.status_code == 200:
                        got[(ex, a)] = float(r.json()[key])
                except Exception:
                    pass
        now = time.time()
        for ex in ("kraken", "bitstamp", "gemini"):
            for a in cb:
                if (ex, a) in got and got[(ex, a)] > 0:
                    self.basis.setdefault(a, {})[ex] = (now, got[(ex, a)] / cb[a])
                    self.dead[(ex, a)] = 0
                elif ex != "kraken" or a in KRAKEN:
                    self.dead[(ex, a)] = self.dead.get((ex, a), 0) + 1

    def composite(self, a, cb_price):
        """Coinbase price scaled by the median ratio across all fresh exchanges."""
        ratios = [1.0] + [r for t, r in self.basis.get(a, {}).values()
                          if time.time() - t < 60 and abs(r - 1) <= 0.001]
        return cb_price * statistics.median(ratios), len(ratios)

    def quotes_for(self, tickers):
        out = {}
        for i in range(0, len(tickers), 50):
            data = kalshi_get("/markets", {"tickers": ",".join(tickers[i:i + 50]), "limit": 1000})
            out.update({m["ticker"]: m for m in data.get("markets", [])})
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
        self.last_spot = spot
        self.extra_prices(spot)
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
            ybid, yask = price(m, "yes_bid"), price(m, "yes_ask")
            mkt_mid = (ybid + yask) / 2 if ybid is not None and yask is not None and yask > 0 else None
            p_up2 = fair_up_v2(spot[a], meta["strike"], secs_left, sig, window,
                               self.trend.get(a, 0.0), mkt_mid)
            idx, n_src = self.composite(a, spot[a])
            p_idx = fair_up(idx, meta["strike"], secs_left, sig, window)

            # Shadow log for model-vs-market accuracy.
            if time.time() - self.last_obs.get(ticker, 0) >= OBS_SECONDS:
                self.obs.append({"time": iso(now), "ticker": ticker, "asset": a,
                                 "secs_left": f"{secs_left:.0f}", "spot": f"{spot[a]:g}",
                                 "strike": meta["strike"], "sigma_pct": f"{sig * 100:.4f}",
                                 "model_up": f"{p_up:.4f}", "model_up_v2": f"{p_up2:.4f}",
                                 "model_up_idx": f"{p_idx:.4f}", "idx_spot": f"{idx:g}", "sources": n_src,
                                 "yes_bid": f"{price(m, 'yes_bid') or 0:.2f}",
                                 "yes_ask": f"{price(m, 'yes_ask') or 0:.2f}"})
                self.last_obs[ticker] = time.time()
                self.seen[ticker] = meta["close"]

            # Early skill check: our side's mid 3 minutes after buying (or 60s before close).
            for t in self.trades_v4:
                if t["ticker"] != ticker or t["status"] != "resting":
                    continue
                _, ask_q = side_quote(m, t["side"])
                book = book_fill(ticker, t["side"], CONTRACTS) if ask_q is not None and \
                    ask_q <= float(t["price"]) + 0.02 else None
                ask_now = book[1] if book else None
                if ask_now is not None and ask_now <= float(t["price"]) + 1e-9:
                    t.update(status="open", filled_at=iso(now))
                    print(f"V4 FILLED {ticker} {t['side']} @ {t['price']}")
                elif (now - parse_ts(t["placed_at"])).total_seconds() > V4_ORDER_SECONDS or secs_left < 60:
                    t.update(status="unfilled", pnl="0.00")

            for t in self.trades_v5 + self.trades_v7:
                if t["ticker"] == ticker and t["status"] == "open":
                    bid_now, _ = side_quote(m, t["side"])
                    if bid_now is not None and bid_now >= V5_TAKE_PROFIT:
                        n = int(t["contracts"])
                        cost = n * (float(t["price"]) + float(t["fee"]))
                        proceeds = n * bid_now - fee_per_contract(bid_now, n) * n
                        t.update(status="settled", result="sold", exit_price=f"{bid_now:.2f}",
                                 exit_at=iso(now), pnl=f"{proceeds - cost:.2f}")
                        if any(t is x for x in self.trades_v7):
                            self.acct.close(ticker, proceeds, "SELL", f"take profit @ {bid_now:.2f}")
                        print(f"TAKE PROFIT {ticker} @ {bid_now:.2f}")

            for t in self.trades + self.trades_v2 + self.trades_v3 + self.trades_v4 + self.trades_v5 + self.trades_v6 + self.trades_v7:
                bought = parse_ts(t.get("filled_at") or t["time"]) if t["ticker"] == ticker else None
                if bought and t["status"] == "open" and not t.get("mid_at_60s") and \
                        ((now - bought).total_seconds() >= 180 or secs_left <= 60):
                    bid, ask = side_quote(m, t["side"])
                    if bid is not None and ask is not None:
                        mid = (bid + ask) / 2
                        t["mid_at_60s"] = f"{mid:.3f}"
                        t["clv"] = f"{mid - float(t['price']):.3f}"

            if not self.accept_new or not (MIN_SECS <= secs_left <= MAX_SECS):
                continue
            gap = (spot[a] - meta["strike"]) / meta["strike"] * 100
            for book, done, pu, tag in ((self.trades, self.traded, p_up, "V1"),
                                        (self.trades_v2, self.traded_v2, p_up2, "V2")):
                if ticker in done:
                    continue
                for side, p in (("yes", pu), ("no", 1 - pu)):
                    _, ask = side_quote(m, side)
                    if ask is None or not (MIN_PRICE <= ask <= MAX_PRICE):
                        continue
                    fee = fee_per_contract(ask, CONTRACTS)
                    if p - ask - fee < EDGE:
                        continue
                    # Re-price against the live order book before buying.
                    fill = book_fill(ticker, side, CONTRACTS)
                    if not fill or not (MIN_PRICE <= fill[0] <= MAX_PRICE):
                        continue
                    quoted, ask = ask, fill[0]
                    fee = fee_per_contract(ask, CONTRACTS)
                    edge = p - ask - fee
                    if edge < EDGE:
                        continue
                    self.signals += 1
                    depth = fill[2]
                    book.append({
                        "time": iso(now), "ticker": ticker, "asset": a, "side": side,
                        "secs_left": f"{secs_left:.0f}", "spot": f"{spot[a]:g}", "strike": meta["strike"],
                        "gap_pct": f"{gap:.4f}", "sigma_pct": f"{sig * 100:.4f}", "model_p": f"{p:.4f}",
                        "price": f"{ask:.4f}", "fee": f"{fee:.4f}", "edge": f"{edge:.4f}",
                        "contracts": CONTRACTS, "status": "open",
                        "depth_at_ask": f"{depth:.0f}" if depth is not None else "",
                        "quoted": f"{quoted:.2f}"})
                    done.add(ticker)
                    print(f"{tag} BUY {CONTRACTS} {'UP' if side == 'yes' else 'DOWN'} {ticker} @ {ask:.2f} "
                          f"model {p:.1%} edge {edge * 100:.1f}c, {secs_left:.0f}s left")
                    break

            win = window_of(ticker)
            base = {"asset": a, "ticker": ticker, "secs_left": f"{secs_left:.0f}", "spot": f"{idx:g}",
                    "strike": meta["strike"], "gap_pct": f"{(idx - meta['strike']) / meta['strike'] * 100:.4f}",
                    "sigma_pct": f"{sig * 100:.4f}", "contracts": CONTRACTS, "window": win, "sources": n_src}
            # V3: timing rule, taker orders.
            if (V3_MIN_SECS <= secs_left <= V3_MAX_SECS and ticker not in {t["ticker"] for t in self.trades_v3}
                    and sum(1 for t in self.trades_v3 if t.get("window") == win) < MAX_PER_WINDOW):
                for side, p in (("yes", p_idx), ("no", 1 - p_idx)):
                    _, ask = side_quote(m, side)
                    if ask is None or not (MIN_PRICE <= ask <= MAX_PRICE):
                        continue
                    fee = fee_per_contract(ask, CONTRACTS)
                    if p - ask - fee < V3_EDGE:
                        continue
                    fill = book_fill(ticker, side, CONTRACTS)
                    if not fill or not (MIN_PRICE <= fill[0] <= MAX_PRICE):
                        continue
                    quoted, ask = ask, fill[0]
                    fee = fee_per_contract(ask, CONTRACTS)
                    edge = p - ask - fee
                    if edge >= V3_EDGE:
                        self.trades_v3.append({**base, "time": iso(now), "side": side, "model_p": f"{p:.4f}",
                                               "price": f"{ask:.4f}", "fee": f"{fee:.4f}", "edge": f"{edge:.4f}",
                                               "status": "open", "quoted": f"{quoted:.2f}",
                                               "depth_at_ask": f"{fill[2]:.0f}"})
                        print(f"V3 BUY {side} {ticker} @ {ask:.2f} edge {edge * 100:.1f}c")
                        break
            # V4: same model, but rest a limit order 2c under the ask.
            if (ticker not in {t["ticker"] for t in self.trades_v4}
                    and sum(1 for t in self.trades_v4 if t.get("window") == win and t["status"] != "unfilled")
                    < MAX_PER_WINDOW and secs_left >= 90):
                for side, p in (("yes", p_idx), ("no", 1 - p_idx)):
                    _, ask = side_quote(m, side)
                    if ask is None or p - (ask - V4_BELOW_ASK) < EDGE:
                        continue
                    fill = book_fill(ticker, side, 1)
                    if not fill:
                        continue
                    lim = round(fill[1] - V4_BELOW_ASK, 2)
                    if not (MIN_PRICE <= lim <= MAX_PRICE):
                        continue
                    fee = maker_fee(lim, CONTRACTS)
                    edge = p - lim - fee
                    if edge >= EDGE:
                        self.trades_v4.append({**base, "time": iso(now), "placed_at": iso(now), "side": side,
                                               "model_p": f"{p:.4f}", "price": f"{lim:.2f}", "fee": f"{fee:.4f}",
                                               "edge": f"{edge:.4f}", "status": "resting"})
                        print(f"V4 ORDER {side} {ticker} limit {lim:.2f} edge {edge * 100:.1f}c")
                        break
            # V5 Trend Sniper: 6-12 min left, 25-55c, 6c+ edge, one bet per direction per window.
            if V5_MIN_SECS <= secs_left <= V5_MAX_SECS and ticker not in {t["ticker"] for t in self.trades_v5}:
                taken = {t["side"] for t in self.trades_v5 if t.get("window") == win}
                for side, p in (("yes", p_up), ("no", 1 - p_up)):
                    _, ask = side_quote(m, side)
                    if side in taken or ask is None or p - ask < V5_EDGE:
                        continue
                    fill = book_fill(ticker, side, CONTRACTS)
                    if not fill or not (V5_MIN_PRICE <= fill[0] <= V5_MAX_PRICE):
                        continue
                    fee = fee_per_contract(fill[0], CONTRACTS)
                    edge = p - fill[0] - fee
                    if edge < V5_EDGE:
                        continue
                    tr = self.trend.get(a, 0.0)
                    self.trades_v5.append({**base, "spot": f"{spot[a]:g}", "time": iso(now), "side": side,
                                           "model_p": f"{p:.4f}", "price": f"{fill[0]:.4f}", "fee": f"{fee:.4f}",
                                           "edge": f"{edge:.4f}", "status": "open", "quoted": f"{ask:.2f}",
                                           "depth_at_ask": f"{fill[2]:.0f}",
                                           "trend_aligned": "yes" if (tr > 0) == (side == "yes") else "no"})
                    print(f"V5 BUY {side} {ticker} @ {fill[0]:.2f} edge {edge * 100:.1f}c")
                    # V7: same signal, sized and guarded by the risk-managed account.
                    ok, why = self.acct.can_open(ticker, side, win)
                    n7 = self.acct.size(fill[0] + fee) if ok else 0
                    fill7 = book_fill(ticker, side, n7) if n7 >= 1 else None
                    if fill7 and V5_MIN_PRICE <= fill7[0] <= V5_MAX_PRICE:
                        fee7 = fee_per_contract(fill7[0], n7)
                        if p - fill7[0] - fee7 >= V5_EDGE and \
                                self.acct.buy(ticker, side, n7, fill7[0], fee7, win):
                            self.trades_v7.append({**base, "spot": f"{spot[a]:g}", "time": iso(now), "side": side,
                                                   "model_p": f"{p:.4f}", "price": f"{fill7[0]:.4f}",
                                                   "fee": f"{fee7:.4f}", "edge": f"{p - fill7[0] - fee7:.4f}",
                                                   "status": "open", "contracts": n7, "quoted": f"{ask:.2f}",
                                                   "depth_at_ask": f"{fill7[2]:.0f}"})
                            print(f"V7 BUY {n7} {side} {ticker} @ {fill7[0]:.2f} (equity ${self.acct.equity():.2f})")
                    elif not ok:
                        print(f"V7 skip {ticker}: {why}")
                    break
            # V6 60s Harvester: final minute, model 98%+ sure, contract still 75-90c.
            if V6_MIN_SECS <= secs_left <= V6_MAX_SECS and ticker not in {t["ticker"] for t in self.trades_v6}:
                for side, p in (("yes", p_up), ("no", 1 - p_up)):
                    _, ask = side_quote(m, side)
                    if p < V6_MIN_PROB or ask is None or ask > V6_MAX_PRICE:
                        continue
                    fill = book_fill(ticker, side, CONTRACTS)
                    if not fill or not (V6_MIN_PRICE <= fill[0] <= V6_MAX_PRICE):
                        continue
                    fee = fee_per_contract(fill[0], CONTRACTS)
                    self.trades_v6.append({**base, "spot": f"{spot[a]:g}", "time": iso(now), "side": side,
                                           "model_p": f"{p:.4f}", "price": f"{fill[0]:.4f}", "fee": f"{fee:.4f}",
                                           "edge": f"{p - fill[0] - fee:.4f}", "status": "open",
                                           "quoted": f"{ask:.2f}", "depth_at_ask": f"{fill[2]:.0f}"})
                    print(f"V6 BUY {side} {ticker} @ {fill[0]:.2f} model {p:.1%}")
                    break

    def settle(self):
        now = now_utc()
        books = (self.trades + self.trades_v2 + self.trades_v3 + self.trades_v4 + self.trades_v5
                 + self.trades_v6 + self.trades_v7 + self.trades_v8)
        pending = {t["ticker"] for t in books if t["status"] == "open"} | set(self.seen)
        for ticker in list(pending):
            if ticker in self.results:
                self.seen.pop(ticker, None)
                continue
            meta = self.markets.get(ticker)
            close = meta["close"] if meta else self.seen.get(ticker)
            if close is None:
                t = next((t for t in books if t["ticker"] == ticker), None)
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
        for t in books:
            r = self.results.get(t["ticker"])
            if t["status"] == "open" and r:
                n = int(t["contracts"])
                cost = n * (float(t["price"]) + float(t["fee"]))
                payout = n if r["result"] == t["side"] else 0
                t.update(status="settled", result=r["result"], pnl=f"{payout - cost:.2f}")
                if any(t is x for x in self.trades_v7):
                    self.acct.close(t["ticker"], payout, "SETTLE", f"result {r['result']}")

    def save(self):
        by_day = {}
        for o in self.obs:
            by_day.setdefault(o["time"][:10], []).append(o)
        for day, rows in by_day.items():
            append_csv(os.path.join(DIR, "obs", f"{day}.csv"), rows, OBS_FIELDS)
            append_csv(os.path.join(DIR, "obs_v2", f"{day}.csv"), rows,
                       ["time", "ticker", "model_up_v2", "model_up_idx", "idx_spot", "sources"])
        self.obs = []
        write_csv(TRADES, self.trades, TRADE_FIELDS)
        write_csv(TRADES_V2, self.trades_v2, TRADE_FIELDS)
        write_csv(TRADES_V3, self.trades_v3, TRADE_FIELDS)
        write_csv(TRADES_V4, self.trades_v4, TRADE_FIELDS)
        write_csv(TRADES_V5, self.trades_v5, TRADE_FIELDS)
        write_csv(TRADES_V6, self.trades_v6, TRADE_FIELDS)
        write_csv(TRADES_V7, self.trades_v7, TRADE_FIELDS)
        write_csv(TRADES_V8, self.trades_v8, TRADE_FIELDS)
        self.acct.save()
        write_csv(RESULTS, list(self.results.values()), RESULT_FIELDS)
        with open(os.path.join(DIR, "status.json"), "w") as fh:
            json.dump({"saved_at": iso(now_utc()), "assets": sorted(set(self.assets.values())),
                       "markets": len(self.markets), "trades": len(self.trades), "trades_v2": len(self.trades_v2),
                       "trades_v3": len(self.trades_v3), "trades_v4": len(self.trades_v4),
                       "trades_v5": len(self.trades_v5), "trades_v6": len(self.trades_v6),
                       "trades_v7": len(self.trades_v7), "trades_v8": len(self.trades_v8), "account_equity": round(self.acct.equity(), 2),
                       "account_halted": self.acct.halted,
                       "extra_exchanges": {a: sorted(v) for a, v in self.basis.items()},
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
            try:
                fv.hourly.check(now_utc(), fv.last_spot, fv.quotes_for, book_fill, fair_up, iso)
            except Exception as exc:
                fv.errors.append(f"{iso(now_utc())} hourly: {exc}")
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
    books = lambda: (fv.trades + fv.trades_v2 + fv.trades_v3 + fv.trades_v4 + fv.trades_v5 + fv.trades_v6
                     + fv.trades_v7 + fv.trades_v8)
    while any(t["status"] in ("open", "resting") for t in books()) and time.time() < deadline:
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
