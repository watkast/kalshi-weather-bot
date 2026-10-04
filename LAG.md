# Lag Tracker

*Updated Sun Oct 04 20:46 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$206.64** | -5.1% | 1033 | $3.96 | $185.87 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1034 | 166 | -$456.06 | -11.1% | -$210.92 / -$245.14 |
| Sell after 30 sec | 1034 | 265 | -$490.45 | -12.0% | -$232.34 / -$258.11 |
| Hold to the close | 1033 | 388 | -$206.64 | -5.1% | -$316.34 / $109.70 |
| Hold, only edge 10¢+ | 368 | 102 | -$149.07 | -12.8% | -$76.12 / -$72.95 |
| Hold, first trade per window only | 321 | 130 | -$43.72 | -3.3% | -$98.69 / $54.97 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 3841 | 10% | 65% | +4.0¢ | 0.3¢ | edge gone 2619, price out of range 101, spread too wide 87 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 763 | 11.1s | 3% | 0% |
| BTC | 950 | 11.9s | 3% | 0% |
| DOGE | 1027 | 10.8s | 3% | 0% |
| ETH | 1162 | 10.9s | 4% | 0% |
| HYPE | 776 | 11.6s | 3% | 0% |
| NEAR | 1115 | 10.8s | 4% | 0% |
| SOL | 2018 | 10.9s | 3% | 0% |
| XRP | 2087 | 11.0s | 3% | 0% |
| ZEC | 1210 | 9.7s | 4% | 0% |
| **All** | **11108** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **6 ms** · Order book check: **61 ms** · Coinbase price delay: **34 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 20:46:23 | DOGE | down | 0.42→0.33 | 0.63 → 0.62 | no | edge gone |  |
| 10-04 20:46:19 | BTC | up | 0.38→0.44 | 0.37 → 0.44 | 6.52s | edge gone |  |
| 10-04 20:45:58 | BTC | down | 0.41→0.35 | 0.60 → 0.67 | no | edge gone |  |
| 10-04 20:45:56 | BNB | up | 0.32→0.40 | 0.52 → 0.52 | no | edge gone |  |
| 10-04 20:45:54 | ETH | up | 0.37→0.44 | 0.40 → 0.43 | no | edge gone |  |
| 10-04 20:45:49 | XRP | down | 0.40→0.32 | 0.59 → 0.63 | 21.79s | DOWN @ 0.63 | -0.13 / -1.05 / · |
| 10-04 20:43:42 | DOGE | up | 0.25→0.32 | 0.34 → 0.33 | 14.32s | edge gone |  |
| 10-04 20:43:40 | SOL | down | 0.97→0.90 | 0.07 → 0.02 | no | price out of range |  |
| 10-04 20:43:23 | BNB | up | 0.42→0.48 | 0.83 → 0.95 | 4.07s | edge gone |  |
| 10-04 20:43:16 | ETH | up | 0.83→0.88 | 0.63 → 0.80 | 11.08s | UP @ 0.80 | 0.76 / 1.28 / 1.88 |
| 10-04 20:43:11 | SOL | up | 0.69→0.90 | 0.85 → 0.87 | 30.58s | edge gone |  |
| 10-04 20:43:01 | DOGE | up | 0.16→0.26 | 0.17 → 0.29 | 26.08s | edge gone |  |
| 10-04 20:42:59 | ETH | up | 0.56→0.61 | 0.53 → 0.56 | 12.83s | edge gone |  |
| 10-04 20:42:51 | SOL | up | 0.67→0.72 | 0.83 → 0.79 | 5.33s | edge gone |  |
| 10-04 20:42:43 | ETH | down | 0.56→0.48 | 0.40 → 0.48 | no | edge gone |  |
| 10-04 20:42:28 | ETH | down | 0.51→0.42 | 0.54 → 0.52 | no | DOWN @ 0.52 | -1.45 / -1.16 / -5.38 |
| 10-04 20:42:22 | NEAR | down | 0.33→0.24 | 0.34 → 0.50 | 5.09s | DOWN @ 0.51 | -1.25 / 0.66 / 4.73 |
| 10-04 20:42:21 | SOL | down | 0.69→0.56 | 0.17 → 0.23 | no | DOWN @ 0.23 | -0.93 / -0.45 / -2.43 |
| 10-04 20:42:03 | ETH | down | 0.65→0.50 | 0.35 → 0.58 | 9.10s | edge gone |  |
| 10-04 20:41:59 | SOL | down | 0.78→0.51 | 0.13 → 0.12 | no | DOWN @ 0.12 | 0.65 / 0.34 / -1.28 |
| 10-04 20:41:48 | ETH | up | 0.59→0.64 | 0.62 → 0.68 | 9.10s | edge gone |  |
| 10-04 20:41:20 | NEAR | up | 0.46→0.54 | 0.73 → 0.79 | no | edge gone |  |
| 10-04 20:41:19 | SOL | up | 0.70→0.76 | 0.83 → 0.88 | 22.61s | edge gone |  |
| 10-04 20:41:11 | ETH | down | 0.69→0.63 | 0.34 → 0.48 | 15.61s | edge gone |  |
| 10-04 20:40:52 | NEAR | up | 0.48→0.63 | 0.70 → 0.75 | no | edge gone |  |
| 10-04 20:40:50 | SOL | up | 0.68→0.75 | 0.77 → 0.79 | 7.12s | edge gone |  |
| 10-04 20:40:46 | DOGE | up | 0.43→0.50 | 0.66 → 0.52 | no | edge gone |  |
| 10-04 20:40:38 | XRP | down | 0.13→0.08 | 0.84 → 0.81 | no | DOWN @ 0.81 | -0.74 / -0.33 / 1.79 |
| 10-04 20:40:35 | BNB | down | 0.29→0.16 | 0.58 → 0.56 | no | DOWN @ 0.56 | -1.16 / -1.60 / -5.78 |
| 10-04 20:40:20 | NEAR | up | 0.49→0.58 | 0.71 → 0.70 | no | edge gone |  |
