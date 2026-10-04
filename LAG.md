# Lag Tracker

*Updated Sun Oct 04 16:25 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$373.00** | -17.8% | 570 | $3.68 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 584 | 100 | -$243.54 | -11.3% | -$124.94 / -$118.60 |
| Sell after 30 sec | 584 | 147 | -$264.90 | -12.3% | -$148.08 / -$116.82 |
| Hold to the close | 570 | 172 | -$373.00 | -17.8% | -$315.59 / -$57.41 |
| Hold, only edge 10¢+ | 202 | 47 | -$107.08 | -18.6% | -$122.55 / $15.47 |
| Hold, first trade per window only | 189 | 69 | -$78.35 | -10.2% | -$55.43 / -$22.92 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 2258 | 10% | 67% | +5.0¢ | 0.3¢ | edge gone 1559, price out of range 58, spread too wide 57 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 694 | 11.2s | 3% | 0% |
| BTC | 805 | 11.9s | 3% | 0% |
| DOGE | 870 | 10.6s | 3% | 0% |
| ETH | 953 | 10.8s | 4% | 0% |
| HYPE | 697 | 11.6s | 3% | 0% |
| NEAR | 928 | 10.8s | 3% | 0% |
| SOL | 1761 | 10.8s | 3% | 0% |
| XRP | 1758 | 11.2s | 3% | 0% |
| ZEC | 1059 | 9.6s | 4% | 0% |
| **All** | **9525** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **19 ms** · Order book check: **25 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 16:25:44 | SOL | up | 0.06→0.12 | 0.07 → 0.13 | no | edge gone |  |
| 10-04 16:25:06 | SOL | down | 0.16→0.09 | 0.83 → 0.92 | 22.32s | edge gone |  |
| 10-04 16:25:05 | BTC | down | 0.17→0.11 | 0.84 → 0.88 | 23.58s | edge gone |  |
| 10-04 16:24:55 | ZEC | down | 0.79→0.70 | 0.20 → 0.18 | no | DOWN @ 0.18 | -0.03 / -0.60 / · |
| 10-04 16:24:52 | NEAR | down | 0.31→0.22 | 0.73 → 0.68 | 21.83s | spread too wide |  |
| 10-04 16:24:51 | SOL | down | 0.20→0.14 | 0.85 → 0.83 | no | edge gone |  |
| 10-04 16:24:46 | XRP | up | 0.10→0.16 | 0.07 → 0.09 | no | UP @ 0.09 | -0.34 / -0.67 / · |
| 10-04 16:24:45 | BNB | down | 0.54→0.42 | 0.32 → 0.22 | no | DOWN @ 0.22 | -1.11 / 0.32 / · |
| 10-04 16:24:27 | NEAR | up | 0.20→0.25 | 0.13 → 0.26 | 1.58s | edge gone |  |
| 10-04 16:24:25 | ZEC | up | 0.65→0.73 | 0.79 → 0.78 | 18.58s | edge gone |  |
| 10-04 16:24:22 | SOL | down | 0.24→0.18 | 0.75 → 0.83 | 6.83s | edge gone |  |
| 10-04 16:23:47 | DOGE | up | 0.27→0.35 | 0.17 → 0.25 | 11.84s | UP @ 0.25 | -0.66 / -0.85 / · |
| 10-04 16:23:45 | NEAR | down | 0.16→0.10 | 0.92 → 0.92 | no | edge gone |  |
| 10-04 16:23:43 | BTC | down | 0.22→0.16 | 0.92 → 0.85 | no | edge gone |  |
| 10-04 16:23:33 | ZEC | up | 0.64→0.72 | 0.55 → 0.74 | 10.59s | edge gone |  |
| 10-04 16:23:32 | BNB | up | 0.34→0.43 | 0.46 → 0.66 | 12.34s | edge gone |  |
| 10-04 16:23:28 | SOL | up | 0.09→0.19 | 0.20 → 0.17 | 15.85s | edge gone |  |
| 10-04 16:23:28 | BTC | up | 0.11→0.16 | 0.10 → 0.12 | 16.35s | UP @ 0.12 | 0.13 / -0.06 / · |
| 10-04 16:23:15 | ZEC | down | 0.67→0.56 | 0.36 → 0.37 | 13.60s | DOWN @ 0.37 | -0.13 / -2.37 / · |
| 10-04 16:23:14 | BNB | down | 0.36→0.29 | 0.33 → 0.50 | 0.35s | DOWN @ 0.50 | 0.04 / -2.72 / · |
| 10-04 16:23:06 | DOGE | down | 0.28→0.23 | 0.81 → 0.89 | 8.35s | edge gone |  |
| 10-04 16:23:02 | BTC | down | 0.27→0.17 | 0.82 → 0.85 | 12.35s | edge gone |  |
| 10-04 16:22:55 | SOL | down | 0.29→0.24 | 0.67 → 0.75 | 18.86s | edge gone |  |
| 10-04 16:22:17 | XRP | down | 0.21→0.16 | 0.88 → 0.92 | 12.11s | edge gone |  |
| 10-04 16:22:15 | SOL | down | 0.35→0.30 | 0.63 → 0.72 | 13.61s | edge gone |  |
| 10-04 16:21:55 | SOL | down | 0.41→0.36 | 0.58 → 0.62 | 4.12s | edge gone |  |
| 10-04 16:21:38 | ETH | down | 0.28→0.23 | 0.78 → 0.82 | 5.62s | edge gone |  |
| 10-04 16:21:37 | SOL | down | 0.42→0.36 | 0.46 → 0.59 | 6.87s | DOWN @ 0.59 | -0.14 / -0.04 / · |
| 10-04 16:21:22 | SOL | down | 0.47→0.42 | 0.50 → 0.46 | 21.88s | DOWN @ 0.46 | -0.21 / 1.05 / · |
| 10-04 16:21:10 | ETH | down | 0.31→0.25 | 0.71 → 0.81 | 4.14s | edge gone |  |
