"""Paper-trading bot for Kalshi daily high-temperature markets.

Compares the National Weather Service forecast high with Kalshi prices,
logs a fake trade when the forecast implies a big enough edge, and later
scores those trades once Kalshi settles them. No real orders are ever sent.
"""
import csv
import math
import os
import sys
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import requests

KALSHI = "https://api.elections.kalshi.com/trade-api/v2"
NWS_HEADERS = {"User-Agent": "kalshi-weather-paper-bot (github actions)"}
TRADES_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "trades.csv")

# Series ticker -> (settlement station lat, lon, local time zone)
CITIES = {
    "KXHIGHNY": (40.7789, -73.9692, "America/New_York"),     # Central Park
    "KXHIGHCHI": (41.7868, -87.7522, "America/Chicago"),     # Midway
    "KXHIGHMIA": (25.7906, -80.3164, "America/New_York"),    # Miami Intl
    "KXHIGHAUS": (30.1831, -97.6799, "America/Chicago"),     # Austin Bergstrom
    "KXHIGHDEN": (39.8466, -104.6562, "America/Denver"),     # Denver Intl
    "KXHIGHLAX": (33.9382, -118.3866, "America/Los_Angeles"),  # LAX
    "KXHIGHPHIL": (39.8733, -75.2268, "America/New_York"),   # Philadelphia Intl
}

# Strategy settings
FORECAST_ERROR_F = 3.0   # typical miss of a next-day NWS high forecast (std dev, deg F)
MIN_EDGE = 0.08          # need model prob to beat price (after fees) by 8 cents
MIN_PRICE = 0.05         # skip lottery tickets
MAX_PRICE = 0.90         # skip near-certainties with tiny upside
CONTRACTS = 10           # paper position size per trade

FIELDS = ["logged_at", "ticker", "city", "market_date", "side", "price",
          "fee", "contracts", "model_prob", "forecast_high", "bracket",
          "status", "result", "pnl"]


def fee_per_contract(price):
    """Kalshi taker fee: 7% * P * (1-P), rounded up to the cent."""
    return math.ceil(0.07 * price * (1 - price) * 100 - 1e-9) / 100


def norm_cdf(x, mu, sigma):
    return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))


def bracket_prob(market, mu, sigma):
    """Probability the day's high lands in this market's YES range.

    Highs are whole degrees, so 'greater than 72' means 73+ -> X > 72.5.
    """
    kind = market.get("strike_type")
    lo, hi = market.get("floor_strike"), market.get("cap_strike")
    if kind == "greater" and lo is not None:
        return 1 - norm_cdf(lo + 0.5, mu, sigma)
    if kind == "less" and hi is not None:
        return norm_cdf(hi - 0.5, mu, sigma)
    if kind == "between" and lo is not None and hi is not None:
        return norm_cdf(hi + 0.5, mu, sigma) - norm_cdf(lo - 0.5, mu, sigma)
    return None


def bracket_label(market):
    kind = market.get("strike_type")
    lo, hi = market.get("floor_strike"), market.get("cap_strike")
    if kind == "greater":
        return f">{lo}"
    if kind == "less":
        return f"<{hi}"
    return f"{lo}-{hi}"


def price(market, key):
    """Read a price in dollars from either the new *_dollars or old cents fields."""
    val = market.get(f"{key}_dollars")
    if val not in (None, ""):
        return float(val)
    val = market.get(key)
    return float(val) / 100 if val not in (None, "") else None


def market_date(ticker):
    """KXHIGHNY-26SEP28-T72 -> date(2026, 9, 28)."""
    try:
        return datetime.strptime(ticker.split("-")[1], "%y%b%d").date()
    except (IndexError, ValueError):
        return None


def get_markets(series, status):
    out, cursor = [], None
    while True:
        params = {"series_ticker": series, "status": status, "limit": 200}
        if cursor:
            params["cursor"] = cursor
        r = requests.get(f"{KALSHI}/markets", params=params, timeout=20)
        r.raise_for_status()
        data = r.json()
        out += data.get("markets", [])
        cursor = data.get("cursor")
        if not cursor:
            return out


def nws_daily_highs(lat, lon):
    """Return {date: forecast high F} from the NWS 7-day forecast."""
    p = requests.get(f"https://api.weather.gov/points/{lat},{lon}",
                     headers=NWS_HEADERS, timeout=20)
    p.raise_for_status()
    f = requests.get(p.json()["properties"]["forecast"],
                     headers=NWS_HEADERS, timeout=20)
    f.raise_for_status()
    highs = {}
    for period in f.json()["properties"]["periods"]:
        if period.get("isDaytime"):
            d = datetime.fromisoformat(period["startTime"]).date()
            temp = period["temperature"]
            if period.get("temperatureUnit") == "C":
                temp = temp * 9 / 5 + 32
            highs[d] = float(temp)
    return highs


