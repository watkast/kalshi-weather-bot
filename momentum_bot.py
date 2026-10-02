"""Momentum bot for Kalshi's 15-minute crypto up/down markets (paper money).

At any point in a coin's 15-minute window, when the UP or DOWN side's price
jumps (mid-price up RISE or more over the last 30 seconds), buy 10 contracts
at the real order-book price, then sell at +5¢ or more. No stop-loss.
One position per window per version; after a sale it looks for the next jump.

Versions run side by side on the same markets:
  J20  jump of 20¢+, sell the moment the bid is +5¢
  J20R jump of 20¢+, once +5¢ is reached keep riding while it rises,
       sell when the bid slips 2¢ off its high (never below +5¢)
Anything not sold is held to the close.

Files (under momentum/): trades.csv, status.json. Dashboard: MOMENTUM.md
"""
import json
import os
import subprocess
import sys
import time
from collections import deque
from datetime import datetime, timezone

import scalp_bot
from common import HERE, fee_per_contract, load_rows
from fifteen_bot import asset_of, iso, side_quote, write_csv
from scalp_bot import book_fill, now_utc

DIR = os.path.join(HERE, "momentum")
TRADES = os.path.join(DIR, "trades.csv")
STATUS = os.path.join(DIR, "status.json")
PAGE = os.path.join(HERE, "MOMENTUM.md")

LOOKBACK = 30           # seconds over which the jump is measured
TAKE_PROFIT = 0.05
TRAIL = 0.02            # ride version: sell when bid falls this far off its high
VERSIONS = {"J20": (0.20, False), "J20R": (0.20, True)}
LABELS = {"J20": "20¢+ jump, sell +5¢", "J20R": "20¢+ jump, ride past +5¢"}
MIN_PRICE, MAX_PRICE, MAX_SPREAD = 0.05, 0.90, 0.04
MIN_SECS_LEFT = 30
CONTRACTS = 10

FIELDS = ["version", "time", "ticker", "asset", "side", "secs_left", "jump", "price", "fee", "contracts",
          "status", "peak_bid", "exit_price", "exit_fee", "exit_at", "exit_secs_left", "result", "pnl"]


class Momentum(scalp_bot.Scalp):
    def __init__(self):
        super().__init__()
        self.trades = load_rows(TRADES)
        self.hist = {}       # ticker -> deque of (time, yes mid)

    def poll(self):
        now = now_utc()
        live = [t for t, c in self.markets.items() if c > now]
        quotes = {}
        for i in range(0, len(live), 50):
            data = scalp_bot.kalshi_get("/markets", {"tickers": ",".join(live[i:i + 50]), "limit": 1000})
            quotes.update({m["ticker"]: m for m in data.get("markets", [])})
        for tk, m in quotes.items():
            yb, ya = side_quote(m, "yes")
            if yb is None or ya is None:
                continue
            dq = self.hist.setdefault(tk, deque(maxlen=60))
            dq.append((now, (yb + ya) / 2))
            for ver in VERSIONS:
                self.step(tk, m, ver, now, dq)
        for tk in [t for t in self.hist if t not in quotes]:
            del self.hist[tk]

    def open_pos(self, ticker, ver):
        for t in self.trades:
            if t["ticker"] == ticker and t["status"] == "open" and t["version"] == ver:
                return t
        return None

    def step(self, tk, m, ver, now, dq):
        rise, ride = VERSIONS[ver]
        secs_left = (self.markets[tk] - now).total_seconds()
        pos = self.open_pos(tk, ver)
        if pos:
            bid, _ = side_quote(m, pos["side"])
            if bid is None or secs_left <= 1:
                return
            entry = float(pos["price"])
            peak = max(float(pos.get("peak_bid") or 0), bid)
            pos["peak_bid"] = f"{peak:.4f}"
            hit = bid >= entry + TAKE_PROFIT - 1e-9
            if hit and (not ride or bid <= peak - TRAIL + 1e-9):
                n = int(pos["contracts"])
                xfee = fee_per_contract(bid, n)
                pnl = n * (bid - xfee - entry - float(pos["fee"]))
                pos.update(status="sold", exit_price=f"{bid:.4f}", exit_fee=f"{xfee:.4f}",
                           exit_at=iso(now), exit_secs_left=int(secs_left), pnl=f"{pnl:.2f}")
                print(f"SELL {ver} {tk} {pos['side']} {entry:.2f}->{bid:.2f}  ${pnl:+.2f}")
            return
        if secs_left < MIN_SECS_LEFT:
            return
        old = [mid for t, mid in dq if (now - t).total_seconds() >= LOOKBACK]
        if not old:
            return
        then, cur = old[-1], dq[-1][1]
        for side, jump in (("yes", cur - then), ("no", then - cur)):
            if jump < rise - 1e-9:
                continue
            bid, ask = side_quote(m, side)
            if ask is None or bid is None or not (MIN_PRICE <= ask <= MAX_PRICE) or ask - bid > MAX_SPREAD:
                continue
            fill = book_fill(tk, side, CONTRACTS)
            if fill is None or fill > ask + 0.02:
                continue
            self.trades.append({
                "version": ver, "time": iso(now), "ticker": tk, "asset": asset_of(tk.split("-")[0]),
                "side": side, "secs_left": int(secs_left), "jump": f"{jump:.3f}", "price": f"{fill:.4f}",
                "fee": f"{fee_per_contract(fill, CONTRACTS):.4f}", "contracts": CONTRACTS,
                "status": "open", "peak_bid": f"{bid:.4f}"})
            print(f"BUY  {ver} {tk} {side} @ {fill:.2f} after {jump * 100:.0f}c jump ({int(secs_left)}s left)")
            return

    def save(self):
        write_csv(TRADES, self.trades, FIELDS)
        with open(STATUS, "w") as fh:
            json.dump({"saved_at": iso(now_utc()), "windows_watched": len(self.markets),
                       "trades": len(self.trades), "errors": self.errors[-20:]}, fh, indent=1)
        write_page(self.trades)
        subprocess.run(["git", "add", "momentum", "MOMENTUM.md"], cwd=HERE, capture_output=True)
        if subprocess.run(["git", "commit", "-q", "-m", "momentum update"], cwd=HERE,
                          capture_output=True).returncode != 0:
            return
        for _ in range(3):
            if subprocess.run(["git", "pull", "-q", "--rebase", "-X", "theirs"], cwd=HERE,
                              capture_output=True).returncode != 0:
                subprocess.run(["git", "rebase", "--abort"], cwd=HERE, capture_output=True)
            if subprocess.run(["git", "push", "-q"], cwd=HERE, capture_output=True).returncode == 0:
                return
            time.sleep(3)


