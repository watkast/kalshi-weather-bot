"""Shared 'Prediction models' section for the 1-cent study dashboards."""
import math

THRESHOLDS = [0.02, 0.05, 0.10]


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def _table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    return "\n".join(out + ["| " + " | ".join(str(c) for c in r) + " |" for r in rows])


def _logloss(p, y):
    p = min(max(p, 1e-4), 1 - 1e-4)
    return -(y * math.log(p) + (1 - y) * math.log(1 - p))


def universes(models):
    """Extra buy filters for the Current Strategy picker: 'model says >= X%'."""
    out = []
    for col, label, _ in models:
        for th in (0.02, 0.05):
            out.append((f"{label} ≥ {th:.0%}",
                        lambda b, c=col, t=th: (_f(b.get(c)) or 0) >= t))
    return out


def section(done, models, won, exit_pnl, cost, targets, note=None):
    md = ["## Prediction models", "",
          "*Each model's chance that our side wins, recorded at the moment we bought. "
          "Kalshi's price said about 1%. If a model knows better, only buying when it "
          "disagrees with the market should improve results.*", ""]
    for _, label, desc in models:
        md.append(f"- **{label}:** {desc}")
    md.append("")
    if note:
        md += [f"*{note}*", ""]

    scored_any = False
    rows = []
    for col, label, _ in models:
        g = [b for b in done if _f(b.get(col)) is not None]
        if not g:
            rows.append([label, 0, "—", "—", "—", "—"])
            continue
        scored_any = True
        wins = sum(1 for b in g if won(b))
        avg = sum(_f(b[col]) for b in g) / len(g)
        ll_model = sum(_logloss(_f(b[col]), won(b)) for b in g)
        ll_mkt = sum(_logloss(_f(b.get("entry_price")) or 0.01, won(b)) for b in g)
        skill = 1 - ll_model / ll_mkt if ll_mkt else 0
        verdict = "✅ Better" if skill > 0.02 else ("❌ Worse" if skill < -0.02 else "≈ Same")
        rows.append([label, len(g), f"{avg:.1%}", f"{wins / len(g):.1%} ({wins})",
                     f"{skill:+.0%}", verdict])
    md += ["### How accurate is each model?", "",
           _table(["Model", "Bets scored", "Avg chance it gave", "Actual win rate",
                   "Accuracy vs market", "Verdict"], rows), "",
           "*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price "
           "(log-loss skill). Positive = the model predicted outcomes better than the market.*", ""]
    if not scored_any:
        return md + ["*Model scores appear once bets with model readings settle.*", ""]

    def ret(g, t):
        c = sum(cost(b) for b in g)
        return f"{sum(exit_pnl(b, t) for b in g) / c:+.0%}" if c else "—"

    head = ["Buy only when…", "Bets", "Won", "Hold return"] + [f"Sell@{t}¢" for t in targets[:3]]
    base = [b for b in done if any(_f(b.get(c)) is not None for c, _, _ in models)]
    rows = [["**Any 1¢ (no model)**", len(base), sum(1 for b in base if won(b)), ret(base, None)]
            + [ret(base, t) for t in targets[:3]]]
    for col, label, _ in models:
        for th in THRESHOLDS:
            g = [b for b in done if (_f(b.get(col)) or -1) >= th]
            if not g:
                continue
            rows.append([f"{label} ≥ {th:.0%}", len(g), sum(1 for b in g if won(b)), ret(g, None)]
                        + [ret(g, t) for t in targets[:3]])
    md += ["### Would the models have helped?", "",
           _table(head, rows), "",
           "*Compare each row with the first one: a model helps if its filtered bets earn more.*", ""]
    return md
