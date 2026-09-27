"""Shared helpers for the Kalshi paper bots."""
import csv
import math
import os
import time

import requests

KALSHI = "https://api.elections.kalshi.com/trade-api/v2"
NWS_HEADERS = {"User-Agent": "kalshi-weather-paper-bot (github actions)"}
HERE = os.path.dirname(os.path.abspath(__file__))


def fee_per_contract(p, contracts=1):
    """Kalshi taker fee, per contract. Kalshi charges 7% * C * P * (1-P)
    per order, rounded up to the cent, so bigger orders round less."""
    total = math.ceil(0.07 * contracts * p * (1 - p) * 100 - 1e-9) / 100
    return total / contracts


def price(market, key):
    """Price in dollars from the *_dollars field (or legacy cents field)."""
    val = market.get(f"{key}_dollars")
    if val not in (None, ""):
        return float(val)
    val = market.get(key)
    return float(val) / 100 if val not in (None, "") else None


def volume(market):
    for key in ("volume_fp", "volume"):
        val = market.get(key)
        if val not in (None, ""):
            return float(val)
    return 0.0


def kalshi_get(path, params=None):
    for attempt in range(4):
        r = requests.get(f"{KALSHI}{path}", params=params, timeout=30)
        if r.status_code == 429:
            time.sleep(2 ** attempt)
            continue
        r.raise_for_status()
        return r.json()
    r.raise_for_status()


def get_markets(max_pages=60, **params):
    out, cursor = [], None
    for _ in range(max_pages):
        q = dict(params, limit=1000)
        if cursor:
            q["cursor"] = cursor
        data = kalshi_get("/markets", q)
        out += data.get("markets", [])
        cursor = data.get("cursor")
        if not cursor:
            return out
    print(f"get_markets: stopped after {max_pages} pages")
    return out


def load_rows(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="") as fh:
        return list(csv.DictReader(fh))


def save_rows(path, rows, fields):
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def settle_by_ticker(rows):
    """Look up each open trade's market and score it once Kalshi settles it."""
    settled = 0
    for t in rows:
        if t["status"] != "open":
            continue
        try:
            m = kalshi_get(f"/markets/{t['ticker']}")["market"]
        except Exception as exc:
            print(f"{t['ticker']}: settle check skipped ({exc})")
            continue
        time.sleep(0.1)
        res = m.get("result")
        if res not in ("yes", "no", "void") or m.get("status") not in ("settled", "finalized", "determined"):
            continue
        n, cost = int(t["contracts"]), float(t["price"]) + float(t["fee"])
        if res == "void":
            pnl = 0.0
        else:
            pnl = n * ((1.0 if res == t["side"] else 0.0) - cost)
        t.update(status="settled", result=res, pnl=f"{pnl:.2f}")
        settled += 1
    return settled


def summary(name, rows):
    done = [t for t in rows if t["status"] == "settled"]
    wins = sum(1 for t in done if float(t["pnl"]) > 0)
    pnl = sum(float(t["pnl"]) for t in done)
    risked = sum(int(t["contracts"]) * (float(t["price"]) + float(t["fee"])) for t in done)
    roi = f"{pnl / risked:.1%}" if risked else "n/a"
    open_n = sum(1 for t in rows if t["status"] == "open")
    return (f"{name} — Settled: {len(done)} | Wins: {wins} | Paper P&L: ${pnl:.2f} | "
            f"Return on risk: {roi} | Open: {open_n}")
