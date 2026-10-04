# Lag Tracker

*Updated Sun Oct 04 17:36 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$304.20** | -11.9% | 689 | $3.73 | $143.33 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 693 | 116 | -$288.48 | -11.2% | -$144.12 / -$144.36 |
| Sell after 30 sec | 693 | 183 | -$303.89 | -11.8% | -$167.09 / -$136.80 |
| Hold to the close | 689 | 226 | -$304.20 | -11.9% | -$389.63 / $85.43 |
| Hold, only edge 10¢+ | 246 | 58 | -$121.48 | -17.3% | -$159.97 / $38.49 |
| Hold, first trade per window only | 225 | 84 | -$71.22 | -7.8% | -$91.10 / $19.88 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 2643 | 9% | 67% | +5.0¢ | 0.3¢ | edge gone 1817, price out of range 71, spread too wide 61 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 714 | 11.2s | 3% | 0% |
| BTC | 834 | 11.9s | 3% | 0% |
| DOGE | 917 | 10.6s | 3% | 0% |
| ETH | 1014 | 10.8s | 4% | 0% |
| HYPE | 716 | 11.6s | 3% | 0% |
| NEAR | 975 | 10.8s | 3% | 0% |
| SOL | 1812 | 10.8s | 3% | 0% |
| XRP | 1843 | 11.2s | 3% | 0% |
| ZEC | 1085 | 9.7s | 4% | 0% |
| **All** | **9910** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **7 ms** · Order book check: **26 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 17:36:07 | ZEC | up | 0.54→0.62 | 0.72 → 0.79 | no | edge gone |  |
| 10-04 17:36:02 | XRP | down | 0.50→0.42 | 0.40 → 0.49 | no | DOWN @ 0.49 | · / · / · |
| 10-04 17:35:51 | BNB | up | 0.20→0.26 | 0.52 → 0.45 | no | edge gone |  |
| 10-04 17:35:32 | SOL | down | 0.19→0.14 | 0.86 → 0.86 | no | edge gone |  |
| 10-04 17:35:31 | DOGE | up | 0.38→0.59 | 0.35 → 0.62 | 10.69s | edge gone |  |
| 10-04 17:35:26 | BNB | down | 0.34→0.26 | 0.58 → 0.47 | no | DOWN @ 0.48 | -0.35 / 0.35 / · |
| 10-04 17:34:58 | ZEC | up | 0.53→0.59 | 0.60 → 0.75 | 13.45s | edge gone |  |
| 10-04 17:34:41 | XRP | up | 0.38→0.48 | 0.39 → 0.51 | 0.96s | edge gone |  |
| 10-04 17:34:33 | SOL | up | 0.17→0.23 | 0.24 → 0.21 | no | edge gone |  |
| 10-04 17:34:09 | BTC | down | 0.54→0.47 | 0.53 → 0.57 | 17.46s | edge gone |  |
| 10-04 17:34:07 | NEAR | down | 0.54→0.48 | 0.39 → 0.44 | 19.46s | DOWN @ 0.47 | -0.84 / -0.84 / · |
| 10-04 17:34:07 | XRP | down | 0.45→0.39 | 0.55 → 0.58 | 4.96s | edge gone |  |
| 10-04 17:33:55 | ETH | down | 0.54→0.41 | 0.50 → 0.66 | 16.72s | edge gone |  |
| 10-04 17:33:54 | BTC | down | 0.67→0.54 | 0.33 → 0.53 | 2.46s | edge gone |  |
| 10-04 17:33:48 | BNB | up | 0.27→0.34 | 0.54 → 0.57 | no | edge gone |  |
| 10-04 17:33:31 | DOGE | down | 0.47→0.41 | 0.52 → 0.60 | 11.22s | edge gone |  |
| 10-04 17:33:27 | BNB | up | 0.28→0.35 | 0.53 → 0.54 | 29.73s | edge gone |  |
| 10-04 17:33:18 | BTC | up | 0.66→0.72 | 0.66 → 0.68 | no | edge gone |  |
| 10-04 17:33:10 | SOL | down | 0.39→0.32 | 0.62 → 0.60 | no | DOWN @ 0.60 | -0.55 / 0.17 / · |
| 10-04 17:32:56 | NEAR | up | 0.41→0.57 | 0.41 → 0.60 | 15.23s | edge gone |  |
| 10-04 17:31:25 | SOL | down | 0.37→0.31 | 0.61 → 0.68 | 0.48s | edge gone |  |
| 10-04 17:31:13 | XRP | up | 0.40→0.46 | 0.52 → 0.50 | no | edge gone |  |
| 10-04 17:30:44 | HYPE | down | 0.59→0.54 | 0.33 → 0.35 | 10.76s | DOWN @ 0.37 | 0.55 / -0.04 / · |
| 10-04 17:28:36 | NEAR | down | 0.88→0.80 | 0.02 → 0.01 | no | price out of range |  |
| 10-04 17:28:21 | NEAR | up | 0.73→0.81 | 0.96 → 0.99 | no | price out of range |  |
| 10-04 17:28:05 | ETH | down | 0.98→0.91 | 0.01 → 0.05 | 8.78s | price out of range |  |
| 10-04 17:27:48 | NEAR | down | 0.78→0.72 | 0.05 → 0.07 | no | DOWN @ 0.07 | -0.19 / -0.62 / -0.75 |
| 10-04 17:27:28 | DOGE | up | 0.49→0.59 | 0.69 → 0.87 | 15.54s | edge gone |  |
| 10-04 17:27:20 | NEAR | down | 0.86→0.72 | 0.07 → 0.05 | no | DOWN @ 0.06 | -0.30 / -0.14 / -0.69 |
| 10-04 17:27:08 | BNB | down | 0.66→0.47 | 0.07 → 0.04 | no | price out of range |  |
