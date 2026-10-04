# Lag Tracker

*Updated Sun Oct 04 10:54 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🟡 **Testing with real order-book fills.** 88 of 150 settled trades needed before calling it. The earlier results below used quoted prices, which may not have been fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **$12.92** | +3.7% | 88 | $3.88 | $83.77 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 94 | 22 | -$34.11 | -9.3% | -$15.77 / -$18.34 |
| Sell after 30 sec | 93 | 28 | -$33.39 | -9.2% | -$24.90 / -$8.49 |
| Hold to the close | 88 | 36 | $12.92 | +3.7% | $2.49 / $10.43 |
| Hold, only edge 10¢+ | 21 | 3 | -$24.92 | -45.4% | -$20.21 / -$4.71 |
| Hold, first trade per window only | 35 | 16 | $8.66 | +5.7% | -$5.72 / $14.38 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 428 | 9% | 69% | +5.0¢ | 0.3¢ | edge gone 312, price out of range 18, spread too wide 4 |

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
| BTC | 572 | 11.9s | 3% | 0% |
| DOGE | 754 | 10.5s | 2% | 0% |
| ETH | 734 | 11.0s | 4% | 0% |
| HYPE | 611 | 11.4s | 4% | 0% |
| NEAR | 747 | 10.8s | 4% | 0% |
| SOL | 1364 | 10.8s | 3% | 0% |
| XRP | 1381 | 11.0s | 4% | 0% |
| ZEC | 882 | 9.6s | 4% | 0% |
| **All** | **7695** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 10:54:28 | DOGE | down | 0.55→0.48 | 0.44 → 0.54 | no | edge gone |  |
| 10-04 10:54:21 | XRP | down | 0.69→0.63 | 0.22 → 0.27 | no | DOWN @ 0.28 | -0.82 / · / · |
| 10-04 10:53:55 | XRP | down | 0.71→0.63 | 0.24 → 0.22 | no | DOWN @ 0.23 | -0.45 / -0.38 / · |
| 10-04 10:53:55 | SOL | down | 0.46→0.34 | 0.55 → 0.66 | 8.83s | edge gone |  |
| 10-04 10:53:48 | NEAR | up | 0.57→0.65 | 0.71 → 0.79 | 16.08s | edge gone |  |
| 10-04 10:53:41 | HYPE | up | 0.46→0.53 | 0.47 → 0.52 | 8.08s | edge gone |  |
| 10-04 10:53:40 | XRP | down | 0.71→0.65 | 0.25 → 0.24 | no | DOWN @ 0.25 | -0.76 / -0.66 / · |
| 10-04 10:53:24 | SOL | up | 0.40→0.46 | 0.44 → 0.44 | no | edge gone |  |
| 10-04 10:53:15 | XRP | down | 0.70→0.64 | 0.29 → 0.29 | no | DOWN @ 0.29 | -0.83 / -0.97 / · |
| 10-04 10:53:07 | SOL | down | 0.46→0.40 | 0.55 → 0.57 | 27.35s | edge gone |  |
| 10-04 10:52:54 | NEAR | up | 0.40→0.47 | 0.47 → 0.59 | 9.60s | edge gone |  |
| 10-04 10:52:32 | SOL | down | 0.51→0.46 | 0.45 → 0.51 | 2.10s | edge gone |  |
| 10-04 10:52:25 | NEAR | down | 0.48→0.41 | 0.41 → 0.55 | 9.35s | edge gone |  |
| 10-04 10:52:17 | SOL | down | 0.56→0.51 | 0.34 → 0.45 | 2.10s | edge gone |  |
| 10-04 10:52:12 | XRP | up | 0.63→0.70 | 0.74 → 0.74 | 22.36s | edge gone |  |
| 10-04 10:51:50 | HYPE | up | 0.47→0.52 | 0.45 → 0.65 | 14.11s | edge gone |  |
| 10-04 10:51:42 | XRP | up | 0.58→0.63 | 0.62 → 0.64 | 21.61s | edge gone |  |
| 10-04 10:51:37 | DOGE | down | 0.46→0.37 | 0.65 → 0.65 | no | edge gone |  |
| 10-04 10:51:34 | BTC | up | 0.44→0.50 | 0.44 → 0.42 | no | UP @ 0.42 | -0.36 / -0.45 / · |
| 10-04 10:51:27 | XRP | up | 0.50→0.55 | 0.63 → 0.60 | no | edge gone |  |
| 10-04 10:51:23 | NEAR | up | 0.39→0.46 | 0.43 → 0.54 | 11.37s | edge gone |  |
| 10-04 10:51:11 | HYPE | up | 0.36→0.41 | 0.34 → 0.45 | 8.12s | edge gone |  |
| 10-04 10:51:01 | XRP | up | 0.53→0.58 | 0.59 → 0.64 | 17.62s | edge gone |  |
| 10-04 10:50:33 | HYPE | down | 0.31→0.24 | 0.68 → 0.80 | 1.38s | edge gone |  |
| 10-04 10:50:30 | SOL | down | 0.49→0.43 | 0.55 → 0.53 | no | edge gone |  |
| 10-04 10:50:15 | BTC | down | 0.46→0.41 | 0.54 → 0.57 | no | edge gone |  |
| 10-04 10:50:14 | NEAR | up | 0.43→0.50 | 0.52 → 0.60 | no | edge gone |  |
| 10-04 10:49:46 | HYPE | down | 0.37→0.23 | 0.70 → 0.73 | 17.39s | edge gone |  |
| 10-04 10:49:46 | SOL | up | 0.49→0.55 | 0.55 → 0.53 | no | edge gone |  |
| 10-04 10:49:36 | NEAR | up | 0.41→0.47 | 0.44 → 0.54 | 13.14s | edge gone |  |
