# Lag Tracker

*Updated Sun Oct 04 20:07 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$246.71** | -6.3% | 982 | $3.97 | $185.87 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 987 | 157 | -$432.70 | -11.1% | -$202.12 / -$230.58 |
| Sell after 30 sec | 987 | 251 | -$467.69 | -11.9% | -$228.90 / -$238.79 |
| Hold to the close | 982 | 364 | -$246.71 | -6.3% | -$353.69 / $106.98 |
| Hold, only edge 10¢+ | 347 | 92 | -$174.48 | -15.9% | -$102.87 / -$71.61 |
| Hold, first trade per window only | 300 | 121 | -$47.13 | -3.7% | -$99.12 / $51.99 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 3640 | 10% | 66% | +4.0¢ | 0.3¢ | edge gone 2478, price out of range 96, spread too wide 79 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 751 | 11.1s | 3% | 0% |
| BTC | 932 | 11.9s | 3% | 0% |
| DOGE | 1008 | 10.8s | 3% | 0% |
| ETH | 1138 | 10.9s | 4% | 0% |
| HYPE | 762 | 11.6s | 3% | 0% |
| NEAR | 1088 | 10.8s | 4% | 0% |
| SOL | 1976 | 10.9s | 3% | 0% |
| XRP | 2059 | 11.0s | 3% | 0% |
| ZEC | 1193 | 9.7s | 4% | 0% |
| **All** | **10907** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **7 ms** · Order book check: **28 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 20:07:05 | XRP | down | 0.22→0.17 | 0.80 → 0.80 | no | edge gone |  |
| 10-04 20:06:37 | XRP | down | 0.23→0.18 | 0.79 → 0.83 | no | edge gone |  |
| 10-04 20:06:36 | ZEC | down | 0.33→0.24 | 0.62 → 0.80 | 12.56s | edge gone |  |
| 10-04 20:06:31 | HYPE | up | 0.46→0.55 | 0.52 → 0.55 | no | edge gone |  |
| 10-04 20:06:29 | BNB | up | 0.13→0.25 | 0.40 → 0.39 | no | edge gone |  |
| 10-04 20:06:00 | ETH | down | 0.30→0.22 | 0.73 → 0.78 | 18.82s | edge gone |  |
| 10-04 20:05:47 | DOGE | down | 0.45→0.38 | 0.53 → 0.62 | 1.32s | edge gone |  |
| 10-04 20:05:46 | XRP | up | 0.26→0.32 | 0.33 → 0.30 | no | edge gone |  |
| 10-04 20:05:46 | BTC | up | 0.36→0.41 | 0.37 → 0.35 | no | UP @ 0.35 | -0.42 / -0.81 / · |
| 10-04 20:05:01 | ETH | down | 0.43→0.36 | 0.59 → 0.73 | 17.84s | edge gone |  |
| 10-04 20:05:00 | XRP | down | 0.38→0.29 | 0.59 → 0.66 | 3.58s | edge gone |  |
| 10-04 20:05:00 | BTC | down | 0.48→0.43 | 0.53 → 0.63 | 18.59s | edge gone |  |
| 10-04 20:04:46 | SOL | down | 0.13→0.07 | 0.71 → 0.75 | 17.59s | DOWN @ 0.75 | 0.35 / 0.77 / · |
| 10-04 20:04:23 | NEAR | up | 0.21→0.27 | 0.29 → 0.30 | no | edge gone |  |
| 10-04 20:04:03 | DOGE | down | 0.56→0.50 | 0.49 → 0.46 | no | edge gone |  |
| 10-04 20:03:51 | HYPE | up | 0.42→0.55 | 0.47 → 0.49 | 12.60s | UP @ 0.49 | 1.26 / 1.26 / · |
| 10-04 20:03:51 | XRP | up | 0.35→0.41 | 0.39 → 0.41 | 13.10s | edge gone |  |
| 10-04 20:03:34 | ZEC | up | 0.39→0.44 | 0.53 → 0.49 | no | edge gone |  |
| 10-04 20:03:32 | DOGE | up | 0.50→0.56 | 0.60 → 0.57 | no | edge gone |  |
| 10-04 20:03:31 | XRP | down | 0.46→0.35 | 0.59 → 0.62 | no | edge gone |  |
| 10-04 20:03:31 | BTC | down | 0.59→0.54 | 0.43 → 0.53 | 17.86s | edge gone |  |
| 10-04 20:03:31 | ETH | down | 0.50→0.39 | 0.56 → 0.65 | 17.86s | edge gone |  |
| 10-04 20:03:09 | XRP | down | 0.46→0.41 | 0.56 → 0.59 | 9.61s | edge gone |  |
| 10-04 20:02:54 | XRP | up | 0.39→0.45 | 0.44 → 0.45 | no | edge gone |  |
| 10-04 20:02:52 | DOGE | up | 0.54→0.62 | 0.54 → 0.59 | 11.62s | edge gone |  |
| 10-04 20:02:52 | NEAR | up | 0.25→0.33 | 0.38 → 0.38 | no | edge gone |  |
| 10-04 20:02:40 | ETH | down | 0.54→0.49 | 0.49 → 0.54 | 8.87s | edge gone |  |
| 10-04 20:02:39 | XRP | down | 0.48→0.39 | 0.51 → 0.56 | 9.62s | edge gone |  |
| 10-04 20:02:24 | HYPE | up | 0.31→0.38 | 0.27 → 0.47 | 9.87s | edge gone |  |
| 10-04 20:02:20 | XRP | up | 0.16→0.52 | 0.19 → 0.55 | 13.63s | UP @ 0.55 | -0.96 / -1.85 / · |
