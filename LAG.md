# Lag Tracker

*Updated Sun Oct 04 12:15 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$217.13** | -32.1% | 195 | $3.55 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 224 | 36 | -$98.31 | -12.4% | -$41.45 / -$56.86 |
| Sell after 30 sec | 224 | 52 | -$101.43 | -12.8% | -$40.33 / -$61.10 |
| Hold to the close | 195 | 46 | -$217.13 | -32.1% | -$12.23 / -$204.90 |
| Hold, only edge 10¢+ | 66 | 4 | -$126.14 | -75.9% | -$39.39 / -$86.75 |
| Hold, first trade per window only | 71 | 24 | -$35.09 | -12.8% | $8.66 / -$43.75 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 788 | 11% | 64% | +5.0¢ | 0.3¢ | edge gone 522, price out of range 29, spread too wide 13 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 661 | 11.1s | 3% | 0% |
| BTC | 603 | 11.9s | 3% | 0% |
| DOGE | 773 | 10.6s | 2% | 0% |
| ETH | 776 | 11.0s | 4% | 0% |
| HYPE | 636 | 11.3s | 4% | 0% |
| NEAR | 793 | 10.8s | 4% | 0% |
| SOL | 1446 | 10.8s | 3% | 0% |
| XRP | 1444 | 11.0s | 4% | 0% |
| ZEC | 923 | 9.7s | 4% | 0% |
| **All** | **8055** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 12:13:43 | ETH | down | 0.86→0.80 | 0.26 → 0.43 | 0.28s | edge gone |  |
| 10-04 12:13:43 | BTC | down | 0.38→0.13 | 0.47 → 0.74 | 15.79s | DOWN @ 0.74 | 1.88 / 2.40 / · |
| 10-04 12:13:19 | BNB | down | 0.26→0.17 | 0.00 → 0.29 | 9.28s | DOWN @ 0.34 | -1.15 / -1.37 / · |
| 10-04 12:13:15 | NEAR | up | 0.81→0.87 | 0.98 → 0.99 | no | price out of range |  |
| 10-04 12:13:09 | BTC | down | 0.27→0.22 | 0.31 → 0.62 | 4.78s | DOWN @ 0.64 | -0.23 / -1.05 / · |
| 10-04 12:12:54 | ETH | down | 0.99→0.92 | 0.03 → 0.33 | 19.54s | edge gone |  |
| 10-04 12:12:54 | BTC | down | 0.99→0.51 | 0.01 → 0.26 | 4.78s | DOWN @ 0.26 | 2.68 / 1.38 / · |
| 10-04 12:12:50 | ZEC | up | 0.06→0.12 | 0.09 → 0.10 | no | edge gone |  |
| 10-04 12:12:46 | NEAR | up | 0.80→0.87 | 0.98 → 0.99 | no | price out of range |  |
| 10-04 12:12:11 | HYPE | down | 0.75→0.69 | 0.18 → 0.14 | 2.78s | DOWN @ 0.14 | -0.84 / -1.12 / · |
| 10-04 12:12:02 | NEAR | down | 0.82→0.77 | 0.06 → 0.05 | no | DOWN @ 0.06 | -0.30 / -0.36 / · |
| 10-04 12:12:00 | ZEC | up | 0.12→0.19 | 0.21 → 0.21 | no | edge gone |  |
| 10-04 12:11:44 | NEAR | up | 0.72→0.77 | 0.98 → 0.95 | no | price out of range |  |
| 10-04 12:11:40 | HYPE | up | 0.56→0.62 | 0.87 → 0.87 | no | edge gone |  |
| 10-04 12:11:37 | BNB | up | 0.86→0.92 | 1.00 → 1.00 | no | price out of range |  |
| 10-04 12:11:34 | ETH | down | 0.99→0.93 | 0.02 → 0.12 | 9.78s | edge gone |  |
| 10-04 12:11:15 | ZEC | down | 0.33→0.21 | 0.52 → 0.50 | 29.29s | DOWN @ 0.50 | -0.56 / 1.77 / · |
| 10-04 12:10:46 | HYPE | up | 0.60→0.65 | 0.83 → 0.82 | 12.53s | spread too wide |  |
| 10-04 12:10:26 | NEAR | down | 0.93→0.84 | 0.02 → 0.03 | no | price out of range |  |
| 10-04 12:10:07 | ETH | up | 0.90→0.95 | 0.85 → 0.91 | 6.78s | UP @ 0.91 | 0.03 / 0.17 / · |
| 10-04 12:09:54 | ZEC | up | 0.25→0.38 | 0.42 → 0.49 | 20.29s | spread too wide |  |
| 10-04 12:09:31 | ZEC | down | 0.51→0.45 | 0.42 → 0.39 | 12.53s | DOWN @ 0.39 | -0.14 / 0.95 / · |
| 10-04 12:09:00 | ZEC | down | 0.47→0.41 | 0.49 → 0.50 | 0.26s | DOWN @ 0.50 | -0.87 / -1.57 / · |
| 10-04 12:08:42 | NEAR | down | 0.94→0.89 | 0.03 → 0.05 | no | DOWN @ 0.05 | -0.06 / -0.24 / · |
| 10-04 12:08:34 | ZEC | down | 0.59→0.53 | 0.32 → 0.41 | 9.53s | DOWN @ 0.41 | -0.64 / 0.06 / · |
| 10-04 12:07:08 | BNB | up | 0.65→0.71 | 0.86 → 0.92 | 6.28s | edge gone |  |
| 10-04 12:07:03 | ZEC | up | 0.77→0.86 | 0.73 → 0.85 | 10.53s | edge gone |  |
| 10-04 12:07:01 | HYPE | up | 0.64→0.71 | 0.74 → 0.80 | 12.53s | edge gone |  |
| 10-04 12:06:54 | ETH | up | 0.84→0.91 | 0.81 → 0.82 | 20.04s | UP @ 0.82 | 0.10 / 0.20 / · |
| 10-04 12:06:52 | NEAR | up | 0.76→0.96 | 0.91 → 0.95 | no | edge gone |  |
