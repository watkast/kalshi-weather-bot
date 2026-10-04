# Lag Tracker

*Updated Sun Oct 04 11:24 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🟡 **Testing with real order-book fills.** 130 of 150 settled trades needed before calling it. The earlier results below used quoted prices, which may not have been fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$81.18** | -17.6% | 130 | $3.56 | $83.77 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 144 | 28 | -$58.06 | -11.3% | -$26.28 / -$31.78 |
| Sell after 30 sec | 144 | 36 | -$61.94 | -12.1% | -$29.74 / -$32.20 |
| Hold to the close | 130 | 38 | -$81.18 | -17.6% | -$11.95 / -$69.23 |
| Hold, only edge 10¢+ | 40 | 4 | -$56.39 | -58.5% | -$28.85 / -$27.54 |
| Hold, first trade per window only | 50 | 18 | -$13.81 | -7.1% | -$8.49 / -$5.32 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 581 | 10% | 66% | +5.0¢ | 0.3¢ | edge gone 408, price out of range 23, spread too wide 6 |

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
| BTC | 582 | 11.9s | 3% | 0% |
| DOGE | 761 | 10.6s | 2% | 0% |
| ETH | 754 | 10.9s | 4% | 0% |
| HYPE | 619 | 11.2s | 4% | 0% |
| NEAR | 769 | 10.8s | 4% | 0% |
| SOL | 1401 | 10.8s | 3% | 0% |
| XRP | 1414 | 11.0s | 4% | 0% |
| ZEC | 896 | 9.6s | 4% | 0% |
| **All** | **7848** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 11:24:35 | XRP | up | 0.72→0.81 | 0.86 → 0.80 | no | edge gone |  |
| 10-04 11:24:20 | XRP | down | 0.75→0.69 | 0.16 → 0.26 | 17.29s | edge gone |  |
| 10-04 11:24:05 | XRP | up | 0.75→0.80 | 0.75 → 0.87 | 5.29s | edge gone |  |
| 10-04 11:23:45 | SOL | down | 0.77→0.71 | 0.09 → 0.10 | no | DOWN @ 0.10 | -0.25 / -0.34 / · |
| 10-04 11:23:23 | HYPE | down | 0.29→0.24 | 0.53 → 0.84 | 3.05s | edge gone |  |
| 10-04 11:23:23 | SOL | down | 0.73→0.67 | 0.13 → 0.15 | no | DOWN @ 0.15 | -0.41 / -0.75 / · |
| 10-04 11:23:01 | ZEC | up | 0.65→0.73 | 0.78 → 0.85 | 9.81s | edge gone |  |
| 10-04 11:23:00 | SOL | down | 0.78→0.66 | 0.14 → 0.15 | no | DOWN @ 0.15 | -0.62 / -0.43 / · |
| 10-04 11:22:50 | XRP | up | 0.60→0.66 | 0.66 → 0.68 | 20.32s | edge gone |  |
| 10-04 11:22:46 | ZEC | down | 0.75→0.61 | 0.31 → 0.39 | no | edge gone |  |
| 10-04 11:22:32 | XRP | down | 0.65→0.60 | 0.34 → 0.36 | no | edge gone |  |
| 10-04 11:22:24 | ETH | down | 0.87→0.81 | 0.11 → 0.18 | 1.82s | edge gone |  |
| 10-04 11:22:15 | NEAR | up | 0.31→0.38 | 0.44 → 0.42 | no | edge gone |  |
| 10-04 11:22:15 | XRP | up | 0.65→0.70 | 0.65 → 0.67 | no | edge gone |  |
| 10-04 11:21:56 | DOGE | up | 0.54→0.61 | 0.65 → 0.66 | no | edge gone |  |
| 10-04 11:21:56 | SOL | down | 0.71→0.65 | 0.17 → 0.17 | no | DOWN @ 0.17 | -0.58 / -0.20 / · |
| 10-04 11:21:42 | XRP | down | 0.63→0.54 | 0.33 → 0.37 | no | DOWN @ 0.37 | -0.45 / -0.83 / · |
| 10-04 11:21:41 | ZEC | up | 0.51→0.59 | 0.60 → 0.61 | no | edge gone |  |
| 10-04 11:21:27 | XRP | down | 0.78→0.69 | 0.13 → 0.33 | 13.84s | edge gone |  |
| 10-04 11:21:24 | BTC | down | 0.74→0.68 | 0.18 → 0.24 | 16.84s | DOWN @ 0.24 | 0.22 / -0.17 / · |
| 10-04 11:21:06 | NEAR | up | 0.43→0.51 | 0.40 → 0.61 | 4.09s | edge gone |  |
| 10-04 11:21:05 | BTC | up | 0.68→0.74 | 0.76 → 0.83 | 5.84s | edge gone |  |
| 10-04 11:21:04 | ZEC | up | 0.49→0.55 | 0.48 → 0.60 | 6.09s | edge gone |  |
| 10-04 11:20:41 | DOGE | up | 0.50→0.60 | 0.45 → 0.57 | 14.35s | edge gone |  |
| 10-04 11:20:39 | XRP | up | 0.53→0.58 | 0.40 → 0.69 | 1.35s | edge gone |  |
| 10-04 11:20:38 | ETH | up | 0.70→0.78 | 0.78 → 0.85 | 17.60s | edge gone |  |
| 10-04 11:20:28 | NEAR | up | 0.23→0.30 | 0.25 → 0.34 | 0.34s | edge gone |  |
| 10-04 11:20:24 | XRP | up | 0.47→0.53 | 0.37 → 0.52 | 16.36s | edge gone |  |
| 10-04 11:20:21 | SOL | up | 0.52→0.58 | 0.63 → 0.70 | 4.36s | edge gone |  |
| 10-04 11:20:00 | SOL | down | 0.49→0.44 | 0.36 → 0.39 | no | DOWN @ 0.39 | -0.54 / -1.90 / · |
