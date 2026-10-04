# Lag Tracker

*Updated Sun Oct 04 12:45 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$268.64** | -30.6% | 246 | $3.55 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 265 | 46 | -$115.96 | -12.3% | -$52.25 / -$63.71 |
| Sell after 30 sec | 265 | 59 | -$132.93 | -14.1% | -$53.72 / -$79.21 |
| Hold to the close | 246 | 61 | -$268.64 | -30.6% | -$69.64 / -$199.00 |
| Hold, only edge 10¢+ | 85 | 12 | -$110.74 | -48.0% | -$64.52 / -$46.22 |
| Hold, first trade per window only | 87 | 29 | -$50.32 | -14.8% | -$9.36 / -$40.96 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 992 | 11% | 64% | +5.0¢ | 0.3¢ | edge gone 679, price out of range 32, spread too wide 16 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 664 | 11.1s | 3% | 0% |
| BTC | 636 | 11.9s | 3% | 0% |
| DOGE | 784 | 10.6s | 2% | 0% |
| ETH | 796 | 11.0s | 4% | 0% |
| HYPE | 643 | 11.4s | 4% | 0% |
| NEAR | 805 | 10.8s | 4% | 0% |
| SOL | 1508 | 10.8s | 3% | 0% |
| XRP | 1487 | 11.0s | 4% | 0% |
| ZEC | 936 | 9.7s | 4% | 0% |
| **All** | **8259** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 12:43:37 | SOL | down | 0.87→0.82 | 0.07 → 0.06 | no | DOWN @ 0.06 | -0.38 / -0.56 / · |
| 10-04 12:43:23 | XRP | down | 0.11→0.04 | 0.96 → 0.99 | 0.29s | price out of range |  |
| 10-04 12:43:20 | SOL | down | 0.83→0.78 | 0.12 → 0.08 | no | DOWN @ 0.08 | -0.41 / -0.76 / · |
| 10-04 12:43:09 | BNB | down | 0.55→0.37 | 0.01 → 0.05 | no | DOWN @ 0.06 | -0.43 / -0.41 / · |
| 10-04 12:43:04 | SOL | down | 0.85→0.75 | 0.11 → 0.12 | no | DOWN @ 0.12 | -0.35 / -0.91 / · |
| 10-04 12:42:58 | XRP | up | 0.19→0.24 | 0.13 → 0.11 | no | UP @ 0.11 | -0.74 / -1.04 / · |
| 10-04 12:42:49 | SOL | up | 0.68→0.78 | 0.79 → 0.93 | 2.82s | edge gone |  |
| 10-04 12:42:38 | HYPE | up | 0.08→0.17 | 0.04 → 0.13 | 13.83s | edge gone |  |
| 10-04 12:42:26 | SOL | up | 0.55→0.66 | 0.75 → 0.78 | 26.08s | edge gone |  |
| 10-04 12:42:23 | HYPE | down | 0.09→0.04 | 0.96 → 0.97 | no | price out of range |  |
| 10-04 12:42:21 | XRP | down | 0.23→0.15 | 0.90 → 0.88 | no | edge gone |  |
| 10-04 12:42:10 | SOL | up | 0.55→0.65 | 0.69 → 0.69 | 12.08s | edge gone |  |
| 10-04 12:41:54 | SOL | up | 0.64→0.73 | 0.76 → 0.82 | 0.07s | edge gone |  |
| 10-04 12:41:47 | XRP | down | 0.26→0.18 | 0.87 → 0.84 | no | edge gone |  |
| 10-04 12:41:35 | SOL | up | 0.54→0.68 | 0.59 → 0.75 | 16.60s | edge gone |  |
| 10-04 12:41:32 | XRP | up | 0.20→0.27 | 0.07 → 0.13 | 4.84s | UP @ 0.13 | 0.23 / -0.07 / · |
| 10-04 12:41:17 | SOL | up | 0.45→0.58 | 0.46 → 0.61 | 4.60s | edge gone |  |
| 10-04 12:41:17 | XRP | up | 0.15→0.20 | 0.08 → 0.17 | 19.85s | edge gone |  |
| 10-04 12:40:57 | SOL | down | 0.45→0.37 | 0.63 → 0.55 | no | DOWN @ 0.55 | -0.36 / -2.15 / · |
| 10-04 12:40:50 | ETH | up | 0.24→0.30 | 0.16 → 0.18 | no | UP @ 0.18 | -0.50 / -0.03 / · |
| 10-04 12:40:15 | SOL | up | 0.46→0.53 | 0.40 → 0.50 | 6.61s | edge gone |  |
| 10-04 12:40:06 | ZEC | up | 0.75→0.81 | 0.88 → 0.82 | 30.87s | edge gone |  |
| 10-04 12:40:00 | SOL | down | 0.46→0.39 | 0.64 → 0.65 | no | edge gone |  |
| 10-04 12:39:59 | XRP | up | 0.09→0.14 | 0.08 → 0.07 | no | UP @ 0.07 | -0.03 / 0.08 / · |
| 10-04 12:39:44 | SOL | up | 0.39→0.46 | 0.38 → 0.39 | no | UP @ 0.40 | -0.54 / 0.15 / · |
| 10-04 12:39:44 | XRP | down | 0.15→0.10 | 0.93 → 0.91 | no | edge gone |  |
| 10-04 12:39:25 | XRP | down | 0.20→0.12 | 0.87 → 0.89 | 11.38s | edge gone |  |
| 10-04 12:39:11 | SOL | up | 0.43→0.50 | 0.55 → 0.51 | no | edge gone |  |
| 10-04 12:39:11 | BNB | up | 0.42→0.53 | 0.80 → 0.77 | no | edge gone |  |
| 10-04 12:39:10 | NEAR | up | 0.15→0.22 | 0.20 → 0.26 | 11.13s | edge gone |  |
