# Lag Tracker

*Updated Sun Oct 04 18:06 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$182.60** | -6.5% | 750 | $3.78 | $145.64 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 761 | 124 | -$321.65 | -11.2% | -$165.91 / -$155.74 |
| Sell after 30 sec | 760 | 200 | -$325.04 | -11.3% | -$190.14 / -$134.90 |
| Hold to the close | 750 | 263 | -$182.60 | -6.5% | -$347.49 / $164.89 |
| Hold, only edge 10¢+ | 262 | 66 | -$86.87 | -11.6% | -$147.58 / $60.71 |
| Hold, first trade per window only | 241 | 95 | -$24.20 | -2.5% | -$80.88 / $56.68 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 2848 | 10% | 67% | +4.7¢ | 0.3¢ | edge gone 1948, price out of range 74, spread too wide 65 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 719 | 11.1s | 3% | 0% |
| BTC | 853 | 11.9s | 3% | 0% |
| DOGE | 947 | 10.7s | 3% | 0% |
| ETH | 1043 | 10.8s | 4% | 0% |
| HYPE | 721 | 11.6s | 3% | 0% |
| NEAR | 986 | 10.8s | 3% | 0% |
| SOL | 1830 | 10.8s | 3% | 0% |
| XRP | 1903 | 11.2s | 3% | 0% |
| ZEC | 1113 | 9.6s | 4% | 0% |
| **All** | **10115** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **8 ms** · Order book check: **26 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 18:06:17 | XRP | up | 0.26→0.39 | 0.38 → 0.42 | no | edge gone |  |
| 10-04 18:06:11 | HYPE | down | 0.64→0.57 | 0.25 → 0.37 | no | DOWN @ 0.37 | -1.05 / · / · |
| 10-04 18:06:01 | BTC | down | 0.73→0.62 | 0.25 → 0.37 | 8.56s | edge gone |  |
| 10-04 18:06:00 | ETH | down | 0.47→0.38 | 0.44 → 0.69 | 9.56s | edge gone |  |
| 10-04 18:06:00 | ZEC | down | 0.52→0.45 | 0.48 → 0.55 | 9.56s | edge gone |  |
| 10-04 18:05:58 | XRP | up | 0.37→0.42 | 0.50 → 0.49 | no | edge gone |  |
| 10-04 18:05:43 | XRP | down | 0.45→0.39 | 0.71 → 0.52 | no | DOWN @ 0.52 | -0.66 / 1.06 / · |
| 10-04 18:05:38 | BTC | up | 0.64→0.73 | 0.66 → 0.75 | 1.31s | edge gone |  |
| 10-04 18:05:27 | XRP | up | 0.19→0.25 | 0.30 → 0.31 | 27.82s | edge gone |  |
| 10-04 18:05:19 | NEAR | up | 0.39→0.45 | 0.48 → 0.50 | no | spread too wide |  |
| 10-04 18:05:05 | ETH | up | 0.39→0.46 | 0.37 → 0.41 | no | UP @ 0.41 | -0.49 / 0.35 / · |
| 10-04 18:05:03 | BNB | up | 0.33→0.40 | 0.59 → 0.68 | 6.82s | edge gone |  |
| 10-04 18:05:01 | XRP | up | 0.16→0.22 | 0.26 → 0.27 | 8.32s | edge gone |  |
| 10-04 18:04:32 | BTC | up | 0.59→0.64 | 0.65 → 0.68 | 7.83s | edge gone |  |
| 10-04 18:04:26 | XRP | down | 0.22→0.17 | 0.75 → 0.74 | no | DOWN @ 0.74 | -0.38 / -0.28 / · |
| 10-04 18:04:21 | DOGE | up | 0.40→0.46 | 0.42 → 0.50 | 18.33s | edge gone |  |
| 10-04 18:04:18 | ETH | up | 0.32→0.38 | 0.28 → 0.43 | 6.33s | edge gone |  |
| 10-04 18:04:18 | ZEC | up | 0.40→0.45 | 0.33 → 0.39 | 6.58s | edge gone |  |
| 10-04 18:04:01 | BTC | down | 0.58→0.50 | 0.37 → 0.49 | no | edge gone |  |
| 10-04 18:04:01 | DOGE | down | 0.48→0.43 | 0.54 → 0.63 | 8.84s | edge gone |  |
| 10-04 18:04:01 | SOL | down | 0.24→0.09 | 0.72 → 0.80 | 9.09s | DOWN @ 0.80 | 0.08 / 0.18 / · |
| 10-04 18:04:00 | BNB | down | 0.41→0.34 | 0.35 → 0.43 | 9.34s | DOWN @ 0.43 | -0.55 / -0.65 / · |
| 10-04 18:03:46 | XRP | down | 0.27→0.21 | 0.69 → 0.70 | 23.34s | DOWN @ 0.70 | -0.30 / 0.11 / · |
| 10-04 18:03:46 | DOGE | down | 0.58→0.53 | 0.41 → 0.45 | 8.84s | edge gone |  |
| 10-04 18:03:17 | BTC | down | 0.60→0.51 | 0.47 → 0.37 | no | DOWN @ 0.37 | -0.53 / -0.44 / · |
| 10-04 18:03:09 | DOGE | up | 0.38→0.43 | 0.36 → 0.42 | 15.85s | edge gone |  |
| 10-04 18:03:08 | XRP | up | 0.19→0.24 | 0.31 → 0.29 | no | edge gone |  |
| 10-04 18:03:02 | ETH | down | 0.42→0.34 | 0.60 → 0.67 | 8.10s | edge gone |  |
| 10-04 18:03:00 | BTC | down | 0.65→0.58 | 0.33 → 0.42 | 9.60s | edge gone |  |
| 10-04 18:02:52 | SOL | up | 0.24→0.29 | 0.33 → 0.33 | no | edge gone |  |
