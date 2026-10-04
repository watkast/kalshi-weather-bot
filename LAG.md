# Lag Tracker

*Updated Sun Oct 04 15:45 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$353.52** | -19.4% | 495 | $3.69 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 513 | 89 | -$209.32 | -11.1% | -$112.99 / -$96.33 |
| Sell after 30 sec | 513 | 129 | -$230.19 | -12.2% | -$127.08 / -$103.11 |
| Hold to the close | 495 | 147 | -$353.52 | -19.4% | -$272.91 / -$80.61 |
| Hold, only edge 10¢+ | 177 | 37 | -$110.76 | -23.0% | -$115.20 / $4.44 |
| Hold, first trade per window only | 168 | 58 | -$110.14 | -16.0% | -$46.09 / -$64.05 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 2011 | 10% | 67% | +5.0¢ | 0.3¢ | edge gone 1395, price out of range 55, spread too wide 48 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 689 | 11.1s | 3% | 0% |
| BTC | 779 | 11.8s | 3% | 0% |
| DOGE | 855 | 10.6s | 3% | 0% |
| ETH | 923 | 10.9s | 4% | 0% |
| HYPE | 688 | 11.6s | 3% | 0% |
| NEAR | 893 | 10.8s | 3% | 0% |
| SOL | 1697 | 10.8s | 3% | 0% |
| XRP | 1718 | 11.1s | 3% | 0% |
| ZEC | 1036 | 9.6s | 4% | 0% |
| **All** | **9278** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **19 ms** · Order book check: **24 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 15:43:32 | ETH | down | 0.22→0.16 | 0.89 → 0.94 | 9.58s | edge gone |  |
| 10-04 15:43:32 | BTC | down | 0.85→0.74 | 0.08 → 0.34 | 9.58s | edge gone |  |
| 10-04 15:43:29 | SOL | up | 0.38→0.45 | 0.47 → 0.44 | no | edge gone |  |
| 10-04 15:43:24 | XRP | down | 0.12→0.07 | 0.92 → 0.96 | 3.08s | price out of range |  |
| 10-04 15:43:08 | SOL | up | 0.28→0.40 | 0.54 → 0.47 | no | edge gone |  |
| 10-04 15:42:57 | XRP | down | 0.23→0.16 | 0.90 → 0.89 | 14.84s | edge gone |  |
| 10-04 15:42:53 | SOL | down | 0.52→0.46 | 0.47 → 0.47 | 19.34s | DOWN @ 0.47 | -1.45 / 0.24 / · |
| 10-04 15:42:39 | XRP | up | 0.18→0.25 | 0.20 → 0.14 | no | UP @ 0.14 | -0.49 / -1.35 / · |
| 10-04 15:42:38 | SOL | up | 0.47→0.52 | 0.48 → 0.53 | 4.34s | spread too wide |  |
| 10-04 15:42:22 | DOGE | up | 0.89→0.95 | 0.96 → 0.98 | 4.59s | price out of range |  |
| 10-04 15:42:22 | SOL | up | 0.42→0.47 | 0.44 → 0.52 | 4.84s | edge gone |  |
| 10-04 15:42:21 | XRP | up | 0.17→0.23 | 0.18 → 0.15 | no | UP @ 0.16 | -0.55 / -0.74 / · |
| 10-04 15:42:14 | BTC | up | 0.59→0.66 | 0.72 → 0.73 | 0.08s | edge gone |  |
| 10-04 15:42:06 | SOL | down | 0.52→0.38 | 0.62 → 0.57 | no | edge gone |  |
| 10-04 15:42:06 | XRP | down | 0.22→0.14 | 0.84 → 0.85 | no | edge gone |  |
| 10-04 15:41:49 | NEAR | down | 0.15→0.08 | 0.62 → 0.74 | 7.85s | DOWN @ 0.75 | 0.88 / 1.40 / · |
| 10-04 15:41:49 | XRP | up | 0.10→0.23 | 0.14 → 0.20 | no | edge gone |  |
| 10-04 15:41:33 | SOL | down | 0.43→0.35 | 0.58 → 0.68 | 8.86s | edge gone |  |
| 10-04 15:41:19 | XRP | up | 0.25→0.34 | 0.23 → 0.32 | 7.61s | edge gone |  |
| 10-04 15:41:18 | SOL | up | 0.43→0.52 | 0.46 → 0.47 | no | edge gone |  |
| 10-04 15:41:00 | SOL | down | 0.44→0.36 | 0.68 → 0.62 | no | edge gone |  |
| 10-04 15:40:59 | XRP | up | 0.21→0.29 | 0.15 → 0.24 | 12.87s | UP @ 0.24 | -0.46 / -0.79 / · |
| 10-04 15:40:59 | DOGE | up | 0.80→0.86 | 0.76 → 0.90 | 13.37s | edge gone |  |
| 10-04 15:40:56 | NEAR | up | 0.16→0.24 | 0.36 → 0.43 | 15.87s | edge gone |  |
| 10-04 15:40:33 | ETH | up | 0.18→0.23 | 0.15 → 0.21 | 9.12s | edge gone |  |
| 10-04 15:40:32 | XRP | up | 0.10→0.16 | 0.09 → 0.14 | 10.37s | edge gone |  |
| 10-04 15:40:32 | DOGE | up | 0.49→0.60 | 0.54 → 0.65 | 10.37s | edge gone |  |
| 10-04 15:40:29 | BTC | up | 0.40→0.46 | 0.37 → 0.36 | 12.87s | UP @ 0.36 | 0.95 / 1.35 / · |
| 10-04 15:40:22 | SOL | up | 0.31→0.37 | 0.36 → 0.30 | no | UP @ 0.30 | -0.40 / -0.11 / · |
| 10-04 15:40:05 | SOL | down | 0.41→0.34 | 0.65 → 0.67 | 22.13s | edge gone |  |
