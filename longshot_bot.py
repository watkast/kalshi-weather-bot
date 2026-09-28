"""Paper-trading bot that fades long shots across all of Kalshi.

Prediction markets tend to overprice long shots: contracts trading under
10 cents win less often than their price implies. This bot bets against
them (buys NO) on liquid markets closing within a week, and tracks how
the strategy does in each market category.
"""
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone

from common import (HERE, fee_per_contract, get_markets, load_rows, price,
                    save_rows, settle_by_ticker, summary, volume)

TRADES_FILE = f"{HERE}/longshot_trades.csv"

MAX_YES_ASK = 0.10      # YES must cost 10 cents or less (a long shot)
MIN_YES_BID = 0.02      # but someone must still be paying for it
MAX_NO_ASK = 0.96       # leave at least ~3 cents of upside after fees
MIN_VOLUME = 100        # skip dead markets
MAX_DAYS_TO_CLOSE = 7   # results within a week
MAX_NEW_PER_RUN = 40
MAX_PER_EVENT = 3       # spread bets across different events
CONTRACTS = 10

FIELDS = ["logged_at", "ticker", "series", "close_time", "side", "price", "fee",
          "contracts", "yes_bid", "yes_ask", "volume", "status", "result", "pnl"]


def candidates(now):
    max_close = int((now + timedelta(days=MAX_DAYS_TO_CLOSE)).timestamp())
    min_close = int((now + timedelta(hours=1)).timestamp())
    for m in get_markets(status="open", min_close_ts=min_close, max_close_ts=max_close,
                         mve_filter="exclude"):
        if m["ticker"].startswith("KXMVE") or m.get("mve_collection_ticker"):
            continue  # multi-leg parlays, not simple long shots
        if m["ticker"].startswith("KXNFL"):
            continue  # NFL long shots were fairly priced (fading them lost money), dropped Sep 27
        yes_bid, yes_ask, no_ask = price(m, "yes_bid"), price(m, "yes_ask"), price(m, "no_ask")
        if None in (yes_bid, yes_ask, no_ask):
            continue
        if yes_bid >= MIN_YES_BID and yes_ask <= MAX_YES_ASK and no_ask <= MAX_NO_ASK \
                and volume(m) >= MIN_VOLUME:
            yield m


def open_new_trades(rows):
    held = {t["ticker"] for t in rows}
    per_event = Counter(t["ticker"].rsplit("-", 1)[0] for t in rows)
    now = datetime.now(timezone.utc)
    added = 0
    for m in sorted(candidates(now), key=volume, reverse=True):
        if added >= MAX_NEW_PER_RUN:
            break
        event = m["ticker"].rsplit("-", 1)[0]
        if m["ticker"] in held or per_event[event] >= MAX_PER_EVENT:
            continue
        ask = price(m, "no_ask")
        fee = fee_per_contract(ask, CONTRACTS)
        rows.append({
            "logged_at": now.isoformat(timespec="seconds"), "ticker": m["ticker"],
            "series": event.split("-")[0], "close_time": m.get("close_time", ""),
            "side": "no", "price": f"{ask:.2f}", "fee": f"{fee:.4f}",
            "contracts": CONTRACTS, "yes_bid": f"{price(m, 'yes_bid'):.2f}",
            "yes_ask": f"{price(m, 'yes_ask'):.2f}", "volume": f"{volume(m):.0f}",
            "status": "open", "result": "", "pnl": "",
        })
        held.add(m["ticker"])
        per_event[event] += 1
        added += 1
        print(f"PAPER BUY {CONTRACTS} NO {m['ticker']} @ {ask:.2f}")
    return added


def main():
    rows = load_rows(TRADES_FILE)
    settled = settle_by_ticker(rows)
    added = open_new_trades(rows)
    save_rows(TRADES_FILE, rows, FIELDS)
    print(f"New: {added} | Newly settled: {settled}")
    print(summary("Longshot fade", rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
