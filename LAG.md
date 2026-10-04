# Lag Tracker

*Updated Sun Oct 04 20:25 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$220.37** | -5.6% | 992 | $3.96 | $185.87 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1006 | 160 | -$443.99 | -11.2% | -$207.11 / -$236.88 |
| Sell after 30 sec | 1006 | 256 | -$477.22 | -12.0% | -$233.66 / -$243.56 |
| Hold to the close | 992 | 371 | -$220.37 | -5.6% | -$349.18 / $128.81 |
| Hold, only edge 10¢+ | 350 | 95 | -$157.75 | -14.2% | -$107.20 / -$50.55 |
| Hold, first trade per window only | 307 | 125 | -$38.28 | -3.0% | -$102.33 / $64.05 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 3722 | 10% | 65% | +4.0¢ | 0.3¢ | edge gone 2537, price out of range 98, spread too wide 81 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 755 | 11.1s | 3% | 0% |
| BTC | 941 | 11.9s | 3% | 0% |
| DOGE | 1013 | 10.9s | 3% | 0% |
| ETH | 1143 | 10.8s | 4% | 0% |
| HYPE | 768 | 11.6s | 3% | 0% |
| NEAR | 1100 | 10.8s | 4% | 0% |
| SOL | 1991 | 10.9s | 3% | 0% |
| XRP | 2073 | 11.0s | 3% | 0% |
| ZEC | 1205 | 9.7s | 4% | 0% |
| **All** | **10989** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **7 ms** · Order book check: **28 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 20:24:38 | DOGE | up | 0.90→0.97 | 0.96 → 0.95 | no | edge gone |  |
| 10-04 20:24:31 | SOL | up | 0.54→0.61 | 0.65 → 0.66 | 22.53s | edge gone |  |
| 10-04 20:24:24 | XRP | down | 0.29→0.23 | 0.81 → 0.81 | 0.26s | edge gone |  |
| 10-04 20:24:16 | SOL | up | 0.54→0.64 | 0.65 → 0.65 | no | edge gone |  |
| 10-04 20:23:59 | SOL | down | 0.60→0.50 | 0.38 → 0.36 | no | DOWN @ 0.36 | -0.53 / -0.58 / · |
| 10-04 20:23:58 | XRP | down | 0.39→0.34 | 0.67 → 0.63 | 26.03s | edge gone |  |
| 10-04 20:23:49 | ZEC | down | 0.18→0.10 | 0.89 → 0.90 | no | edge gone |  |
| 10-04 20:23:44 | NEAR | down | 0.85→0.78 | 0.08 → 0.11 | 9.28s | DOWN @ 0.12 | -0.11 / -0.26 / · |
| 10-04 20:23:42 | XRP | up | 0.37→0.42 | 0.46 → 0.41 | no | edge gone |  |
| 10-04 20:23:39 | SOL | down | 0.63→0.57 | 0.39 → 0.39 | no | edge gone |  |
| 10-04 20:23:20 | SOL | up | 0.53→0.60 | 0.59 → 0.62 | 18.78s | edge gone |  |
| 10-04 20:23:09 | XRP | down | 0.47→0.38 | 0.59 → 0.54 | no | DOWN @ 0.54 | -0.49 / 0.15 / · |
| 10-04 20:23:07 | ZEC | down | 0.20→0.12 | 0.82 → 0.90 | 1.27s | edge gone |  |
| 10-04 20:23:05 | SOL | down | 0.59→0.53 | 0.27 → 0.44 | 3.77s | edge gone |  |
| 10-04 20:22:54 | XRP | up | 0.43→0.55 | 0.45 → 0.53 | no | edge gone |  |
| 10-04 20:22:47 | SOL | up | 0.65→0.71 | 0.69 → 0.74 | 6.77s | edge gone |  |
| 10-04 20:22:17 | SOL | up | 0.59→0.65 | 0.67 → 0.68 | no | edge gone |  |
| 10-04 20:22:16 | ZEC | up | 0.12→0.20 | 0.14 → 0.25 | 7.27s | edge gone |  |
| 10-04 20:22:04 | BTC | down | 0.86→0.81 | 0.14 → 0.18 | 19.53s | edge gone |  |
| 10-04 20:22:00 | XRP | down | 0.55→0.49 | 0.39 → 0.48 | 8.27s | edge gone |  |
| 10-04 20:21:56 | HYPE | down | 0.52→0.43 | 0.52 → 0.55 | 12.52s | edge gone |  |
| 10-04 20:21:52 | SOL | down | 0.79→0.72 | 0.16 → 0.18 | 16.52s | DOWN @ 0.18 | 0.36 / 1.04 / · |
| 10-04 20:21:39 | XRP | down | 0.63→0.57 | 0.31 → 0.40 | 14.27s | edge gone |  |
| 10-04 20:21:33 | BNB | down | 0.70→0.60 | 0.14 → 0.13 | no | DOWN @ 0.13 | -0.26 / -0.26 / · |
| 10-04 20:21:20 | HYPE | up | 0.43→0.52 | 0.53 → 0.54 | no | edge gone |  |
| 10-04 20:21:12 | ZEC | up | 0.22→0.29 | 0.26 → 0.35 | no | edge gone |  |
| 10-04 20:21:12 | BNB | down | 0.70→0.59 | 0.15 → 0.15 | no | DOWN @ 0.15 | -0.47 / -0.47 / · |
| 10-04 20:20:43 | XRP | up | 0.54→0.61 | 0.67 → 0.68 | 25.28s | edge gone |  |
| 10-04 20:20:38 | HYPE | down | 0.52→0.43 | 0.60 → 0.56 | no | spread too wide |  |
| 10-04 20:20:23 | SOL | up | 0.72→0.80 | 0.72 → 0.81 | 0.27s | edge gone |  |
