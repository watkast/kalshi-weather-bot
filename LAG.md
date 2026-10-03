# Lag Tracker

*Updated Sat Oct 03 19:12 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 142 | 10.8s | 6% | 0% |
| BTC | 86 | 10.8s | 4% | 0% |
| DOGE | 97 | 9.0s | 4% | 0% |
| ETH | 75 | 11.1s | 3% | 0% |
| HYPE | 66 | 11.6s | 3% | 0% |
| NEAR | 95 | 9.3s | 4% | 0% |
| SOL | 170 | 7.8s | 7% | 0% |
| XRP | 142 | 8.8s | 9% | 0% |
| ZEC | 128 | 9.1s | 5% | 0% |
| **All** | **1001** | **9.6s** | **6%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 521 | 185 | $-16.81 | -0.8% | $2.80 / $-19.61 |
| Sell after 30 sec | 521 | 348 | $279.20 | +13.1% | $147.95 / $131.25 |
| Hold to the close | 482 | 249 | $534.41 | +27.3% | $210.64 / $323.77 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 19:11:39 | BNB | up | 0.77→0.85 | 0.90 → 0.90 → 0.89 | no | — |  |
| 10-03 19:11:20 | BNB | up | 0.54→0.68 | 0.71 → 0.71 → 0.71 | 6.08s | — |  |
| 10-03 19:11:03 | NEAR | down | 0.15→0.06 | 0.10 → 0.10 → 0.10 | 23.09s | DOWN @ 0.91 | 0.12 / 0.30 / · |
| 10-03 19:10:36 | BNB | up | 0.45→0.58 | 0.56 → 0.56 → 0.64 | 4.89s | — |  |
| 10-03 19:10:36 | NEAR | up | 0.20→0.28 | 0.30 → 0.30 → 0.18 | no | — |  |
| 10-03 19:10:12 | NEAR | up | 0.30→0.37 | 0.34 → 0.34 → 0.34 | no | — |  |
| 10-03 19:09:57 | BNB | up | 0.38→0.57 | 0.47 → 0.47 → 0.47 | no | — |  |
| 10-03 19:09:51 | NEAR | up | 0.28→0.37 | 0.34 → 0.34 → 0.34 | no | — |  |
| 10-03 19:09:28 | NEAR | down | 0.37→0.30 | 0.33 → 0.29 → 0.29 | no | — |  |
| 10-03 19:09:26 | BNB | down | 0.45→0.39 | 0.59 → 0.49 → 0.49 | 0.32s | DOWN @ 0.52 | -0.56 / -0.36 / · |
| 10-03 19:09:11 | DOGE | up | 0.15→0.28 | 0.18 → 0.23 → 0.23 | no | — |  |
| 10-03 19:09:02 | BNB | up | 0.46→0.59 | 0.54 → 0.54 → 0.54 | no | UP @ 0.54 | 0.04 / -0.96 / · |
| 10-03 19:09:02 | NEAR | up | 0.25→0.32 | 0.28 → 0.28 → 0.28 | 8.62s | — |  |
| 10-03 19:08:44 | NEAR | up | 0.19→0.25 | 0.18 → 0.18 → 0.18 | 11.37s | UP @ 0.20 | -0.52 / 0.83 / · |
| 10-03 19:08:37 | DOGE | down | 0.20→0.15 | 0.21 → 0.21 → 0.20 | 18.62s | DOWN @ 0.79 | -0.14 / -0.03 / · |
| 10-03 19:08:37 | BNB | down | 0.46→0.37 | 0.50 → 0.50 → 0.48 | no | — |  |
| 10-03 19:08:17 | NEAR | down | 0.36→0.27 | 0.34 → 0.34 → 0.34 | 8.88s | DOWN @ 0.67 | 1.23 / 1.02 / · |
| 10-03 19:07:52 | NEAR | down | 0.39→0.30 | 0.32 → 0.32 → 0.34 | no | — |  |
| 10-03 19:07:40 | BNB | down | 0.52→0.46 | 0.54 → 0.54 → 0.52 | 15.64s | DOWN @ 0.47 | -0.36 / -0.06 / · |
| 10-03 19:07:36 | DOGE | up | 0.19→0.26 | 0.15 → 0.15 → 0.21 | 4.38s | UP @ 0.16 | 0.28 / 0.37 / · |
| 10-03 19:07:26 | NEAR | up | 0.27→0.35 | 0.20 → 0.28 → 0.28 | 0.35s | UP @ 0.30 | -0.69 / -0.11 / · |
| 10-03 19:07:25 | BNB | down | 0.55→0.50 | 0.67 → 0.67 → 0.54 | 0.63s | DOWN @ 0.34 | 0.86 / 0.96 / · |
| 10-03 19:06:34 | DOGE | down | 0.31→0.22 | 0.20 → 0.20 → 0.20 | no | — |  |
| 10-03 19:06:19 | DOGE | up | 0.14→0.31 | 0.14 → 0.14 → 0.14 | no | UP @ 0.14 | 0.39 / 0.30 / · |
| 10-03 19:06:17 | ETH | up | 0.07→0.12 | 0.09 → 0.09 → 0.09 | 8.65s | — |  |
| 10-03 19:06:17 | NEAR | up | 0.20→0.25 | 0.23 → 0.23 → 0.23 | 9.15s | — |  |
| 10-03 19:06:16 | ZEC | up | 0.62→0.68 | 0.53 → 0.53 → 0.53 | 9.65s | UP @ 0.54 | 1.06 / 1.58 / · |
| 10-03 19:06:15 | BNB | up | 0.49→0.54 | 0.54 → 0.54 → 0.54 | 11.15s | — |  |
| 10-03 19:05:50 | ZEC | up | 0.47→0.55 | 0.41 → 0.41 → 0.41 | 20.42s | — |  |
| 10-03 19:05:42 | BNB | down | 0.46→0.38 | 0.53 → 0.51 → 0.51 | no | DOWN @ 0.50 | -0.46 / -0.86 / · |
