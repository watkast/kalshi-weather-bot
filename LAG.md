# Lag Tracker

*Updated Sun Oct 04 13:35 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$386.48** | -33.7% | 321 | $3.61 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 326 | 56 | -$140.54 | -12.0% | -$69.97 / -$70.57 |
| Sell after 30 sec | 326 | 74 | -$163.91 | -14.0% | -$70.80 / -$93.11 |
| Hold to the close | 321 | 76 | -$386.48 | -33.7% | -$117.12 / -$269.36 |
| Hold, only edge 10¢+ | 116 | 16 | -$146.61 | -47.8% | -$103.97 / -$42.64 |
| Hold, first trade per window only | 112 | 34 | -$91.10 | -21.1% | -$18.55 / -$72.55 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 1238 | 11% | 65% | +5.0¢ | 0.3¢ | edge gone 850, price out of range 35, spread too wide 26 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 675 | 11.0s | 3% | 0% |
| BTC | 664 | 11.9s | 3% | 0% |
| DOGE | 799 | 10.5s | 3% | 0% |
| ETH | 822 | 11.2s | 4% | 0% |
| HYPE | 649 | 11.4s | 4% | 0% |
| NEAR | 830 | 10.8s | 4% | 0% |
| SOL | 1552 | 10.9s | 3% | 0% |
| XRP | 1547 | 10.9s | 4% | 0% |
| ZEC | 967 | 9.7s | 4% | 0% |
| **All** | **8505** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 13:35:33 | ETH | down | 0.56→0.46 | 0.44 → 0.62 | no | edge gone |  |
| 10-04 13:35:31 | BTC | down | 0.79→0.73 | 0.23 → 0.30 | no | edge gone |  |
| 10-04 13:35:26 | BNB | down | 0.23→0.16 | 0.69 → 0.68 | no | DOWN @ 0.70 | · / · / · |
| 10-04 13:35:20 | XRP | down | 0.74→0.67 | 0.35 → 0.31 | no | edge gone |  |
| 10-04 13:35:08 | ZEC | down | 0.60→0.52 | 0.44 → 0.44 | no | spread too wide |  |
| 10-04 13:35:05 | XRP | down | 0.74→0.67 | 0.27 → 0.35 | 0.78s | edge gone |  |
| 10-04 13:34:50 | XRP | down | 0.76→0.67 | 0.28 → 0.34 | 16.04s | edge gone |  |
| 10-04 13:34:26 | XRP | up | 0.70→0.78 | 0.74 → 0.74 | no | edge gone |  |
| 10-04 13:34:15 | SOL | down | 0.91→0.85 | 0.16 → 0.17 | no | edge gone |  |
| 10-04 13:33:46 | DOGE | up | 0.68→0.73 | 0.79 → 0.86 | 5.03s | edge gone |  |
| 10-04 13:33:36 | SOL | up | 0.89→0.94 | 0.86 → 0.86 | no | UP @ 0.86 | -0.49 / -0.28 / · |
| 10-04 13:33:24 | NEAR | down | 0.53→0.47 | 0.31 → 0.31 | 11.04s | DOWN @ 0.31 | 0.17 / 0.18 / · |
| 10-04 13:33:19 | XRP | up | 0.66→0.77 | 0.74 → 0.74 | no | edge gone |  |
| 10-04 13:32:55 | BNB | up | 0.34→0.40 | 0.45 → 0.40 | no | edge gone |  |
| 10-04 13:32:52 | XRP | up | 0.61→0.66 | 0.71 → 0.71 | 13.03s | edge gone |  |
| 10-04 13:32:25 | XRP | down | 0.66→0.61 | 0.30 → 0.34 | 11.29s | DOWN @ 0.34 | -0.81 / -0.71 / · |
| 10-04 13:32:05 | NEAR | down | 0.55→0.50 | 0.29 → 0.29 | 16.04s | DOWN @ 0.32 | -0.38 / 0.10 / · |
| 10-04 13:32:00 | BTC | up | 0.69→0.74 | 0.70 → 0.71 | 21.29s | edge gone |  |
| 10-04 13:31:47 | ZEC | up | 0.71→0.77 | 0.80 → 0.80 | no | edge gone |  |
| 10-04 13:31:42 | XRP | up | 0.72→0.78 | 0.76 → 0.77 | no | edge gone |  |
| 10-04 13:31:19 | ETH | up | 0.66→0.71 | 0.67 → 0.74 | 1.79s | edge gone |  |
| 10-04 13:31:17 | HYPE | down | 0.33→0.26 | 0.63 → 0.64 | 18.54s | DOWN @ 0.64 | -0.44 / 0.59 / · |
| 10-04 13:31:17 | ZEC | up | 0.65→0.71 | 0.65 → 0.77 | 3.79s | edge gone |  |
| 10-04 13:31:11 | XRP | up | 0.65→0.77 | 0.56 → 0.75 | 9.54s | edge gone |  |
| 10-04 13:27:53 | SOL | up | 0.34→0.79 | 0.52 → 0.76 | 14.85s | edge gone |  |
| 10-04 13:27:38 | SOL | down | 0.29→0.18 | 0.71 → 0.74 | no | DOWN @ 0.74 | -2.72 / -7.10 / -7.54 |
| 10-04 13:27:23 | SOL | up | 0.24→0.30 | 0.35 → 0.34 | 0.33s | edge gone |  |
| 10-04 13:27:22 | ZEC | up | 0.02→0.08 | 0.01 → 0.07 | 15.60s | edge gone |  |
| 10-04 13:27:08 | SOL | down | 0.31→0.26 | 0.73 → 0.76 | 0.34s | edge gone |  |
| 10-04 13:27:03 | DOGE | down | 0.76→0.71 | 0.32 → 0.29 | no | edge gone |  |
