# Lag Tracker

*Updated Sun Oct 04 14:35 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$346.56** | -23.5% | 408 | $3.61 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 415 | 70 | -$171.02 | -11.4% | -$94.72 / -$76.30 |
| Sell after 30 sec | 415 | 97 | -$197.95 | -13.2% | -$97.47 / -$100.48 |
| Hold to the close | 408 | 113 | -$346.56 | -23.5% | -$221.49 / -$125.07 |
| Hold, only edge 10¢+ | 144 | 26 | -$129.86 | -33.3% | -$117.30 / -$12.56 |
| Hold, first trade per window only | 140 | 47 | -$89.59 | -16.0% | -$36.59 / -$53.00 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 1558 | 10% | 65% | +4.0¢ | 0.3¢ | edge gone 1064, price out of range 46, spread too wide 33 |

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
| BTC | 720 | 11.9s | 3% | 0% |
| DOGE | 819 | 10.5s | 3% | 0% |
| ETH | 859 | 11.2s | 4% | 0% |
| HYPE | 665 | 11.6s | 3% | 0% |
| NEAR | 852 | 10.8s | 4% | 0% |
| SOL | 1607 | 10.9s | 3% | 0% |
| XRP | 1628 | 11.0s | 3% | 0% |
| ZEC | 999 | 9.6s | 4% | 0% |
| **All** | **8825** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 14:35:44 | BTC | up | 0.47→0.55 | 0.41 → 0.61 | 4.04s | edge gone |  |
| 10-04 14:35:43 | ETH | up | 0.76→0.81 | 0.80 → 0.89 | 4.79s | edge gone |  |
| 10-04 14:35:35 | SOL | up | 0.70→0.77 | 0.79 → 0.82 | 12.29s | edge gone |  |
| 10-04 14:35:34 | XRP | up | 0.69→0.76 | 0.83 → 0.87 | 13.79s | edge gone |  |
| 10-04 14:35:26 | BTC | down | 0.52→0.46 | 0.42 → 0.59 | 6.28s | edge gone |  |
| 10-04 14:35:05 | XRP | up | 0.66→0.72 | 0.78 → 0.82 | 12.53s | edge gone |  |
| 10-04 14:35:02 | NEAR | up | 0.54→0.68 | 0.65 → 0.82 | 16.04s | edge gone |  |
| 10-04 14:34:56 | SOL | down | 0.76→0.68 | 0.24 → 0.21 | no | DOWN @ 0.21 | -0.61 / -0.24 / · |
| 10-04 14:34:48 | XRP | down | 0.68→0.62 | 0.27 → 0.25 | no | DOWN @ 0.25 | -0.18 / -0.85 / · |
| 10-04 14:34:30 | XRP | down | 0.71→0.66 | 0.20 → 0.22 | 17.54s | DOWN @ 0.25 | -0.28 / -0.35 / · |
| 10-04 14:33:50 | XRP | up | 0.64→0.70 | 0.81 → 0.79 | no | edge gone |  |
| 10-04 14:33:40 | SOL | down | 0.70→0.63 | 0.28 → 0.35 | 8.05s | edge gone |  |
| 10-04 14:33:33 | BTC | up | 0.51→0.57 | 0.53 → 0.63 | no | edge gone |  |
| 10-04 14:33:31 | XRP | up | 0.67→0.73 | 0.85 → 0.82 | no | edge gone |  |
| 10-04 14:33:26 | DOGE | down | 0.77→0.71 | 0.23 → 0.21 | 21.56s | DOWN @ 0.21 | -0.15 / 0.14 / · |
| 10-04 14:33:22 | ZEC | down | 0.76→0.71 | 0.29 → 0.31 | 25.56s | edge gone |  |
| 10-04 14:33:17 | SOL | down | 0.73→0.66 | 0.26 → 0.30 | 30.81s | edge gone |  |
| 10-04 14:33:00 | ZEC | up | 0.64→0.69 | 0.77 → 0.79 | no | spread too wide |  |
| 10-04 14:32:56 | DOGE | up | 0.62→0.69 | 0.80 → 0.73 | no | edge gone |  |
| 10-04 14:32:56 | BTC | down | 0.58→0.47 | 0.38 → 0.54 | 6.81s | edge gone |  |
| 10-04 14:32:56 | NEAR | up | 0.35→0.41 | 0.52 → 0.53 | 22.06s | edge gone |  |
| 10-04 14:32:55 | XRP | up | 0.58→0.69 | 0.85 → 0.77 | no | edge gone |  |
| 10-04 14:32:55 | ETH | down | 0.58→0.52 | 0.38 → 0.55 | 7.81s | edge gone |  |
| 10-04 14:32:51 | SOL | up | 0.71→0.77 | 0.79 → 0.83 | no | edge gone |  |
| 10-04 14:32:41 | BTC | up | 0.57→0.62 | 0.56 → 0.65 | 6.81s | edge gone |  |
| 10-04 14:32:41 | HYPE | up | 0.82→0.87 | 0.85 → 0.89 | 22.07s | edge gone |  |
| 10-04 14:32:07 | DOGE | up | 0.74→0.86 | 0.78 → 0.81 | no | UP @ 0.81 | -0.12 / -0.33 / · |
| 10-04 14:31:58 | ZEC | up | 0.73→0.79 | 0.69 → 0.80 | 4.82s | edge gone |  |
| 10-04 14:31:55 | XRP | down | 0.65→0.59 | 0.25 → 0.24 | no | DOWN @ 0.24 | -0.65 / -0.93 / · |
| 10-04 14:31:49 | DOGE | up | 0.66→0.74 | 0.70 → 0.77 | 0.31s | edge gone |  |
