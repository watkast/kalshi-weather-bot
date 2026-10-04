# Lag Tracker

*Updated Sun Oct 04 11:14 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🟡 **Testing with real order-book fills.** 104 of 150 settled trades needed before calling it. The earlier results below used quoted prices, which may not have been fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$24.32** | -6.3% | 104 | $3.55 | $83.77 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 130 | 27 | -$50.21 | -10.9% | -$24.80 / -$25.41 |
| Sell after 30 sec | 130 | 36 | -$51.23 | -11.1% | -$30.93 / -$20.30 |
| Hold to the close | 104 | 36 | -$24.32 | -6.3% | -$9.38 / -$14.94 |
| Hold, only edge 10¢+ | 26 | 3 | -$33.83 | -53.0% | -$24.67 / -$9.16 |
| Hold, first trade per window only | 43 | 16 | -$9.36 | -5.5% | -$5.20 / -$4.16 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 531 | 10% | 67% | +5.0¢ | 0.3¢ | edge gone 372, price out of range 23, spread too wide 6 |

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
| BTC | 579 | 11.9s | 3% | 0% |
| DOGE | 758 | 10.5s | 2% | 0% |
| ETH | 750 | 10.9s | 4% | 0% |
| HYPE | 618 | 11.2s | 4% | 0% |
| NEAR | 761 | 10.8s | 4% | 0% |
| SOL | 1392 | 10.8s | 3% | 0% |
| XRP | 1399 | 11.0s | 4% | 0% |
| ZEC | 889 | 9.6s | 4% | 0% |
| **All** | **7798** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 11:13:41 | SOL | down | 0.49→0.39 | 0.41 → 0.24 | no | DOWN @ 0.24 | -1.22 / -1.92 / · |
| 10-04 11:13:41 | ETH | up | 0.34→0.40 | 0.34 → 0.20 | no | UP @ 0.20 | -0.33 / -2.00 / · |
| 10-04 11:13:24 | ETH | down | 0.51→0.37 | 0.61 → 0.74 | 21.79s | edge gone |  |
| 10-04 11:13:15 | SOL | up | 0.35→0.42 | 0.91 → 0.71 | no | edge gone |  |
| 10-04 11:13:06 | HYPE | up | 0.69→0.86 | 0.91 → 0.89 | no | edge gone |  |
| 10-04 11:12:54 | SOL | down | 0.73→0.55 | 0.10 → 0.26 | 21.54s | DOWN @ 0.26 | 0.31 / 0.99 / · |
| 10-04 11:12:53 | ETH | down | 0.74→0.64 | 0.30 → 0.55 | 23.04s | edge gone |  |
| 10-04 11:12:46 | HYPE | up | 0.53→0.79 | 0.35 → 0.91 | 0.28s | edge gone |  |
| 10-04 11:12:39 | SOL | down | 0.76→0.61 | 0.06 → 0.11 | no | DOWN @ 0.11 | -0.45 / 1.63 / · |
| 10-04 11:12:37 | ETH | down | 0.81→0.74 | 0.16 → 0.33 | 9.03s | edge gone |  |
| 10-04 11:12:33 | XRP | up | 0.08→0.13 | 0.09 → 0.09 | no | UP @ 0.09 | -0.39 / -0.76 / · |
| 10-04 11:12:22 | SOL | down | 0.74→0.65 | 0.07 → 0.07 | no | DOWN @ 0.07 | -0.29 / 0.11 / · |
| 10-04 11:11:54 | SOL | up | 0.59→0.68 | 0.89 → 0.90 | 22.04s | edge gone |  |
| 10-04 11:11:53 | XRP | up | 0.11→0.17 | 0.16 → 0.12 | no | UP @ 0.12 | -0.44 / -0.48 / · |
| 10-04 11:11:30 | XRP | up | 0.11→0.18 | 0.11 → 0.19 | 15.54s | edge gone |  |
| 10-04 11:11:20 | SOL | down | 0.70→0.62 | 0.11 → 0.11 | no | DOWN @ 0.11 | 0.24 / -0.28 / · |
| 10-04 11:11:05 | ZEC | up | 0.88→0.94 | 0.95 → 0.97 | 25.79s | price out of range |  |
| 10-04 11:11:04 | ETH | up | 0.70→0.77 | 0.53 → 0.64 | 11.78s | UP @ 0.64 | -0.03 / 0.90 / · |
| 10-04 11:11:02 | SOL | up | 0.61→0.69 | 0.89 → 0.90 | no | edge gone |  |
| 10-04 11:10:58 | DOGE | up | 0.64→0.74 | 0.78 → 0.82 | 18.29s | edge gone |  |
| 10-04 11:10:45 | SOL | down | 0.68→0.61 | 0.14 → 0.12 | no | DOWN @ 0.12 | -0.25 / -0.40 / · |
| 10-04 11:10:28 | ZEC | down | 0.83→0.76 | 0.12 → 0.11 | no | DOWN @ 0.11 | -0.70 / -0.71 / · |
| 10-04 11:10:28 | SOL | down | 0.67→0.60 | 0.21 → 0.14 | no | DOWN @ 0.14 | -0.46 / -0.46 / · |
| 10-04 11:10:10 | NEAR | up | 0.84→0.92 | 0.90 → 0.93 | 21.29s | edge gone |  |
| 10-04 11:09:42 | SOL | down | 0.66→0.60 | 0.20 → 0.29 | 4.03s | DOWN @ 0.29 | -1.02 / -1.66 / · |
| 10-04 11:09:41 | ZEC | down | 0.71→0.66 | 0.18 → 0.23 | no | DOWN @ 0.23 | -1.21 / -1.57 / · |
| 10-04 11:09:40 | NEAR | up | 0.65→0.74 | 0.87 → 0.84 | no | edge gone |  |
| 10-04 11:09:13 | NEAR | down | 0.71→0.65 | 0.27 → 0.22 | no | DOWN @ 0.22 | -0.83 / -0.83 / · |
| 10-04 11:09:01 | SOL | up | 0.46→0.53 | 0.67 → 0.71 | 14.31s | edge gone |  |
| 10-04 11:08:40 | SOL | down | 0.56→0.50 | 0.36 → 0.36 | no | DOWN @ 0.36 | -0.67 / -1.74 / · |
