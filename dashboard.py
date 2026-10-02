"""Builds README.md as a results dashboard from all the bots' CSV logs.

GitHub shows README.md on the repository's home page, so opening
github.com/<you>/kalshi-weather-bot shows the latest results.
"""
import csv
import os
from collections import defaultdict
from datetime import datetime
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))

BOTS = [  # (label, file, what it does)
    ("Temperature", "trades.csv", "NWS forecast high vs Kalshi daily high brackets (7 cities)"),
    ("Rain", "rain_trades.csv", "NWS hourly rain chance vs Kalshi \"Will it rain?\" (28 cities)"),
    ("Longshot fade", "longshot_trades.csv", "Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27)"),
]

# Longshot bets grouped by Kalshi series prefix
CATEGORIES = [
    ("NFL", ("KXNFL",)), ("College football", ("KXNCAAF",)), ("MLB", ("KXMLB",)),
    ("NHL", ("KXNHL",)), ("NBA / WNBA", ("KXNBA", "KXWNBA")),
    ("College basketball", ("KXNCAAB", "KXNCAAMB", "KXNCAAWB")),
    ("Soccer", ("KXEPL", "KXUCL", "KXLALIGA", "KXSERIEA", "KXBUNDES", "KXLIGUE", "KXMLS",
                "KXINTLFRIENDLY", "KXSOCCER", "KXFIFA", "KXWC")),
    ("Tennis", ("KXATP", "KXWTA", "KXTENNIS")), ("Golf", ("KXPGA", "KXGOLF", "KXLIV")),
    ("UFC / boxing", ("KXUFC", "KXBOX", "KXMMA")),
    ("Crypto", ("KXBTC", "KXETH", "KXSOL", "KXXRP", "KXDOGE", "KXCRYPTO")),
    ("Weather", ("KXHIGH", "KXLOW", "KXRAIN", "KXSNOW")),
]


def load(name):
    path = os.path.join(HERE, name)
    if not os.path.exists(path):
        return []
    with open(path, newline="") as fh:
        return list(csv.DictReader(fh))


def money(x):
    return f"-${abs(x):,.2f}" if x < 0 else f"${x:,.2f}"


def stats(rows):
    done = [r for r in rows if r.get("status") == "settled"]
    pnl = sum(float(r["pnl"] or 0) for r in done)
    risked = sum(int(r["contracts"]) * (float(r["price"]) + float(r["fee"])) for r in done)
    wins = sum(1 for r in done if float(r["pnl"] or 0) > 0)
    return {
        "bets": len(rows), "settled": len(done), "open": len(rows) - len(done),
        "wins": wins, "win_rate": f"{wins / len(done):.0%}" if done else "—",
        "pnl": money(pnl) if done else "—",
        "roi": f"{pnl / risked:+.1%}" if risked else "—",
    }


def category(series):
    for name, prefixes in CATEGORIES:
        if series.startswith(prefixes):
            return name
    return "Other"


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def verdict(s):
    if s["settled"] < 20:
        return "Too early"
    roi = float(s["roi"].strip("%+")) if s["roi"] != "—" else 0
    return "Promising" if roi > 3 else "Losing" if roi < -3 else "Break-even"


