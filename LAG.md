# Lag Tracker

*Updated Sun Oct 04 11:54 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$114.90** | -20.7% | 159 | $3.49 | $83.77 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 180 | 30 | -$76.47 | -12.2% | -$31.25 / -$45.22 |
| Sell after 30 sec | 179 | 42 | -$77.67 | -12.5% | -$30.93 / -$46.74 |
| Hold to the close | 159 | 44 | -$114.90 | -20.7% | -$1.82 / -$113.08 |
| Hold, only edge 10¢+ | 50 | 4 | -$82.31 | -67.3% | -$32.34 / -$49.97 |
| Hold, first trade per window only | 62 | 22 | -$20.87 | -8.7% | $2.73 / -$23.60 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 691 | 11% | 64% | +5.0¢ | 0.3¢ | edge gone 478, price out of range 24, spread too wide 9 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 653 | 11.1s | 3% | 0% |
| BTC | 596 | 11.9s | 3% | 0% |
| DOGE | 768 | 10.5s | 2% | 0% |
| ETH | 763 | 11.0s | 4% | 0% |
| HYPE | 626 | 11.2s | 4% | 0% |
| NEAR | 776 | 10.8s | 4% | 0% |
| SOL | 1430 | 10.8s | 3% | 0% |
| XRP | 1438 | 11.0s | 4% | 0% |
| ZEC | 908 | 9.6s | 4% | 0% |
| **All** | **7958** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 11:54:54 | SOL | up | 0.38→0.49 | 0.55 → 0.50 | no | edge gone |  |
| 10-04 11:54:42 | BNB | up | 0.35→0.41 | 0.59 → 0.68 | no | edge gone |  |
| 10-04 11:54:39 | SOL | down | 0.49→0.38 | 0.45 → 0.53 | no | DOWN @ 0.53 | -0.56 / · / · |
| 10-04 11:54:25 | HYPE | up | 0.11→0.18 | 0.20 → 0.18 | no | edge gone |  |
| 10-04 11:54:16 | SOL | up | 0.38→0.43 | 0.61 → 0.56 | no | edge gone |  |
| 10-04 11:54:11 | ETH | down | 0.65→0.60 | 0.41 → 0.48 | 0.14s | edge gone |  |
| 10-04 11:54:01 | SOL | up | 0.65→0.70 | 0.85 → 0.74 | no | edge gone |  |
| 10-04 11:53:46 | SOL | down | 0.83→0.75 | 0.19 → 0.17 | 25.41s | DOWN @ 0.17 | 0.85 / 2.42 / · |
| 10-04 11:53:40 | HYPE | down | 0.20→0.14 | 0.71 → 0.82 | 16.91s | edge gone |  |
| 10-04 11:53:38 | BTC | up | 0.73→0.80 | 0.77 → 0.86 | 18.41s | edge gone |  |
| 10-04 11:53:38 | ETH | up | 0.61→0.72 | 0.53 → 0.62 | 18.41s | UP @ 0.62 | -0.85 / -1.05 / · |
| 10-04 11:53:38 | NEAR | up | 0.15→0.21 | 0.24 → 0.26 | no | spread too wide |  |
| 10-04 11:53:33 | ZEC | up | 0.59→0.70 | 0.69 → 0.75 | no | spread too wide |  |
| 10-04 11:53:30 | SOL | up | 0.59→0.65 | 0.83 → 0.83 | no | edge gone |  |
| 10-04 11:53:08 | BTC | up | 0.57→0.64 | 0.61 → 0.69 | 3.41s | edge gone |  |
| 10-04 11:53:00 | ETH | down | 0.67→0.59 | 0.42 → 0.47 | 11.67s | edge gone |  |
| 10-04 11:52:54 | SOL | down | 0.69→0.59 | 0.24 → 0.22 | no | DOWN @ 0.22 | -0.49 / -0.73 / · |
| 10-04 11:52:42 | ETH | up | 0.59→0.65 | 0.54 → 0.65 | 14.18s | UP @ 0.65 | -1.14 / -1.67 / · |
| 10-04 11:52:39 | BTC | down | 0.64→0.55 | 0.32 → 0.43 | 17.43s | edge gone |  |
| 10-04 11:52:17 | NEAR | down | 0.24→0.18 | 0.85 → 0.84 | no | edge gone |  |
| 10-04 11:52:00 | SOL | down | 0.68→0.58 | 0.26 → 0.26 | no | DOWN @ 0.26 | -0.23 / -0.76 / · |
| 10-04 11:51:31 | SOL | down | 0.79→0.71 | 0.15 → 0.23 | 10.44s | DOWN @ 0.23 | -0.07 / -0.26 / · |
| 10-04 11:51:14 | NEAR | down | 0.27→0.22 | 0.66 → 0.75 | 12.70s | spread too wide |  |
| 10-04 11:50:57 | SOL | down | 0.84→0.76 | 0.10 → 0.10 | 29.96s | DOWN @ 0.10 | -0.21 / 0.43 / · |
| 10-04 11:50:23 | BTC | up | 0.57→0.66 | 0.58 → 0.70 | 18.97s | edge gone |  |
| 10-04 11:50:16 | XRP | down | 0.79→0.73 | 0.25 → 0.20 | no | DOWN @ 0.20 | -0.52 / -0.90 / · |
| 10-04 11:50:02 | DOGE | up | 0.58→0.66 | 0.75 → 0.77 | 9.72s | edge gone |  |
| 10-04 11:50:00 | XRP | up | 0.67→0.73 | 0.71 → 0.75 | 11.97s | edge gone |  |
| 10-04 11:49:59 | BTC | up | 0.43→0.56 | 0.44 → 0.57 | 12.47s | edge gone |  |
| 10-04 11:49:55 | SOL | down | 0.78→0.72 | 0.19 → 0.18 | no | DOWN @ 0.18 | -0.53 / -0.60 / · |
