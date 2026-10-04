# Lag Tracker

*Updated Sun Oct 04 00:23 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 358 | 10.8s | 4% | 0% |
| BTC | 272 | 11.8s | 2% | 0% |
| DOGE | 388 | 10.6s | 2% | 0% |
| ETH | 343 | 10.9s | 3% | 0% |
| HYPE | 267 | 11.8s | 3% | 0% |
| NEAR | 308 | 10.3s | 4% | 0% |
| SOL | 662 | 10.2s | 3% | 0% |
| XRP | 620 | 11.2s | 3% | 0% |
| ZEC | 372 | 9.5s | 5% | 0% |
| **All** | **3590** | **10.7s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1885 | 531 | $-205.17 | -2.5% | $-72.02 / $-133.15 |
| Sell after 30 sec | 1882 | 1092 | $594.12 | +7.3% | $393.65 / $200.47 |
| Hold to the close | 1848 | 943 | $1460.76 | +18.3% | $586.36 / $874.40 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **39 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 00:23:35 | NEAR | up | 0.61→0.70 | 0.84 → 0.84 → 0.84 | no | — |  |
| 10-04 00:23:28 | BNB | down | 0.44→0.26 | 0.81 → 0.81 → 0.56 | 3.19s | DOWN @ 0.20 | 2.00 / · / · |
| 10-04 00:23:19 | HYPE | down | 0.79→0.73 | 0.81 → 0.81 → 0.81 | no | DOWN @ 0.20 | -0.43 / · / · |
| 10-04 00:23:12 | BNB | down | 0.58→0.52 | 0.85 → 0.85 → 0.81 | 3.71s | DOWN @ 0.15 | 0.10 / · / · |
| 10-04 00:23:05 | BTC | down | 0.87→0.81 | 0.72 → 0.72 → 0.72 | 25.70s | — |  |
| 10-04 00:22:58 | NEAR | down | 0.72→0.65 | 0.88 → 0.88 → 0.81 | 2.69s | DOWN @ 0.14 | 0.20 / 0.11 / · |
| 10-04 00:22:57 | BNB | down | 0.63→0.56 | 0.85 → 0.85 → 0.85 | 18.71s | DOWN @ 0.16 | -0.39 / -0.01 / · |
| 10-04 00:22:43 | NEAR | down | 0.79→0.71 | 0.86 → 0.86 → 0.88 | 17.70s | DOWN @ 0.15 | -0.56 / 0.10 / · |
| 10-04 00:22:11 | HYPE | down | 0.83→0.75 | 0.94 → 0.94 → 0.93 | 17.44s | DOWN @ 0.07 | -0.07 / 0.76 / · |
| 10-04 00:22:06 | NEAR | up | 0.51→0.60 | 0.67 → 0.67 → 0.67 | 7.94s | — |  |
| 10-04 00:21:50 | BNB | down | 0.54→0.45 | 0.79 → 0.79 → 0.79 | no | DOWN @ 0.22 | -0.73 / -0.83 / · |
| 10-04 00:21:50 | NEAR | up | 0.48→0.54 | 0.59 → 0.59 → 0.59 | 8.94s | — |  |
| 10-04 00:21:35 | NEAR | down | 0.56→0.49 | 0.68 → 0.68 → 0.68 | 8.94s | DOWN @ 0.34 | 0.17 / -0.42 / · |
| 10-04 00:21:31 | DOGE | up | 0.76→0.85 | 0.85 → 0.89 → 0.89 | 12.95s | — |  |
| 10-04 00:21:23 | BNB | up | 0.57→0.68 | 0.77 → 0.77 → 0.77 | 5.44s | — |  |
| 10-04 00:21:18 | ZEC | up | 0.88→0.95 | 0.90 → 0.90 → 0.90 | 10.70s | UP @ 0.90 | -0.24 / 0.39 / · |
| 10-04 00:21:18 | BTC | up | 0.73→0.80 | 0.70 → 0.70 → 0.70 | no | UP @ 0.71 | -0.40 / -0.81 / · |
| 10-04 00:21:17 | SOL | up | 0.87→0.92 | 0.90 → 0.90 → 0.90 | 11.70s | — |  |
| 10-04 00:21:00 | BNB | down | 0.46→0.34 | 0.70 → 0.76 → 0.76 | no | DOWN @ 0.26 | -0.57 / -1.43 / · |
| 10-04 00:20:41 | NEAR | down | 0.63→0.58 | 0.80 → 0.80 → 0.77 | 3.20s | DOWN @ 0.21 | -0.05 / 0.24 / · |
| 10-04 00:20:40 | BNB | up | 0.53→0.59 | 0.76 → 0.76 → 0.70 | no | — |  |
| 10-04 00:20:29 | ZEC | down | 0.91→0.85 | 0.83 → 0.89 → 0.89 | no | — |  |
| 10-04 00:20:29 | DOGE | down | 0.81→0.72 | 0.89 → 0.89 → 0.89 | 14.70s | DOWN @ 0.12 | -0.25 / 0.22 / · |
| 10-04 00:20:19 | NEAR | up | 0.58→0.65 | 0.71 → 0.71 → 0.71 | 9.71s | — |  |
| 10-04 00:20:14 | HYPE | down | 0.96→0.90 | 0.93 → 0.93 → 0.93 | no | — |  |
| 10-04 00:20:05 | BNB | up | 0.40→0.47 | 0.56 → 0.56 → 0.56 | 8.46s | — |  |
| 10-04 00:20:05 | XRP | up | 0.81→0.94 | 0.84 → 0.84 → 0.84 | 23.46s | UP @ 0.85 | -0.18 / 0.53 / · |
| 10-04 00:20:05 | BTC | up | 0.73→0.86 | 0.66 → 0.66 → 0.66 | 8.46s | UP @ 0.66 | 1.02 / 0.91 / · |
| 10-04 00:20:05 | SOL | up | 0.85→0.91 | 0.89 → 0.89 → 0.89 | 23.46s | — |  |
| 10-04 00:20:05 | ZEC | up | 0.80→0.86 | 0.80 → 0.80 → 0.80 | 8.46s | UP @ 0.81 | -0.12 / 0.51 / · |
