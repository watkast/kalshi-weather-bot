"""One-off scan: every Kalshi 15-minute series and what its markets look like."""
import json, sys, time
sys.path.insert(0, ".")
from common import kalshi_get, get_markets
out = []
def p(*a): out.append(" ".join(str(x) for x in a))
series = kalshi_get("/series", {}).get("series", [])
p("TOTAL SERIES", len(series))
fifteen = [s for s in series if s.get("frequency") == "fifteen_min" or "15M" in s["ticker"]]
p("15-MIN SERIES", len(fifteen))
for s in sorted(fifteen, key=lambda s: s["ticker"]):
    ms = get_markets(max_pages=1, series_ticker=s["ticker"], status="open")
    p(f"\n== {s['ticker']} | {s.get('title')} | freq={s.get('frequency')} | cat={s.get('category')} | open={len(ms)}")
    p("   settlement:", json.dumps(s.get("settlement_sources", []))[:200])
    evs = sorted({m["event_ticker"] for m in ms})
    p("   events:", evs[:4])
    for m in ms[:3]:
        keep = {k: m.get(k) for k in ("ticker", "title", "yes_sub_title", "strike_type", "floor_strike", "cap_strike",
                                      "open_time", "close_time", "expected_expiration_time", "yes_ask_dollars",
                                      "yes_bid_dollars", "volume_fp", "rules_primary")}
        p("  ", json.dumps(keep)[:700])
    time.sleep(0.1)
# one recently settled BTC market, with trades and candles, to confirm history endpoints
st = get_markets(max_pages=1, series_ticker="KXBTC15M", status="settled")[:1]
if st:
    m = st[0]; p("\nSETTLED SAMPLE", json.dumps({k: m.get(k) for k in ("ticker","open_time","close_time","result","expiration_value","floor_strike")}))
    tr = kalshi_get("/markets/trades", {"ticker": m["ticker"], "limit": 5})
    p("trades sample", json.dumps(tr.get("trades", [])[:2])[:500])
open("discovery15.txt", "w").write("\n".join(out) + "\n")
print("\n".join(out))