def main():
    now = datetime.now(ZoneInfo("America/Denver")).strftime("%a %b %-d, %-I:%M %p MT")
    data = {label: load(f) for label, f, _ in BOTS}
    md = ["# Kalshi Paper Bots — Results", "",
          f"*Updated {now}. Paper money only — no real trades. "
          "Study pages refresh about every 10 minutes; this page every few hours.*", "",
          "### → [1¢ Study dashboard](STUDY.md) — every 1¢ moment across all sports, tracked to the final whistle", "",
          "### → [15-Minute 1¢ Study](FIFTEEN.md) — every 1¢ moment in Kalshi's 15-minute up/down markets", "",
          "### → [Fair-Value Bot](FAIRVALUE.md) — buys 15-minute crypto markets when a model says the price is wrong", "",
          "### → [Gold & Silver Fair-Value Bot](METALS.md) — the same idea on 15-minute gold and silver markets", "",
          "### → [Range-Scalp Bot](SCALP.md) — buys 15-minute crypto sides holding at 55–70¢, sells at +20¢, repeats", "",
          "### → [Momentum Bot](MOMENTUM.md) — buys a 15-minute crypto side right after its price jumps, sells at +5¢ or more", "",
          "## Scoreboard", ""]
    rows = []
    for label, f, _ in BOTS:
        s = stats(data[label])
        rows.append([f"**{label}**", s["bets"], s["settled"], s["win_rate"], s["pnl"],
                     s["roi"], s["open"], verdict(s)])
    md += [table(["Bot", "Bets", "Settled", "Win rate", "Paper P&L", "Return", "Open",
                  "Verdict"], rows), "",
           "*Return = profit ÷ money risked on settled bets. Verdicts need at least 20 "
           "settled bets.*", ""]

    # Longshot fade split by sport / category
    ls = data["Longshot fade"]
    if ls:
        groups = defaultdict(list)
        for r in ls:
            groups[category(r.get("series", ""))].append(r)
        rows = []
        for name in sorted(groups, key=lambda g: -len(groups[g])):
            s = stats(groups[name])
            rows.append([name, s["bets"], s["settled"], s["win_rate"], s["pnl"], s["roi"]])
        md += ["## Longshot fade by category", "",
               table(["Category", "Bets", "Settled", "Win rate", "Paper P&L", "Return"], rows), ""]

    # Retired 1-cent bots (replaced by the 1¢ Study)
    for label in ():
        rows_ = data[label]
        md += [f"## {label} bets", ""]
        if not rows_:
            md += ["*No 1¢ moments caught yet.*", ""]
            continue
        rows = []
        for r in reversed(rows_[-25:]):
            when = r.get("period_at_entry") or r.get("inning_at_entry", "")
            result = {"yes": "✅ Won", "no": "❌ Lost", "void": "Void"}.get(r["result"], "In play")
            rows.append([r["logged_at"][:10], r["team"], f"{when} · {r['score_at_entry']}",
                         f"{float(r['peak_bid'] or 0) * 100:.0f}¢", result,
                         money(float(r["pnl"])) if r["pnl"] else "—"])
        md += [table(["Date", "Team", "Entry situation", "Highest price after", "Result",
                      "P&L"], rows), "",
               "*Highest price after = best price you could have sold at before the end. "
               "Minute-by-minute prices are in the price log files.*", ""]

    # Latest forecast-bot bets
    for label, key in (("Temperature", "bracket"), ("Rain", None)):
        rows_ = data[label]
        if not rows_:
            continue
        rows = []
        for r in reversed(rows_[-10:]):
            what = f"{r['city']} {r[key]}" if key else r["city"]
            result = {"yes": "YES", "no": "NO"}.get(r["result"], "Open")
            rows.append([r["market_date"], what, r["side"].upper(), f"{float(r['price']) * 100:.0f}¢",
                         f"{float(r['model_prob']):.0%}", result,
                         money(float(r["pnl"])) if r["pnl"] else "—"])
        md += [f"## Latest {label.lower()} bets", "",
               table(["Day", "Market", "Bet", "Paid", "Bot's odds", "Outcome", "P&L"], rows), ""]

    md += ["## The bots", "", table(["Bot", "What it does", "Full log"],
                                     [[l, d, f"[{f}]({f})"] for l, f, d in BOTS]), "",
           "Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — "
           "[mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).", "",
           "Run everything now: **Actions → paper-trade → Run workflow**.", ""]

    with open(os.path.join(HERE, "README.md"), "w") as fh:
        fh.write("\n".join(md))
    print("Dashboard updated")


if __name__ == "__main__":
    main()
