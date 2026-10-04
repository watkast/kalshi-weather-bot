# Lag Tracker

*Updated Sun Oct 04 10:24 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🟡 **Testing with real order-book fills.** 58 of 150 settled trades needed before calling it. The earlier results below used quoted prices, which may not have been fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$9.00** | -4.1% | 58 | $3.97 | $83.77 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 69 | 16 | -$26.11 | -9.5% | -$12.38 / -$13.73 |
| Sell after 30 sec | 69 | 19 | -$29.49 | -10.8% | -$20.62 / -$8.87 |
| Hold to the close | 58 | 21 | -$9.00 | -4.1% | $7.88 / -$16.88 |
| Hold, only edge 10¢+ | 15 | 1 | -$25.89 | -72.1% | -$6.91 / -$18.98 |
| Hold, first trade per window only | 24 | 10 | -$4.01 | -3.9% | -$10.62 / $6.61 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 301 | 8% | 71% | +6.0¢ | 0.2¢ | edge gone 218, price out of range 10, spread too wide 4 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 647 | 11.1s | 3% | 0% |
| BTC | 561 | 11.9s | 3% | 0% |
| DOGE | 743 | 10.5s | 2% | 0% |
| ETH | 724 | 11.2s | 4% | 0% |
| HYPE | 602 | 11.3s | 4% | 0% |
| NEAR | 729 | 10.8s | 4% | 0% |
| SOL | 1337 | 11.0s | 3% | 0% |
| XRP | 1345 | 11.0s | 4% | 0% |
| ZEC | 880 | 9.6s | 4% | 0% |
| **All** | **7568** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **34 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 10:24:08 | XRP | up | 0.43→0.50 | 0.51 → 0.47 | no | edge gone |  |
| 10-04 10:23:50 | SOL | down | 0.61→0.52 | 0.38 → 0.39 | 22.85s | DOWN @ 0.39 | 0.40 / 0.45 / · |
| 10-04 10:23:35 | SOL | down | 0.66→0.55 | 0.24 → 0.39 | 7.83s | DOWN @ 0.39 | -1.42 / 0.95 / · |
| 10-04 10:23:35 | XRP | down | 0.61→0.52 | 0.44 → 0.52 | 23.08s | edge gone |  |
| 10-04 10:23:20 | SOL | up | 0.58→0.68 | 0.70 → 0.77 | 7.83s | edge gone |  |
| 10-04 10:23:17 | XRP | up | 0.52→0.59 | 0.51 → 0.58 | 11.08s | edge gone |  |
| 10-04 10:23:05 | SOL | down | 0.63→0.57 | 0.28 → 0.39 | 7.84s | edge gone |  |
| 10-04 10:23:05 | NEAR | down | 0.11→0.06 | 0.86 → 0.90 | 8.34s | DOWN @ 0.90 | 0.07 / 0.20 / · |
| 10-04 10:22:53 | XRP | down | 0.70→0.65 | 0.34 → 0.36 | 20.34s | edge gone |  |
| 10-04 10:22:35 | XRP | down | 0.73→0.68 | 0.16 → 0.34 | 7.59s | edge gone |  |
| 10-04 10:22:16 | XRP | up | 0.74→0.80 | 0.75 → 0.85 | 11.85s | edge gone |  |
| 10-04 10:22:12 | SOL | up | 0.62→0.73 | 0.70 → 0.78 | 16.10s | edge gone |  |
| 10-04 10:22:11 | DOGE | up | 0.53→0.62 | 0.64 → 0.79 | 1.85s | spread too wide |  |
| 10-04 10:22:01 | XRP | up | 0.64→0.71 | 0.67 → 0.75 | 12.35s | edge gone |  |
| 10-04 10:21:51 | ZEC | down | 0.31→0.24 | 0.74 → 0.86 | 7.10s | edge gone |  |
| 10-04 10:21:38 | DOGE | up | 0.50→0.59 | 0.51 → 0.65 | 4.86s | edge gone |  |
| 10-04 10:21:37 | XRP | up | 0.54→0.60 | 0.49 → 0.60 | 21.11s | edge gone |  |
| 10-04 10:21:37 | SOL | up | 0.57→0.64 | 0.60 → 0.70 | 6.36s | edge gone |  |
| 10-04 10:21:35 | ZEC | up | 0.26→0.32 | 0.24 → 0.27 | 8.11s | edge gone |  |
| 10-04 10:21:30 | HYPE | up | 0.62→0.75 | 0.70 → 0.76 | 12.61s | edge gone |  |
| 10-04 10:21:01 | SOL | up | 0.47→0.54 | 0.56 → 0.60 | 12.12s | edge gone |  |
| 10-04 10:21:00 | XRP | up | 0.46→0.52 | 0.45 → 0.46 | 12.87s | UP @ 0.46 | -0.36 / -0.16 / · |
| 10-04 10:20:35 | ZEC | up | 0.34→0.39 | 0.33 → 0.36 | 8.37s | edge gone |  |
| 10-04 10:20:28 | XRP | down | 0.61→0.55 | 0.37 → 0.39 | 14.87s | DOWN @ 0.39 | -0.09 / 1.17 / · |
| 10-04 10:20:11 | XRP | down | 0.61→0.55 | 0.34 → 0.38 | 2.13s | DOWN @ 0.38 | -0.37 / 0.75 / · |
| 10-04 10:20:03 | NEAR | up | 0.17→0.23 | 0.25 → 0.25 | no | edge gone |  |
| 10-04 10:19:57 | ZEC | up | 0.27→0.33 | 0.30 → 0.26 | 30.89s | UP @ 0.26 | -0.13 / 0.36 / · |
| 10-04 10:19:53 | XRP | up | 0.57→0.62 | 0.73 → 0.65 | no | edge gone |  |
| 10-04 10:19:52 | SOL | down | 0.61→0.54 | 0.36 → 0.41 | no | DOWN @ 0.41 | -1.13 / -1.42 / · |
| 10-04 10:19:46 | DOGE | down | 0.58→0.50 | 0.41 → 0.51 | 11.88s | edge gone |  |