def write_page(trades):
    lines = [
        "# Momentum Bot", "",
        f"*Updated {datetime.now(timezone.utc):%a %b %d %H:%M} UTC. Paper money. Kalshi's 15-minute crypto "
        "up/down markets: when either side's price jumps 20¢ or more within 30 seconds, buy 10 contracts and sell at "
        "+5¢ or more. No stop-loss; anything not sold rides to the close.*", "",
        "[← Back to all bots](README.md)", "",
        "| Version | Trades | Sold early | Held to close (won) | Open | P&L | Return |",
        "|---|---|---|---|---|---|---|",
    ]
    for ver in dict.fromkeys(list(VERSIONS) + [t["version"] for t in trades]):
        vt = [t for t in trades if t["version"] == ver]
        if not vt and ver not in VERSIONS:
            continue
        vd = [t for t in vt if t["status"] in ("sold", "settled")]
        vh = [t for t in vd if t["status"] == "settled"]
        vp = sum(float(t["pnl"]) for t in vd)
        vr = sum(int(t["contracts"]) * (float(t["price"]) + float(t["fee"])) for t in vd)
        lines.append(f"| **{LABELS.get(ver, ver + ' (retired)')}** | {len(vd)} | {len(vd) - len(vh)} | {len(vh)} "
                     f"({sum(1 for t in vh if float(t['pnl']) > 0)}) | "
                     f"{sum(1 for t in vt if t['status'] == 'open')} | ${vp:.2f} | "
                     f"{(vp / vr if vr else 0):+.1%} |")
    lines += ["", "*Verdicts need at least 20 finished trades per version.*", "",
              "## Latest trades", "",
              "| Time (UTC) | Version | Coin | Side | Jump | Paid | Sold / result | P&L |",
              "|---|---|---|---|---|---|---|---|"]
    for t in trades[-40:][::-1]:
        out = f"{float(t['exit_price']):.2f}" if t["status"] == "sold" else (t.get("result") or "open")
        lines.append(f"| {t['time'][5:16].replace('T', ' ')} | {t['version']} | {t['asset']} | "
                     f"{'UP' if t['side'] == 'yes' else 'DOWN'} | {float(t['jump']) * 100:.0f}¢ | "
                     f"{float(t['price']):.2f} | {out} | {t.get('pnl') or ''} |")
    with open(PAGE, "w") as fh:
        fh.write("\n".join(lines) + "\n")


def main():
    os.makedirs(DIR, exist_ok=True)
    scalp_bot.TRADES = TRADES   # Scalp.__init__ loads this path; we reload ours anyway
    bot = Momentum()
    end = time.time() + scalp_bot.RUN_MINUTES * 60
    last_save = time.time()
    while time.time() < end:
        try:
            if time.time() - bot.last_series > 3600:
                bot.load_series()
            if time.time() - bot.last_refresh > 60:
                bot.refresh()
                bot.settle()
            bot.poll()
        except Exception as exc:
            bot.errors.append(f"{iso(now_utc())} {exc}")
            print("error:", exc)
        if time.time() - last_save > scalp_bot.SAVE_MINUTES * 60:
            bot.save()
            last_save = time.time()
        time.sleep(scalp_bot.POLL_SECONDS)
    bot.refresh()
    bot.settle()
    bot.save()


if __name__ == "__main__":
    sys.exit(main())
