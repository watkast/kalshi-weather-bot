# Lag Tracker

*Updated Sun Oct 04 13:45 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$379.29** | -30.9% | 337 | $3.66 | $122.22 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 345 | 63 | -$142.86 | -11.3% | -$73.77 / -$69.09 |
| Sell after 30 sec | 345 | 83 | -$168.04 | -13.3% | -$76.05 / -$91.99 |
| Hold to the close | 337 | 85 | -$379.29 | -30.9% | -$136.43 / -$242.86 |
| Hold, only edge 10¢+ | 121 | 17 | -$156.52 | -47.9% | -$111.15 / -$45.37 |
| Hold, first trade per window only | 119 | 39 | -$78.97 | -16.8% | -$14.43 / -$64.54 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 1310 | 10% | 65% | +5.0¢ | 0.3¢ | edge gone 901, price out of range 37, spread too wide 27 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 675 | 11.1s | 3% | 0% |
| BTC | 683 | 11.9s | 3% | 0% |
| DOGE | 800 | 10.5s | 2% | 0% |
| ETH | 838 | 11.2s | 4% | 0% |
| HYPE | 652 | 11.3s | 4% | 0% |
| NEAR | 839 | 10.8s | 4% | 0% |
| SOL | 1558 | 10.9s | 3% | 0% |
| XRP | 1558 | 11.0s | 4% | 0% |
| ZEC | 974 | 9.6s | 4% | 0% |
| **All** | **8577** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 13:45:34 | BTC | down | 0.42→0.36 | 0.54 → 0.61 | no | edge gone |  |
| 10-04 13:43:42 | BTC | down | 0.80→0.61 | 0.14 → 0.25 | 8.51s | DOWN @ 0.25 | 0.40 / -2.23 / · |
| 10-04 13:43:42 | ETH | up | 0.27→0.43 | 0.28 → 0.08 | no | UP @ 0.08 | -0.48 / -0.72 / · |
| 10-04 13:43:27 | BTC | down | 0.88→0.83 | 0.09 → 0.16 | 8.51s | edge gone |  |
| 10-04 13:43:27 | ETH | down | 0.58→0.43 | 0.46 → 0.75 | 9.01s | edge gone |  |
| 10-04 13:43:04 | BTC | up | 0.62→0.79 | 0.26 → 0.81 | 16.27s | edge gone |  |
| 10-04 13:43:02 | ZEC | up | 0.89→0.96 | 0.81 → 0.97 | 3.77s | price out of range |  |
| 10-04 13:43:02 | XRP | up | 0.75→0.87 | 0.77 → 0.92 | 19.02s | UP @ 0.92 | 0.16 / 0.47 / · |
| 10-04 13:43:02 | ETH | up | 0.07→0.25 | 0.05 → 0.58 | 19.02s | edge gone |  |
| 10-04 13:43:00 | SOL | up | 0.86→0.95 | 0.88 → 0.91 | 20.27s | UP @ 0.91 | 0.52 / 0.70 / · |
| 10-04 13:42:49 | BTC | up | 0.23→0.29 | 0.19 → 0.25 | 1.27s | edge gone |  |
| 10-04 13:42:34 | XRP | down | 0.76→0.68 | 0.19 → 0.27 | 1.27s | edge gone |  |
| 10-04 13:42:27 | ETH | down | 0.17→0.10 | 0.82 → 0.94 | 8.53s | edge gone |  |
| 10-04 13:42:17 | SOL | down | 0.95→0.88 | 0.09 → 0.13 | 18.78s | edge gone |  |
| 10-04 13:42:17 | BTC | down | 0.38→0.25 | 0.57 → 0.72 | 18.78s | edge gone |  |
| 10-04 13:42:13 | XRP | down | 0.84→0.78 | 0.09 → 0.19 | 7.78s | edge gone |  |
| 10-04 13:42:04 | ZEC | up | 0.72→0.77 | 0.84 → 0.88 | 1.28s | edge gone |  |
| 10-04 13:42:03 | NEAR | up | 0.78→0.84 | 0.94 → 0.95 | 17.79s | price out of range |  |
| 10-04 13:41:52 | ETH | down | 0.16→0.11 | 0.85 → 0.91 | no | edge gone |  |
| 10-04 13:41:47 | XRP | up | 0.85→0.90 | 0.90 → 0.90 | no | edge gone |  |
| 10-04 13:41:46 | BTC | down | 0.46→0.37 | 0.42 → 0.53 | 4.78s | DOWN @ 0.53 | -0.06 / 0.04 / · |
| 10-04 13:41:31 | ZEC | up | 0.77→0.84 | 0.88 → 0.89 | 4.53s | edge gone |  |
| 10-04 13:41:30 | BTC | down | 0.58→0.49 | 0.51 → 0.52 | no | edge gone |  |
| 10-04 13:41:30 | XRP | down | 0.94→0.89 | 0.10 → 0.11 | no | edge gone |  |
| 10-04 13:41:20 | ETH | up | 0.25→0.30 | 0.33 → 0.31 | no | edge gone |  |
| 10-04 13:41:15 | XRP | down | 0.90→0.83 | 0.11 → 0.13 | no | DOWN @ 0.13 | -0.76 / -0.46 / · |
| 10-04 13:41:13 | ZEC | down | 0.88→0.78 | 0.08 → 0.18 | 8.03s | DOWN @ 0.18 | -1.25 / -0.69 / · |
| 10-04 13:41:11 | SOL | down | 0.95→0.88 | 0.06 → 0.15 | 9.53s | edge gone |  |
| 10-04 13:41:09 | BTC | down | 0.68→0.58 | 0.18 → 0.39 | 12.03s | edge gone |  |
| 10-04 13:40:58 | ETH | up | 0.26→0.33 | 0.41 → 0.32 | no | edge gone |  |
