"""Range-scalp bot for Kalshi's 15-minute crypto up/down markets (paper money).

For every coin's 15-minute window, from the moment it opens:
  1. Watch both sides every ~2 seconds. When the UP or DOWN side's ask
     stays between 55¢ and 70¢ for 20 seconds straight, buy 10 contracts
     at the real order-book price.
  2. Sell as soon as that side's bid is 20¢ above what we paid.
  3. Then start watching again (either side) and repeat. One position per
     window at a time. Anything not sold is held to the close.

Files (under scalp/): trades.csv, status.json. Dashboard: SCALP.md
"""
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone

from common import HERE, fee_per_contract, get_markets, kalshi_get
from fifteen_bot import asset_of, iso, parse_ts, side_quote, write_csv
from common import load_rows

DIR = os.path.join(HERE, "scalp")
TRADES = os.path.join(DIR, "trades.csv")
STATUS = os.path.join(DIR, "status.json")
PAGE = os.path.join(HERE, "SCALP.md")

LOW, HIGH = 0.55, 0.70      # entry band for the side we buy
HOLD_SECONDS = 20           # price must stay in the band this long
TAKE_PROFIT = 0.20          # sell when bid >= entry + 20 cents
MIN_SECS_LEFT = 30          # no new buys in the last 30 seconds
CONTRACTS = 10
POLL_SECONDS = 2
SAVE_MINUTES = 10
RUN_MINUTES = float(os.environ.get("RUN_MINUTES", "330"))

FIELDS = ["time", "ticker", "asset", "side", "secs_left", "price", "fee", "contracts",
          "status", "exit_price", "exit_fee", "exit_at", "exit_secs_left", "result", "pnl"]


def now_utc():
    return datetime.now(timezone.utc)


def book_fill(ticker, side, contracts):
    """Average price to buy `contracts` of `side` now, walking the order book."""
    try:
        book = kalshi_get(f"/markets/{ticker}/orderbook").get("orderbook_fp") or {}
    except Exception:
        return None
    levels = sorted((1 - float(p), float(q)) for p, q in
                    (book.get("no_dollars" if side == "yes" else "yes_dollars") or []) if float(q) > 0)
    need, cost = contracts, 0.0
    for px, qty in levels:
        take = min(need, qty)
        cost += take * px
        need -= take
        if need <= 1e-9:
            return round(cost / contracts, 4)
    return None


