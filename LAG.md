# Lag Tracker

*Updated Sun Oct 04 21:46 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$194.14** | -4.3% | 1130 | $3.97 | $185.87 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1131 | 185 | -$492.92 | -11.0% | -$232.99 / -$259.93 |
| Sell after 30 sec | 1131 | 294 | -$529.12 | -11.8% | -$251.18 / -$277.94 |
| Hold to the close | 1130 | 429 | -$194.14 | -4.3% | -$359.35 / $165.21 |
| Hold, only edge 10¢+ | 397 | 111 | -$155.70 | -12.3% | -$96.99 / -$58.71 |
| Hold, first trade per window only | 351 | 144 | -$45.65 | -3.1% | -$87.33 / $41.68 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 4188 | 10% | 66% | +4.0¢ | 0.3¢ | edge gone 2858, price out of range 104, spread too wide 95 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 781 | 11.1s | 3% | 0% |
| BTC | 984 | 11.9s | 3% | 0% |
| DOGE | 1068 | 10.8s | 3% | 0% |
| ETH | 1198 | 10.8s | 4% | 0% |
| HYPE | 795 | 11.5s | 3% | 0% |
| NEAR | 1145 | 10.8s | 4% | 0% |
| SOL | 2084 | 10.9s | 3% | 0% |
| XRP | 2159 | 11.0s | 3% | 0% |
| ZEC | 1241 | 9.8s | 4% | 0% |
| **All** | **11455** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **6 ms** · Order book check: **61 ms** · Coinbase price delay: **34 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 21:46:49 | SOL | down | 0.74→0.67 | 0.27 → 0.31 | no | edge gone |  |
| 10-04 21:46:40 | ETH | down | 0.69→0.63 | 0.45 → 0.40 | no | edge gone |  |
| 10-04 21:46:33 | SOL | up | 0.63→0.71 | 0.68 → 0.75 | 10.64s | edge gone |  |
| 10-04 21:46:23 | XRP | up | 0.51→0.57 | 0.60 → 0.63 | 6.13s | edge gone |  |
| 10-04 21:46:21 | ZEC | up | 0.77→0.83 | 0.61 → 0.87 | 7.63s | edge gone |  |
| 10-04 21:46:09 | DOGE | up | 0.70→0.75 | 0.64 → 0.74 | 4.63s | edge gone |  |
| 10-04 21:46:06 | ZEC | down | 0.56→0.48 | 0.45 → 0.41 | no | DOWN @ 0.41 | -2.39 / -2.96 / · |
| 10-04 21:46:04 | ETH | up | 0.51→0.56 | 0.48 → 0.54 | 10.39s | edge gone |  |
| 10-04 21:43:35 | SOL | up | 0.82→0.87 | 0.70 → 0.94 | 9.18s | edge gone |  |
| 10-04 21:43:21 | XRP | up | 0.08→0.15 | 0.13 → 0.07 | no | UP @ 0.08 | -0.22 / -0.07 / -0.81 |
| 10-04 21:43:17 | SOL | up | 0.46→0.60 | 0.52 → 0.72 | 11.69s | edge gone |  |
| 10-04 21:43:11 | DOGE | up | 0.69→0.78 | 0.72 → 0.88 | 2.94s | edge gone |  |
| 10-04 21:43:06 | XRP | up | 0.18→0.23 | 0.18 → 0.17 | no | spread too wide |  |
| 10-04 21:43:02 | SOL | up | 0.46→0.53 | 0.58 → 0.51 | 26.69s | edge gone |  |
| 10-04 21:42:52 | DOGE | up | 0.70→0.78 | 0.70 → 0.74 | 21.95s | edge gone |  |
| 10-04 21:42:51 | XRP | down | 0.28→0.13 | 0.84 → 0.84 | no | edge gone |  |
| 10-04 21:42:47 | SOL | up | 0.30→0.58 | 0.28 → 0.56 | 11.70s | edge gone |  |
| 10-04 21:42:32 | XRP | up | 0.20→0.27 | 0.17 → 0.17 | no | UP @ 0.17 | -0.35 / -0.59 / -1.80 |
| 10-04 21:42:32 | SOL | up | 0.31→0.41 | 0.40 → 0.32 | 26.71s | UP @ 0.32 | -0.32 / 1.21 / 6.64 |
| 10-04 21:42:31 | NEAR | down | 0.79→0.70 | 0.06 → 0.06 | no | DOWN @ 0.06 | -0.28 / -0.32 / -0.64 |
| 10-04 21:42:17 | XRP | down | 0.34→0.23 | 0.70 → 0.81 | 11.46s | edge gone |  |
| 10-04 21:42:13 | SOL | down | 0.42→0.28 | 0.53 → 0.63 | 0.95s | DOWN @ 0.63 | -0.13 / -0.13 / -6.47 |
| 10-04 21:41:59 | ETH | down | 0.88→0.79 | 0.07 → 0.15 | no | DOWN @ 0.15 | -0.77 / -1.15 / -1.59 |
| 10-04 21:41:59 | XRP | down | 0.47→0.41 | 0.54 → 0.67 | 14.96s | edge gone |  |
| 10-04 21:41:51 | NEAR | down | 0.79→0.71 | 0.06 → 0.05 | no | DOWN @ 0.05 | -0.16 / -0.21 / -0.56 |
| 10-04 21:41:43 | ETH | up | 0.85→0.90 | 0.86 → 0.90 | 0.96s | edge gone |  |
| 10-04 21:41:40 | SOL | down | 0.52→0.43 | 0.46 → 0.50 | 19.22s | DOWN @ 0.50 | -0.66 / 0.55 / -5.18 |
| 10-04 21:41:35 | XRP | up | 0.36→0.44 | 0.52 → 0.41 | no | edge gone |  |
| 10-04 21:41:24 | SOL | down | 0.52→0.43 | 0.34 → 0.53 | 4.51s | edge gone |  |
| 10-04 21:41:15 | BNB | down | 0.67→0.60 | 0.06 → 0.06 | no | DOWN @ 0.06 | -0.33 / -0.04 / -0.61 |
