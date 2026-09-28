"""Builds FAIRVALUE.md (+ charts) for the fair-value bot."""
import csv
import glob
import math
import os
import statistics
from collections import defaultdict
from datetime import datetime
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(HERE, "fv")
CHARTS = os.path.join(DIR, "charts")
MT = ZoneInfo("America/Denver")
CONTRACTS = 10
LIVE_EDGE = 0.04
THRESHOLDS = [0.02, 0.04, 0.06, 0.08, 0.10, 0.15]
MIN_TRADES = 30

SURFACE, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e6e5e1"
BLUE, ORANGE, RED, MUTED = "#2a78d6", "#eb6834", "#e34948", "#b9b8b3"


def fee(p, n):
    return math.ceil(0.07 * n * p * (1 - p) * 100 - 1e-9) / 100


def f(x, d=None):
    try:
        return float(x)
    except (TypeError, ValueError):
        return d


def load(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="") as fh:
        return list(csv.DictReader(fh))


def money(x):
    return f"-${abs(x):,.2f}" if x < 0 else f"${x:,.2f}"


def pct(n, d):
    return f"{n / d:.0%}" if d else "—"


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    return "\n".join(out + ["| " + " | ".join(str(c) for c in r) + " |" for r in rows])


def logloss(p, y):
    p = min(max(p, 1e-3), 1 - 1e-3)
    return -(y * math.log(p) + (1 - y) * math.log(1 - p))


def cost(t):
    return int(t["contracts"]) * (f(t["price"]) + f(t["fee"], 0))


def pnl(t):
    return f(t["pnl"], 0)


def summary(ts):
    c = sum(cost(t) for t in ts)
    p = sum(pnl(t) for t in ts)
    wins = sum(1 for t in ts if t["result"] == t["side"])
    return {"n": len(ts), "pnl": p, "ret": p / c if c else 0, "wins": wins,
            "avg_price": statistics.fmean(f(t["price"]) for t in ts) if ts else 0,
            "avg_model": statistics.fmean(f(t["model_p"]) for t in ts) if ts else 0}


def backtest(obs_by_ticker, results, th):
    """Replay the shadow log: first 30-second reading per market where either
    side was at least `th` cheaper than the model after fees."""
    trades = []
    for ticker, rows in obs_by_ticker.items():
        res = results.get(ticker)
        if res not in ("yes", "no"):
            continue
        for o in rows:
            secs = f(o["secs_left"], 0)
            if not (30 <= secs <= 840):
                continue
            up, bid, ask = f(o["model_up"]), f(o["yes_bid"], 0), f(o["yes_ask"], 0)
            opts = [("yes", up, ask), ("no", 1 - up, 1 - bid if bid else None)]
            done = False
            for side, p, a in opts:
                if a is None or not (0.05 <= a <= 0.95):
                    continue
                fe = fee(a, CONTRACTS) / CONTRACTS
                if p - a - fe >= th:
                    c = CONTRACTS * (a + fe)
                    trades.append({"time": o["time"], "pnl": (CONTRACTS if res == side else 0) - c, "cost": c})
                    done = True
                    break
            if done:
                break
    trades.sort(key=lambda t: t["time"])
    h = len(trades) // 2
    c = sum(t["cost"] for t in trades)
    return {"n": len(trades), "pnl": sum(t["pnl"] for t in trades),
            "ret": sum(t["pnl"] for t in trades) / c if c else 0,
            "halves": (sum(t["pnl"] for t in trades[:h]), sum(t["pnl"] for t in trades[h:]))}


