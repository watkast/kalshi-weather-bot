"""Builds FIFTEEN.md (+ charts) from the 15-minute 1-cent study."""
import csv
import glob
import math
import os
import statistics
from collections import defaultdict
from datetime import datetime
from zoneinfo import ZoneInfo

import models_report

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(HERE, "fifteen")
CHARTS = os.path.join(DIR, "charts")
TARGETS = [2, 3, 5, 10, 25, 50]
STAKE = 14
MIN_BETS = 30
MT = ZoneInfo("America/Denver")

SURFACE, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e6e5e1"
BLUE, ORANGE, AQUA, RED, MUTED = "#2a78d6", "#eb6834", "#1baf7a", "#e34948", "#b9b8b3"

LEFT_BUCKETS = [(600, 1e9, "Over 10 min"), (300, 600, "5–10 min"), (120, 300, "2–5 min"),
                (60, 120, "1–2 min"), (0, 60, "Under 1 min")]
GAP_BUCKETS = [(0, 0.05, "Under 0.05%"), (0.05, 0.1, "0.05–0.1%"), (0.1, 0.2, "0.1–0.2%"),
               (0.2, 0.5, "0.2–0.5%"), (0.5, 1e9, "Over 0.5%")]
HOUR_BUCKETS = [(0, 6, "Night (12–6am MT)"), (6, 12, "Morning (6am–12pm)"),
                (12, 18, "Afternoon (12–6pm)"), (18, 24, "Evening (6pm–12am)")]


def fee(p, n):
    return math.ceil(0.07 * n * p * (1 - p) * 100 - 1e-9) / 100


def f(x, default=None):
    try:
        return float(x)
    except (TypeError, ValueError):
        return default


def load():
    path = os.path.join(DIR, "bets.csv")
    if not os.path.exists(path):
        return []
    with open(path, newline="") as fh:
        return list(csv.DictReader(fh))


def cost(b):
    p = f(b.get("entry_price"), 0.01)
    return STAKE * p + fee(p, STAKE)


def won(b):
    return b.get("result") == b.get("side")


def reached(b, t):
    return bool(b.get(f"s_to_{t}c"))


def hold_pnl(b):
    if b.get("result") == "void":
        return 0.0
    return (STAKE if won(b) else 0) - cost(b)


def exit_pnl(b, t):
    if t is not None and reached(b, t):
        p = t / 100
        return STAKE * p - fee(p, STAKE) - cost(b)
    return hold_pnl(b)


def pct(n, d):
    return f"{n / d:.0%}" if d else "—"


def money(x):
    return f"-${abs(x):,.2f}" if x < 0 else f"${x:,.2f}"


def ret(bets, t):
    c = sum(cost(b) for b in bets)
    return f"{sum(exit_pnl(b, t) for b in bets) / c:+.0%}" if c else "—"


def med(xs):
    xs = [x for x in xs if x is not None]
    return statistics.median(xs) if xs else None


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    return "\n".join(out + ["| " + " | ".join(str(c) for c in r) + " |" for r in rows])


def mins(secs):
    if secs is None:
        return "—"
    return f"{secs:.0f} sec" if secs < 90 else f"{secs / 60:.1f} min"


def hour_mt(b):
    return datetime.fromisoformat(b["detected_at"]).astimezone(MT).hour


def group_row(label, g):
    return [label, len(g), f"{sum(won(b) for b in g)}", pct(sum(reached(b, 2) for b in g), len(g)),
            pct(sum(reached(b, 5) for b in g), len(g)), ret(g, None), ret(g, 2), ret(g, 3)]


GROUP_HEAD = ["", "Bets", "Won", "≥2¢", "≥5¢", "Hold return", "Sell@2¢", "Sell@3¢"]


def bucketed(done, key, buckets, title, note=None):
    rows = []
    for lo, hi, label in buckets:
        g = [b for b in done if key(b) is not None and lo <= key(b) < hi]
        if g:
            rows.append(group_row(label, g))
    if not rows:
        return []
    head = [title] + GROUP_HEAD[1:]
    return (["", f"*{note}*", ""] if note else [""]) + [table(head, rows), ""]


