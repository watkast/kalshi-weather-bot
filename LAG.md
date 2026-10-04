# Lag Tracker

*Updated Sun Oct 04 11:44 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$107.98** | -20.8% | 148 | $3.49 | $83.77 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 159 | 28 | -$67.85 | -12.2% | -$32.40 / -$35.45 |
| Sell after 30 sec | 159 | 38 | -$69.15 | -12.5% | -$32.85 / -$36.30 |
| Hold to the close | 148 | 41 | -$107.98 | -20.8% | $9.07 / -$117.05 |
| Hold, only edge 10¢+ | 49 | 4 | -$79.36 | -66.5% | -$31.43 / -$47.93 |
| Hold, first trade per window only | 56 | 20 | -$18.55 | -8.5% | -$4.65 / -$13.90 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 636 | 11% | 65% | +5.0¢ | 0.3¢ | edge gone 447, price out of range 24, spread too wide 6 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 652 | 11.1s | 3% | 0% |
| BTC | 590 | 11.9s | 3% | 0% |
| DOGE | 766 | 10.5s | 2% | 0% |
| ETH | 756 | 10.9s | 4% | 0% |
| HYPE | 622 | 11.2s | 4% | 0% |
| NEAR | 772 | 10.8s | 4% | 0% |
| SOL | 1410 | 10.8s | 3% | 0% |
| XRP | 1430 | 11.0s | 4% | 0% |
| ZEC | 905 | 9.6s | 4% | 0% |
| **All** | **7903** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 11:41:35 | HYPE | up | 0.37→0.42 | 0.36 → 0.28 | no | UP @ 0.28 | -0.49 / 0.30 / · |
| 10-04 11:40:36 | ZEC | up | 0.08→0.13 | 0.11 → 0.08 | no | UP @ 0.08 | -0.48 / -0.44 / · |
| 10-04 11:40:30 | BTC | down | 0.11→0.06 | 0.90 → 0.95 | 4.78s | edge gone |  |
| 10-04 11:38:50 | BTC | down | 0.16→0.09 | 0.93 → 0.93 | 14.56s | edge gone |  |
| 10-04 11:38:07 | BTC | down | 0.30→0.21 | 0.72 → 0.80 | 12.57s | edge gone |  |
| 10-04 11:37:53 | XRP | down | 0.23→0.17 | 0.83 → 0.84 | no | edge gone |  |
| 10-04 11:37:36 | ZEC | down | 0.39→0.33 | 0.73 → 0.78 | 29.08s | edge gone |  |
| 10-04 11:36:44 | SOL | up | 0.07→0.15 | 0.14 → 0.14 | no | edge gone |  |
| 10-04 11:35:50 | XRP | up | 0.17→0.23 | 0.19 → 0.19 | no | UP @ 0.19 | -0.36 / -0.60 / · |
| 10-04 11:35:47 | HYPE | up | 0.37→0.42 | 0.56 → 0.52 | no | edge gone |  |
| 10-04 11:35:35 | XRP | up | 0.17→0.23 | 0.19 → 0.20 | no | edge gone |  |
| 10-04 11:35:32 | HYPE | up | 0.31→0.37 | 0.52 → 0.42 | 2.36s | edge gone |  |
| 10-04 11:35:18 | DOGE | up | 0.20→0.26 | 0.22 → 0.20 | no | UP @ 0.20 | -0.62 / -0.62 / · |
| 10-04 11:35:08 | BTC | down | 0.48→0.43 | 0.50 → 0.55 | 11.87s | edge gone |  |
| 10-04 11:34:32 | DOGE | up | 0.26→0.34 | 0.24 → 0.26 | no | UP @ 0.26 | -0.57 / -0.73 / · |
| 10-04 11:33:58 | XRP | up | 0.21→0.28 | 0.24 → 0.25 | 6.53s | edge gone |  |
| 10-04 11:33:45 | SOL | down | 0.31→0.24 | 0.65 → 0.75 | 4.53s | edge gone |  |
| 10-04 11:33:45 | BTC | down | 0.52→0.45 | 0.41 → 0.55 | 20.04s | edge gone |  |
| 10-04 11:33:43 | ETH | down | 0.33→0.24 | 0.65 → 0.75 | 6.28s | edge gone |  |
| 10-04 11:33:40 | XRP | down | 0.29→0.24 | 0.77 → 0.77 | no | edge gone |  |
| 10-04 11:33:18 | ZEC | down | 0.35→0.29 | 0.66 → 0.73 | 1.28s | edge gone |  |
| 10-04 11:33:11 | DOGE | up | 0.22→0.31 | 0.22 → 0.25 | no | UP @ 0.25 | -0.57 / -0.08 / · |
| 10-04 11:32:58 | BTC | up | 0.44→0.52 | 0.46 → 0.56 | 6.79s | edge gone |  |
| 10-04 11:32:53 | XRP | up | 0.24→0.30 | 0.23 → 0.24 | 11.29s | UP @ 0.24 | -0.17 / -0.26 / · |
| 10-04 11:32:39 | BTC | down | 0.52→0.46 | 0.44 → 0.58 | 11.05s | edge gone |  |
| 10-04 11:32:38 | SOL | down | 0.48→0.43 | 0.50 → 0.58 | 11.30s | edge gone |  |
| 10-04 11:32:38 | XRP | down | 0.32→0.26 | 0.68 → 0.79 | 11.30s | edge gone |  |
| 10-04 11:32:38 | ETH | down | 0.65→0.47 | 0.43 → 0.61 | 11.30s | edge gone |  |
| 10-04 11:32:12 | DOGE | down | 0.38→0.25 | 0.61 → 0.75 | 7.55s | edge gone |  |
| 10-04 11:32:10 | SOL | down | 0.51→0.43 | 0.44 → 0.50 | 9.80s | DOWN @ 0.50 | -0.46 / 0.50 / · |
