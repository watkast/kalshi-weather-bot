# Lag Tracker

*Updated Sat Oct 03 18:42 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 105 | 11.1s | 6% | 0% |
| BTC | 73 | 10.8s | 4% | 0% |
| DOGE | 85 | 9.1s | 5% | 0% |
| ETH | 67 | 11.1s | 3% | 0% |
| HYPE | 51 | 11.3s | 2% | 0% |
| NEAR | 62 | 10.2s | 5% | 0% |
| SOL | 138 | 7.6s | 7% | 0% |
| XRP | 135 | 8.7s | 8% | 0% |
| ZEC | 106 | 9.1s | 7% | 0% |
| **All** | **822** | **9.6s** | **6%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 430 | 155 | $-14.15 | -0.8% | $-10.11 / $-4.04 |
| Sell after 30 sec | 428 | 291 | $242.48 | +13.8% | $111.68 / $130.80 |
| Hold to the close | 377 | 200 | $438.73 | +28.1% | $171.62 / $267.11 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 18:42:26 | ZEC | up | 0.56→0.63 | 0.27 → 0.27 → — | no | UP @ 0.28 | · / · / · |
| 10-03 18:42:19 | SOL | up | 0.52→0.57 | 0.38 → 0.52 → 0.52 | 0.27s | — |  |
| 10-03 18:42:16 | XRP | down | 0.32→0.25 | 0.18 → 0.18 → 0.30 | no | — |  |
| 10-03 18:42:06 | ZEC | up | 0.32→0.39 | 0.07 → 0.10 → 0.10 | 13.31s | UP @ 0.10 | -0.15 / · / · |
| 10-03 18:42:03 | SOL | up | 0.42→0.52 | 0.36 → 0.36 → 0.38 | 15.56s | UP @ 0.37 | -0.34 / · / · |
| 10-03 18:42:02 | NEAR | up | 0.88→0.94 | 0.98 → 0.98 → 0.99 | no | — |  |
| 10-03 18:42:01 | DOGE | up | 0.73→0.87 | 0.93 → 0.93 → 0.93 | no | — |  |
| 10-03 18:41:55 | XRP | up | 0.17→0.24 | 0.17 → 0.17 → 0.17 | 23.57s | UP @ 0.18 | -0.22 / 0.84 / · |
| 10-03 18:41:51 | ZEC | up | 0.23→0.29 | 0.07 → 0.07 → 0.07 | 28.32s | UP @ 0.09 | -0.40 / 1.40 / · |
| 10-03 18:41:48 | SOL | down | 0.43→0.34 | 0.50 → 0.50 → 0.36 | 0.55s | DOWN @ 0.51 | 0.85 / 0.75 / · |
| 10-03 18:41:39 | XRP | down | 0.28→0.20 | 0.29 → 0.29 → 0.29 | 9.56s | DOWN @ 0.71 | 0.84 / 0.74 / · |
| 10-03 18:41:35 | BNB | down | 0.54→0.46 | 0.64 → 0.64 → 0.64 | no | DOWN @ 0.37 | -0.53 / -0.73 / · |
| 10-03 18:41:30 | SOL | down | 0.47→0.39 | 0.64 → 0.64 → 0.50 | 3.56s | DOWN @ 0.38 | 0.75 / 2.16 / · |
| 10-03 18:41:29 | DOGE | down | 0.84→0.77 | 0.93 → 0.93 → 0.93 | no | DOWN @ 0.08 | 0.05 / -0.20 / · |
| 10-03 18:41:24 | XRP | down | 0.32→0.23 | 0.56 → 0.56 → 0.56 | 9.56s | DOWN @ 0.44 | 2.27 / 3.51 / · |
| 10-03 18:41:22 | ZEC | down | 0.31→0.21 | 0.14 → 0.14 → 0.14 | 11.81s | — |  |
| 10-03 18:41:18 | BNB | down | 0.69→0.56 | 0.88 → 0.88 → 0.85 | 16.06s | DOWN @ 0.14 | -0.27 / 1.85 / · |
| 10-03 18:41:09 | XRP | down | 0.47→0.41 | 0.71 → 0.71 → 0.71 | 9.56s | DOWN @ 0.29 | 1.07 / 3.80 / · |
| 10-03 18:41:03 | BNB | down | 0.79→0.72 | 0.88 → 0.88 → 0.88 | no | DOWN @ 0.13 | -0.48 / -0.16 / · |
| 10-03 18:41:01 | SOL | up | 0.47→0.55 | 0.48 → 0.48 → 0.59 | 2.80s | UP @ 0.49 | 0.54 / 0.95 / · |
| 10-03 18:41:00 | ZEC | up | 0.28→0.35 | 0.15 → 0.15 → 0.18 | no | UP @ 0.16 | -0.10 / -0.39 / · |
| 10-03 18:40:54 | XRP | up | 0.41→0.47 | 0.58 → 0.58 → 0.58 | 10.31s | — |  |
| 10-03 18:40:52 | NEAR | up | 0.72→0.83 | 0.90 → 0.90 → 0.90 | 12.06s | — |  |
| 10-03 18:40:45 | SOL | down | 0.47→0.40 | 0.57 → 0.57 → 0.48 | 3.81s | DOWN @ 0.44 | 0.34 / -0.75 / · |
| 10-03 18:40:38 | XRP | up | 0.41→0.47 | 0.58 → 0.58 → 0.58 | 25.81s | — |  |
| 10-03 18:40:31 | ZEC | down | 0.40→0.28 | 0.34 → 0.34 → 0.25 | 3.06s | — |  |
| 10-03 18:40:31 | BNB | up | 0.67→0.75 | 0.80 → 0.80 → 0.84 | 3.31s | — |  |
| 10-03 18:40:30 | SOL | up | 0.44→0.51 | 0.57 → 0.57 → 0.57 | no | — |  |
| 10-03 18:40:18 | XRP | down | 0.55→0.50 | 0.41 → 0.41 → 0.64 | no | — |  |
| 10-03 18:40:16 | NEAR | up | 0.63→0.72 | 0.83 → 0.83 → 0.88 | 3.31s | — |  |
