# Lag Tracker

*Updated Sun Oct 04 16:05 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$332.96** | -16.8% | 535 | $3.72 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 544 | 91 | -$227.34 | -11.2% | -$117.65 / -$109.69 |
| Sell after 30 sec | 543 | 134 | -$250.21 | -12.4% | -$137.05 / -$113.16 |
| Hold to the close | 535 | 165 | -$332.96 | -16.8% | -$279.09 / -$53.87 |
| Hold, only edge 10¢+ | 188 | 46 | -$76.90 | -14.3% | -$114.17 / $37.27 |
| Hold, first trade per window only | 182 | 66 | -$87.59 | -11.7% | -$57.21 / -$30.38 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 2126 | 10% | 67% | +4.9¢ | 0.3¢ | edge gone 1471, price out of range 58, spread too wide 53 |

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
| BTC | 789 | 11.8s | 3% | 0% |
| DOGE | 865 | 10.7s | 3% | 0% |
| ETH | 932 | 10.9s | 4% | 0% |
| HYPE | 696 | 11.6s | 3% | 0% |
| NEAR | 910 | 10.8s | 3% | 0% |
| SOL | 1724 | 10.9s | 3% | 0% |
| XRP | 1740 | 11.2s | 3% | 0% |
| ZEC | 1047 | 9.6s | 4% | 0% |
| **All** | **9393** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **19 ms** · Order book check: **25 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 16:05:28 | NEAR | down | 0.43→0.36 | 0.50 → 0.50 | no | DOWN @ 0.50 | -0.46 / · / · |
| 10-04 16:04:46 | NEAR | up | 0.36→0.42 | 0.42 → 0.48 | 26.72s | edge gone |  |
| 10-04 16:04:25 | NEAR | up | 0.27→0.33 | 0.39 → 0.42 | 18.22s | edge gone |  |
| 10-04 16:04:13 | SOL | down | 0.21→0.16 | 0.81 → 0.85 | 14.48s | edge gone |  |
| 10-04 16:03:56 | NEAR | down | 0.27→0.21 | 0.65 → 0.68 | no | DOWN @ 0.68 | -1.02 / -1.34 / · |
| 10-04 16:03:49 | DOGE | down | 0.61→0.54 | 0.37 → 0.41 | 23.74s | DOWN @ 0.41 | -0.74 / -0.74 / · |
| 10-04 16:03:40 | BTC | up | 0.13→0.22 | 0.15 → 0.19 | no | edge gone |  |
| 10-04 16:03:34 | SOL | down | 0.29→0.22 | 0.80 → 0.82 | no | edge gone |  |
| 10-04 16:03:31 | DOGE | down | 0.68→0.58 | 0.30 → 0.31 | 11.24s | DOWN @ 0.31 | 0.28 / 0.00 / · |
| 10-04 16:03:23 | NEAR | up | 0.27→0.32 | 0.38 → 0.42 | no | edge gone |  |
| 10-04 16:03:15 | BTC | down | 0.23→0.17 | 0.85 → 0.87 | 0.47s | edge gone |  |
| 10-04 16:03:14 | DOGE | up | 0.52→0.73 | 0.61 → 0.73 | 0.47s | edge gone |  |
| 10-04 16:03:12 | SOL | down | 0.42→0.35 | 0.63 → 0.75 | 0.99s | edge gone |  |
| 10-04 16:03:05 | ZEC | down | 0.21→0.15 | 0.83 → 0.92 | 7.74s | edge gone |  |
| 10-04 16:03:00 | XRP | up | 0.15→0.20 | 0.16 → 0.16 | no | edge gone |  |
| 10-04 16:02:55 | SOL | down | 0.46→0.40 | 0.60 → 0.64 | 17.75s | edge gone |  |
| 10-04 16:02:52 | BTC | down | 0.30→0.24 | 0.75 → 0.78 | 20.50s | edge gone |  |
| 10-04 16:02:51 | DOGE | up | 0.32→0.43 | 0.20 → 0.40 | 6.75s | edge gone |  |
| 10-04 16:02:50 | HYPE | down | 0.40→0.31 | 0.64 → 0.70 | 7.25s | edge gone |  |
| 10-04 16:02:49 | NEAR | down | 0.41→0.29 | 0.49 → 0.62 | 8.75s | DOWN @ 0.64 | -0.51 / -0.41 / · |
| 10-04 16:02:33 | SOL | up | 0.46→0.55 | 0.42 → 0.41 | no | UP @ 0.41 | -0.84 / -0.84 / · |
| 10-04 16:02:26 | HYPE | down | 0.47→0.38 | 0.43 → 0.61 | 1.25s | edge gone |  |
| 10-04 16:02:19 | ZEC | down | 0.37→0.32 | 0.57 → 0.79 | 9.00s | edge gone |  |
| 10-04 16:02:17 | SOL | down | 0.55→0.46 | 0.47 → 0.52 | 10.76s | edge gone |  |
| 10-04 16:02:14 | XRP | up | 0.27→0.33 | 0.23 → 0.24 | no | UP @ 0.24 | -0.65 / -1.12 / · |
| 10-04 16:02:14 | NEAR | up | 0.53→0.58 | 0.63 → 0.62 | no | spread too wide |  |
| 10-04 16:01:59 | NEAR | down | 0.62→0.55 | 0.36 → 0.34 | 13.51s | DOWN @ 0.34 | -0.04 / 0.55 / · |
| 10-04 16:01:50 | XRP | down | 0.46→0.40 | 0.48 → 0.67 | 7.26s | edge gone |  |
| 10-04 16:01:44 | NEAR | up | 0.58→0.65 | 0.68 → 0.68 | no | edge gone |  |
| 10-04 16:01:38 | ETH | down | 0.46→0.41 | 0.54 → 0.62 | 4.27s | edge gone |  |
