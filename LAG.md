# Lag Tracker

*Updated Sun Oct 04 09:44 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🟡 **Testing with real order-book fills.** 9 of 150 settled trades needed before calling it. The earlier results below used quoted prices, which may not have been fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$19.52** | -66.1% | 9 | $3.65 | $32.59 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 17 | 5 | -$3.42 | -5.5% | -$2.77 / -$0.65 |
| Sell after 30 sec | 16 | 4 | -$12.43 | -21.3% | -$4.56 / -$7.87 |
| Hold to the close | 9 | 1 | -$19.52 | -66.1% | -$12.62 / -$6.90 |
| Hold, only edge 10¢+ | 4 | 0 | -$8.39 | -100.0% | -$2.07 / -$6.32 |
| Hold, first trade per window only | 6 | 1 | -$8.64 | -46.4% | -$6.55 / -$2.09 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 108 | 6% | 69% | +5.0¢ | 0.2¢ | edge gone 86, price out of range 4, spread too wide 1 |

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
| BTC | 534 | 11.9s | 3% | 0% |
| DOGE | 724 | 10.3s | 2% | 0% |
| ETH | 702 | 11.2s | 4% | 0% |
| HYPE | 598 | 11.2s | 4% | 0% |
| NEAR | 703 | 10.8s | 4% | 0% |
| SOL | 1294 | 11.0s | 3% | 0% |
| XRP | 1306 | 10.9s | 4% | 0% |
| ZEC | 868 | 9.6s | 4% | 0% |
| **All** | **7375** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **34 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 09:43:39 | ETH | up | 0.18→0.52 | 0.17 → 0.37 | 3.78s | UP @ 0.37 | 3.29 / · / · |
| 10-04 09:43:39 | SOL | up | 0.03→0.13 | 0.65 → 0.18 | no | edge gone |  |
| 10-04 09:43:37 | BTC | up | 0.08→0.19 | 0.45 → 0.19 | no | edge gone |  |
| 10-04 09:43:37 | DOGE | up | 0.11→0.28 | 0.26 → 0.49 | 20.54s | edge gone |  |
| 10-04 09:43:20 | ETH | down | 0.83→0.53 | 0.32 → 0.72 | 7.78s | edge gone |  |
| 10-04 09:43:20 | BTC | down | 0.72→0.36 | 0.35 → 0.65 | 8.03s | edge gone |  |
| 10-04 09:43:19 | DOGE | down | 0.77→0.61 | 0.22 → 0.41 | 8.28s | edge gone |  |
| 10-04 09:43:19 | SOL | down | 0.66→0.57 | 0.37 → 0.44 | 24.04s | edge gone |  |
| 10-04 09:43:03 | SOL | up | 0.56→0.65 | 0.95 → 0.61 | no | edge gone |  |
| 10-04 09:43:01 | BTC | down | 0.91→0.71 | 0.25 → 0.33 | 26.29s | edge gone |  |
| 10-04 09:43:01 | ETH | down | 0.98→0.90 | 0.08 → 0.35 | 11.28s | edge gone |  |
| 10-04 09:42:44 | BTC | down | 0.80→0.69 | 0.17 → 0.27 | 13.29s | edge gone |  |
| 10-04 09:42:41 | SOL | up | 0.63→0.70 | 0.78 → 0.81 | 17.04s | edge gone |  |
| 10-04 09:42:40 | XRP | down | 0.59→0.50 | 0.46 → 0.63 | 2.54s | edge gone |  |
| 10-04 09:42:20 | SOL | down | 0.87→0.69 | 0.37 → 0.25 | no | DOWN @ 0.25 | -0.08 / -1.78 / · |
| 10-04 09:42:15 | BTC | up | 0.70→0.76 | 0.74 → 0.79 | 0.28s | edge gone |  |
| 10-04 09:42:05 | SOL | up | 0.47→0.54 | 0.55 → 0.65 | 7.30s | edge gone |  |
| 10-04 09:41:55 | XRP | down | 0.34→0.27 | 0.71 → 0.75 | no | edge gone |  |
| 10-04 09:41:53 | BTC | up | 0.64→0.71 | 0.62 → 0.73 | 19.80s | edge gone |  |
| 10-04 09:41:50 | SOL | up | 0.41→0.54 | 0.47 → 0.56 | 7.30s | edge gone |  |
| 10-04 09:41:35 | SOL | up | 0.35→0.41 | 0.32 → 0.47 | 7.56s | edge gone |  |
| 10-04 09:41:31 | XRP | down | 0.39→0.29 | 0.64 → 0.76 | 11.31s | edge gone |  |
| 10-04 09:41:24 | DOGE | up | 0.62→0.72 | 0.60 → 0.90 | 4.06s | edge gone |  |
| 10-04 09:41:20 | SOL | up | 0.35→0.48 | 0.32 → 0.44 | 22.56s | edge gone |  |
| 10-04 09:41:20 | BTC | up | 0.35→0.41 | 0.31 → 0.49 | 23.06s | edge gone |  |
| 10-04 09:41:18 | BNB | up | 0.17→0.23 | 0.16 → 0.33 | 9.56s | edge gone |  |
| 10-04 09:41:17 | ETH | up | 0.45→0.51 | 0.39 → 0.55 | 10.56s | edge gone |  |
| 10-04 09:41:13 | XRP | down | 0.33→0.16 | 0.76 → 0.87 | no | edge gone |  |
| 10-04 09:41:05 | SOL | down | 0.42→0.36 | 0.69 → 0.70 | no | edge gone |  |
| 10-04 09:40:43 | SOL | up | 0.42→0.48 | 0.25 → 0.40 | 0.30s | UP @ 0.40 | -1.03 / -1.22 / · |