# ---------------------------------------------------------------- strategy
MODELS = [
    ("model_vol", "Volatility model",
     "random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility"),
    ("model_mom", "Momentum model", "same, but assumes the last 5 minutes' trend keeps going"),
    ("model_rev", "Mean-reversion model", "same, but assumes the last 5 minutes' trend reverses"),
]

UNIVERSES = [
    ("all markets", lambda b: True),
    ("crypto only", lambda b: b["category"] == "Crypto"),
    ("FX & commodities only", lambda b: b["category"] != "Crypto"),
    ("5+ min left", lambda b: f(b["secs_left"], 0) >= 300),
    ("2–5 min left", lambda b: 120 <= f(b["secs_left"], 0) < 300),
    ("under 2 min left", lambda b: f(b["secs_left"], 0) < 120),
] + models_report.universes(MODELS)


def rule_stats(bets, t):
    pnls = [exit_pnl(b, t) for b in bets]
    spent = sum(cost(b) for b in bets)
    ordered = sorted(bets, key=lambda b: b["detected_at"])
    h = len(ordered) // 2
    return {"n": len(bets), "pnl": sum(pnls), "ret": sum(pnls) / spent if spent else 0,
            "hits": sum(1 for b in bets if (won(b) if t is None else reached(b, t))),
            "halves": (sum(exit_pnl(b, t) for b in ordered[:h]), sum(exit_pnl(b, t) for b in ordered[h:]))}


def current_strategy(bets, done):
    md = ["## Current strategy", ""]
    rules = []
    for name, keep in UNIVERSES:
        g = [b for b in done if keep(b)]
        if g:
            rules += [(name, keep, t, rule_stats(g, t)) for t in [None] + TARGETS]
    if not rules:
        return md + ["*No finished bets yet — the strategy appears once windows settle.*", ""]
    trusted = [r for r in rules if r[3]["n"] >= MIN_BETS]
    pool = trusted or rules
    name, keep, t, st = max(pool, key=lambda r: r[3]["pnl"])
    both = st["halves"][0] > 0 and st["halves"][1] > 0
    if st["pnl"] <= 0:
        verdict = "🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything."
    elif st["n"] < MIN_BETS:
        verdict = f"🟡 **Provisional.** Best rule so far, but only {st['n']} finished bets (needs {MIN_BETS})."
    elif not both:
        verdict = "🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data."
    elif st["n"] < 100:
        verdict = "🟢 **Trade small.** Profitable in both halves of the data; sample still modest."
    else:
        verdict = "🟢 **Trade.** Profitable in both halves of the data over 100+ bets."
    sell = "hold to the close" if t is None else f"sell at {t}¢"
    buy_cost = cost({"entry_price": "0.01"})
    md += [verdict, ""]
    if st["pnl"] > 0:
        md += [f"1. **Watch** every 15-minute up/down market ({name}).",
               f"2. **Buy** the UP or DOWN side the moment it costs **1¢**: **{STAKE} contracts** "
               f"with a 1¢ limit order ({buy_cost * 100:.0f}¢ including the fee). One buy per side per window.",
               ("3. **Hold** until the 15 minutes are up. No selling." if t is None else
                f"3. **Sell** straight away with a limit order at **{t}¢**; if it never fills, "
                "hold until the window closes."), ""]
    md += [table(["Rule", "Based on", "Hit rate", f"P&L ({STAKE} per buy)", "Return", "Avg per bet",
                  "Earlier half / later half"],
                 [[f"{name}, {sell}", f"{st['n']} finished bets", pct(st["hits"], st["n"]),
                   money(st["pnl"]), f"{st['ret']:+.0%}", f"{st['pnl'] / st['n'] * 100:+.2f}¢",
                   f"{money(st['halves'][0])} / {money(st['halves'][1])}"]]), ""]
    matching = [b for b in bets if keep(b)]
    span_h = 0.0
    if matching:
        first = min(datetime.fromisoformat(b["detected_at"]) for b in matching)
        span_h = (datetime.now(first.tzinfo) - first).total_seconds() / 3600
    if span_h >= 24:
        pace = f"about **{len(matching) / (span_h / 24):.0f} buys a day** (~{money(len(matching) / (span_h / 24) * buy_cost)}/day at risk)"
    else:
        pace = f"**{len(matching)} buys in the first {max(span_h, 0.1):.0f} hours** — daily pace shows after 24 hours"
    wait = med([f(b.get(f"s_to_{t}c")) for b in done if keep(b) and t and reached(b, t)])
    extra = f"; typical wait to sell **{mins(wait)}**" if wait is not None else ""
    md += [f"*Expect {pace}; max loss per buy **{buy_cost * 100:.0f}¢**{extra}.*", ""]
    alt = sorted(pool, key=lambda r: -r[3]["pnl"])[1:4]
    if alt:
        md += ["<details><summary>Runner-up rules</summary>", "",
               table(["Rule", "Bets", "P&L", "Return"],
                     [[f"{u}, {'hold to the close' if tt is None else f'sell at {tt}¢'}", x["n"],
                       money(x["pnl"]), f"{x['ret']:+.0%}"] for u, _, tt, x in alt]), "", "</details>", ""]
    md += ["*Re-picked from the latest data every refresh, using only what's knowable at the moment "
           "of buying (market type, time left, price, model readings).*", ""]
    return md


