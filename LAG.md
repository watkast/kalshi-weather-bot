# Lag Tracker

*Updated Sun Oct 04 00:43 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 372 | 10.7s | 5% | 0% |
| BTC | 285 | 11.6s | 2% | 0% |
| DOGE | 407 | 10.6s | 2% | 0% |
| ETH | 356 | 10.9s | 3% | 0% |
| HYPE | 285 | 11.8s | 3% | 0% |
| NEAR | 329 | 10.4s | 4% | 0% |
| SOL | 682 | 10.4s | 3% | 0% |
| XRP | 648 | 11.2s | 3% | 0% |
| ZEC | 380 | 9.6s | 5% | 0% |
| **All** | **3744** | **10.7s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1967 | 561 | $-195.08 | -2.3% | $-83.35 / $-111.73 |
| Sell after 30 sec | 1964 | 1146 | $651.99 | +7.7% | $397.97 / $254.02 |
| Hold to the close | 1896 | 962 | $1463.70 | +17.9% | $678.82 / $784.88 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **38 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 00:43:39 | NEAR | up | 0.67→0.76 | 0.91 → 0.91 → 0.91 | no | — |  |
| 10-04 00:43:37 | XRP | up | 0.24→0.41 | 0.20 → 0.20 → 0.20 | no | UP @ 0.21 | · / · / · |
| 10-04 00:43:26 | ETH | down | 0.62→0.53 | 0.83 → 0.83 → 0.74 | 4.38s | DOWN @ 0.17 | 0.56 / · / · |
| 10-04 00:43:22 | XRP | down | 0.21→0.15 | 0.58 → 0.58 → 0.58 | 9.13s | DOWN @ 0.43 | 3.30 / · / · |
| 10-04 00:43:19 | DOGE | down | 0.83→0.72 | 0.94 → 0.94 → 0.94 | no | DOWN @ 0.08 | -0.40 / · / · |
| 10-04 00:43:06 | NEAR | up | 0.68→0.73 | 0.87 → 0.87 → 0.87 | 24.39s | — |  |
| 10-04 00:43:04 | XRP | up | 0.24→0.29 | 0.41 → 0.41 → 0.41 | 11.63s | — |  |
| 10-04 00:43:04 | DOGE | up | 0.54→0.73 | 0.86 → 0.86 → 0.86 | no | — |  |
| 10-04 00:42:51 | NEAR | down | 0.71→0.65 | 0.88 → 0.88 → 0.88 | no | — |  |
| 10-04 00:42:43 | XRP | up | 0.26→0.37 | 0.53 → 0.53 → 0.59 | 3.14s | — |  |
| 10-04 00:42:42 | ETH | down | 0.72→0.62 | 0.84 → 0.84 → 0.89 | no | DOWN @ 0.17 | -0.93 / -0.01 / · |
| 10-04 00:42:29 | NEAR | up | 0.46→0.53 | 0.72 → 0.72 → 0.68 | 16.64s | — |  |
| 10-04 00:42:28 | XRP | up | 0.23→0.38 | 0.32 → 0.32 → 0.53 | 3.14s | UP @ 0.33 | 1.56 / 2.16 / · |
| 10-04 00:42:12 | XRP | down | 0.24→0.16 | 0.41 → 0.41 → 0.32 | 3.14s | DOWN @ 0.60 | 0.37 / -1.65 / · |
| 10-04 00:42:05 | DOGE | down | 0.74→0.38 | 0.84 → 0.84 → 0.84 | 10.15s | DOWN @ 0.16 | -0.29 / 1.44 / · |
| 10-04 00:42:05 | ETH | down | 0.78→0.67 | 0.93 → 0.93 → 0.93 | 10.90s | DOWN @ 0.08 | -0.20 / 0.60 / · |
| 10-04 00:42:03 | NEAR | down | 0.66→0.60 | 0.78 → 0.78 → 0.78 | 12.40s | DOWN @ 0.23 | -0.36 / 0.52 / · |
| 10-04 00:41:50 | DOGE | up | 0.67→0.73 | 0.82 → 0.82 → 0.82 | no | — |  |
| 10-04 00:41:49 | XRP | down | 0.34→0.21 | 0.49 → 0.49 → 0.49 | 11.15s | DOWN @ 0.51 | -0.46 / 1.26 / · |
| 10-04 00:41:48 | NEAR | down | 0.69→0.64 | 0.81 → 0.81 → 0.81 | 12.40s | DOWN @ 0.20 | -0.33 / 0.44 / · |
| 10-04 00:41:29 | XRP | up | 0.27→0.35 | 0.39 → 0.39 → 0.43 | 1.90s | — |  |
| 10-04 00:41:24 | NEAR | down | 0.75→0.66 | 0.82 → 0.82 → 0.82 | 6.90s | DOWN @ 0.18 | 0.16 / -0.12 / · |
| 10-04 00:41:23 | ETH | up | 0.71→0.76 | 0.88 → 0.88 → 0.88 | 22.41s | — |  |
| 10-04 00:41:20 | HYPE | up | 0.06→0.14 | 0.06 → 0.06 → 0.06 | 25.16s | UP @ 0.06 | -0.15 / 0.17 / · |
| 10-04 00:41:10 | BNB | up | 0.06→0.13 | 0.34 → 0.34 → 0.34 | no | — |  |
| 10-04 00:41:01 | ZEC | down | 0.95→0.87 | 0.95 → 0.95 → 0.95 | no | DOWN @ 0.06 | -0.31 / -0.20 / · |
| 10-04 00:40:47 | SOL | down | 0.92→0.87 | 0.89 → 0.89 → 0.89 | no | — |  |
| 10-04 00:40:44 | NEAR | down | 0.82→0.76 | 0.93 → 0.93 → 0.92 | 16.67s | DOWN @ 0.08 | -0.14 / 0.50 / · |
| 10-04 00:40:35 | BTC | down | 0.47→0.36 | 0.52 → 0.52 → 0.52 | 10.17s | DOWN @ 0.49 | -0.46 / 1.26 / · |
| 10-04 00:40:20 | XRP | up | 0.27→0.34 | 0.46 → 0.46 → 0.46 | no | — |  |
