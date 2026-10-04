# Lag Tracker

*Updated Sun Oct 04 19:47 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$304.04** | -8.1% | 957 | $3.93 | $185.87 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 958 | 152 | -$420.63 | -11.2% | -$195.33 / -$225.30 |
| Sell after 30 sec | 957 | 245 | -$446.66 | -11.9% | -$225.16 / -$221.50 |
| Hold to the close | 957 | 346 | -$304.04 | -8.1% | -$354.57 / $50.53 |
| Hold, only edge 10¢+ | 341 | 88 | -$187.04 | -17.5% | -$103.70 / -$83.34 |
| Hold, first trade per window only | 294 | 118 | -$52.90 | -4.3% | -$82.17 / $29.27 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 3505 | 10% | 66% | +4.0¢ | 0.3¢ | edge gone 2376, price out of range 95, spread too wide 76 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 747 | 11.1s | 3% | 0% |
| BTC | 918 | 11.9s | 3% | 0% |
| DOGE | 994 | 10.7s | 3% | 0% |
| ETH | 1120 | 10.8s | 4% | 0% |
| HYPE | 749 | 11.6s | 3% | 0% |
| NEAR | 1080 | 10.8s | 4% | 0% |
| SOL | 1963 | 10.9s | 3% | 0% |
| XRP | 2019 | 11.0s | 3% | 0% |
| ZEC | 1182 | 9.7s | 4% | 0% |
| **All** | **10772** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **7 ms** · Order book check: **27 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 19:46:53 | ZEC | up | 0.52→0.60 | 0.55 → 0.62 | no | edge gone |  |
| 10-04 19:46:53 | XRP | up | 0.42→0.48 | 0.46 → 0.54 | no | edge gone |  |
| 10-04 19:46:52 | ETH | up | 0.56→0.62 | 0.57 → 0.66 | no | edge gone |  |
| 10-04 19:46:51 | BTC | up | 0.48→0.55 | 0.50 → 0.57 | no | edge gone |  |
| 10-04 19:46:42 | SOL | down | 0.45→0.40 | 0.53 → 0.53 | no | DOWN @ 0.53 | -1.36 / · / · |
| 10-04 19:46:38 | XRP | down | 0.48→0.42 | 0.48 → 0.54 | 8.50s | edge gone |  |
| 10-04 19:46:17 | SOL | up | 0.37→0.43 | 0.48 → 0.47 | no | edge gone |  |
| 10-04 19:46:02 | SOL | up | 0.40→0.51 | 0.50 → 0.47 | no | edge gone |  |
| 10-04 19:45:53 | BNB | up | 0.28→0.39 | 0.58 → 0.59 | no | edge gone |  |
| 10-04 19:42:55 | NEAR | up | 0.08→0.21 | 0.19 → 0.26 | no | spread too wide |  |
| 10-04 19:42:34 | DOGE | down | 0.15→0.09 | 0.81 → 0.95 | 0.02s | edge gone |  |
| 10-04 19:42:10 | DOGE | up | 0.17→0.23 | 0.19 → 0.20 | no | edge gone |  |
| 10-04 19:41:55 | ETH | down | 0.14→0.07 | 0.92 → 0.97 | 8.53s | price out of range |  |
| 10-04 19:41:55 | DOGE | down | 0.34→0.24 | 0.63 → 0.81 | 9.03s | edge gone |  |
| 10-04 19:41:53 | ZEC | down | 0.15→0.07 | 0.70 → 0.91 | 10.78s | edge gone |  |
| 10-04 19:41:53 | SOL | down | 0.32→0.26 | 0.60 → 0.79 | 11.03s | edge gone |  |
| 10-04 19:41:51 | HYPE | down | 0.43→0.34 | 0.54 → 0.61 | 13.03s | DOWN @ 0.61 | 2.40 / 3.14 / 3.73 |
| 10-04 19:41:50 | BTC | down | 0.24→0.17 | 0.70 → 0.83 | 0.27s | edge gone |  |
| 10-04 19:41:39 | NEAR | down | 0.43→0.27 | 0.44 → 0.54 | 9.53s | DOWN @ 0.61 | -1.14 / 0.52 / -6.28 |
| 10-04 19:41:38 | ZEC | down | 0.54→0.32 | 0.60 → 0.70 | 10.79s | edge gone |  |
| 10-04 19:41:38 | DOGE | down | 0.71→0.56 | 0.51 → 0.47 | 10.79s | edge gone |  |
| 10-04 19:41:34 | XRP | up | 0.03→0.10 | 0.07 → 0.11 | no | edge gone |  |
| 10-04 19:41:34 | ETH | up | 0.18→0.37 | 0.08 → 0.20 | no | UP @ 0.20 | -1.22 / -1.68 / -2.12 |
| 10-04 19:41:34 | BTC | up | 0.41→0.51 | 0.25 → 0.51 | 0.03s | edge gone |  |
| 10-04 19:41:30 | SOL | down | 0.49→0.44 | 0.53 → 0.48 | 19.29s | DOWN @ 0.48 | -0.21 / 3.01 / 5.02 |
| 10-04 19:41:23 | DOGE | down | 0.53→0.45 | 0.62 → 0.51 | no | edge gone |  |
| 10-04 19:41:22 | ZEC | down | 0.52→0.41 | 0.45 → 0.60 | 12.04s | edge gone |  |
| 10-04 19:41:22 | HYPE | down | 0.44→0.36 | 0.59 → 0.68 | 12.04s | spread too wide |  |
| 10-04 19:41:19 | NEAR | up | 0.40→0.48 | 0.54 → 0.59 | no | edge gone |  |
| 10-04 19:41:18 | BTC | up | 0.33→0.51 | 0.34 → 0.51 | 16.29s | edge gone |  |
