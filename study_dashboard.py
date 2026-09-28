"""Builds STUDY.md (+ charts) from the 1-cent study's data."""
import csv
import math
import os
import statistics
from collections import defaultdict
from datetime import datetime
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(HERE, "study")
CHARTS = os.path.join(DIR, "charts")
TARGETS = [2, 3, 5, 10, 25, 50]
STAKE = 14         # contracts per buy — all P&L on this page is at this size
MIN_BETS = 30      # finished bets a rule needs before we trust it at all
TIME_BUCKETS = [(0, 5, "Under 5 min"), (5, 15, "5–15 min"), (15, 30, "15–30 min"),
                (30, 60, "30–60 min"), (60, 1e9, "Over 60 min")]

# Reference palette (light surface) — see dataviz skill palette.md
SURFACE, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e6e5e1"
BLUE, ORANGE, RED, MUTED = "#2a78d6", "#eb6834", "#e34948", "#b9b8b3"


def fee(p, n):
    return math.ceil(0.07 * n * p * (1 - p) * 100 - 1e-9) / 100


def load():
    path = os.path.join(DIR, "bets.csv")
    if not os.path.exists(path):
        return []
    with open(path, newline="") as fh:
        return list(csv.DictReader(fh))


def f(x, default=None):
    try:
        return float(x)
    except (TypeError, ValueError):
        return default


def enrich(b):
    """Recompute peak and time-to-target from the saved minute bars, using only
    minutes that started after our buy (so nothing from before we owned it)."""
    path = os.path.join(DIR, "candles", f"{b['ticker']}.csv")
    if b.get("data") != "complete" or not os.path.exists(path):
        return b
    t0 = datetime.fromisoformat(b["detected_at"])
    end = f(b.get("minutes_to_end"))
    peak, peak_at, hit = 0.0, None, {}
    with open(path, newline="") as fh:
        for r in csv.DictReader(fh):
            m_end = (datetime.fromisoformat(r["minute_end"]) - t0).total_seconds() / 60
            if m_end - 1 < 0 or (end is not None and m_end - 1 > end):
                continue
            bid = f(r["bid_high"], 0) or 0
            if bid > peak:
                peak, peak_at = bid, m_end
            for t in TARGETS:
                if bid >= t / 100 - 1e-9 and t not in hit:
                    hit[t] = m_end
    b["peak_bid"] = f"{peak:.2f}"
    b["peak_bid_min"] = f"{peak_at:.1f}" if peak_at is not None else ""
    for t in TARGETS:
        b[f"min_to_{t}c"] = f"{hit[t]:.1f}" if t in hit else ""
    return b


def cost(b):
    """Cash to buy STAKE contracts at the entry price, including Kalshi's fee."""
    p = f(b["entry_price"], 0.01)
    return STAKE * p + fee(p, STAKE)


def hold_pnl(b):
    if b.get("result") == "void":
        return 0.0
    return (STAKE if b.get("result") == "yes" else 0) - cost(b)


def exit_pnl(b, target):
    """P&L if we sold the first time the bid reached `target` cents, else held."""
    if target is not None and b.get(f"min_to_{target}c"):
        p = target / 100
        return STAKE * p - fee(p, STAKE) - cost(b)
    return hold_pnl(b)


def pct(n, d):
    return f"{n / d:.0%}" if d else "—"


def money(x):
    return f"-${abs(x):,.2f}" if x < 0 else f"${x:,.2f}"


def roi(pnls, costs):
    return f"{sum(pnls) / sum(costs):+.0%}" if costs and sum(costs) else "—"


def med(xs):
    xs = [x for x in xs if x is not None]
    return statistics.median(xs) if xs else None


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    return "\n".join(out + ["| " + " | ".join(str(c) for c in r) + " |" for r in rows])


def reached(b, t):
    return bool(b.get(f"min_to_{t}c"))


def strategies(bets):
    rows = []
    for label, t in [("Hold to the end", None)] + [(f"Sell at {t}¢", t) for t in TARGETS]:
        pnls = [exit_pnl(b, t) for b in bets]
        hits = sum(1 for b in bets if (b["result"] == "yes" if t is None else reached(b, t)))
        rows.append((label, t, hits, sum(pnls), roi(pnls, [cost(b) for b in bets])))
    return rows


