"""Paper bot: buy MLB teams at 1 cent and hold to the final out.

Watches Kalshi's MLB game-winner markets (KXMLBGAME) about every 30
seconds. When a team's YES price hits 1 cent while MLB's live feed shows
the game still in progress, it logs a paper buy and then records the
price every minute until the game ends, so we can see how often these
near-dead teams come back and what the price does along the way.
"""
import os
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import requests

from common import (HERE, fee_per_contract, get_markets, load_rows, price,
                    save_rows, settle_by_ticker, summary)

TRADES_FILE = f"{HERE}/mlb_trades.csv"
PRICES_FILE = f"{HERE}/mlb_price_log.csv"

MAX_ENTRY = 0.01        # buy when YES costs 1 cent
CONTRACTS = 100         # $1 per bet at 1 cent
POLL_SECONDS = 30
SNAPSHOT_SECONDS = 60
SAVE_MINUTES = 10
RUN_MINUTES = float(os.environ.get("RUN_MINUTES", "345"))

TRADE_FIELDS = ["logged_at", "ticker", "team", "game", "inning_at_entry",
                "score_at_entry", "side", "price", "fee", "contracts",
                "peak_bid", "status", "result", "pnl"]
PRICE_FIELDS = ["time", "ticker", "yes_bid", "yes_ask", "last_price",
                "inning", "score", "game_state"]

# Different sources spell some teams differently; map them all to one code.
ALIASES = {"AZ": "ARI", "CHW": "CWS", "KCR": "KC", "SDP": "SD", "SFG": "SF",
           "TBR": "TB", "WSN": "WSH", "WAS": "WSH", "OAK": "ATH", "LA": "LAD"}


def canon(code):
    code = (code or "").upper()
    return ALIASES.get(code, code)


def live_games():
    """Return {team code: game info} for today's and yesterday's MLB games."""
    today = datetime.now(ZoneInfo("America/New_York")).date()
    games = {}
    for d in (today - timedelta(days=1), today):
        r = requests.get("https://statsapi.mlb.com/api/v1/schedule",
                         params={"sportId": 1, "date": d.isoformat(),
                                 "hydrate": "team,linescore"}, timeout=20)
        r.raise_for_status()
        for day in r.json().get("dates", []):
            for g in day.get("games", []):
                away, home = g["teams"]["away"], g["teams"]["home"]
                ls = g.get("linescore", {})
                info = {
                    "live": g["status"].get("abstractGameState") == "Live"
                            and g["status"].get("detailedState") not in ("Game Over", "Final"),
                    "state": g["status"].get("detailedState", ""),
                    "inning": f"{ls.get('inningHalf', '')} {ls.get('currentInning', '')}".strip(),
                    "score": f"{away['team'].get('abbreviation')} {away.get('score', 0)}-"
                             f"{home.get('score', 0)} {home['team'].get('abbreviation')}",
                }
                for side in (away, home):
                    code = canon(side["team"].get("abbreviation"))
                    # Keep the live game if a team has two on the list.
                    if code not in games or info["live"]:
                        games[code] = info
    return games


def team_of(ticker):
    """KXMLBGAME-26SEP29NYYBOS-NYY -> 'NYY'."""
    return canon(ticker.rsplit("-", 1)[-1])


def git_save():
    cmds = [["git", "add", "mlb_trades.csv", "mlb_price_log.csv"],
            ["git", "commit", "-q", "-m", "MLB 1-cent bot update"],
            ["git", "pull", "-q", "--rebase"],
            ["git", "push", "-q"]]
    for c in cmds:
        if subprocess.run(c, cwd=HERE, capture_output=True).returncode != 0 and c[1] == "commit":
            return  # nothing new to commit


