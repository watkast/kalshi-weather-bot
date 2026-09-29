"""Builds METALS.md for the gold & silver fair-value bot."""
import glob
import math
import os
from datetime import datetime
from zoneinfo import ZoneInfo

from common import HERE, fee_per_contract
from fv_bot import load

DIR = os.path.join(HERE, "metals")
MT = ZoneInfo("America/Denver")
MIN_SETTLED = 30


def money(x):
    return f"-${-x:,.2f}" if x < 0 else f"${x:,.2f}"


def pct(x):
    return f"{x:+.0%}"


def stats(rows):
    done = [t for t in rows if t["status"] == "settled"]
    won = sum(1 for t in done if float(t["pnl"]) > 0)
    pnl = sum(float(t["pnl"]) for t in done)
    risk = sum(int(t["contracts"]) * (float(t["price"]) + float(t["fee"])) for t in done)
    paid = sum(float(t["price"]) for t in done) / len(done) if done else 0
    model = sum(float(t["model_p"]) for t in done) / len(done) if done else 0
    return len(rows), done, won, pnl, risk, paid, model


def row(label, rows):
    n, done, won, pnl, risk, paid, model = stats(rows)
    if not done:
        return f"| {label} | {n} | 0 | — | — | — | — | — |"
    return (f"| {label} | {n} | {len(done)} | {won} ({won / len(done):.0%}) | {paid * 100:.0f}¢ | "
            f"{model:.0%} | {money(pnl)} | {pct(pnl / risk) if risk else '—'} |")


def load_obs():
    out = []
    for p in sorted(glob.glob(os.path.join(DIR, "obs", "*.csv"))):
        out += load(p)
    return out


def replay(obs, results, threshold, model_key="model_up"):
    """First moment in each market where a side was `threshold` cheaper than the
    model after fees (quoted prices, 30 s to 14 min left), held to the close."""
    taken, trades = set(), []
    for o in obs:
        t = o["ticker"]
        if t in taken or t not in results or not o.get("yes_ask") or not o.get("yes_bid"):
            continue
        secs = float(o["secs_left"])
        if not 30 <= secs <= 840:
            continue
        p_up = float(o[model_key])
        for side, p, ask in (("yes", p_up, float(o["yes_ask"])), ("no", 1 - p_up, 1 - float(o["yes_bid"]))):
            if not 0.05 <= ask <= 0.95:
                continue
            fee = fee_per_contract(ask, 10)
            if p - ask - fee >= threshold:
                win = results[t] == side
                trades.append({"time": o["time"], "pnl": 10 * ((1 if win else 0) - ask - fee),
                               "risk": 10 * (ask + fee), "win": win})
                taken.add(t)
                break
    return trades


def skill(obs, results, key):
    """Log-loss skill vs Kalshi's mid price (positive = model better)."""
    ll_m = ll_k = 0.0
    n = 0
    for o in obs:
        r = results.get(o["ticker"])
        if r not in ("yes", "no") or float(o["secs_left"]) < 60 or not o.get("yes_ask") or not o.get("yes_bid"):
            continue
        y = 1 if r == "yes" else 0
        pm = min(max(float(o[key]), 0.01), 0.99)
        pk = min(max((float(o["yes_ask"]) + float(o["yes_bid"])) / 2, 0.01), 0.99)
        ll_m -= math.log(pm if y else 1 - pm)
        ll_k -= math.log(pk if y else 1 - pk)
        n += 1
    return (1 - ll_m / ll_k, n) if n and ll_k else (None, n)


def main():
    trades = load(os.path.join(DIR, "trades.csv"))
    results = {r["ticker"]: r["result"] for r in load(os.path.join(DIR, "results.csv"))}
    obs = load_obs()
    now = datetime.now(MT).strftime("%a %b %-d, %-I:%M %p MT")
    n, done, won, pnl, risk, _, _ = stats(trades)

    half = len(done) // 2
    first = sum(float(t["pnl"]) for t in done[:half])
    second = sum(float(t["pnl"]) for t in done[half:])
    if len(done) < MIN_SETTLED:
        verdict = f"⏳ **Too early.** {len(done)} of {MIN_SETTLED} settled trades needed before judging."
    elif first > 0 and second > 0:
        verdict = "🟢 **Promising.** Profitable in both halves of the data."
    elif pnl > 0:
        verdict = "🟡 **Mixed.** Up overall, but not in both halves — could be luck."
    else:
        verdict = "🔴 **Losing.** Not beating Kalshi's prices after fees."

    L = ["# Gold & Silver Fair-Value Bot", "",
         f"*Updated {now}. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds "
         "the bot works out the fair chance of UP from how far the metal has moved since the window "
         "started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's "
         "real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*", "",
         "[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)", "",
         "## Verdict", "", verdict, "",
         "## Live results", "",
         "| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |",
         "|---|---|---|---|---|---|---|---|",
         row("**All**", trades)]
    for a in ("SILVER", "GOLD"):
        L.append(row(a.title(), [t for t in trades if t["asset"] == a]))
    if len(done) >= 4:
        L += ["", f"*Earlier half {money(first)} / later half {money(second)}.*"]
    L += ["", "*If the model is right, the win rate should land near the model's average chance, "
          "above the average price paid.*", ""]

    L += ["## Which edge threshold works best?", "",
          "*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*", "",
          "| Buy when edge is | Trades | Won | P&L | Return |", "|---|---|---|---|---|"]
    for th in (0.02, 0.04, 0.06, 0.08, 0.10, 0.15):
        tr = replay(obs, results, th)
        if tr:
            p = sum(x["pnl"] for x in tr)
            r = sum(x["risk"] for x in tr)
            w = sum(x["win"] for x in tr)
            mark = " ← live bot" if th == 0.04 else ""
            L.append(f"| {th * 100:.0f}¢+{mark} | {len(tr)} | {w} ({w / len(tr):.0%}) | {money(p)} | {pct(p / r)} |")
        else:
            L.append(f"| {th * 100:.0f}¢+ | 0 | — | — | — |")

    L += ["", "## Does the model beat the market?", "",
          "| Model | Readings scored | Accuracy vs Kalshi |", "|---|---|---|"]
    for key, name in (("model_up", "Move since window start (live bot)"),
                      ("model_direct", "Hyperliquid price vs Kalshi's target")):
        s, k = skill(obs, results, key)
        L.append(f"| {name} | {k} | {'—' if s is None else f'{s:+.1%}'} |")
    L += ["", "*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes "
          "better than Kalshi's price.*", ""]

    L += ["## Latest trades", "",
          "| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |",
          "|---|---|---|---|---|---|---|---|---|"]
    for t in reversed(trades[-12:]):
        when = datetime.fromisoformat(t["time"]).astimezone(MT).strftime("%-m/%-d %-I:%M:%S %p")
        res = "Open" if t["status"] == "open" else ("✅ Won" if float(t["pnl"]) > 0 else "❌ Lost")
        pl = "—" if t["status"] == "open" else money(float(t["pnl"]))
        side = "UP" if t["side"] == "yes" else "DOWN"
        L.append(f"| {when} | {t['asset'].title()} | {side} | {float(t['secs_left']) / 60:.1f} min | "
                 f"{float(t['price']) * 100:.0f}¢ | {float(t['model_p']):.0%} | {float(t['edge']) * 100:.0f}¢ | {res} | {pl} |")
    if not trades:
        L.append("| — | | | | | | | | |")

    with open(os.path.join(HERE, "METALS.md"), "w") as fh:
        fh.write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
