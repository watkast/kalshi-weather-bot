# Lag Tracker

*Updated Sun Oct 04 20:36 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$225.11** | -5.6% | 1010 | $3.94 | $185.87 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1017 | 162 | -$447.50 | -11.2% | -$207.25 / -$240.25 |
| Sell after 30 sec | 1014 | 259 | -$481.39 | -12.0% | -$230.30 / -$251.09 |
| Hold to the close | 1010 | 376 | -$225.11 | -5.6% | -$322.94 / $97.83 |
| Hold, only edge 10¢+ | 357 | 96 | -$167.09 | -14.8% | -$104.41 / -$62.68 |
| Hold, first trade per window only | 313 | 126 | -$47.07 | -3.6% | -$98.66 / $51.59 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 3780 | 10% | 65% | +4.0¢ | 0.3¢ | edge gone 2581, price out of range 100, spread too wide 82 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 757 | 11.1s | 3% | 0% |
| BTC | 948 | 11.9s | 3% | 0% |
| DOGE | 1019 | 10.8s | 3% | 0% |
| ETH | 1150 | 10.8s | 4% | 0% |
| HYPE | 773 | 11.5s | 3% | 0% |
| NEAR | 1106 | 10.8s | 4% | 0% |
| SOL | 2005 | 10.9s | 3% | 0% |
| XRP | 2080 | 11.0s | 3% | 0% |
| ZEC | 1209 | 9.7s | 4% | 0% |
| **All** | **11047** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **6 ms** · Order book check: **61 ms** · Coinbase price delay: **35 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 20:36:06 | XRP | down | 0.77→0.68 | 0.21 → 0.24 | no | DOWN @ 0.24 | -0.36 / · / · |
| 10-04 20:36:05 | NEAR | down | 0.70→0.62 | 0.25 → 0.19 | no | DOWN @ 0.20 | -0.90 / · / · |
| 10-04 20:35:56 | ZEC | down | 0.79→0.72 | 0.16 → 0.19 | no | DOWN @ 0.19 | -0.98 / · / · |
| 10-04 20:35:50 | XRP | down | 0.81→0.75 | 0.16 → 0.19 | 6.69s | DOWN @ 0.19 | -0.13 / 0.26 / · |
| 10-04 20:35:32 | NEAR | down | 0.59→0.52 | 0.29 → 0.26 | no | DOWN @ 0.26 | -0.47 / -1.14 / · |
| 10-04 20:35:30 | XRP | up | 0.74→0.80 | 0.82 → 0.85 | 11.45s | edge gone |  |
| 10-04 20:35:29 | BNB | up | 0.27→0.39 | 0.53 → 0.62 | 12.20s | edge gone |  |
| 10-04 20:35:06 | NEAR | up | 0.52→0.58 | 0.69 → 0.73 | 20.71s | edge gone |  |
| 10-04 20:35:05 | HYPE | up | 0.58→0.65 | 0.55 → 0.68 | 6.96s | edge gone |  |
| 10-04 20:34:50 | ETH | up | 0.71→0.77 | 0.71 → 0.80 | 6.96s | edge gone |  |
| 10-04 20:34:43 | HYPE | down | 0.61→0.53 | 0.45 → 0.39 | no | DOWN @ 0.41 | -0.11 / -1.48 / · |
| 10-04 20:34:34 | ZEC | up | 0.43→0.49 | 0.52 → 0.50 | 22.22s | edge gone |  |
| 10-04 20:34:10 | SOL | up | 0.67→0.73 | 0.63 → 0.75 | 1.22s | edge gone |  |
| 10-04 20:34:03 | BTC | up | 0.75→0.82 | 0.76 → 0.78 | no | edge gone |  |
| 10-04 20:34:03 | XRP | up | 0.58→0.63 | 0.65 → 0.70 | 23.98s | edge gone |  |
| 10-04 20:33:46 | DOGE | up | 0.62→0.70 | 0.49 → 0.68 | 10.23s | edge gone |  |
| 10-04 20:33:46 | ZEC | up | 0.34→0.46 | 0.30 → 0.44 | 10.23s | edge gone |  |
| 10-04 20:33:46 | ETH | up | 0.51→0.67 | 0.38 → 0.63 | 10.23s | edge gone |  |
| 10-04 20:33:46 | HYPE | up | 0.42→0.49 | 0.43 → 0.57 | 10.23s | edge gone |  |
| 10-04 20:33:46 | BTC | up | 0.56→0.68 | 0.55 → 0.74 | 10.48s | edge gone |  |
| 10-04 20:33:46 | NEAR | up | 0.44→0.53 | 0.52 → 0.60 | 10.48s | edge gone |  |
| 10-04 20:33:46 | SOL | up | 0.39→0.51 | 0.46 → 0.62 | 10.48s | edge gone |  |
| 10-04 20:33:40 | XRP | down | 0.42→0.37 | 0.64 → 0.58 | no | edge gone |  |
| 10-04 20:33:28 | BTC | up | 0.48→0.55 | 0.50 → 0.52 | 13.24s | edge gone |  |
| 10-04 20:33:20 | XRP | up | 0.34→0.39 | 0.31 → 0.39 | 6.49s | edge gone |  |
| 10-04 20:33:09 | ETH | up | 0.25→0.32 | 0.28 → 0.29 | 17.99s | edge gone |  |
| 10-04 20:33:03 | SOL | up | 0.26→0.31 | 0.33 → 0.34 | 23.75s | edge gone |  |
| 10-04 20:33:01 | DOGE | up | 0.32→0.41 | 0.38 → 0.43 | 10.74s | edge gone |  |
| 10-04 20:32:45 | ETH | up | 0.21→0.30 | 0.27 → 0.32 | no | edge gone |  |
| 10-04 20:32:44 | BTC | up | 0.36→0.45 | 0.36 → 0.45 | 12.25s | edge gone |  |
