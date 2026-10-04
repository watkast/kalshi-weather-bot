# Lag Tracker

*Updated Sun Oct 04 15:15 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$344.20** | -21.2% | 450 | $3.65 | $122.22 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 473 | 83 | -$190.28 | -11.0% | -$103.10 / -$87.18 |
| Sell after 30 sec | 473 | 115 | -$223.10 | -12.9% | -$113.90 / -$109.20 |
| Hold to the close | 450 | 128 | -$344.20 | -21.2% | -$211.19 / -$133.01 |
| Hold, only edge 10¢+ | 157 | 29 | -$132.17 | -31.3% | -$97.39 / -$34.78 |
| Hold, first trade per window only | 153 | 52 | -$102.33 | -16.4% | -$32.95 / -$69.38 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 1792 | 10% | 66% | +4.9¢ | 0.3¢ | edge gone 1224, price out of range 51, spread too wide 44 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 682 | 11.1s | 3% | 0% |
| BTC | 751 | 11.8s | 3% | 0% |
| DOGE | 834 | 10.6s | 3% | 0% |
| ETH | 892 | 11.0s | 4% | 0% |
| HYPE | 681 | 11.6s | 3% | 0% |
| NEAR | 873 | 10.8s | 4% | 0% |
| SOL | 1651 | 10.9s | 3% | 0% |
| XRP | 1666 | 11.0s | 3% | 0% |
| ZEC | 1029 | 9.6s | 4% | 0% |
| **All** | **9059** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **19 ms** · Order book check: **24 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 15:13:35 | ZEC | up | 0.82→0.90 | 0.63 → 0.95 | 13.86s | price out of range |  |
| 10-04 15:13:32 | ETH | up | 0.78→0.93 | 0.82 → 0.95 | 16.61s | edge gone |  |
| 10-04 15:13:32 | SOL | up | 0.51→0.73 | 0.64 → 0.91 | 16.86s | edge gone |  |
| 10-04 15:13:24 | HYPE | up | 0.09→0.29 | 0.15 → 0.25 | 24.61s | spread too wide |  |
| 10-04 15:13:20 | ZEC | up | 0.55→0.63 | 0.61 → 0.54 | 0.34s | UP @ 0.55 | 2.10 / 4.26 / · |
| 10-04 15:13:17 | SOL | down | 0.58→0.44 | 0.45 → 0.33 | no | DOWN @ 0.33 | -0.12 / -3.26 / · |
| 10-04 15:13:09 | BTC | up | 0.86→0.92 | 0.92 → 0.94 | 9.86s | edge gone |  |
| 10-04 15:13:00 | ZEC | up | 0.28→0.36 | 0.13 → 0.28 | 4.11s | spread too wide |  |
| 10-04 15:12:59 | SOL | down | 0.51→0.38 | 0.50 → 0.45 | no | DOWN @ 0.45 | -1.34 / -1.05 / · |
| 10-04 15:12:41 | SOL | up | 0.39→0.51 | 0.50 → 0.51 | 23.12s | edge gone |  |
| 10-04 15:12:39 | HYPE | down | 0.16→0.08 | 0.80 → 0.92 | 9.64s | edge gone |  |
| 10-04 15:12:19 | ETH | down | 0.81→0.75 | 0.22 → 0.33 | 0.38s | edge gone |  |
| 10-04 15:12:19 | BTC | down | 0.90→0.83 | 0.14 → 0.21 | no | edge gone |  |
| 10-04 15:12:15 | SOL | down | 0.55→0.40 | 0.44 → 0.53 | 4.38s | DOWN @ 0.53 | -0.66 / -0.76 / · |
| 10-04 15:12:03 | ETH | down | 0.84→0.75 | 0.20 → 0.21 | 16.38s | DOWN @ 0.21 | 0.35 / 0.63 / · |
| 10-04 15:11:42 | SOL | up | 0.46→0.55 | 0.68 → 0.53 | no | edge gone |  |
| 10-04 15:11:31 | ZEC | up | 0.30→0.36 | 0.16 → 0.22 | 3.39s | UP @ 0.22 | -1.07 / -1.11 / · |
| 10-04 15:11:27 | SOL | up | 0.42→0.50 | 0.39 → 0.67 | 7.39s | edge gone |  |
| 10-04 15:11:27 | ETH | up | 0.76→0.82 | 0.74 → 0.88 | 7.39s | edge gone |  |
| 10-04 15:11:15 | BTC | up | 0.67→0.79 | 0.65 → 0.78 | 18.89s | edge gone |  |
| 10-04 15:11:11 | SOL | up | 0.34→0.46 | 0.32 → 0.44 | 8.39s | edge gone |  |
| 10-04 15:11:02 | ETH | up | 0.59→0.71 | 0.48 → 0.71 | 2.39s | edge gone |  |
| 10-04 15:11:01 | BNB | up | 0.66→0.71 | 0.90 → 0.97 | 17.65s | price out of range |  |
| 10-04 15:11:00 | BTC | up | 0.51→0.57 | 0.40 → 0.60 | 3.90s | edge gone |  |
| 10-04 15:10:52 | HYPE | up | 0.13→0.24 | 0.15 → 0.27 | 26.90s | edge gone |  |
| 10-04 15:10:48 | SOL | down | 0.25→0.19 | 0.80 → 0.80 | no | edge gone |  |
| 10-04 15:10:33 | SOL | down | 0.20→0.15 | 0.80 → 0.81 | no | DOWN @ 0.81 | -0.43 / -2.08 / · |
| 10-04 15:10:10 | BTC | up | 0.32→0.38 | 0.32 → 0.37 | 23.66s | edge gone |  |
| 10-04 15:10:10 | HYPE | up | 0.12→0.18 | 0.11 → 0.19 | 9.41s | edge gone |  |
| 10-04 15:10:04 | SOL | down | 0.16→0.11 | 0.85 → 0.86 | 0.14s | edge gone |  |
