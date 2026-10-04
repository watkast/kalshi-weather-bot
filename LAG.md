# Lag Tracker

*Updated Sun Oct 04 14:54 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$312.75** | -20.1% | 433 | $3.61 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 448 | 75 | -$183.01 | -11.3% | -$98.31 / -$84.70 |
| Sell after 30 sec | 448 | 105 | -$212.63 | -13.1% | -$101.43 / -$111.20 |
| Hold to the close | 433 | 124 | -$312.75 | -20.1% | -$218.09 / -$94.66 |
| Hold, only edge 10¢+ | 154 | 29 | -$122.90 | -29.8% | -$103.88 / -$19.02 |
| Hold, first trade per window only | 146 | 51 | -$75.80 | -12.9% | -$43.83 / -$31.97 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 1679 | 10% | 65% | +4.1¢ | 0.3¢ | edge gone 1143, price out of range 49, spread too wide 39 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 677 | 11.1s | 3% | 0% |
| BTC | 733 | 11.8s | 3% | 0% |
| DOGE | 832 | 10.6s | 3% | 0% |
| ETH | 875 | 11.1s | 4% | 0% |
| HYPE | 672 | 11.6s | 3% | 0% |
| NEAR | 862 | 10.8s | 3% | 0% |
| SOL | 1626 | 10.9s | 3% | 0% |
| XRP | 1652 | 11.0s | 3% | 0% |
| ZEC | 1017 | 9.6s | 4% | 0% |
| **All** | **8946** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 14:53:55 | ZEC | down | 0.62→0.56 | 0.45 → 0.32 | no | spread too wide |  |
| 10-04 14:53:29 | NEAR | down | 0.43→0.36 | 0.38 → 0.39 | 12.53s | DOWN @ 0.39 | -0.73 / -0.54 / · |
| 10-04 14:53:05 | SOL | down | 0.90→0.85 | 0.09 → 0.10 | no | DOWN @ 0.10 | -0.34 / -0.35 / · |
| 10-04 14:53:05 | ETH | down | 0.85→0.76 | 0.23 → 0.26 | no | edge gone |  |
| 10-04 14:52:53 | ZEC | up | 0.46→0.52 | 0.47 → 0.54 | 4.28s | edge gone |  |
| 10-04 14:52:50 | ETH | up | 0.72→0.80 | 0.70 → 0.78 | 6.78s | edge gone |  |
| 10-04 14:52:29 | XRP | down | 0.96→0.91 | 0.06 → 0.07 | no | edge gone |  |
| 10-04 14:52:25 | SOL | down | 0.90→0.85 | 0.10 → 0.09 | no | DOWN @ 0.09 | 0.01 / -0.32 / · |
| 10-04 14:52:24 | ETH | up | 0.69→0.77 | 0.53 → 0.72 | 3.03s | UP @ 0.72 | -0.71 / 0.74 / · |
| 10-04 14:52:22 | HYPE | up | 0.41→0.48 | 0.35 → 0.51 | no | edge gone |  |
| 10-04 14:52:19 | ZEC | up | 0.35→0.47 | 0.32 → 0.40 | 8.28s | UP @ 0.40 | -0.44 / 0.20 / · |
| 10-04 14:52:15 | BTC | up | 0.84→0.90 | 0.84 → 0.89 | 12.03s | edge gone |  |
| 10-04 14:52:09 | ETH | up | 0.54→0.59 | 0.36 → 0.53 | 3.03s | UP @ 0.53 | 0.45 / 1.27 / · |
| 10-04 14:52:03 | DOGE | up | 0.84→0.89 | 0.84 → 0.86 | 23.79s | edge gone |  |
| 10-04 14:52:01 | NEAR | up | 0.19→0.30 | 0.28 → 0.52 | 11.04s | edge gone |  |
| 10-04 14:51:49 | HYPE | up | 0.22→0.28 | 0.18 → 0.28 | 8.04s | edge gone |  |
| 10-04 14:51:48 | ETH | up | 0.29→0.42 | 0.26 → 0.42 | 9.29s | edge gone |  |
| 10-04 14:51:46 | BTC | up | 0.60→0.72 | 0.60 → 0.73 | 11.04s | edge gone |  |
| 10-04 14:51:43 | DOGE | up | 0.70→0.75 | 0.72 → 0.79 | 14.04s | edge gone |  |
| 10-04 14:51:38 | SOL | up | 0.68→0.77 | 0.76 → 0.81 | 4.29s | edge gone |  |
| 10-04 14:51:24 | ETH | down | 0.28→0.21 | 0.65 → 0.75 | 18.30s | edge gone |  |
| 10-04 14:51:20 | XRP | down | 0.81→0.75 | 0.14 → 0.18 | 6.54s | DOWN @ 0.18 | -0.22 / -0.69 / · |
| 10-04 14:51:17 | ZEC | down | 0.33→0.27 | 0.48 → 0.76 | 9.55s | edge gone |  |
| 10-04 14:51:16 | DOGE | down | 0.81→0.72 | 0.20 → 0.26 | 11.05s | edge gone |  |
| 10-04 14:51:11 | SOL | up | 0.71→0.76 | 0.81 → 0.83 | 1.05s | edge gone |  |
| 10-04 14:51:02 | ZEC | down | 0.58→0.48 | 0.40 → 0.49 | 9.55s | spread too wide |  |
| 10-04 14:50:37 | ZEC | up | 0.48→0.60 | 0.39 → 0.56 | 4.55s | edge gone |  |
| 10-04 14:50:27 | BTC | up | 0.49→0.56 | 0.50 → 0.58 | 15.06s | edge gone |  |
| 10-04 14:50:26 | SOL | up | 0.70→0.75 | 0.78 → 0.84 | 16.31s | edge gone |  |
| 10-04 14:50:04 | XRP | up | 0.76→0.81 | 0.83 → 0.83 | no | edge gone |  |
