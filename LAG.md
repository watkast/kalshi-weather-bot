# Lag Tracker

*Updated Sun Oct 04 21:06 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$191.39** | -4.5% | 1065 | $3.98 | $185.87 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1073 | 171 | -$470.88 | -11.0% | -$223.36 / -$247.52 |
| Sell after 30 sec | 1073 | 275 | -$504.74 | -11.8% | -$246.31 / -$258.43 |
| Hold to the close | 1065 | 404 | -$191.39 | -4.5% | -$328.02 / $136.63 |
| Hold, only edge 10¢+ | 383 | 110 | -$128.28 | -10.4% | -$80.53 / -$47.75 |
| Hold, first trade per window only | 330 | 134 | -$55.61 | -4.0% | -$104.51 / $48.90 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 3978 | 10% | 65% | +4.0¢ | 0.3¢ | edge gone 2710, price out of range 102, spread too wide 92 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 776 | 11.1s | 3% | 0% |
| BTC | 970 | 11.8s | 3% | 0% |
| DOGE | 1035 | 10.9s | 3% | 0% |
| ETH | 1174 | 10.9s | 4% | 0% |
| HYPE | 784 | 11.4s | 3% | 0% |
| NEAR | 1135 | 10.8s | 4% | 0% |
| SOL | 2030 | 10.9s | 3% | 0% |
| XRP | 2108 | 11.0s | 3% | 0% |
| ZEC | 1233 | 9.8s | 4% | 0% |
| **All** | **11245** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **6 ms** · Order book check: **61 ms** · Coinbase price delay: **34 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 21:06:35 | BTC | up | 0.66→0.72 | 0.65 → 0.65 | no | UP @ 0.66 | · / · / · |
| 10-04 21:06:04 | SOL | down | 0.56→0.48 | 0.54 → 0.53 | no | edge gone |  |
| 10-04 21:06:02 | BNB | down | 0.41→0.36 | 0.34 → 0.44 | 13.45s | DOWN @ 0.48 | -1.11 / -1.28 / · |
| 10-04 21:05:37 | NEAR | down | 0.23→0.15 | 0.85 → 0.86 | no | edge gone |  |
| 10-04 21:05:22 | NEAR | up | 0.15→0.21 | 0.19 → 0.19 | no | edge gone |  |
| 10-04 21:05:19 | ETH | up | 0.49→0.55 | 0.53 → 0.54 | 11.96s | edge gone |  |
| 10-04 21:05:18 | ZEC | up | 0.33→0.41 | 0.35 → 0.38 | 27.22s | edge gone |  |
| 10-04 21:05:14 | BTC | up | 0.50→0.57 | 0.55 → 0.54 | 16.47s | edge gone |  |
| 10-04 21:05:02 | ETH | down | 0.62→0.56 | 0.44 → 0.52 | 0.43s | edge gone |  |
| 10-04 21:04:57 | SOL | down | 0.48→0.40 | 0.52 → 0.62 | 18.47s | edge gone |  |
| 10-04 21:04:54 | BTC | down | 0.63→0.58 | 0.40 → 0.48 | 6.97s | edge gone |  |
| 10-04 21:04:37 | ETH | down | 0.62→0.56 | 0.37 → 0.40 | 8.98s | edge gone |  |
| 10-04 21:04:32 | BNB | down | 0.58→0.49 | 0.26 → 0.34 | 13.73s | DOWN @ 0.34 | -0.66 / -0.57 / · |
| 10-04 21:04:26 | SOL | up | 0.44→0.50 | 0.51 → 0.50 | no | edge gone |  |
| 10-04 21:04:19 | ETH | up | 0.53→0.59 | 0.57 → 0.61 | 11.73s | edge gone |  |
| 10-04 21:04:10 | BTC | down | 0.58→0.52 | 0.46 → 0.52 | no | edge gone |  |
| 10-04 21:04:10 | XRP | down | 0.52→0.45 | 0.46 → 0.52 | 5.98s | edge gone |  |
| 10-04 21:04:01 | ZEC | down | 0.38→0.32 | 0.56 → 0.69 | 14.24s | edge gone |  |
| 10-04 21:04:01 | NEAR | down | 0.34→0.28 | 0.69 → 0.79 | 14.74s | edge gone |  |
| 10-04 21:03:59 | DOGE | up | 0.75→0.83 | 0.76 → 0.83 | 1.23s | edge gone |  |
| 10-04 21:03:42 | ZEC | down | 0.49→0.41 | 0.64 → 0.56 | no | edge gone |  |
| 10-04 21:03:20 | ZEC | up | 0.33→0.38 | 0.30 → 0.37 | 10.25s | edge gone |  |
| 10-04 21:03:18 | SOL | down | 0.53→0.46 | 0.47 → 0.54 | 12.50s | edge gone |  |
| 10-04 21:03:17 | ETH | down | 0.60→0.53 | 0.44 → 0.50 | no | edge gone |  |
| 10-04 21:03:12 | NEAR | up | 0.25→0.30 | 0.31 → 0.25 | no | UP @ 0.25 | -0.37 / 0.21 / · |
| 10-04 21:03:04 | BTC | down | 0.73→0.66 | 0.35 → 0.41 | 11.75s | edge gone |  |
| 10-04 21:02:57 | SOL | up | 0.48→0.55 | 0.54 → 0.59 | no | edge gone |  |
| 10-04 21:02:34 | BTC | up | 0.70→0.75 | 0.63 → 0.69 | 12.01s | UP @ 0.69 | -0.61 / -1.32 / · |
| 10-04 21:02:31 | SOL | down | 0.48→0.42 | 0.51 → 0.53 | no | edge gone |  |
| 10-04 21:02:16 | SOL | down | 0.48→0.41 | 0.59 → 0.57 | no | edge gone |  |
