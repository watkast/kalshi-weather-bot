# Lag Tracker

*Updated Sun Oct 04 19:36 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$258.17** | -7.2% | 921 | $3.91 | $161.50 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 939 | 150 | -$413.50 | -11.3% | -$190.26 / -$223.24 |
| Sell after 30 sec | 939 | 236 | -$446.19 | -12.2% | -$222.29 / -$223.90 |
| Hold to the close | 921 | 332 | -$258.17 | -7.2% | -$331.19 / $73.02 |
| Hold, only edge 10¢+ | 326 | 87 | -$121.98 | -12.3% | -$115.03 / -$6.95 |
| Hold, first trade per window only | 286 | 116 | -$29.77 | -2.5% | -$73.17 / $43.40 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 3431 | 10% | 65% | +4.0¢ | 0.3¢ | edge gone 2325, price out of range 94, spread too wide 72 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 744 | 11.1s | 3% | 0% |
| BTC | 908 | 11.9s | 3% | 0% |
| DOGE | 985 | 10.8s | 3% | 0% |
| ETH | 1107 | 10.8s | 4% | 0% |
| HYPE | 744 | 11.6s | 3% | 0% |
| NEAR | 1074 | 10.8s | 4% | 0% |
| SOL | 1952 | 10.9s | 3% | 0% |
| XRP | 2008 | 11.1s | 3% | 0% |
| ZEC | 1176 | 9.7s | 4% | 0% |
| **All** | **10698** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **7 ms** · Order book check: **27 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 19:36:53 | XRP | down | 0.47→0.42 | 0.55 → 0.52 | no | DOWN @ 0.52 | · / · / · |
| 10-04 19:36:35 | BNB | up | 0.70→0.79 | 0.91 → 0.90 | no | edge gone |  |
| 10-04 19:36:24 | XRP | up | 0.45→0.50 | 0.48 → 0.49 | no | edge gone |  |
| 10-04 19:35:51 | DOGE | down | 0.81→0.75 | 0.20 → 0.20 | no | DOWN @ 0.20 | -0.05 / -0.08 / · |
| 10-04 19:35:51 | ETH | down | 0.60→0.53 | 0.49 → 0.53 | no | edge gone |  |
| 10-04 19:35:48 | XRP | down | 0.60→0.53 | 0.45 → 0.50 | 1.31s | edge gone |  |
| 10-04 19:35:40 | SOL | down | 0.80→0.72 | 0.21 → 0.21 | no | DOWN @ 0.21 | -0.53 / -0.91 / · |
| 10-04 19:35:32 | XRP | up | 0.60→0.65 | 0.53 → 0.58 | 1.32s | UP @ 0.58 | -0.86 / -1.76 / · |
| 10-04 19:35:16 | XRP | up | 0.57→0.65 | 0.61 → 0.56 | no | UP @ 0.56 | -0.46 / -0.76 / · |
| 10-04 19:35:15 | SOL | up | 0.69→0.75 | 0.80 → 0.78 | no | edge gone |  |
| 10-04 19:35:01 | XRP | up | 0.62→0.72 | 0.61 → 0.59 | no | UP @ 0.59 | -1.05 / -0.95 / · |
| 10-04 19:34:54 | ZEC | up | 0.79→0.84 | 0.81 → 0.84 | 9.58s | edge gone |  |
| 10-04 19:34:54 | BTC | up | 0.87→0.93 | 0.74 → 0.80 | 9.58s | UP @ 0.80 | -0.13 / -0.34 / · |
| 10-04 19:34:54 | ETH | up | 0.51→0.56 | 0.46 → 0.53 | no | edge gone |  |
| 10-04 19:34:48 | SOL | down | 0.74→0.69 | 0.27 → 0.29 | no | edge gone |  |
| 10-04 19:34:45 | XRP | down | 0.67→0.57 | 0.35 → 0.48 | 4.08s | edge gone |  |
| 10-04 19:34:43 | DOGE | down | 0.87→0.77 | 0.10 → 0.19 | 5.58s | edge gone |  |
| 10-04 19:34:39 | ETH | down | 0.60→0.52 | 0.47 → 0.53 | 10.08s | edge gone |  |
| 10-04 19:34:34 | BNB | down | 0.73→0.65 | 0.14 → 0.15 | no | DOWN @ 0.15 | -0.40 / -0.51 / · |
| 10-04 19:34:28 | SOL | down | 0.76→0.69 | 0.22 → 0.27 | 6.09s | edge gone |  |
| 10-04 19:34:25 | XRP | down | 0.80→0.71 | 0.30 → 0.36 | 9.09s | edge gone |  |
| 10-04 19:34:24 | ZEC | down | 0.89→0.81 | 0.12 → 0.16 | 10.09s | edge gone |  |
| 10-04 19:34:22 | ETH | down | 0.75→0.68 | 0.27 → 0.42 | 11.84s | edge gone |  |
| 10-04 19:34:18 | DOGE | up | 0.77→0.84 | 0.49 → 0.87 | 0.59s | edge gone |  |
| 10-04 19:34:10 | XRP | up | 0.77→0.88 | 0.47 → 0.75 | 9.09s | UP @ 0.75 | -0.74 / -1.61 / · |
| 10-04 19:34:04 | ZEC | up | 0.82→0.88 | 0.85 → 0.91 | 14.84s | edge gone |  |
| 10-04 19:34:03 | ETH | up | 0.51→0.82 | 0.48 → 0.69 | 15.59s | UP @ 0.69 | -0.20 / -2.53 / · |
| 10-04 19:34:03 | SOL | up | 0.56→0.71 | 0.61 → 0.75 | 15.59s | edge gone |  |
| 10-04 19:34:03 | BTC | up | 0.81→0.92 | 0.77 → 0.80 | 15.59s | UP @ 0.80 | 0.18 / -0.55 / · |
| 10-04 19:34:02 | DOGE | up | 0.43→0.51 | 0.51 → 0.53 | 16.60s | edge gone |  |
