# Lag Tracker

*Updated Sun Oct 04 17:46 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$326.96** | -12.3% | 716 | $3.72 | $143.33 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 716 | 117 | -$298.42 | -11.2% | -$151.87 / -$146.55 |
| Sell after 30 sec | 716 | 187 | -$314.22 | -11.8% | -$174.14 / -$140.08 |
| Hold to the close | 716 | 234 | -$326.96 | -12.3% | -$365.22 / $38.26 |
| Hold, only edge 10¢+ | 254 | 60 | -$124.42 | -17.2% | -$151.31 / $26.89 |
| Hold, first trade per window only | 233 | 88 | -$60.45 | -6.4% | -$93.25 / $32.80 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 2706 | 10% | 67% | +4.7¢ | 0.3¢ | edge gone 1855, price out of range 74, spread too wide 61 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 716 | 11.1s | 3% | 0% |
| BTC | 837 | 11.9s | 3% | 0% |
| DOGE | 926 | 10.6s | 3% | 0% |
| ETH | 1023 | 10.8s | 4% | 0% |
| HYPE | 720 | 11.6s | 3% | 0% |
| NEAR | 982 | 10.9s | 3% | 0% |
| SOL | 1813 | 10.8s | 3% | 0% |
| XRP | 1864 | 11.2s | 3% | 0% |
| ZEC | 1092 | 9.7s | 4% | 0% |
| **All** | **9973** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **7 ms** · Order book check: **26 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 17:46:07 | ZEC | up | 0.64→0.75 | 0.79 → 0.85 | 0.26s | edge gone |  |
| 10-04 17:46:02 | SOL | up | 0.55→0.61 | 0.65 → 0.70 | 4.28s | edge gone |  |
| 10-04 17:46:01 | DOGE | up | 0.61→0.69 | 0.62 → 0.68 | no | edge gone |  |
| 10-04 17:43:25 | ETH | up | 0.04→0.09 | 0.01 → 0.03 | no | price out of range |  |
| 10-04 17:43:24 | XRP | up | 0.73→0.80 | 0.76 → 0.93 | 3.32s | edge gone |  |
| 10-04 17:43:23 | BTC | up | 0.05→0.17 | 0.01 → 0.07 | no | UP @ 0.07 | -0.25 / -0.45 / 9.22 |
| 10-04 17:43:18 | ZEC | down | 0.71→0.65 | 0.04 → 0.04 | no | price out of range |  |
| 10-04 17:42:57 | XRP | up | 0.44→0.50 | 0.55 → 0.58 | 0.31s | edge gone |  |
| 10-04 17:42:42 | XRP | up | 0.23→0.33 | 0.46 → 0.37 | 15.08s | edge gone |  |
| 10-04 17:42:30 | ETH | up | 0.01→0.10 | 0.02 → 0.02 | no | price out of range |  |
| 10-04 17:42:22 | ZEC | down | 0.81→0.76 | 0.10 → 0.05 | no | DOWN @ 0.05 | -0.18 / -0.19 / -0.54 |
| 10-04 17:42:09 | DOGE | down | 0.96→0.90 | 0.09 → 0.08 | 17.84s | edge gone |  |
| 10-04 17:42:05 | XRP | down | 0.50→0.35 | 0.45 → 0.33 | 6.59s | DOWN @ 0.34 | 1.65 / 1.85 / -3.57 |
| 10-04 17:41:56 | NEAR | up | 0.69→0.77 | 0.95 → 0.95 | no | edge gone |  |
| 10-04 17:41:48 | XRP | down | 0.55→0.45 | 0.27 → 0.44 | 8.86s | DOWN @ 0.44 | -0.56 / 0.26 / -4.58 |
| 10-04 17:41:41 | NEAR | down | 0.81→0.72 | 0.08 → 0.07 | no | DOWN @ 0.08 | -0.33 / -0.55 / -0.87 |
| 10-04 17:41:37 | HYPE | up | 0.60→0.72 | 0.76 → 0.75 | no | edge gone |  |
| 10-04 17:41:35 | DOGE | up | 0.85→0.92 | 0.92 → 0.94 | no | edge gone |  |
| 10-04 17:41:33 | XRP | down | 0.46→0.37 | 0.52 → 0.44 | no | DOWN @ 0.44 | -2.22 / -1.73 / -4.58 |
| 10-04 17:41:30 | ZEC | up | 0.73→0.81 | 0.91 → 0.93 | no | edge gone |  |
| 10-04 17:41:18 | XRP | up | 0.33→0.41 | 0.83 → 0.46 | no | edge gone |  |
| 10-04 17:41:17 | ETH | down | 0.23→0.15 | 0.89 → 0.92 | 24.61s | edge gone |  |
| 10-04 17:41:02 | XRP | up | 0.46→0.66 | 0.70 → 0.78 | 10.11s | edge gone |  |
| 10-04 17:40:55 | ZEC | up | 0.70→0.75 | 0.93 → 0.93 | no | edge gone |  |
| 10-04 17:40:54 | DOGE | up | 0.77→0.83 | 0.60 → 0.85 | 2.60s | edge gone |  |
| 10-04 17:40:43 | XRP | up | 0.42→0.50 | 0.58 → 0.64 | 13.86s | edge gone |  |
| 10-04 17:40:30 | ETH | up | 0.14→0.23 | 0.05 → 0.12 | 12.12s | UP @ 0.12 | -0.25 / -0.40 / 8.72 |
| 10-04 17:40:25 | HYPE | down | 0.30→0.25 | 0.58 → 0.58 | no | DOWN @ 0.59 | -1.44 / -0.84 / -6.06 |
| 10-04 17:40:23 | XRP | up | 0.28→0.35 | 0.38 → 0.38 | 18.37s | edge gone |  |
| 10-04 17:40:19 | BNB | down | 0.10→0.04 | 0.94 → 0.94 | no | edge gone |  |