# ---------------------------------------------------------------- charts
def charts(done_v, done_u):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        return []
    os.makedirs(CHARTS, exist_ok=True)
    plt.rcParams.update({"font.size": 11, "axes.edgecolor": GRID, "axes.labelcolor": INK2,
                         "xtick.color": INK2, "ytick.color": INK2, "text.color": INK,
                         "axes.spines.top": False, "axes.spines.right": False})
    made = []

    def frame(fig, ax, title):
        fig.patch.set_facecolor(SURFACE)
        ax.set_facecolor(SURFACE)
        ax.grid(axis="y", color=GRID, linewidth=0.8)
        ax.set_axisbelow(True)
        ax.set_title(title, loc="left", fontsize=13, color=INK, pad=12)

    # 1. Bounce curve: share of bets whose bid later reached at least X cents
    xs = list(range(2, 51))
    fig, ax = plt.subplots(figsize=(8, 4.2), dpi=150)
    frame(fig, ax, "How often the price bounced back after hitting 1¢")
    for bets, color, name in ((done_v, BLUE, "Verified live"), (done_u, ORANGE, "Unverified")):
        if not bets:
            continue
        ys = [100 * sum(1 for b in bets if f(b["peak_bid"], 0) >= x / 100 - 1e-9) / len(bets) for x in xs]
        ax.plot(xs, ys, color=color, linewidth=2, label=f"{name} ({len(bets)} bets)")
        ax.annotate(f"{ys[0]:.0f}%", (xs[0], ys[0]), textcoords="offset points", xytext=(6, 4),
                    color=INK2, fontsize=10)
    ax.set_xlabel("Price the bid later reached (¢)")
    ax.set_ylabel("% of bets")
    ax.set_ylim(0, 100)
    ax.legend(frameon=False, loc="upper right")
    fig.tight_layout()
    fig.savefig(os.path.join(CHARTS, "bounce.png"), facecolor=SURFACE)
    plt.close(fig)
    made.append("bounce.png")

    # 2. Return on money risked, per exit strategy (verified bets)
    if done_v:
        rows = strategies(done_v)
        labels = [r[0] for r in rows]
        vals = [100 * r[3] / sum(cost(b) for b in done_v) for r in rows]
        fig, ax = plt.subplots(figsize=(8, 4.2), dpi=150)
        frame(fig, ax, "Return by exit strategy (verified bets)")
        ax.grid(axis="y", visible=False)
        ax.grid(axis="x", color=GRID, linewidth=0.8)
        colors = [BLUE if v >= 0 else RED for v in vals]
        bars = ax.barh(labels[::-1], vals[::-1], color=colors[::-1], height=0.6,
                       edgecolor=SURFACE, linewidth=2)
        ax.axvline(0, color=INK2, linewidth=1)
        for bar, v in zip(bars, vals[::-1]):
            ax.annotate(f"{v:+.0f}%", (v, bar.get_y() + bar.get_height() / 2),
                        xytext=(6 if v >= 0 else -6, 0), textcoords="offset points",
                        ha="left" if v >= 0 else "right", va="center", color=INK, fontsize=10)
        ax.set_xlabel("Profit ÷ money risked (%)")
        lo, hi = min(vals + [0]), max(vals + [0])
        pad = (hi - lo) * 0.18 + 5
        ax.set_xlim(lo - pad, hi + pad)
        fig.tight_layout()
        fig.savefig(os.path.join(CHARTS, "exits.png"), facecolor=SURFACE)
        plt.close(fig)
        made.append("exits.png")

    # 3. Price paths after the 1¢ moment (verified bets)
    paths = []
    for b in done_v:
        p = os.path.join(DIR, "candles", f"{b['ticker']}.csv")
        if not os.path.exists(p):
            continue
        t0 = datetime.fromisoformat(b["detected_at"])
        end = f(b["minutes_to_end"])
        pts = []
        with open(p, newline="") as fh:
            for r in csv.DictReader(fh):
                m = (datetime.fromisoformat(r["minute_end"]) - t0).total_seconds() / 60
                if m < 0 or (end is not None and m > end + 1):
                    continue
                pts.append((m, max(f(r["bid_high"], 0), 0.005) * 100))
        if pts:
            paths.append((b["result"] == "yes", pts))
    if paths:
        fig, ax = plt.subplots(figsize=(8, 4.2), dpi=150)
        frame(fig, ax, "Best bid, minute by minute, after the 1¢ moment")
        for won, pts in sorted(paths, key=lambda x: x[0]):
            ax.plot([p[0] for p in pts], [p[1] for p in pts],
                    color=ORANGE if won else MUTED, linewidth=2 if won else 1,
                    alpha=1 if won else 0.6)
        ax.set_yscale("log")
        ax.minorticks_off()
        ax.set_yticks([0.5, 1, 2, 5, 10, 25, 50, 100])
        ax.set_yticklabels(["0", "1¢", "2¢", "5¢", "10¢", "25¢", "50¢", "$1"])
        ax.set_xlabel("Minutes after our 1¢ buy")
        ax.plot([], [], color=MUTED, linewidth=1, label="Lost")
        ax.plot([], [], color=ORANGE, linewidth=2, label="Came back and won")
        ax.legend(frameon=False, loc="upper right")
        fig.tight_layout()
        fig.savefig(os.path.join(CHARTS, "paths.png"), facecolor=SURFACE)
        plt.close(fig)
        made.append("paths.png")
    return made


