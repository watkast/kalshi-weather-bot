# Lag Tracker

*Updated Sun Oct 04 21:56 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$194.14** | -4.3% | 1130 | $3.97 | $185.87 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1157 | 197 | -$492.44 | -10.7% | -$241.40 / -$251.04 |
| Sell after 30 sec | 1156 | 309 | -$522.04 | -11.4% | -$260.67 / -$261.37 |
| Hold to the close | 1130 | 429 | -$194.14 | -4.3% | -$359.35 / $165.21 |
| Hold, only edge 10¢+ | 397 | 111 | -$155.70 | -12.3% | -$96.99 / -$58.71 |
| Hold, first trade per window only | 351 | 144 | -$45.65 | -3.1% | -$87.33 / $41.68 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 4260 | 10% | 66% | +4.0¢ | 0.3¢ | edge gone 2904, price out of range 104, spread too wide 95 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 783 | 11.1s | 3% | 0% |
| BTC | 991 | 11.8s | 3% | 0% |
| DOGE | 1073 | 10.9s | 3% | 0% |
| ETH | 1209 | 10.8s | 4% | 0% |
| HYPE | 796 | 11.6s | 3% | 0% |
| NEAR | 1151 | 10.8s | 3% | 0% |
| SOL | 2100 | 10.9s | 3% | 0% |
| XRP | 2181 | 11.1s | 3% | 0% |
| ZEC | 1243 | 9.8s | 4% | 0% |
| **All** | **11527** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **6 ms** · Order book check: **61 ms** · Coinbase price delay: **34 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 21:56:46 | XRP | up | 0.35→0.41 | 0.35 → 0.30 | no | UP @ 0.30 | -0.79 / · / · |
| 10-04 21:56:31 | XRP | down | 0.41→0.35 | 0.69 → 0.69 | no | edge gone |  |
| 10-04 21:56:26 | BTC | up | 0.20→0.26 | 0.12 → 0.23 | 3.04s | edge gone |  |
| 10-04 21:56:06 | XRP | up | 0.16→0.25 | 0.12 → 0.15 | 22.55s | UP @ 0.15 | 1.16 / 1.40 / · |
| 10-04 21:56:03 | NEAR | down | 0.15→0.10 | 0.74 → 0.87 | 10.29s | edge gone |  |
| 10-04 21:55:41 | XRP | down | 0.42→0.35 | 0.65 → 0.80 | 3.04s | edge gone |  |
| 10-04 21:55:30 | HYPE | down | 0.39→0.32 | 0.52 → 0.56 | 28.55s | DOWN @ 0.56 | -0.36 / 0.35 / · |
| 10-04 21:55:30 | SOL | down | 0.12→0.06 | 0.92 → 0.93 | 29.05s | edge gone |  |
| 10-04 21:55:17 | XRP | up | 0.33→0.42 | 0.25 → 0.39 | 12.04s | edge gone |  |
| 10-04 21:55:15 | DOGE | down | 0.17→0.12 | 0.83 → 0.89 | 0.26s | edge gone |  |
| 10-04 21:54:55 | BTC | down | 0.15→0.10 | 0.88 → 0.93 | 3.29s | edge gone |  |
| 10-04 21:54:53 | XRP | down | 0.52→0.43 | 0.47 → 0.47 | 20.80s | DOWN @ 0.47 | 0.74 / 1.46 / · |
| 10-04 21:54:52 | NEAR | down | 0.29→0.23 | 0.59 → 0.66 | 6.54s | DOWN @ 0.66 | -0.53 / -0.42 / · |
| 10-04 21:54:45 | SOL | down | 0.17→0.11 | 0.84 → 0.86 | 0.01s | edge gone |  |
| 10-04 21:54:39 | BTC | down | 0.22→0.17 | 0.84 → 0.90 | 5.04s | edge gone |  |
| 10-04 21:54:37 | DOGE | down | 0.37→0.30 | 0.67 → 0.69 | 21.30s | edge gone |  |
| 10-04 21:54:36 | ZEC | down | 0.84→0.79 | 0.09 → 0.09 | no | DOWN @ 0.13 | -0.89 / -0.71 / · |
| 10-04 21:54:35 | XRP | down | 0.53→0.47 | 0.47 → 0.46 | no | DOWN @ 0.46 | -0.85 / 2.38 / · |
| 10-04 21:54:24 | BTC | down | 0.31→0.25 | 0.74 → 0.84 | 5.04s | edge gone |  |
| 10-04 21:54:23 | SOL | down | 0.23→0.15 | 0.64 → 0.81 | 5.29s | DOWN @ 0.81 | -0.95 / 0.20 / · |
| 10-04 21:54:18 | NEAR | down | 0.40→0.35 | 0.48 → 0.52 | 10.54s | DOWN @ 0.52 | 0.04 / 0.55 / · |
| 10-04 21:54:16 | XRP | down | 0.64→0.59 | 0.22 → 0.36 | 0.26s | DOWN @ 0.36 | 0.65 / 0.16 / · |
| 10-04 21:54:12 | ETH | down | 0.32→0.27 | 0.67 → 0.77 | 2.04s | edge gone |  |
| 10-04 21:54:11 | DOGE | down | 0.48→0.42 | 0.35 → 0.53 | 2.54s | edge gone |  |
| 10-04 21:54:09 | BTC | down | 0.41→0.35 | 0.67 → 0.72 | 5.04s | edge gone |  |
| 10-04 21:54:07 | SOL | down | 0.38→0.31 | 0.57 → 0.63 | 6.29s | DOWN @ 0.63 | 0.28 / 1.52 / · |
| 10-04 21:54:01 | XRP | down | 0.79→0.72 | 0.19 → 0.18 | 27.80s | DOWN @ 0.18 | 0.55 / 2.41 / · |
| 10-04 21:53:46 | SOL | down | 0.38→0.32 | 0.61 → 0.70 | no | edge gone |  |
| 10-04 21:53:27 | ETH | down | 0.59→0.54 | 0.50 → 0.55 | 16.81s | edge gone |  |
| 10-04 21:53:24 | NEAR | down | 0.38→0.32 | 0.49 → 0.58 | 19.81s | DOWN @ 0.58 | 0.46 / -2.05 / · |
