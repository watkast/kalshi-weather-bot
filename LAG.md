# Lag Tracker

*Updated Sun Oct 04 19:26 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$274.14** | -8.0% | 892 | $3.90 | $161.50 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 915 | 145 | -$406.11 | -11.4% | -$188.09 / -$218.02 |
| Sell after 30 sec | 915 | 234 | -$424.61 | -11.9% | -$219.16 / -$205.45 |
| Hold to the close | 892 | 316 | -$274.14 | -8.0% | -$333.87 / $59.73 |
| Hold, only edge 10¢+ | 321 | 84 | -$128.44 | -13.3% | -$115.89 / -$12.55 |
| Hold, first trade per window only | 277 | 110 | -$44.04 | -3.8% | -$86.61 / $42.57 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 3351 | 10% | 65% | +4.0¢ | 0.3¢ | edge gone 2270, price out of range 93, spread too wide 72 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 740 | 11.1s | 3% | 0% |
| BTC | 901 | 11.9s | 3% | 0% |
| DOGE | 973 | 10.9s | 3% | 0% |
| ETH | 1096 | 10.9s | 4% | 0% |
| HYPE | 742 | 11.6s | 3% | 0% |
| NEAR | 1071 | 10.8s | 4% | 0% |
| SOL | 1938 | 10.9s | 3% | 0% |
| XRP | 1990 | 11.1s | 3% | 0% |
| ZEC | 1167 | 9.7s | 4% | 0% |
| **All** | **10618** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **8 ms** · Order book check: **27 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 19:26:49 | ZEC | down | 0.33→0.27 | 0.58 → 0.60 | 0.03s | DOWN @ 0.60 | · / · / · |
| 10-04 19:26:25 | BTC | down | 0.89→0.80 | 0.09 → 0.22 | 7.30s | edge gone |  |
| 10-04 19:26:13 | ZEC | down | 0.64→0.53 | 0.31 → 0.41 | 19.31s | DOWN @ 0.42 | 0.80 / 1.00 / · |
| 10-04 19:26:09 | HYPE | up | 0.37→0.52 | 0.18 → 0.72 | 8.55s | edge gone |  |
| 10-04 19:25:39 | NEAR | up | 0.05→0.11 | 0.15 → 0.10 | no | edge gone |  |
| 10-04 19:25:31 | ZEC | down | 0.83→0.77 | 0.19 → 0.18 | 17.06s | DOWN @ 0.18 | 0.45 / 0.94 / · |
| 10-04 19:25:15 | ZEC | up | 0.62→0.81 | 0.65 → 0.82 | 2.31s | edge gone |  |
| 10-04 19:25:14 | HYPE | down | 0.16→0.10 | 0.83 → 0.81 | no | DOWN @ 0.81 | -0.12 / -0.12 / · |
| 10-04 19:25:03 | ETH | up | 0.83→0.89 | 0.81 → 0.84 | 0.31s | UP @ 0.84 | 0.68 / 0.33 / · |
| 10-04 19:25:00 | BTC | up | 0.74→0.81 | 0.56 → 0.77 | 2.82s | edge gone |  |
| 10-04 19:24:59 | ZEC | up | 0.51→0.61 | 0.52 → 0.59 | 3.32s | edge gone |  |
| 10-04 19:24:38 | BTC | up | 0.53→0.59 | 0.53 → 0.60 | 24.33s | edge gone |  |
| 10-04 19:24:18 | HYPE | up | 0.09→0.14 | 0.24 → 0.22 | no | edge gone |  |
| 10-04 19:24:09 | NEAR | down | 0.21→0.14 | 0.80 → 0.84 | 9.08s | edge gone |  |
| 10-04 19:24:06 | ZEC | up | 0.35→0.44 | 0.40 → 0.51 | 11.58s | edge gone |  |
| 10-04 19:23:53 | XRP | up | 0.89→0.96 | 0.89 → 0.88 | no | UP @ 0.88 | -0.16 / -0.26 / · |
| 10-04 19:23:45 | BTC | down | 0.62→0.53 | 0.41 → 0.54 | 3.10s | edge gone |  |
| 10-04 19:23:44 | ZEC | down | 0.40→0.34 | 0.53 → 0.62 | 18.59s | edge gone |  |
| 10-04 19:23:35 | SOL | down | 0.16→0.06 | 0.87 → 0.92 | 13.10s | edge gone |  |
| 10-04 19:23:11 | DOGE | up | 0.81→0.90 | 0.80 → 0.88 | 6.60s | edge gone |  |
| 10-04 19:23:11 | SOL | up | 0.15→0.20 | 0.16 → 0.16 | no | edge gone |  |
| 10-04 19:22:56 | BTC | up | 0.52→0.60 | 0.45 → 0.56 | 6.35s | edge gone |  |
| 10-04 19:22:34 | ZEC | down | 0.53→0.46 | 0.43 → 0.52 | 14.11s | edge gone |  |
| 10-04 19:22:34 | BTC | down | 0.66→0.59 | 0.46 → 0.56 | 14.11s | edge gone |  |
| 10-04 19:22:30 | DOGE | up | 0.74→0.81 | 0.81 → 0.80 | no | edge gone |  |
| 10-04 19:22:22 | NEAR | up | 0.23→0.31 | 0.36 → 0.32 | no | edge gone |  |
| 10-04 19:22:06 | SOL | down | 0.25→0.19 | 0.80 → 0.81 | no | edge gone |  |
| 10-04 19:22:06 | NEAR | down | 0.37→0.31 | 0.61 → 0.63 | 11.12s | DOWN @ 0.64 | 0.33 / 0.43 / · |
| 10-04 19:22:01 | ZEC | down | 0.54→0.46 | 0.40 → 0.44 | no | DOWN @ 0.44 | -0.65 / -0.95 / · |
| 10-04 19:21:52 | HYPE | down | 0.70→0.61 | 0.26 → 0.33 | 10.12s | DOWN @ 0.33 | -0.81 / -0.90 / · |
