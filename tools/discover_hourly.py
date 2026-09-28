import json, sys, time
sys.path.insert(0, ".")
from common import kalshi_get, get_markets
out=[]; p=lambda *a: out.append(" ".join(str(x) for x in a))
series = kalshi_get("/series", {}).get("series", [])
hourly = [s for s in series if s.get("frequency") == "hourly" and s.get("category") in ("Crypto", "Financials", "Commodities")]
p("HOURLY SERIES", len(hourly))
for s in sorted(hourly, key=lambda s: s["ticker"]):
    ms = get_markets(max_pages=1, series_ticker=s["ticker"], status="open")
    evs = sorted({m["event_ticker"] for m in ms})
    p(f"\n== {s['ticker']} | {s.get('title')} | cat={s.get('category')} | open={len(ms)} events={evs[:3]}")
    for m in ms[:2]:
        p("  ", json.dumps({k: m.get(k) for k in ("ticker","title","yes_sub_title","strike_type","floor_strike","cap_strike","open_time","close_time","yes_bid_dollars","yes_ask_dollars","volume_fp","rules_primary")})[:600])
    time.sleep(0.1)
open("discovery_hourly.txt","w").write("\n".join(out)+"\n"); print("\n".join(out))
