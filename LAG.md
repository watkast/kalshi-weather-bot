# Lag Tracker

*Updated Sun Oct 04 18:16 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$173.56** | -6.0% | 770 | $3.77 | $145.64 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 770 | 125 | -$324.72 | -11.2% | -$167.27 / -$157.45 |
| Sell after 30 sec | 770 | 203 | -$325.51 | -11.2% | -$188.85 / -$136.66 |
| Hold to the close | 770 | 273 | -$173.56 | -6.0% | -$351.58 / $178.02 |
| Hold, only edge 10¢+ | 266 | 67 | -$89.87 | -11.8% | -$141.96 / $52.09 |
| Hold, first trade per window only | 249 | 98 | -$32.24 | -3.2% | -$85.44 / $53.20 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 2889 | 10% | 67% | +4.6¢ | 0.3¢ | edge gone 1976, price out of range 77, spread too wide 65 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 721 | 11.1s | 3% | 0% |
| BTC | 858 | 11.9s | 3% | 0% |
| DOGE | 953 | 10.7s | 3% | 0% |
| ETH | 1047 | 10.8s | 4% | 0% |
| HYPE | 724 | 11.6s | 3% | 0% |
| NEAR | 991 | 10.9s | 3% | 0% |
| SOL | 1833 | 10.8s | 3% | 0% |
| XRP | 1913 | 11.1s | 3% | 0% |
| ZEC | 1116 | 9.6s | 4% | 0% |
| **All** | **10156** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **9 ms** · Order book check: **26 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 18:16:26 | SOL | up | 0.62→0.68 | 0.76 → 0.76 | no | edge gone |  |
| 10-04 18:16:18 | XRP | down | 0.55→0.48 | 0.46 → 0.47 | no | DOWN @ 0.47 | · / · / · |
| 10-04 18:16:11 | SOL | up | 0.62→0.68 | 0.71 → 0.76 | 10.85s | edge gone |  |
| 10-04 18:15:32 | SOL | up | 0.47→0.53 | 0.52 → 0.57 | 4.36s | edge gone |  |
| 10-04 18:13:42 | ZEC | down | 0.14→0.07 | 0.96 → 0.98 | 27.89s | price out of range |  |
| 10-04 18:13:01 | HYPE | up | 0.73→0.80 | 0.93 → 0.95 | 24.15s | edge gone |  |
| 10-04 18:12:34 | NEAR | up | 0.85→0.93 | 0.98 → 0.98 | no | price out of range |  |
| 10-04 18:12:19 | DOGE | down | 0.11→0.05 | 0.94 → 0.96 | 20.41s | price out of range |  |
| 10-04 18:12:19 | XRP | up | 0.02→0.10 | 0.04 → 0.05 | no | UP @ 0.05 | -0.26 / -0.19 / -0.54 |
| 10-04 18:11:23 | ETH | up | 0.18→0.23 | 0.17 → 0.15 | no | UP @ 0.15 | -0.28 / -0.70 / -1.59 |
| 10-04 18:11:06 | DOGE | down | 0.24→0.18 | 0.83 → 0.85 | 3.43s | edge gone |  |
| 10-04 18:11:02 | BNB | down | 0.40→0.21 | 0.15 → 0.09 | no | DOWN @ 0.09 | -0.33 / -0.34 / -1.00 |
| 10-04 18:10:37 | HYPE | up | 0.59→0.77 | 0.58 → 0.86 | 17.69s | edge gone |  |
| 10-04 18:10:34 | ZEC | up | 0.14→0.20 | 0.09 → 0.15 | no | UP @ 0.15 | -0.98 / -1.31 / -1.59 |
| 10-04 18:10:33 | DOGE | up | 0.17→0.25 | 0.14 → 0.18 | 21.44s | UP @ 0.19 | -0.39 / -0.46 / -1.99 |
| 10-04 18:10:33 | NEAR | up | 0.71→0.76 | 0.88 → 0.92 | 7.19s | edge gone |  |
| 10-04 18:10:32 | ETH | up | 0.15→0.22 | 0.13 → 0.26 | 7.44s | edge gone |  |
| 10-04 18:10:07 | BTC | up | 0.35→0.45 | 0.48 → 0.47 | no | edge gone |  |
| 10-04 18:09:55 | NEAR | up | 0.59→0.66 | 0.70 → 0.81 | 14.95s | edge gone |  |
| 10-04 18:09:50 | BTC | down | 0.45→0.35 | 0.51 → 0.62 | 19.95s | edge gone |  |
| 10-04 18:09:41 | DOGE | down | 0.28→0.22 | 0.70 → 0.78 | 13.96s | edge gone |  |
| 10-04 18:09:14 | XRP | down | 0.16→0.09 | 0.81 → 0.85 | 10.71s | DOWN @ 0.85 | -0.29 / -0.29 / 1.41 |
| 10-04 18:08:46 | XRP | up | 0.13→0.22 | 0.19 → 0.21 | no | edge gone |  |
| 10-04 18:08:45 | NEAR | up | 0.41→0.49 | 0.68 → 0.65 | no | edge gone |  |
| 10-04 18:08:31 | XRP | down | 0.30→0.25 | 0.70 → 0.78 | 9.22s | edge gone |  |
| 10-04 18:08:30 | DOGE | down | 0.44→0.34 | 0.50 → 0.67 | 9.97s | edge gone |  |
| 10-04 18:08:21 | BTC | up | 0.42→0.48 | 0.45 → 0.54 | 3.72s | edge gone |  |
| 10-04 18:08:16 | XRP | down | 0.34→0.23 | 0.73 → 0.70 | 24.23s | DOWN @ 0.70 | -0.43 / 0.57 / 2.85 |
| 10-04 18:08:14 | DOGE | up | 0.57→0.64 | 0.57 → 0.64 | no | edge gone |  |
| 10-04 18:07:55 | ETH | down | 0.30→0.23 | 0.74 → 0.79 | 15.23s | edge gone |  |
