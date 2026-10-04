# Lag Tracker

*Updated Sun Oct 04 07:15 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 601 | 10.9s | 3% | 0% |
| BTC | 463 | 11.9s | 3% | 0% |
| DOGE | 649 | 10.4s | 2% | 0% |
| ETH | 630 | 11.2s | 3% | 0% |
| HYPE | 532 | 11.4s | 4% | 0% |
| NEAR | 603 | 10.8s | 4% | 0% |
| SOL | 1143 | 10.8s | 3% | 0% |
| XRP | 1137 | 11.0s | 3% | 0% |
| ZEC | 756 | 9.7s | 4% | 0% |
| **All** | **6514** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3327 | 925 | $-398.37 | -2.8% | $-177.57 / $-220.80 |
| Sell after 30 sec | 3327 | 1906 | $1014.21 | +7.0% | $563.65 / $450.56 |
| Hold to the close | 3286 | 1645 | $2185.09 | +15.3% | $1156.82 / $1028.27 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **31 ms** · Coinbase price delay: **14 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 07:13:36 | XRP | down | 0.98→0.91 | 0.97 → 0.98 → 0.98 | 15.19s | — |  |
| 10-04 07:13:18 | ZEC | down | 0.11→0.05 | 0.02 → 0.02 → 0.04 | no | — |  |
| 10-04 07:13:07 | NEAR | up | 0.08→0.14 | 0.08 → 0.08 → 0.08 | 13.94s | UP @ 0.08 | -0.20 / -0.33 / · |
| 10-04 07:12:58 | XRP | up | 0.86→0.93 | 0.92 → 0.92 → 0.92 | 23.20s | — |  |
| 10-04 07:12:26 | ETH | down | 0.18→0.10 | 0.05 → 0.05 → 0.05 | no | — |  |
| 10-04 07:12:14 | DOGE | down | 0.95→0.87 | 0.97 → 0.97 → 0.97 | no | — |  |
| 10-04 07:11:59 | ZEC | down | 0.13→0.05 | 0.07 → 0.07 → 0.07 | no | — |  |
| 10-04 07:11:47 | XRP | up | 0.78→0.83 | 0.89 → 0.89 → 0.90 | no | — |  |
| 10-04 07:11:47 | NEAR | up | 0.02→0.11 | 0.03 → 0.03 → 0.23 | 3.96s | — |  |
| 10-04 07:11:46 | ETH | up | 0.21→0.27 | 0.10 → 0.10 → 0.05 | no | UP @ 0.10 | -0.61 / -0.60 / · |
| 10-04 07:11:36 | DOGE | down | 0.84→0.72 | 0.93 → 0.88 → 0.88 | no | DOWN @ 0.13 | -0.26 / -0.99 / · |
| 10-04 07:11:28 | ETH | down | 0.27→0.22 | 0.14 → 0.14 → 0.14 | 8.22s | — |  |
| 10-04 07:11:21 | XRP | down | 0.96→0.89 | 0.93 → 0.92 → 0.92 | 14.47s | DOWN @ 0.09 | -0.17 / 0.01 / · |
| 10-04 07:10:53 | ETH | down | 0.30→0.22 | 0.17 → 0.15 → 0.15 | no | — |  |
| 10-04 07:10:26 | HYPE | down | 0.17→0.11 | 0.17 → 0.17 → 0.17 | 10.23s | DOWN @ 0.83 | -0.31 / 0.53 / · |
| 10-04 07:10:24 | SOL | down | 0.88→0.82 | 0.93 → 0.93 → 0.93 | 12.23s | DOWN @ 0.08 | -0.12 / -0.57 / · |
| 10-04 07:10:22 | DOGE | down | 0.89→0.80 | 0.95 → 0.95 → 0.95 | 28.98s | DOWN @ 0.06 | -0.17 / 0.31 / · |
| 10-04 07:10:19 | BNB | down | 0.28→0.21 | 0.41 → 0.41 → 0.38 | 16.73s | DOWN @ 0.60 | -0.44 / 0.58 / · |
| 10-04 07:10:10 | BTC | down | 0.29→0.21 | 0.21 → 0.21 → 0.21 | 26.23s | — |  |
| 10-04 07:10:04 | ZEC | down | 0.28→0.22 | 0.23 → 0.23 → 0.26 | no | — |  |
| 10-04 07:09:53 | XRP | up | 0.81→0.86 | 0.86 → 0.81 → 0.81 | 12.99s | UP @ 0.81 | -0.33 / 0.95 / · |
| 10-04 07:09:52 | DOGE | up | 0.80→0.85 | 0.96 → 0.91 → 0.91 | no | — |  |
| 10-04 07:09:37 | ETH | down | 0.36→0.29 | 0.27 → 0.30 → 0.30 | 13.74s | — |  |
| 10-04 07:09:35 | XRP | down | 0.84→0.76 | 0.78 → 0.78 → 0.86 | no | — |  |
| 10-04 07:09:33 | HYPE | up | 0.16→0.27 | 0.12 → 0.12 → 0.14 | 17.49s | UP @ 0.12 | 0.03 / 0.60 / · |
| 10-04 07:09:28 | ZEC | down | 0.34→0.28 | 0.25 → 0.25 → 0.25 | no | — |  |
| 10-04 07:09:26 | DOGE | up | 0.84→0.91 | 0.95 → 0.95 → 0.95 | no | — |  |
| 10-04 07:09:26 | SOL | up | 0.69→0.84 | 0.84 → 0.84 → 0.84 | no | — |  |
| 10-04 07:09:17 | ETH | up | 0.30→0.38 | 0.24 → 0.24 → 0.27 | 18.49s | UP @ 0.25 | -0.18 / 0.21 / · |
| 10-04 07:09:00 | XRP | down | 0.79→0.73 | 0.81 → 0.81 → 0.81 | 5.99s | — |  |
