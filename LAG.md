# Lag Tracker

*Updated Sun Oct 04 21:26 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$199.26** | -4.6% | 1081 | $3.99 | $185.87 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1103 | 179 | -$480.24 | -10.9% | -$227.51 / -$252.73 |
| Sell after 30 sec | 1102 | 287 | -$513.51 | -11.7% | -$249.07 / -$264.44 |
| Hold to the close | 1081 | 410 | -$199.26 | -4.6% | -$335.15 / $135.89 |
| Hold, only edge 10¢+ | 387 | 110 | -$144.77 | -11.6% | -$84.85 / -$59.92 |
| Hold, first trade per window only | 338 | 138 | -$47.27 | -3.3% | -$105.80 / $58.53 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 4096 | 10% | 66% | +4.0¢ | 0.3¢ | edge gone 2795, price out of range 104, spread too wide 93 |

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
| BTC | 981 | 11.9s | 3% | 0% |
| DOGE | 1049 | 10.9s | 3% | 0% |
| ETH | 1191 | 10.8s | 4% | 0% |
| HYPE | 795 | 11.5s | 3% | 0% |
| NEAR | 1139 | 10.8s | 4% | 0% |
| SOL | 2057 | 10.9s | 3% | 0% |
| XRP | 2134 | 11.0s | 3% | 0% |
| ZEC | 1237 | 9.8s | 4% | 0% |
| **All** | **11363** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **6 ms** · Order book check: **61 ms** · Coinbase price delay: **34 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 21:26:36 | HYPE | up | 0.19→0.42 | 0.41 → 0.42 | no | edge gone |  |
| 10-04 21:26:36 | XRP | down | 0.68→0.61 | 0.23 → 0.33 | no | DOWN @ 0.33 | · / · / · |
| 10-04 21:26:23 | SOL | down | 0.32→0.22 | 0.81 → 0.83 | no | edge gone |  |
| 10-04 21:26:20 | XRP | up | 0.60→0.68 | 0.62 → 0.83 | 2.82s | edge gone |  |
| 10-04 21:26:19 | ETH | up | 0.06→0.12 | 0.04 → 0.05 | no | UP @ 0.05 | -0.19 / · / · |
| 10-04 21:26:08 | SOL | up | 0.16→0.23 | 0.13 → 0.17 | 14.32s | UP @ 0.17 | -0.01 / -0.98 / · |
| 10-04 21:26:05 | XRP | down | 0.58→0.50 | 0.32 → 0.39 | 2.79s | DOWN @ 0.39 | -1.35 / -1.54 / · |
| 10-04 21:25:42 | SOL | down | 0.27→0.22 | 0.79 → 0.83 | 10.30s | edge gone |  |
| 10-04 21:25:31 | XRP | up | 0.66→0.74 | 0.66 → 0.80 | 6.80s | edge gone |  |
| 10-04 21:25:24 | SOL | up | 0.23→0.28 | 0.21 → 0.25 | 0.26s | edge gone |  |
| 10-04 21:25:16 | XRP | up | 0.55→0.61 | 0.62 → 0.70 | 6.80s | edge gone |  |
| 10-04 21:24:58 | XRP | down | 0.54→0.48 | 0.45 → 0.45 | no | DOWN @ 0.45 | -0.70 / -2.61 / · |
| 10-04 21:24:52 | ETH | up | 0.03→0.09 | 0.03 → 0.05 | no | price out of range |  |
| 10-04 21:24:51 | SOL | up | 0.16→0.29 | 0.12 → 0.21 | no | UP @ 0.21 | -0.34 / -0.05 / · |
| 10-04 21:24:42 | XRP | up | 0.42→0.48 | 0.41 → 0.44 | 10.55s | edge gone |  |
| 10-04 21:24:26 | XRP | up | 0.37→0.44 | 0.35 → 0.40 | 12.30s | edge gone |  |
| 10-04 21:24:09 | DOGE | down | 0.76→0.69 | 0.23 → 0.33 | 13.80s | edge gone |  |
| 10-04 21:24:06 | XRP | down | 0.42→0.36 | 0.61 → 0.64 | 2.29s | edge gone |  |
| 10-04 21:23:47 | XRP | down | 0.42→0.36 | 0.60 → 0.61 | 21.31s | edge gone |  |
| 10-04 21:23:33 | DOGE | up | 0.65→0.70 | 0.64 → 0.63 | 20.31s | edge gone |  |
| 10-04 21:23:20 | SOL | down | 0.14→0.07 | 0.88 → 0.89 | no | DOWN @ 0.89 | -0.46 / -0.35 / · |
| 10-04 21:23:19 | XRP | up | 0.32→0.37 | 0.24 → 0.30 | 18.80s | UP @ 0.30 | 0.28 / 0.28 / · |
| 10-04 21:23:13 | DOGE | up | 0.57→0.66 | 0.58 → 0.61 | 9.80s | edge gone |  |
| 10-04 21:23:02 | XRP | up | 0.26→0.32 | 0.18 → 0.25 | 6.29s | UP @ 0.25 | -0.66 / 0.79 / · |
| 10-04 21:22:40 | XRP | up | 0.18→0.24 | 0.17 → 0.17 | 27.81s | UP @ 0.17 | -0.11 / 0.18 / · |
| 10-04 21:22:21 | DOGE | down | 0.56→0.46 | 0.46 → 0.57 | 2.29s | edge gone |  |
| 10-04 21:21:56 | DOGE | down | 0.80→0.71 | 0.32 → 0.37 | 11.55s | edge gone |  |
| 10-04 21:21:47 | XRP | down | 0.45→0.35 | 0.68 → 0.69 | 20.56s | edge gone |  |
| 10-04 21:21:37 | SOL | down | 0.24→0.19 | 0.78 → 0.81 | 15.55s | edge gone |  |
| 10-04 21:21:25 | HYPE | up | 0.17→0.24 | 0.07 → 0.24 | 12.55s | edge gone |  |
