# Lag Tracker

*Updated Sun Oct 04 21:16 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$199.26** | -4.6% | 1081 | $3.98 | $185.87 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1083 | 174 | -$475.69 | -11.0% | -$225.12 / -$250.57 |
| Sell after 30 sec | 1081 | 279 | -$506.30 | -11.8% | -$248.13 / -$258.17 |
| Hold to the close | 1081 | 410 | -$199.26 | -4.6% | -$335.15 / $135.89 |
| Hold, only edge 10¢+ | 387 | 110 | -$144.77 | -11.6% | -$84.85 / -$59.92 |
| Hold, first trade per window only | 338 | 138 | -$47.27 | -3.3% | -$105.80 / $58.53 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 4021 | 10% | 65% | +4.0¢ | 0.3¢ | edge gone 2743, price out of range 103, spread too wide 92 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 780 | 11.1s | 3% | 0% |
| BTC | 975 | 11.9s | 3% | 0% |
| DOGE | 1036 | 10.9s | 3% | 0% |
| ETH | 1180 | 10.8s | 4% | 0% |
| HYPE | 790 | 11.4s | 3% | 0% |
| NEAR | 1136 | 10.8s | 4% | 0% |
| SOL | 2043 | 10.9s | 3% | 0% |
| XRP | 2113 | 11.0s | 3% | 0% |
| ZEC | 1235 | 9.8s | 4% | 0% |
| **All** | **11288** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **6 ms** · Order book check: **61 ms** · Coinbase price delay: **34 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 21:16:28 | BNB | up | 0.17→0.24 | 0.22 → 0.34 | 9.78s | edge gone |  |
| 10-04 21:16:19 | ETH | up | 0.38→0.44 | 0.40 → 0.52 | 4.27s | edge gone |  |
| 10-04 21:16:18 | SOL | down | 0.43→0.30 | 0.58 → 0.59 | no | DOWN @ 0.60 | -1.61 / · / · |
| 10-04 21:16:12 | NEAR | down | 0.36→0.29 | 0.54 → 0.59 | 7.53s | DOWN @ 0.61 | -0.75 / · / · |
| 10-04 21:15:57 | SOL | down | 0.52→0.45 | 0.49 → 0.57 | 7.78s | edge gone |  |
| 10-04 21:15:56 | ETH | down | 0.48→0.42 | 0.54 → 0.62 | 8.78s | edge gone |  |
| 10-04 21:15:42 | SOL | down | 0.54→0.48 | 0.49 → 0.51 | 22.79s | edge gone |  |
| 10-04 21:13:38 | ETH | down | 1.00→0.92 | 0.01 → 0.11 | 7.31s | edge gone |  |
| 10-04 21:12:53 | HYPE | up | 0.74→0.84 | 0.78 → 0.90 | 7.32s | edge gone |  |
| 10-04 21:11:52 | HYPE | up | 0.54→0.64 | 0.60 → 0.64 | 8.34s | edge gone |  |
| 10-04 21:11:07 | SOL | down | 0.91→0.83 | 0.28 → 0.11 | no | DOWN @ 0.11 | -0.65 / -0.80 / -1.22 |
| 10-04 21:11:01 | HYPE | up | 0.24→0.40 | 0.18 → 0.33 | 14.36s | UP @ 0.33 | 1.51 / 2.37 / 6.54 |
| 10-04 21:10:56 | BTC | up | 0.85→0.95 | 0.88 → 0.91 | 19.61s | UP @ 0.91 | 0.40 / 0.57 / 0.85 |
| 10-04 21:10:56 | ETH | up | 0.78→0.86 | 0.88 → 0.92 | 19.61s | edge gone |  |
| 10-04 21:10:52 | SOL | down | 0.68→0.57 | 0.17 → 0.28 | 8.60s | DOWN @ 0.28 | -2.09 / -2.40 / -2.95 |
| 10-04 21:10:43 | HYPE | down | 0.36→0.25 | 0.72 → 0.80 | 17.86s | edge gone |  |
| 10-04 21:10:33 | BNB | up | 0.83→0.88 | 0.96 → 0.97 | 27.86s | price out of range |  |
| 10-04 21:10:23 | ZEC | up | 0.79→0.85 | 0.86 → 0.92 | 8.11s | edge gone |  |
| 10-04 21:09:52 | SOL | up | 0.56→0.66 | 0.59 → 0.73 | 9.12s | edge gone |  |
| 10-04 21:09:43 | BTC | up | 0.73→0.79 | 0.80 → 0.80 | 17.37s | edge gone |  |
| 10-04 21:09:42 | ETH | up | 0.71→0.77 | 0.75 → 0.80 | 19.13s | edge gone |  |
| 10-04 21:09:29 | XRP | down | 0.93→0.87 | 0.11 → 0.14 | no | edge gone |  |
| 10-04 21:09:28 | BTC | down | 0.82→0.76 | 0.16 → 0.29 | 2.37s | edge gone |  |
| 10-04 21:09:23 | SOL | down | 0.62→0.56 | 0.31 → 0.35 | 7.63s | DOWN @ 0.35 | 0.46 / -1.49 / -3.66 |
| 10-04 21:09:04 | ZEC | down | 0.66→0.59 | 0.42 → 0.31 | no | DOWN @ 0.31 | -0.50 / 0.38 / -3.25 |
| 10-04 21:09:03 | SOL | up | 0.47→0.67 | 0.56 → 0.69 | 0.09s | edge gone |  |
| 10-04 21:09:02 | XRP | up | 0.86→0.92 | 0.88 → 0.90 | 0.35s | edge gone |  |
| 10-04 21:09:01 | BNB | up | 0.66→0.81 | 0.87 → 0.93 | 14.89s | edge gone |  |
| 10-04 21:08:48 | SOL | up | 0.38→0.47 | 0.38 → 0.56 | 13.14s | edge gone |  |
| 10-04 21:08:47 | HYPE | up | 0.21→0.26 | 0.14 → 0.33 | 14.14s | edge gone |  |
