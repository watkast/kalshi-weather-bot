# Lag Tracker

*Updated Sun Oct 04 09:22 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🟡 **Testing with real order-book fills.** 2 of 150 settled trades needed before calling it. The earlier results below used quoted prices, which may not have been fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$2.07** | -100.0% | 2 | $3.36 | $24.79 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 8 | 2 | -$2.77 | -10.3% | -$2.07 / -$0.70 |
| Sell after 30 sec | 7 | 2 | -$0.90 | -3.9% | -$2.39 / $1.49 |
| Hold to the close | 2 | 0 | -$2.07 | -100.0% | -$1.38 / -$0.69 |
| Hold, only edge 10¢+ | 2 | 0 | -$2.07 | -100.0% | -$1.38 / -$0.69 |
| Hold, first trade per window only | 2 | 0 | -$2.07 | -100.0% | -$1.38 / -$0.69 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 39 | 10% | 54% | +3.0¢ | 0.4¢ | edge gone 28, price out of range 2, spread too wide 1 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 645 | 11.1s | 3% | 0% |
| BTC | 517 | 11.9s | 3% | 0% |
| DOGE | 715 | 10.4s | 2% | 0% |
| ETH | 692 | 11.1s | 4% | 0% |
| HYPE | 598 | 11.2s | 4% | 0% |
| NEAR | 695 | 10.8s | 4% | 0% |
| SOL | 1280 | 11.0s | 3% | 0% |
| XRP | 1297 | 10.9s | 4% | 0% |
| ZEC | 867 | 9.6s | 4% | 0% |
| **All** | **7306** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **12 ms** · Order book check: **26 ms** · Coinbase price delay: **24 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 09:20:44 | ZEC | up | 0.48→0.53 | 0.53 → 0.49 | no | edge gone |  |
| 10-04 09:20:39 | HYPE | up | 0.28→0.33 | 0.30 → 0.29 | no | edge gone |  |
| 10-04 09:20:25 | SOL | down | 0.58→0.50 | 0.36 → 0.35 | no | DOWN @ 0.35 | -0.51 / · / · |
| 10-04 09:20:06 | XRP | down | 0.76→0.68 | 0.25 → 0.26 | no | DOWN @ 0.26 | -0.38 / 0.50 / · |
| 10-04 09:20:01 | ZEC | down | 0.42→0.36 | 0.74 → 0.72 | no | edge gone |  |
| 10-04 09:19:51 | XRP | up | 0.62→0.68 | 0.77 → 0.76 | no | edge gone |  |
| 10-04 09:19:20 | XRP | up | 0.62→0.70 | 0.73 → 0.76 | no | edge gone |  |
| 10-04 09:19:08 | BNB | down | 0.95→0.82 | 0.13 → 0.18 | no | edge gone |  |
| 10-04 09:19:05 | XRP | up | 0.67→0.72 | 0.74 → 0.76 | no | edge gone |  |
| 10-04 09:19:05 | NEAR | up | 0.23→0.28 | 0.38 → 0.39 | no | edge gone |  |
| 10-04 09:19:03 | SOL | down | 0.54→0.47 | 0.41 → 0.40 | 16.98s | DOWN @ 0.43 | 0.02 / -0.95 / · |
| 10-04 09:18:44 | SOL | up | 0.47→0.54 | 0.52 → 0.60 | 5.73s | edge gone |  |
| 10-04 09:18:38 | ZEC | up | 0.25→0.32 | 0.35 → 0.33 | no | spread too wide |  |
| 10-04 09:18:35 | XRP | up | 0.62→0.67 | 0.86 → 0.73 | 0.22s | edge gone |  |
| 10-04 09:18:30 | BTC | up | 0.57→0.63 | 0.75 → 0.69 | no | edge gone |  |
| 10-04 09:18:29 | ETH | down | 0.66→0.60 | 0.32 → 0.48 | 20.74s | edge gone |  |
| 10-04 09:18:29 | DOGE | down | 0.66→0.55 | 0.53 → 0.44 | no | edge gone |  |
| 10-04 09:18:26 | BNB | down | 0.90→0.83 | 0.15 → 0.15 | no | edge gone |  |
| 10-04 09:18:20 | XRP | up | 0.64→0.72 | 0.75 → 0.82 | 14.74s | edge gone |  |
| 10-04 09:18:15 | BTC | up | 0.65→0.71 | 0.69 → 0.75 | 4.24s | edge gone |  |
| 10-04 09:18:07 | HYPE | down | 0.36→0.30 | 0.64 → 0.69 | 12.74s | edge gone |  |
| 10-04 09:18:01 | XRP | up | 0.56→0.61 | 0.61 → 0.74 | 3.24s | edge gone |  |
| 10-04 09:18:01 | SOL | up | 0.37→0.44 | 0.40 → 0.52 | 18.24s | edge gone |  |
| 10-04 09:17:54 | DOGE | up | 0.32→0.41 | 0.36 → 0.32 | 25.49s | UP @ 0.32 | 0.17 / 2.28 / · |
| 10-04 09:17:54 | BNB | up | 0.41→0.51 | 0.52 → 0.62 | 10.99s | edge gone |  |
| 10-04 09:17:45 | XRP | up | 0.47→0.53 | 0.63 → 0.61 | 19.24s | edge gone |  |
| 10-04 09:17:25 | XRP | up | 0.47→0.56 | 0.61 → 0.64 | no | edge gone |  |
| 10-04 09:17:21 | SOL | down | 0.41→0.35 | 0.44 → 0.59 | 13.74s | DOWN @ 0.59 | -0.36 / -0.34 / · |
| 10-04 09:17:02 | XRP | down | 0.53→0.47 | 0.42 → 0.43 | no | DOWN @ 0.43 | -0.75 / -0.95 / · |
| 10-04 09:16:30 | BTC | up | 0.56→0.65 | 0.60 → 0.67 | 14.25s | edge gone |  |
