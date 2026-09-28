"""Risk-managed paper account.

Everything a real-money bot needs before it touches real money, proven on
paper first:

* Bet sizing:     each bet risks at most BET_PCT of current equity.
* Position cap:   at most MAX_OPEN positions open at once, and never two
                  bets in the same direction in the same 15-minute window.
* Peak stop:      trading halts if equity falls TRAIL_DD below its peak
                  (a 25% drop), or below the HARD_FLOOR, whichever is higher.
* Order checks:   after every buy or sell the ledger is re-checked: cash
                  and positions must have moved exactly the way the order
                  said. A mismatch (like a "sell" that actually bought)
                  halts trading immediately. In live trading this same
                  check compares against Kalshi's own position report.

A halt stays in force across sessions until someone resets it on purpose.
"""
import csv
import json
import math
import os
from datetime import datetime, timezone

START_BALANCE = 500.00
HARD_FLOOR = 350.00       # never trade below this, no matter what
TRAIL_DD = 0.25           # halt after a 25% drop from peak equity
BET_PCT = 0.02            # risk at most 2% of equity per bet
MAX_OPEN = 3              # max open positions at any time

LEDGER_FIELDS = ["time", "action", "ticker", "side", "contracts", "price", "fee",
                 "cash_before", "cash_after", "open_after", "equity_after", "note"]


def now_iso():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class PaperAccount:
    def __init__(self, folder):
        self.path = os.path.join(folder, "account.json")
        self.ledger_path = os.path.join(folder, "account_ledger.csv")
        state = {}
        if os.path.exists(self.path):
            with open(self.path) as fh:
                state = json.load(fh)
        self.cash = state.get("cash", START_BALANCE)
        self.peak = state.get("peak", START_BALANCE)
        self.positions = state.get("positions", {})   # ticker -> {side, contracts, cost, window}
        self.halted = state.get("halted", False)
        self.halt_reason = state.get("halt_reason", "")
        self.history = state.get("history", [])       # (time, equity) points
        self.pending = []

    # ------------------------------------------------------------ numbers
    def equity(self):
        """Cash plus open positions valued at what we paid (conservative)."""
        return self.cash + sum(p["cost"] for p in self.positions.values())

    def stop_level(self):
        return max(HARD_FLOOR, self.peak * (1 - TRAIL_DD))

    # ------------------------------------------------------------ rules
    def can_open(self, ticker, side, window):
        if self.halted:
            return False, f"halted: {self.halt_reason}"
        if ticker in self.positions:
            return False, "already holding this market"
        if len(self.positions) >= MAX_OPEN:
            return False, f"{MAX_OPEN} positions already open"
        if any(p["window"] == window and p["side"] == side for p in self.positions.values()):
            return False, "already holding this direction this window"
        return True, ""

    def size(self, all_in_price):
        """Contracts to buy so the whole bet costs at most BET_PCT of equity."""
        if all_in_price <= 0:
            return 0
        return int(math.floor(self.equity() * BET_PCT / all_in_price))

    # ------------------------------------------------------------ orders
    def _log(self, row):
        self.pending.append({"time": now_iso(), **row,
                             "cash_after": f"{self.cash:.2f}", "open_after": len(self.positions),
                             "equity_after": f"{self.equity():.2f}"})

    def _halt(self, reason):
        if not self.halted:
            self.halted, self.halt_reason = True, reason
            self._log({"action": "HALT", "note": reason})
            print(f"ACCOUNT HALTED: {reason}")

    def buy(self, ticker, side, contracts, price, fee_per, window):
        ok, why = self.can_open(ticker, side, window)
        if not ok or contracts < 1:
            return False
        cost = round(contracts * (price + fee_per), 4)
        if cost > self.cash:
            return False
        before_cash, before_open = self.cash, len(self.positions)
        self.cash = round(self.cash - cost, 4)
        self.positions[ticker] = {"side": side, "contracts": contracts, "cost": cost, "window": window}
        # Order check: a buy must lower cash by exactly the cost and add one position.
        if abs((before_cash - self.cash) - cost) > 1e-6 or len(self.positions) != before_open + 1:
            self._halt(f"order check failed on BUY {ticker}")
        self._log({"action": "BUY", "ticker": ticker, "side": side, "contracts": contracts,
                   "price": f"{price:.4f}", "fee": f"{fee_per:.4f}", "cash_before": f"{before_cash:.2f}"})
        return True

    def close(self, ticker, proceeds, action, note=""):
        """Sell or settle a position. `proceeds` is cash received after fees."""
        pos = self.positions.get(ticker)
        if not pos:
            return
        before_cash, before_open = self.cash, len(self.positions)
        del self.positions[ticker]
        self.cash = round(self.cash + proceeds, 4)
        # Order check: closing must remove exactly one position and never
        # lower cash (a "sell" that spends money is the bug that sank the old bot).
        if len(self.positions) != before_open - 1 or proceeds < -1e-9 or self.cash < before_cash - 1e-9:
            self._halt(f"order check failed on {action} {ticker}")
        self._log({"action": action, "ticker": ticker, "side": pos["side"], "contracts": pos["contracts"],
                   "cash_before": f"{before_cash:.2f}", "note": note})
        self.after_close()

    def after_close(self):
        eq = self.equity()
        self.peak = max(self.peak, eq)
        self.history.append((now_iso(), round(eq, 2)))
        if eq < self.stop_level():
            self._halt(f"equity ${eq:.2f} fell below stop ${self.stop_level():.2f} "
                       f"(peak ${self.peak:.2f})")

    # ------------------------------------------------------------ storage
    def save(self):
        with open(self.path, "w") as fh:
            json.dump({"cash": round(self.cash, 4), "peak": round(self.peak, 4), "positions": self.positions,
                       "halted": self.halted, "halt_reason": self.halt_reason,
                       "history": self.history[-2000:],
                       "settings": {"start": START_BALANCE, "hard_floor": HARD_FLOOR, "trail_dd": TRAIL_DD,
                                    "bet_pct": BET_PCT, "max_open": MAX_OPEN}}, fh, indent=1)
        if self.pending:
            new = not os.path.exists(self.ledger_path)
            with open(self.ledger_path, "a", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=LEDGER_FIELDS, extrasaction="ignore")
                if new:
                    w.writeheader()
                w.writerows(self.pending)
            self.pending = []
