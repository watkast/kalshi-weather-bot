# Lag Tracker

*Updated Sun Oct 04 15:05 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$344.20** | -21.2% | 450 | $3.64 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 459 | 78 | -$188.25 | -11.3% | -$99.66 / -$88.59 |
| Sell after 30 sec | 456 | 108 | -$219.40 | -13.3% | -$106.49 / -$112.91 |
| Hold to the close | 450 | 128 | -$344.20 | -21.2% | -$211.19 / -$133.01 |
| Hold, only edge 10¢+ | 157 | 29 | -$132.17 | -31.3% | -$97.39 / -$34.78 |
| Hold, first trade per window only | 153 | 52 | -$102.33 | -16.4% | -$32.95 / -$69.38 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 1730 | 10% | 66% | +4.3¢ | 0.3¢ | edge gone 1181, price out of range 49, spread too wide 41 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 679 | 11.1s | 3% | 0% |
| BTC | 739 | 11.8s | 3% | 0% |
| DOGE | 834 | 10.6s | 3% | 0% |
| ETH | 881 | 11.0s | 4% | 0% |
| HYPE | 676 | 11.6s | 3% | 0% |
| NEAR | 872 | 10.8s | 4% | 0% |
| SOL | 1635 | 11.0s | 3% | 0% |
| XRP | 1659 | 11.0s | 3% | 0% |
| ZEC | 1022 | 9.6s | 4% | 0% |
| **All** | **8997** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **19 ms** · Order book check: **23 ms** · Coinbase price delay: **8 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 15:05:08 | ETH | down | 0.78→0.72 | 0.28 → 0.30 | no | edge gone |  |
| 10-04 15:05:07 | SOL | down | 0.57→0.48 | 0.39 → 0.47 | no | DOWN @ 0.47 | -0.46 / · / · |
| 10-04 15:05:05 | NEAR | down | 0.47→0.41 | 0.39 → 0.43 | no | DOWN @ 0.45 | 0.30 / · / · |
| 10-04 15:04:52 | SOL | down | 0.64→0.46 | 0.32 → 0.52 | no | edge gone |  |
| 10-04 15:04:50 | NEAR | down | 0.42→0.36 | 0.37 → 0.47 | no | DOWN @ 0.47 | -1.25 / · / · |
| 10-04 15:04:45 | BTC | down | 0.89→0.83 | 0.13 → 0.23 | 3.96s | edge gone |  |
| 10-04 15:04:40 | ZEC | down | 0.87→0.82 | 0.15 → 0.13 | no | edge gone |  |
| 10-04 15:04:40 | ETH | down | 0.88→0.81 | 0.14 → 0.22 | 8.97s | edge gone |  |
| 10-04 15:04:37 | SOL | down | 0.88→0.80 | 0.20 → 0.22 | 12.22s | edge gone |  |
| 10-04 15:04:31 | NEAR | down | 0.58→0.52 | 0.48 → 0.33 | no | DOWN @ 0.33 | -0.17 / 0.17 / · |
| 10-04 15:04:14 | ZEC | up | 0.68→0.75 | 0.73 → 0.85 | 4.97s | edge gone |  |
| 10-04 15:04:13 | BNB | up | 0.61→0.75 | 0.80 → 0.90 | 20.72s | edge gone |  |
| 10-04 15:04:13 | SOL | up | 0.76→0.81 | 0.72 → 0.79 | 20.97s | edge gone |  |
| 10-04 15:04:13 | ETH | up | 0.78→0.89 | 0.78 → 0.86 | 5.97s | edge gone |  |
| 10-04 15:04:13 | NEAR | up | 0.41→0.49 | 0.50 → 0.65 | 5.97s | edge gone |  |
| 10-04 15:04:05 | XRP | up | 0.73→0.80 | 0.79 → 0.86 | 0.46s | edge gone |  |
| 10-04 15:03:57 | ETH | up | 0.70→0.76 | 0.73 → 0.76 | 7.22s | edge gone |  |
| 10-04 15:03:56 | BTC | up | 0.81→0.86 | 0.73 → 0.77 | 8.23s | UP @ 0.77 | 0.37 / 0.68 / · |
| 10-04 15:03:55 | SOL | down | 0.72→0.65 | 0.28 → 0.33 | no | edge gone |  |
| 10-04 15:03:51 | HYPE | down | 0.47→0.40 | 0.56 → 0.57 | no | edge gone |  |
| 10-04 15:03:49 | XRP | down | 0.69→0.64 | 0.30 → 0.28 | no | DOWN @ 0.28 | -1.02 / -2.35 / · |
| 10-04 15:03:36 | NEAR | down | 0.51→0.35 | 0.50 → 0.52 | no | DOWN @ 0.52 | -0.66 / -1.61 / · |
| 10-04 15:03:27 | XRP | up | 0.65→0.71 | 0.64 → 0.75 | 6.48s | edge gone |  |
| 10-04 15:03:22 | ZEC | down | 0.64→0.56 | 0.46 → 0.46 | no | edge gone |  |
| 10-04 15:03:13 | NEAR | up | 0.40→0.46 | 0.54 → 0.60 | 5.99s | edge gone |  |
| 10-04 15:03:11 | ETH | up | 0.68→0.73 | 0.63 → 0.69 | 7.74s | edge gone |  |
| 10-04 15:03:07 | XRP | up | 0.50→0.58 | 0.53 → 0.60 | 11.99s | edge gone |  |
| 10-04 15:03:02 | BTC | up | 0.63→0.70 | 0.59 → 0.61 | 17.24s | UP @ 0.61 | 0.48 / 0.78 / · |
| 10-04 15:02:38 | XRP | up | 0.44→0.50 | 0.41 → 0.53 | 11.00s | edge gone |  |
| 10-04 15:02:29 | BTC | down | 0.70→0.63 | 0.47 → 0.43 | 5.00s | edge gone |  |
