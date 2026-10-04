# Lag Tracker

*Updated Sun Oct 04 16:15 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$373.00** | -17.8% | 570 | $3.67 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 570 | 98 | -$237.09 | -11.3% | -$122.98 / -$114.11 |
| Sell after 30 sec | 570 | 144 | -$257.30 | -12.3% | -$143.44 / -$113.86 |
| Hold to the close | 570 | 172 | -$373.00 | -17.8% | -$315.59 / -$57.41 |
| Hold, only edge 10¢+ | 202 | 47 | -$107.08 | -18.6% | -$122.55 / $15.47 |
| Hold, first trade per window only | 189 | 69 | -$78.35 | -10.2% | -$55.43 / -$22.92 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 2190 | 10% | 67% | +5.0¢ | 0.3¢ | edge gone 1507, price out of range 58, spread too wide 55 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 690 | 11.1s | 3% | 0% |
| BTC | 795 | 11.9s | 3% | 0% |
| DOGE | 867 | 10.7s | 3% | 0% |
| ETH | 947 | 10.9s | 4% | 0% |
| HYPE | 697 | 11.6s | 3% | 0% |
| NEAR | 920 | 10.8s | 3% | 0% |
| SOL | 1739 | 10.8s | 3% | 0% |
| XRP | 1748 | 11.2s | 3% | 0% |
| ZEC | 1054 | 9.6s | 4% | 0% |
| **All** | **9457** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **19 ms** · Order book check: **25 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 16:13:35 | ETH | down | 0.65→0.58 | 0.26 → 0.34 | 7.86s | DOWN @ 0.34 | -1.96 / -3.46 / -3.56 |
| 10-04 16:13:15 | SOL | down | 0.71→0.66 | 0.11 → 0.11 | 12.62s | DOWN @ 0.11 | -0.24 / -0.36 / -1.17 |
| 10-04 16:13:14 | ETH | down | 0.62→0.56 | 0.36 → 0.27 | no | DOWN @ 0.27 | -0.09 / -0.09 / -2.84 |
| 10-04 16:12:53 | SOL | down | 0.69→0.58 | 0.25 → 0.19 | no | DOWN @ 0.19 | -0.98 / -0.79 / -2.01 |
| 10-04 16:12:52 | ETH | down | 0.57→0.44 | 0.35 → 0.39 | no | DOWN @ 0.39 | -0.83 / -1.42 / -4.07 |
| 10-04 16:12:35 | SOL | up | 0.62→0.67 | 0.87 → 0.80 | no | edge gone |  |
| 10-04 16:12:34 | ETH | down | 0.64→0.58 | 0.28 → 0.39 | 8.88s | edge gone |  |
| 10-04 16:12:19 | ETH | up | 0.59→0.66 | 0.71 → 0.73 | no | edge gone |  |
| 10-04 16:12:16 | SOL | down | 0.78→0.66 | 0.32 → 0.29 | no | DOWN @ 0.29 | -1.83 / -1.64 / -3.05 |
| 10-04 16:12:09 | ZEC | up | 0.21→0.27 | 0.23 → 0.14 | no | UP @ 0.14 | -0.32 / -0.79 / -1.49 |
| 10-04 16:12:04 | XRP | up | 0.09→0.16 | 0.08 → 0.07 | no | UP @ 0.07 | -0.24 / -0.30 / -0.72 |
| 10-04 16:12:04 | ETH | down | 0.60→0.51 | 0.28 → 0.43 | no | DOWN @ 0.43 | -0.75 / -1.05 / -4.48 |
| 10-04 16:12:01 | SOL | down | 0.73→0.61 | 0.23 → 0.35 | 12.14s | edge gone |  |
| 10-04 16:11:52 | ZEC | up | 0.26→0.34 | 0.21 → 0.19 | no | UP @ 0.19 | -1.24 / -0.70 / -2.01 |
| 10-04 16:11:47 | ETH | up | 0.62→0.68 | 0.77 → 0.73 | no | edge gone |  |
| 10-04 16:11:47 | XRP | up | 0.10→0.16 | 0.09 → 0.07 | no | UP @ 0.07 | -0.20 / -0.04 / -0.74 |
| 10-04 16:11:35 | SOL | up | 0.56→0.64 | 0.41 → 0.71 | 7.89s | edge gone |  |
| 10-04 16:11:32 | ETH | down | 0.69→0.64 | 0.37 → 0.23 | no | DOWN @ 0.24 | 0.34 / 1.71 / -2.51 |
| 10-04 16:11:28 | XRP | up | 0.06→0.12 | 0.06 → 0.09 | no | edge gone |  |
| 10-04 16:11:20 | SOL | down | 0.43→0.35 | 0.52 → 0.60 | 7.90s | DOWN @ 0.60 | -2.64 / -4.19 / -6.17 |
| 10-04 16:11:17 | ETH | up | 0.43→0.48 | 0.57 → 0.52 | 11.15s | edge gone |  |
| 10-04 16:11:16 | BTC | up | 0.22→0.30 | 0.27 → 0.28 | 26.90s | edge gone |  |
| 10-04 16:11:02 | SOL | down | 0.59→0.35 | 0.34 → 0.52 | 10.90s | DOWN @ 0.52 | 0.96 / -2.24 / -5.38 |
| 10-04 16:11:01 | BTC | down | 0.48→0.37 | 0.58 → 0.72 | 11.90s | edge gone |  |
| 10-04 16:11:01 | ETH | down | 0.61→0.50 | 0.36 → 0.46 | 12.15s | edge gone |  |
| 10-04 16:11:00 | ZEC | down | 0.49→0.44 | 0.42 → 0.63 | 12.40s | spread too wide |  |
| 10-04 16:11:00 | XRP | down | 0.17→0.06 | 0.89 → 0.94 | 12.40s | edge gone |  |
| 10-04 16:10:47 | SOL | down | 0.72→0.66 | 0.23 → 0.36 | 11.15s | edge gone |  |
| 10-04 16:10:46 | NEAR | down | 0.87→0.81 | 0.06 → 0.07 | 27.16s | DOWN @ 0.07 | 0.01 / 0.37 / -0.75 |
| 10-04 16:10:44 | ETH | down | 0.74→0.65 | 0.22 → 0.32 | 13.65s | edge gone |  |
