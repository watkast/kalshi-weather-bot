# Lag Tracker

*Updated Sun Oct 04 11:04 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🟡 **Testing with real order-book fills.** 104 of 150 settled trades needed before calling it. The earlier results below used quoted prices, which may not have been fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$24.32** | -6.3% | 104 | $3.68 | $83.77 | 10.8s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 107 | 24 | -$39.46 | -10.0% | -$18.80 / -$20.66 |
| Sell after 30 sec | 106 | 30 | -$41.54 | -10.6% | -$28.43 / -$13.11 |
| Hold to the close | 104 | 36 | -$24.32 | -6.3% | -$9.38 / -$14.94 |
| Hold, only edge 10¢+ | 26 | 3 | -$33.83 | -53.0% | -$24.67 / -$9.16 |
| Hold, first trade per window only | 43 | 16 | -$9.36 | -5.5% | -$5.20 / -$4.16 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 478 | 9% | 68% | +5.0¢ | 0.3¢ | edge gone 343, price out of range 22, spread too wide 6 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 651 | 11.1s | 3% | 0% |
| BTC | 576 | 11.9s | 3% | 0% |
| DOGE | 756 | 10.5s | 2% | 0% |
| ETH | 742 | 11.0s | 4% | 0% |
| HYPE | 614 | 11.3s | 4% | 0% |
| NEAR | 755 | 10.8s | 4% | 0% |
| SOL | 1373 | 10.8s | 3% | 0% |
| XRP | 1394 | 11.0s | 4% | 0% |
| ZEC | 884 | 9.6s | 4% | 0% |
| **All** | **7745** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 11:04:21 | SOL | up | 0.29→0.41 | 0.23 → 0.29 | 9.58s | UP @ 0.29 | -0.59 / · / · |
| 10-04 11:04:18 | NEAR | up | 0.33→0.40 | 0.46 → 0.48 | no | edge gone |  |
| 10-04 11:03:36 | BTC | up | 0.25→0.30 | 0.24 → 0.24 | no | UP @ 0.25 | -0.65 / -1.03 / · |
| 10-04 11:02:58 | NEAR | down | 0.22→0.16 | 0.74 → 0.84 | 17.11s | edge gone |  |
| 10-04 11:02:42 | ETH | down | 0.38→0.32 | 0.77 → 0.71 | no | edge gone |  |
| 10-04 11:02:20 | SOL | down | 0.36→0.30 | 0.67 → 0.71 | 10.61s | edge gone |  |
| 10-04 11:02:09 | XRP | down | 0.23→0.18 | 0.80 → 0.86 | 6.12s | edge gone |  |
| 10-04 11:02:03 | SOL | down | 0.42→0.36 | 0.53 → 0.58 | 0.35s | edge gone |  |
| 10-04 11:02:00 | DOGE | down | 0.45→0.33 | 0.55 → 0.63 | 15.87s | edge gone |  |
| 10-04 11:01:59 | NEAR | up | 0.26→0.31 | 0.30 → 0.36 | 16.62s | spread too wide |  |
| 10-04 11:01:44 | ZEC | down | 0.65→0.59 | 0.24 → 0.35 | 1.87s | DOWN @ 0.36 | 1.06 / 2.68 / · |
| 10-04 11:01:21 | NEAR | down | 0.39→0.33 | 0.61 → 0.67 | 19.16s | edge gone |  |
| 10-04 11:01:21 | ETH | up | 0.41→0.52 | 0.41 → 0.54 | no | edge gone |  |
| 10-04 11:01:19 | XRP | down | 0.38→0.31 | 0.67 → 0.75 | 21.41s | edge gone |  |
| 10-04 11:00:59 | XRP | down | 0.48→0.42 | 0.57 → 0.65 | 11.39s | edge gone |  |
| 10-04 11:00:47 | HYPE | up | 0.44→0.53 | 0.51 → 0.55 | no | edge gone |  |
| 10-04 10:58:34 | XRP | up | 0.85→0.93 | 0.87 → 0.97 | 0.16s | price out of range |  |
| 10-04 10:58:21 | ETH | down | 0.22→0.14 | 0.81 → 0.93 | 12.93s | edge gone |  |
| 10-04 10:58:14 | XRP | down | 0.70→0.64 | 0.30 → 0.28 | no | DOWN @ 0.28 | -1.16 / -2.60 / -2.95 |
| 10-04 10:58:09 | NEAR | down | 0.97→0.92 | 0.01 → 0.02 | no | price out of range |  |
| 10-04 10:58:03 | ETH | up | 0.25→0.31 | 0.24 → 0.14 | no | UP @ 0.14 | -0.18 / -1.26 / -1.49 |
| 10-04 10:57:59 | XRP | up | 0.62→0.68 | 0.73 → 0.65 | 19.44s | spread too wide |  |
| 10-04 10:57:50 | ZEC | down | 0.95→0.85 | 0.01 → 0.03 | no | DOWN @ 0.06 | -0.48 / -0.60 / -0.65 |
| 10-04 10:57:41 | BTC | down | 0.18→0.11 | 0.94 → 0.97 | no | price out of range |  |
| 10-04 10:57:38 | ETH | down | 0.41→0.34 | 0.67 → 0.67 | 10.94s | edge gone |  |
| 10-04 10:57:36 | NEAR | up | 0.86→0.91 | 0.97 → 0.98 | 13.45s | price out of range |  |
| 10-04 10:57:34 | XRP | down | 0.84→0.76 | 0.14 → 0.19 | 15.20s | DOWN @ 0.20 | 0.64 / 0.25 / -2.11 |
| 10-04 10:57:26 | HYPE | down | 0.44→0.38 | 0.71 → 0.83 | 8.45s | edge gone |  |
| 10-04 10:57:22 | DOGE | up | 0.18→0.26 | 0.16 → 0.09 | no | UP @ 0.09 | -0.51 / -0.59 / -0.91 |
| 10-04 10:57:20 | SOL | down | 0.18→0.12 | 0.90 → 0.91 | 14.20s | edge gone |  |
