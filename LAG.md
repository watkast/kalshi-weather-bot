# Lag Tracker

*Updated Sun Oct 04 07:25 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 605 | 11.1s | 3% | 0% |
| BTC | 466 | 11.9s | 3% | 0% |
| DOGE | 654 | 10.4s | 2% | 0% |
| ETH | 635 | 11.2s | 3% | 0% |
| HYPE | 535 | 11.4s | 4% | 0% |
| NEAR | 613 | 10.8s | 3% | 0% |
| SOL | 1153 | 10.8s | 3% | 0% |
| XRP | 1152 | 11.0s | 3% | 0% |
| ZEC | 763 | 9.7s | 4% | 0% |
| **All** | **6576** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3357 | 935 | $-398.83 | -2.7% | $-180.33 / $-218.50 |
| Sell after 30 sec | 3356 | 1931 | $1034.52 | +7.1% | $561.55 / $472.97 |
| Hold to the close | 3327 | 1665 | $2217.37 | +15.4% | $1185.18 / $1032.19 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **15 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 07:25:01 | XRP | down | 0.60→0.50 | 0.58 → 0.58 → — | no | DOWN @ 0.42 | · / · / · |
| 10-04 07:24:45 | SOL | up | 0.26→0.36 | 0.24 → 0.24 → 0.24 | 10.65s | UP @ 0.25 | -0.37 / · / · |
| 10-04 07:24:27 | SOL | up | 0.19→0.24 | 0.17 → 0.17 → 0.17 | 13.15s | UP @ 0.18 | -0.41 / 1.04 / · |
| 10-04 07:24:05 | XRP | down | 0.63→0.54 | 0.65 → 0.65 → 0.65 | 5.41s | DOWN @ 0.36 | 0.65 / 0.25 / · |
| 10-04 07:23:33 | NEAR | up | 0.18→0.25 | 0.23 → 0.23 → 0.23 | no | — |  |
| 10-04 07:23:33 | BTC | up | 0.31→0.37 | 0.24 → 0.24 → 0.24 | 7.92s | UP @ 0.25 | 1.58 / 1.19 / · |
| 10-04 07:23:27 | BNB | up | 0.10→0.18 | 0.07 → 0.07 → 0.07 | 13.42s | UP @ 0.07 | -0.27 / 0.80 / · |
| 10-04 07:23:24 | XRP | up | 0.56→0.62 | 0.56 → 0.56 → 0.58 | 16.68s | UP @ 0.56 | -0.26 / 0.76 / · |
| 10-04 07:23:15 | NEAR | down | 0.24→0.19 | 0.20 → 0.20 → 0.20 | no | — |  |
| 10-04 07:22:59 | DOGE | up | 0.08→0.14 | 0.08 → 0.08 → 0.08 | 26.18s | UP @ 0.08 | -0.20 / 0.32 / · |
| 10-04 07:22:49 | ETH | down | 0.18→0.12 | 0.06 → 0.06 → 0.06 | no | — |  |
| 10-04 07:22:49 | XRP | down | 0.68→0.58 | 0.69 → 0.69 → 0.69 | 21.43s | DOWN @ 0.31 | -0.50 / 0.97 / · |
| 10-04 07:22:49 | SOL | down | 0.20→0.14 | 0.15 → 0.15 → 0.15 | 21.43s | — |  |
| 10-04 07:22:44 | BTC | up | 0.25→0.37 | 0.18 → 0.18 → 0.18 | 11.68s | UP @ 0.19 | -0.32 / 0.16 / · |
| 10-04 07:22:42 | BNB | up | 0.07→0.15 | 0.09 → 0.09 → 0.09 | no | UP @ 0.09 | -0.14 / -0.43 / · |
| 10-04 07:22:34 | ETH | up | 0.06→0.12 | 0.03 → 0.03 → 0.03 | 21.19s | — |  |
| 10-04 07:22:28 | XRP | up | 0.56→0.62 | 0.69 → 0.57 → 0.57 | no | — |  |
| 10-04 07:22:24 | DOGE | up | 0.09→0.15 | 0.09 → 0.09 → 0.08 | 16.94s | UP @ 0.10 | -0.33 / 0.08 / · |
| 10-04 07:22:09 | SOL | down | 0.14→0.08 | 0.23 → 0.23 → 0.18 | 1.94s | DOWN @ 0.77 | 0.16 / 0.26 / · |
| 10-04 07:22:07 | XRP | down | 0.66→0.60 | 0.57 → 0.57 → 0.69 | no | — |  |
| 10-04 07:21:54 | SOL | down | 0.21→0.16 | 0.27 → 0.27 → 0.23 | 1.94s | DOWN @ 0.74 | -0.07 / 0.45 / · |
| 10-04 07:21:50 | NEAR | down | 0.47→0.40 | 0.58 → 0.58 → 0.58 | 20.95s | DOWN @ 0.42 | -1.14 / 0.64 / · |
| 10-04 07:21:48 | ETH | down | 0.14→0.06 | 0.05 → 0.05 → 0.05 | no | — |  |
| 10-04 07:21:47 | XRP | down | 0.73→0.66 | 0.70 → 0.70 → 0.70 | 8.19s | — |  |
| 10-04 07:21:36 | DOGE | up | 0.21→0.30 | 0.20 → 0.20 → 0.15 | no | UP @ 0.21 | -0.81 / -1.10 / · |
| 10-04 07:21:35 | NEAR | up | 0.42→0.47 | 0.56 → 0.56 → 0.56 | 20.95s | — |  |
| 10-04 07:21:32 | XRP | down | 0.78→0.71 | 0.27 → 0.27 → 0.27 | no | — |  |
| 10-04 07:21:32 | SOL | down | 0.37→0.28 | 0.34 → 0.34 → 0.34 | 8.95s | DOWN @ 0.66 | 0.40 / 0.71 / · |
| 10-04 07:21:21 | DOGE | up | 0.09→0.22 | 0.10 → 0.10 → 0.20 | 4.20s | UP @ 0.10 | 0.81 / 0.34 / · |
| 10-04 07:21:17 | XRP | up | 0.35→0.67 | 0.28 → 0.28 → 0.28 | 23.21s | UP @ 0.28 | -0.59 / 3.90 / · |