def charts(settled, cal_rows):
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
        ax.grid(color=GRID, linewidth=0.8)
        ax.set_axisbelow(True)
        ax.set_title(title, loc="left", fontsize=13, color=INK, pad=12)

    if settled:
        ts = sorted(settled, key=lambda t: t["time"])
        cum, run = [], 0.0
        for t in ts:
            run += pnl(t)
            cum.append(run)
        fig, ax = plt.subplots(figsize=(8, 4), dpi=150)
        frame(fig, ax, "Cumulative paper P&L")
        ax.plot(range(1, len(cum) + 1), cum, color=BLUE if cum[-1] >= 0 else RED, linewidth=2)
        ax.axhline(0, color=INK2, linewidth=1)
        ax.set_xlabel("Trades")
        ax.set_ylabel("Dollars")
        ax.annotate(money(cum[-1]), (len(cum), cum[-1]), xytext=(6, 0), textcoords="offset points",
                    va="center", fontsize=10)
        fig.tight_layout()
        fig.savefig(os.path.join(CHARTS, "pnl.png"), facecolor=SURFACE)
        plt.close(fig)
        made.append("pnl.png")

    rows = [r for r in cal_rows if r["n"] >= 5]
    if rows:
        fig, ax = plt.subplots(figsize=(6.5, 5), dpi=150)
        frame(fig, ax, "Calibration: predicted vs actual chance of UP")
        ax.plot([0, 100], [0, 100], color=MUTED, linewidth=1, linestyle="--", label="Perfect")
        ax.plot([r["model"] * 100 for r in rows], [r["actual"] * 100 for r in rows], color=BLUE,
                linewidth=2, marker="o", markersize=5, label="Model")
        ax.plot([r["market"] * 100 for r in rows], [r["actual"] * 100 for r in rows], color=ORANGE,
                linewidth=2, marker="s", markersize=5, label="Kalshi price")
        ax.set_xlabel("Predicted chance of UP (%)")
        ax.set_ylabel("Actually went UP (%)")
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.legend(frameon=False, loc="upper left")
        fig.tight_layout()
        fig.savefig(os.path.join(CHARTS, "calibration.png"), facecolor=SURFACE)
        plt.close(fig)
        made.append("calibration.png")
    return made


def bucket_rows(settled, key, buckets):
    rows = []
    for lo, hi, label in buckets:
        g = [t for t in settled if key(t) is not None and lo <= key(t) < hi]
        if g:
            s = summary(g)
            rows.append([label, s["n"], f"{s['wins']} ({pct(s['wins'], s['n'])})",
                         f"{s['avg_price'] * 100:.0f}¢", f"{s['avg_model']:.0%}",
                         money(s["pnl"]), f"{s['ret']:+.0%}"])
    return rows


HEAD = ["", "Trades", "Won", "Avg price paid", "Model's avg chance", "P&L", "Return"]


