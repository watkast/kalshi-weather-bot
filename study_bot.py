"""1-cent study: catch every sports team / outcome that drops to 1 cent,
paper-buy it, and record exactly what the price does until the game ends.

How it works
------------
* Every 30 min it scans every Kalshi sports "game" / "match" winner series
  (MLB, NFL, NHL, NBA, soccer worldwide, tennis, esports, cricket, ...).
* Every ~10 s it checks the markets of games that are underway. When a
  market's YES price hits 1 cent it logs a paper buy of 100 contracts.
* For ~30 major leagues ESPN's live scoreboard confirms the game is still
  being played ("verified"). Other leagues are logged as "unverified" and
  kept separate on the dashboard, because we can't rule out that the game
  had already ended.
* After the market settles it downloads Kalshi's own records for the bet:
  every trade from the first 1-cent trade onward (study/ticks/) and the
  minute-by-minute bid/ask (study/candles/), then works out the metrics.
"""
import csv
import os
import re
import subprocess
import sys
import time
import unicodedata
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import requests

from common import HERE, fee_per_contract, get_markets, kalshi_get, price

DIR = os.path.join(HERE, "study")
BETS_FILE = os.path.join(DIR, "bets.csv")
ENTRY = 0.01
CONTRACTS = 5
POLL_SECONDS = 10
SCAN_MINUTES = 30
ESPN_SECONDS = 30
SAVE_MINUTES = 10
RUN_MINUTES = float(os.environ.get("RUN_MINUTES", "350"))
TARGETS = [0.02, 0.03, 0.05, 0.10, 0.25, 0.50]
ET = ZoneInfo("America/New_York")

SERIES_RE = re.compile(r"(GAME|MATCH)$")
SERIES_SKIP = ("EXACT", "BOWL", "HOMEGAME", "1STHOME")

ESPN = "https://site.api.espn.com/apis/site/v2/sports"
ESPN_LEAGUES = {
    "KXMLBGAME": "baseball/mlb", "KXNFLGAME": "football/nfl", "KXNHLGAME": "hockey/nhl",
    "KXNBAGAME": "basketball/nba", "KXWNBAGAME": "basketball/wnba",
    "KXNCAAFGAME": "football/college-football", "KXCFLGAME": "football/cfl",
    "KXNCAAMBGAME": "basketball/mens-college-basketball",
    "KXNCAAWBGAME": "basketball/womens-college-basketball",
    "KXMLSGAME": "soccer/usa.1", "KXNWSLGAME": "soccer/usa.nwsl", "KXUSLGAME": "soccer/usa.usl.1",
    "KXEPLGAME": "soccer/eng.1", "KXEFLCHAMPIONSHIPGAME": "soccer/eng.2",
    "KXEFLL1GAME": "soccer/eng.3", "KXEFLL2GAME": "soccer/eng.4",
    "KXLALIGAGAME": "soccer/esp.1", "KXLALIGA2GAME": "soccer/esp.2",
    "KXSERIEAGAME": "soccer/ita.1", "KXBUNDESLIGAGAME": "soccer/ger.1",
    "KXBUNDESLIGA2GAME": "soccer/ger.2", "KXLIGUE1GAME": "soccer/fra.1",
    "KXLIGAMXGAME": "soccer/mex.1", "KXEREDIVISIEGAME": "soccer/ned.1",
    "KXBRASILEIROGAME": "soccer/bra.1", "KXUCLGAME": "soccer/uefa.champions",
    "KXUELGAME": "soccer/uefa.europa", "KXUECLGAME": "soccer/uefa.europa.conf",
    "KXUEFANLGAME": "soccer/uefa.nations", "KXINTLFRIENDLYGAME": "soccer/fifa.friendly",
    "KXCONCACAFNLGAME": "soccer/concacaf.nations.league",
    "KXUCLWGAME": "soccer/uefa.wchampions",
}
CODE_ALIASES = {"AZ": "ARI", "CHW": "CWS", "JAX": "JAC", "WSH": "WAS", "UTAH": "UTA"}
STOPWORDS = {"fc", "cf", "sc", "afc", "cd", "ac", "the", "club", "bc", "kk", "hc"}

