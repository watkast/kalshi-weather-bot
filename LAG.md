# Lag Tracker

*Updated Sat Oct 03 20:53 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 216 | 10.6s | 6% | 0% |
| BTC | 136 | 11.6s | 2% | 0% |
| DOGE | 210 | 10.2s | 2% | 0% |
| ETH | 144 | 10.6s | 3% | 0% |
| HYPE | 136 | 11.4s | 4% | 0% |
| NEAR | 148 | 9.3s | 4% | 0% |
| SOL | 320 | 9.1s | 4% | 0% |
| XRP | 318 | 9.9s | 4% | 0% |
| ZEC | 221 | 9.6s | 5% | 0% |
| **All** | **1849** | **10.1s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 952 | 305 | $-74.54 | -1.8% | $-14.50 / $-60.04 |
| Sell after 30 sec | 952 | 601 | $394.89 | +9.8% | $265.61 / $129.28 |
| Hold to the close | 910 | 436 | $513.77 | +13.4% | $501.19 / $12.58 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **34 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 20:53:14 | ETH | down | 0.40→0.32 | 0.41 → 0.40 → — | no | DOWN @ 0.61 | · / · / · |
| 10-03 20:53:08 | HYPE | down | 0.18→0.13 | 0.17 → 0.17 → 0.17 | no | — |  |
| 10-03 20:53:08 | ZEC | down | 0.29→0.24 | 0.17 → 0.17 → 0.14 | 4.90s | — |  |
| 10-03 20:52:46 | DOGE | up | 0.21→0.30 | 0.38 → 0.38 → 0.38 | no | — |  |
| 10-03 20:52:41 | XRP | up | 0.17→0.22 | 0.30 → 0.30 → 0.30 | no | — |  |
| 10-03 20:52:37 | HYPE | up | 0.14→0.19 | 0.14 → 0.14 → 0.14 | 5.88s | — |  |
| 10-03 20:52:26 | XRP | down | 0.25→0.18 | 0.26 → 0.26 → 0.30 | no | DOWN @ 0.75 | -0.89 / -0.89 / · |
| 10-03 20:52:16 | HYPE | up | 0.07→0.12 | 0.12 → 0.12 → 0.12 | 26.39s | — |  |
| 10-03 20:52:00 | DOGE | up | 0.17→0.23 | 0.20 → 0.20 → 0.20 | 12.89s | — |  |
| 10-03 20:51:57 | ZEC | down | 0.27→0.21 | 0.12 → 0.12 → 0.10 | no | — |  |
| 10-03 20:51:26 | XRP | down | 0.45→0.14 | 0.52 → 0.52 → 0.52 | 16.15s | DOWN @ 0.49 | -0.56 / 2.39 / · |
| 10-03 20:51:26 | HYPE | down | 0.18→0.06 | 0.20 → 0.20 → 0.20 | 16.15s | DOWN @ 0.80 | -0.34 / 0.50 / · |
| 10-03 20:51:26 | SOL | down | 0.20→0.06 | 0.23 → 0.23 → 0.26 | no | DOWN @ 0.78 | -0.77 / -0.67 / · |
| 10-03 20:51:22 | ZEC | down | 0.31→0.25 | 0.17 → 0.17 → 0.17 | 20.90s | — |  |
| 10-03 20:51:16 | ETH | down | 0.82→0.77 | 0.78 → 0.78 → 0.78 | 26.41s | — |  |
| 10-03 20:51:06 | XRP | up | 0.42→0.47 | 0.48 → 0.48 → 0.48 | 6.92s | — |  |
| 10-03 20:51:01 | ETH | down | 0.72→0.65 | 0.71 → 0.71 → 0.71 | no | DOWN @ 0.29 | -0.40 / -1.36 / · |
| 10-03 20:50:48 | XRP | up | 0.42→0.50 | 0.54 → 0.54 → 0.54 | no | — |  |
| 10-03 20:50:40 | DOGE | up | 0.31→0.41 | 0.38 → 0.38 → 0.41 | 17.41s | — |  |
| 10-03 20:50:33 | XRP | up | 0.40→0.47 | 0.41 → 0.41 → 0.41 | 9.16s | UP @ 0.42 | 0.64 / 0.24 / · |
| 10-03 20:50:26 | HYPE | up | 0.09→0.16 | 0.08 → 0.08 → 0.13 | 1.66s | UP @ 0.09 | 0.21 / 0.31 / · |
| 10-03 20:50:20 | BNB | down | 0.12→0.07 | 0.20 → 0.20 → 0.20 | 7.66s | DOWN @ 0.81 | 0.41 / 0.30 / · |
| 10-03 20:50:17 | XRP | up | 0.36→0.43 | 0.41 → 0.41 → 0.41 | 25.92s | — |  |
| 10-03 20:50:13 | ETH | up | 0.50→0.56 | 0.52 → 0.54 → 0.54 | 29.92s | — |  |
| 10-03 20:50:05 | SOL | down | 0.21→0.15 | 0.23 → 0.23 → 0.23 | no | DOWN @ 0.77 | -0.36 / -0.67 / · |
| 10-03 20:50:03 | DOGE | up | 0.28→0.34 | 0.34 → 0.34 → 0.34 | 24.42s | — |  |
| 10-03 20:50:00 | XRP | down | 0.50→0.43 | 0.48 → 0.48 → 0.48 | 12.17s | DOWN @ 0.52 | -0.46 / 0.24 / · |
| 10-03 20:49:55 | ETH | up | 0.44→0.50 | 0.57 → 0.57 → 0.52 | no | — |  |
| 10-03 20:49:45 | XRP | down | 0.45→0.38 | 0.29 → 0.29 → 0.29 | no | — |  |
| 10-03 20:49:36 | ETH | up | 0.54→0.64 | 0.39 → 0.39 → 0.39 | 6.17s | UP @ 0.39 | 1.35 / 0.85 / · |
