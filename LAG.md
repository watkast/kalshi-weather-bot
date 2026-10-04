# Lag Tracker

*Updated Sun Oct 04 16:55 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$395.51** | -18.0% | 603 | $3.68 | $126.78 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 631 | 110 | -$255.53 | -11.0% | -$137.21 / -$118.32 |
| Sell after 30 sec | 629 | 166 | -$270.40 | -11.7% | -$161.32 / -$109.08 |
| Hold to the close | 603 | 180 | -$395.51 | -18.0% | -$363.06 / -$32.45 |
| Hold, only edge 10¢+ | 218 | 48 | -$138.42 | -22.4% | -$140.77 / $2.35 |
| Hold, first trade per window only | 201 | 71 | -$91.72 | -11.4% | -$74.30 / -$17.42 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 2409 | 9% | 67% | +5.0¢ | 0.3¢ | edge gone 1655, price out of range 63, spread too wide 60 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 706 | 11.1s | 3% | 0% |
| BTC | 818 | 11.9s | 3% | 0% |
| DOGE | 900 | 10.5s | 3% | 0% |
| ETH | 975 | 10.8s | 4% | 0% |
| HYPE | 700 | 11.6s | 3% | 0% |
| NEAR | 941 | 10.8s | 3% | 0% |
| SOL | 1776 | 10.9s | 3% | 0% |
| XRP | 1795 | 11.2s | 3% | 0% |
| ZEC | 1065 | 9.6s | 4% | 0% |
| **All** | **9676** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **7 ms** · Order book check: **25 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 16:55:45 | XRP | down | 0.68→0.62 | 0.30 → 0.27 | no | DOWN @ 0.27 | -0.77 / · / · |
| 10-04 16:55:37 | ETH | down | 0.79→0.69 | 0.26 → 0.18 | no | DOWN @ 0.19 | -0.50 / · / · |
| 10-04 16:55:35 | DOGE | up | 0.89→0.95 | 0.93 → 0.96 | no | price out of range |  |
| 10-04 16:55:28 | XRP | up | 0.53→0.65 | 0.54 → 0.64 | no | edge gone |  |
| 10-04 16:55:28 | BTC | up | 0.55→0.63 | 0.60 → 0.74 | 14.40s | edge gone |  |
| 10-04 16:55:20 | ETH | down | 0.77→0.72 | 0.26 → 0.30 | no | edge gone |  |
| 10-04 16:55:20 | DOGE | down | 0.90→0.81 | 0.08 → 0.07 | no | DOWN @ 0.07 | -0.24 / -0.58 / · |
| 10-04 16:55:19 | SOL | up | 0.81→0.86 | 0.92 → 0.92 | 23.90s | edge gone |  |
| 10-04 16:55:05 | ETH | down | 0.78→0.70 | 0.18 → 0.29 | 7.52s | edge gone |  |
| 10-04 16:54:59 | BTC | down | 0.69→0.62 | 0.21 → 0.32 | 13.27s | DOWN @ 0.32 | 0.57 / -1.00 / · |
| 10-04 16:54:52 | XRP | down | 0.64→0.55 | 0.35 → 0.35 | no | DOWN @ 0.35 | -0.32 / 0.96 / · |
| 10-04 16:54:45 | ETH | up | 0.76→0.83 | 0.80 → 0.79 | 12.27s | edge gone |  |
| 10-04 16:54:44 | BTC | down | 0.73→0.68 | 0.21 → 0.26 | 28.53s | DOWN @ 0.26 | -0.67 / 0.89 / · |
| 10-04 16:54:33 | ZEC | down | 0.85→0.79 | 0.07 → 0.06 | no | DOWN @ 0.06 | -0.32 / -0.38 / · |
| 10-04 16:54:31 | XRP | up | 0.55→0.61 | 0.67 → 0.62 | no | edge gone |  |
| 10-04 16:54:12 | XRP | down | 0.58→0.53 | 0.31 → 0.41 | 15.27s | DOWN @ 0.41 | -1.13 / -1.03 / · |
| 10-04 16:54:02 | ETH | up | 0.70→0.78 | 0.68 → 0.77 | 25.28s | edge gone |  |
| 10-04 16:53:57 | XRP | down | 0.67→0.60 | 0.18 → 0.29 | 0.27s | DOWN @ 0.29 | 0.68 / 0.97 / · |
| 10-04 16:53:42 | BTC | down | 0.79→0.71 | 0.15 → 0.26 | 15.52s | edge gone |  |
| 10-04 16:53:41 | ETH | down | 0.86→0.77 | 0.17 → 0.25 | 17.03s | edge gone |  |
| 10-04 16:53:40 | XRP | down | 0.77→0.71 | 0.19 → 0.26 | 17.28s | edge gone |  |
| 10-04 16:53:16 | BTC | down | 0.85→0.79 | 0.15 → 0.15 | no | DOWN @ 0.15 | -0.28 / 0.58 / · |
| 10-04 16:53:15 | XRP | down | 0.80→0.73 | 0.18 → 0.19 | no | DOWN @ 0.19 | -0.32 / 0.94 / · |
| 10-04 16:53:12 | DOGE | up | 0.88→0.93 | 0.78 → 0.93 | 1.02s | edge gone |  |
| 10-04 16:53:07 | ETH | up | 0.79→0.86 | 0.75 → 0.84 | 5.52s | edge gone |  |
| 10-04 16:52:51 | XRP | up | 0.61→0.70 | 0.75 → 0.73 | 21.03s | edge gone |  |
| 10-04 16:52:42 | HYPE | up | 0.74→0.79 | 0.86 → 0.90 | 30.03s | edge gone |  |
| 10-04 16:52:31 | ETH | up | 0.80→0.85 | 0.76 → 0.80 | 11.52s | UP @ 0.80 | -0.24 / -0.55 / · |
| 10-04 16:52:29 | XRP | up | 0.63→0.70 | 0.70 → 0.75 | no | edge gone |  |
| 10-04 16:52:14 | XRP | up | 0.64→0.71 | 0.72 → 0.76 | no | edge gone |  |
