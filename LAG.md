# Lag Tracker

*Updated Sun Oct 04 10:14 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🟡 **Testing with real order-book fills.** 34 of 150 settled trades needed before calling it. The earlier results below used quoted prices, which may not have been fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$5.88** | -4.0% | 34 | $3.78 | $83.77 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 58 | 14 | -$22.05 | -10.1% | -$6.80 / -$15.25 |
| Sell after 30 sec | 58 | 12 | -$30.54 | -13.9% | -$11.78 / -$18.76 |
| Hold to the close | 34 | 14 | -$5.88 | -4.0% | -$2.11 / -$3.77 |
| Hold, only edge 10¢+ | 9 | 1 | -$15.83 | -61.3% | -$8.39 / -$7.44 |
| Hold, first trade per window only | 16 | 6 | -$10.24 | -14.6% | -$9.87 / -$0.37 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 256 | 9% | 70% | +6.0¢ | 0.2¢ | edge gone 185, price out of range 10, spread too wide 3 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 647 | 11.1s | 3% | 0% |
| BTC | 559 | 11.9s | 3% | 0% |
| DOGE | 739 | 10.6s | 2% | 0% |
| ETH | 723 | 11.2s | 4% | 0% |
| HYPE | 601 | 11.3s | 4% | 0% |
| NEAR | 727 | 10.8s | 4% | 0% |
| SOL | 1327 | 11.0s | 3% | 0% |
| XRP | 1328 | 10.9s | 4% | 0% |
| ZEC | 872 | 9.6s | 4% | 0% |
| **All** | **7523** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 10:13:44 | BTC | down | 0.16→0.10 | 0.78 → 0.87 | 0.26s | edge gone |  |
| 10-04 10:13:42 | SOL | down | 0.85→0.79 | 0.08 → 0.05 | no | DOWN @ 0.05 | -0.33 / -0.53 / · |
| 10-04 10:13:27 | SOL | up | 0.81→0.90 | 0.92 → 0.93 | no | edge gone |  |
| 10-04 10:13:25 | XRP | up | 0.71→0.84 | 0.90 → 0.90 | no | edge gone |  |
| 10-04 10:13:22 | ETH | up | 0.42→0.53 | 0.44 → 0.44 | no | UP @ 0.44 | -1.63 / -0.56 / · |
| 10-04 10:13:18 | BTC | down | 0.30→0.22 | 0.63 → 0.74 | 11.03s | edge gone |  |
| 10-04 10:13:04 | ETH | down | 0.74→0.46 | 0.26 → 0.56 | 9.53s | edge gone |  |
| 10-04 10:13:03 | BTC | down | 0.59→0.41 | 0.22 → 0.63 | 11.28s | edge gone |  |
| 10-04 10:13:02 | SOL | down | 0.92→0.86 | 0.03 → 0.07 | 11.53s | DOWN @ 0.07 | 0.01 / -0.18 / · |
| 10-04 10:12:45 | SOL | down | 0.92→0.87 | 0.05 → 0.04 | 28.54s | price out of range |  |
| 10-04 10:12:43 | XRP | down | 0.86→0.77 | 0.10 → 0.18 | no | DOWN @ 0.18 | -0.79 / -0.79 / · |
| 10-04 10:12:37 | ETH | down | 0.76→0.69 | 0.30 → 0.29 | no | edge gone |  |
| 10-04 10:12:18 | XRP | down | 0.85→0.80 | 0.11 → 0.11 | no | DOWN @ 0.11 | -0.51 / -0.05 / · |
| 10-04 10:12:18 | ETH | down | 0.75→0.68 | 0.32 → 0.33 | no | edge gone |  |
| 10-04 10:12:16 | NEAR | down | 0.81→0.75 | 0.07 → 0.06 | no | DOWN @ 0.06 | -0.59 / -0.64 / · |
| 10-04 10:12:12 | SOL | up | 0.83→0.89 | 0.93 → 0.93 | no | edge gone |  |
| 10-04 10:11:49 | SOL | up | 0.78→0.84 | 0.90 → 0.93 | 24.56s | edge gone |  |
| 10-04 10:11:36 | XRP | down | 0.86→0.79 | 0.11 → 0.13 | 7.56s | DOWN @ 0.13 | 0.03 / -0.34 / · |
| 10-04 10:11:12 | NEAR | down | 0.86→0.74 | 0.13 → 0.16 | no | DOWN @ 0.16 | -0.54 / -1.13 / · |
| 10-04 10:10:52 | XRP | down | 0.87→0.81 | 0.11 → 0.18 | 6.32s | edge gone |  |
| 10-04 10:10:49 | NEAR | down | 0.84→0.75 | 0.06 → 0.13 | 10.07s | DOWN @ 0.13 | -0.58 / -0.42 / · |
| 10-04 10:10:36 | ETH | down | 0.82→0.75 | 0.29 → 0.27 | no | edge gone |  |
| 10-04 10:10:32 | NEAR | down | 0.96→0.90 | 0.04 → 0.04 | 26.58s | price out of range |  |
| 10-04 10:10:20 | XRP | down | 0.92→0.87 | 0.08 → 0.14 | 23.83s | edge gone |  |
| 10-04 10:10:09 | SOL | up | 0.79→0.86 | 0.87 → 0.90 | no | edge gone |  |
| 10-04 10:09:57 | XRP | down | 0.90→0.84 | 0.09 → 0.10 | no | DOWN @ 0.10 | -0.32 / -0.01 / · |
| 10-04 10:09:56 | BTC | down | 0.71→0.66 | 0.21 → 0.32 | 18.08s | spread too wide |  |
| 10-04 10:09:55 | NEAR | down | 0.81→0.73 | 0.06 → 0.13 | no | DOWN @ 0.13 | -1.03 / -1.29 / · |
| 10-04 10:09:53 | ETH | down | 0.83→0.77 | 0.19 → 0.20 | no | edge gone |  |
| 10-04 10:09:50 | SOL | down | 0.88→0.81 | 0.09 → 0.14 | 8.86s | DOWN @ 0.14 | -0.18 / 0.30 / · |
