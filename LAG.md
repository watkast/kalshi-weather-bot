# Lag Tracker

*Updated Sun Oct 04 14:25 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$346.77** | -24.3% | 391 | $3.64 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 401 | 69 | -$171.70 | -11.8% | -$93.23 / -$78.47 |
| Sell after 30 sec | 400 | 94 | -$194.36 | -13.3% | -$98.31 / -$96.05 |
| Hold to the close | 391 | 108 | -$346.77 | -24.3% | -$217.13 / -$129.64 |
| Hold, only edge 10¢+ | 138 | 23 | -$143.01 | -38.3% | -$127.76 / -$15.25 |
| Hold, first trade per window only | 134 | 45 | -$84.80 | -15.9% | -$30.48 / -$54.32 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 1498 | 11% | 65% | +4.3¢ | 0.3¢ | edge gone 1025, price out of range 41, spread too wide 31 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 676 | 11.1s | 3% | 0% |
| BTC | 707 | 11.9s | 3% | 0% |
| DOGE | 813 | 10.4s | 3% | 0% |
| ETH | 855 | 11.2s | 4% | 0% |
| HYPE | 663 | 11.6s | 3% | 0% |
| NEAR | 850 | 10.8s | 4% | 0% |
| SOL | 1600 | 10.9s | 3% | 0% |
| XRP | 1612 | 11.0s | 3% | 0% |
| ZEC | 989 | 9.6s | 4% | 0% |
| **All** | **8765** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 14:25:52 | XRP | down | 0.40→0.30 | 0.76 → 0.66 | no | edge gone |  |
| 10-04 14:25:41 | ZEC | down | 0.14→0.08 | 0.95 → 0.97 | no | price out of range |  |
| 10-04 14:25:38 | DOGE | up | 0.65→0.73 | 0.84 → 0.85 | no | edge gone |  |
| 10-04 14:25:30 | XRP | up | 0.25→0.31 | 0.24 → 0.24 | no | UP @ 0.24 | -0.26 / · / · |
| 10-04 14:25:22 | ZEC | down | 0.15→0.07 | 0.90 → 0.96 | 1.26s | price out of range |  |
| 10-04 14:25:15 | XRP | up | 0.23→0.28 | 0.23 → 0.24 | no | edge gone |  |
| 10-04 14:24:47 | ZEC | down | 0.20→0.15 | 0.91 → 0.94 | no | spread too wide |  |
| 10-04 14:24:42 | XRP | up | 0.22→0.29 | 0.21 → 0.18 | 11.27s | UP @ 0.18 | 0.26 / 0.28 / · |
| 10-04 14:24:30 | ZEC | down | 0.31→0.24 | 0.83 → 0.80 | 8.52s | edge gone |  |
| 10-04 14:24:07 | XRP | up | 0.21→0.28 | 0.21 → 0.19 | no | UP @ 0.19 | -0.41 / -0.29 / · |
| 10-04 14:24:06 | ZEC | up | 0.15→0.24 | 0.16 → 0.14 | 18.28s | UP @ 0.14 | 0.01 / -0.68 / · |
| 10-04 14:23:37 | ETH | up | 0.11→0.18 | 0.13 → 0.12 | no | UP @ 0.12 | -0.35 / -0.48 / · |
| 10-04 14:23:20 | XRP | up | 0.18→0.26 | 0.18 → 0.22 | 19.29s | edge gone |  |
| 10-04 14:22:40 | ETH | up | 0.16→0.22 | 0.14 → 0.16 | 29.79s | UP @ 0.16 | -0.10 / 0.18 / · |
| 10-04 14:22:32 | ZEC | up | 0.30→0.37 | 0.22 → 0.27 | 7.53s | UP @ 0.27 | -0.14 / -1.05 / · |
| 10-04 14:22:15 | XRP | up | 0.10→0.32 | 0.07 → 0.25 | 9.28s | UP @ 0.25 | -1.04 / -1.23 / · |
| 10-04 14:22:15 | ETH | up | 0.05→0.20 | 0.06 → 0.18 | 9.28s | edge gone |  |
| 10-04 14:21:45 | HYPE | down | 0.22→0.17 | 0.84 → 0.85 | 25.29s | edge gone |  |
| 10-04 14:21:34 | XRP | down | 0.13→0.07 | 0.91 → 0.92 | no | edge gone |  |
| 10-04 14:21:29 | ZEC | down | 0.55→0.39 | 0.75 → 0.78 | no | spread too wide |  |
| 10-04 14:21:18 | DOGE | up | 0.36→0.42 | 0.39 → 0.44 | 6.53s | edge gone |  |
| 10-04 14:20:59 | BTC | down | 0.13→0.08 | 0.87 → 0.91 | 10.53s | edge gone |  |
| 10-04 14:20:43 | XRP | down | 0.26→0.14 | 0.81 → 0.85 | 12.03s | edge gone |  |
| 10-04 14:20:31 | NEAR | down | 0.21→0.16 | 0.69 → 0.77 | 8.53s | DOWN @ 0.79 | -0.52 / -0.11 / · |
| 10-04 14:19:57 | BTC | down | 0.25→0.17 | 0.78 → 0.85 | 12.78s | edge gone |  |
| 10-04 14:19:57 | ETH | down | 0.30→0.25 | 0.78 → 0.84 | 13.28s | edge gone |  |
| 10-04 14:19:54 | XRP | down | 0.41→0.34 | 0.64 → 0.66 | 15.79s | edge gone |  |
| 10-04 14:19:40 | HYPE | down | 0.28→0.22 | 0.70 → 0.80 | 14.78s | edge gone |  |
| 10-04 14:19:38 | NEAR | down | 0.33→0.27 | 0.68 → 0.68 | no | edge gone |  |
| 10-04 14:19:35 | XRP | down | 0.48→0.41 | 0.53 → 0.64 | 5.03s | edge gone |  |
