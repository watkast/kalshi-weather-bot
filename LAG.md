# Lag Tracker

*Updated Sat Oct 03 18:02 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 51 | 11.6s | 6% | 0% |
| BTC | 47 | 10.6s | 4% | 0% |
| DOGE | 52 | 9.2s | 4% | 0% |
| ETH | 42 | 9.9s | 2% | 0% |
| HYPE | 38 | 9.8s | 3% | 0% |
| NEAR | 28 | 9.0s | 7% | 0% |
| SOL | 86 | 7.2s | 5% | 0% |
| XRP | 78 | 8.1s | 12% | 0% |
| ZEC | 72 | 9.8s | 6% | 0% |
| **All** | **494** | **9.1s** | **6%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 259 | 102 | $2.79 | +0.3% | $-7.94 / $10.73 |
| Sell after 30 sec | 258 | 179 | $148.59 | +14.0% | $72.42 / $76.17 |
| Hold to the close | 257 | 129 | $230.87 | +21.8% | $122.77 / $108.10 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 18:02:00 | SOL | down | 0.47→0.41 | 0.41 → 0.41 → 0.45 | no | — |  |
| 10-03 18:02:00 | BTC | up | 0.43→0.49 | 0.43 → 0.43 → 0.45 | no | UP @ 0.44 | -0.36 / · / · |
| 10-03 18:02:00 | ETH | up | 0.39→0.46 | 0.36 → 0.36 → 0.40 | no | — |  |
| 10-03 18:01:56 | ZEC | up | 0.59→0.66 | 0.64 → 0.64 → 0.67 | no | — |  |
| 10-03 18:01:49 | DOGE | up | 0.52→0.62 | 0.61 → 0.61 → 0.61 | 12.03s | — |  |
| 10-03 18:01:38 | HYPE | up | 0.55→0.63 | 0.59 → 0.59 → 0.59 | 7.79s | — |  |
| 10-03 18:01:38 | XRP | up | 0.51→0.56 | 0.54 → 0.54 → 0.54 | 23.04s | — |  |
| 10-03 18:01:23 | XRP | up | 0.49→0.54 | 0.53 → 0.53 → 0.53 | no | — |  |
| 10-03 18:01:20 | NEAR | up | 0.44→0.49 | 0.58 → 0.58 → 0.58 | 26.29s | — |  |
| 10-03 18:01:11 | DOGE | up | 0.40→0.52 | 0.41 → 0.41 → 0.41 | 20.29s | UP @ 0.42 | -0.26 / 1.24 / · |
| 10-03 18:01:05 | NEAR | up | 0.44→0.51 | 0.45 → 0.45 → 0.45 | 11.29s | — |  |
| 10-03 17:58:38 | SOL | down | 0.14→0.09 | 0.32 → 0.32 → 0.34 | 16.31s | DOWN @ 0.69 | -0.82 / 0.73 / 2.95 |
| 10-03 17:58:31 | XRP | down | 0.40→0.15 | 0.15 → 0.15 → 0.15 | no | — |  |
| 10-03 17:58:31 | ZEC | down | 0.73→0.64 | 0.77 → 0.77 → 0.77 | no | — |  |
| 10-03 17:58:23 | SOL | up | 0.29→0.36 | 0.14 → 0.14 → 0.32 | 1.31s | UP @ 0.15 | 1.36 / 1.55 / -1.59 |
| 10-03 17:58:16 | DOGE | up | 0.14→0.26 | 0.38 → 0.38 → 0.38 | no | — |  |
| 10-03 17:58:16 | XRP | up | 0.28→0.41 | 0.12 → 0.12 → 0.12 | 23.07s | UP @ 0.12 | 0.13 / 1.86 / 8.72 |
| 10-03 17:58:09 | HYPE | down | 0.90→0.83 | 0.90 → 0.88 → 0.88 | no | DOWN @ 0.13 | -0.35 / -1.07 / -1.38 |
| 10-03 17:58:06 | SOL | up | 0.07→0.12 | 0.30 → 0.30 → 0.14 | no | — |  |
| 10-03 17:58:01 | ZEC | down | 0.73→0.68 | 0.84 → 0.84 → 0.84 | 8.31s | — |  |
| 10-03 17:58:00 | DOGE | down | 0.30→0.17 | 0.47 → 0.47 → 0.47 | 8.56s | DOWN @ 0.54 | 0.35 / -0.16 / -5.58 |
| 10-03 17:57:57 | XRP | down | 0.31→0.24 | 0.21 → 0.21 → 0.21 | 11.56s | — |  |
| 10-03 17:57:51 | SOL | up | 0.14→0.23 | 0.10 → 0.10 → 0.30 | 3.31s | UP @ 0.11 | 1.58 / 0.14 / -1.17 |
| 10-03 17:57:38 | BTC | up | 0.84→0.91 | 0.90 → 0.90 → 0.91 | 16.06s | — |  |
| 10-03 17:57:37 | DOGE | up | 0.20→0.31 | 0.26 → 0.26 → 0.42 | 1.56s | UP @ 0.26 | 1.28 / 1.68 / 7.26 |
| 10-03 17:57:35 | SOL | up | 0.08→0.13 | 0.05 → 0.05 → 0.10 | 3.81s | UP @ 0.06 | 0.26 / 2.15 / -0.60 |
| 10-03 17:57:33 | XRP | up | 0.19→0.24 | 0.14 → 0.14 → 0.14 | 20.81s | UP @ 0.14 | -0.46 / 0.39 / 8.51 |
| 10-03 17:57:32 | ZEC | up | 0.57→0.68 | 0.63 → 0.63 → 0.63 | 21.56s | — |  |
| 10-03 17:57:22 | DOGE | up | 0.08→0.23 | 0.28 → 0.28 → 0.26 | 16.57s | — |  |
| 10-03 17:57:17 | HYPE | up | 0.63→0.76 | 0.79 → 0.79 → 0.79 | no | — |  |
