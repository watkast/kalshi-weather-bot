# Lag Tracker

*Updated Sun Oct 04 14:05 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$356.18** | -26.1% | 378 | $3.61 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 383 | 64 | -$167.24 | -12.1% | -$87.49 / -$79.75 |
| Sell after 30 sec | 382 | 88 | -$190.33 | -13.8% | -$93.06 / -$97.27 |
| Hold to the close | 378 | 101 | -$356.18 | -26.1% | -$208.26 / -$147.92 |
| Hold, only edge 10¢+ | 136 | 21 | -$147.67 | -41.3% | -$133.89 / -$13.78 |
| Hold, first trade per window only | 127 | 42 | -$84.98 | -16.8% | -$23.09 / -$61.89 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 1417 | 11% | 65% | +4.6¢ | 0.3¢ | edge gone 967, price out of range 38, spread too wide 28 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 676 | 11.1s | 3% | 0% |
| BTC | 698 | 11.9s | 3% | 0% |
| DOGE | 805 | 10.5s | 2% | 0% |
| ETH | 848 | 11.2s | 4% | 0% |
| HYPE | 658 | 11.4s | 4% | 0% |
| NEAR | 846 | 10.8s | 4% | 0% |
| SOL | 1584 | 11.0s | 3% | 0% |
| XRP | 1590 | 11.0s | 4% | 0% |
| ZEC | 979 | 9.7s | 4% | 0% |
| **All** | **8684** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 14:05:39 | XRP | up | 0.26→0.32 | 0.25 → 0.23 | no | UP @ 0.23 | · / · / · |
| 10-04 14:05:39 | SOL | up | 0.54→0.62 | 0.59 → 0.64 | no | edge gone |  |
| 10-04 14:05:21 | SOL | down | 0.54→0.48 | 0.48 → 0.42 | no | DOWN @ 0.42 | -0.54 / · / · |
| 10-04 14:05:19 | BTC | up | 0.43→0.49 | 0.49 → 0.49 | no | edge gone |  |
| 10-04 14:05:06 | SOL | up | 0.43→0.51 | 0.47 → 0.60 | 4.28s | edge gone |  |
| 10-04 14:04:40 | NEAR | down | 0.22→0.15 | 0.67 → 0.71 | 15.29s | DOWN @ 0.71 | -0.49 / 0.79 / · |
| 10-04 14:04:27 | XRP | down | 0.33→0.27 | 0.70 → 0.72 | 28.79s | edge gone |  |
| 10-04 14:04:24 | SOL | down | 0.43→0.36 | 0.59 → 0.60 | no | edge gone |  |
| 10-04 14:03:58 | SOL | up | 0.36→0.44 | 0.42 → 0.42 | no | edge gone |  |
| 10-04 14:03:48 | HYPE | up | 0.20→0.29 | 0.30 → 0.28 | no | edge gone |  |
| 10-04 14:03:40 | NEAR | up | 0.06→0.16 | 0.20 → 0.34 | 16.04s | spread too wide |  |
| 10-04 14:03:27 | SOL | up | 0.33→0.39 | 0.38 → 0.40 | 0.01s | edge gone |  |
| 10-04 14:03:26 | HYPE | up | 0.32→0.38 | 0.32 → 0.30 | no | UP @ 0.30 | -0.30 / -0.98 / · |
| 10-04 14:03:23 | ZEC | up | 0.17→0.23 | 0.11 → 0.14 | 18.04s | UP @ 0.15 | -0.55 / -0.36 / · |
| 10-04 14:03:16 | BTC | up | 0.31→0.43 | 0.39 → 0.39 | 9.78s | edge gone |  |
| 10-04 14:03:02 | XRP | down | 0.24→0.19 | 0.74 → 0.84 | 8.28s | edge gone |  |
| 10-04 14:03:02 | DOGE | down | 0.60→0.48 | 0.40 → 0.60 | 8.53s | edge gone |  |
| 10-04 14:02:58 | HYPE | down | 0.58→0.51 | 0.29 → 0.53 | 13.03s | edge gone |  |
| 10-04 14:02:57 | BTC | down | 0.49→0.42 | 0.50 → 0.55 | 13.79s | edge gone |  |
| 10-04 14:02:57 | ETH | down | 0.23→0.14 | 0.81 → 0.86 | 14.04s | edge gone |  |
| 10-04 14:02:50 | SOL | down | 0.44→0.37 | 0.61 → 0.60 | 20.29s | edge gone |  |
| 10-04 14:02:42 | XRP | up | 0.21→0.28 | 0.21 → 0.23 | 13.54s | UP @ 0.23 | -0.56 / -1.13 / · |
| 10-04 14:02:42 | BTC | up | 0.41→0.48 | 0.47 → 0.50 | 13.79s | edge gone |  |
| 10-04 14:02:41 | DOGE | up | 0.60→0.65 | 0.57 → 0.64 | no | edge gone |  |
| 10-04 14:02:23 | SOL | down | 0.44→0.37 | 0.55 → 0.61 | 17.54s | edge gone |  |
| 10-04 14:01:49 | XRP | down | 0.32→0.23 | 0.76 → 0.75 | no | edge gone |  |
| 10-04 14:01:28 | XRP | down | 0.32→0.26 | 0.72 → 0.76 | 12.28s | edge gone |  |
| 10-04 14:01:28 | ETH | down | 0.37→0.31 | 0.69 → 0.74 | 13.04s | edge gone |  |
| 10-04 13:58:41 | BTC | up | 0.56→0.69 | 0.80 → 0.89 | 6.83s | edge gone |  |
| 10-04 13:58:39 | SOL | up | 0.59→0.68 | 0.92 → 0.94 | no | edge gone |  |
