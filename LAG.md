# Lag Tracker

*Updated Sun Oct 04 21:36 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$181.48** | -4.1% | 1106 | $3.99 | $185.87 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1111 | 181 | -$483.22 | -10.9% | -$227.08 / -$256.14 |
| Sell after 30 sec | 1110 | 289 | -$517.85 | -11.7% | -$242.31 / -$275.54 |
| Hold to the close | 1106 | 423 | -$181.48 | -4.1% | -$343.41 / $161.93 |
| Hold, only edge 10¢+ | 388 | 110 | -$148.13 | -11.9% | -$85.60 / -$62.53 |
| Hold, first trade per window only | 345 | 142 | -$47.19 | -3.2% | -$94.31 / $47.12 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 4133 | 10% | 66% | +4.0¢ | 0.3¢ | edge gone 2823, price out of range 104, spread too wide 94 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 780 | 11.1s | 3% | 0% |
| BTC | 984 | 11.9s | 3% | 0% |
| DOGE | 1059 | 10.9s | 3% | 0% |
| ETH | 1192 | 10.8s | 4% | 0% |
| HYPE | 795 | 11.5s | 3% | 0% |
| NEAR | 1142 | 10.8s | 4% | 0% |
| SOL | 2066 | 10.9s | 3% | 0% |
| XRP | 2143 | 11.0s | 3% | 0% |
| ZEC | 1239 | 9.8s | 4% | 0% |
| **All** | **11400** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **6 ms** · Order book check: **61 ms** · Coinbase price delay: **34 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 21:36:43 | DOGE | up | 0.53→0.61 | 0.49 → 0.55 | no | UP @ 0.55 | · / · / · |
| 10-04 21:36:35 | SOL | down | 0.66→0.60 | 0.26 → 0.31 | 8.94s | DOWN @ 0.31 | -0.40 / · / · |
| 10-04 21:36:21 | DOGE | up | 0.40→0.49 | 0.40 → 0.49 | 8.00s | edge gone |  |
| 10-04 21:36:04 | SOL | up | 0.62→0.68 | 0.71 → 0.76 | 10.20s | edge gone |  |
| 10-04 21:35:48 | DOGE | up | 0.39→0.46 | 0.29 → 0.44 | 11.20s | edge gone |  |
| 10-04 21:35:47 | BTC | up | 0.74→0.80 | 0.77 → 0.83 | 11.95s | edge gone |  |
| 10-04 21:35:46 | SOL | up | 0.55→0.64 | 0.68 → 0.71 | 13.20s | edge gone |  |
| 10-04 21:35:30 | DOGE | down | 0.36→0.29 | 0.61 → 0.68 | 14.21s | edge gone |  |
| 10-04 21:35:09 | ETH | down | 0.71→0.64 | 0.25 → 0.33 | 4.96s | edge gone |  |
| 10-04 21:35:09 | SOL | down | 0.63→0.57 | 0.26 → 0.41 | 4.96s | edge gone |  |
| 10-04 21:35:08 | DOGE | down | 0.57→0.46 | 0.43 → 0.53 | 6.21s | edge gone |  |
| 10-04 21:35:06 | XRP | down | 0.74→0.66 | 0.23 → 0.29 | 7.96s | DOWN @ 0.29 | 0.97 / 0.78 / · |
| 10-04 21:34:59 | NEAR | down | 0.60→0.53 | 0.32 → 0.32 | no | DOWN @ 0.32 | -0.90 / -1.86 / · |
| 10-04 21:34:44 | NEAR | up | 0.59→0.64 | 0.67 → 0.70 | 14.97s | edge gone |  |
| 10-04 21:34:42 | DOGE | down | 0.77→0.70 | 0.27 → 0.39 | 2.22s | edge gone |  |
| 10-04 21:34:37 | BTC | up | 0.62→0.68 | 0.66 → 0.70 | 21.48s | edge gone |  |
| 10-04 21:34:30 | SOL | down | 0.63→0.57 | 0.36 → 0.36 | no | DOWN @ 0.36 | -1.40 / -1.50 / · |
| 10-04 21:34:12 | ZEC | up | 0.60→0.75 | 0.70 → 0.83 | 16.73s | edge gone |  |
| 10-04 21:34:10 | DOGE | down | 0.88→0.82 | 0.16 → 0.20 | 18.73s | edge gone |  |
| 10-04 21:34:02 | SOL | up | 0.55→0.61 | 0.67 → 0.64 | no | edge gone |  |
| 10-04 21:33:47 | ZEC | up | 0.46→0.57 | 0.68 → 0.69 | no | edge gone |  |
| 10-04 21:33:35 | BTC | up | 0.50→0.58 | 0.53 → 0.59 | 8.49s | edge gone |  |
| 10-04 21:33:33 | DOGE | up | 0.79→0.85 | 0.88 → 0.79 | no | edge gone |  |
| 10-04 21:33:10 | XRP | down | 0.78→0.72 | 0.20 → 0.25 | 3.50s | edge gone |  |
| 10-04 21:32:25 | SOL | up | 0.53→0.58 | 0.64 → 0.58 | no | edge gone |  |
| 10-04 21:32:10 | SOL | down | 0.60→0.54 | 0.35 → 0.40 | 18.52s | DOWN @ 0.40 | 0.35 / -0.64 / · |
| 10-04 21:32:05 | XRP | up | 0.71→0.76 | 0.76 → 0.77 | 23.77s | edge gone |  |
| 10-04 21:31:13 | DOGE | down | 0.84→0.78 | 0.39 → 0.27 | no | edge gone |  |
| 10-04 21:30:56 | DOGE | up | 0.52→0.57 | 0.53 → 0.60 | 0.24s | edge gone |  |
| 10-04 21:30:41 | NEAR | up | 0.54→0.78 | 0.64 → 0.78 | no | edge gone |  |
