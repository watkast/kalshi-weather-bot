# Lag Tracker

*Updated Sun Oct 04 16:35 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$363.43** | -16.9% | 587 | $3.67 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 592 | 101 | -$248.48 | -11.4% | -$127.03 / -$121.45 |
| Sell after 30 sec | 592 | 148 | -$270.79 | -12.5% | -$150.86 / -$119.93 |
| Hold to the close | 587 | 179 | -$363.43 | -16.9% | -$344.01 / -$19.42 |
| Hold, only edge 10¢+ | 209 | 48 | -$116.09 | -19.5% | -$130.66 / $14.57 |
| Hold, first trade per window only | 196 | 71 | -$81.58 | -10.3% | -$66.44 / -$15.14 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 2291 | 10% | 67% | +5.0¢ | 0.3¢ | edge gone 1578, price out of range 62, spread too wide 59 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 702 | 11.2s | 3% | 0% |
| BTC | 807 | 11.9s | 3% | 0% |
| DOGE | 876 | 10.5s | 3% | 0% |
| ETH | 956 | 10.8s | 4% | 0% |
| HYPE | 698 | 11.6s | 3% | 0% |
| NEAR | 933 | 10.8s | 3% | 0% |
| SOL | 1766 | 10.9s | 3% | 0% |
| XRP | 1760 | 11.2s | 3% | 0% |
| ZEC | 1060 | 9.6s | 4% | 0% |
| **All** | **9558** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **7 ms** · Order book check: **25 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 16:35:30 | DOGE | up | 0.71→0.80 | 0.82 → 0.89 | 12.80s | edge gone |  |
| 10-04 16:34:15 | NEAR | up | 0.83→0.92 | 0.73 → 0.90 | 12.31s | UP @ 0.91 | 0.03 / -0.61 / · |
| 10-04 16:34:00 | NEAR | up | 0.62→0.67 | 0.70 → 0.75 | 27.57s | edge gone |  |
| 10-04 16:33:43 | NEAR | up | 0.72→0.77 | 0.79 → 0.85 | no | edge gone |  |
| 10-04 16:33:43 | SOL | up | 0.77→0.85 | 0.85 → 0.87 | 14.57s | edge gone |  |
| 10-04 16:33:37 | BNB | up | 0.34→0.42 | 0.71 → 0.69 | no | edge gone |  |
| 10-04 16:33:01 | ETH | down | 0.89→0.84 | 0.13 → 0.14 | no | edge gone |  |
| 10-04 16:33:00 | BNB | down | 0.46→0.38 | 0.32 → 0.33 | no | DOWN @ 0.34 | -0.86 / -0.61 / · |
| 10-04 16:33:00 | SOL | down | 0.78→0.73 | 0.15 → 0.20 | 12.58s | DOWN @ 0.20 | -0.62 / -0.71 / · |
| 10-04 16:32:32 | BNB | down | 0.59→0.51 | 0.31 → 0.26 | no | DOWN @ 0.26 | -0.38 / 0.30 / · |
| 10-04 16:32:21 | ETH | up | 0.81→0.87 | 0.79 → 0.84 | 6.59s | edge gone |  |
| 10-04 16:32:21 | XRP | up | 0.67→0.73 | 0.71 → 0.76 | 6.84s | edge gone |  |
| 10-04 16:32:18 | ZEC | up | 0.53→0.59 | 0.64 → 0.65 | 24.85s | spread too wide |  |
| 10-04 16:32:12 | SOL | up | 0.68→0.74 | 0.72 → 0.78 | 16.10s | edge gone |  |
| 10-04 16:31:57 | ETH | up | 0.75→0.80 | 0.77 → 0.77 | no | edge gone |  |
| 10-04 16:31:57 | NEAR | down | 0.55→0.48 | 0.28 → 0.36 | no | DOWN @ 0.36 | -1.12 / -0.73 / · |
| 10-04 16:31:33 | DOGE | up | 0.59→0.65 | 0.68 → 0.72 | 9.85s | edge gone |  |
| 10-04 16:31:04 | HYPE | up | 0.60→0.65 | 0.72 → 0.75 | 8.36s | edge gone |  |
| 10-04 16:31:03 | XRP | up | 0.58→0.66 | 0.69 → 0.70 | 25.11s | edge gone |  |
| 10-04 16:31:02 | SOL | up | 0.55→0.60 | 0.69 → 0.68 | no | edge gone |  |
| 10-04 16:30:58 | BNB | up | 0.39→0.49 | 0.66 → 0.65 | no | edge gone |  |
| 10-04 16:30:57 | BTC | down | 0.72→0.66 | 0.33 → 0.36 | 15.11s | edge gone |  |
| 10-04 16:28:37 | BNB | down | 0.65→0.58 | 0.03 → 0.02 | no | price out of range |  |
| 10-04 16:28:36 | DOGE | up | 0.22→0.27 | 0.13 → 0.15 | 7.39s | UP @ 0.15 | -0.41 / -1.52 / -1.65 |
| 10-04 16:28:17 | BNB | up | 0.28→0.71 | 0.98 → 0.99 | no | price out of range |  |
| 10-04 16:28:17 | BTC | up | 0.02→0.08 | 0.02 → 0.03 | no | price out of range |  |
| 10-04 16:27:30 | BNB | down | 0.49→0.25 | 0.09 → 0.09 | no | DOWN @ 0.09 | -0.49 / -0.62 / -0.94 |
| 10-04 16:27:25 | DOGE | down | 0.22→0.16 | 0.92 → 0.96 | 3.41s | price out of range |  |
| 10-04 16:27:03 | NEAR | down | 0.25→0.17 | 0.56 → 0.70 | 10.92s | spread too wide |  |
| 10-04 16:26:47 | DOGE | down | 0.28→0.19 | 0.95 → 0.90 | no | edge gone |  |
