# Lag Tracker

*Updated Sun Oct 04 18:36 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$315.06** | -10.3% | 808 | $3.83 | $161.50 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 819 | 134 | -$355.42 | -11.4% | -$169.03 / -$186.39 |
| Sell after 30 sec | 819 | 213 | -$366.00 | -11.7% | -$195.39 / -$170.61 |
| Hold to the close | 808 | 275 | -$315.06 | -10.3% | -$357.67 / $42.61 |
| Hold, only edge 10¢+ | 283 | 67 | -$148.35 | -18.1% | -$136.05 / -$12.30 |
| Hold, first trade per window only | 256 | 99 | -$49.23 | -4.7% | -$87.42 / $38.19 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 3064 | 10% | 66% | +4.1¢ | 0.3¢ | edge gone 2094, price out of range 82, spread too wide 68 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 727 | 11.1s | 3% | 0% |
| BTC | 877 | 11.9s | 3% | 0% |
| DOGE | 960 | 10.7s | 3% | 0% |
| ETH | 1069 | 10.8s | 4% | 0% |
| HYPE | 727 | 11.6s | 3% | 0% |
| NEAR | 1025 | 10.8s | 3% | 0% |
| SOL | 1871 | 10.8s | 3% | 0% |
| XRP | 1946 | 11.1s | 3% | 0% |
| ZEC | 1129 | 9.6s | 4% | 0% |
| **All** | **10331** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **9 ms** · Order book check: **26 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 18:36:31 | BTC | down | 0.57→0.51 | 0.33 → 0.51 | no | edge gone |  |
| 10-04 18:36:25 | NEAR | up | 0.82→0.89 | 0.84 → 0.85 | no | UP @ 0.85 | · / · / · |
| 10-04 18:36:19 | SOL | up | 0.57→0.65 | 0.72 → 0.72 | no | edge gone |  |
| 10-04 18:36:00 | SOL | up | 0.57→0.65 | 0.72 → 0.72 | no | edge gone |  |
| 10-04 18:35:55 | NEAR | up | 0.79→0.86 | 0.74 → 0.80 | 0.31s | UP @ 0.80 | -0.03 / 0.08 / · |
| 10-04 18:35:52 | ETH | up | 0.52→0.57 | 0.51 → 0.58 | 0.57s | edge gone |  |
| 10-04 18:35:49 | BTC | up | 0.51→0.56 | 0.59 → 0.66 | 3.32s | edge gone |  |
| 10-04 18:35:44 | SOL | up | 0.57→0.64 | 0.67 → 0.72 | 8.58s | edge gone |  |
| 10-04 18:35:40 | NEAR | up | 0.58→0.66 | 0.65 → 0.69 | 12.33s | edge gone |  |
| 10-04 18:35:25 | NEAR | up | 0.56→0.63 | 0.63 → 0.63 | 27.83s | edge gone |  |
| 10-04 18:35:09 | NEAR | down | 0.56→0.47 | 0.35 → 0.43 | no | DOWN @ 0.44 | -1.11 / -1.20 / · |
| 10-04 18:34:50 | SOL | up | 0.49→0.60 | 0.49 → 0.69 | 2.84s | edge gone |  |
| 10-04 18:34:46 | NEAR | up | 0.55→0.61 | 0.59 → 0.62 | 6.59s | edge gone |  |
| 10-04 18:34:23 | SOL | down | 0.56→0.45 | 0.44 → 0.50 | no | DOWN @ 0.50 | -0.26 / -2.04 / · |
| 10-04 18:34:22 | XRP | down | 0.84→0.78 | 0.30 → 0.33 | no | edge gone |  |
| 10-04 18:34:22 | BTC | down | 0.55→0.49 | 0.54 → 0.51 | no | edge gone |  |
| 10-04 18:34:21 | ETH | down | 0.60→0.48 | 0.61 → 0.53 | no | edge gone |  |
| 10-04 18:34:21 | ZEC | down | 0.68→0.61 | 0.34 → 0.33 | 16.60s | edge gone |  |
| 10-04 18:34:09 | NEAR | up | 0.75→0.82 | 0.66 → 0.76 | 13.85s | UP @ 0.76 | -0.73 / -2.30 / · |
| 10-04 18:34:08 | SOL | up | 0.35→0.56 | 0.38 → 0.56 | 14.60s | edge gone |  |
| 10-04 18:34:07 | XRP | up | 0.78→0.84 | 0.75 → 0.77 | no | UP @ 0.77 | -0.47 / -0.98 / · |
| 10-04 18:34:07 | BTC | up | 0.45→0.50 | 0.44 → 0.53 | 0.60s | edge gone |  |
| 10-04 18:33:53 | SOL | down | 0.38→0.32 | 0.63 → 0.62 | 0.09s | DOWN @ 0.63 | -0.48 / -1.79 / · |
| 10-04 18:33:37 | ZEC | down | 0.78→0.71 | 0.19 → 0.21 | 16.11s | edge gone |  |
| 10-04 18:33:34 | SOL | down | 0.56→0.41 | 0.34 → 0.46 | 3.35s | DOWN @ 0.46 | 1.45 / 1.25 / · |
| 10-04 18:33:30 | BTC | down | 0.61→0.56 | 0.48 → 0.48 | 22.11s | edge gone |  |
| 10-04 18:33:28 | ETH | up | 0.56→0.61 | 0.51 → 0.58 | 9.11s | edge gone |  |
| 10-04 18:33:27 | NEAR | up | 0.63→0.68 | 0.58 → 0.64 | 10.11s | edge gone |  |
| 10-04 18:33:19 | XRP | up | 0.73→0.81 | 0.80 → 0.77 | no | edge gone |  |
| 10-04 18:33:18 | ZEC | up | 0.73→0.82 | 0.88 → 0.85 | no | edge gone |  |
