# Lag Tracker

*Updated Sun Oct 04 10:34 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

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
| Sell after 10 sec | 76 | 18 | -$29.66 | -9.9% | -$16.11 / -$13.55 |
| Sell after 30 sec | 76 | 22 | -$31.34 | -10.5% | -$25.99 / -$5.35 |
| Hold to the close | 74 | 30 | $9.07 | +3.1% | -$11.90 / $20.97 |
| Hold, only edge 10¢+ | 18 | 2 | -$23.31 | -53.8% | -$15.83 / -$7.48 |
| Hold, first trade per window only | 31 | 14 | $2.73 | +2.0% | -$8.54 / $11.27 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 344 | 8% | 70% | +6.0¢ | 0.2¢ | edge gone 251, price out of range 13, spread too wide 4 |

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
| BTC | 566 | 11.9s | 3% | 0% |
| DOGE | 746 | 10.5s | 2% | 0% |
| ETH | 730 | 11.0s | 4% | 0% |
| HYPE | 604 | 11.4s | 4% | 0% |
| NEAR | 731 | 10.8s | 4% | 0% |
| SOL | 1344 | 11.0s | 3% | 0% |
| XRP | 1359 | 10.8s | 4% | 0% |
| ZEC | 881 | 9.6s | 4% | 0% |
| **All** | **7611** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **34 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 10:34:12 | BTC | down | 0.33→0.23 | 0.70 → 0.78 | no | edge gone |  |
| 10-04 10:34:12 | SOL | down | 0.50→0.44 | 0.37 → 0.54 | 8.28s | edge gone |  |
| 10-04 10:34:12 | ETH | down | 0.30→0.24 | 0.72 → 0.78 | 8.28s | edge gone |  |
| 10-04 10:34:11 | XRP | down | 0.52→0.46 | 0.41 → 0.57 | 10.03s | edge gone |  |
| 10-04 10:33:43 | ZEC | down | 0.30→0.25 | 0.76 → 0.80 | 7.28s | edge gone |  |
| 10-04 10:33:32 | XRP | down | 0.67→0.61 | 0.55 → 0.37 | no | edge gone |  |
| 10-04 10:33:29 | DOGE | up | 0.62→0.68 | 0.60 → 0.80 | 21.54s | edge gone |  |
| 10-04 10:33:28 | SOL | up | 0.42→0.67 | 0.47 → 0.64 | 22.54s | edge gone |  |
| 10-04 10:33:28 | BTC | up | 0.21→0.29 | 0.20 → 0.38 | 7.78s | edge gone |  |
| 10-04 10:33:28 | ETH | up | 0.19→0.25 | 0.20 → 0.38 | 7.78s | edge gone |  |
| 10-04 10:33:14 | DOGE | up | 0.50→0.56 | 0.55 → 0.60 | 6.54s | edge gone |  |
| 10-04 10:32:38 | BTC | down | 0.37→0.30 | 0.65 → 0.74 | 12.55s | edge gone |  |
| 10-04 10:32:31 | SOL | down | 0.48→0.42 | 0.46 → 0.56 | 4.79s | edge gone |  |
| 10-04 10:32:30 | ETH | down | 0.32→0.27 | 0.72 → 0.73 | 5.80s | edge gone |  |
| 10-04 10:32:05 | ETH | down | 0.45→0.34 | 0.58 → 0.68 | 0.55s | edge gone |  |
| 10-04 10:32:04 | SOL | down | 0.59→0.54 | 0.36 → 0.41 | 16.55s | DOWN @ 0.41 | 0.05 / 0.90 / · |
| 10-04 10:32:02 | BTC | down | 0.49→0.44 | 0.56 → 0.58 | 18.81s | edge gone |  |
| 10-04 10:31:50 | NEAR | up | 0.57→0.72 | 0.58 → 0.76 | 0.30s | edge gone |  |
| 10-04 10:31:50 | ETH | up | 0.40→0.47 | 0.35 → 0.45 | 0.55s | edge gone |  |
| 10-04 10:31:50 | XRP | up | 0.50→0.55 | 0.38 → 0.56 | 1.05s | edge gone |  |
| 10-04 10:31:41 | BTC | up | 0.44→0.49 | 0.42 → 0.47 | 9.81s | edge gone |  |
| 10-04 10:31:35 | NEAR | down | 0.56→0.49 | 0.45 → 0.39 | no | DOWN @ 0.41 | -1.49 / -2.07 / · |
| 10-04 10:31:15 | ETH | down | 0.40→0.34 | 0.61 → 0.64 | 5.56s | edge gone |  |
| 10-04 10:31:14 | HYPE | down | 0.24→0.19 | 0.76 → 0.78 | 22.07s | edge gone |  |
| 10-04 10:31:03 | SOL | up | 0.46→0.52 | 0.49 → 0.57 | 2.31s | edge gone |  |
| 10-04 10:30:58 | XRP | up | 0.40→0.47 | 0.40 → 0.42 | no | edge gone |  |
| 10-04 10:28:39 | XRP | up | 0.50→0.63 | 0.67 → 0.68 | no | edge gone |  |
| 10-04 10:28:24 | XRP | up | 0.56→0.61 | 0.63 → 0.60 | 2.60s | edge gone |  |
| 10-04 10:28:09 | BNB | down | 0.78→0.69 | 0.02 → 0.02 | no | price out of range |  |
| 10-04 10:27:48 | DOGE | down | 0.69→0.63 | 0.38 → 0.16 | no | DOWN @ 0.17 | -0.53 / 2.72 / 8.25 |
