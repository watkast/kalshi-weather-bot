# Lag Tracker

*Updated Sun Oct 04 19:16 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$274.14** | -8.0% | 892 | $3.85 | $161.50 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 894 | 140 | -$399.53 | -11.6% | -$182.28 / -$217.25 |
| Sell after 30 sec | 892 | 226 | -$417.61 | -12.2% | -$211.74 / -$205.87 |
| Hold to the close | 892 | 316 | -$274.14 | -8.0% | -$333.87 / $59.73 |
| Hold, only edge 10¢+ | 321 | 84 | -$128.44 | -13.3% | -$115.89 / -$12.55 |
| Hold, first trade per window only | 277 | 110 | -$44.04 | -3.8% | -$86.61 / $42.57 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 3287 | 10% | 66% | +4.0¢ | 0.3¢ | edge gone 2229, price out of range 93, spread too wide 71 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 739 | 11.1s | 3% | 0% |
| BTC | 892 | 11.9s | 3% | 0% |
| DOGE | 970 | 10.9s | 3% | 0% |
| ETH | 1093 | 10.9s | 4% | 0% |
| HYPE | 736 | 11.6s | 3% | 0% |
| NEAR | 1061 | 10.8s | 4% | 0% |
| SOL | 1923 | 10.9s | 3% | 0% |
| XRP | 1987 | 11.1s | 3% | 0% |
| ZEC | 1153 | 9.6s | 4% | 0% |
| **All** | **10554** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **9 ms** · Order book check: **27 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 19:16:45 | XRP | down | 0.78→0.68 | 0.26 → 0.31 | no | edge gone |  |
| 10-04 19:16:31 | BNB | down | 0.35→0.24 | 0.41 → 0.44 | no | DOWN @ 0.44 | -0.75 / · / · |
| 10-04 19:16:23 | NEAR | down | 0.72→0.66 | 0.24 → 0.25 | 9.75s | DOWN @ 0.26 | 0.11 / · / · |
| 10-04 19:16:20 | SOL | down | 0.56→0.50 | 0.51 → 0.51 | 27.75s | edge gone |  |
| 10-04 19:16:20 | ZEC | down | 0.57→0.45 | 0.44 → 0.52 | 13.00s | edge gone |  |
| 10-04 19:13:35 | ETH | down | 0.99→0.85 | 0.07 → 0.07 | no | DOWN @ 0.09 | -0.67 / -0.72 / -0.92 |
| 10-04 19:12:42 | ZEC | up | 0.19→0.31 | 0.22 → 0.30 | 7.27s | edge gone |  |
| 10-04 19:12:31 | SOL | down | 0.95→0.90 | 0.04 → 0.04 | no | price out of range |  |
| 10-04 19:12:30 | NEAR | down | 0.16→0.10 | 0.80 → 0.88 | 18.78s | spread too wide |  |
| 10-04 19:12:06 | NEAR | down | 0.34→0.16 | 0.77 → 0.80 | 0.01s | edge gone |  |
| 10-04 19:12:00 | ZEC | down | 0.45→0.33 | 0.53 → 0.63 | 18.54s | edge gone |  |
| 10-04 19:11:51 | NEAR | up | 0.17→0.33 | 0.51 → 0.34 | no | edge gone |  |
| 10-04 19:11:32 | NEAR | up | 0.39→0.45 | 0.72 → 0.65 | no | edge gone |  |
| 10-04 19:11:11 | HYPE | down | 0.82→0.71 | 0.18 → 0.18 | no | DOWN @ 0.19 | -0.95 / -0.95 / -1.98 |
| 10-04 19:11:10 | NEAR | up | 0.49→0.60 | 0.71 → 0.72 | no | edge gone |  |
| 10-04 19:10:56 | ETH | up | 0.81→0.91 | 0.76 → 0.87 | 7.52s | edge gone |  |
| 10-04 19:10:48 | SOL | up | 0.85→0.90 | 0.88 → 0.91 | 15.78s | edge gone |  |
| 10-04 19:10:40 | ETH | up | 0.72→0.80 | 0.60 → 0.73 | 9.02s | UP @ 0.73 | -0.18 / -0.18 / 2.56 |
| 10-04 19:10:37 | NEAR | up | 0.47→0.55 | 0.67 → 0.74 | 12.02s | edge gone |  |
| 10-04 19:10:29 | SOL | down | 0.87→0.77 | 0.09 → 0.14 | no | DOWN @ 0.14 | -0.56 / -0.95 / -1.49 |
| 10-04 19:10:24 | ZEC | down | 0.69→0.61 | 0.26 → 0.34 | 9.52s | edge gone |  |
| 10-04 19:10:19 | NEAR | down | 0.61→0.54 | 0.19 → 0.23 | 0.02s | DOWN @ 0.23 | 0.56 / 0.32 / 7.57 |
| 10-04 19:10:04 | SOL | down | 0.88→0.83 | 0.09 → 0.10 | 30.28s | DOWN @ 0.10 | -0.22 / 0.16 / -1.06 |
| 10-04 19:09:40 | HYPE | up | 0.67→0.81 | 0.69 → 0.78 | 9.02s | edge gone |  |
| 10-04 19:09:38 | NEAR | down | 0.69→0.62 | 0.20 → 0.25 | no | DOWN @ 0.25 | -1.14 / -1.33 / 7.36 |
| 10-04 19:09:31 | SOL | up | 0.81→0.87 | 0.87 → 0.90 | 18.03s | edge gone |  |
| 10-04 19:09:26 | ZEC | up | 0.57→0.64 | 0.67 → 0.65 | 22.53s | edge gone |  |
| 10-04 19:09:12 | ETH | down | 0.67→0.61 | 0.48 → 0.45 | no | edge gone |  |
| 10-04 19:09:10 | SOL | up | 0.73→0.80 | 0.79 → 0.85 | 9.28s | edge gone |  |
| 10-04 19:09:07 | HYPE | up | 0.34→0.50 | 0.52 → 0.76 | 12.03s | edge gone |  |