# ---------------------------------------------------------------- page
def rule_stats(bets, target):
    pnls = [exit_pnl(b, target) for b in bets]
    spent = sum(cost(b) for b in bets)
    ordered = sorted(bets, key=lambda b: b["detected_at"])
    half = len(ordered) // 2
    first = sum(exit_pnl(b, target) for b in ordered[:half])
    second = sum(exit_pnl(b, target) for b in ordered[half:])
    hits = sum(1 for b in bets if (b["result"] == "yes" if target is None else reached(b, target)))
    return {"n": len(bets), "pnl": sum(pnls), "ret": sum(pnls) / spent if spent else 0,
            "hits": hits, "halves": (first, second)}


def current_strategy(bets, done):
    """Pick the best simple rule from the data so far and spell out what the
    bot would do if it were switched on right now."""
    universes = [("all leagues", lambda b: True),
                 ("ESPN-verified leagues only", lambda b: b["verified"] == "yes")]
    rules = []
    for uname, keep in universes:
        group = [b for b in done if keep(b)]
        if not group:
            continue
        for t in [None] + TARGETS:
            st = rule_stats(group, t)
            rules.append((uname, keep, t, st))
    md = ["## Current strategy", ""]
    if not rules:
        return md + ["*No finished bets yet — the strategy appears once games settle.*", ""]

    trusted = [r for r in rules if r[3]["n"] >= MIN_BETS]
    pool = trusted or rules
    uname, keep, t, st = max(pool, key=lambda r: r[3]["pnl"])
    group = [b for b in done if keep(b)]
    sell = "hold to the end" if t is None else f"sell at {t}¢"
    both_halves = st["halves"][0] > 0 and st["halves"][1] > 0

    if st["pnl"] <= 0:
        verdict = "🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything."
    elif st["n"] < MIN_BETS:
        verdict = f"🟡 **Provisional.** Best rule so far, but only {st['n']} finished bets (needs {MIN_BETS})."
    elif not both_halves:
        verdict = "🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data."
    elif st["n"] < 100:
        verdict = "🟢 **Trade small.** Profitable in both halves of the data; sample still modest."
    else:
        verdict = "🟢 **Trade.** Profitable in both halves of the data over 100+ bets."

    all_in = [b for b in bets if keep(b)]
    span_h = 0.0
    if all_in:
        ts = sorted(datetime.fromisoformat(b["detected_at"]) for b in all_in)
        span_h = (datetime.now(ts[0].tzinfo) - ts[0]).total_seconds() / 3600
    per_day = len(all_in) / max(span_h / 24, 1)
    buy_cost = cost({"entry_price": "0.01"})
    wait = med([f(b.get(f"min_to_{t}c")) for b in group if t and reached(b, t)])

    md += [verdict, ""]
    if st["pnl"] > 0:
        steps = [
            f"1. **Watch** every live game in **{uname}**.",
            "2. **Buy** when a team or player's YES price hits **1¢**"
            + (" and ESPN confirms the game is still being played" if "verified" in uname else "")
            + f": **{STAKE} contracts** with a 1¢ limit order "
              f"(cost {buy_cost * 100:.0f}¢ including the fee). One buy per outcome.",
        ]
        if t is None:
            steps.append("3. **Hold** every position until the game ends. No selling.")
        else:
            steps.append(f"3. **Sell** straight away with a limit order at **{t}¢**. "
                         f"If the price never gets there, hold until the game ends.")
        md += steps + [""]
    md += [table(["Rule", "Based on", "Hit rate", f"P&L ({STAKE} per buy)", "Return",
                  "Avg per bet", "Earlier half / later half"],
                 [[f"{uname}, {sell}", f"{st['n']} finished bets", pct(st["hits"], st["n"]),
                   money(st["pnl"]), f"{st['ret']:+.0%}", f"{st['pnl'] / st['n'] * 100:+.2f}¢",
                   f"{money(st['halves'][0])} / {money(st['halves'][1])}"]]), ""]
    if span_h >= 24:
        pace = f"about **{per_day:.0f} buys a day**, roughly **{money(per_day * buy_cost)}/day** at risk"
    else:
        pace = (f"**{len(all_in)} buys in the first {span_h:.0f} hours** "
                f"({money(len(all_in) * buy_cost)} risked) — daily pace shows after 24 hours")
    extras = [pace,
              f"max loss per buy **{buy_cost * 100:.0f}¢**"]
    if wait is not None:
        extras.append(f"typical wait to sell **{max(wait, 1):.0f} min**")
    md += ["*Expect " + "; ".join(extras) + ".*", ""]

    alt = sorted(pool, key=lambda r: -r[3]["pnl"])[1:4]
    if alt:
        md += ["<details><summary>Runner-up rules</summary>", "",
               table(["Rule", "Bets", "P&L", "Return"],
                     [[f"{u}, {'hold to the end' if tt is None else f'sell at {tt}¢'}", x["n"],
                       money(x["pnl"]), f"{x['ret']:+.0%}"] for u, _, tt, x in alt]),
               "", "</details>", ""]
    md += ["*Re-picked automatically from the latest data every refresh. Rules only use "
           "what's knowable at the moment of buying (league, price), not hindsight like "
           "how the game ended.*", ""]
    return md