BET_FIELDS = [
    "detected_at", "league", "series", "event", "ticker", "pick", "verified",
    "situation_at_entry", "entry_price", "contracts", "entry_fee", "status",
    "result", "pnl_hold", "game_end_at", "end_source", "first_1c_trade_at",
    "detect_lag_s", "minutes_to_end", "peak_bid", "peak_bid_min", "peak_trade",
    *[f"min_to_{int(t * 100)}c" for t in TARGETS], "contracts_traded_at_1c",
    "trades_after_1c", "data",
]


# ---------------------------------------------------------------- helpers
def now_utc():
    return datetime.now(timezone.utc)


def iso(dt):
    return dt.isoformat(timespec="seconds") if dt else ""


def parse_ts(s):
    if not s:
        return None
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    s = s.replace("&", " and ").replace("reg time:", "")
    tokens = [t for t in re.split(r"[^a-z0-9]+", s) if t and t not in STOPWORDS]
    return " ".join(tokens)


def canon_code(c):
    c = (c or "").upper()
    return CODE_ALIASES.get(c, c)


def start_estimate(m):
    """Game start: the ET time inside the ticker if it has one, else ~3.5h
    before Kalshi's expected finish."""
    mt = re.search(r"-(\d{2}[A-Z]{3}\d{2})(\d{4})", m["ticker"])
    if mt:
        try:
            d = datetime.strptime(mt.group(1) + mt.group(2), "%y%b%d%H%M")
            return d.replace(tzinfo=ET).astimezone(timezone.utc)
        except ValueError:
            pass
    exp = parse_ts(m.get("expected_expiration_time") or m.get("occurrence_datetime"))
    return exp - timedelta(hours=3, minutes=30) if exp else None


