# Lag Tracker

*Updated Sun Oct 04 22:07 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$83.75** | -1.8% | 1157 | $3.97 | $185.87 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1158 | 197 | -$492.58 | -10.7% | -$241.53 / -$251.05 |
| Sell after 30 sec | 1158 | 309 | -$524.40 | -11.4% | -$263.04 / -$261.36 |
| Hold to the close | 1157 | 451 | -$83.75 | -1.8% | -$345.65 / $261.90 |
| Hold, only edge 10¢+ | 399 | 113 | -$143.92 | -11.3% | -$101.06 / -$42.86 |
| Hold, first trade per window only | 358 | 149 | -$29.27 | -1.9% | -$101.27 / $72.00 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 4277 | 10% | 66% | +4.0¢ | 0.3¢ | edge gone 2917, price out of range 107, spread too wide 95 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 784 | 11.1s | 3% | 0% |
| BTC | 995 | 11.8s | 3% | 0% |
| DOGE | 1075 | 10.8s | 3% | 0% |
| ETH | 1209 | 10.8s | 4% | 0% |
| HYPE | 796 | 11.6s | 3% | 0% |
| NEAR | 1153 | 10.8s | 3% | 0% |
| SOL | 2101 | 10.9s | 3% | 0% |
| XRP | 2183 | 11.1s | 3% | 0% |
| ZEC | 1248 | 9.8s | 4% | 0% |
| **All** | **11544** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **7 ms** · Order book check: **61 ms** · Coinbase price delay: **35 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 22:05:53 | DOGE | down | 0.90→0.84 | 0.10 → 0.14 | 10.69s | edge gone |  |
| 10-04 22:02:15 | BTC | up | 0.89→0.95 | 0.82 → 0.89 | 4.25s | UP @ 0.89 | -0.14 / -0.14 / · |
| 10-04 22:02:15 | BNB | up | 0.72→0.79 | 0.80 → 0.91 | 4.25s | edge gone |  |
| 10-04 22:01:25 | BTC | down | 0.86→0.81 | 0.18 → 0.20 | no | edge gone |  |
| 10-04 22:01:24 | SOL | down | 0.93→0.86 | 0.17 → 0.19 | no | edge gone |  |
| 10-04 22:00:55 | NEAR | up | 0.79→0.84 | 0.83 → 0.89 | 19.53s | edge gone |  |
| 10-04 22:00:40 | DOGE | up | 0.69→0.76 | 0.68 → 0.75 | 5.03s | edge gone |  |
| 10-04 22:00:33 | NEAR | up | 0.65→0.72 | 0.77 → 0.81 | 11.78s | edge gone |  |
| 10-04 21:58:26 | ZEC | down | 0.14→0.08 | 0.91 → 0.97 | 2.54s | price out of range |  |
| 10-04 21:58:06 | ZEC | up | 0.24→0.33 | 0.25 → 0.32 | no | edge gone |  |
| 10-04 21:57:48 | ZEC | down | 0.35→0.28 | 0.84 → 0.87 | 25.55s | edge gone |  |
| 10-04 21:57:33 | ZEC | down | 0.39→0.29 | 0.54 → 0.85 | 10.55s | edge gone |  |
| 10-04 21:57:32 | BTC | down | 0.09→0.03 | 0.94 → 0.98 | 12.05s | price out of range |  |
| 10-04 21:57:21 | XRP | down | 0.12→0.07 | 0.91 → 0.95 | 22.31s | edge gone |  |
| 10-04 21:57:12 | BTC | down | 0.16→0.09 | 0.85 → 0.92 | 2.05s | edge gone |  |
| 10-04 21:57:06 | XRP | down | 0.31→0.25 | 0.75 → 0.85 | 7.31s | edge gone |  |
| 10-04 21:57:06 | ZEC | down | 0.87→0.79 | 0.01 → 0.04 | 7.31s | price out of range |  |
| 10-04 21:56:46 | XRP | up | 0.35→0.41 | 0.35 → 0.30 | no | UP @ 0.30 | -0.79 / -2.22 / -3.15 |
| 10-04 21:56:31 | XRP | down | 0.41→0.35 | 0.69 → 0.69 | 27.55s | edge gone |  |
| 10-04 21:56:26 | BTC | up | 0.20→0.26 | 0.12 → 0.23 | 3.04s | edge gone |  |
| 10-04 21:56:06 | XRP | up | 0.16→0.25 | 0.12 → 0.15 | 22.55s | UP @ 0.15 | 1.16 / 1.40 / -1.59 |
| 10-04 21:56:03 | NEAR | down | 0.15→0.10 | 0.74 → 0.87 | 10.29s | edge gone |  |
| 10-04 21:55:41 | XRP | down | 0.42→0.35 | 0.65 → 0.80 | 3.04s | edge gone |  |
| 10-04 21:55:30 | HYPE | down | 0.39→0.32 | 0.52 → 0.56 | 28.55s | DOWN @ 0.56 | -0.36 / 0.35 / 4.22 |
| 10-04 21:55:30 | SOL | down | 0.12→0.06 | 0.92 → 0.93 | 29.05s | edge gone |  |
| 10-04 21:55:17 | XRP | up | 0.33→0.42 | 0.25 → 0.39 | 12.04s | edge gone |  |
| 10-04 21:55:15 | DOGE | down | 0.17→0.12 | 0.83 → 0.89 | 0.26s | edge gone |  |
| 10-04 21:54:55 | BTC | down | 0.15→0.10 | 0.88 → 0.93 | 3.29s | edge gone |  |
| 10-04 21:54:53 | XRP | down | 0.52→0.43 | 0.47 → 0.47 | 20.80s | DOWN @ 0.47 | 0.74 / 1.46 / 5.12 |
| 10-04 21:54:52 | NEAR | down | 0.29→0.23 | 0.59 → 0.66 | 6.54s | DOWN @ 0.66 | -0.53 / -0.42 / 3.24 |