class Scalp:
    def __init__(self):
        self.trades = load_rows(TRADES)
        self.series = []
        self.markets = {}        # ticker -> close time
        self.streak = {}         # (ticker, side) -> time the ask entered the band
        self.errors = []
        self.last_series = self.last_refresh = 0.0

    def load_series(self):
        found = []
        for s in kalshi_get("/series", {}).get("series", []):
            t = s["ticker"]
            if s.get("category") == "Crypto" and (s.get("frequency") == "fifteen_min" or t.endswith("15M")) \
                    and not any(k in t for k in ("TEST", "CRYPTOLEAD", "CRYPTOCOMP")):
                found.append(t)
        self.series = found
        self.last_series = time.time()
        print(f"watching {len(found)} series: {sorted(asset_of(s) for s in found)}")

    def refresh(self):
        out = {}
        for st in self.series:
            try:
                for m in get_markets(max_pages=1, series_ticker=st, status="open"):
                    out[m["ticker"]] = parse_ts(m["close_time"])
            except Exception as exc:
                self.errors.append(f"{iso(now_utc())} refresh {st}: {exc}")
        self.markets = out
        self.last_refresh = time.time()

    def open_pos(self, ticker):
        for t in self.trades:
            if t["ticker"] == ticker and t["status"] == "open":
                return t
        return None

    def poll(self):
        now = now_utc()
        live = [t for t, c in self.markets.items() if c > now]
        quotes = {}
        for i in range(0, len(live), 50):
            data = kalshi_get("/markets", {"tickers": ",".join(live[i:i + 50]), "limit": 1000})
            quotes.update({m["ticker"]: m for m in data.get("markets", [])})
        for tk, m in quotes.items():
            secs_left = (self.markets[tk] - now).total_seconds()
            pos = self.open_pos(tk)
            if pos:
                bid, _ = side_quote(m, pos["side"])
                entry = float(pos["price"])
                if bid is not None and bid >= entry + TAKE_PROFIT - 1e-9 and secs_left > 1:
                    n = int(pos["contracts"])
                    xfee = fee_per_contract(bid, n)
                    pnl = n * (bid - xfee - entry - float(pos["fee"]))
                    pos.update(status="sold", exit_price=f"{bid:.4f}", exit_fee=f"{xfee:.4f}",
                               exit_at=iso(now), exit_secs_left=int(secs_left), pnl=f"{pnl:.2f}")
                    print(f"SELL {tk} {pos['side']} {entry:.2f}->{bid:.2f}  ${pnl:+.2f}")
                    self.streak.pop((tk, "yes"), None)
                    self.streak.pop((tk, "no"), None)
                continue
            for side in ("yes", "no"):
                _, ask = side_quote(m, side)
                key = (tk, side)
                if ask is None or not (LOW <= ask <= HIGH):
                    self.streak.pop(key, None)
                    continue
                start = self.streak.setdefault(key, now)
                if (now - start).total_seconds() < HOLD_SECONDS or secs_left < MIN_SECS_LEFT:
                    continue
                fill = book_fill(tk, side, CONTRACTS)
                if fill is None or fill > HIGH + 0.01:
                    continue
                self.trades.append({
                    "time": iso(now), "ticker": tk, "asset": asset_of(tk.split("-")[0]), "side": side,
                    "secs_left": int(secs_left), "price": f"{fill:.4f}",
                    "fee": f"{fee_per_contract(fill, CONTRACTS):.4f}", "contracts": CONTRACTS,
                    "status": "open"})
                print(f"BUY  {tk} {side} @ {fill:.2f} ({int(secs_left)}s left)")
                self.streak.pop((tk, "yes"), None)
                self.streak.pop((tk, "no"), None)
                break

    def settle(self):
        now = now_utc()
        for t in self.trades:
            if t["status"] != "open":
                continue
            close = self.markets.get(t["ticker"])
            if close and close > now:
                continue
            try:
                m = kalshi_get(f"/markets/{t['ticker']}")["market"]
            except Exception:
                continue
            res = m.get("result")
            if res not in ("yes", "no", "void") or m.get("status") not in ("settled", "finalized", "determined"):
                continue
            n, cost = int(t["contracts"]), float(t["price"]) + float(t["fee"])
            pnl = 0.0 if res == "void" else n * ((1.0 if res == t["side"] else 0.0) - cost)
            t.update(status="settled", result=res, pnl=f"{pnl:.2f}")

    def save(self):
        write_csv(TRADES, self.trades, FIELDS)
        with open(STATUS, "w") as fh:
            json.dump({"saved_at": iso(now_utc()), "windows_watched": len(self.markets),
                       "trades": len(self.trades), "errors": self.errors[-20:]}, fh, indent=1)
        write_page(self.trades)
        subprocess.run(["git", "add", "scalp", "SCALP.md"], cwd=HERE, capture_output=True)
        if subprocess.run(["git", "commit", "-q", "-m", "scalp update"], cwd=HERE,
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
    done = [t for t in trades if t["status"] in ("sold", "settled")]
    sold = [t for t in done if t["status"] == "sold"]
    held = [t for t in done if t["status"] == "settled"]
    pnl = sum(float(t["pnl"]) for t in done)
    risked = sum(int(t["contracts"]) * (float(t["price"]) + float(t["fee"])) for t in done)
    held_won = sum(1 for t in held if float(t["pnl"]) > 0)
    if len(done) < 20:
        verdict = "🟡 **Too early.** Needs at least 20 finished trades."
    elif pnl > 0:
        verdict = "🟢 **Making money** so far."
    else:
        verdict = "🔴 **Losing.** The +20¢ wins aren't covering the trades that never get there."
    lines = [
        "# Range-Scalp Bot", "",
        f"*Updated {datetime.now(timezone.utc):%a %b %d %H:%M} UTC. Paper money. Kalshi's 15-minute crypto "
        "up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 "
        "contracts, sell at +20¢, then look for the next one. Anything not sold rides to the close.*", "",
        "[← Back to all bots](README.md)", "",
        "## Verdict", "", verdict, "",
        "| Trades | Sold at +20¢ | Held to close (won) | Open | P&L | Return |",
        "|---|---|---|---|---|---|",
        f"| {len(done)} | {len(sold)} | {len(held)} ({held_won}) | "
        f"{sum(1 for t in trades if t['status'] == 'open')} | ${pnl:.2f} | "
        f"{(pnl / risked if risked else 0):+.1%} |", "",
        "## Latest trades", "",
        "| Time (UTC) | Coin | Side | Paid | Sold / result | P&L |",
        "|---|---|---|---|---|---|",
    ]
    for t in trades[-25:][::-1]:
        out = f"{float(t['exit_price']):.2f}" if t["status"] == "sold" else (t.get("result") or "open")
        lines.append(f"| {t['time'][5:16].replace('T', ' ')} | {t['asset']} | "
                     f"{'UP' if t['side'] == 'yes' else 'DOWN'} | {float(t['price']):.2f} | {out} | "
                     f"{t.get('pnl') or ''} |")
    with open(PAGE, "w") as fh:
        fh.write("\n".join(lines) + "\n")


def main():
    os.makedirs(DIR, exist_ok=True)
    bot = Scalp()
    end = time.time() + RUN_MINUTES * 60
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
        if time.time() - last_save > SAVE_MINUTES * 60:
            bot.save()
            last_save = time.time()
        time.sleep(POLL_SECONDS)
    bot.refresh()
    bot.settle()
    bot.save()


if __name__ == "__main__":
    sys.exit(main())
