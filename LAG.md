# Lag Tracker

*Updated Sun Oct 04 12:55 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$281.46** | -29.9% | 265 | $3.55 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 275 | 50 | -$116.86 | -12.0% | -$55.43 / -$61.43 |
| Sell after 30 sec | 274 | 62 | -$136.19 | -14.0% | -$57.32 / -$78.87 |
| Hold to the close | 265 | 66 | -$281.46 | -29.9% | -$76.55 / -$204.91 |
| Hold, only edge 10¢+ | 92 | 12 | -$118.61 | -49.7% | -$75.91 / -$42.70 |
| Hold, first trade per window only | 92 | 30 | -$57.80 | -16.2% | -$8.80 / -$49.00 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 1049 | 11% | 64% | +4.7¢ | 0.3¢ | edge gone 721, price out of range 33, spread too wide 20 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 666 | 11.0s | 3% | 0% |
| BTC | 643 | 11.9s | 3% | 0% |
| DOGE | 787 | 10.6s | 2% | 0% |
| ETH | 804 | 11.0s | 4% | 0% |
| HYPE | 646 | 11.4s | 4% | 0% |
| NEAR | 809 | 10.8s | 4% | 0% |
| SOL | 1515 | 10.9s | 3% | 0% |
| XRP | 1499 | 11.0s | 4% | 0% |
| ZEC | 947 | 9.7s | 4% | 0% |
| **All** | **8316** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 12:55:14 | NEAR | down | 0.41→0.31 | 0.62 → 0.59 | no | spread too wide |  |
| 10-04 12:55:13 | ZEC | up | 0.18→0.23 | 0.12 → 0.22 | 1.75s | edge gone |  |
| 10-04 12:54:56 | DOGE | up | 0.13→0.19 | 0.07 → 0.11 | 18.75s | UP @ 0.11 | 0.43 / · / · |
| 10-04 12:54:30 | XRP | down | 0.14→0.08 | 0.87 → 0.96 | 15.01s | price out of range |  |
| 10-04 12:54:22 | NEAR | down | 0.37→0.32 | 0.44 → 0.48 | 7.78s | DOWN @ 0.48 | 0.34 / 1.05 / · |
| 10-04 12:54:15 | XRP | down | 0.24→0.18 | 0.87 → 0.89 | 0.01s | edge gone |  |
| 10-04 12:54:06 | ZEC | down | 0.28→0.22 | 0.69 → 0.80 | 8.51s | edge gone |  |
| 10-04 12:53:58 | XRP | down | 0.33→0.27 | 0.76 → 0.80 | 16.77s | edge gone |  |
| 10-04 12:53:57 | ETH | down | 0.12→0.06 | 0.94 → 0.94 | 17.52s | edge gone |  |
| 10-04 12:53:40 | SOL | down | 0.14→0.08 | 0.95 → 0.95 | no | edge gone |  |
| 10-04 12:53:40 | ZEC | down | 0.38→0.28 | 0.54 → 0.74 | 5.27s | edge gone |  |
| 10-04 12:53:35 | DOGE | down | 0.41→0.32 | 0.74 → 0.75 | 24.55s | edge gone |  |
| 10-04 12:53:26 | ETH | down | 0.14→0.07 | 0.92 → 0.93 | no | edge gone |  |
| 10-04 12:52:43 | XRP | down | 0.38→0.32 | 0.74 → 0.73 | no | edge gone |  |
| 10-04 12:52:27 | ZEC | up | 0.42→0.48 | 0.45 → 0.48 | 17.79s | edge gone |  |
| 10-04 12:52:23 | XRP | up | 0.30→0.35 | 0.26 → 0.38 | no | edge gone |  |
| 10-04 12:51:13 | SOL | up | 0.20→0.26 | 0.24 → 0.23 | no | edge gone |  |
| 10-04 12:51:10 | ZEC | down | 0.52→0.46 | 0.47 → 0.56 | 20.04s | edge gone |  |
| 10-04 12:51:06 | BTC | down | 0.25→0.19 | 0.78 → 0.84 | 8.78s | edge gone |  |
| 10-04 12:51:01 | HYPE | up | 0.06→0.12 | 0.11 → 0.08 | no | edge gone |  |
| 10-04 12:50:41 | XRP | down | 0.37→0.32 | 0.68 → 0.67 | no | edge gone |  |
| 10-04 12:50:37 | HYPE | up | 0.11→0.16 | 0.11 → 0.09 | no | UP @ 0.09 | 0.02 / -0.26 / · |
| 10-04 12:50:30 | SOL | up | 0.18→0.34 | 0.18 → 0.19 | no | UP @ 0.20 | -0.03 / 0.07 / · |
| 10-04 12:50:25 | BTC | up | 0.19→0.25 | 0.17 → 0.23 | 19.54s | edge gone |  |
| 10-04 12:50:06 | ZEC | up | 0.53→0.64 | 0.75 → 0.67 | no | spread too wide |  |
| 10-04 12:49:41 | SOL | down | 0.26→0.21 | 0.78 → 0.80 | 18.79s | edge gone |  |
| 10-04 12:49:39 | BNB | up | 0.35→0.44 | 0.63 → 0.72 | 6.03s | edge gone |  |
| 10-04 12:49:22 | SOL | up | 0.20→0.27 | 0.25 → 0.22 | no | UP @ 0.22 | -0.35 / -0.64 / · |
| 10-04 12:48:52 | ZEC | up | 0.51→0.57 | 0.51 → 0.55 | 8.03s | edge gone |  |
| 10-04 12:48:20 | ETH | down | 0.24→0.15 | 0.75 → 0.79 | 24.79s | DOWN @ 0.79 | -0.24 / -0.45 / · |
