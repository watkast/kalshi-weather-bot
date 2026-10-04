# Lag Tracker

*Updated Sun Oct 04 14:15 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$346.77** | -24.3% | 391 | $3.65 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 391 | 67 | -$168.90 | -11.8% | -$90.21 / -$78.69 |
| Sell after 30 sec | 391 | 91 | -$191.26 | -13.4% | -$95.78 / -$95.48 |
| Hold to the close | 391 | 108 | -$346.77 | -24.3% | -$217.13 / -$129.64 |
| Hold, only edge 10¢+ | 138 | 23 | -$143.01 | -38.3% | -$127.76 / -$15.25 |
| Hold, first trade per window only | 134 | 45 | -$84.80 | -15.9% | -$30.48 / -$54.32 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 1451 | 11% | 65% | +4.4¢ | 0.3¢ | edge gone 993, price out of range 39, spread too wide 28 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 676 | 11.1s | 3% | 0% |
| BTC | 704 | 11.9s | 3% | 0% |
| DOGE | 809 | 10.5s | 2% | 0% |
| ETH | 850 | 11.2s | 4% | 0% |
| HYPE | 660 | 11.5s | 3% | 0% |
| NEAR | 847 | 10.8s | 4% | 0% |
| SOL | 1597 | 10.9s | 3% | 0% |
| XRP | 1596 | 11.0s | 4% | 0% |
| ZEC | 979 | 9.7s | 4% | 0% |
| **All** | **8718** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 14:15:31 | HYPE | down | 0.54→0.48 | 0.54 → 0.56 | no | edge gone |  |
| 10-04 14:13:21 | XRP | up | 0.03→0.16 | 0.05 → 0.05 | no | price out of range |  |
| 10-04 14:13:15 | SOL | down | 0.21→0.16 | 0.83 → 0.87 | 25.89s | edge gone |  |
| 10-04 14:12:55 | SOL | up | 0.07→0.19 | 0.11 → 0.16 | 15.64s | edge gone |  |
| 10-04 14:12:30 | SOL | down | 0.19→0.10 | 0.76 → 0.89 | 10.64s | edge gone |  |
| 10-04 14:12:06 | SOL | up | 0.06→0.21 | 0.05 → 0.23 | 5.15s | edge gone |  |
| 10-04 14:12:06 | XRP | up | 0.01→0.09 | 0.03 → 0.14 | 5.15s | UP @ 0.14 | -0.77 / -0.85 / -1.49 |
| 10-04 14:11:11 | DOGE | down | 0.31→0.07 | 0.86 → 0.90 | 14.91s | edge gone |  |
| 10-04 14:11:05 | SOL | down | 0.13→0.08 | 0.87 → 0.94 | 5.91s | edge gone |  |
| 10-04 14:10:28 | XRP | up | 0.10→0.15 | 0.12 → 0.13 | no | edge gone |  |
| 10-04 14:10:23 | BTC | down | 0.11→0.06 | 0.84 → 0.95 | 3.17s | edge gone |  |
| 10-04 14:10:12 | SOL | up | 0.18→0.26 | 0.22 → 0.26 | no | edge gone |  |
| 10-04 14:09:57 | SOL | down | 0.24→0.13 | 0.81 → 0.78 | no | DOWN @ 0.78 | -0.26 / 0.48 / 2.07 |
| 10-04 14:09:46 | XRP | up | 0.08→0.13 | 0.06 → 0.11 | 24.43s | edge gone |  |
| 10-04 14:09:33 | SOL | down | 0.25→0.20 | 0.78 → 0.81 | 8.18s | edge gone |  |
| 10-04 14:09:09 | DOGE | up | 0.31→0.39 | 0.30 → 0.28 | no | UP @ 0.28 | -0.34 / -0.44 / -3.00 |
| 10-04 14:08:46 | SOL | down | 0.41→0.35 | 0.47 → 0.65 | 10.19s | edge gone |  |
| 10-04 14:08:27 | XRP | up | 0.09→0.15 | 0.08 → 0.11 | no | edge gone |  |
| 10-04 14:08:27 | BTC | up | 0.17→0.24 | 0.19 → 0.27 | no | edge gone |  |
| 10-04 14:08:22 | SOL | up | 0.27→0.33 | 0.27 → 0.34 | 4.20s | edge gone |  |
| 10-04 14:08:08 | BTC | down | 0.23→0.17 | 0.78 → 0.79 | 17.45s | DOWN @ 0.79 | 0.07 / -0.55 / 1.98 |
| 10-04 14:07:53 | DOGE | down | 0.40→0.32 | 0.71 → 0.74 | no | edge gone |  |
| 10-04 14:07:46 | BTC | down | 0.26→0.21 | 0.74 → 0.77 | 9.71s | edge gone |  |
| 10-04 14:07:35 | DOGE | up | 0.26→0.33 | 0.31 → 0.29 | no | edge gone |  |
| 10-04 14:07:22 | BTC | down | 0.36→0.30 | 0.59 → 0.69 | 3.71s | edge gone |  |
| 10-04 14:07:11 | HYPE | down | 0.26→0.20 | 0.78 → 0.81 | 14.72s | edge gone |  |
| 10-04 14:06:42 | ETH | down | 0.13→0.07 | 0.91 → 0.93 | 0.20s | edge gone |  |
| 10-04 14:06:41 | BTC | down | 0.50→0.42 | 0.48 → 0.60 | 14.97s | edge gone |  |
| 10-04 14:06:39 | XRP | down | 0.31→0.25 | 0.75 → 0.82 | 16.97s | edge gone |  |
| 10-04 14:06:39 | NEAR | down | 0.12→0.07 | 0.81 → 0.78 | no | DOWN @ 0.80 | -0.42 / -0.83 / 1.91 |
