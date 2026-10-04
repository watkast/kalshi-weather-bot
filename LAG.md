# Lag Tracker

*Updated Sun Oct 04 12:25 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$204.92** | -25.8% | 224 | $3.61 | $122.22 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 238 | 41 | -$103.41 | -12.0% | -$46.66 / -$56.75 |
| Sell after 30 sec | 238 | 53 | -$114.10 | -13.3% | -$48.31 / -$65.79 |
| Hold to the close | 224 | 59 | -$204.92 | -25.8% | -$34.74 / -$170.18 |
| Hold, only edge 10¢+ | 79 | 12 | -$94.93 | -44.2% | -$53.86 / -$41.07 |
| Hold, first trade per window only | 80 | 28 | -$32.55 | -10.4% | -$6.31 / -$26.24 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 877 | 11% | 65% | +5.0¢ | 0.3¢ | edge gone 596, price out of range 29, spread too wide 14 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 662 | 11.1s | 3% | 0% |
| BTC | 622 | 11.9s | 3% | 0% |
| DOGE | 777 | 10.6s | 2% | 0% |
| ETH | 786 | 11.1s | 4% | 0% |
| HYPE | 640 | 11.2s | 4% | 0% |
| NEAR | 799 | 10.8s | 4% | 0% |
| SOL | 1470 | 10.8s | 3% | 0% |
| XRP | 1459 | 11.0s | 4% | 0% |
| ZEC | 929 | 9.7s | 4% | 0% |
| **All** | **8144** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 12:24:51 | HYPE | up | 0.74→0.82 | 0.80 → 0.87 | no | edge gone |  |
| 10-04 12:24:50 | BTC | up | 0.76→0.82 | 0.77 → 0.85 | no | edge gone |  |
| 10-04 12:24:49 | SOL | up | 0.43→0.51 | 0.54 → 0.58 | no | edge gone |  |
| 10-04 12:24:27 | XRP | up | 0.84→0.91 | 0.92 → 0.87 | no | edge gone |  |
| 10-04 12:24:26 | ETH | down | 0.99→0.94 | 0.05 → 0.18 | 11.44s | edge gone |  |
| 10-04 12:24:26 | ZEC | down | 0.22→0.10 | 0.81 → 0.91 | 11.44s | edge gone |  |
| 10-04 12:24:26 | BTC | down | 0.80→0.71 | 0.18 → 0.41 | 11.69s | edge gone |  |
| 10-04 12:24:26 | SOL | down | 0.55→0.39 | 0.41 → 0.61 | no | edge gone |  |
| 10-04 12:24:05 | SOL | up | 0.43→0.51 | 0.56 → 0.63 | 17.50s | edge gone |  |
| 10-04 12:24:03 | BTC | up | 0.69→0.76 | 0.74 → 0.78 | 20.00s | edge gone |  |
| 10-04 12:23:48 | BTC | down | 0.76→0.69 | 0.29 → 0.31 | no | edge gone |  |
| 10-04 12:23:32 | XRP | up | 0.87→0.94 | 0.93 → 0.90 | no | edge gone |  |
| 10-04 12:23:29 | SOL | down | 0.51→0.44 | 0.43 → 0.56 | 6.76s | edge gone |  |
| 10-04 12:23:27 | HYPE | down | 0.95→0.82 | 0.08 → 0.10 | no | DOWN @ 0.11 | -0.35 / -0.29 / · |
| 10-04 12:23:23 | BTC | down | 0.85→0.77 | 0.14 → 0.30 | 13.26s | edge gone |  |
| 10-04 12:23:22 | DOGE | down | 0.55→0.49 | 0.34 → 0.46 | 13.51s | edge gone |  |
| 10-04 12:23:22 | NEAR | down | 0.82→0.77 | 0.08 → 0.08 | no | DOWN @ 0.08 | 0.04 / 0.09 / · |
| 10-04 12:23:14 | SOL | down | 0.58→0.47 | 0.44 → 0.42 | no | DOWN @ 0.42 | 0.14 / -0.16 / · |
| 10-04 12:23:13 | XRP | down | 0.94→0.88 | 0.08 → 0.13 | no | edge gone |  |
| 10-04 12:23:11 | ZEC | up | 0.26→0.31 | 0.23 → 0.28 | 10.01s | edge gone |  |
| 10-04 12:22:58 | BTC | up | 0.81→0.86 | 0.81 → 0.86 | 7.52s | edge gone |  |
| 10-04 12:22:56 | SOL | up | 0.44→0.51 | 0.56 → 0.58 | no | edge gone |  |
| 10-04 12:22:56 | ZEC | up | 0.23→0.29 | 0.18 → 0.19 | 10.02s | UP @ 0.21 | 0.31 / -0.60 / · |
| 10-04 12:22:29 | BTC | down | 0.86→0.81 | 0.14 → 0.22 | 6.52s | edge gone |  |
| 10-04 12:22:21 | SOL | down | 0.64→0.57 | 0.43 → 0.43 | no | edge gone |  |
| 10-04 12:22:08 | BTC | up | 0.73→0.82 | 0.77 → 0.81 | 0.26s | edge gone |  |
| 10-04 12:22:07 | NEAR | up | 0.54→0.60 | 0.76 → 0.80 | 14.03s | edge gone |  |
| 10-04 12:21:53 | BTC | up | 0.65→0.73 | 0.58 → 0.73 | 12.78s | edge gone |  |
| 10-04 12:21:48 | XRP | up | 0.82→0.87 | 0.86 → 0.89 | 17.29s | edge gone |  |
| 10-04 12:21:35 | SOL | down | 0.54→0.44 | 0.40 → 0.50 | 0.28s | DOWN @ 0.50 | -0.66 / -1.25 / · |
