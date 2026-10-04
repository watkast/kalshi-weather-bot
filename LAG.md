# Lag Tracker

*Updated Sun Oct 04 09:34 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🟡 **Testing with real order-book fills.** 9 of 150 settled trades needed before calling it. The earlier results below used quoted prices, which may not have been fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$19.52** | -66.1% | 9 | $3.22 | $27.45 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 10 | 2 | -$4.30 | -13.4% | -$1.90 / -$2.40 |
| Sell after 30 sec | 10 | 2 | -$6.70 | -20.8% | -$0.45 / -$6.25 |
| Hold to the close | 9 | 1 | -$19.52 | -66.1% | -$12.62 / -$6.90 |
| Hold, only edge 10¢+ | 4 | 0 | -$8.39 | -100.0% | -$2.07 / -$6.32 |
| Hold, first trade per window only | 6 | 1 | -$8.64 | -46.4% | -$6.55 / -$2.09 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 61 | 8% | 61% | +3.1¢ | 0.3¢ | edge gone 46, price out of range 4, spread too wide 1 |

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
| BTC | 522 | 11.9s | 3% | 0% |
| DOGE | 717 | 10.4s | 2% | 0% |
| ETH | 695 | 11.2s | 4% | 0% |
| HYPE | 598 | 11.2s | 4% | 0% |
| NEAR | 703 | 10.8s | 4% | 0% |
| SOL | 1280 | 11.0s | 3% | 0% |
| XRP | 1300 | 10.9s | 4% | 0% |
| ZEC | 868 | 9.6s | 4% | 0% |
| **All** | **7328** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 09:34:00 | ETH | down | 0.24→0.19 | 0.73 → 0.84 | no | edge gone |  |
| 10-04 09:33:56 | BTC | down | 0.28→0.21 | 0.69 → 0.79 | 1.97s | edge gone |  |
| 10-04 09:33:38 | BTC | down | 0.36→0.27 | 0.67 → 0.72 | 19.48s | edge gone |  |
| 10-04 09:33:20 | XRP | down | 0.21→0.15 | 0.81 → 0.83 | no | edge gone |  |
| 10-04 09:33:17 | BTC | down | 0.45→0.38 | 0.57 → 0.65 | 10.98s | edge gone |  |
| 10-04 09:33:15 | ETH | down | 0.50→0.34 | 0.55 → 0.68 | 12.48s | edge gone |  |
| 10-04 09:32:37 | ETH | down | 0.51→0.45 | 0.49 → 0.54 | 20.24s | edge gone |  |
| 10-04 09:32:29 | XRP | down | 0.22→0.16 | 0.83 → 0.82 | no | edge gone |  |
| 10-04 09:32:24 | BTC | up | 0.36→0.51 | 0.34 → 0.49 | no | edge gone |  |
| 10-04 09:31:55 | DOGE | up | 0.25→0.31 | 0.28 → 0.25 | no | UP @ 0.25 | -0.37 / -0.37 / · |
| 10-04 09:31:18 | BTC | down | 0.49→0.43 | 0.52 → 0.57 | 9.51s | edge gone |  |
| 10-04 09:31:14 | XRP | down | 0.33→0.20 | 0.72 → 0.76 | no | edge gone |  |
| 10-04 09:28:04 | NEAR | up | 0.56→0.74 | 0.96 → 0.98 | no | price out of range |  |
| 10-04 09:27:33 | NEAR | up | 0.60→0.70 | 0.92 → 0.95 | 24.54s | edge gone |  |
| 10-04 09:26:48 | NEAR | up | 0.47→0.58 | 0.65 → 0.84 | 10.03s | edge gone |  |
| 10-04 09:26:34 | DOGE | down | 0.99→0.94 | 0.01 → 0.04 | 9.03s | price out of range |  |
| 10-04 09:26:30 | NEAR | up | 0.33→0.42 | 0.60 → 0.67 | 12.53s | edge gone |  |
| 10-04 09:25:30 | NEAR | up | 0.53→0.59 | 0.90 → 0.87 | no | edge gone |  |
| 10-04 09:25:11 | NEAR | up | 0.59→0.64 | 0.90 → 0.90 | no | edge gone |  |
| 10-04 09:24:48 | ZEC | up | 0.77→0.83 | 0.90 → 0.92 | 10.28s | edge gone |  |
| 10-04 09:24:24 | NEAR | down | 0.60→0.52 | 0.14 → 0.25 | 3.78s | DOWN @ 0.25 | -1.16 / -1.77 / -2.66 |
| 10-04 09:24:09 | NEAR | up | 0.62→0.68 | 0.84 → 0.87 | no | edge gone |  |
| 10-04 09:20:44 | ZEC | up | 0.48→0.53 | 0.53 → 0.49 | no | edge gone |  |
| 10-04 09:20:39 | HYPE | up | 0.28→0.33 | 0.30 → 0.29 | no | edge gone |  |
| 10-04 09:20:25 | SOL | down | 0.58→0.50 | 0.36 → 0.35 | no | DOWN @ 0.35 | -0.51 / · / -3.66 |
| 10-04 09:20:06 | XRP | down | 0.76→0.68 | 0.25 → 0.26 | no | DOWN @ 0.26 | -0.38 / 0.50 / -2.74 |
| 10-04 09:20:01 | ZEC | down | 0.42→0.36 | 0.74 → 0.72 | no | edge gone |  |
| 10-04 09:19:51 | XRP | up | 0.62→0.68 | 0.77 → 0.76 | no | edge gone |  |
| 10-04 09:19:20 | XRP | up | 0.62→0.70 | 0.73 → 0.76 | no | edge gone |  |
| 10-04 09:19:08 | BNB | down | 0.95→0.82 | 0.13 → 0.18 | no | edge gone |  |