def main():
    trades = load_rows(TRADES_FILE)
    prices = load_rows(PRICES_FILE)
    held = {t["ticker"]: t for t in trades}
    end = time.time() + RUN_MINUTES * 60
    last_snap = last_save = last_settle = 0.0
    unmatched = set()

    while time.time() < end:
        now = datetime.now(timezone.utc)
        try:
            markets = {m["ticker"]: m for m in get_markets(series_ticker="KXMLBGAME", status="open")}
        except Exception as exc:
            print(f"Kalshi fetch failed: {exc}")
            time.sleep(POLL_SECONDS)
            continue

        cheap = [m for m in markets.values()
                 if m["ticker"] not in held and price(m, "yes_ask") is not None
                 and 0 < price(m, "yes_ask") <= MAX_ENTRY]
        watching = [t for t in trades if t["status"] == "open" and t["ticker"] in markets]
        games = {}
        if cheap or watching:
            try:
                games = live_games()
            except Exception as exc:
                print(f"MLB feed failed: {exc}")

        # New entries: only while the game is actually still being played.
        for m in cheap:
            g = games.get(team_of(m["ticker"]))
            if not g:
                if m["ticker"] not in unmatched:
                    print(f"No MLB game matched for {m['ticker']}; skipping")
                    unmatched.add(m["ticker"])
                continue
            if not g["live"]:
                continue
            ask = price(m, "yes_ask")
            fee = fee_per_contract(ask, CONTRACTS)
            row = {"logged_at": now.isoformat(timespec="seconds"), "ticker": m["ticker"],
                   "team": team_of(m["ticker"]), "game": m.get("event_ticker", ""),
                   "inning_at_entry": g["inning"], "score_at_entry": g["score"],
                   "side": "yes", "price": f"{ask:.2f}", "fee": f"{fee:.4f}",
                   "contracts": CONTRACTS, "peak_bid": f"{price(m, 'yes_bid') or 0:.2f}",
                   "status": "open", "result": "", "pnl": ""}
            trades.append(row)
            held[m["ticker"]] = row
            print(f"PAPER BUY {CONTRACTS} YES {m['ticker']} @ {ask:.2f} ({g['inning']}, {g['score']})")

        # Track the price of every open bet.
        for t in trades:
            m = markets.get(t["ticker"])
            if t["status"] != "open" or not m:
                continue
            bid = price(m, "yes_bid") or 0
            if bid > float(t["peak_bid"] or 0):
                t["peak_bid"] = f"{bid:.2f}"
        if time.time() - last_snap >= SNAPSHOT_SECONDS:
            for t in trades:
                m = markets.get(t["ticker"])
                if t["status"] != "open" or not m:
                    continue
                g = games.get(t["team"], {})
                last = price(m, "last_price")
                prices.append({"time": now.isoformat(timespec="seconds"), "ticker": t["ticker"],
                               "yes_bid": f"{price(m, 'yes_bid') or 0:.2f}",
                               "yes_ask": f"{price(m, 'yes_ask') or 0:.2f}",
                               "last_price": f"{last:.2f}" if last is not None else "",
                               "inning": g.get("inning", ""), "score": g.get("score", ""),
                               "game_state": g.get("state", "")})
            last_snap = time.time()

        # Score finished games.
        if time.time() - last_settle >= 300:
            waiting = [t for t in trades if t["status"] == "open" and t["ticker"] not in markets]
            if waiting and settle_by_ticker(waiting):
                print(summary("MLB 1-cent", trades))
            last_settle = time.time()

        if time.time() - last_save >= SAVE_MINUTES * 60:
            save_rows(TRADES_FILE, trades, TRADE_FIELDS)
            save_rows(PRICES_FILE, prices, PRICE_FIELDS)
            git_save()
            last_save = time.time()

        time.sleep(POLL_SECONDS)

    settle_by_ticker(trades)
    save_rows(TRADES_FILE, trades, TRADE_FIELDS)
    save_rows(PRICES_FILE, prices, PRICE_FIELDS)
    print(summary("MLB 1-cent", trades))
    return 0


if __name__ == "__main__":
    sys.exit(main())
