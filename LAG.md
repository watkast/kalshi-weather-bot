# Lag Tracker

*Updated Sun Oct 04 19:57 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$304.04** | -8.1% | 957 | $3.96 | $185.87 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 982 | 155 | -$431.97 | -11.1% | -$200.79 / -$231.18 |
| Sell after 30 sec | 981 | 249 | -$462.65 | -11.9% | -$224.92 / -$237.73 |
| Hold to the close | 957 | 346 | -$304.04 | -8.1% | -$354.57 / $50.53 |
| Hold, only edge 10¢+ | 341 | 88 | -$187.04 | -17.5% | -$103.70 / -$83.34 |
| Hold, first trade per window only | 294 | 118 | -$52.90 | -4.3% | -$82.17 / $29.27 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 3594 | 10% | 66% | +4.0¢ | 0.3¢ | edge gone 2439, price out of range 95, spread too wide 78 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 749 | 11.1s | 3% | 0% |
| BTC | 928 | 11.9s | 3% | 0% |
| DOGE | 1001 | 10.8s | 3% | 0% |
| ETH | 1132 | 10.8s | 4% | 0% |
| HYPE | 758 | 11.6s | 3% | 0% |
| NEAR | 1084 | 10.8s | 4% | 0% |
| SOL | 1974 | 10.9s | 3% | 0% |
| XRP | 2046 | 11.0s | 3% | 0% |
| ZEC | 1189 | 9.7s | 4% | 0% |
| **All** | **10861** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **7 ms** · Order book check: **27 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 19:56:46 | ETH | down | 0.34→0.28 | 0.75 → 0.86 | 10.50s | edge gone |  |
| 10-04 19:56:45 | XRP | down | 0.87→0.79 | 0.14 → 0.17 | no | edge gone |  |
| 10-04 19:56:37 | HYPE | down | 0.43→0.27 | 0.64 → 0.64 | no | DOWN @ 0.64 | -0.38 / · / · |
| 10-04 19:56:27 | XRP | down | 0.89→0.81 | 0.11 → 0.15 | no | DOWN @ 0.15 | -0.47 / -0.32 / · |
| 10-04 19:56:27 | DOGE | up | 0.22→0.32 | 0.20 → 0.21 | no | UP @ 0.21 | -0.85 / -1.04 / · |
| 10-04 19:56:18 | ETH | up | 0.43→0.48 | 0.41 → 0.44 | 8.26s | edge gone |  |
| 10-04 19:56:12 | XRP | up | 0.84→0.89 | 0.86 → 0.88 | 14.76s | edge gone |  |
| 10-04 19:55:59 | BTC | down | 0.60→0.49 | 0.43 → 0.49 | 12.76s | edge gone |  |
| 10-04 19:55:58 | ETH | down | 0.52→0.45 | 0.56 → 0.54 | 13.26s | edge gone |  |
| 10-04 19:55:58 | DOGE | up | 0.20→0.30 | 0.21 → 0.25 | no | edge gone |  |
| 10-04 19:55:42 | XRP | down | 0.88→0.82 | 0.21 → 0.17 | no | edge gone |  |
| 10-04 19:55:42 | HYPE | down | 0.37→0.30 | 0.50 → 0.58 | 4.01s | DOWN @ 0.58 | -0.40 / -0.80 / · |
| 10-04 19:55:27 | XRP | up | 0.75→0.82 | 0.35 → 0.80 | 4.01s | edge gone |  |
| 10-04 19:55:23 | BNB | down | 0.52→0.42 | 0.10 → 0.21 | 22.31s | DOWN @ 0.22 | -0.85 / -0.82 / · |
| 10-04 19:55:20 | NEAR | down | 0.19→0.13 | 0.81 → 0.82 | no | DOWN @ 0.82 | -0.54 / -0.65 / · |
| 10-04 19:55:19 | HYPE | down | 0.59→0.44 | 0.38 → 0.50 | 11.31s | spread too wide |  |
| 10-04 19:55:19 | SOL | down | 0.11→0.06 | 0.91 → 0.90 | no | DOWN @ 0.90 | -0.12 / 0.49 / · |
| 10-04 19:55:15 | ETH | up | 0.47→0.55 | 0.45 → 0.59 | no | edge gone |  |
| 10-04 19:55:15 | BTC | up | 0.54→0.63 | 0.51 → 0.62 | 1.05s | edge gone |  |
| 10-04 19:55:11 | XRP | up | 0.34→0.43 | 0.28 → 0.44 | 4.55s | edge gone |  |
| 10-04 19:55:01 | ZEC | down | 0.36→0.26 | 0.71 → 0.71 | 29.57s | edge gone |  |
| 10-04 19:54:51 | ETH | down | 0.53→0.47 | 0.53 → 0.59 | 9.55s | edge gone |  |
| 10-04 19:54:45 | ZEC | down | 0.39→0.26 | 0.61 → 0.75 | 0.55s | edge gone |  |
| 10-04 19:54:42 | HYPE | down | 0.52→0.26 | 0.58 → 0.51 | no | DOWN @ 0.52 | -1.60 / -2.19 / · |
| 10-04 19:54:31 | XRP | down | 0.35→0.29 | 0.71 → 0.71 | 0.29s | edge gone |  |
| 10-04 19:54:28 | ETH | up | 0.48→0.53 | 0.42 → 0.49 | 2.55s | edge gone |  |
| 10-04 19:54:27 | BTC | up | 0.44→0.54 | 0.48 → 0.52 | 3.55s | edge gone |  |
| 10-04 19:54:12 | XRP | down | 0.35→0.27 | 0.61 → 0.67 | 4.06s | edge gone |  |
| 10-04 19:54:10 | ZEC | up | 0.45→0.52 | 0.54 → 0.52 | no | edge gone |  |
| 10-04 19:54:05 | ETH | down | 0.58→0.48 | 0.45 → 0.57 | 10.81s | edge gone |  |
