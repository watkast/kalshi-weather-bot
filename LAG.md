# Lag Tracker

*Updated Sun Oct 04 10:44 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🟡 **Testing with real order-book fills.** 74 of 150 settled trades needed before calling it. The earlier results below used quoted prices, which may not have been fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **$9.07** | +3.1% | 74 | $3.94 | $83.77 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 88 | 22 | -$30.59 | -8.8% | -$14.79 / -$15.80 |
| Sell after 30 sec | 88 | 28 | -$30.57 | -8.8% | -$24.19 / -$6.38 |
| Hold to the close | 74 | 30 | $9.07 | +3.1% | -$11.90 / $20.97 |
| Hold, only edge 10¢+ | 18 | 2 | -$23.31 | -53.8% | -$15.83 / -$7.48 |
| Hold, first trade per window only | 31 | 14 | $2.73 | +2.0% | -$8.54 / $11.27 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 385 | 9% | 70% | +5.1¢ | 0.2¢ | edge gone 275, price out of range 18, spread too wide 4 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 650 | 11.1s | 3% | 0% |
| BTC | 568 | 11.9s | 3% | 0% |
| DOGE | 752 | 10.5s | 2% | 0% |
| ETH | 732 | 11.0s | 4% | 0% |
| HYPE | 604 | 11.4s | 4% | 0% |
| NEAR | 738 | 10.8s | 4% | 0% |
| SOL | 1356 | 10.9s | 3% | 0% |
| XRP | 1371 | 10.9s | 4% | 0% |
| ZEC | 881 | 9.6s | 4% | 0% |
| **All** | **7652** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **34 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 10:43:38 | XRP | up | 0.82→0.91 | 0.95 → 0.96 | 27.57s | price out of range |  |
| 10-04 10:43:29 | SOL | down | 0.98→0.91 | 0.01 → 0.01 | no | price out of range |  |
| 10-04 10:42:49 | DOGE | down | 0.95→0.89 | 0.09 → 0.09 | no | edge gone |  |
| 10-04 10:42:45 | XRP | up | 0.77→0.84 | 0.88 → 0.88 | no | edge gone |  |
| 10-04 10:42:21 | XRP | up | 0.59→0.71 | 0.70 → 0.79 | 14.84s | edge gone |  |
| 10-04 10:42:04 | XRP | down | 0.73→0.62 | 0.26 → 0.27 | no | DOWN @ 0.27 | -0.09 / -1.72 / · |
| 10-04 10:42:02 | DOGE | down | 0.84→0.77 | 0.21 → 0.19 | no | edge gone |  |
| 10-04 10:42:01 | NEAR | down | 0.90→0.80 | 0.02 → 0.05 | no | price out of range |  |
| 10-04 10:41:41 | XRP | down | 0.77→0.72 | 0.32 → 0.21 | no | DOWN @ 0.21 | -0.43 / 0.22 / · |
| 10-04 10:41:28 | SOL | up | 0.77→0.84 | 0.34 → 0.79 | 7.35s | UP @ 0.79 | 0.24 / 1.07 / · |
| 10-04 10:41:27 | BTC | up | 0.00→0.06 | 0.01 → 0.04 | no | price out of range |  |
| 10-04 10:41:27 | DOGE | up | 0.63→0.74 | 0.08 → 0.59 | 9.10s | UP @ 0.59 | 0.78 / 1.98 / · |
| 10-04 10:41:26 | NEAR | up | 0.79→0.89 | 0.92 → 0.97 | 24.35s | price out of range |  |
| 10-04 10:41:26 | XRP | up | 0.15→0.68 | 0.10 → 0.58 | 9.35s | UP @ 0.58 | 1.18 / 1.90 / · |
| 10-04 10:41:26 | ETH | up | 0.00→0.09 | 0.01 → 0.09 | 9.35s | edge gone |  |
| 10-04 10:40:44 | NEAR | down | 0.77→0.72 | 0.05 → 0.08 | no | DOWN @ 0.08 | -0.27 / -0.07 / · |
| 10-04 10:40:32 | SOL | down | 0.43→0.37 | 0.49 → 0.59 | 3.86s | edge gone |  |
| 10-04 10:40:23 | XRP | down | 0.26→0.18 | 0.82 → 0.88 | 12.36s | edge gone |  |
| 10-04 10:40:19 | NEAR | up | 0.77→0.83 | 0.93 → 0.95 | no | edge gone |  |
| 10-04 10:40:04 | SOL | up | 0.41→0.47 | 0.34 → 0.50 | 1.37s | edge gone |  |
| 10-04 10:39:53 | DOGE | up | 0.24→0.30 | 0.13 → 0.25 | 12.87s | UP @ 0.25 | -0.85 / -0.76 / · |
| 10-04 10:39:44 | XRP | up | 0.16→0.22 | 0.21 → 0.18 | no | UP @ 0.18 | -0.10 / -0.68 / · |
| 10-04 10:39:28 | SOL | down | 0.47→0.41 | 0.49 → 0.45 | 22.88s | DOWN @ 0.45 | 1.35 / 0.34 / · |
| 10-04 10:39:05 | SOL | down | 0.53→0.47 | 0.36 → 0.46 | 15.38s | DOWN @ 0.46 | -0.36 / 1.06 / · |
| 10-04 10:38:42 | SOL | up | 0.55→0.60 | 0.65 → 0.65 | no | edge gone |  |
| 10-04 10:38:32 | XRP | down | 0.30→0.24 | 0.77 → 0.82 | 18.89s | edge gone |  |
| 10-04 10:38:25 | SOL | up | 0.50→0.62 | 0.50 → 0.67 | 10.89s | edge gone |  |
| 10-04 10:38:05 | NEAR | up | 0.60→0.65 | 0.78 → 0.77 | 15.40s | edge gone |  |
| 10-04 10:38:04 | XRP | up | 0.25→0.33 | 0.16 → 0.26 | 17.15s | UP @ 0.28 | -1.04 / -1.23 / · |
| 10-04 10:38:04 | DOGE | up | 0.30→0.39 | 0.29 → 0.41 | 2.14s | edge gone |  |
