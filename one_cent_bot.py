"""Paper bot: buy NFL / NHL teams at 1 cent and hold to the final whistle.

Same idea as mlb_bot.py, for other sports. Watches Kalshi's game-winner
markets about every 30 seconds. When a team's YES price hits 1 cent while
ESPN's live scoreboard shows the game still in progress, it logs a paper
buy and records the price every minute until the game ends.

Each sport gets its own files: <sport>_trades.csv and <sport>_price_log.csv.
Choose sports with the SPORTS env var, e.g. SPORTS="NFL,NHL".
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

MAX_ENTRY = 0.01
CONTRACTS = 100         # $1 per bet at 1 cent
POLL_SECONDS = 30
SNAPSHOT_SECONDS = 60
SAVE_MINUTES = 30
RUN_MINUTES = float(os.environ.get("RUN_MINUTES", "345"))

ESPN = "https://site.api.espn.com/apis/site/v2/sports"
SPORTS = {
    "NFL": {"series": "KXNFLGAME", "espn": "football/nfl",
            "aliases": {"JAX": "JAC", "WSH": "WAS", "LA": "LAR"}},
    "NHL": {"series": "KXNHLGAME", "espn": "hockey/nhl",
            "aliases": {"UTAH": "UTA", "LAK": "LA", "SJS": "SJ", "NJD": "NJ",
                        "TBL": "TB", "VEG": "VGK"}},
}

TRADE_FIELDS = ["logged_at", "sport", "ticker", "team", "game", "period_at_entry",
                "score_at_entry", "side", "price", "fee", "contracts",
                "peak_bid", "status", "result", "pnl"]
PRICE_FIELDS = ["time", "sport", "ticker", "yes_bid", "yes_ask", "last_price",
                "period", "score", "game_state"]


def files(sport):
    s = sport.lower()
    return f"{HERE}/{s}_trades.csv", f"{HERE}/{s}_price_log.csv"


def canon(sport, code):
    code = (code or "").upper()
    return SPORTS[sport]["aliases"].get(code, code)


def live_games(sport):
    """Return {team code: game info} from ESPN for yesterday and today (US Eastern)."""
    today = datetime.now(ZoneInfo("America/New_York")).date()
    games = {}
    for d in (today - timedelta(days=1), today):
        r = requests.get(f"{ESPN}/{SPORTS[sport]['espn']}/scoreboard",
                         params={"dates": d.strftime("%Y%m%d")}, timeout=20)
        r.raise_for_status()
        for ev in r.json().get("events", []):
            comp = ev["competitions"][0]
            st = comp.get("status", ev.get("status", {}))
            teams = sorted(comp["competitors"], key=lambda c: c.get("homeAway") != "away")
            info = {
                "live": st.get("type", {}).get("state") == "in",
                "state": st.get("type", {}).get("description", ""),
                "period": f"P{st.get('period', '')} {st.get('displayClock', '')}".strip(),
                "score": " - ".join(f"{c['team'].get('abbreviation')} {c.get('score', '0')}"
                                    for c in teams),
            }
            for c in teams:
                code = canon(sport, c["team"].get("abbreviation"))
                if code not in games or info["live"]:
                    games[code] = info
    return games


def team_of(ticker):
    return ticker.rsplit("-", 1)[-1].upper()


def git_save(paths):
    names = [os.path.basename(p) for p in paths if os.path.exists(p)]
    if not names:
        return
    subprocess.run(["git", "add", *names], cwd=HERE, capture_output=True)
    if subprocess.run(["git", "commit", "-q", "-m", "1-cent bot update"],
                      cwd=HERE, capture_output=True).returncode != 0:
        return
    subprocess.run(["git", "pull", "-q", "--rebase"], cwd=HERE, capture_output=True)
    subprocess.run(["git", "push", "-q"], cwd=HERE, capture_output=True)


class SportWatcher:
    def __init__(self, sport):
        self.sport = sport
        self.trades_file, self.prices_file = files(sport)
        self.trades = load_rows(self.trades_file)
        self.prices = load_rows(self.prices_file)
        self.held = {t["ticker"] for t in self.trades}
        self.unmatched = set()
        self.last_snap = self.last_settle = 0.0

    def poll(self):
        now = datetime.now(timezone.utc)
        markets = {m["ticker"]: m for m in
                   get_markets(series_ticker=SPORTS[self.sport]["series"], status="open")}
        cheap = [m for m in markets.values()
                 if m["ticker"] not in self.held and price(m, "yes_ask") is not None
                 and 0 < price(m, "yes_ask") <= MAX_ENTRY]
        watching = [t for t in self.trades if t["status"] == "open" and t["ticker"] in markets]
        games = {}
        if cheap or watching:
            try:
                games = live_games(self.sport)
            except Exception as exc:
                print(f"{self.sport} scoreboard failed: {exc}")

        for m in cheap:
            g = games.get(team_of(m["ticker"]))
            if not g:
                if games and m["ticker"] not in self.unmatched:
                    print(f"{self.sport}: no game matched for {m['ticker']}; skipping")
                    self.unmatched.add(m["ticker"])
                continue
            if not g["live"]:
                continue
            ask = price(m, "yes_ask")
            fee = fee_per_contract(ask, CONTRACTS)
            self.trades.append({
                "logged_at": now.isoformat(timespec="seconds"), "sport": self.sport,
                "ticker": m["ticker"], "team": team_of(m["ticker"]),
                "game": m.get("event_ticker", ""), "period_at_entry": g["period"],
                "score_at_entry": g["score"], "side": "yes", "price": f"{ask:.2f}",
                "fee": f"{fee:.4f}", "contracts": CONTRACTS,
                "peak_bid": f"{price(m, 'yes_bid') or 0:.2f}",
                "status": "open", "result": "", "pnl": ""})
            self.held.add(m["ticker"])
            print(f"{self.sport} PAPER BUY {CONTRACTS} YES {m['ticker']} @ {ask:.2f} "
                  f"({g['period']}, {g['score']})")

        snap = time.time() - self.last_snap >= SNAPSHOT_SECONDS
        for t in self.trades:
            m = markets.get(t["ticker"])
            if t["status"] != "open" or not m:
                continue
            bid = price(m, "yes_bid") or 0
            if bid > float(t["peak_bid"] or 0):
                t["peak_bid"] = f"{bid:.2f}"
            if snap:
                g = games.get(t["team"], {})
                last = price(m, "last_price")
                self.prices.append({
                    "time": now.isoformat(timespec="seconds"), "sport": self.sport,
                    "ticker": t["ticker"], "yes_bid": f"{bid:.2f}",
                    "yes_ask": f"{price(m, 'yes_ask') or 0:.2f}",
                    "last_price": f"{last:.2f}" if last is not None else "",
                    "period": g.get("period", ""), "score": g.get("score", ""),
                    "game_state": g.get("state", "")})
        if snap:
            self.last_snap = time.time()

        if time.time() - self.last_settle >= 300:
            waiting = [t for t in self.trades if t["status"] == "open" and t["ticker"] not in markets]
            if waiting and settle_by_ticker(waiting):
                print(summary(f"{self.sport} 1-cent", self.trades))
            self.last_settle = time.time()

    def save(self):
        save_rows(self.trades_file, self.trades, TRADE_FIELDS)
        save_rows(self.prices_file, self.prices, PRICE_FIELDS)
        return [self.trades_file, self.prices_file]


def main():
    wanted = [s.strip().upper() for s in os.environ.get("SPORTS", "NFL,NHL").split(",")]
    watchers = [SportWatcher(s) for s in wanted if s in SPORTS]
    end = time.time() + RUN_MINUTES * 60
    last_save = time.time()
    while time.time() < end:
        for w in watchers:
            try:
                w.poll()
            except Exception as exc:
                print(f"{w.sport} poll failed: {exc}")
        if time.time() - last_save >= SAVE_MINUTES * 60:
            git_save([p for w in watchers for p in w.save()])
            last_save = time.time()
        time.sleep(POLL_SECONDS)

    for w in watchers:
        settle_by_ticker(w.trades)
        w.save()
    for w in watchers:
        print(summary(f"{w.sport} 1-cent", w.trades))
    return 0


if __name__ == "__main__":
    sys.exit(main())
