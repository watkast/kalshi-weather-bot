# Lag Tracker

*Updated Sun Oct 04 19:06 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$382.81** | -11.6% | 861 | $3.85 | $161.50 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 875 | 138 | -$388.98 | -11.5% | -$179.37 / -$209.61 |
| Sell after 30 sec | 875 | 220 | -$408.99 | -12.1% | -$209.45 / -$199.54 |
| Hold to the close | 861 | 292 | -$382.81 | -11.6% | -$308.27 / -$74.54 |
| Hold, only edge 10¢+ | 309 | 72 | -$192.44 | -21.1% | -$122.90 / -$69.54 |
| Hold, first trade per window only | 270 | 105 | -$61.18 | -5.5% | -$83.14 / $21.96 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 3233 | 10% | 65% | +4.0¢ | 0.3¢ | edge gone 2195, price out of range 92, spread too wide 70 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 737 | 11.1s | 3% | 0% |
| BTC | 891 | 11.9s | 3% | 0% |
| DOGE | 969 | 10.9s | 3% | 0% |
| ETH | 1087 | 10.9s | 4% | 0% |
| HYPE | 730 | 11.6s | 3% | 0% |
| NEAR | 1046 | 10.8s | 3% | 0% |
| SOL | 1912 | 10.9s | 3% | 0% |
| XRP | 1984 | 11.1s | 3% | 0% |
| ZEC | 1144 | 9.6s | 4% | 0% |
| **All** | **10500** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **9 ms** · Order book check: **27 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 19:06:43 | BNB | down | 0.76→0.51 | 0.18 → 0.15 | no | DOWN @ 0.15 | · / · / · |
| 10-04 19:05:48 | NEAR | down | 0.72→0.60 | 0.33 → 0.28 | no | DOWN @ 0.29 | -0.64 / -0.49 / · |
| 10-04 19:05:38 | ZEC | down | 0.79→0.73 | 0.15 → 0.20 | 10.53s | DOWN @ 0.20 | -0.50 / -0.04 / · |
| 10-04 19:05:37 | BNB | down | 0.69→0.60 | 0.17 → 0.20 | no | DOWN @ 0.20 | -0.33 / -0.71 / · |
| 10-04 19:05:30 | NEAR | up | 0.57→0.62 | 0.68 → 0.72 | no | edge gone |  |
| 10-04 19:05:17 | ZEC | down | 0.86→0.81 | 0.19 → 0.14 | no | DOWN @ 0.14 | -0.24 / 0.13 / · |
| 10-04 19:05:00 | SOL | down | 0.90→0.84 | 0.13 → 0.18 | no | edge gone |  |
| 10-04 19:04:58 | ZEC | down | 0.82→0.76 | 0.20 → 0.17 | no | DOWN @ 0.17 | -0.39 / -0.57 / · |
| 10-04 19:04:17 | ZEC | up | 0.65→0.76 | 0.56 → 0.80 | 1.78s | edge gone |  |
| 10-04 19:04:02 | ZEC | up | 0.53→0.58 | 0.58 → 0.68 | 16.78s | edge gone |  |
| 10-04 19:03:45 | SOL | up | 0.83→0.88 | 0.82 → 0.79 | no | UP @ 0.79 | -0.24 / 0.18 / · |
| 10-04 19:03:15 | SOL | down | 0.78→0.73 | 0.23 → 0.24 | no | edge gone |  |
| 10-04 19:02:55 | ETH | up | 0.81→0.86 | 0.69 → 0.72 | 8.80s | UP @ 0.72 | -0.40 / -0.40 / · |
| 10-04 19:02:41 | SOL | up | 0.74→0.81 | 0.78 → 0.76 | no | UP @ 0.76 | -0.37 / -0.16 / · |
| 10-04 19:02:39 | BNB | down | 0.59→0.39 | 0.32 → 0.30 | no | DOWN @ 0.30 | -0.30 / -0.59 / · |
| 10-04 19:02:36 | NEAR | up | 0.50→0.57 | 0.59 → 0.62 | 0.29s | edge gone |  |
| 10-04 19:02:27 | BTC | up | 0.71→0.83 | 0.59 → 0.70 | 6.80s | UP @ 0.70 | -0.61 / -0.51 / · |
| 10-04 19:02:24 | ZEC | up | 0.45→0.52 | 0.50 → 0.59 | 9.31s | edge gone |  |
| 10-04 19:02:10 | SOL | down | 0.74→0.68 | 0.29 → 0.29 | no | edge gone |  |
| 10-04 19:01:53 | HYPE | up | 0.67→0.73 | 0.65 → 0.77 | 10.57s | edge gone |  |
| 10-04 19:01:52 | BNB | up | 0.40→0.47 | 0.51 → 0.76 | 11.32s | edge gone |  |
| 10-04 19:01:52 | SOL | up | 0.68→0.86 | 0.49 → 0.68 | 12.07s | UP @ 0.68 | -0.21 / 0.20 / · |
| 10-04 19:01:51 | ETH | up | 0.45→0.75 | 0.42 → 0.68 | 12.32s | UP @ 0.68 | -1.03 / -0.73 / · |
| 10-04 19:01:51 | ZEC | up | 0.33→0.49 | 0.35 → 0.62 | 12.32s | edge gone |  |
| 10-04 19:01:51 | DOGE | up | 0.55→0.67 | 0.52 → 0.75 | 12.32s | edge gone |  |
| 10-04 19:01:51 | BTC | up | 0.51→0.78 | 0.49 → 0.65 | 12.32s | UP @ 0.65 | -0.93 / -0.22 / · |
| 10-04 19:01:47 | XRP | up | 0.36→0.41 | 0.40 → 0.42 | 16.32s | edge gone |  |
| 10-04 19:01:32 | BNB | up | 0.25→0.30 | 0.60 → 0.53 | no | edge gone |  |
| 10-04 19:01:29 | XRP | up | 0.33→0.38 | 0.44 → 0.40 | no | edge gone |  |
| 10-04 19:01:18 | SOL | down | 0.46→0.39 | 0.50 → 0.51 | no | DOWN @ 0.51 | -0.46 / -0.36 / · |
