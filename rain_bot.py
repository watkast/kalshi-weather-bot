"""Paper-trading bot for Kalshi's daily 'Will it rain in <city>?' markets.

Uses the National Weather Service hourly chance of rain for tomorrow,
turns it into a chance of any measurable rain that calendar day, and
logs a paper trade when that beats Kalshi's price after fees.
"""
import re
import sys
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import requests

from common import (HERE, NWS_HEADERS, fee_per_contract, get_markets, load_rows,
                    price, save_rows, settle_by_ticker, summary)

TRADES_FILE = f"{HERE}/rain_trades.csv"

# Kalshi market suffix -> (settlement station lat, lon, time zone)
CITIES = {
    "ATL": (33.6301, -84.4418, "America/New_York"),
    "AUS": (30.1831, -97.6799, "America/Chicago"),
    "BOS": (42.3606, -71.0097, "America/New_York"),
    "CHI": (41.9786, -87.9048, "America/Chicago"),
    "CLL": (30.5886, -96.3638, "America/Chicago"),
    "CMH": (39.9950, -82.8778, "America/New_York"),
    "DAL": (32.8998, -97.0403, "America/Chicago"),
    "DC": (38.8483, -77.0341, "America/New_York"),
    "DEN": (39.8466, -104.6562, "America/Denver"),
    "EWR": (40.6925, -74.1687, "America/New_York"),
    "HOU": (29.6375, -95.2825, "America/Chicago"),
    "LAX": (33.9382, -118.3866, "America/Los_Angeles"),
    "LEX": (38.0365, -84.6059, "America/New_York"),
    "LV": (36.0719, -115.1634, "America/Los_Angeles"),
    "MIA": (25.7906, -80.3164, "America/New_York"),
    "MIN": (44.8831, -93.2289, "America/Chicago"),
    "MKE": (42.9550, -87.9044, "America/Chicago"),
    "NOLA": (29.9934, -90.2580, "America/Chicago"),
    "NYC": (40.7789, -73.9692, "America/New_York"),
    "OKC": (35.3889, -97.6003, "America/Chicago"),
    "PHIL": (39.8733, -75.2268, "America/New_York"),
    "PHX": (33.4278, -112.0037, "America/Phoenix"),
    "PIT": (40.4846, -80.2144, "America/New_York"),
    "PVD": (41.7225, -71.4325, "America/New_York"),
    "SATX": (29.5443, -98.4839, "America/Chicago"),
    "SEA": (47.4447, -122.3144, "America/Los_Angeles"),
    "SFO": (37.7705, -122.4270, "America/Los_Angeles"),
    "TTN": (40.2767, -74.8158, "America/New_York"),
}

MIN_EDGE = 0.10     # model must beat price + fee by 10 cents
MIN_PRICE = 0.05
MAX_PRICE = 0.90
CONTRACTS = 10

FIELDS = ["logged_at", "ticker", "city", "market_date", "side", "price", "fee",
          "contracts", "model_prob", "status", "result", "pnl"]


def hours_in(duration):
    """ISO-8601 duration like PT6H, P1D or P1DT3H -> hours."""
    m = re.fullmatch(r"P(?:(\d+)D)?(?:T(?:(\d+)H)?)?", duration)
    return int(m.group(1) or 0) * 24 + int(m.group(2) or 0) if m else 1


def hourly_rain_chance(lat, lon):
    """Return {aware datetime (UTC hour): chance 0-1} from NWS grid data."""
    p = requests.get(f"https://api.weather.gov/points/{lat},{lon}",
                     headers=NWS_HEADERS, timeout=20)
    p.raise_for_status()
    g = requests.get(p.json()["properties"]["forecastGridData"],
                     headers=NWS_HEADERS, timeout=30)
    g.raise_for_status()
    out = {}
    for v in g.json()["properties"]["probabilityOfPrecipitation"]["values"]:
        if v.get("value") is None:
            continue
        start, dur = v["validTime"].split("/")
        t0 = datetime.fromisoformat(start).astimezone(timezone.utc)
        for h in range(hours_in(dur)):
            out[t0 + timedelta(hours=h)] = v["value"] / 100
    return out


def day_rain_chance(hourly, day, tz):
    """Chance of any rain over a local calendar day.

    NWS gives chances per block of hours. Rain in neighbouring blocks is
    strongly linked, so we blend the 'blocks are independent' answer
    (too high) with the 'wettest block only' answer (too low).
    """
    start = datetime(day.year, day.month, day.day, tzinfo=ZoneInfo(tz)).astimezone(timezone.utc)
    blocks = []
    for b in range(4):  # four 6-hour blocks
        vals = [hourly.get(start + timedelta(hours=6 * b + h)) for h in range(6)]
        vals = [v for v in vals if v is not None]
        if len(vals) < 3:
            return None  # not enough forecast coverage
        blocks.append(max(vals))
    wettest = max(blocks)
    independent = 1.0
    for b in blocks:
        independent *= 1 - b
    independent = 1 - independent
    return wettest + 0.5 * (independent - wettest)


def open_new_trades(rows):
    held = {t["ticker"] for t in rows}
    now = datetime.now(timezone.utc)
    added = 0
    by_date = {}
    for code, (lat, lon, tz) in CITIES.items():
        tomorrow = (now.astimezone(ZoneInfo(tz)) + timedelta(days=1)).date()
        by_date.setdefault(tomorrow, []).append(code)

    for day, codes in by_date.items():
        event = f"KXRAIN-{day.strftime('%y%b%d').upper()}"
        try:
            markets = {m["ticker"].split("-")[-1]: m for m in get_markets(event_ticker=event)}
        except Exception as exc:
            print(f"{event}: skipped ({exc})")
            continue
        for code in codes:
            m = markets.get(code)
            if not m or m["ticker"] in held or m.get("status") not in (None, "open", "active"):
                continue
            lat, lon, tz = CITIES[code]
            try:
                p_yes = day_rain_chance(hourly_rain_chance(lat, lon), day, tz)
            except Exception as exc:
                print(f"{code}: forecast skipped ({exc})")
                continue
            if p_yes is None:
                continue
            best = None
            for side, prob, ask in (("yes", p_yes, price(m, "yes_ask")),
                                    ("no", 1 - p_yes, price(m, "no_ask"))):
                if ask is None or not (MIN_PRICE <= ask <= MAX_PRICE):
                    continue
                fee = fee_per_contract(ask)
                edge = prob - ask - fee
                if edge >= MIN_EDGE and (best is None or edge > best[0]):
                    best = (edge, side, ask, fee, prob)
            if not best:
                continue
            _, side, ask, fee, prob = best
            rows.append({
                "logged_at": now.isoformat(timespec="seconds"), "ticker": m["ticker"],
                "city": code, "market_date": day.isoformat(), "side": side,
                "price": f"{ask:.2f}", "fee": f"{fee:.2f}", "contracts": CONTRACTS,
                "model_prob": f"{prob:.3f}", "status": "open", "result": "", "pnl": "",
            })
            held.add(m["ticker"])
            added += 1
            print(f"PAPER BUY {CONTRACTS} {side.upper()} {m['ticker']} @ {ask:.2f} (model {prob:.0%})")
    return added


def main():
    rows = load_rows(TRADES_FILE)
    settled = settle_by_ticker(rows)
    added = open_new_trades(rows)
    save_rows(TRADES_FILE, rows, FIELDS)
    print(f"New: {added} | Newly settled: {settled}")
    print(summary("Rain", rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
