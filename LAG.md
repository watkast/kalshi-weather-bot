# Lag Tracker

*Updated Sun Oct 04 17:26 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$251.06** | -10.2% | 664 | $3.73 | $143.33 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 685 | 115 | -$285.80 | -11.2% | -$142.94 / -$142.86 |
| Sell after 30 sec | 685 | 181 | -$297.28 | -11.6% | -$165.56 / -$131.72 |
| Hold to the close | 664 | 222 | -$251.06 | -10.2% | -$376.95 / $125.89 |
| Hold, only edge 10¢+ | 230 | 58 | -$76.90 | -11.7% | -$143.97 / $67.07 |
| Hold, first trade per window only | 217 | 81 | -$60.89 | -7.0% | -$82.51 / $21.62 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 2605 | 9% | 67% | +5.0¢ | 0.3¢ | edge gone 1794, price out of range 65, spread too wide 61 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 709 | 11.1s | 3% | 0% |
| BTC | 831 | 11.9s | 3% | 0% |
| DOGE | 914 | 10.5s | 3% | 0% |
| ETH | 1012 | 10.8s | 4% | 0% |
| HYPE | 713 | 11.6s | 3% | 0% |
| NEAR | 967 | 10.8s | 3% | 0% |
| SOL | 1807 | 10.8s | 3% | 0% |
| XRP | 1837 | 11.2s | 3% | 0% |
| ZEC | 1082 | 9.7s | 4% | 0% |
| **All** | **9872** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **7 ms** · Order book check: **25 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 17:25:56 | DOGE | up | 0.42→0.50 | 0.31 → 0.51 | no | edge gone |  |
| 10-04 17:25:37 | ZEC | up | 0.71→0.76 | 0.93 → 0.93 | no | edge gone |  |
| 10-04 17:25:26 | DOGE | up | 0.32→0.38 | 0.21 → 0.30 | 2.13s | UP @ 0.31 | -0.49 / 1.88 / · |
| 10-04 17:25:21 | XRP | up | 0.04→0.10 | 0.11 → 0.10 | no | edge gone |  |
| 10-04 17:25:21 | NEAR | down | 0.48→0.40 | 0.41 → 0.55 | no | edge gone |  |
| 10-04 17:25:21 | BTC | up | 0.83→0.88 | 0.90 → 0.92 | 7.88s | edge gone |  |
| 10-04 17:25:17 | ETH | up | 0.81→0.86 | 0.87 → 0.88 | 26.39s | edge gone |  |
| 10-04 17:25:17 | HYPE | down | 0.27→0.20 | 0.86 → 0.83 | no | edge gone |  |
| 10-04 17:25:10 | SOL | down | 0.85→0.80 | 0.05 → 0.06 | no | DOWN @ 0.06 | -0.09 / -0.29 / · |
| 10-04 17:25:06 | DOGE | down | 0.29→0.19 | 0.70 → 0.83 | 7.89s | edge gone |  |
| 10-04 17:24:56 | HYPE | up | 0.12→0.18 | 0.17 → 0.15 | no | edge gone |  |
| 10-04 17:24:52 | NEAR | down | 0.61→0.54 | 0.33 → 0.32 | 21.39s | DOWN @ 0.32 | -0.12 / 1.61 / · |
| 10-04 17:24:36 | SOL | up | 0.78→0.84 | 0.91 → 0.92 | 7.89s | edge gone |  |
| 10-04 17:24:34 | DOGE | up | 0.35→0.41 | 0.33 → 0.35 | no | edge gone |  |
| 10-04 17:24:32 | NEAR | up | 0.51→0.56 | 0.59 → 0.71 | 11.39s | edge gone |  |
| 10-04 17:24:30 | XRP | up | 0.06→0.12 | 0.16 → 0.14 | no | edge gone |  |
| 10-04 17:24:11 | SOL | up | 0.74→0.83 | 0.90 → 0.91 | no | edge gone |  |
| 10-04 17:24:10 | ETH | down | 0.85→0.79 | 0.13 → 0.18 | 3.15s | edge gone |  |
| 10-04 17:24:07 | NEAR | down | 0.51→0.45 | 0.41 → 0.41 | no | DOWN @ 0.41 | -0.59 / -1.62 / · |
| 10-04 17:23:55 | SOL | down | 0.80→0.74 | 0.16 → 0.12 | no | DOWN @ 0.12 | -0.41 / -0.45 / · |
| 10-04 17:23:45 | XRP | up | 0.12→0.18 | 0.19 → 0.19 | no | edge gone |  |
| 10-04 17:23:39 | SOL | down | 0.79→0.73 | 0.11 → 0.15 | 4.91s | DOWN @ 0.15 | -0.66 / -0.73 / · |
| 10-04 17:23:32 | HYPE | up | 0.13→0.20 | 0.22 → 0.23 | no | edge gone |  |
| 10-04 17:23:31 | ETH | up | 0.83→0.89 | 0.90 → 0.85 | no | edge gone |  |
| 10-04 17:23:27 | NEAR | down | 0.52→0.45 | 0.36 → 0.47 | 16.91s | DOWN @ 0.49 | -0.93 / -1.22 / · |
| 10-04 17:23:19 | SOL | up | 0.70→0.76 | 0.81 → 0.89 | 9.66s | edge gone |  |
| 10-04 17:23:17 | XRP | up | 0.09→0.15 | 0.13 → 0.16 | 11.16s | edge gone |  |
| 10-04 17:23:16 | ETH | up | 0.75→0.83 | 0.71 → 0.85 | 12.41s | edge gone |  |
| 10-04 17:23:16 | DOGE | up | 0.37→0.42 | 0.23 → 0.44 | 12.41s | edge gone |  |
| 10-04 17:23:11 | BTC | up | 0.53→0.58 | 0.50 → 0.65 | 2.91s | edge gone |  |
