# Lag Tracker

*Updated Sun Oct 04 11:34 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$107.98** | -20.8% | 148 | $3.53 | $83.77 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 155 | 28 | -$65.90 | -12.0% | -$31.00 / -$34.90 |
| Sell after 30 sec | 154 | 37 | -$67.06 | -12.3% | -$32.68 / -$34.38 |
| Hold to the close | 148 | 41 | -$107.98 | -20.8% | $9.07 / -$117.05 |
| Hold, only edge 10¢+ | 49 | 4 | -$79.36 | -66.5% | -$31.43 / -$47.93 |
| Hold, first trade per window only | 56 | 20 | -$18.55 | -8.5% | -$4.65 / -$13.90 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 622 | 11% | 66% | +5.0¢ | 0.3¢ | edge gone 437, price out of range 24, spread too wide 6 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 652 | 11.1s | 3% | 0% |
| BTC | 586 | 11.9s | 3% | 0% |
| DOGE | 765 | 10.5s | 2% | 0% |
| ETH | 756 | 10.9s | 4% | 0% |
| HYPE | 619 | 11.2s | 4% | 0% |
| NEAR | 772 | 10.8s | 4% | 0% |
| SOL | 1409 | 10.8s | 3% | 0% |
| XRP | 1427 | 11.0s | 4% | 0% |
| ZEC | 903 | 9.6s | 4% | 0% |
| **All** | **7889** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 11:34:32 | DOGE | up | 0.26→0.34 | 0.24 → 0.26 | no | UP @ 0.26 | -0.57 / · / · |
| 10-04 11:33:58 | XRP | up | 0.21→0.28 | 0.24 → 0.25 | 6.53s | edge gone |  |
| 10-04 11:33:45 | SOL | down | 0.31→0.24 | 0.65 → 0.75 | 4.53s | edge gone |  |
| 10-04 11:33:45 | BTC | down | 0.52→0.45 | 0.41 → 0.55 | 20.04s | edge gone |  |
| 10-04 11:33:43 | ETH | down | 0.33→0.24 | 0.65 → 0.75 | 6.28s | edge gone |  |
| 10-04 11:33:40 | XRP | down | 0.29→0.24 | 0.77 → 0.77 | no | edge gone |  |
| 10-04 11:33:18 | ZEC | down | 0.35→0.29 | 0.66 → 0.73 | 1.28s | edge gone |  |
| 10-04 11:33:11 | DOGE | up | 0.22→0.31 | 0.22 → 0.25 | no | UP @ 0.25 | -0.57 / -0.08 / · |
| 10-04 11:32:58 | BTC | up | 0.44→0.52 | 0.46 → 0.56 | 6.79s | edge gone |  |
| 10-04 11:32:53 | XRP | up | 0.24→0.30 | 0.23 → 0.24 | 11.29s | UP @ 0.24 | -0.17 / -0.26 / · |
| 10-04 11:32:39 | BTC | down | 0.52→0.46 | 0.44 → 0.58 | 11.05s | edge gone |  |
| 10-04 11:32:38 | SOL | down | 0.48→0.43 | 0.50 → 0.58 | 11.30s | edge gone |  |
| 10-04 11:32:38 | XRP | down | 0.32→0.26 | 0.68 → 0.79 | 11.30s | edge gone |  |
| 10-04 11:32:38 | ETH | down | 0.65→0.47 | 0.43 → 0.61 | 11.30s | edge gone |  |
| 10-04 11:32:12 | DOGE | down | 0.38→0.25 | 0.61 → 0.75 | 7.55s | edge gone |  |
| 10-04 11:32:10 | SOL | down | 0.51→0.43 | 0.44 → 0.50 | 9.80s | DOWN @ 0.50 | -0.46 / 0.50 / · |
| 10-04 11:31:59 | XRP | up | 0.38→0.45 | 0.36 → 0.42 | 6.06s | edge gone |  |
| 10-04 11:31:49 | SOL | up | 0.43→0.48 | 0.50 → 0.49 | 15.81s | edge gone |  |
| 10-04 11:31:42 | XRP | up | 0.38→0.45 | 0.47 → 0.40 | no | UP @ 0.40 | -0.33 / -1.42 / · |
| 10-04 11:31:40 | NEAR | down | 0.39→0.33 | 0.50 → 0.57 | 9.31s | DOWN @ 0.57 | -0.66 / -0.36 / · |
| 10-04 11:31:38 | ZEC | down | 0.31→0.24 | 0.48 → 0.77 | 12.06s | edge gone |  |
| 10-04 11:31:03 | SOL | up | 0.48→0.57 | 0.54 → 0.58 | 0.30s | edge gone |  |
| 10-04 11:30:48 | SOL | down | 0.43→0.38 | 0.57 → 0.56 | no | DOWN @ 0.56 | -1.81 / -1.01 / · |
| 10-04 11:30:43 | XRP | up | 0.45→0.52 | 0.44 → 0.51 | 3.07s | edge gone |  |
| 10-04 11:28:39 | XRP | up | 0.86→0.91 | 0.97 → 0.94 | no | edge gone |  |
| 10-04 11:28:32 | ZEC | up | 0.41→0.52 | 0.96 → 0.66 | no | edge gone |  |
| 10-04 11:28:13 | ZEC | up | 0.76→0.84 | 0.92 → 0.97 | 10.11s | price out of range |  |
| 10-04 11:28:04 | XRP | down | 0.96→0.88 | 0.02 → 0.07 | 3.36s | DOWN @ 0.07 | -0.51 / -0.24 / -0.80 |
| 10-04 11:27:52 | ZEC | down | 0.73→0.62 | 0.39 → 0.30 | no | DOWN @ 0.30 | -2.39 / -2.02 / -3.19 |
| 10-04 11:27:29 | ZEC | down | 0.64→0.56 | 0.21 → 0.38 | 9.12s | edge gone |  |
