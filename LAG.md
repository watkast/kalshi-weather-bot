# Lag Tracker

*Updated Sun Oct 04 14:46 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$312.75** | -20.1% | 433 | $3.59 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 433 | 72 | -$176.48 | -11.4% | -$99.82 / -$76.66 |
| Sell after 30 sec | 433 | 102 | -$201.56 | -13.0% | -$103.25 / -$98.31 |
| Hold to the close | 433 | 124 | -$312.75 | -20.1% | -$218.09 / -$94.66 |
| Hold, only edge 10¢+ | 154 | 29 | -$122.90 | -29.8% | -$103.88 / -$19.02 |
| Hold, first trade per window only | 146 | 51 | -$75.80 | -12.9% | -$43.83 / -$31.97 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 1608 | 10% | 65% | +4.0¢ | 0.3¢ | edge gone 1090, price out of range 49, spread too wide 36 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 676 | 11.1s | 3% | 0% |
| BTC | 723 | 11.8s | 3% | 0% |
| DOGE | 824 | 10.5s | 3% | 0% |
| ETH | 863 | 11.2s | 4% | 0% |
| HYPE | 666 | 11.6s | 3% | 0% |
| NEAR | 857 | 10.8s | 4% | 0% |
| SOL | 1616 | 11.0s | 3% | 0% |
| XRP | 1643 | 11.1s | 3% | 0% |
| ZEC | 1007 | 9.6s | 4% | 0% |
| **All** | **8875** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 14:43:39 | SOL | down | 0.16→0.11 | 0.96 → 0.98 | 24.06s | price out of range |  |
| 10-04 14:43:33 | XRP | down | 0.58→0.42 | 0.32 → 0.60 | 14.56s | edge gone |  |
| 10-04 14:43:16 | XRP | down | 0.57→0.50 | 0.43 → 0.51 | 1.56s | edge gone |  |
| 10-04 14:43:14 | SOL | down | 0.21→0.16 | 0.85 → 0.92 | 3.56s | edge gone |  |
| 10-04 14:43:14 | ZEC | down | 0.82→0.76 | 0.11 → 0.13 | 4.06s | DOWN @ 0.13 | -0.16 / -1.17 / -1.38 |
| 10-04 14:43:05 | ETH | down | 0.19→0.11 | 0.96 → 0.97 | no | price out of range |  |
| 10-04 14:42:46 | XRP | up | 0.50→0.55 | 0.58 → 0.52 | no | edge gone |  |
| 10-04 14:42:46 | SOL | down | 0.30→0.17 | 0.73 → 0.85 | 17.32s | edge gone |  |
| 10-04 14:42:40 | ZEC | down | 0.78→0.67 | 0.17 → 0.20 | 7.82s | DOWN @ 0.20 | -0.89 / -1.59 / -2.12 |
| 10-04 14:42:31 | XRP | up | 0.45→0.50 | 0.50 → 0.52 | 2.07s | edge gone |  |
| 10-04 14:42:25 | ZEC | down | 0.93→0.83 | 0.03 → 0.09 | 7.83s | DOWN @ 0.09 | -0.15 / -0.57 / -0.98 |
| 10-04 14:41:49 | XRP | up | 0.19→0.26 | 0.19 → 0.18 | 13.59s | UP @ 0.19 | 1.82 / 2.91 / -2.01 |
| 10-04 14:41:34 | XRP | up | 0.18→0.23 | 0.22 → 0.18 | 28.60s | UP @ 0.18 | -0.31 / 2.46 / -1.91 |
| 10-04 14:41:17 | XRP | down | 0.28→0.22 | 0.81 → 0.79 | 0.84s | edge gone |  |
| 10-04 14:41:04 | SOL | down | 0.40→0.30 | 0.59 → 0.75 | 13.85s | edge gone |  |
| 10-04 14:41:02 | HYPE | up | 0.88→0.94 | 0.95 → 0.98 | 16.10s | price out of range |  |
| 10-04 14:41:01 | DOGE | up | 0.63→0.72 | 0.85 → 0.89 | no | edge gone |  |
| 10-04 14:40:52 | XRP | up | 0.20→0.26 | 0.20 → 0.18 | no | UP @ 0.20 | -0.33 / -0.42 / -2.12 |
| 10-04 14:40:45 | NEAR | down | 0.83→0.76 | 0.09 → 0.09 | no | DOWN @ 0.09 | -0.35 / -0.31 / -0.99 |
| 10-04 14:40:41 | DOGE | down | 0.75→0.67 | 0.15 → 0.17 | no | DOWN @ 0.17 | -0.39 / -0.58 / -1.80 |
| 10-04 14:40:35 | XRP | down | 0.27→0.21 | 0.81 → 0.82 | no | edge gone |  |
| 10-04 14:40:24 | DOGE | down | 0.78→0.66 | 0.19 → 0.17 | no | DOWN @ 0.17 | -0.39 / -0.39 / -1.80 |
| 10-04 14:40:22 | ZEC | down | 0.81→0.67 | 0.29 → 0.24 | no | DOWN @ 0.24 | -1.21 / -1.89 / -2.53 |
| 10-04 14:40:17 | NEAR | up | 0.70→0.76 | 0.84 → 0.93 | 15.36s | edge gone |  |
| 10-04 14:40:16 | XRP | down | 0.30→0.25 | 0.77 → 0.78 | 16.61s | edge gone |  |
| 10-04 14:39:47 | XRP | down | 0.37→0.26 | 0.71 → 0.70 | 15.62s | edge gone |  |
| 10-04 14:39:46 | NEAR | down | 0.66→0.60 | 0.23 → 0.22 | no | DOWN @ 0.23 | -0.96 / -1.20 / -2.47 |
| 10-04 14:39:37 | SOL | down | 0.45→0.39 | 0.57 → 0.53 | no | DOWN @ 0.53 | -0.36 / -0.16 / 4.52 |
| 10-04 14:39:12 | ETH | down | 0.38→0.30 | 0.63 → 0.71 | 6.13s | edge gone |  |
| 10-04 14:39:10 | SOL | down | 0.42→0.37 | 0.52 → 0.53 | 22.38s | DOWN @ 0.53 | -0.56 / -0.46 / 4.52 |