def main():
    # Current files plus anything archived from earlier sessions, de-duplicated.
    by_ticker = {}
    for t in load(os.path.join(DIR, "archive", "trades__prev_session.csv")) + load(os.path.join(DIR, "trades.csv")):
        cur = by_ticker.get(t["ticker"])
        if cur is None or (cur["status"] != "settled" and t["status"] == "settled"):
            by_ticker[t["ticker"]] = t
    trades = sorted(by_ticker.values(), key=lambda t: t["time"])
    results = {}
    for r in load(os.path.join(DIR, "archive", "results__prev_session.csv")) + load(os.path.join(DIR, "results.csv")):
        results[r["ticker"]] = r["result"]
    seen, obs = set(), []
    for path in sorted(glob.glob(os.path.join(DIR, "obs", "*.csv")) + glob.glob(os.path.join(DIR, "archive", "obs_*.csv"))):
        for o in load(path):
            key = (o["time"], o["ticker"])
            if key not in seen:
                seen.add(key)
                obs.append(o)
    settled = [t for t in trades if t["status"] == "settled"]
    now = datetime.now(MT).strftime("%a %b %-d, %-I:%M %p MT")

    md = ["# Fair-Value Bot", "",
          f"*Updated {now}. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds "
          "the bot works out the fair chance of UP from the live Coinbase price, the target price, "
          "time left and recent volatility, then buys whichever side is at least "
          f"{LIVE_EDGE * 100:.0f}¢ cheaper than fair value after fees ({CONTRACTS} contracts, held to the close).*", "",
          "[← Back to all bots](README.md)", ""]

    # ---------------- model vs market (shadow log)
    scored = [(o, results[o["ticker"]]) for o in obs if results.get(o["ticker"]) in ("yes", "no")]
    skill_txt, skill = "not enough data yet", None
    if scored:
        ll_m = sum(logloss(f(o["model_up"]), r == "yes") for o, r in scored)
        ll_k = sum(logloss((f(o["yes_bid"], 0) + f(o["yes_ask"], 0)) / 2 or 0.5, r == "yes") for o, r in scored)
        skill = 1 - ll_m / ll_k if ll_k else 0

    # ---------------- strategy (live rule + backtested thresholds)
    obs_by_ticker = defaultdict(list)
    for o in sorted(obs, key=lambda o: o["time"]):
        obs_by_ticker[o["ticker"]].append(o)
    bt = {th: backtest(obs_by_ticker, results, th) for th in THRESHOLDS}
    trusted = {th: r for th, r in bt.items() if r["n"] >= MIN_TRADES}
    best_th = max(trusted, key=lambda th: trusted[th]["pnl"]) if trusted else None
    live = summary(settled) if settled else None

    md += ["## Current strategy", ""]
    if best_th is None:
        n = len(settled)
        md += [f"⏳ **Too early to call.** {n} settled trades so far — a verdict needs at least "
               f"{MIN_TRADES}, spread over many 15-minute windows (coins tend to move together, so "
               "trades in the same window aren't independent).", ""]
        rows = [[f"{th * 100:.0f}¢+" + (" ← live bot" if th == LIVE_EDGE else ""), bt[th]["n"],
                 money(bt[th]["pnl"]), f"{bt[th]['ret']:+.0%}"] for th in THRESHOLDS]
        md += ["**Edge thresholds so far** (replayed from the 30-second shadow log)", "",
               table(["Buy when edge is", "Trades", "P&L", "Return"], rows), ""]
    else:
        b = trusted.get(best_th)
        if b and b["pnl"] > 0 and b["halves"][0] > 0 and b["halves"][1] > 0 and (skill or 0) > 0:
            verdict = (f"🟢 **Trade small.** Buying when the edge is **{best_th * 100:.0f}¢+** made money in "
                       "both halves of the data, and the model predicts better than Kalshi's prices.")
        elif b and b["pnl"] > 0:
            verdict = (f"🟡 **Promising, unproven.** An edge of **{best_th * 100:.0f}¢+** is profitable so far, "
                       "but not consistently yet (needs both halves positive and the model beating the market).")
        else:
            verdict = "🔴 **Sit out.** No edge threshold has made money yet."
        md += [verdict, ""]
        if b and b["pnl"] > 0:
            md += [f"1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.",
                   f"2. **Buy** whichever side's price is at least **{best_th * 100:.0f}¢ below** that fair chance "
                   f"after fees, priced 5¢–95¢, with 30 sec–14 min left. {CONTRACTS} contracts, one trade per window.",
                   "3. **Hold** to the close.", ""]
        rows = []
        for th in THRESHOLDS:
            r = bt[th]
            rows.append([f"{th * 100:.0f}¢+" + (" ← live bot" if th == LIVE_EDGE else ""), r["n"],
                         money(r["pnl"]), f"{r['ret']:+.0%}",
                         f"{money(r['halves'][0])} / {money(r['halves'][1])}"])
        md += ["**Which edge threshold works best?** (replayed from the 30-second shadow log)", "",
               table(["Buy when edge is", "Trades", "P&L", "Return", "Earlier / later half"], rows), ""]

    # ---------------- headline
    if live:
        clv = [f(t["clv"]) for t in settled if f(t.get("clv")) is not None]
        md += ["## Live bot results", "",
               table(["Trades", "Settled", "Won", "Avg price paid", "Model's avg chance", "P&L", "Return",
                      "Avg price move 3 min after buying"],
                     [[len(trades), live["n"], f"{live['wins']} ({pct(live['wins'], live['n'])})",
                       f"{live['avg_price'] * 100:.0f}¢", f"{live['avg_model']:.0%}", money(live["pnl"]),
                       f"{live['ret']:+.0%}", f"{statistics.fmean(clv) * 100:+.1f}¢" if clv else "—"]]), "",
               "*If the model is right, the win rate should land near the model's average chance, above the "
               "average price paid. \"Price move 3 min after buying\" shows whether the market moved toward the "
               "model's number soon after we bought — an early sign of real skill.*", ""]

    # ---------------- model accuracy
    md += ["## Does the model beat the market?", ""]
    if skill is None:
        md += ["*Appears once shadow-logged windows settle.*", ""]
    else:
        verdict = "✅ Yes" if skill > 0.01 else ("❌ No" if skill < -0.01 else "≈ About the same")
        md += [f"**{verdict}** — accuracy vs Kalshi's prices: **{skill:+.1%}** over {len(scored):,} readings "
               f"from {len({o['ticker'] for o, _ in scored})} windows (log-loss skill; positive = model better).", ""]
    cal = []
    for lo in range(0, 100, 10):
        g = [(o, r) for o, r in scored if lo <= f(o["model_up"]) * 100 < lo + 10 or (lo == 90 and f(o["model_up"]) == 1)]
        if g:
            cal.append({"label": f"{lo}–{lo + 10}%", "n": len(g),
                        "model": statistics.fmean(f(o["model_up"]) for o, _ in g),
                        "market": statistics.fmean((f(o["yes_bid"], 0) + f(o["yes_ask"], 0)) / 2 for o, _ in g),
                        "actual": sum(1 for _, r in g if r == "yes") / len(g)})
    if cal:
        md += [table(["Model said UP", "Readings", "Model avg", "Kalshi price avg", "Actually UP"],
                     [[c["label"], c["n"], f"{c['model']:.0%}", f"{c['market']:.0%}", f"{c['actual']:.0%}"]
                      for c in cal]), "",
               "*A well-calibrated model's 'Actually UP' matches its own average in every row.*", ""]
    made = charts(settled, cal)
    if "calibration.png" in made:
        md += ["![Calibration](fv/charts/calibration.png)", ""]
    if "pnl.png" in made:
        md += ["![Cumulative P&L](fv/charts/pnl.png)", ""]

    # ---------------- breakdowns
    if settled:
        md += ["## By edge size", "",
               table(["Edge at buy"] + HEAD[1:], bucket_rows(settled, lambda t: f(t["edge"]),
                     [(0.04, 0.06, "4–6¢"), (0.06, 0.10, "6–10¢"), (0.10, 0.20, "10–20¢"), (0.20, 1, "20¢+")])), "",
               "*If bigger claimed edges don't do better, the model is overconfident.*", "",
               "## By time left", "",
               table(["Time left"] + HEAD[1:], bucket_rows(settled, lambda t: f(t["secs_left"]),
                     [(600, 900, "10–14 min"), (300, 600, "5–10 min"), (120, 300, "2–5 min"),
                      (60, 120, "1–2 min"), (0, 60, "Under 1 min")])), "",
               "## By price paid", "",
               table(["Price"] + HEAD[1:], bucket_rows(settled, lambda t: f(t["price"]),
                     [(0, 0.25, "Underdog (5–25¢)"), (0.25, 0.75, "Toss-up (25–75¢)"),
                      (0.75, 1, "Favorite (75–95¢)")])), ""]
        by_asset = defaultdict(list)
        for t in settled:
            by_asset[t["asset"]].append(t)
        md += ["## By coin", "",
               table(["Coin"] + HEAD[1:], [[a] + [c for c in bucket_rows(g, lambda t: 0, [(0, 1, a)])[0][1:]]
                                           for a, g in sorted(by_asset.items(), key=lambda kv: -len(kv[1]))]), ""]

    if trades:
        rows = []
        for t in reversed(trades[-25:]):
            when = datetime.fromisoformat(t["time"]).astimezone(MT).strftime("%-m/%-d %-I:%M:%S %p")
            res = ("✅ Won" if t["result"] == t["side"] else "❌ Lost") if t["status"] == "settled" else "Open"
            rows.append([when, t["asset"], "UP" if t["side"] == "yes" else "DOWN", f"{f(t['secs_left'], 0) / 60:.1f} min",
                         f"{f(t['price']) * 100:.0f}¢", f"{f(t['model_p']):.0%}", f"{f(t['edge']) * 100:.0f}¢",
                         res, money(pnl(t)) if t["status"] == "settled" else "—"])
        md += ["## Latest trades", "",
               table(["When (MT)", "Coin", "Side", "Time left", "Paid", "Model", "Edge", "Result", "P&L"], rows), ""]

    md += ["## How the model works", "",
           "- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves "
           "randomly with the volatility of the last hour (weighted toward the last 15 minutes).",
           "- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages "
           "its own price samples the same way and only models the part still to come.",
           "- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, "
           "and no trades under 5¢ or over 95¢ where small model errors matter most.", "",
           "## Raw data", "",
           "- [fv/trades.csv](fv/trades.csv) — every paper trade",
           "- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)",
           "- [fv/status.json](fv/status.json) — bot health", ""]
    with open(os.path.join(HERE, "FAIRVALUE.md"), "w") as fh:
        fh.write("\n".join(md))
    print(f"Fair-value page updated ({len(trades)} trades, {len(obs)} readings)")


if __name__ == "__main__":
    main()