# ---------------------------------------------------------------- charts
def charts(done):
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

    # Bounce curve by time left at entry
    xs = list(range(2, 51))
    groups = [("5+ min left", BLUE, lambda b: f(b["secs_left"], 0) >= 300),
              ("1–5 min left", ORANGE, lambda b: 60 <= f(b["secs_left"], 0) < 300),
              ("Under 1 min left", AQUA, lambda b: f(b["secs_left"], 0) < 60)]
    fig, ax = plt.subplots(figsize=(8, 4.2), dpi=150)
    frame(fig, ax, "How often the price bounced after hitting 1¢")
    drawn = False
    for name, color, keep in groups:
        g = [b for b in done if keep(b)]
        if not g:
            continue
        ys = [100 * sum(1 for b in g if f(b["peak_bid"], 0) >= x / 100 - 1e-9) / len(g) for x in xs]
        ax.plot(xs, ys, color=color, linewidth=2, label=f"{name} ({len(g)})")
        drawn = True
    if drawn:
        ax.set_xlabel("Price the bid later reached (¢)")
        ax.set_ylabel("% of bets")
        ax.set_ylim(0, 100)
        ax.legend(frameon=False, loc="upper right")
        fig.tight_layout()
        fig.savefig(os.path.join(CHARTS, "bounce.png"), facecolor=SURFACE)
        made.append("bounce.png")
    plt.close(fig)

    # Exit strategies
    rows = [("Hold to the close", None)] + [(f"Sell at {t}¢", t) for t in TARGETS]
    spent = sum(cost(b) for b in done)
    vals = [100 * sum(exit_pnl(b, t) for b in done) / spent for _, t in rows]
    fig, ax = plt.subplots(figsize=(8, 4.2), dpi=150)
    frame(fig, ax, "Return by exit strategy (all markets)")
    ax.grid(axis="y", visible=False)
    ax.grid(axis="x", color=GRID, linewidth=0.8)
    labels = [r[0] for r in rows]
    bars = ax.barh(labels[::-1], vals[::-1], color=[BLUE if v >= 0 else RED for v in vals[::-1]],
                   height=0.6, edgecolor=SURFACE, linewidth=2)
    ax.axvline(0, color=INK2, linewidth=1)
    for bar, v in zip(bars, vals[::-1]):
        ax.annotate(f"{v:+.0f}%", (v, bar.get_y() + bar.get_height() / 2),
                    xytext=(6 if v >= 0 else -6, 0), textcoords="offset points",
                    ha="left" if v >= 0 else "right", va="center", fontsize=10)
    lo, hi = min(vals + [0]), max(vals + [0])
    ax.set_xlim(lo - (hi - lo) * 0.18 - 5, hi + (hi - lo) * 0.18 + 5)
    ax.set_xlabel("Profit ÷ money risked (%)")
    fig.tight_layout()
    fig.savefig(os.path.join(CHARTS, "exits.png"), facecolor=SURFACE)
    plt.close(fig)
    made.append("exits.png")

    # Price paths from our 2-second snapshots (most recent 300 bets)
    recent = {(b["ticker"], b["side"]): b for b in sorted(done, key=lambda b: b["detected_at"])[-300:]}
    paths = defaultdict(list)
    for path in sorted(glob.glob(os.path.join(DIR, "snaps", "*.csv")))[-3:]:
        with open(path, newline="") as fh:
            for r in csv.DictReader(fh):
                key = (r["ticker"], r["side"])
                if key in recent:
                    paths[key].append(r)
    if paths:
        fig, ax = plt.subplots(figsize=(8, 4.2), dpi=150)
        frame(fig, ax, "Bid for our side, every ~2 seconds after the 1¢ buy")
        for key, rows_ in sorted(paths.items(), key=lambda kv: won(recent[kv[0]])):
            b = recent[key]
            t0 = datetime.fromisoformat(b["detected_at"])
            xs_ = [(datetime.fromisoformat(r["time"]) - t0).total_seconds() / 60 for r in rows_]
            ys_ = [max(f(r["bid"], 0), 0.005) * 100 for r in rows_]
            w = won(b)
            ax.plot(xs_, ys_, color=ORANGE if w else MUTED, linewidth=2 if w else 0.8, alpha=1 if w else 0.5)
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
def main():
    bets = load()
    done = [b for b in bets if b["status"] == "settled" and f(b.get("snapshots"), 0) > 0]
    in_play = sum(1 for b in bets if b["status"] != "settled")
    now = datetime.now(MT).strftime("%a %b %-d, %-I:%M %p MT")
    buy_cost = cost({"entry_price": "0.01"})

    md = ["# 15-Minute 1¢ Study", "",
          f"*Updated {now}. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, "
          f"commodities). Each time the UP or DOWN side hits 1¢ we buy {STAKE} contracts "
          f"({STAKE}¢ + {fee(0.01, STAKE) * 100:.0f}¢ fee) and track that side's price every ~2 seconds "
          "until the window closes.*", "",
          "[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)", ""]
    md += current_strategy(bets, done)

    wins = sum(won(b) for b in done)
    best = max(((lab, t) for lab, t in [("Hold to the close", None)] + [(f"Sell at {t}¢", t) for t in TARGETS]),
               key=lambda x: sum(exit_pnl(b, x[1]) for b in done)) if done else None
    md += ["## Headline", "",
           table(["1¢ moments caught", "Finished", "Came back & won", "Break-even win rate",
                  "Hold-to-close P&L", "Best exit so far"],
                 [[len(bets), len(done), f"{wins} ({pct(wins, len(done))})", f"{buy_cost / STAKE:.2%}",
                   f"{money(sum(hold_pnl(b) for b in done))} ({ret(done, None)})" if done else "—",
                   f"{best[0]}: {money(sum(exit_pnl(b, best[1]) for b in done))} ({ret(done, best[1])})"
                   if best else "—"]]), "",
           f"*In play or awaiting result: {in_play}. Commodity markets can take a few hours to settle.*", ""]

    md += models_report.section(done, MODELS, won, exit_pnl, cost, TARGETS,
                                note="Models cover the crypto markets (live prices from Coinbase). "
                                     "Readings start with the next watch session (about 12:45 AM MT, Sep 28).")

    if not done:
        md += ["*Charts and breakdowns appear after the first windows settle.*", ""]
    else:
        made = charts(done)
        if "bounce.png" in made:
            md += ["![Bounce curve](fifteen/charts/bounce.png)", ""]
        cats = defaultdict(list)
        for b in done:
            cats[b["category"] or "Other"].append(b)
        md += ["## How high did the price bounce?", "",
               "*Share of bets where the bid for our side later reached at least this much before the close.*", "",
               table(["Market type", "Bets"] + [f"≥{t}¢" for t in TARGETS],
                     [[c, len(g)] + [pct(sum(reached(b, t) for b in g), len(g)) for t in TARGETS]
                      for c, g in sorted(cats.items(), key=lambda kv: -len(kv[1]))]
                     + [["**All**", len(done)] + [pct(sum(reached(b, t) for b in done), len(done)) for t in TARGETS]]), ""]

        md += ["## Exit strategies", "",
               "*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); "
               f"otherwise hold to the close. Uses our 2-second snapshots, assuming a {STAKE}-contract sale fills.*", "",
               table(["Strategy", "Hits", "Hit rate", "P&L", "Return", "Typical wait"],
                     [[lab, sum(1 for b in done if (won(b) if t is None else reached(b, t))),
                       pct(sum(1 for b in done if (won(b) if t is None else reached(b, t))), len(done)),
                       money(sum(exit_pnl(b, t) for b in done)), ret(done, t),
                       mins(med([f(b.get(f"s_to_{t}c")) for b in done if t and reached(b, t)])) if t else "—"]
                      for lab, t in [("Hold to the close", None)] + [(f"Sell at {t}¢", t) for t in TARGETS]]), ""]
        if "exits.png" in made:
            md += ["![Exit strategies](fifteen/charts/exits.png)", ""]

        md += ["## By time left when it hit 1¢"]
        md += bucketed(done, lambda b: f(b["secs_left"]), LEFT_BUCKETS, "Time left in window")

        assets = defaultdict(list)
        for b in done:
            assets[b["asset"]].append(b)
        md += ["## By market", "",
               table(["Market"] + GROUP_HEAD[1:],
                     [group_row(a, g) for a, g in sorted(assets.items(), key=lambda kv: -len(kv[1]))]), ""]

        md += ["## UP vs DOWN", "",
               table(["Side"] + GROUP_HEAD[1:],
                     [group_row(lbl, [b for b in done if b["side"] == s])
                      for lbl, s in (("UP (bought YES)", "yes"), ("DOWN (bought NO)", "no"))
                      if any(b["side"] == s for b in done)]), ""]

        md += ["## By how far price had to move (crypto)"]
        md += bucketed(done, lambda b: abs(f(b["gap_pct"])) if f(b.get("gap_pct")) is not None else None,
                       GAP_BUCKETS, "Gap to target at buy",
                       "Distance between the coin's live price (Coinbase) and the window's target price when we bought.")

        md += ["## By time of day"]
        md += bucketed(done, hour_mt, HOUR_BUCKETS, "When (MT)")

        md += ["## Speed & liquidity", "",
               table(["Metric", "Typical (median)"], [
                   ["Our buy vs Kalshi's first 1¢ trade", mins(med([f(b.get("detect_lag_s")) for b in done]))],
                   ["Contracts traded at 1¢ after our buy (room to buy more)",
                    f"{med([f(b.get('contracts_at_1c_after')) for b in done]) or 0:,.0f}"],
                   ["Time from buy to best bounce (bounced bets)",
                    mins(med([f(b.get("peak_at_s")) for b in done if f(b.get("peak_bid"), 0) >= 0.02]))],
                   ["Price snapshots per bet", f"{med([f(b.get('snapshots')) for b in done]) or 0:.0f}"],
               ]), ""]
        if "paths.png" in made:
            md += ["![Price paths](fifteen/charts/paths.png)", ""]

    if bets:
        rows = []
        for b in reversed(bets[-30:]):
            when = datetime.fromisoformat(b["detected_at"]).astimezone(MT).strftime("%-m/%-d %-I:%M:%S %p")
            res = ("✅ Won" if won(b) else "❌ Lost") if b["status"] == "settled" else "In play"
            gap = f"{f(b['gap_pct']):+.3f}%" if f(b.get("gap_pct")) is not None else "—"
            peak = f"{f(b.get('peak_bid'), 0) * 100:.0f}¢" if b.get("peak_bid") else "—"
            rows.append([when, b["asset"], "UP" if b["side"] == "yes" else "DOWN", mins(f(b["secs_left"])),
                         gap, peak, res, money(hold_pnl(b)) if b["status"] == "settled" else "—"])
        md += ["## Latest bets", "",
               table(["When (MT)", "Market", "Side", "Time left", "Gap", "Peak bid", "Result", "Hold P&L"], rows), ""]

    md += ["## Raw data", "",
           "- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric",
           "- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day",
           "- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close",
           "- [fifteen/status.json](fifteen/status.json) — bot health", ""]
    with open(os.path.join(HERE, "FIFTEEN.md"), "w") as fh:
        fh.write("\n".join(md))
    print(f"15-min page updated ({len(bets)} bets, {len(done)} finished)")


if __name__ == "__main__":
    main()
