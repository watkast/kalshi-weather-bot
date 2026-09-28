"""V8: the Trend Sniper rules on Kalshi's 1-hour crypto "above/below" markets.

Each hour Kalshi lists a ladder of strikes per coin ("BTC at or above
$84,250 at 5 PM ET?"), settled on the same 60-second index average as the
15-minute markets, so the same fair-value model applies. Scaled to an hour:

* 20-45 minutes left in the hour
* contract priced 25-55c (checked against the live order book)
* model edge 6c+ after fees
* one bet per coin per hour, never two bets in the same direction in the
  same hour, and at most 3 open bets at a time
"""
from datetime import datetime, timezone

from common import fee_per_contract, get_markets, price

SERIES = {"KXBTCD": "BTC", "KXETHD": "ETH", "KXSOLD": "SOL", "KXXRPD": "XRP",
          "KXDOGED": "DOGE", "KXBNBD": "BNB", "KXHYPED": "HYPE"}
MIN_SECS, MAX_SECS = 20 * 60, 45 * 60
MIN_PRICE, MAX_PRICE = 0.25, 0.55
EDGE = 0.06
MAX_OPEN = 3
STRIKES_EACH_SIDE = 4          # watch the strikes nearest the live price
REFRESH_SECONDS = 60
CHECK_SECONDS = 10


def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00")) if s else None


def strike_of(m):
    """Return the 'at or above' level for a market, or None if it isn't one."""
    if m.get("strike_type") == "greater" and m.get("floor_strike"):
        return float(m["floor_strike"])
    if m.get("strike_type") == "custom" and "above" in (m.get("yes_sub_title") or "") and "-T" in m["ticker"]:
        try:
            return float(m["ticker"].rsplit("-T", 1)[1])
        except ValueError:
            return None
    return None


class Hourly:
    def __init__(self, bot):
        self.bot = bot                 # the FairValue bot: prices, volatility, trades, helpers
        self.ladders = {}              # asset -> list of (strike, ticker, close)
        self.last_refresh = 0.0
        self.last_check = 0.0

    def refresh(self, now, spot):
        ladders = {}
        for series, a in SERIES.items():
            if a not in spot:
                continue
            try:
                ms = get_markets(max_pages=2, series_ticker=series, status="open")
            except Exception as exc:
                self.bot.errors.append(f"hourly {series}: {exc}")
                continue
            # Only the event that settles next (the current hour).
            upcoming = [m for m in ms if parse_ts(m.get("close_time")) and parse_ts(m["close_time"]) > now]
            if not upcoming:
                continue
            close = min(parse_ts(m["close_time"]) for m in upcoming)
            rungs = [(strike_of(m), m["ticker"], close) for m in upcoming
                     if parse_ts(m["close_time"]) == close and strike_of(m)]
            rungs.sort(key=lambda r: abs(r[0] - spot[a]))
            ladders[a] = rungs[:STRIKES_EACH_SIDE * 2]
        self.ladders = ladders
        self.last_refresh = now.timestamp()

    def check(self, now, spot, quotes_for, book_fill, fair_up, iso):
        if now.timestamp() - self.last_refresh > REFRESH_SECONDS:
            self.refresh(now, spot)
        if now.timestamp() - self.last_check < CHECK_SECONDS:
            return
        self.last_check = now.timestamp()
        book = self.bot.trades_v8
        tickers = [t for rungs in self.ladders.values() for _, t, _ in rungs]
        if not tickers:
            return
        q = quotes_for(tickers)
        open_n = sum(1 for t in book if t["status"] == "open")
        for a, rungs in self.ladders.items():
            if open_n >= MAX_OPEN or a not in spot:
                continue
            hour = rungs[0][1].split("-")[1] if rungs else ""
            if any(t["asset"] == a and t.get("window") == hour for t in book):
                continue                                     # one bet per coin per hour
            taken = {t["side"] for t in book if t.get("window") == hour}
            sig = self.bot.vol(a)
            if not sig:
                continue
            best = None
            for strike, ticker, close in rungs:
                m = q.get(ticker)
                secs_left = (close - now).total_seconds()
                if not m or m.get("status") not in ("active", "open") or not (MIN_SECS <= secs_left <= MAX_SECS):
                    continue
                p_up = fair_up(spot[a], strike, secs_left, sig, [])
                for side, p in (("yes", p_up), ("no", 1 - p_up)):
                    ask = price(m, "yes_ask" if side == "yes" else "no_ask")
                    if side in taken or ask is None or not (MIN_PRICE - 0.02 <= ask <= MAX_PRICE + 0.02):
                        continue
                    if p - ask - fee_per_contract(ask, 10) >= EDGE and (best is None or p - ask > best[0]):
                        best = (p - ask, ticker, side, p, ask, strike, secs_left)
            if not best:
                continue
            _, ticker, side, p, ask, strike, secs_left = best
            fill = book_fill(ticker, side, 10)
            if not fill or not (MIN_PRICE <= fill[0] <= MAX_PRICE):
                continue
            fee = fee_per_contract(fill[0], 10)
            edge = p - fill[0] - fee
            if edge < EDGE:
                continue
            book.append({"time": iso(now), "ticker": ticker, "asset": a, "side": side,
                         "secs_left": f"{secs_left:.0f}", "spot": f"{spot[a]:g}", "strike": strike,
                         "gap_pct": f"{(spot[a] - strike) / strike * 100:.4f}", "sigma_pct": f"{sig * 100:.4f}",
                         "model_p": f"{p:.4f}", "price": f"{fill[0]:.4f}", "fee": f"{fee:.4f}",
                         "edge": f"{edge:.4f}", "contracts": 10, "status": "open", "quoted": f"{ask:.2f}",
                         "depth_at_ask": f"{fill[2]:.0f}", "window": hour})
            open_n += 1
            print(f"V8 BUY {side} {ticker} @ {fill[0]:.2f} model {p:.0%} ({secs_left / 60:.0f} min left)")