def load_trades():
    if not os.path.exists(TRADES_FILE):
        return []
    with open(TRADES_FILE, newline="") as fh:
        return list(csv.DictReader(fh))


def save_trades(rows):
    with open(TRADES_FILE, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)


def pick_trade(market, mu, sigma):
    """Return (side, price, fee, model_prob) if there's an edge, else None."""
    p_yes = bracket_prob(market, mu, sigma)
    if p_yes is None:
        return None
    best = None
    for side, prob, ask in (("yes", p_yes, price(market, "yes_ask")),
                            ("no", 1 - p_yes, price(market, "no_ask"))):
        if ask is None or not (MIN_PRICE <= ask <= MAX_PRICE):
            continue
        fee = fee_per_contract(ask)
        edge = prob - ask - fee
        if edge >= MIN_EDGE and (best is None or edge > best[0]):
            best = (edge, side, ask, fee, prob)
    return best[1:] if best else None


def open_new_trades(trades):
    held = {t["ticker"] for t in trades}
    now = datetime.now(timezone.utc)
    added = 0
    for series, (lat, lon, tz) in CITIES.items():
        tomorrow = (now.astimezone(ZoneInfo(tz)) + timedelta(days=1)).date()
        try:
            highs = nws_daily_highs(lat, lon)
            markets = get_markets(series, "open")
        except Exception as exc:  # one bad city shouldn't stop the rest
            print(f"{series}: skipped ({exc})")
            continue
        mu = highs.get(tomorrow)
        if mu is None:
            print(f"{series}: no forecast for {tomorrow}")
            continue
        for m in markets:
            if m["ticker"] in held or market_date(m["ticker"]) != tomorrow:
                continue
            pick = pick_trade(m, mu, FORECAST_ERROR_F)
            if not pick:
                continue
            side, ask, fee, prob = pick
            trades.append({
                "logged_at": now.isoformat(timespec="seconds"),
                "ticker": m["ticker"], "city": series.replace("KXHIGH", ""),
                "market_date": tomorrow.isoformat(), "side": side,
                "price": f"{ask:.2f}", "fee": f"{fee:.2f}",
                "contracts": CONTRACTS, "model_prob": f"{prob:.3f}",
                "forecast_high": f"{mu:.0f}", "bracket": bracket_label(m),
                "status": "open", "result": "", "pnl": "",
            })
            held.add(m["ticker"])
            added += 1
            print(f"PAPER BUY {CONTRACTS} {side.upper()} {m['ticker']} @ {ask:.2f} "
                  f"(model {prob:.0%}, forecast {mu:.0f}F)")
    return added


def settle_trades(trades):
    open_by_series = {}
    for t in trades:
        if t["status"] == "open":
            open_by_series.setdefault("KXHIGH" + t["city"], []).append(t)
    settled = 0
    for series, rows in open_by_series.items():
        try:
            results = {m["ticker"]: m.get("result")
                       for m in get_markets(series, "settled")}
        except Exception as exc:
            print(f"{series}: settle check skipped ({exc})")
            continue
        for t in rows:
            res = results.get(t["ticker"])
            if res not in ("yes", "no"):
                continue
            n, cost = int(t["contracts"]), float(t["price"]) + float(t["fee"])
            payout = 1.0 if res == t["side"] else 0.0
            t.update(status="settled", result=res,
                     pnl=f"{n * (payout - cost):.2f}")
            settled += 1
    return settled


def summary(trades):
    done = [t for t in trades if t["status"] == "settled"]
    wins = sum(1 for t in done if float(t["pnl"]) > 0)
    pnl = sum(float(t["pnl"]) for t in done)
    risked = sum(int(t["contracts"]) * (float(t["price"]) + float(t["fee"])) for t in done)
    roi = f"{pnl / risked:.1%}" if risked else "n/a"
    open_n = sum(1 for t in trades if t["status"] == "open")
    return (f"Settled: {len(done)} | Wins: {wins} | Paper P&L: ${pnl:.2f} | "
            f"Return on risk: {roi} | Open: {open_n}")


def main():
    trades = load_trades()
    settled = settle_trades(trades)
    added = open_new_trades(trades)
    save_trades(trades)
    print(f"New: {added} | Newly settled: {settled}")
    print(summary(trades))
    return 0


if __name__ == "__main__":
    sys.exit(main())
