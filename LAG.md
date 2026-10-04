# Lag Tracker

*Updated Sun Oct 04 15:25 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$348.75** | -20.2% | 473 | $3.70 | $122.22 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 485 | 84 | -$196.98 | -10.9% | -$104.17 / -$92.81 |
| Sell after 30 sec | 485 | 120 | -$223.18 | -12.4% | -$109.71 / -$113.47 |
| Hold to the close | 473 | 138 | -$348.75 | -20.2% | -$246.41 / -$102.34 |
| Hold, only edge 10¢+ | 166 | 34 | -$115.50 | -25.4% | -$99.88 / -$15.62 |
| Hold, first trade per window only | 160 | 55 | -$98.69 | -15.2% | -$32.55 / -$66.14 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 1890 | 10% | 67% | +5.0¢ | 0.3¢ | edge gone 1309, price out of range 51, spread too wide 44 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 686 | 11.1s | 3% | 0% |
| BTC | 763 | 11.8s | 3% | 0% |
| DOGE | 845 | 10.6s | 3% | 0% |
| ETH | 905 | 11.0s | 4% | 0% |
| HYPE | 686 | 11.6s | 3% | 0% |
| NEAR | 880 | 10.8s | 4% | 0% |
| SOL | 1670 | 10.8s | 3% | 0% |
| XRP | 1690 | 11.1s | 3% | 0% |
| ZEC | 1032 | 9.6s | 4% | 0% |
| **All** | **9157** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **19 ms** · Order book check: **24 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 15:25:21 | XRP | up | 0.50→0.56 | 0.59 → 0.59 | no | edge gone |  |
| 10-04 15:25:19 | NEAR | down | 0.89→0.78 | 0.07 → 0.11 | no | DOWN @ 0.11 | · / · / · |
| 10-04 15:25:06 | XRP | down | 0.63→0.58 | 0.42 → 0.40 | no | edge gone |  |
| 10-04 15:25:05 | ETH | up | 0.85→0.91 | 0.85 → 0.88 | 11.59s | edge gone |  |
| 10-04 15:24:56 | NEAR | up | 0.74→0.83 | 0.85 → 0.89 | 5.34s | edge gone |  |
| 10-04 15:24:48 | XRP | down | 0.66→0.58 | 0.32 → 0.40 | 14.09s | edge gone |  |
| 10-04 15:24:46 | ZEC | down | 0.97→0.92 | 0.06 → 0.06 | no | edge gone |  |
| 10-04 15:24:45 | BTC | down | 0.78→0.72 | 0.15 → 0.24 | 1.34s | edge gone |  |
| 10-04 15:24:41 | ETH | down | 0.93→0.88 | 0.12 → 0.15 | 5.84s | edge gone |  |
| 10-04 15:24:30 | XRP | down | 0.72→0.65 | 0.26 → 0.33 | 16.59s | edge gone |  |
| 10-04 15:24:28 | BTC | down | 0.83→0.77 | 0.15 → 0.21 | 18.85s | edge gone |  |
| 10-04 15:24:16 | NEAR | down | 0.73→0.62 | 0.20 → 0.19 | no | DOWN @ 0.19 | -0.98 / -0.75 / · |
| 10-04 15:24:14 | XRP | down | 0.74→0.67 | 0.31 → 0.29 | no | edge gone |  |
| 10-04 15:23:59 | NEAR | up | 0.71→0.76 | 0.83 → 0.85 | no | edge gone |  |
| 10-04 15:23:57 | XRP | up | 0.71→0.77 | 0.71 → 0.75 | 19.85s | edge gone |  |
| 10-04 15:23:37 | NEAR | up | 0.74→0.81 | 0.87 → 0.87 | no | edge gone |  |
| 10-04 15:23:35 | BNB | down | 0.54→0.44 | 0.23 → 0.23 | no | DOWN @ 0.23 | -0.79 / -0.21 / · |
| 10-04 15:23:30 | XRP | down | 0.78→0.72 | 0.19 → 0.30 | 2.12s | edge gone |  |
| 10-04 15:23:15 | XRP | down | 0.84→0.78 | 0.22 → 0.25 | 17.13s | edge gone |  |
| 10-04 15:22:57 | DOGE | down | 0.41→0.32 | 0.61 → 0.68 | 4.37s | edge gone |  |
| 10-04 15:22:56 | BTC | up | 0.89→0.96 | 0.84 → 0.90 | 20.87s | UP @ 0.90 | -0.04 / -0.35 / · |
| 10-04 15:22:54 | HYPE | up | 0.27→0.33 | 0.35 → 0.34 | 22.87s | edge gone |  |
| 10-04 15:22:54 | XRP | down | 0.82→0.75 | 0.32 → 0.31 | no | edge gone |  |
| 10-04 15:22:27 | ETH | down | 0.95→0.88 | 0.14 → 0.17 | no | edge gone |  |
| 10-04 15:22:27 | XRP | down | 0.78→0.73 | 0.26 → 0.29 | 4.87s | edge gone |  |
| 10-04 15:22:26 | HYPE | down | 0.31→0.24 | 0.62 → 0.75 | 5.38s | edge gone |  |
| 10-04 15:22:09 | XRP | down | 0.86→0.79 | 0.23 → 0.24 | 22.63s | edge gone |  |
| 10-04 15:21:53 | SOL | down | 0.38→0.28 | 0.52 → 0.62 | 8.64s | DOWN @ 0.62 | -0.34 / 0.27 / · |
| 10-04 15:21:39 | ETH | down | 0.98→0.91 | 0.04 → 0.23 | 7.89s | edge gone |  |
| 10-04 15:21:39 | BTC | down | 0.99→0.94 | 0.06 → 0.15 | 22.89s | edge gone |  |