def main():
    bets = [enrich(b) for b in load()]
    done = [b for b in bets if b["status"] == "settled" and b.get("data") == "complete"]
    done_v = [b for b in done if b["verified"] == "yes"]
    done_u = [b for b in done if b["verified"] != "yes"]
    open_n = sum(1 for b in bets if b["status"] == "open")
    now = datetime.now(ZoneInfo("America/Denver")).strftime("%a %b %-d, %-I:%M %p MT")

    md = ["# 1¢ Study", "",
          f"*Updated {now}. Paper money: each bet buys {STAKE} contracts at 1¢ "
          f"({STAKE}¢ + {fee(0.01, STAKE) * 100:.0f}¢ fee). "
          "Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*", "",
          "[← Back to all bots](README.md)", ""]
    md += current_strategy(bets, done)

    base = done_v or done
    wins = sum(1 for b in base if b["result"] == "yes")
    hold = [hold_pnl(b) for b in base]
    best = max(strategies(base), key=lambda r: r[3]) if base else None
    md += ["## Headline (verified live bets)", "",
           table(["1¢ moments (all leagues)", "Finished (verified)", "Came back & won", "Break-even win rate",
                  "Hold-to-end P&L", "Best exit so far"],
                 [[len(bets), len(base), f"{wins} ({pct(wins, len(base))})", f"{cost({'entry_price': '0.01'}) / STAKE:.1%}",
                   f"{money(sum(hold))} ({roi(hold, [cost(b) for b in base])})" if base else "—",
                   f"{best[0]}: {money(best[3])} ({best[4]})" if best else "—"]]), "",
           f"*In play right now: {open_n}. Verified = ESPN confirmed the game was still being "
           "played when we bought. Unverified leagues are shown separately below.*", ""]

    made = charts(done_v, done_u) if done else []
    if "bounce.png" in made:
        md += ["![Bounce curve](study/charts/bounce.png)", ""]

    # Bounce table
    rows = []
    for label, group in (("Verified", done_v), ("Unverified", done_u)):
        if group:
            rows.append([label, len(group)] + [pct(sum(1 for b in group if reached(b, t)), len(group))
                                               for t in TARGETS])
    if rows:
        md += ["## How high did the price bounce?", "",
               "*Share of bets where someone later bid at least this much before the game ended.*", "",
               table(["Group", "Bets"] + [f"≥{t}¢" for t in TARGETS], rows), ""]

    # Exit strategies
    if base:
        rows = [[lab, hits, pct(hits, len(base)), money(p), r] for lab, _, hits, p, r in strategies(base)]
        md += ["## Exit strategies", "",
               "*Sell the first time the bid reaches the target (after Kalshi's selling fee); "
               "if it never does, hold to the end. Based on the best bid each minute, "
               f"assuming a {STAKE}-contract sale would fill.*", "",
               table(["Strategy", "Hits", "Hit rate", "P&L", "Return"], rows), ""]
        if "exits.png" in made:
            md += ["![Exit strategies](study/charts/exits.png)", ""]

    # By league
    if done:
        groups = defaultdict(list)
        for b in done:
            groups[b["league"]].append(b)
        rows = []
        for lg in sorted(groups, key=lambda g: -len(groups[g])):
            g = groups[lg]
            ver = "✔" if all(b["verified"] == "yes" for b in g) else (
                "partly" if any(b["verified"] == "yes" for b in g) else "✘")
            rows.append([lg, ver, len(g), sum(1 for b in g if b["result"] == "yes"),
                         pct(sum(1 for b in g if reached(b, 2)), len(g)),
                         pct(sum(1 for b in g if reached(b, 5)), len(g)),
                         roi([exit_pnl(b, None) for b in g], [cost(b) for b in g]),
                         roi([exit_pnl(b, 2) for b in g], [cost(b) for b in g]),
                         f"{med([f(b['minutes_to_end']) for b in g]):.0f} min"
                         if med([f(b['minutes_to_end']) for b in g]) is not None else "—"])
        md += ["## By league", "",
               table(["League", "Verified", "Bets", "Won", "≥2¢", "≥5¢", "Hold return",
                      "Sell@2¢ return", "Typical time left"], rows), ""]

    # By time left
    if base:
        rows = []
        for lo, hi, label in TIME_BUCKETS:
            g = [b for b in base if lo <= f(b["minutes_to_end"], -1) < hi]
            if g:
                rows.append([label, len(g), pct(sum(1 for b in g if reached(b, 2)), len(g)),
                             pct(sum(1 for b in g if reached(b, 5)), len(g)),
                             pct(sum(1 for b in g if b["result"] == "yes"), len(g)),
                             roi([exit_pnl(b, 2) for b in g], [cost(b) for b in g])])
        md += ["## By time left when it hit 1¢", "",
               table(["Time left in game", "Bets", "≥2¢", "≥5¢", "Won", "Sell@2¢ return"], rows), ""]

    # Speed & liquidity
    if done:
        lag = med([f(b["detect_lag_s"]) for b in done])
        to_peak = med([f(b["peak_bid_min"]) for b in done if f(b["peak_bid"], 0) >= 0.02])
        liq = med([f(b["contracts_traded_at_1c"]) for b in done])
        md += ["## Speed & liquidity", "",
               table(["Metric", "Typical (median)"], [
                   ["Our buy vs Kalshi's first 1¢ trade", f"{lag:.0f} sec later" if lag is not None else "—"],
                   ["Time from 1¢ to its best bounce (bounced bets)",
                    f"{to_peak:.0f} min" if to_peak is not None else "—"],
                   ["Contracts traded at 1¢ after our buy (how much you could buy)",
                    f"{liq:,.0f}" if liq is not None else "—"],
               ]), ""]
    if "paths.png" in made:
        md += ["![Price paths](study/charts/paths.png)", ""]

    # Recent bets
    if bets:
        rows = []
        for b in reversed(bets[-30:]):
            res = {"yes": "✅ Won", "no": "❌ Lost", "void": "Void"}.get(b.get("result"), "In play")
            peak = f"{f(b.get('peak_bid'), 0) * 100:.0f}¢" if b.get("peak_bid") else "—"
            rows.append([b["detected_at"][5:16].replace("T", " "), b["league"], b["pick"],
                         "✔" if b["verified"] == "yes" else "✘",
                         b.get("situation_at_entry") or "—", peak, res,
                         money(hold_pnl(b)) if b.get("result") else "—"])
        md += ["## Latest bets", "", "*Times are UTC. Peak = best bid after our buy.*", "",
               table(["When", "League", "Pick", "Verified", "Situation at 1¢", "Peak", "Result",
                      "Hold P&L"], rows), ""]

    md += ["## Raw data", "",
           "- [study/bets.csv](study/bets.csv) — one row per bet with every metric",
           "- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet",
           "- `study/candles/` — minute-by-minute bid / ask / volume, per bet", ""]

    with open(os.path.join(HERE, "STUDY.md"), "w") as fh:
        fh.write("\n".join(md))
    print(f"Study page updated ({len(bets)} bets, {len(done)} finished)")


if __name__ == "__main__":
    main()
