# Lag Tracker

*Updated Sun Oct 04 13:25 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$365.28** | -34.6% | 302 | $3.55 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 316 | 54 | -$137.60 | -12.3% | -$67.36 / -$70.24 |
| Sell after 30 sec | 316 | 69 | -$162.30 | -14.5% | -$69.45 / -$92.85 |
| Hold to the close | 302 | 69 | -$365.28 | -34.6% | -$103.86 / -$261.42 |
| Hold, only edge 10¢+ | 109 | 14 | -$140.77 | -50.1% | -$91.90 / -$48.87 |
| Hold, first trade per window only | 105 | 31 | -$89.87 | -22.5% | -$15.61 / -$74.26 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 1201 | 10% | 65% | +5.0¢ | 0.3¢ | edge gone 826, price out of range 34, spread too wide 25 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 672 | 11.1s | 3% | 0% |
| BTC | 662 | 11.9s | 3% | 0% |
| DOGE | 796 | 10.6s | 3% | 0% |
| ETH | 819 | 11.2s | 4% | 0% |
| HYPE | 648 | 11.3s | 4% | 0% |
| NEAR | 828 | 10.8s | 4% | 0% |
| SOL | 1543 | 11.0s | 3% | 0% |
| XRP | 1537 | 10.9s | 4% | 0% |
| ZEC | 963 | 9.7s | 4% | 0% |
| **All** | **8468** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **22 ms** · Order book check: **49 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 13:25:20 | XRP | down | 0.88→0.83 | 0.17 → 0.16 | no | edge gone |  |
| 10-04 13:25:11 | ZEC | down | 0.18→0.13 | 0.84 → 0.90 | 11.58s | edge gone |  |
| 10-04 13:24:44 | NEAR | up | 0.08→0.13 | 0.21 → 0.28 | 9.34s | edge gone |  |
| 10-04 13:24:39 | SOL | up | 0.41→0.50 | 0.50 → 0.58 | 13.84s | edge gone |  |
| 10-04 13:24:30 | XRP | up | 0.77→0.83 | 0.89 → 0.80 | no | edge gone |  |
| 10-04 13:24:20 | SOL | up | 0.38→0.46 | 0.54 → 0.52 | no | edge gone |  |
| 10-04 13:24:18 | DOGE | down | 0.72→0.64 | 0.27 → 0.39 | 21.87s | edge gone |  |
| 10-04 13:24:05 | ZEC | down | 0.40→0.33 | 0.66 → 0.67 | 20.35s | spread too wide |  |
| 10-04 13:24:04 | BTC | up | 0.81→0.87 | 0.85 → 0.88 | 20.85s | edge gone |  |
| 10-04 13:23:54 | XRP | up | 0.82→0.89 | 0.85 → 0.86 | no | edge gone |  |
| 10-04 13:23:47 | SOL | down | 0.57→0.50 | 0.31 → 0.47 | 8.35s | edge gone |  |
| 10-04 13:23:31 | XRP | up | 0.78→0.84 | 0.84 → 0.85 | no | edge gone |  |
| 10-04 13:23:15 | XRP | up | 0.75→0.81 | 0.81 → 0.79 | 9.86s | edge gone |  |
| 10-04 13:22:57 | SOL | up | 0.57→0.63 | 0.67 → 0.70 | 12.37s | edge gone |  |
| 10-04 13:22:35 | XRP | up | 0.77→0.82 | 0.78 → 0.81 | 4.37s | edge gone |  |
| 10-04 13:22:35 | SOL | down | 0.63→0.57 | 0.40 → 0.36 | no | DOWN @ 0.36 | -0.39 / -0.87 / · |
| 10-04 13:22:29 | ZEC | up | 0.26→0.36 | 0.27 → 0.38 | 10.37s | edge gone |  |
| 10-04 13:22:15 | BTC | down | 0.76→0.68 | 0.18 → 0.17 | no | DOWN @ 0.17 | -0.20 / -0.11 / · |
| 10-04 13:22:11 | SOL | up | 0.33→0.46 | 0.44 → 0.58 | 0.11s | edge gone |  |
| 10-04 13:21:58 | ZEC | down | 0.50→0.42 | 0.44 → 0.52 | 11.66s | edge gone |  |
| 10-04 13:21:57 | XRP | up | 0.76→0.81 | 0.82 → 0.84 | 12.91s | edge gone |  |
| 10-04 13:21:37 | XRP | down | 0.78→0.72 | 0.33 → 0.26 | no | edge gone |  |
| 10-04 13:21:21 | XRP | up | 0.69→0.75 | 0.54 → 0.73 | 3.39s | edge gone |  |
| 10-04 13:21:21 | SOL | up | 0.25→0.31 | 0.23 → 0.32 | 18.64s | edge gone |  |
| 10-04 13:21:15 | DOGE | up | 0.42→0.53 | 0.57 → 0.63 | 9.89s | edge gone |  |
| 10-04 13:21:10 | ZEC | up | 0.53→0.60 | 0.58 → 0.61 | no | edge gone |  |
| 10-04 13:21:06 | XRP | up | 0.56→0.63 | 0.52 → 0.54 | 18.40s | UP @ 0.55 | 0.72 / 1.63 / · |
| 10-04 13:21:05 | BTC | up | 0.66→0.77 | 0.71 → 0.77 | 20.15s | edge gone |  |
| 10-04 13:20:56 | BNB | down | 0.44→0.33 | 0.40 → 0.40 | no | DOWN @ 0.41 | -0.77 / -1.70 / · |
| 10-04 13:20:51 | XRP | up | 0.56→0.62 | 0.53 → 0.55 | no | UP @ 0.55 | -0.76 / 1.37 / · |
