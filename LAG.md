# Lag Tracker

*Updated Sun Oct 04 09:54 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🟡 **Testing with real order-book fills.** 17 of 150 settled trades needed before calling it. The earlier results below used quoted prices, which may not have been fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$2.11** | -3.4% | 17 | $4.21 | $60.01 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 29 | 9 | -$6.80 | -5.6% | -$5.60 / -$1.20 |
| Sell after 30 sec | 29 | 7 | -$11.78 | -9.6% | -$9.43 / -$2.35 |
| Hold to the close | 17 | 6 | -$2.11 | -3.4% | -$16.86 / $14.75 |
| Hold, only edge 10¢+ | 5 | 1 | -$2.26 | -18.4% | -$2.07 / -$0.19 |
| Hold, first trade per window only | 10 | 3 | -$10.01 | -25.0% | -$5.98 / -$4.03 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 162 | 7% | 71% | +5.0¢ | 0.2¢ | edge gone 127, price out of range 4, spread too wide 2 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 646 | 11.1s | 3% | 0% |
| BTC | 542 | 12.0s | 3% | 0% |
| DOGE | 729 | 10.5s | 2% | 0% |
| ETH | 711 | 11.2s | 4% | 0% |
| HYPE | 599 | 11.3s | 4% | 0% |
| NEAR | 711 | 10.7s | 4% | 0% |
| SOL | 1305 | 11.0s | 3% | 0% |
| XRP | 1315 | 10.9s | 4% | 0% |
| ZEC | 871 | 9.6s | 4% | 0% |
| **All** | **7429** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 09:54:04 | NEAR | up | 0.54→0.59 | 0.72 → 0.80 | 4.03s | spread too wide |  |
| 10-04 09:53:13 | SOL | up | 0.80→0.86 | 0.76 → 0.82 | 10.09s | UP @ 0.82 | 0.41 / 0.20 / · |
| 10-04 09:53:03 | ETH | down | 0.35→0.29 | 0.71 → 0.72 | no | edge gone |  |
| 10-04 09:52:48 | DOGE | down | 0.28→0.23 | 0.84 → 0.82 | no | edge gone |  |
| 10-04 09:52:40 | ETH | down | 0.42→0.36 | 0.71 → 0.71 | no | edge gone |  |
| 10-04 09:52:28 | NEAR | up | 0.55→0.63 | 0.58 → 0.70 | 10.03s | edge gone |  |
| 10-04 09:52:24 | SOL | down | 0.83→0.76 | 0.26 → 0.33 | no | edge gone |  |
| 10-04 09:52:19 | BTC | up | 0.22→0.31 | 0.17 → 0.28 | 19.29s | edge gone |  |
| 10-04 09:52:16 | ETH | up | 0.30→0.36 | 0.32 → 0.37 | no | edge gone |  |
| 10-04 09:52:16 | XRP | up | 0.23→0.28 | 0.20 → 0.24 | no | UP @ 0.24 | -0.74 / -0.65 / · |
| 10-04 09:52:09 | SOL | up | 0.68→0.76 | 0.67 → 0.74 | 14.03s | edge gone |  |
| 10-04 09:52:01 | BTC | down | 0.25→0.20 | 0.77 → 0.83 | 6.53s | edge gone |  |
| 10-04 09:52:00 | DOGE | up | 0.23→0.29 | 0.21 → 0.16 | no | UP @ 0.16 | -0.10 / -0.29 / · |
| 10-04 09:51:55 | ETH | down | 0.38→0.27 | 0.61 → 0.66 | 12.53s | DOWN @ 0.67 | -0.31 / -0.00 / · |
| 10-04 09:51:50 | NEAR | down | 0.63→0.56 | 0.30 → 0.27 | 18.29s | DOWN @ 0.28 | 0.09 / 0.58 / · |
| 10-04 09:51:36 | SOL | up | 0.59→0.65 | 0.62 → 0.63 | 17.29s | edge gone |  |
| 10-04 09:51:35 | NEAR | up | 0.57→0.62 | 0.68 → 0.75 | 3.28s | edge gone |  |
| 10-04 09:51:12 | ETH | down | 0.56→0.46 | 0.50 → 0.63 | 10.53s | edge gone |  |
| 10-04 09:51:03 | SOL | up | 0.61→0.72 | 0.61 → 0.67 | 5.03s | UP @ 0.67 | -1.27 / -0.93 / · |
| 10-04 09:51:00 | BTC | up | 0.31→0.38 | 0.38 → 0.37 | no | edge gone |  |
| 10-04 09:50:58 | NEAR | up | 0.27→0.33 | 0.33 → 0.44 | 9.53s | edge gone |  |
| 10-04 09:50:23 | NEAR | up | 0.15→0.23 | 0.28 → 0.34 | no | edge gone |  |
| 10-04 09:50:16 | ZEC | up | 0.74→0.79 | 0.81 → 0.81 | 6.53s | edge gone |  |
| 10-04 09:50:15 | SOL | down | 0.59→0.53 | 0.41 → 0.46 | 8.28s | edge gone |  |
| 10-04 09:50:10 | DOGE | down | 0.37→0.31 | 0.63 → 0.69 | 13.04s | edge gone |  |
| 10-04 09:50:10 | ETH | down | 0.75→0.60 | 0.40 → 0.52 | 0.26s | edge gone |  |
| 10-04 09:50:09 | BTC | down | 0.52→0.45 | 0.51 → 0.59 | 0.26s | edge gone |  |
| 10-04 09:49:55 | XRP | up | 0.36→0.41 | 0.76 → 0.40 | no | edge gone |  |
| 10-04 09:49:49 | SOL | down | 0.93→0.78 | 0.15 → 0.41 | 18.54s | edge gone |  |
| 10-04 09:49:49 | DOGE | down | 0.69→0.52 | 0.16 → 0.51 | 18.54s | edge gone |  |
