# Lag Tracker

*Updated Sun Oct 04 02:54 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 455 | 10.6s | 4% | 0% |
| BTC | 368 | 12.4s | 2% | 0% |
| DOGE | 487 | 10.5s | 2% | 0% |
| ETH | 461 | 11.2s | 3% | 0% |
| HYPE | 368 | 11.7s | 3% | 0% |
| NEAR | 403 | 10.8s | 4% | 0% |
| SOL | 899 | 10.6s | 3% | 0% |
| XRP | 824 | 11.1s | 3% | 0% |
| ZEC | 521 | 9.7s | 5% | 0% |
| **All** | **4786** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2519 | 702 | $-290.69 | -2.7% | $-118.37 / $-172.32 |
| Sell after 30 sec | 2517 | 1461 | $795.53 | +7.3% | $480.10 / $315.43 |
| Hold to the close | 2475 | 1237 | $1676.79 | +15.7% | $1010.60 / $666.19 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **38 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 02:54:05 | ZEC | up | 0.38→0.45 | 0.34 → 0.46 → — | 0.27s | — |  |
| 10-04 02:54:04 | SOL | down | 0.83→0.72 | 0.82 → 0.82 → 0.83 | no | DOWN @ 0.19 | · / · / · |
| 10-04 02:54:03 | XRP | down | 0.38→0.27 | 0.38 → 0.38 → 0.32 | 2.04s | DOWN @ 0.63 | · / · / · |
| 10-04 02:53:58 | ETH | down | 0.51→0.43 | 0.65 → 0.65 → 0.65 | no | DOWN @ 0.36 | -0.24 / · / · |
| 10-04 02:53:43 | XRP | up | 0.28→0.35 | 0.38 → 0.38 → 0.38 | no | — |  |
| 10-04 02:53:42 | ZEC | down | 0.39→0.31 | 0.39 → 0.39 → 0.39 | 7.53s | DOWN @ 0.63 | -0.13 / · / · |
| 10-04 02:53:41 | ETH | up | 0.47→0.56 | 0.57 → 0.57 → 0.57 | 8.78s | — |  |
| 10-04 02:53:40 | BTC | up | 0.28→0.36 | 0.35 → 0.35 → 0.35 | 10.04s | — |  |
| 10-04 02:53:34 | SOL | down | 0.80→0.70 | 0.80 → 0.80 → 0.79 | no | — |  |
| 10-04 02:53:27 | NEAR | down | 0.17→0.11 | 0.21 → 0.21 → 0.21 | 22.79s | DOWN @ 0.80 | -0.55 / 0.81 / · |
| 10-04 02:53:27 | XRP | up | 0.28→0.39 | 0.41 → 0.41 → 0.40 | no | — |  |
| 10-04 02:53:17 | SOL | down | 0.82→0.76 | 0.85 → 0.85 → 0.85 | 10.54s | DOWN @ 0.15 | -0.28 / 0.29 / · |
| 10-04 02:53:12 | XRP | up | 0.35→0.42 | 0.43 → 0.43 → 0.41 | no | — |  |
| 10-04 02:53:11 | ZEC | down | 0.49→0.43 | 0.54 → 0.54 → 0.48 | 2.03s | DOWN @ 0.47 | -0.06 / 0.95 / · |
| 10-04 02:52:57 | XRP | up | 0.35→0.43 | 0.41 → 0.41 → 0.43 | no | — |  |
| 10-04 02:52:53 | ZEC | down | 0.54→0.48 | 0.63 → 0.63 → 0.63 | 5.03s | DOWN @ 0.38 | 0.35 / 0.85 / · |
| 10-04 02:52:42 | XRP | up | 0.36→0.43 | 0.41 → 0.41 → 0.41 | no | — |  |
| 10-04 02:52:41 | BNB | down | 0.12→0.03 | 0.07 → 0.07 → 0.08 | no | DOWN @ 0.93 | -0.20 / -0.20 / · |
| 10-04 02:52:38 | ZEC | up | 0.53→0.58 | 0.57 → 0.57 → 0.57 | 5.03s | — |  |
| 10-04 02:52:27 | XRP | down | 0.46→0.35 | 0.48 → 0.48 → 0.41 | 1.03s | DOWN @ 0.52 | 0.35 / 0.24 / · |
| 10-04 02:52:20 | ZEC | down | 0.69→0.61 | 0.70 → 0.70 → 0.70 | 8.28s | DOWN @ 0.30 | 0.87 / 0.28 / · |
| 10-04 02:52:13 | ETH | down | 0.58→0.47 | 0.59 → 0.59 → 0.59 | 14.54s | DOWN @ 0.41 | -0.44 / 0.85 / · |
| 10-04 02:52:12 | HYPE | down | 0.62→0.55 | 0.68 → 0.68 → 0.63 | 0.53s | DOWN @ 0.33 | -0.03 / 0.96 / · |
| 10-04 02:52:10 | BNB | down | 0.23→0.14 | 0.19 → 0.19 → 0.17 | 17.79s | — |  |
| 10-04 02:52:10 | XRP | down | 0.57→0.50 | 0.58 → 0.58 → 0.48 | 3.29s | DOWN @ 0.42 | 0.54 / 1.35 / · |
| 10-04 02:51:55 | XRP | up | 0.50→0.57 | 0.60 → 0.60 → 0.58 | no | — |  |
| 10-04 02:51:39 | ZEC | down | 0.70→0.63 | 0.82 → 0.82 → 0.71 | 3.57s | DOWN @ 0.19 | 0.64 / 0.74 / · |
| 10-04 02:51:39 | XRP | down | 0.57→0.50 | 0.70 → 0.70 → 0.60 | 4.32s | DOWN @ 0.30 | 0.58 / 0.78 / · |
| 10-04 02:51:25 | BTC | down | 0.47→0.42 | 0.39 → 0.39 → 0.41 | 18.07s | — |  |
| 10-04 02:51:21 | XRP | down | 0.67→0.57 | 0.71 → 0.71 → 0.71 | 22.32s | DOWN @ 0.29 | -0.30 / 0.68 / · |
