# Lag Tracker

*Updated Sun Oct 04 17:06 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$338.85** | -14.5% | 637 | $3.68 | $143.33 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 640 | 112 | -$260.83 | -11.1% | -$135.87 / -$124.96 |
| Sell after 30 sec | 640 | 170 | -$269.27 | -11.4% | -$156.69 / -$112.58 |
| Hold to the close | 637 | 200 | -$338.85 | -14.5% | -$369.64 / $30.79 |
| Hold, only edge 10¢+ | 227 | 55 | -$92.98 | -14.5% | -$136.75 / $43.77 |
| Hold, first trade per window only | 209 | 75 | -$88.73 | -10.6% | -$87.23 / -$1.50 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 2451 | 9% | 67% | +5.0¢ | 0.3¢ | edge gone 1686, price out of range 64, spread too wide 60 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 706 | 11.1s | 3% | 0% |
| BTC | 820 | 11.9s | 3% | 0% |
| DOGE | 902 | 10.5s | 3% | 0% |
| ETH | 987 | 10.8s | 4% | 0% |
| HYPE | 701 | 11.6s | 3% | 0% |
| NEAR | 943 | 10.8s | 3% | 0% |
| SOL | 1781 | 10.9s | 3% | 0% |
| XRP | 1809 | 11.2s | 3% | 0% |
| ZEC | 1069 | 9.6s | 4% | 0% |
| **All** | **9718** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **7 ms** · Order book check: **25 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 17:05:59 | ZEC | down | 0.68→0.57 | 0.26 → 0.34 | no | DOWN @ 0.36 | · / · / · |
| 10-04 17:05:46 | XRP | up | 0.59→0.66 | 0.70 → 0.68 | no | edge gone |  |
| 10-04 17:05:42 | ETH | up | 0.50→0.56 | 0.48 → 0.54 | no | edge gone |  |
| 10-04 17:05:24 | XRP | up | 0.55→0.62 | 0.55 → 0.63 | 7.29s | edge gone |  |
| 10-04 17:05:24 | NEAR | up | 0.81→0.88 | 0.78 → 0.86 | 7.79s | edge gone |  |
| 10-04 17:05:22 | SOL | up | 0.43→0.51 | 0.51 → 0.53 | 10.04s | edge gone |  |
| 10-04 17:05:15 | ZEC | down | 0.59→0.54 | 0.25 → 0.37 | 1.29s | DOWN @ 0.39 | -1.90 / -2.16 / · |
| 10-04 17:05:10 | DOGE | up | 0.61→0.82 | 0.64 → 0.84 | 6.54s | edge gone |  |
| 10-04 17:05:04 | ETH | down | 0.54→0.48 | 0.51 → 0.53 | no | edge gone |  |
| 10-04 17:05:03 | SOL | up | 0.40→0.46 | 0.46 → 0.48 | 13.54s | edge gone |  |
| 10-04 17:05:01 | XRP | down | 0.48→0.41 | 0.51 → 0.55 | no | edge gone |  |
| 10-04 17:05:01 | NEAR | down | 0.91→0.86 | 0.07 → 0.17 | 0.79s | edge gone |  |
| 10-04 17:04:41 | XRP | down | 0.52→0.45 | 0.49 → 0.47 | 20.55s | DOWN @ 0.49 | -0.36 / -1.15 / · |
| 10-04 17:04:30 | SOL | down | 0.46→0.40 | 0.49 → 0.53 | no | DOWN @ 0.53 | -1.06 / -0.56 / · |
| 10-04 17:04:22 | XRP | up | 0.46→0.52 | 0.55 → 0.51 | no | edge gone |  |
| 10-04 17:04:10 | SOL | down | 0.51→0.46 | 0.46 → 0.50 | no | edge gone |  |
| 10-04 17:04:04 | ETH | up | 0.48→0.53 | 0.42 → 0.49 | 12.31s | edge gone |  |
| 10-04 17:03:53 | SOL | up | 0.38→0.48 | 0.37 → 0.51 | 9.06s | edge gone |  |
| 10-04 17:03:49 | ETH | up | 0.30→0.36 | 0.30 → 0.36 | 13.06s | edge gone |  |
| 10-04 17:03:49 | BTC | up | 0.50→0.57 | 0.54 → 0.60 | 0.05s | edge gone |  |
| 10-04 17:03:49 | DOGE | up | 0.49→0.55 | 0.53 → 0.53 | 28.07s | edge gone |  |
| 10-04 17:03:41 | ZEC | up | 0.55→0.60 | 0.60 → 0.70 | 20.57s | edge gone |  |
| 10-04 17:03:35 | HYPE | up | 0.45→0.51 | 0.51 → 0.49 | 27.07s | edge gone |  |
| 10-04 16:58:37 | ETH | down | 0.68→0.47 | 0.26 → 0.38 | 2.88s | DOWN @ 0.38 | -0.73 / 5.30 / 6.03 |
| 10-04 16:58:32 | XRP | up | 0.50→0.64 | 0.73 → 0.80 | no | edge gone |  |
| 10-04 16:58:22 | ETH | down | 0.71→0.61 | 0.09 → 0.27 | 2.89s | DOWN @ 0.27 | -1.15 / 4.32 / 7.16 |
| 10-04 16:58:16 | XRP | up | 0.50→0.62 | 0.72 → 0.75 | no | edge gone |  |
| 10-04 16:58:01 | XRP | down | 0.80→0.71 | 0.23 → 0.16 | 8.39s | DOWN @ 0.16 | 0.71 / 0.13 / 8.25 |
| 10-04 16:57:55 | ETH | up | 0.81→0.88 | 0.90 → 0.90 | no | edge gone |  |
| 10-04 16:57:41 | XRP | down | 0.77→0.69 | 0.44 → 0.18 | no | DOWN @ 0.19 | -0.22 / 0.55 / 7.99 |
