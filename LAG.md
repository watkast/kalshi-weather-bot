# Lag Tracker

*Updated Sat Oct 03 22:44 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 288 | 10.7s | 5% | 0% |
| BTC | 200 | 12.1s | 2% | 0% |
| DOGE | 299 | 10.2s | 2% | 0% |
| ETH | 262 | 11.1s | 3% | 0% |
| HYPE | 212 | 11.6s | 4% | 0% |
| NEAR | 237 | 10.4s | 3% | 0% |
| SOL | 497 | 9.8s | 4% | 0% |
| XRP | 450 | 10.3s | 4% | 0% |
| ZEC | 312 | 9.6s | 5% | 0% |
| **All** | **2757** | **10.6s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1437 | 411 | $-157.14 | -2.6% | $-52.28 / $-104.86 |
| Sell after 30 sec | 1437 | 858 | $501.25 | +8.2% | $323.92 / $177.33 |
| Hold to the close | 1388 | 686 | $931.38 | +15.7% | $591.86 / $339.52 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **37 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 22:43:34 | ZEC | down | 0.66→0.60 | 0.64 → 0.64 → 0.64 | no | — |  |
| 10-03 22:43:32 | SOL | up | 0.73→0.90 | 0.89 → 0.94 → 0.94 | 27.82s | — |  |
| 10-03 22:43:18 | ZEC | up | 0.50→0.75 | 0.24 → 0.24 → 0.24 | 12.06s | UP @ 0.25 | -0.37 / 3.80 / · |
| 10-03 22:43:14 | SOL | down | 0.70→0.61 | 0.84 → 0.84 → 0.89 | no | DOWN @ 0.17 | -0.87 / -1.37 / · |
| 10-03 22:43:05 | DOGE | up | 0.47→0.60 | 0.85 → 0.85 → 0.85 | 25.06s | — |  |
| 10-03 22:42:59 | ZEC | up | 0.40→0.46 | 0.29 → 0.29 → 0.29 | no | UP @ 0.31 | -0.60 / -0.98 / · |
| 10-03 22:42:59 | SOL | down | 0.69→0.60 | 0.81 → 0.81 → 0.84 | no | DOWN @ 0.19 | -0.70 / -1.08 / · |
| 10-03 22:42:43 | ZEC | up | 0.34→0.41 | 0.21 → 0.21 → 0.29 | 1.81s | UP @ 0.22 | 0.32 / 0.32 / · |
| 10-03 22:42:41 | SOL | down | 0.75→0.67 | 0.77 → 0.77 → 0.81 | no | DOWN @ 0.25 | -0.95 / -1.33 / · |
| 10-03 22:42:40 | DOGE | down | 0.62→0.48 | 0.84 → 0.84 → 0.88 | no | DOWN @ 0.16 | -0.58 / -0.39 / · |
| 10-03 22:42:34 | BTC | down | 0.83→0.76 | 0.79 → 0.79 → 0.79 | no | — |  |
| 10-03 22:42:21 | SOL | up | 0.58→0.73 | 0.74 → 0.74 → 0.74 | no | — |  |
| 10-03 22:42:20 | ZEC | down | 0.26→0.19 | 0.24 → 0.24 → 0.24 | no | — |  |
| 10-03 22:42:06 | SOL | down | 0.72→0.65 | 0.73 → 0.73 → 0.73 | no | DOWN @ 0.27 | -0.48 / -0.77 / · |
| 10-03 22:42:02 | ZEC | down | 0.35→0.25 | 0.34 → 0.28 → 0.28 | 0.27s | — |  |
| 10-03 22:41:56 | XRP | down | 0.96→0.90 | 0.97 → 0.97 → 0.97 | no | — |  |
| 10-03 22:41:52 | DOGE | up | 0.54→0.60 | 0.88 → 0.88 → 0.88 | no | — |  |
| 10-03 22:41:46 | SOL | down | 0.86→0.76 | 0.93 → 0.93 → 0.93 | 13.33s | DOWN @ 0.07 | -0.26 / 1.56 / · |
| 10-03 22:41:46 | ETH | down | 0.65→0.55 | 0.73 → 0.69 → 0.69 | 13.83s | DOWN @ 0.32 | -0.51 / 0.76 / · |
| 10-03 22:41:42 | ZEC | down | 0.71→0.37 | 0.82 → 0.82 → 0.34 | 2.81s | DOWN @ 0.20 | 4.32 / 4.93 / · |
| 10-03 22:41:36 | DOGE | up | 0.54→0.63 | 0.88 → 0.88 → 0.88 | no | — |  |
| 10-03 22:41:28 | SOL | down | 0.85→0.75 | 0.92 → 0.92 → 0.93 | no | DOWN @ 0.09 | -0.25 / -0.37 / · |
| 10-03 22:41:21 | DOGE | down | 0.65→0.54 | 0.85 → 0.85 → 0.85 | no | DOWN @ 0.15 | -0.47 / -0.47 / · |
| 10-03 22:41:13 | SOL | up | 0.74→0.79 | 0.92 → 0.92 → 0.92 | no | — |  |
| 10-03 22:40:52 | BNB | up | 0.88→0.95 | 0.97 → 0.97 → 0.97 | no | — |  |
| 10-03 22:40:50 | ZEC | down | 0.77→0.72 | 0.88 → 0.88 → 0.88 | 10.06s | DOWN @ 0.13 | -0.26 / 0.41 / · |
| 10-03 22:40:46 | SOL | up | 0.73→0.86 | 0.90 → 0.91 → 0.91 | no | — |  |
| 10-03 22:40:42 | ETH | down | 0.66→0.59 | 0.69 → 0.69 → 0.68 | 18.06s | DOWN @ 0.31 | -0.30 / 1.57 / · |
| 10-03 22:40:41 | DOGE | down | 0.72→0.63 | 0.91 → 0.91 → 0.92 | 18.31s | DOWN @ 0.09 | -0.25 / 0.44 / · |
| 10-03 22:40:37 | BNB | down | 0.94→0.87 | 0.97 → 0.97 → 0.97 | no | — |  |
