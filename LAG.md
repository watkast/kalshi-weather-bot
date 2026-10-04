# Lag Tracker

*Updated Sun Oct 04 15:35 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

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
| Sell after 10 sec | 499 | 85 | -$204.17 | -11.1% | -$106.32 / -$97.85 |
| Sell after 30 sec | 499 | 123 | -$231.72 | -12.6% | -$118.59 / -$113.13 |
| Hold to the close | 495 | 147 | -$353.52 | -19.4% | -$272.91 / -$80.61 |
| Hold, only edge 10¢+ | 177 | 37 | -$110.76 | -23.0% | -$115.20 / $4.44 |
| Hold, first trade per window only | 168 | 58 | -$110.14 | -16.0% | -$46.09 / -$64.05 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 1958 | 10% | 67% | +5.0¢ | 0.3¢ | edge gone 1359, price out of range 53, spread too wide 47 |

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
| BTC | 775 | 11.9s | 3% | 0% |
| DOGE | 848 | 10.6s | 3% | 0% |
| ETH | 917 | 10.9s | 4% | 0% |
| HYPE | 687 | 11.6s | 3% | 0% |
| NEAR | 888 | 10.8s | 4% | 0% |
| SOL | 1678 | 10.8s | 3% | 0% |
| XRP | 1707 | 11.1s | 3% | 0% |
| ZEC | 1036 | 9.6s | 4% | 0% |
| **All** | **9225** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **19 ms** · Order book check: **24 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 15:35:18 | ETH | down | 0.48→0.42 | 0.55 → 0.62 | 8.34s | edge gone |  |
| 10-04 15:35:18 | XRP | down | 0.40→0.33 | 0.65 → 0.68 | no | edge gone |  |
| 10-04 15:35:18 | BTC | down | 0.34→0.29 | 0.68 → 0.75 | 8.59s | edge gone |  |
| 10-04 15:34:56 | XRP | down | 0.47→0.38 | 0.54 → 0.64 | 15.85s | edge gone |  |
| 10-04 15:34:53 | SOL | up | 0.46→0.53 | 0.44 → 0.53 | 3.34s | edge gone |  |
| 10-04 15:34:48 | NEAR | down | 0.68→0.62 | 0.18 → 0.26 | 8.60s | DOWN @ 0.26 | -0.76 / -1.05 / · |
| 10-04 15:34:38 | SOL | up | 0.40→0.47 | 0.43 → 0.44 | 18.35s | edge gone |  |
| 10-04 15:34:18 | XRP | up | 0.45→0.50 | 0.46 → 0.48 | no | edge gone |  |
| 10-04 15:34:03 | XRP | down | 0.53→0.45 | 0.58 → 0.54 | no | edge gone |  |
| 10-04 15:33:59 | SOL | up | 0.36→0.45 | 0.40 → 0.45 | no | edge gone |  |
| 10-04 15:33:44 | SOL | down | 0.43→0.37 | 0.56 → 0.57 | no | DOWN @ 0.57 | -0.05 / -0.36 / · |
| 10-04 15:33:17 | NEAR | up | 0.50→0.65 | 0.65 → 0.76 | 9.37s | edge gone |  |
| 10-04 15:33:06 | BTC | down | 0.44→0.37 | 0.61 → 0.62 | no | edge gone |  |
| 10-04 15:33:06 | SOL | down | 0.41→0.34 | 0.60 → 0.62 | no | edge gone |  |
| 10-04 15:33:06 | ETH | down | 0.47→0.39 | 0.54 → 0.64 | 5.87s | edge gone |  |
| 10-04 15:33:06 | XRP | down | 0.50→0.44 | 0.48 → 0.58 | 6.12s | edge gone |  |
| 10-04 15:33:02 | NEAR | down | 0.57→0.52 | 0.35 → 0.31 | no | DOWN @ 0.35 | -0.31 / -1.74 / · |
| 10-04 15:32:43 | XRP | down | 0.55→0.48 | 0.42 → 0.48 | 13.88s | edge gone |  |
| 10-04 15:32:11 | SOL | down | 0.53→0.47 | 0.52 → 0.50 | no | edge gone |  |
| 10-04 15:31:50 | ETH | down | 0.50→0.44 | 0.53 → 0.56 | 6.89s | edge gone |  |
| 10-04 15:31:35 | XRP | down | 0.60→0.55 | 0.57 → 0.44 | no | edge gone |  |
| 10-04 15:31:29 | SOL | up | 0.42→0.49 | 0.45 → 0.52 | 12.66s | edge gone |  |
| 10-04 15:31:29 | BNB | up | 0.29→0.38 | 0.44 → 0.49 | 12.91s | edge gone |  |
| 10-04 15:31:23 | BTC | up | 0.32→0.38 | 0.34 → 0.37 | 18.41s | edge gone |  |
| 10-04 15:31:17 | DOGE | up | 0.42→0.48 | 0.44 → 0.52 | 10.15s | edge gone |  |
| 10-04 15:31:16 | XRP | up | 0.41→0.48 | 0.49 → 0.51 | 25.41s | edge gone |  |
| 10-04 15:31:15 | NEAR | up | 0.38→0.57 | 0.57 → 0.69 | 11.90s | edge gone |  |
| 10-04 15:31:12 | ETH | down | 0.42→0.34 | 0.60 → 0.63 | no | edge gone |  |
| 10-04 15:31:11 | ZEC | down | 0.38→0.30 | 0.65 → 0.75 | 0.65s | spread too wide |  |
| 10-04 15:30:45 | BTC | down | 0.45→0.40 | 0.55 → 0.63 | 11.65s | edge gone |  |
