# Lag Tracker

*Updated Sat Oct 03 22:23 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 277 | 10.7s | 5% | 0% |
| BTC | 192 | 11.9s | 2% | 0% |
| DOGE | 287 | 10.1s | 2% | 0% |
| ETH | 246 | 11.0s | 3% | 0% |
| HYPE | 208 | 11.7s | 4% | 0% |
| NEAR | 223 | 10.3s | 4% | 0% |
| SOL | 456 | 9.6s | 4% | 0% |
| XRP | 439 | 10.3s | 4% | 0% |
| ZEC | 296 | 9.6s | 5% | 0% |
| **All** | **2624** | **10.6s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1371 | 400 | $-139.14 | -2.4% | $-49.00 / $-90.14 |
| Sell after 30 sec | 1371 | 829 | $502.49 | +8.6% | $309.51 / $192.98 |
| Hold to the close | 1315 | 648 | $928.84 | +16.7% | $591.80 / $337.04 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **37 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 22:23:45 | BNB | up | 0.29→0.38 | 0.43 → 0.43 → 0.61 | 3.81s | — |  |
| 10-03 22:23:44 | ETH | up | 0.17→0.23 | 0.23 → 0.23 → 0.23 | no | — |  |
| 10-03 22:23:38 | XRP | down | 0.16→0.10 | 0.15 → 0.15 → 0.15 | no | — |  |
| 10-03 22:23:30 | NEAR | down | 0.70→0.59 | 0.74 → 0.74 → 0.71 | 18.81s | — |  |
| 10-03 22:23:27 | SOL | down | 0.30→0.22 | 0.26 → 0.26 → 0.26 | no | — |  |
| 10-03 22:23:12 | XRP | down | 0.22→0.15 | 0.20 → 0.20 → 0.20 | 22.32s | DOWN @ 0.81 | -0.12 / 0.09 / · |
| 10-03 22:23:08 | SOL | up | 0.26→0.34 | 0.21 → 0.21 → 0.21 | 11.08s | UP @ 0.22 | -0.35 / -0.06 / · |
| 10-03 22:23:03 | ZEC | up | 0.36→0.42 | 0.30 → 0.30 → 0.30 | 16.09s | UP @ 0.31 | -0.50 / 0.48 / · |
| 10-03 22:22:36 | XRP | up | 0.20→0.25 | 0.23 → 0.23 → 0.23 | no | — |  |
| 10-03 22:22:36 | ETH | up | 0.18→0.29 | 0.21 → 0.21 → 0.21 | no | UP @ 0.22 | -0.35 / 0.03 / · |
| 10-03 22:22:36 | BTC | up | 0.27→0.38 | 0.28 → 0.28 → 0.27 | 15.82s | UP @ 0.29 | -0.59 / 0.09 / · |
| 10-03 22:22:34 | HYPE | down | 0.22→0.14 | 0.29 → 0.29 → 0.27 | 17.83s | DOWN @ 0.73 | -0.39 / 0.65 / · |
| 10-03 22:22:33 | NEAR | up | 0.63→0.68 | 0.68 → 0.68 → 0.70 | 30.57s | — |  |
| 10-03 22:22:27 | SOL | down | 0.21→0.16 | 0.23 → 0.23 → 0.23 | no | DOWN @ 0.77 | -0.36 / -0.26 / · |
| 10-03 22:22:20 | ZEC | down | 0.44→0.39 | 0.43 → 0.43 → 0.37 | 1.81s | — |  |
| 10-03 22:22:12 | SOL | down | 0.25→0.19 | 0.20 → 0.20 → 0.20 | no | — |  |
| 10-03 22:21:57 | SOL | down | 0.32→0.22 | 0.28 → 0.28 → 0.28 | 9.81s | DOWN @ 0.72 | 0.43 / 0.12 / · |
| 10-03 22:21:57 | BTC | down | 0.39→0.33 | 0.36 → 0.36 → 0.36 | 10.06s | DOWN @ 0.64 | -0.44 / 0.38 / · |
| 10-03 22:21:55 | ETH | down | 0.27→0.21 | 0.30 → 0.30 → 0.30 | 11.31s | DOWN @ 0.70 | -0.40 / 0.52 / · |
| 10-03 22:21:53 | HYPE | down | 0.40→0.33 | 0.41 → 0.42 → 0.42 | 13.81s | DOWN @ 0.59 | -0.55 / 0.68 / · |
| 10-03 22:21:53 | NEAR | down | 0.75→0.67 | 0.89 → 0.74 → 0.74 | 0.02s | DOWN @ 0.28 | -0.68 / 0.09 / · |
| 10-03 22:21:45 | DOGE | down | 0.19→0.12 | 0.17 → 0.17 → 0.17 | 7.07s | DOWN @ 0.84 | 0.12 / 0.22 / · |
| 10-03 22:21:42 | ZEC | down | 0.62→0.56 | 0.70 → 0.70 → 0.70 | 9.32s | DOWN @ 0.31 | 1.97 / 2.07 / · |
| 10-03 22:21:37 | NEAR | down | 0.89→0.67 | 0.89 → 0.89 → 0.89 | 14.32s | DOWN @ 0.12 | -0.25 / 2.25 / · |
| 10-03 22:21:30 | ETH | down | 0.37→0.30 | 0.38 → 0.38 → 0.38 | 21.32s | DOWN @ 0.63 | -0.13 / 0.28 / · |
| 10-03 22:21:25 | SOL | down | 0.39→0.29 | 0.32 → 0.32 → 0.32 | no | — |  |
| 10-03 22:21:11 | HYPE | up | 0.14→0.29 | 0.20 → 0.20 → 0.20 | 10.56s | UP @ 0.21 | -0.43 / 1.61 / · |
| 10-03 22:21:11 | NEAR | up | 0.76→0.88 | 0.80 → 0.80 → 0.80 | 10.81s | UP @ 0.82 | -0.64 / 0.41 / · |
| 10-03 22:21:10 | XRP | down | 0.31→0.26 | 0.30 → 0.30 → 0.30 | no | — |  |
| 10-03 22:21:02 | DOGE | down | 0.20→0.14 | 0.17 → 0.17 → 0.17 | no | — |  |