def load_bets():
    if not os.path.exists(BETS_FILE):
        return []
    with open(BETS_FILE, newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(path, rows, fields):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def git_save():
    subprocess.run(["git", "add", "study"], cwd=HERE, capture_output=True)
    if subprocess.run(["git", "commit", "-q", "-m", "1-cent study update"],
                      cwd=HERE, capture_output=True).returncode != 0:
        return
    for _ in range(3):
        subprocess.run(["git", "pull", "-q", "--rebase"], cwd=HERE, capture_output=True)
        if subprocess.run(["git", "push", "-q"], cwd=HERE, capture_output=True).returncode == 0:
            return
        time.sleep(3)


# ---------------------------------------------------------------- ESPN
class Scoreboards:
    """Cached ESPN scoreboards, used to confirm a game is still being played."""

    def __init__(self):
        self.cache = {}   # path -> (fetched_at, games)
        self.links = {}   # kalshi event -> (path, espn game id)

    def games(self, path):
        hit = self.cache.get(path)
        if hit and time.time() - hit[0] < ESPN_SECONDS:
            return hit[1]
        games = {}
        today = datetime.now(ET).date()
        for d in (today - timedelta(days=1), today, today + timedelta(days=1)):
            try:
                r = requests.get(f"{ESPN}/{path}/scoreboard",
                                 params={"dates": d.strftime("%Y%m%d")}, timeout=15)
                if r.status_code != 200:
                    continue
                for ev in r.json().get("events", []):
                    comp = ev["competitions"][0]
                    st = comp.get("status") or ev.get("status") or {}
                    teams = []
                    for c in sorted(comp.get("competitors", []), key=lambda c: c.get("homeAway") != "away"):
                        t = c.get("team", {})
                        teams.append({
                            "code": canon_code(t.get("abbreviation")),
                            "names": [norm(t.get(k)) for k in
                                      ("displayName", "shortDisplayName", "name", "location")
                                      if t.get(k)],
                            "abbr": t.get("abbreviation", ""), "score": c.get("score", ""),
                        })
                    games[ev["id"]] = {
                        "state": st.get("type", {}).get("state", ""),
                        "detail": st.get("type", {}).get("shortDetail")
                                  or st.get("type", {}).get("description", ""),
                        "teams": teams,
                    }
            except Exception as exc:
                print(f"ESPN {path}: {exc}")
        self.cache[path] = (time.time(), games)
        return games

    @staticmethod
    def team_matches(name, code, team):
        n = norm(name)
        if code and canon_code(code) == team["code"]:
            return 2
        for v in team["names"]:
            if n and (n == v or (len(n) >= 4 and len(v) >= 4 and (n in v or v in n))):
                return 1
        return 0

    def find(self, series, event, picks):
        """picks: [(team name, ticker code)] for the event's non-tie markets."""
        path = ESPN_LEAGUES.get(series)
        if not path:
            return None
        if event in self.links:
            p, gid = self.links[event]
            g = self.games(p).get(gid)
            return g
        best, best_score = None, 0
        for gid, g in self.games(path).items():
            if len(g["teams"]) != 2 or len(picks) < 2:
                continue
            a = [self.team_matches(n, c, g["teams"][0]) for n, c in picks[:2]]
            b = [self.team_matches(n, c, g["teams"][1]) for n, c in picks[:2]]
            score = max(a[0] and b[1] and a[0] + b[1], a[1] and b[0] and a[1] + b[0])
            if score and score > best_score:
                best, best_score = gid, score
        if best:
            self.links[event] = (path, best)
            return self.games(path)[best]
        return None


def situation(g):
    if not g:
        return ""
    score = " - ".join(f"{t['abbr']} {t['score']}" for t in g["teams"])
    return f"{g['detail']} · {score}"


# ---------------------------------------------------------------- Kalshi data
def all_trades(ticker, min_ts, max_ts):
    trades, cursor = [], None
    for _ in range(100):
        q = {"ticker": ticker, "limit": 1000, "min_ts": min_ts, "max_ts": max_ts}
        if cursor:
            q["cursor"] = cursor
        data = kalshi_get("/markets/trades", q)
        trades += data.get("trades", [])
        cursor = data.get("cursor")
        if not cursor:
            break
        time.sleep(0.1)
    trades.sort(key=lambda t: t["created_time"])
    return trades


def candles(series, ticker, start_ts, end_ts):
    out = []
    step = 4000 * 60
    t = start_ts
    while t < end_ts:
        data = kalshi_get(f"/series/{series}/markets/{ticker}/candlesticks",
                          {"start_ts": t, "end_ts": min(end_ts, t + step), "period_interval": 1})
        out += data.get("candlesticks", [])
        t += step
        time.sleep(0.1)
    return out


def d(obj, *keys):
    for k in keys:
        obj = (obj or {}).get(k)
    try:
        return float(obj) if obj not in (None, "") else None
    except (TypeError, ValueError):
        return None


def finalize(bet, market):
    """Download the trade tape and minute bars, then compute the bet's metrics."""
    ticker, series = bet["ticker"], bet["series"]
    detected = parse_ts(bet["detected_at"])
    close = parse_ts(market.get("close_time")) or now_utc()
    game_end = parse_ts(bet.get("game_end_at"))
    if not game_end:
        bet["end_source"] = "approx (market close)"
    end = game_end or close
    start = int((detected - timedelta(hours=6)).timestamp())

    trades = all_trades(ticker, start, int(close.timestamp()) + 60)
    first_1c = next((t for t in trades
                     if (d(t, "yes_price_dollars") or 1) <= ENTRY
                     and parse_ts(t["created_time"]) <= detected + timedelta(seconds=60)), None)
    t0 = parse_ts(first_1c["created_time"]) if first_1c else detected
    tape = [t for t in trades if parse_ts(t["created_time"]) >= t0]
    write_csv(os.path.join(DIR, "ticks", f"{ticker}.csv"),
              [{"time": t["created_time"], "yes_price": t.get("yes_price_dollars"),
                "contracts": t.get("count_fp", t.get("count")), "taker": t.get("taker_side")}
               for t in tape], ["time", "yes_price", "contracts", "taker"])

    bars = candles(series, ticker, int(t0.timestamp()) - 60, int(close.timestamp()) + 60)
    rows = []
    for c in bars:
        ts = datetime.fromtimestamp(c["end_period_ts"], timezone.utc)
        rows.append({"minute_end": iso(ts),
                     "bid_high": d(c, "yes_bid", "high_dollars"), "bid_close": d(c, "yes_bid", "close_dollars"),
                     "ask_low": d(c, "yes_ask", "low_dollars"), "ask_close": d(c, "yes_ask", "close_dollars"),
                     "last": d(c, "price", "close_dollars"), "volume": c.get("volume_fp", c.get("volume"))})
    write_csv(os.path.join(DIR, "candles", f"{ticker}.csv"), rows,
              ["minute_end", "bid_high", "bid_close", "ask_low", "ask_close", "last", "volume"])

    # Metrics measured from our entry until the game ended.
    live = [r for r in rows
            if parse_ts(r["minute_end"]) - timedelta(minutes=1) >= detected
            and parse_ts(r["minute_end"]) - timedelta(minutes=1) <= end]
    peak, peak_at = 0.0, None
    first_hit = {}
    for r in live:
        b = r["bid_high"] or 0
        at = (parse_ts(r["minute_end"]) - detected).total_seconds() / 60  # minute fully after buy
        if b > peak:
            peak, peak_at = b, at
        for tgt in TARGETS:
            if b >= tgt - 1e-9 and tgt not in first_hit:
                first_hit[tgt] = max(at, 0)
    live_trades = [t for t in tape if detected <= parse_ts(t["created_time"]) <= end]
    bet.update({
        "first_1c_trade_at": iso(t0) if first_1c else "",
        "detect_lag_s": f"{(detected - t0).total_seconds():.0f}" if first_1c else "",
        "minutes_to_end": f"{(end - detected).total_seconds() / 60:.1f}",
        "peak_bid": f"{peak:.2f}", "peak_bid_min": f"{peak_at:.1f}" if peak_at is not None else "",
        "peak_trade": f"{max((d(t, 'yes_price_dollars') or 0) for t in live_trades):.2f}" if live_trades else "",
        "contracts_traded_at_1c": f"{sum(d(t, 'count_fp') or d(t, 'count') or 0 for t in live_trades if (d(t, 'yes_price_dollars') or 1) <= ENTRY):.0f}",
        "trades_after_1c": len(tape),
        "data": "complete",
    })
    for tgt in TARGETS:
        v = first_hit.get(tgt)
        bet[f"min_to_{int(tgt * 100)}c"] = f"{v:.1f}" if v is not None else ""


# ---------------------------------------------------------------- watcher
class Study:
    def __init__(self):
        self.bets = load_bets()
        self.by_ticker = {b["ticker"]: b for b in self.bets}
        self.markets = {}      # ticker -> meta for games in or near play
        self.events = {}       # event -> [(name, code)]
        self.series_names = {}
        self.espn = Scoreboards()
        self.last_scan = 0.0
        self.batch_ok = True
        self.errors = []
        self.espn_check = {}

    def scan(self):
        try:
            series = kalshi_get("/series", {"category": "Sports"}).get("series", [])
        except Exception as exc:
            print(f"series scan failed: {exc}")
            return
        wanted = [s for s in series if SERIES_RE.search(s["ticker"])
                  and not any(k in s["ticker"] for k in SERIES_SKIP)]
        self.series_names = {s["ticker"]: s.get("title", s["ticker"]) for s in wanted}
        now = now_utc()
        markets, events = {}, {}
        for s in wanted:
            try:
                ms = get_markets(max_pages=5, series_ticker=s["ticker"], status="open")
            except Exception as exc:
                print(f"{s['ticker']}: {exc}")
                continue
            time.sleep(0.05)
            for m in ms:
                st = start_estimate(m)
                if st is None or st > now + timedelta(minutes=SCAN_MINUTES + 5):
                    continue
                if st < now - timedelta(hours=14):
                    continue
                ev = m.get("event_ticker") or m["ticker"].rsplit("-", 1)[0]
                markets[m["ticker"]] = {"series": s["ticker"], "event": ev, "start": st,
                                        "pick": m.get("yes_sub_title") or m.get("title", ""),
                                        "exp": parse_ts(m.get("expected_expiration_time"))}
                sub = norm(m.get("yes_sub_title", ""))
                if sub not in ("tie", "draw tie", "draw"):
                    events.setdefault(ev, []).append((m.get("yes_sub_title", ""),
                                                      m["ticker"].rsplit("-", 1)[-1]))
        self.markets, self.events = markets, events
        self.last_scan = time.time()
        print(f"scan: {len(wanted)} series, {len(markets)} markets in/near play")
        self.check_espn(now)

    def check_espn(self, now):
        """Link every started game in an ESPN league now, so status.json shows
        whether matching works before any 1-cent moment happens."""
        started = {}
        for m in self.markets.values():
            if m["series"] in ESPN_LEAGUES and m["start"] <= now:
                started[m["event"]] = m["series"]
        matched, missed = 0, []
        for ev, series in started.items():
            try:
                g = self.espn.find(series, ev, self.events.get(ev, []))
            except Exception as exc:
                g = None
                self.errors.append(f"{iso(now)} espn {ev}: {exc}")
            if g:
                matched += 1
            else:
                missed.append(ev)
        self.espn_check = {"at": iso(now), "started_games": len(started),
                           "matched": matched, "unmatched_sample": missed[:10]}
        print(f"ESPN check: {matched}/{len(started)} started games matched")

    def fetch_live(self):
        now = now_utc()
        tickers = [t for t, m in self.markets.items() if m["start"] <= now + timedelta(minutes=2)]
        out = {}
        if self.batch_ok:
            for i in range(0, len(tickers), 50):
                chunk = tickers[i:i + 50]
                try:
                    data = kalshi_get("/markets", {"tickers": ",".join(chunk), "limit": 1000})
                    got = data.get("markets", [])
                    if chunk and not got and i == 0 and len(tickers) > 5:
                        raise ValueError("batch lookup returned nothing")
                    out.update({m["ticker"]: m for m in got})
                except Exception as exc:
                    print(f"batch lookup off ({exc}); using per-event lookups")
                    self.batch_ok, out = False, {}
                    break
        if not self.batch_ok:
            for ev in {self.markets[t]["event"] for t in tickers}:
                try:
                    for m in get_markets(max_pages=1, event_ticker=ev):
                        out[m["ticker"]] = m
                except Exception as exc:
                    print(f"{ev}: {exc}")
        return out

    def poll(self):
        now = now_utc()
        live = self.fetch_live()
        for ticker, m in live.items():
            meta = self.markets.get(ticker)
            if not meta or ticker in self.by_ticker:
                continue
            if m.get("status") not in ("active", "open"):
                continue
            ask = price(m, "yes_ask")
            if ask is None or not (0 < ask <= ENTRY):
                continue
            g = None
            if meta["series"] in ESPN_LEAGUES:
                g = self.espn.find(meta["series"], meta["event"], self.events.get(meta["event"], []))
                if g and g["state"] != "in":
                    continue          # not started or already over
            verified = "yes" if g else "no"
            if not g and meta["exp"] and now > meta["exp"] + timedelta(minutes=20):
                continue              # probably finished; skip
            fee = fee_per_contract(ask, CONTRACTS)
            bet = {"detected_at": iso(now), "league": self.series_names.get(meta["series"], meta["series"]),
                   "series": meta["series"], "event": meta["event"], "ticker": ticker,
                   "pick": meta["pick"], "verified": verified, "situation_at_entry": situation(g),
                   "entry_price": f"{ask:.2f}", "contracts": CONTRACTS, "entry_fee": f"{fee * CONTRACTS:.2f}",
                   "status": "open", "end_source": "ESPN final" if g else "", "data": "pending"}
            self.bets.append(bet)
            self.by_ticker[ticker] = bet
            print(f"BUY {ticker} ({bet['league']}, {meta['pick']}) verified={verified} {bet['situation_at_entry']}")

        # Watch verified games for the final whistle.
        for b in self.bets:
            if b["status"] == "open" and b["verified"] == "yes" and not b.get("game_end_at"):
                g = self.espn.find(b["series"], b["event"], self.events.get(b["event"], []))
                if g and g["state"] == "post":
                    b["game_end_at"] = iso(now)

        # Finished markets: settle and download the full price history.
        for b in self.bets:
            if b["status"] == "settled" and b.get("data") == "complete":
                continue
            if b["ticker"] in live and live[b["ticker"]].get("status") in ("active", "open"):
                continue
            if b.get("_checked") and time.time() - b["_checked"] < 300:
                continue
            b["_checked"] = time.time()
            try:
                m = kalshi_get(f"/markets/{b['ticker']}")["market"]
            except Exception as exc:
                print(f"{b['ticker']}: {exc}")
                continue
            if m.get("result") not in ("yes", "no", "void"):
                continue
            n, cost = int(b["contracts"]), float(b["entry_price"]) * int(b["contracts"]) + float(b["entry_fee"])
            payout = n if m["result"] == "yes" else (n * float(b["entry_price"]) if m["result"] == "void" else 0)
            b.update(status="settled", result=m["result"], pnl_hold=f"{payout - cost:.2f}")
            try:
                finalize(b, m)
                print(f"FINAL {b['ticker']} result={m['result']} peak={b['peak_bid']}")
            except Exception as exc:
                b["data"] = "retry"
                print(f"{b['ticker']}: history download failed ({exc})")
                self.errors.append(f"{iso(now_utc())} {b['ticker']} history: {exc}")

    def save(self):
        write_csv(BETS_FILE, self.bets, BET_FIELDS)
        import json
        status = {"saved_at": iso(now_utc()), "series_watched": len(self.series_names),
                  "markets_in_or_near_play": len(self.markets),
                  "batch_lookup": self.batch_ok, "espn_games_linked": len(self.espn.links),
                  "espn_check": self.espn_check,
                  "bets": len(self.bets), "open": sum(1 for b in self.bets if b["status"] == "open"),
                  "errors": self.errors[-15:]}
        with open(os.path.join(DIR, "status.json"), "w") as fh:
            json.dump(status, fh, indent=1)


def main():
    study = Study()
    end = time.time() + RUN_MINUTES * 60
    last_save = time.time()
    while time.time() < end:
        if time.time() - study.last_scan >= SCAN_MINUTES * 60:
            study.scan()
        try:
            study.poll()
        except Exception as exc:
            print(f"poll failed: {exc}")
            study.errors.append(f"{iso(now_utc())} poll: {exc}")
        if time.time() - last_save >= SAVE_MINUTES * 60:
            study.save()
            git_save()
            last_save = time.time()
        time.sleep(POLL_SECONDS)
    study.save()
    open_n = sum(1 for b in study.bets if b["status"] == "open")
    print(f"1¢ study: {len(study.bets)} bets, {open_n} still in play")
    return 0


if __name__ == "__main__":
    sys.exit(main())
