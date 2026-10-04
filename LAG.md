# Lag Tracker

*Updated Sun Oct 04 17:16 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$251.06** | -10.2% | 664 | $3.72 | $143.33 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 664 | 114 | -$273.92 | -11.1% | -$139.90 / -$134.02 |
| Sell after 30 sec | 664 | 175 | -$286.43 | -11.6% | -$161.35 / -$125.08 |
| Hold to the close | 664 | 222 | -$251.06 | -10.2% | -$376.95 / $125.89 |
| Hold, only edge 10¢+ | 230 | 58 | -$76.90 | -11.7% | -$143.97 / $67.07 |
| Hold, first trade per window only | 217 | 81 | -$60.89 | -7.0% | -$82.51 / $21.62 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 2524 | 9% | 67% | +5.0¢ | 0.3¢ | edge gone 1735, price out of range 65, spread too wide 60 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 708 | 11.1s | 3% | 0% |
| BTC | 828 | 11.9s | 3% | 0% |
| DOGE | 902 | 10.5s | 3% | 0% |
| ETH | 1001 | 10.8s | 4% | 0% |
| HYPE | 705 | 11.6s | 3% | 0% |
| NEAR | 958 | 10.8s | 3% | 0% |
| SOL | 1789 | 10.8s | 3% | 0% |
| XRP | 1825 | 11.2s | 3% | 0% |
| ZEC | 1075 | 9.6s | 4% | 0% |
| **All** | **9791** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **7 ms** · Order book check: **25 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 17:15:35 | ZEC | down | 0.51→0.45 | 0.50 → 0.54 | 5.51s | edge gone |  |
| 10-04 17:15:30 | ETH | down | 0.55→0.49 | 0.49 → 0.54 | no | edge gone |  |
| 10-04 17:13:10 | ETH | up | 0.08→0.14 | 0.17 → 0.08 | no | UP @ 0.08 | -0.19 / -0.73 / -0.91 |
| 10-04 17:12:54 | NEAR | down | 0.14→0.08 | 0.81 → 0.87 | 7.77s | DOWN @ 0.87 | -0.72 / -0.11 / 1.22 |
| 10-04 17:12:54 | ETH | up | 0.10→0.15 | 0.06 → 0.17 | 8.02s | edge gone |  |
| 10-04 17:12:25 | ETH | up | 0.05→0.18 | 0.05 → 0.12 | no | UP @ 0.12 | -0.68 / 0.13 / -1.28 |
| 10-04 17:12:02 | BTC | down | 0.10→0.05 | 0.95 → 0.97 | 15.27s | price out of range |  |
| 10-04 17:12:01 | ETH | down | 0.15→0.10 | 0.90 → 0.95 | 15.77s | edge gone |  |
| 10-04 17:11:51 | XRP | down | 0.19→0.14 | 0.83 → 0.86 | 11.27s | edge gone |  |
| 10-04 17:11:49 | NEAR | down | 0.48→0.38 | 0.45 → 0.49 | 12.52s | DOWN @ 0.53 | -0.26 / 1.88 / 4.52 |
| 10-04 17:11:26 | BTC | down | 0.21→0.13 | 0.89 → 0.92 | 5.77s | edge gone |  |
| 10-04 17:11:17 | NEAR | down | 0.40→0.33 | 0.58 → 0.52 | 0.26s | DOWN @ 0.53 | -0.65 / -1.15 / 4.53 |
| 10-04 17:11:14 | XRP | down | 0.19→0.13 | 0.78 → 0.81 | 2.77s | DOWN @ 0.81 | -0.33 / -0.15 / 1.79 |
| 10-04 17:11:00 | NEAR | down | 0.42→0.34 | 0.46 → 0.55 | 2.02s | DOWN @ 0.55 | -0.46 / -2.19 / 4.32 |
| 10-04 17:10:54 | XRP | down | 0.21→0.12 | 0.73 → 0.83 | 8.27s | DOWN @ 0.83 | -0.35 / -0.52 / 1.60 |
| 10-04 17:10:45 | NEAR | up | 0.49→0.55 | 0.35 → 0.70 | 2.02s | edge gone |  |
| 10-04 17:10:30 | ETH | up | 0.25→0.31 | 0.23 → 0.36 | 1.52s | edge gone |  |
| 10-04 17:10:30 | NEAR | up | 0.27→0.36 | 0.36 → 0.49 | 17.03s | edge gone |  |
| 10-04 17:10:22 | XRP | up | 0.20→0.27 | 0.22 → 0.29 | 9.77s | edge gone |  |
| 10-04 17:10:15 | NEAR | down | 0.27→0.20 | 0.68 → 0.69 | no | DOWN @ 0.69 | -0.71 / -4.59 / 2.95 |
| 10-04 17:10:07 | XRP | down | 0.25→0.15 | 0.71 → 0.83 | 9.77s | edge gone |  |
| 10-04 17:10:05 | BTC | up | 0.25→0.32 | 0.21 → 0.20 | no | UP @ 0.20 | -0.43 / -0.43 / -2.12 |
| 10-04 17:09:53 | NEAR | up | 0.24→0.30 | 0.44 → 0.39 | no | edge gone |  |
| 10-04 17:09:47 | XRP | down | 0.37→0.31 | 0.67 → 0.66 | 0.26s | edge gone |  |
| 10-04 17:09:34 | ETH | up | 0.23→0.29 | 0.29 → 0.27 | no | edge gone |  |
| 10-04 17:09:28 | XRP | up | 0.35→0.40 | 0.64 → 0.41 | no | edge gone |  |
| 10-04 17:09:26 | NEAR | down | 0.32→0.24 | 0.21 → 0.64 | 5.77s | DOWN @ 0.64 | -1.15 / -0.13 / 3.43 |
| 10-04 17:09:25 | SOL | down | 0.18→0.12 | 0.74 → 0.86 | 6.77s | edge gone |  |
| 10-04 17:09:19 | ETH | down | 0.38→0.33 | 0.60 → 0.71 | 0.01s | edge gone |  |
| 10-04 17:09:17 | BTC | down | 0.48→0.36 | 0.56 → 0.70 | 14.77s | edge gone |  |
