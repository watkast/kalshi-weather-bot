# Lag Tracker

*Updated Sun Oct 04 15:55 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, the bot pulls Kalshi's live order book, prices 10 contracts exactly as they'd fill, and paper-buys if that's still 3¢+ below fair value after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **The gap was mostly a stale quote.** Kalshi's real order book had usually already moved, so the earlier paper profits weren't fillable.

## At a glance

| Paper P&L (hold) | Return | Trades | Avg bet | Most money tied up at once | Kalshi lag (median) |
|---|---|---|---|---|---|
| **-$311.06** | -16.4% | 513 | $3.72 | $122.22 | 10.9s |

*Order-book fills. 10 contracts per buy, no bankroll limit — every trade is scored on its own.*

## Paper trades on real order-book prices

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 532 | 90 | -$222.04 | -11.2% | -$116.40 / -$105.64 |
| Sell after 30 sec | 532 | 132 | -$243.83 | -12.3% | -$133.57 / -$110.26 |
| Hold to the close | 513 | 158 | -$311.06 | -16.4% | -$267.14 / -$43.92 |
| Hold, only edge 10¢+ | 183 | 43 | -$78.58 | -15.5% | -$117.95 / $39.37 |
| Hold, first trade per window only | 174 | 62 | -$89.79 | -12.7% | -$50.32 / -$39.47 |

![Cumulative P&L](lag/charts/pnl.png)

*Every buy and sell is priced by walking Kalshi's live order book for 10 contracts, using only what the bot knew at that moment. A timed sell with no buyers counts as held to the close. The last two rows re-score the same trades with stricter rules, as a robustness check.*

## Was the quoted price real?

| Events checked | Order book matched the quote (within 1¢) | Book was 2¢+ worse | Median gap (book − quote) | Avg cost of filling 10 vs best price | Skipped |
|---|---|---|---|---|---|
| 2079 | 10% | 67% | +5.0¢ | 0.3¢ | edge gone 1442, price out of range 55, spread too wide 50 |

*If the book usually matches the quote, the lag is real. If the book is usually worse, the "lag" was just a slow price display and the old paper profits weren't fillable.*

## Before the order-book check (quoted prices)

| Exit | Trades | Won | P&L | Return |
|---|---|---|---|---|
| Hold to the close | 3732 | 1844 | $2,348.29 | +14.6% |

*Oct 3–4. Bought at Kalshi's quoted price without checking the order book — likely optimistic.*

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 690 | 11.1s | 3% | 0% |
| BTC | 785 | 11.8s | 3% | 0% |
| DOGE | 858 | 10.7s | 3% | 0% |
| ETH | 928 | 10.9s | 4% | 0% |
| HYPE | 692 | 11.6s | 3% | 0% |
| NEAR | 900 | 10.8s | 3% | 0% |
| SOL | 1714 | 10.9s | 3% | 0% |
| XRP | 1735 | 11.2s | 3% | 0% |
| ZEC | 1044 | 9.6s | 4% | 0% |
| **All** | **9346** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's quoted price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

![How fast Kalshi follows](lag/charts/lag.png)

## Feed speed

Kalshi quote check: **19 ms** · Order book check: **25 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Quote → book | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 15:55:26 | SOL | down | 0.37→0.30 | 0.73 → 0.76 | no | edge gone |  |
| 10-04 15:55:15 | ZEC | up | 0.46→0.52 | 0.46 → 0.58 | 11.81s | edge gone |  |
| 10-04 15:54:50 | SOL | down | 0.38→0.31 | 0.70 → 0.72 | no | edge gone |  |
| 10-04 15:54:46 | ETH | down | 0.73→0.68 | 0.16 → 0.17 | 10.89s | DOWN @ 0.17 | -0.11 / -0.49 / · |
| 10-04 15:54:42 | HYPE | down | 0.42→0.31 | 0.65 → 0.65 | 0.11s | edge gone |  |
| 10-04 15:54:39 | BTC | down | 0.54→0.47 | 0.42 → 0.54 | 2.38s | edge gone |  |
| 10-04 15:54:19 | SOL | up | 0.35→0.42 | 0.36 → 0.36 | no | edge gone |  |
| 10-04 15:54:02 | SOL | up | 0.36→0.42 | 0.37 → 0.37 | no | UP @ 0.37 | -0.68 / -0.95 / · |
| 10-04 15:53:52 | HYPE | down | 0.36→0.27 | 0.71 → 0.65 | no | DOWN @ 0.66 | -1.02 / -1.43 / · |
| 10-04 15:53:36 | SOL | down | 0.42→0.36 | 0.64 → 0.66 | no | edge gone |  |
| 10-04 15:53:19 | SOL | down | 0.42→0.34 | 0.66 → 0.63 | no | edge gone |  |
| 10-04 15:53:15 | XRP | up | 0.72→0.77 | 0.67 → 0.84 | 11.40s | edge gone |  |
| 10-04 15:52:56 | XRP | down | 0.54→0.48 | 0.45 → 0.45 | no | DOWN @ 0.45 | -2.61 / -3.37 / · |
| 10-04 15:52:53 | ZEC | up | 0.39→0.44 | 0.45 → 0.42 | no | edge gone |  |
| 10-04 15:52:36 | DOGE | down | 0.50→0.39 | 0.47 → 0.51 | 20.16s | DOWN @ 0.51 | -0.29 / -0.39 / · |
| 10-04 15:52:34 | XRP | down | 0.56→0.50 | 0.47 → 0.41 | no | DOWN @ 0.41 | -0.05 / -1.71 / · |
| 10-04 15:52:20 | SOL | down | 0.40→0.35 | 0.65 → 0.63 | no | edge gone |  |
| 10-04 15:52:05 | ZEC | down | 0.62→0.51 | 0.35 → 0.35 | no | DOWN @ 0.38 | -0.75 / 1.36 / · |
| 10-04 15:52:05 | SOL | up | 0.38→0.43 | 0.38 → 0.40 | no | edge gone |  |
| 10-04 15:51:50 | SOL | up | 0.35→0.41 | 0.36 → 0.39 | no | edge gone |  |
| 10-04 15:51:46 | XRP | up | 0.52→0.58 | 0.66 → 0.65 | no | edge gone |  |
| 10-04 15:51:37 | ETH | down | 0.72→0.66 | 0.23 → 0.28 | no | DOWN @ 0.28 | -0.59 / -1.07 / · |
| 10-04 15:51:36 | ZEC | down | 0.67→0.61 | 0.21 → 0.35 | 20.18s | edge gone |  |
| 10-04 15:51:35 | SOL | down | 0.46→0.38 | 0.51 → 0.66 | 6.42s | edge gone |  |
| 10-04 15:51:33 | BTC | down | 0.54→0.48 | 0.44 → 0.49 | no | edge gone |  |
| 10-04 15:51:33 | DOGE | down | 0.58→0.50 | 0.30 → 0.48 | 8.67s | edge gone |  |
| 10-04 15:51:31 | XRP | down | 0.66→0.58 | 0.32 → 0.36 | 25.94s | edge gone |  |
| 10-04 15:51:09 | SOL | down | 0.49→0.44 | 0.56 → 0.55 | no | edge gone |  |
| 10-04 15:51:02 | ETH | up | 0.66→0.72 | 0.73 → 0.78 | 9.43s | edge gone |  |
| 10-04 15:50:34 | ZEC | down | 0.57→0.51 | 0.43 → 0.37 | no | DOWN @ 0.41 | -1.31 / -1.81 / · |
