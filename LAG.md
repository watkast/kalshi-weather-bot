# Lag Tracker

*Updated Sun Oct 04 13:55 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$392.27** | -31.1% | 345 | $3.64 | $122.22 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 371 | 64 | -$158.17 | -11.7% | -$81.09 / -$77.08 |
| Sell after 30 sec | 368 | 86 | -$179.10 | -13.3% | -$83.07 / -$96.03 |
| Hold to the close | 345 | 87 | -$392.27 | -31.1% | -$149.09 / -$243.18 |
| Hold, only edge 10¢+ | 123 | 17 | -$159.97 | -48.5% | -$114.92 / -$45.05 |
| Hold, first trade per window only | 120 | 39 | -$80.88 | -17.2% | -$17.07 / -$63.81 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 1370 | 11% | 65% | +5.0¢ | 0.3¢ | edge gone 935, price out of range 37, spread too wide 27 |

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
| BTC | 690 | 11.9s | 3% | 0% |
| DOGE | 803 | 10.5s | 2% | 0% |
| ETH | 846 | 11.2s | 4% | 0% |
| HYPE | 655 | 11.4s | 4% | 0% |
| NEAR | 844 | 10.8s | 4% | 0% |
| SOL | 1569 | 10.9s | 3% | 0% |
| XRP | 1576 | 10.9s | 4% | 0% |
| ZEC | 978 | 9.6s | 4% | 0% |
| **All** | **8637** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 13:55:30 | SOL | down | 0.75→0.68 | 0.15 → 0.16 | 3.03s | DOWN @ 0.16 | -0.29 / · / · |
| 10-04 13:55:25 | XRP | up | 0.50→0.61 | 0.53 → 0.67 | 7.78s | edge gone |  |
| 10-04 13:55:12 | DOGE | down | 0.85→0.65 | 0.08 → 0.29 | 5.53s | DOWN @ 0.29 | -1.45 / · / · |
| 10-04 13:55:11 | ETH | down | 0.83→0.76 | 0.12 → 0.21 | no | edge gone |  |
| 10-04 13:55:10 | SOL | down | 0.74→0.67 | 0.13 → 0.15 | 22.54s | DOWN @ 0.17 | -0.11 / · / · |
| 10-04 13:55:10 | XRP | down | 0.73→0.67 | 0.09 → 0.29 | 7.78s | edge gone |  |
| 10-04 13:55:02 | BTC | up | 0.76→0.82 | 0.88 → 0.92 | no | edge gone |  |
| 10-04 13:54:40 | BTC | down | 0.82→0.75 | 0.14 → 0.14 | no | DOWN @ 0.14 | -0.46 / -0.18 / · |
| 10-04 13:54:17 | XRP | down | 0.81→0.74 | 0.14 → 0.12 | no | DOWN @ 0.12 | -0.35 / -0.44 / · |
| 10-04 13:54:16 | SOL | down | 0.80→0.75 | 0.11 → 0.14 | 2.28s | DOWN @ 0.14 | 0.01 / -0.18 / · |
| 10-04 13:54:01 | SOL | down | 0.84→0.74 | 0.14 → 0.15 | no | DOWN @ 0.15 | -0.47 / -0.11 / · |
| 10-04 13:53:46 | SOL | down | 0.79→0.74 | 0.16 → 0.13 | no | DOWN @ 0.13 | -0.53 / -0.16 / · |
| 10-04 13:53:26 | XRP | down | 0.77→0.70 | 0.16 → 0.21 | 6.78s | DOWN @ 0.21 | -0.46 / -1.03 / · |
| 10-04 13:53:02 | XRP | up | 0.76→0.84 | 0.83 → 0.85 | no | edge gone |  |
| 10-04 13:52:49 | SOL | down | 0.82→0.75 | 0.17 → 0.20 | no | DOWN @ 0.20 | -0.71 / -1.19 / · |
| 10-04 13:52:46 | XRP | up | 0.74→0.84 | 0.84 → 0.84 | no | edge gone |  |
| 10-04 13:52:38 | ETH | up | 0.58→0.63 | 0.71 → 0.76 | 9.78s | edge gone |  |
| 10-04 13:52:37 | DOGE | down | 0.79→0.69 | 0.19 → 0.20 | no | DOWN @ 0.20 | -0.81 / -1.00 / · |
| 10-04 13:52:06 | XRP | up | 0.71→0.77 | 0.82 → 0.80 | no | edge gone |  |
| 10-04 13:51:50 | HYPE | down | 0.82→0.60 | 0.15 → 0.36 | 12.53s | edge gone |  |
| 10-04 13:51:34 | XRP | down | 0.80→0.74 | 0.21 → 0.21 | no | DOWN @ 0.21 | -0.43 / -0.34 / · |
| 10-04 13:51:27 | ETH | up | 0.52→0.58 | 0.61 → 0.67 | 5.53s | edge gone |  |
| 10-04 13:51:27 | SOL | up | 0.73→0.80 | 0.80 → 0.78 | no | edge gone |  |
| 10-04 13:51:16 | XRP | down | 0.80→0.74 | 0.21 → 0.20 | 1.53s | DOWN @ 0.20 | -0.24 / -0.33 / · |
| 10-04 13:51:07 | SOL | down | 0.91→0.72 | 0.13 → 0.24 | 25.54s | edge gone |  |
| 10-04 13:51:07 | ETH | down | 0.62→0.56 | 0.27 → 0.45 | 10.53s | edge gone |  |
| 10-04 13:50:49 | XRP | down | 0.75→0.69 | 0.22 → 0.23 | 28.54s | DOWN @ 0.23 | -0.26 / -0.55 / · |
| 10-04 13:50:33 | XRP | up | 0.69→0.75 | 0.79 → 0.77 | no | edge gone |  |
| 10-04 13:50:25 | BTC | down | 0.89→0.81 | 0.14 → 0.22 | 7.78s | edge gone |  |
| 10-04 13:50:14 | ETH | down | 0.81→0.74 | 0.17 → 0.29 | 19.29s | edge gone |  |
