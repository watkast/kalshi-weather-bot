# Lag Tracker

*Updated Sun Oct 04 18:46 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$353.42** | -11.1% | 835 | $3.83 | $161.50 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 837 | 136 | -$365.80 | -11.4% | -$171.71 / -$194.09 |
| Sell after 30 sec | 836 | 215 | -$378.83 | -11.8% | -$198.55 / -$180.28 |
| Hold to the close | 835 | 284 | -$353.42 | -11.1% | -$309.96 / -$43.46 |
| Hold, only edge 10¢+ | 296 | 69 | -$173.77 | -20.1% | -$112.34 / -$61.43 |
| Hold, first trade per window only | 263 | 103 | -$47.13 | -4.4% | -$89.40 / $42.27 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 3119 | 10% | 66% | +4.0¢ | 0.3¢ | edge gone 2125, price out of range 88, spread too wide 69 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 727 | 11.1s | 3% | 0% |
| BTC | 881 | 11.9s | 3% | 0% |
| DOGE | 967 | 10.7s | 3% | 0% |
| ETH | 1074 | 10.8s | 4% | 0% |
| HYPE | 727 | 11.6s | 3% | 0% |
| NEAR | 1034 | 10.9s | 3% | 0% |
| SOL | 1887 | 10.8s | 3% | 0% |
| XRP | 1960 | 11.1s | 3% | 0% |
| ZEC | 1129 | 9.6s | 4% | 0% |
| **All** | **10386** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **9 ms** · Order book check: **26 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 18:46:30 | SOL | up | 0.50→0.56 | 0.59 → 0.64 | 5.00s | edge gone |  |
| 10-04 18:46:18 | NEAR | up | 0.36→0.42 | 0.46 → 0.47 | no | edge gone |  |
| 10-04 18:46:14 | XRP | down | 0.52→0.45 | 0.48 → 0.49 | no | DOWN @ 0.49 | -0.65 / · / · |
| 10-04 18:46:02 | NEAR | down | 0.44→0.37 | 0.51 → 0.56 | 3.25s | DOWN @ 0.56 | -0.39 / -0.56 / · |
| 10-04 18:43:41 | DOGE | down | 0.78→0.63 | 0.07 → 0.19 | 11.52s | DOWN @ 0.19 | -0.79 / 0.64 / -2.01 |
| 10-04 18:43:39 | SOL | up | 0.59→0.71 | 0.98 → 0.99 | no | price out of range |  |
| 10-04 18:43:17 | SOL | up | 0.84→0.90 | 0.99 → 0.99 | no | price out of range |  |
| 10-04 18:43:16 | BTC | up | 0.87→0.96 | 0.93 → 0.96 | no | price out of range |  |
| 10-04 18:42:57 | SOL | down | 0.86→0.81 | 0.02 → 0.01 | no | price out of range |  |
| 10-04 18:42:55 | BTC | up | 0.76→0.82 | 0.92 → 0.94 | 0.01s | edge gone |  |
| 10-04 18:42:42 | DOGE | up | 0.78→0.84 | 0.79 → 0.91 | 11.02s | edge gone |  |
| 10-04 18:42:35 | SOL | up | 0.64→0.71 | 0.87 → 0.98 | 3.27s | price out of range |  |
| 10-04 18:42:31 | XRP | up | 0.87→0.93 | 0.91 → 0.93 | 22.03s | edge gone |  |
| 10-04 18:42:31 | ETH | down | 0.83→0.77 | 0.31 → 0.24 | no | edge gone |  |
| 10-04 18:42:20 | SOL | up | 0.55→0.70 | 0.88 → 0.95 | 18.27s | price out of range |  |
| 10-04 18:42:16 | XRP | down | 0.92→0.86 | 0.13 → 0.10 | no | DOWN @ 0.10 | -0.42 / -0.86 / -1.07 |
| 10-04 18:42:10 | DOGE | down | 0.57→0.51 | 0.38 → 0.38 | no | DOWN @ 0.38 | -0.93 / -3.04 / -3.97 |
| 10-04 18:42:03 | SOL | down | 0.55→0.47 | 0.15 → 0.13 | no | DOWN @ 0.13 | -0.92 / -1.23 / -1.39 |
| 10-04 18:41:59 | XRP | down | 0.90→0.84 | 0.14 → 0.12 | no | edge gone |  |
| 10-04 18:41:52 | DOGE | down | 0.59→0.52 | 0.40 → 0.47 | no | edge gone |  |
| 10-04 18:41:48 | SOL | down | 0.55→0.41 | 0.21 → 0.16 | no | DOWN @ 0.16 | -0.63 / -1.10 / -1.70 |
| 10-04 18:41:32 | DOGE | down | 0.61→0.54 | 0.32 → 0.43 | 6.27s | edge gone |  |
| 10-04 18:41:21 | XRP | up | 0.85→0.90 | 0.86 → 0.88 | no | edge gone |  |
| 10-04 18:41:15 | SOL | up | 0.54→0.60 | 0.73 → 0.67 | 22.78s | edge gone |  |
| 10-04 18:41:08 | DOGE | down | 0.33→0.26 | 0.66 → 0.81 | no | edge gone |  |
| 10-04 18:41:03 | NEAR | down | 0.99→0.85 | 0.04 → 0.15 | 5.02s | spread too wide |  |
| 10-04 18:40:52 | SOL | up | 0.54→0.60 | 0.68 → 0.72 | 15.53s | edge gone |  |
| 10-04 18:40:51 | XRP | up | 0.72→0.86 | 0.77 → 0.87 | 16.53s | edge gone |  |
| 10-04 18:40:44 | ETH | up | 0.62→0.77 | 0.59 → 0.75 | 8.77s | edge gone |  |
| 10-04 18:40:42 | BTC | down | 0.68→0.54 | 0.27 → 0.24 | no | DOWN @ 0.24 | -0.26 / -0.36 / -2.53 |
