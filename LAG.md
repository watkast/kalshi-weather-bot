# Lag Tracker

*Updated Sun Oct 04 17:56 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$326.96** | -12.3% | 716 | $3.76 | $143.33 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 746 | 123 | -$313.40 | -11.2% | -$159.53 / -$153.87 |
| Sell after 30 sec | 745 | 194 | -$325.87 | -11.6% | -$182.06 / -$143.81 |
| Hold to the close | 716 | 234 | -$326.96 | -12.3% | -$365.22 / $38.26 |
| Hold, only edge 10¢+ | 254 | 60 | -$124.42 | -17.2% | -$151.31 / $26.89 |
| Hold, first trade per window only | 233 | 88 | -$60.45 | -6.4% | -$93.25 / $32.80 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 2799 | 10% | 67% | +4.6¢ | 0.3¢ | edge gone 1917, price out of range 74, spread too wide 62 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 717 | 11.1s | 3% | 0% |
| BTC | 845 | 11.9s | 3% | 0% |
| DOGE | 941 | 10.7s | 3% | 0% |
| ETH | 1036 | 10.8s | 4% | 0% |
| HYPE | 720 | 11.6s | 3% | 0% |
| NEAR | 984 | 10.8s | 3% | 0% |
| SOL | 1827 | 10.8s | 3% | 0% |
| XRP | 1891 | 11.2s | 3% | 0% |
| ZEC | 1105 | 9.6s | 4% | 0% |
| **All** | **10066** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **7 ms** · Order book check: **26 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 17:56:11 | ETH | down | 0.13→0.07 | 0.92 → 0.94 | no | edge gone |  |
| 10-04 17:56:01 | XRP | down | 0.22→0.16 | 0.80 → 0.85 | 3.04s | edge gone |  |
| 10-04 17:55:57 | ZEC | down | 0.69→0.63 | 0.18 → 0.28 | 7.29s | DOWN @ 0.28 | -1.16 / · / · |
| 10-04 17:55:36 | XRP | up | 0.23→0.30 | 0.25 → 0.24 | no | UP @ 0.25 | -0.85 / -1.23 / · |
| 10-04 17:55:21 | XRP | down | 0.31→0.21 | 0.76 → 0.76 | no | edge gone |  |
| 10-04 17:55:17 | ETH | up | 0.20→0.26 | 0.12 → 0.23 | no | edge gone |  |
| 10-04 17:55:10 | ZEC | up | 0.53→0.58 | 0.80 → 0.77 | no | edge gone |  |
| 10-04 17:55:03 | XRP | down | 0.25→0.19 | 0.70 → 0.78 | 2.58s | edge gone |  |
| 10-04 17:54:49 | ETH | up | 0.22→0.27 | 0.19 → 0.14 | no | UP @ 0.14 | -0.37 / -0.37 / · |
| 10-04 17:54:48 | XRP | up | 0.28→0.35 | 0.34 → 0.31 | no | edge gone |  |
| 10-04 17:54:47 | ZEC | down | 0.64→0.58 | 0.24 → 0.30 | 3.08s | DOWN @ 0.30 | -1.17 / -1.36 / · |
| 10-04 17:54:41 | DOGE | down | 0.14→0.04 | 0.88 → 0.92 | 24.09s | DOWN @ 0.92 | 0.16 / 0.23 / · |
| 10-04 17:54:32 | XRP | up | 0.29→0.36 | 0.32 → 0.34 | no | edge gone |  |
| 10-04 17:54:15 | XRP | down | 0.33→0.27 | 0.75 → 0.68 | no | DOWN @ 0.69 | -0.57 / -0.06 / · |
| 10-04 17:54:02 | ZEC | down | 0.63→0.57 | 0.31 → 0.32 | no | DOWN @ 0.32 | -1.23 / -1.29 / · |
| 10-04 17:54:00 | XRP | down | 0.27→0.22 | 0.70 → 0.73 | 5.34s | DOWN @ 0.73 | -0.49 / -1.00 / · |
| 10-04 17:54:00 | ETH | down | 0.29→0.21 | 0.79 → 0.88 | no | edge gone |  |
| 10-04 17:54:00 | DOGE | down | 0.22→0.15 | 0.87 → 0.89 | no | edge gone |  |
| 10-04 17:53:35 | ZEC | down | 0.65→0.60 | 0.25 → 0.27 | 0.10s | DOWN @ 0.27 | -0.23 / -0.54 / · |
| 10-04 17:53:27 | XRP | up | 0.25→0.34 | 0.53 → 0.39 | no | edge gone |  |
| 10-04 17:53:23 | BTC | down | 0.17→0.04 | 0.81 → 0.88 | 12.11s | DOWN @ 0.88 | 0.12 / 0.24 / · |
| 10-04 17:53:23 | DOGE | down | 0.35→0.22 | 0.66 → 0.79 | 12.11s | edge gone |  |
| 10-04 17:53:23 | ETH | down | 0.43→0.30 | 0.58 → 0.75 | 12.36s | edge gone |  |
| 10-04 17:53:23 | SOL | down | 0.12→0.06 | 0.81 → 0.83 | 27.36s | DOWN @ 0.83 | 0.22 / 0.32 / · |
| 10-04 17:53:12 | XRP | down | 0.60→0.50 | 0.38 → 0.40 | 8.61s | DOWN @ 0.40 | -0.64 / 2.47 / · |
| 10-04 17:53:06 | BTC | down | 0.28→0.20 | 0.77 → 0.78 | 29.12s | edge gone |  |
| 10-04 17:53:04 | SOL | down | 0.16→0.10 | 0.86 → 0.87 | no | edge gone |  |
| 10-04 17:52:57 | XRP | up | 0.50→0.56 | 0.53 → 0.59 | 8.61s | edge gone |  |
| 10-04 17:52:31 | ETH | down | 0.55→0.48 | 0.49 → 0.61 | 19.62s | edge gone |  |
| 10-04 17:52:27 | XRP | up | 0.38→0.50 | 0.33 → 0.54 | 8.37s | edge gone |  |
