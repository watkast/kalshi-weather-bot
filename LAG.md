# Lag Tracker

*Updated Sun Oct 04 20:56 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$206.64** | -5.1% | 1033 | $3.98 | $185.87 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1060 | 169 | -$467.78 | -11.1% | -$221.25 / -$246.53 |
| Sell after 30 sec | 1060 | 270 | -$504.64 | -12.0% | -$242.39 / -$262.25 |
| Hold to the close | 1033 | 388 | -$206.64 | -5.1% | -$316.34 / $109.70 |
| Hold, only edge 10¢+ | 368 | 102 | -$149.07 | -12.8% | -$76.12 / -$72.95 |
| Hold, first trade per window only | 321 | 130 | -$43.72 | -3.3% | -$98.69 / $54.97 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 3925 | 10% | 65% | +4.0¢ | 0.3¢ | edge gone 2672, price out of range 101, spread too wide 91 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 772 | 11.1s | 3% | 0% |
| BTC | 960 | 11.8s | 3% | 0% |
| DOGE | 1032 | 10.9s | 3% | 0% |
| ETH | 1167 | 10.8s | 4% | 0% |
| HYPE | 782 | 11.4s | 3% | 0% |
| NEAR | 1129 | 10.8s | 4% | 0% |
| SOL | 2020 | 10.9s | 3% | 0% |
| XRP | 2105 | 11.0s | 3% | 0% |
| ZEC | 1225 | 9.7s | 4% | 0% |
| **All** | **11192** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **6 ms** · Order book check: **61 ms** · Coinbase price delay: **34 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 20:56:33 | BNB | down | 0.81→0.61 | 0.08 → 0.09 | no | DOWN @ 0.10 | · / · / · |
| 10-04 20:56:08 | NEAR | up | 0.28→0.34 | 0.49 → 0.63 | 2.93s | spread too wide |  |
| 10-04 20:55:25 | NEAR | up | 0.27→0.33 | 0.49 → 0.51 | no | spread too wide |  |
| 10-04 20:55:23 | ZEC | up | 0.61→0.70 | 0.37 → 0.76 | 2.93s | spread too wide |  |
| 10-04 20:55:06 | BTC | up | 0.85→0.91 | 0.82 → 0.87 | 5.19s | UP @ 0.87 | -0.48 / -0.06 / · |
| 10-04 20:55:05 | XRP | up | 0.72→0.78 | 0.76 → 0.86 | 5.69s | edge gone |  |
| 10-04 20:55:05 | ZEC | up | 0.46→0.51 | 0.39 → 0.55 | 21.19s | edge gone |  |
| 10-04 20:54:46 | NEAR | up | 0.31→0.36 | 0.46 → 0.48 | 24.70s | edge gone |  |
| 10-04 20:54:45 | XRP | up | 0.62→0.68 | 0.70 → 0.76 | 10.45s | edge gone |  |
| 10-04 20:54:31 | NEAR | up | 0.34→0.39 | 0.45 → 0.46 | no | edge gone |  |
| 10-04 20:54:29 | XRP | up | 0.52→0.61 | 0.63 → 0.69 | 11.70s | edge gone |  |
| 10-04 20:54:04 | XRP | up | 0.48→0.54 | 0.68 → 0.57 | no | edge gone |  |
| 10-04 20:53:54 | NEAR | down | 0.31→0.26 | 0.60 → 0.60 | no | DOWN @ 0.60 | -1.14 / -0.95 / · |
| 10-04 20:53:51 | BNB | down | 0.75→0.60 | 0.07 → 0.14 | no | DOWN @ 0.14 | -0.57 / -0.58 / · |
| 10-04 20:53:51 | HYPE | down | 0.95→0.88 | 0.11 → 0.15 | no | edge gone |  |
| 10-04 20:53:51 | DOGE | down | 0.89→0.83 | 0.11 → 0.13 | no | edge gone |  |
| 10-04 20:53:51 | ZEC | down | 0.60→0.54 | 0.35 → 0.52 | 5.21s | edge gone |  |
| 10-04 20:53:50 | BTC | down | 0.81→0.67 | 0.20 → 0.37 | 5.46s | edge gone |  |
| 10-04 20:53:49 | XRP | down | 0.61→0.54 | 0.34 → 0.42 | 21.46s | edge gone |  |
| 10-04 20:53:35 | BTC | down | 0.88→0.83 | 0.19 → 0.21 | 20.47s | edge gone |  |
| 10-04 20:53:32 | XRP | down | 0.64→0.58 | 0.35 → 0.34 | no | DOWN @ 0.34 | -0.66 / 0.57 / · |
| 10-04 20:53:16 | XRP | down | 0.64→0.56 | 0.36 → 0.38 | no | DOWN @ 0.39 | -1.07 / -1.25 / · |
| 10-04 20:52:59 | XRP | down | 0.64→0.58 | 0.33 → 0.33 | no | DOWN @ 0.33 | -0.24 / -0.61 / · |
| 10-04 20:52:46 | ZEC | up | 0.65→0.71 | 0.77 → 0.78 | no | edge gone |  |
| 10-04 20:52:43 | XRP | up | 0.58→0.64 | 0.69 → 0.66 | no | edge gone |  |
| 10-04 20:52:42 | BNB | down | 0.65→0.57 | 0.19 → 0.15 | no | DOWN @ 0.15 | -0.53 / -0.66 / · |
| 10-04 20:52:40 | DOGE | down | 0.87→0.80 | 0.14 → 0.17 | no | edge gone |  |
| 10-04 20:52:32 | NEAR | down | 0.56→0.43 | 0.34 → 0.36 | 23.73s | DOWN @ 0.38 | 0.56 / 0.65 / · |
| 10-04 20:52:16 | XRP | up | 0.52→0.58 | 0.56 → 0.67 | 9.99s | edge gone |  |
| 10-04 20:52:07 | BNB | down | 0.64→0.52 | 0.22 → 0.19 | no | DOWN @ 0.19 | -0.36 / -0.47 / · |
