# Lag Tracker

*Updated Sat Oct 03 17:42 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟡 **Too early.** Collecting data — needs at least 150 paper trades before calling it.

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 39 | 11.1s | 3% | 0% |
| BTC | 23 | 10.8s | 4% | 0% |
| DOGE | 26 | 9.5s | 4% | 0% |
| ETH | 27 | 9.3s | 4% | 0% |
| HYPE | 23 | 8.8s | 4% | 0% |
| NEAR | 18 | 8.3s | 11% | 0% |
| SOL | 53 | 5.6s | 6% | 0% |
| XRP | 42 | 7.6s | 10% | 0% |
| ZEC | 37 | 11.8s | 11% | 0% |
| **All** | **288** | **9.0s** | **6%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 161 | 58 | $-8.00 | -1.2% | $-9.90 / $1.90 |
| Sell after 30 sec | 158 | 111 | $87.07 | +13.7% | $33.71 / $53.36 |
| Hold to the close | 91 | 47 | $117.36 | +33.3% | $-68.79 / $186.15 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **34 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 17:41:58 | ZEC | down | 0.18→0.12 | 0.03 → 0.05 → 0.05 | no | — |  |
| 10-03 17:41:57 | XRP | down | 0.29→0.23 | 0.20 → 0.20 → 0.23 | no | — |  |
| 10-03 17:41:54 | DOGE | up | 0.01→0.07 | 0.04 → 0.04 → 0.06 | no | — |  |
| 10-03 17:41:41 | ZEC | up | 0.09→0.16 | 0.03 → 0.03 → 0.03 | no | — |  |
| 10-03 17:41:37 | XRP | up | 0.16→0.21 | 0.16 → 0.16 → 0.16 | 5.31s | UP @ 0.17 | -0.01 / · / · |
| 10-03 17:41:37 | BTC | up | 0.90→0.97 | 0.88 → 0.88 → 0.88 | 20.56s | UP @ 0.88 | -0.16 / · / · |
| 10-03 17:41:37 | ETH | up | 0.76→0.84 | 0.59 → 0.59 → 0.59 | 5.56s | UP @ 0.60 | 2.55 / · / · |
| 10-03 17:41:32 | BNB | down | 0.66→0.56 | 0.81 → 0.81 → 0.81 | 10.81s | DOWN @ 0.22 | -0.73 / -0.92 / · |
| 10-03 17:41:19 | BTC | down | 0.95→0.89 | 0.93 → 0.93 → 0.93 | 9.06s | DOWN @ 0.07 | 0.35 / 0.26 / · |
| 10-03 17:41:18 | XRP | down | 0.23→0.14 | 0.18 → 0.18 → 0.18 | no | DOWN @ 0.82 | -0.11 / -0.64 / · |
| 10-03 17:41:14 | ZEC | up | 0.13→0.19 | 0.06 → 0.06 → 0.06 | no | UP @ 0.07 | -0.24 / -0.52 / · |
| 10-03 17:41:12 | BNB | up | 0.62→0.69 | 0.75 → 0.75 → 0.74 | 16.06s | — |  |
| 10-03 17:41:02 | DOGE | down | 0.15→0.08 | 0.12 → 0.12 → 0.12 | 10.31s | DOWN @ 0.88 | -0.26 / 0.75 / · |
| 10-03 17:41:01 | ETH | down | 0.82→0.75 | 0.81 → 0.81 → 0.81 | 11.81s | DOWN @ 0.20 | -0.33 / 1.71 / · |
| 10-03 17:41:00 | BTC | down | 0.96→0.90 | 0.95 → 0.95 → 0.95 | 28.07s | — |  |
| 10-03 17:40:59 | ZEC | down | 0.26→0.17 | 0.12 → 0.11 → 0.11 | 13.31s | — |  |
| 10-03 17:40:48 | XRP | up | 0.30→0.35 | 0.29 → 0.29 → 0.29 | no | — |  |
| 10-03 17:40:38 | ETH | up | 0.67→0.74 | 0.59 → 0.59 → 0.59 | 5.06s | UP @ 0.60 | 0.99 / 1.71 / · |
| 10-03 17:40:36 | ZEC | up | 0.22→0.31 | 0.14 → 0.14 → 0.14 | no | — |  |
| 10-03 17:40:33 | XRP | up | 0.28→0.33 | 0.22 → 0.22 → 0.22 | 9.31s | UP @ 0.23 | 0.22 / 0.13 / · |
| 10-03 17:40:32 | BNB | up | 0.49→0.60 | 0.64 → 0.64 → 0.64 | 25.31s | — |  |
| 10-03 17:40:32 | HYPE | up | 0.74→0.85 | 0.86 → 0.86 → 0.86 | no | — |  |
| 10-03 17:40:31 | BTC | up | 0.74→0.83 | 0.74 → 0.74 → 0.74 | 11.81s | UP @ 0.75 | -0.38 / 1.83 / · |
| 10-03 17:40:18 | XRP | down | 0.28→0.23 | 0.24 → 0.24 → 0.24 | no | — |  |
| 10-03 17:40:15 | BNB | down | 0.57→0.49 | 0.64 → 0.64 → 0.64 | no | DOWN @ 0.37 | -0.53 / -0.92 / · |
| 10-03 17:40:14 | ZEC | down | 0.32→0.25 | 0.20 → 0.14 → 0.14 | 0.27s | — |  |
| 10-03 17:40:02 | XRP | down | 0.34→0.29 | 0.30 → 0.30 → 0.30 | 10.31s | — |  |
| 10-03 17:40:01 | ETH | down | 0.66→0.60 | 0.61 → 0.61 → 0.61 | 11.81s | — |  |
| 10-03 17:40:00 | BNB | down | 0.52→0.46 | 0.52 → 0.52 → 0.52 | no | DOWN @ 0.49 | -0.56 / -1.84 / · |
| 10-03 17:39:47 | XRP | down | 0.37→0.32 | 0.30 → 0.30 → 0.30 | 25.31s | — |  |
