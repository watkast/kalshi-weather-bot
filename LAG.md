# Lag Tracker

*Updated Sat Oct 03 20:43 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **No profitable gap yet.** Kalshi sometimes lags, but not by enough to beat the fees.

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 211 | 10.7s | 6% | 0% |
| BTC | 132 | 11.6s | 2% | 0% |
| DOGE | 200 | 9.9s | 2% | 0% |
| ETH | 131 | 10.7s | 3% | 0% |
| HYPE | 125 | 11.7s | 3% | 0% |
| NEAR | 146 | 9.3s | 4% | 0% |
| SOL | 305 | 8.9s | 5% | 0% |
| XRP | 302 | 9.9s | 5% | 0% |
| ZEC | 212 | 9.6s | 5% | 0% |
| **All** | **1764** | **10.1s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 909 | 293 | $-67.96 | -1.8% | $-11.30 / $-56.66 |
| Sell after 30 sec | 909 | 573 | $371.96 | +9.7% | $256.63 / $115.33 |
| Hold to the close | 874 | 420 | $511.46 | +13.9% | $515.18 / $-3.72 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 20:43:12 | ZEC | up | 0.21→0.40 | 0.06 → 0.06 → — | no | UP @ 0.08 | · / · / · |
| 10-03 20:42:45 | XRP | up | 0.11→0.22 | 0.23 → 0.23 → 0.18 | 15.65s | — |  |
| 10-03 20:42:41 | DOGE | up | 0.04→0.30 | 0.06 → 0.06 → 0.06 | no | UP @ 0.06 | -0.41 / -0.27 / · |
| 10-03 20:42:36 | BNB | down | 0.14→0.09 | 0.13 → 0.13 → 0.13 | 10.39s | — |  |
| 10-03 20:42:30 | XRP | down | 0.21→0.11 | 0.26 → 0.26 → 0.23 | 15.65s | DOWN @ 0.75 | -0.17 / 0.35 / · |
| 10-03 20:42:24 | ZEC | down | 0.34→0.24 | 0.11 → 0.11 → 0.11 | no | — |  |
| 10-03 20:42:21 | BNB | down | 0.26→0.17 | 0.23 → 0.23 → 0.23 | 10.40s | DOWN @ 0.78 | -0.36 / 0.90 / · |
| 10-03 20:42:13 | DOGE | down | 0.12→0.05 | 0.05 → 0.05 → 0.08 | no | — |  |
| 10-03 20:42:09 | ZEC | up | 0.29→0.34 | 0.09 → 0.09 → 0.09 | no | — |  |
| 10-03 20:42:06 | XRP | up | 0.20→0.27 | 0.15 → 0.15 → 0.15 | 9.90s | UP @ 0.16 | 0.66 / 0.28 / · |
| 10-03 20:41:55 | DOGE | up | 0.03→0.09 | 0.05 → 0.05 → 0.05 | no | — |  |
| 10-03 20:41:51 | XRP | up | 0.12→0.18 | 0.18 → 0.18 → 0.18 | 24.91s | — |  |
| 10-03 20:41:39 | ZEC | up | 0.21→0.27 | 0.05 → 0.05 → 0.05 | 6.91s | UP @ 0.06 | 0.17 / -0.08 / · |
| 10-03 20:41:36 | XRP | up | 0.08→0.16 | 0.10 → 0.10 → 0.10 | 9.91s | UP @ 0.10 | 0.63 / 0.35 / · |
| 10-03 20:41:33 | NEAR | up | 0.11→0.17 | 0.13 → 0.13 → 0.13 | 12.66s | — |  |
| 10-03 20:41:22 | BNB | down | 0.39→0.28 | 0.49 → 0.49 → 0.49 | 24.42s | — |  |
| 10-03 20:41:07 | DOGE | up | 0.05→0.12 | 0.04 → 0.04 → 0.04 | no | — |  |
| 10-03 20:41:06 | ZEC | down | 0.28→0.21 | 0.11 → 0.11 → 0.11 | 25.42s | — |  |
| 10-03 20:40:57 | XRP | down | 0.16→0.09 | 0.15 → 0.15 → 0.14 | no | DOWN @ 0.86 | -0.18 / 0.03 / · |
| 10-03 20:40:35 | HYPE | up | 0.76→0.84 | 0.89 → 0.89 → 0.89 | 26.18s | — |  |
| 10-03 20:40:29 | ZEC | down | 0.22→0.16 | 0.14 → 0.14 → 0.09 | 1.67s | — |  |
| 10-03 20:40:04 | DOGE | down | 0.18→0.11 | 0.10 → 0.10 → 0.10 | no | — |  |
| 10-03 20:39:58 | BTC | up | 0.13→0.22 | 0.09 → 0.09 → 0.08 | no | UP @ 0.09 | -0.24 / -0.21 / · |
| 10-03 20:39:47 | XRP | down | 0.27→0.22 | 0.37 → 0.32 → 0.32 | 0.14s | DOWN @ 0.70 | -0.61 / 0.84 / · |
| 10-03 20:39:31 | ZEC | up | 0.29→0.36 | 0.12 → 0.15 → 0.15 | 14.69s | UP @ 0.16 | -0.29 / -0.58 / · |
| 10-03 20:39:27 | NEAR | down | 0.18→0.11 | 0.12 → 0.12 → 0.15 | no | — |  |
| 10-03 20:39:18 | DOGE | down | 0.24→0.18 | 0.17 → 0.18 → 0.18 | no | — |  |
| 10-03 20:39:12 | HYPE | up | 0.78→0.90 | 0.76 → 0.76 → 0.78 | 18.69s | UP @ 0.76 | -0.16 / 0.89 / · |
| 10-03 20:39:10 | XRP | up | 0.26→0.31 | 0.21 → 0.21 → 0.21 | 5.94s | UP @ 0.22 | 0.71 / 1.10 / · |
| 10-03 20:39:08 | ETH | up | 0.14→0.20 | 0.09 → 0.09 → 0.09 | 7.44s | UP @ 0.09 | 0.55 / 0.36 / · |
