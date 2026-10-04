# Lag Tracker

*Updated Sun Oct 04 13:15 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$286.27** | -29.3% | 275 | $3.49 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 302 | 53 | -$131.22 | -12.4% | -$64.13 / -$67.09 |
| Sell after 30 sec | 302 | 67 | -$156.59 | -14.8% | -$67.22 / -$89.37 |
| Hold to the close | 275 | 69 | -$286.27 | -29.3% | -$85.77 / -$200.50 |
| Hold, only edge 10¢+ | 95 | 14 | -$109.15 | -43.8% | -$77.54 / -$31.61 |
| Hold, first trade per window only | 97 | 31 | -$61.66 | -16.6% | -$10.15 / -$51.51 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 1137 | 11% | 65% | +5.0¢ | 0.3¢ | edge gone 778, price out of range 34, spread too wide 23 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 671 | 11.1s | 3% | 0% |
| BTC | 652 | 11.9s | 3% | 0% |
| DOGE | 792 | 10.6s | 2% | 0% |
| ETH | 815 | 11.1s | 4% | 0% |
| HYPE | 647 | 11.4s | 4% | 0% |
| NEAR | 822 | 10.8s | 4% | 0% |
| SOL | 1533 | 10.9s | 3% | 0% |
| XRP | 1517 | 11.0s | 4% | 0% |
| ZEC | 955 | 9.7s | 4% | 0% |
| **All** | **8404** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 13:13:43 | NEAR | down | 0.44→0.33 | 0.08 → 0.16 | 12.11s | spread too wide |  |
| 10-04 13:12:51 | BTC | up | 0.71→0.82 | 0.80 → 0.85 | 18.88s | edge gone |  |
| 10-04 13:12:32 | ZEC | up | 0.67→0.76 | 0.63 → 0.87 | 7.38s | spread too wide |  |
| 10-04 13:12:29 | BTC | up | 0.49→0.60 | 0.66 → 0.70 | 10.88s | edge gone |  |
| 10-04 13:12:10 | ETH | up | 0.89→0.94 | 0.87 → 0.95 | 0.37s | edge gone |  |
| 10-04 13:12:01 | SOL | down | 0.66→0.56 | 0.24 → 0.21 | no | DOWN @ 0.21 | -1.63 / -1.97 / · |
| 10-04 13:12:00 | ZEC | down | 0.60→0.47 | 0.43 → 0.42 | no | DOWN @ 0.42 | -0.65 / -2.69 / · |
| 10-04 13:11:59 | BNB | down | 0.82→0.61 | 0.08 → 0.05 | no | DOWN @ 0.05 | -0.43 / -0.21 / · |
| 10-04 13:11:46 | SOL | up | 0.55→0.78 | 0.77 → 0.77 | no | edge gone |  |
| 10-04 13:11:31 | SOL | down | 0.64→0.50 | 0.25 → 0.25 | no | DOWN @ 0.25 | -0.37 / -0.76 / · |
| 10-04 13:11:22 | NEAR | down | 0.58→0.50 | 0.21 → 0.26 | 3.15s | DOWN @ 0.28 | -0.54 / 0.19 / · |
| 10-04 13:10:59 | DOGE | down | 0.76→0.68 | 0.16 → 0.16 | no | DOWN @ 0.16 | -0.57 / -0.29 / · |
| 10-04 13:10:38 | SOL | down | 0.67→0.59 | 0.29 → 0.25 | no | DOWN @ 0.27 | -0.57 / -0.38 / · |
| 10-04 13:10:22 | XRP | up | 0.84→0.91 | 0.80 → 0.91 | 2.91s | edge gone |  |
| 10-04 13:10:19 | ETH | down | 0.71→0.64 | 0.34 → 0.25 | no | DOWN @ 0.25 | -0.85 / -0.95 / · |
| 10-04 13:10:17 | NEAR | down | 0.72→0.66 | 0.11 → 0.11 | 7.91s | DOWN @ 0.12 | 0.77 / 0.18 / · |
| 10-04 13:10:09 | SOL | up | 0.50→0.58 | 0.64 → 0.72 | 15.67s | edge gone |  |
| 10-04 13:10:05 | ZEC | down | 0.57→0.51 | 0.36 → 0.44 | 4.42s | DOWN @ 0.44 | -1.44 / -1.63 / · |
| 10-04 13:09:59 | XRP | down | 0.83→0.78 | 0.11 → 0.23 | 10.17s | edge gone |  |
| 10-04 13:09:59 | ETH | down | 0.73→0.59 | 0.24 → 0.39 | 10.67s | edge gone |  |
| 10-04 13:09:59 | BTC | down | 0.63→0.44 | 0.26 → 0.54 | 25.67s | edge gone |  |
| 10-04 13:09:58 | NEAR | up | 0.66→0.74 | 0.88 → 0.91 | no | edge gone |  |
| 10-04 13:09:54 | SOL | down | 0.54→0.47 | 0.38 → 0.38 | 15.67s | DOWN @ 0.38 | 0.05 / -1.61 / · |
| 10-04 13:09:39 | SOL | up | 0.47→0.54 | 0.61 → 0.63 | no | edge gone |  |
| 10-04 13:09:33 | NEAR | up | 0.43→0.58 | 0.74 → 0.84 | 6.18s | edge gone |  |
| 10-04 13:09:32 | XRP | down | 0.82→0.77 | 0.15 → 0.11 | no | DOWN @ 0.11 | -0.31 / 0.63 / · |
| 10-04 13:09:25 | ZEC | down | 0.67→0.58 | 0.19 → 0.35 | 14.43s | DOWN @ 0.36 | 0.52 / -0.41 / · |
| 10-04 13:09:24 | SOL | down | 0.54→0.47 | 0.43 → 0.38 | no | DOWN @ 0.38 | -0.44 / -0.63 / · |
| 10-04 13:09:18 | NEAR | up | 0.43→0.48 | 0.82 → 0.74 | no | edge gone |  |
| 10-04 13:09:07 | SOL | down | 0.57→0.47 | 0.48 → 0.44 | no | DOWN @ 0.44 | -0.75 / -1.05 / · |
