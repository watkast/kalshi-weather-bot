# Lag Tracker

*Updated Sun Oct 04 12:04 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$217.13** | -32.1% | 195 | $3.49 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 209 | 32 | -$96.42 | -13.2% | -$39.28 / -$57.14 |
| Sell after 30 sec | 209 | 45 | -$100.76 | -13.8% | -$43.19 / -$57.57 |
| Hold to the close | 195 | 46 | -$217.13 | -32.1% | -$12.23 / -$204.90 |
| Hold, only edge 10¢+ | 66 | 4 | -$126.14 | -75.9% | -$39.39 / -$86.75 |
| Hold, first trade per window only | 71 | 24 | -$35.09 | -12.8% | $8.66 / -$43.75 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 746 | 11% | 64% | +5.0¢ | 0.3¢ | edge gone 502, price out of range 24, spread too wide 11 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 656 | 11.2s | 3% | 0% |
| BTC | 598 | 11.9s | 3% | 0% |
| DOGE | 772 | 10.6s | 2% | 0% |
| ETH | 770 | 11.0s | 4% | 0% |
| HYPE | 631 | 11.2s | 4% | 0% |
| NEAR | 783 | 10.8s | 4% | 0% |
| SOL | 1446 | 10.8s | 3% | 0% |
| XRP | 1444 | 11.0s | 4% | 0% |
| ZEC | 913 | 9.6s | 4% | 0% |
| **All** | **8013** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 12:04:47 | SOL | up | 0.82→0.87 | 0.85 → 0.89 | no | edge gone |  |
| 10-04 12:04:36 | DOGE | up | 0.77→0.84 | 0.85 → 0.84 | no | edge gone |  |
| 10-04 12:04:31 | ZEC | down | 0.55→0.48 | 0.44 → 0.50 | no | edge gone |  |
| 10-04 12:04:24 | SOL | up | 0.74→0.79 | 0.71 → 0.81 | 4.55s | edge gone |  |
| 10-04 12:04:24 | HYPE | up | 0.35→0.43 | 0.53 → 0.44 | no | edge gone |  |
| 10-04 12:04:09 | SOL | down | 0.71→0.64 | 0.30 → 0.30 | no | DOWN @ 0.30 | -1.25 / -1.84 / · |
| 10-04 12:03:54 | SOL | down | 0.71→0.60 | 0.30 → 0.30 | no | DOWN @ 0.30 | -0.45 / -1.45 / · |
| 10-04 12:03:38 | XRP | up | 0.82→0.88 | 0.87 → 0.87 | no | edge gone |  |
| 10-04 12:03:30 | DOGE | down | 0.50→0.44 | 0.28 → 0.45 | 13.29s | DOWN @ 0.45 | -0.26 / -0.46 / · |
| 10-04 12:03:30 | SOL | down | 0.80→0.73 | 0.17 → 0.23 | 13.79s | edge gone |  |
| 10-04 12:03:30 | ETH | down | 0.81→0.70 | 0.26 → 0.40 | 13.79s | edge gone |  |
| 10-04 12:03:29 | BTC | down | 0.75→0.69 | 0.23 → 0.33 | 15.04s | edge gone |  |
| 10-04 12:03:22 | HYPE | up | 0.47→0.53 | 0.48 → 0.57 | 6.78s | edge gone |  |
| 10-04 12:03:17 | BNB | down | 0.55→0.46 | 0.25 → 0.37 | 11.54s | DOWN @ 0.37 | -0.57 / -0.24 / · |
| 10-04 12:03:05 | NEAR | down | 0.57→0.51 | 0.23 → 0.35 | 8.53s | DOWN @ 0.37 | -0.85 / -0.06 / · |
| 10-04 12:03:04 | SOL | down | 0.75→0.70 | 0.29 → 0.22 | no | DOWN @ 0.23 | -0.23 / 0.24 / · |
| 10-04 12:02:57 | ZEC | up | 0.59→0.73 | 0.71 → 0.69 | 16.54s | edge gone |  |
| 10-04 12:02:39 | HYPE | down | 0.62→0.56 | 0.44 → 0.42 | 19.29s | edge gone |  |
| 10-04 12:02:35 | XRP | down | 0.83→0.76 | 0.15 → 0.18 | no | DOWN @ 0.18 | -0.40 / -0.50 / · |
| 10-04 12:02:31 | SOL | down | 0.72→0.56 | 0.22 → 0.39 | no | edge gone |  |
| 10-04 12:02:05 | SOL | up | 0.52→0.69 | 0.63 → 0.69 | 8.79s | edge gone |  |
| 10-04 12:01:59 | ZEC | down | 0.72→0.64 | 0.32 → 0.25 | no | DOWN @ 0.28 | -0.49 / -0.20 / · |
| 10-04 12:01:46 | HYPE | up | 0.35→0.41 | 0.31 → 0.36 | 12.54s | UP @ 0.36 | 1.31 / 2.06 / · |
| 10-04 12:01:42 | XRP | up | 0.68→0.75 | 0.51 → 0.77 | 1.54s | edge gone |  |
| 10-04 12:01:42 | NEAR | down | 0.67→0.62 | 0.32 → 0.27 | no | DOWN @ 0.27 | -1.05 / -1.05 / · |
| 10-04 12:01:41 | SOL | up | 0.45→0.52 | 0.40 → 0.58 | 2.29s | edge gone |  |
| 10-04 12:01:27 | XRP | up | 0.50→0.75 | 0.53 → 0.64 | 17.05s | UP @ 0.64 | 0.28 / 1.29 / · |
| 10-04 12:01:27 | NEAR | up | 0.57→0.62 | 0.69 → 0.73 | 17.05s | edge gone |  |
| 10-04 12:01:06 | NEAR | down | 0.56→0.49 | 0.61 → 0.32 | no | DOWN @ 0.37 | -1.43 / -1.75 / · |
| 10-04 12:00:50 | NEAR | up | 0.36→0.47 | 0.39 → 0.67 | 18.06s | edge gone |  |
