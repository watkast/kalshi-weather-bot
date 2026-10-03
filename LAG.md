# Lag Tracker

*Updated Sat Oct 03 21:43 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 248 | 10.7s | 5% | 0% |
| BTC | 159 | 11.9s | 2% | 0% |
| DOGE | 250 | 10.4s | 2% | 0% |
| ETH | 194 | 11.1s | 4% | 0% |
| HYPE | 176 | 11.3s | 4% | 0% |
| NEAR | 180 | 9.9s | 4% | 0% |
| SOL | 380 | 9.4s | 4% | 0% |
| XRP | 364 | 10.3s | 4% | 0% |
| ZEC | 273 | 9.6s | 5% | 0% |
| **All** | **2224** | **10.5s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1165 | 346 | $-113.64 | -2.3% | $-27.09 / $-86.55 |
| Sell after 30 sec | 1164 | 711 | $445.84 | +9.0% | $298.00 / $147.84 |
| Hold to the close | 1090 | 562 | $961.46 | +20.6% | $571.25 / $390.21 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 21:43:32 | SOL | up | 0.18→0.27 | 0.62 → 0.62 → 0.62 | no | — |  |
| 10-03 21:43:27 | HYPE | up | 0.89→0.96 | 0.98 → 0.98 → 0.99 | no | — |  |
| 10-03 21:43:25 | DOGE | up | 0.20→0.52 | 0.51 → 0.51 → 0.59 | no | — |  |
| 10-03 21:43:21 | BTC | down | 0.85→0.64 | 0.96 → 0.96 → 0.96 | no | — |  |
| 10-03 21:43:20 | ETH | down | 0.27→0.22 | 0.20 → 0.20 → 0.20 | 7.31s | — |  |
| 10-03 21:43:19 | ZEC | down | 0.26→0.10 | 0.02 → 0.02 → 0.02 | no | — |  |
| 10-03 21:43:17 | SOL | up | 0.67→0.88 | 0.94 → 0.94 → 0.94 | no | — |  |
| 10-03 21:43:07 | DOGE | down | 0.32→0.23 | 0.49 → 0.49 → 0.49 | no | DOWN @ 0.51 | -0.56 / · / · |
| 10-03 21:43:04 | ZEC | up | 0.03→0.28 | 0.00 → 0.00 → 0.00 | no | — |  |
| 10-03 21:43:02 | SOL | up | 0.49→0.66 | 0.86 → 0.86 → 0.86 | no | — |  |
| 10-03 21:43:02 | ETH | down | 0.28→0.20 | 0.17 → 0.17 → 0.17 | 25.82s | — |  |
| 10-03 21:43:00 | BTC | up | 0.76→0.88 | 0.89 → 0.92 → 0.92 | 12.81s | — |  |
| 10-03 21:42:47 | SOL | down | 0.49→0.41 | 0.88 → 0.88 → 0.88 | no | DOWN @ 0.13 | -0.26 / -0.85 / · |
| 10-03 21:42:37 | BNB | down | 0.92→0.84 | 0.95 → 0.95 → 0.95 | no | DOWN @ 0.05 | -0.51 / -0.52 / · |
| 10-03 21:42:29 | ETH | up | 0.29→0.35 | 0.20 → 0.20 → 0.20 | no | UP @ 0.20 | -0.33 / -0.62 / · |
| 10-03 21:42:22 | SOL | up | 0.42→0.56 | 0.76 → 0.76 → 0.76 | 5.56s | — |  |
| 10-03 21:42:15 | BTC | down | 0.77→0.67 | 0.68 → 0.68 → 0.68 | no | — |  |
| 10-03 21:42:09 | ETH | up | 0.22→0.35 | 0.15 → 0.15 → 0.15 | no | UP @ 0.16 | -0.29 / 0.09 / · |
| 10-03 21:42:05 | DOGE | up | 0.44→0.52 | 0.59 → 0.59 → 0.59 | no | — |  |
| 10-03 21:42:00 | SOL | up | 0.36→0.42 | 0.69 → 0.69 → 0.69 | 12.31s | — |  |
| 10-03 21:42:00 | BTC | up | 0.56→0.67 | 0.51 → 0.54 → 0.54 | 12.81s | UP @ 0.54 | -0.46 / 2.30 / · |
| 10-03 21:41:54 | NEAR | up | 0.84→0.90 | 0.97 → 0.97 → 0.98 | no | — |  |
| 10-03 21:41:46 | ETH | down | 0.23→0.18 | 0.15 → 0.15 → 0.15 | no | — |  |
| 10-03 21:41:41 | XRP | down | 0.11→0.06 | 0.17 → 0.17 → 0.14 | 16.83s | DOWN @ 0.84 | -0.09 / 0.33 / · |
| 10-03 21:41:40 | ZEC | down | 0.09→0.04 | 0.06 → 0.06 → 0.04 | 17.83s | — |  |
| 10-03 21:41:36 | DOGE | down | 0.45→0.38 | 0.80 → 0.80 → 0.80 | 6.81s | — |  |
| 10-03 21:41:31 | BNB | down | 0.71→0.62 | 0.90 → 0.90 → 0.90 | no | DOWN @ 0.11 | -0.33 / -0.58 / · |
| 10-03 21:41:23 | SOL | down | 0.38→0.32 | 0.64 → 0.64 → 0.65 | no | DOWN @ 0.37 | -0.53 / -0.53 / · |
| 10-03 21:41:21 | DOGE | down | 0.51→0.38 | 0.79 → 0.79 → 0.79 | 22.07s | DOWN @ 0.22 | -0.54 / 1.50 / · |
| 10-03 21:41:17 | ETH | down | 0.26→0.20 | 0.24 → 0.24 → 0.24 | 26.07s | — |  |
