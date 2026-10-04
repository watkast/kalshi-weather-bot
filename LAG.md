# Lag Tracker

*Updated Sun Oct 04 16:45 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$363.43** | -16.9% | 587 | $3.64 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 603 | 103 | -$250.13 | -11.4% | -$129.59 / -$120.54 |
| Sell after 30 sec | 603 | 150 | -$271.03 | -12.3% | -$154.62 / -$116.41 |
| Hold to the close | 587 | 179 | -$363.43 | -16.9% | -$344.01 / -$19.42 |
| Hold, only edge 10¢+ | 209 | 48 | -$116.09 | -19.5% | -$130.66 / $14.57 |
| Hold, first trade per window only | 196 | 71 | -$81.58 | -10.3% | -$66.44 / -$15.14 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 2314 | 10% | 67% | +5.0¢ | 0.3¢ | edge gone 1590, price out of range 62, spread too wide 59 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 705 | 11.1s | 3% | 0% |
| BTC | 807 | 11.9s | 3% | 0% |
| DOGE | 885 | 10.5s | 3% | 0% |
| ETH | 956 | 10.8s | 4% | 0% |
| HYPE | 698 | 11.6s | 3% | 0% |
| NEAR | 935 | 10.8s | 3% | 0% |
| SOL | 1767 | 10.9s | 3% | 0% |
| XRP | 1768 | 11.2s | 3% | 0% |
| ZEC | 1060 | 9.6s | 4% | 0% |
| **All** | **9581** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **7 ms** · Order book check: **25 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 16:41:56 | DOGE | down | 0.83→0.78 | 0.18 → 0.08 | no | DOWN @ 0.08 | -0.57 / -0.69 / · |
| 10-04 16:41:38 | DOGE | down | 0.73→0.66 | 0.19 → 0.13 | no | DOWN @ 0.13 | -0.01 / -1.13 / · |
| 10-04 16:41:20 | XRP | up | 0.84→0.90 | 0.92 → 0.93 | 23.06s | edge gone |  |
| 10-04 16:40:52 | XRP | down | 0.83→0.76 | 0.09 → 0.14 | 5.82s | DOWN @ 0.14 | -0.37 / -0.98 / · |
| 10-04 16:40:29 | XRP | up | 0.85→0.90 | 0.90 → 0.91 | no | edge gone |  |
| 10-04 16:40:19 | DOGE | up | 0.71→0.78 | 0.77 → 0.89 | 8.58s | edge gone |  |
| 10-04 16:40:15 | SOL | down | 0.97→0.88 | 0.06 → 0.08 | no | DOWN @ 0.08 | -0.17 / -0.17 / · |
| 10-04 16:39:55 | XRP | down | 0.93→0.87 | 0.09 → 0.11 | no | edge gone |  |
| 10-04 16:39:49 | BNB | up | 0.24→0.39 | 0.57 → 0.63 | no | edge gone |  |
| 10-04 16:39:33 | DOGE | down | 0.69→0.59 | 0.26 → 0.33 | 9.84s | DOWN @ 0.33 | -1.48 / -1.58 / · |
| 10-04 16:39:18 | XRP | up | 0.89→0.95 | 0.91 → 0.95 | no | edge gone |  |
| 10-04 16:39:16 | DOGE | up | 0.59→0.67 | 0.69 → 0.76 | 12.09s | edge gone |  |
| 10-04 16:38:49 | BNB | down | 0.34→0.14 | 0.24 → 0.44 | 8.35s | DOWN @ 0.44 | -0.16 / -0.85 / · |
| 10-04 16:38:49 | XRP | down | 0.93→0.88 | 0.12 → 0.10 | no | edge gone |  |
| 10-04 16:38:34 | DOGE | up | 0.27→0.34 | 0.27 → 0.33 | 8.85s | edge gone |  |
| 10-04 16:38:33 | NEAR | up | 0.88→0.94 | 0.87 → 0.90 | 9.60s | edge gone |  |
| 10-04 16:38:27 | XRP | down | 0.84→0.77 | 0.06 → 0.18 | 15.61s | DOWN @ 0.18 | -1.10 / -1.19 / · |
| 10-04 16:38:26 | BNB | down | 0.61→0.46 | 0.11 → 0.25 | 2.10s | DOWN @ 0.28 | -1.11 / 1.27 / · |
| 10-04 16:38:13 | DOGE | down | 0.46→0.39 | 0.45 → 0.60 | 0.09s | edge gone |  |
| 10-04 16:38:12 | XRP | down | 0.93→0.88 | 0.04 → 0.07 | 15.61s | DOWN @ 0.07 | 0.24 / -0.18 / · |
| 10-04 16:37:58 | DOGE | down | 0.84→0.69 | 0.06 → 0.16 | 15.11s | DOWN @ 0.16 | 3.27 / 5.46 / · |
| 10-04 16:37:01 | DOGE | down | 0.88→0.82 | 0.06 → 0.07 | no | DOWN @ 0.07 | -0.19 / -0.20 / · |
| 10-04 16:36:07 | NEAR | down | 0.93→0.87 | 0.14 → 0.16 | no | edge gone |  |
| 10-04 16:35:30 | DOGE | up | 0.71→0.80 | 0.82 → 0.89 | 12.80s | edge gone |  |
| 10-04 16:34:15 | NEAR | up | 0.83→0.92 | 0.73 → 0.90 | 12.31s | UP @ 0.91 | 0.03 / -0.61 / · |
| 10-04 16:34:00 | NEAR | up | 0.62→0.67 | 0.70 → 0.75 | 27.57s | edge gone |  |
| 10-04 16:33:43 | NEAR | up | 0.72→0.77 | 0.79 → 0.85 | no | edge gone |  |
| 10-04 16:33:43 | SOL | up | 0.77→0.85 | 0.85 → 0.87 | 14.57s | edge gone |  |
| 10-04 16:33:37 | BNB | up | 0.34→0.42 | 0.71 → 0.69 | no | edge gone |  |
| 10-04 16:33:01 | ETH | down | 0.89→0.84 | 0.13 → 0.14 | no | edge gone |  |
