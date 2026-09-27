"""One-off scan: Kalshi sports game-winner series, sample markets, ESPN team codes."""
import json, re, sys, requests
sys.path.insert(0, ".")
from common import kalshi_get, get_markets
out = []
def p(*a): out.append(" ".join(str(x) for x in a))
series = kalshi_get("/series", {"category": "Sports"}).get("series", [])
p("TOTAL SPORTS SERIES", len(series))
game = [s for s in series if re.search(r"(GAME|MATCH)$", s["ticker"])]
p("GAME/MATCH SERIES", len(game))
for s in sorted(game, key=lambda s: s["ticker"]):
    try:
        ms = get_markets(max_pages=1, series_ticker=s["ticker"], status="open")
    except Exception as e:
        ms = []; p("ERR", s["ticker"], e)
    ex = ms[0] if ms else {}
    p(f"{s['ticker']:28} open={len(ms):4} | {s.get('title','')[:40]} | ex={ex.get('ticker','')} "
      f"sub={ex.get('yes_sub_title','')!r} title={ex.get('title','')!r}")
p("")
ESPN = {"mlb": "baseball/mlb", "nfl": "football/nfl", "nhl": "hockey/nhl", "nba": "basketball/nba",
        "wnba": "basketball/wnba", "ncaaf": "football/college-football",
        "ncaamb": "basketball/mens-college-basketball", "mls": "soccer/usa.1", "epl": "soccer/eng.1",
        "laliga": "soccer/esp.1", "seriea": "soccer/ita.1", "bundesliga": "soccer/ger.1",
        "ligue1": "soccer/fra.1", "ucl": "soccer/uefa.champions", "atp": "tennis/atp", "wta": "tennis/wta"}
for k, path in ESPN.items():
    try:
        r = requests.get(f"https://site.api.espn.com/apis/site/v2/sports/{path}/scoreboard", timeout=20).json()
        evs = r.get("events", [])
        teams = []
        for ev in evs[:12]:
            for c in ev.get("competitions", [{}])[0].get("competitors", []):
                t = c.get("team") or c.get("athlete") or {}
                teams.append(f"{t.get('abbreviation','?')}/{t.get('location', t.get('displayName',''))}")
        p(f"ESPN {k:10} events={len(evs):3} {' '.join(teams[:24])}")
    except Exception as e:
        p("ESPN ERR", k, e)
open("discovery.txt", "w").write("\n".join(out) + "\n")
print("\n".join(out))
