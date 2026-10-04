# Lag Tracker

*Updated Sun Oct 04 20:17 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$220.37** | -5.6% | 992 | $3.96 | $185.87 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 992 | 158 | -$434.92 | -11.1% | -$203.05 / -$231.87 |
| Sell after 30 sec | 992 | 252 | -$470.52 | -12.0% | -$228.57 / -$241.95 |
| Hold to the close | 992 | 371 | -$220.37 | -5.6% | -$349.18 / $128.81 |
| Hold, only edge 10¢+ | 350 | 95 | -$157.75 | -14.2% | -$107.20 / -$50.55 |
| Hold, first trade per window only | 307 | 125 | -$38.28 | -3.0% | -$102.33 / $64.05 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 3665 | 10% | 66% | +4.0¢ | 0.3¢ | edge gone 2495, price out of range 98, spread too wide 80 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 752 | 11.1s | 3% | 0% |
| BTC | 938 | 11.9s | 3% | 0% |
| DOGE | 1011 | 10.9s | 3% | 0% |
| ETH | 1139 | 10.9s | 4% | 0% |
| HYPE | 765 | 11.6s | 3% | 0% |
| NEAR | 1093 | 10.8s | 4% | 0% |
| SOL | 1976 | 10.9s | 3% | 0% |
| XRP | 2059 | 11.0s | 3% | 0% |
| ZEC | 1199 | 9.7s | 4% | 0% |
| **All** | **10932** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **7 ms** · Order book check: **28 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 20:13:24 | ZEC | down | 0.93→0.84 | 0.06 → 0.04 | no | price out of range |  |
| 10-04 20:13:08 | NEAR | down | 0.85→0.76 | 0.23 → 0.04 | no | DOWN @ 0.05 | -0.28 / -0.05 / 9.45 |
| 10-04 20:13:06 | BTC | up | 0.33→0.41 | 0.10 → 0.43 | 28.11s | edge gone |  |
| 10-04 20:13:03 | ETH | up | 0.06→0.11 | 0.01 → 0.03 | no | price out of range |  |
| 10-04 20:13:00 | DOGE | down | 0.31→0.25 | 0.87 → 0.80 | 19.12s | edge gone |  |
| 10-04 20:12:51 | NEAR | up | 0.59→0.68 | 0.83 → 0.92 | 0.10s | edge gone |  |
| 10-04 20:12:51 | ZEC | up | 0.66→0.75 | 0.65 → 0.88 | 13.12s | edge gone |  |
| 10-04 20:12:51 | BTC | up | 0.12→0.19 | 0.07 → 0.23 | no | edge gone |  |
| 10-04 20:11:58 | NEAR | up | 0.38→0.58 | 0.43 → 0.64 | 20.63s | edge gone |  |
| 10-04 20:11:55 | ZEC | up | 0.39→0.52 | 0.42 → 0.68 | 24.13s | spread too wide |  |
| 10-04 20:11:43 | NEAR | up | 0.22→0.27 | 0.34 → 0.45 | 5.88s | edge gone |  |
| 10-04 20:11:20 | NEAR | up | 0.11→0.17 | 0.17 → 0.27 | 14.38s | edge gone |  |
| 10-04 20:11:10 | DOGE | up | 0.27→0.34 | 0.30 → 0.24 | no | UP @ 0.24 | -1.25 / -1.70 / -2.56 |
| 10-04 20:11:01 | BTC | down | 0.33→0.27 | 0.77 → 0.80 | 17.64s | edge gone |  |
| 10-04 20:10:56 | ZEC | up | 0.44→0.49 | 0.42 → 0.49 | 7.89s | edge gone |  |
| 10-04 20:10:33 | HYPE | up | 0.69→0.80 | 0.50 → 0.73 | 1.14s | UP @ 0.73 | 0.13 / 0.13 / 2.56 |
| 10-04 20:10:29 | BTC | up | 0.20→0.28 | 0.15 → 0.23 | 5.14s | UP @ 0.23 | -0.16 / -0.26 / 7.57 |
| 10-04 20:10:17 | ZEC | up | 0.17→0.22 | 0.17 → 0.23 | 1.65s | edge gone |  |
| 10-04 20:09:56 | HYPE | down | 0.51→0.39 | 0.50 → 0.58 | 7.65s | edge gone |  |
| 10-04 20:09:38 | HYPE | down | 0.57→0.45 | 0.59 → 0.51 | no | edge gone |  |
| 10-04 20:09:31 | DOGE | down | 0.29→0.24 | 0.87 → 0.86 | no | edge gone |  |
| 10-04 20:09:04 | ZEC | down | 0.22→0.15 | 0.93 → 0.85 | 0.40s | edge gone |  |
| 10-04 20:08:09 | BTC | up | 0.27→0.36 | 0.26 → 0.25 | no | UP @ 0.25 | -0.66 / -0.95 / 7.36 |
| 10-04 20:07:29 | BTC | down | 0.33→0.28 | 0.67 → 0.74 | 5.19s | edge gone |  |
| 10-04 20:07:23 | BNB | up | 0.12→0.21 | 0.36 → 0.36 | no | edge gone |  |
| 10-04 20:07:05 | XRP | down | 0.22→0.17 | 0.80 → 0.80 | 29.06s | edge gone |  |
| 10-04 20:06:37 | XRP | down | 0.23→0.18 | 0.79 → 0.83 | no | edge gone |  |
| 10-04 20:06:36 | ZEC | down | 0.33→0.24 | 0.62 → 0.80 | 12.56s | edge gone |  |
| 10-04 20:06:31 | HYPE | up | 0.46→0.55 | 0.52 → 0.55 | no | edge gone |  |
| 10-04 20:06:29 | BNB | up | 0.13→0.25 | 0.40 → 0.39 | no | edge gone |  |
