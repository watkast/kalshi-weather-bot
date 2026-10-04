# Lag Tracker

*Updated Sun Oct 04 18:56 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$353.42** | -11.1% | 835 | $3.85 | $161.50 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 855 | 137 | -$378.93 | -11.5% | -$176.46 / -$202.47 |
| Sell after 30 sec | 855 | 217 | -$392.42 | -11.9% | -$203.18 / -$189.24 |
| Hold to the close | 835 | 284 | -$353.42 | -11.1% | -$309.96 / -$43.46 |
| Hold, only edge 10¢+ | 296 | 69 | -$173.77 | -20.1% | -$112.34 / -$61.43 |
| Hold, first trade per window only | 263 | 103 | -$47.13 | -4.4% | -$89.40 / $42.27 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 3185 | 10% | 66% | +4.0¢ | 0.3¢ | edge gone 2170, price out of range 88, spread too wide 70 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 731 | 11.0s | 3% | 0% |
| BTC | 889 | 11.9s | 3% | 0% |
| DOGE | 968 | 10.8s | 3% | 0% |
| ETH | 1082 | 10.9s | 4% | 0% |
| HYPE | 729 | 11.6s | 3% | 0% |
| NEAR | 1041 | 10.8s | 3% | 0% |
| SOL | 1898 | 10.8s | 3% | 0% |
| XRP | 1978 | 11.1s | 3% | 0% |
| ZEC | 1136 | 9.6s | 4% | 0% |
| **All** | **10452** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **9 ms** · Order book check: **27 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 18:56:35 | XRP | down | 0.85→0.77 | 0.12 → 0.10 | no | DOWN @ 0.10 | · / · / · |
| 10-04 18:56:31 | BNB | down | 0.10→0.04 | 0.70 → 0.65 | no | DOWN @ 0.65 | · / · / · |
| 10-04 18:56:20 | SOL | up | 0.31→0.37 | 0.54 → 0.54 | no | edge gone |  |
| 10-04 18:56:05 | SOL | down | 0.38→0.31 | 0.49 → 0.48 | no | DOWN @ 0.48 | -0.46 / -0.47 / · |
| 10-04 18:56:03 | XRP | down | 0.75→0.61 | 0.21 → 0.18 | no | DOWN @ 0.18 | -0.69 / -1.03 / · |
| 10-04 18:55:50 | BTC | down | 0.76→0.70 | 0.29 → 0.31 | no | edge gone |  |
| 10-04 18:55:42 | ZEC | up | 0.31→0.38 | 0.38 → 0.26 | no | UP @ 0.27 | -0.81 / -0.72 / · |
| 10-04 18:55:42 | XRP | up | 0.66→0.71 | 0.81 → 0.81 | no | edge gone |  |
| 10-04 18:55:28 | NEAR | down | 0.21→0.13 | 0.84 → 0.88 | 7.52s | edge gone |  |
| 10-04 18:55:22 | SOL | down | 0.39→0.33 | 0.48 → 0.51 | no | DOWN @ 0.51 | -0.96 / -0.66 / · |
| 10-04 18:55:22 | XRP | up | 0.55→0.60 | 0.71 → 0.77 | 0.01s | edge gone |  |
| 10-04 18:55:17 | BTC | up | 0.69→0.74 | 0.63 → 0.68 | 3.77s | UP @ 0.68 | -0.01 / -0.01 / · |
| 10-04 18:55:10 | BNB | down | 0.16→0.08 | 0.65 → 0.67 | no | spread too wide |  |
| 10-04 18:55:07 | SOL | up | 0.34→0.39 | 0.51 → 0.52 | 28.57s | edge gone |  |
| 10-04 18:55:01 | XRP | down | 0.45→0.35 | 0.45 → 0.49 | 4.03s | DOWN @ 0.49 | -2.43 / -3.29 / · |
| 10-04 18:54:28 | HYPE | down | 0.68→0.63 | 0.27 → 0.34 | 7.54s | edge gone |  |
| 10-04 18:54:27 | BTC | up | 0.49→0.59 | 0.45 → 0.60 | 8.29s | edge gone |  |
| 10-04 18:54:27 | BNB | up | 0.10→0.22 | 0.34 → 0.41 | 8.54s | edge gone |  |
| 10-04 18:54:18 | XRP | down | 0.55→0.45 | 0.27 → 0.40 | 2.04s | DOWN @ 0.40 | -1.22 / -0.24 / · |
| 10-04 18:54:04 | BNB | down | 0.16→0.08 | 0.77 → 0.66 | no | DOWN @ 0.66 | -0.32 / -1.03 / · |
| 10-04 18:54:01 | ZEC | down | 0.36→0.26 | 0.70 → 0.79 | no | edge gone |  |
| 10-04 18:53:53 | XRP | up | 0.37→0.50 | 0.46 → 0.62 | 12.05s | edge gone |  |
| 10-04 18:53:40 | NEAR | down | 0.21→0.15 | 0.80 → 0.83 | 10.80s | edge gone |  |
| 10-04 18:53:24 | XRP | up | 0.33→0.42 | 0.42 → 0.41 | 26.31s | edge gone |  |
| 10-04 18:53:00 | ZEC | up | 0.17→0.27 | 0.15 → 0.22 | 5.06s | UP @ 0.22 | -0.16 / 0.42 / · |
| 10-04 18:52:58 | XRP | down | 0.35→0.28 | 0.66 → 0.67 | no | edge gone |  |
| 10-04 18:52:49 | BTC | down | 0.49→0.43 | 0.56 → 0.56 | no | edge gone |  |
| 10-04 18:52:44 | ETH | up | 0.41→0.49 | 0.35 → 0.34 | no | UP @ 0.34 | -0.91 / -1.49 / · |
| 10-04 18:52:30 | XRP | down | 0.39→0.32 | 0.69 → 0.66 | no | edge gone |  |
| 10-04 18:52:24 | ETH | up | 0.30→0.42 | 0.29 → 0.35 | no | UP @ 0.35 | -0.52 / -0.52 / · |
