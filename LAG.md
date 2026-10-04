# Lag Tracker

*Updated Sun Oct 04 13:05 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$286.27** | -29.3% | 275 | $3.56 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 279 | 50 | -$120.15 | -12.1% | -$55.75 / -$64.40 |
| Sell after 30 sec | 279 | 62 | -$141.15 | -14.2% | -$59.39 / -$81.76 |
| Hold to the close | 275 | 69 | -$286.27 | -29.3% | -$85.77 / -$200.50 |
| Hold, only edge 10¢+ | 95 | 14 | -$109.15 | -43.8% | -$77.54 / -$31.61 |
| Hold, first trade per window only | 97 | 31 | -$61.66 | -16.6% | -$10.15 / -$51.51 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 1084 | 11% | 65% | +5.0¢ | 0.3¢ | edge gone 750, price out of range 34, spread too wide 21 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 670 | 11.0s | 3% | 0% |
| BTC | 645 | 11.9s | 3% | 0% |
| DOGE | 790 | 10.6s | 2% | 0% |
| ETH | 809 | 11.1s | 4% | 0% |
| HYPE | 647 | 11.4s | 4% | 0% |
| NEAR | 814 | 10.8s | 4% | 0% |
| SOL | 1518 | 10.8s | 3% | 0% |
| XRP | 1509 | 11.0s | 4% | 0% |
| ZEC | 949 | 9.7s | 4% | 0% |
| **All** | **8351** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 13:05:08 | BNB | up | 0.43→0.49 | 0.73 → 0.75 | no | edge gone |  |
| 10-04 13:05:04 | NEAR | up | 0.64→0.69 | 0.81 → 0.87 | 5.86s | edge gone |  |
| 10-04 13:04:57 | BTC | up | 0.42→0.50 | 0.42 → 0.48 | 12.62s | edge gone |  |
| 10-04 13:04:56 | ETH | up | 0.37→0.42 | 0.40 → 0.40 | 13.12s | edge gone |  |
| 10-04 13:04:54 | XRP | up | 0.63→0.68 | 0.73 → 0.67 | no | edge gone |  |
| 10-04 13:04:50 | HYPE | up | 0.65→0.71 | 0.74 → 0.80 | 4.62s | edge gone |  |
| 10-04 13:04:23 | XRP | up | 0.62→0.70 | 0.62 → 0.73 | 16.63s | edge gone |  |
| 10-04 13:04:23 | ZEC | down | 0.72→0.67 | 0.25 → 0.31 | 1.87s | edge gone |  |
| 10-04 13:04:19 | ETH | down | 0.46→0.38 | 0.56 → 0.65 | 20.63s | edge gone |  |
| 10-04 13:03:35 | NEAR | up | 0.62→0.72 | 0.78 → 0.85 | 19.89s | edge gone |  |
| 10-04 13:03:30 | ETH | up | 0.34→0.43 | 0.40 → 0.44 | 24.64s | edge gone |  |
| 10-04 13:03:20 | BNB | down | 0.54→0.46 | 0.24 → 0.23 | no | DOWN @ 0.29 | -1.00 / -1.23 / · |
| 10-04 13:03:02 | SOL | up | 0.27→0.37 | 0.29 → 0.36 | 7.90s | edge gone |  |
| 10-04 13:03:02 | DOGE | up | 0.45→0.52 | 0.51 → 0.60 | 7.90s | edge gone |  |
| 10-04 13:03:02 | ZEC | up | 0.75→0.80 | 0.80 → 0.85 | 7.90s | edge gone |  |
| 10-04 13:02:43 | DOGE | down | 0.52→0.45 | 0.40 → 0.49 | 11.65s | DOWN @ 0.49 | -0.46 / -1.25 / · |
| 10-04 13:02:40 | BTC | down | 0.51→0.42 | 0.48 → 0.57 | 14.41s | edge gone |  |
| 10-04 13:02:40 | NEAR | down | 0.74→0.67 | 0.15 → 0.22 | no | DOWN @ 0.26 | -1.37 / -0.99 / · |
| 10-04 13:02:35 | XRP | up | 0.55→0.61 | 0.54 → 0.64 | 4.66s | edge gone |  |
| 10-04 13:02:28 | SOL | down | 0.41→0.35 | 0.64 → 0.66 | 11.91s | edge gone |  |
| 10-04 13:02:25 | ETH | up | 0.48→0.54 | 0.46 → 0.52 | 15.41s | edge gone |  |
| 10-04 13:02:20 | XRP | up | 0.50→0.57 | 0.58 → 0.55 | no | edge gone |  |
| 10-04 13:02:05 | XRP | down | 0.55→0.48 | 0.48 → 0.46 | no | DOWN @ 0.46 | -0.46 / -1.35 / · |
| 10-04 13:01:47 | XRP | down | 0.57→0.48 | 0.48 → 0.48 | no | edge gone |  |
| 10-04 13:01:30 | ETH | down | 0.60→0.52 | 0.42 → 0.49 | 9.67s | edge gone |  |
| 10-04 13:01:30 | SOL | down | 0.48→0.42 | 0.52 → 0.59 | 10.17s | edge gone |  |
| 10-04 13:01:27 | XRP | down | 0.61→0.54 | 0.42 → 0.46 | 12.67s | edge gone |  |
| 10-04 13:01:10 | XRP | up | 0.52→0.63 | 0.56 → 0.60 | no | edge gone |  |
| 10-04 13:00:55 | XRP | up | 0.48→0.54 | 0.44 → 0.50 | 10.43s | edge gone |  |
| 10-04 13:00:38 | XRP | down | 0.48→0.38 | 0.58 → 0.58 | no | edge gone |  |
