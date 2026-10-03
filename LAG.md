# Lag Tracker

*Updated Sat Oct 03 18:32 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 89 | 10.8s | 7% | 0% |
| BTC | 71 | 10.8s | 4% | 0% |
| DOGE | 74 | 9.3s | 4% | 0% |
| ETH | 64 | 10.9s | 3% | 0% |
| HYPE | 48 | 11.6s | 2% | 0% |
| NEAR | 50 | 9.9s | 6% | 0% |
| SOL | 120 | 7.6s | 6% | 0% |
| XRP | 120 | 8.4s | 9% | 0% |
| ZEC | 94 | 9.1s | 6% | 0% |
| **All** | **730** | **9.3s** | **6%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 385 | 137 | $-15.77 | -1.0% | $-10.41 / $-5.36 |
| Sell after 30 sec | 385 | 264 | $215.37 | +13.5% | $101.44 / $113.93 |
| Hold to the close | 377 | 200 | $438.73 | +28.1% | $171.62 / $267.11 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **29 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 18:32:19 | BNB | up | 0.53→0.60 | 0.58 → 0.65 → 0.65 | 0.25s | — |  |
| 10-03 18:31:55 | NEAR | down | 0.43→0.37 | 0.55 → 0.55 → 0.55 | 9.04s | DOWN @ 0.47 | 0.24 / 0.24 / · |
| 10-03 18:31:53 | HYPE | down | 0.36→0.27 | 0.40 → 0.40 → 0.40 | 25.30s | DOWN @ 0.61 | -0.44 / 1.09 / · |
| 10-03 18:31:36 | ZEC | up | 0.32→0.37 | 0.28 → 0.28 → 0.28 | no | UP @ 0.29 | -0.40 / -1.07 / · |
| 10-03 18:31:22 | BNB | up | 0.51→0.57 | 0.58 → 0.58 → 0.58 | 26.80s | — |  |
| 10-03 18:31:05 | SOL | down | 0.31→0.23 | 0.36 → 0.34 → 0.34 | 13.80s | DOWN @ 0.67 | -0.42 / 0.71 / · |
| 10-03 18:31:04 | ZEC | down | 0.37→0.30 | 0.39 → 0.28 → 0.28 | 0.05s | — |  |
| 10-03 18:31:00 | NEAR | down | 0.60→0.54 | 0.73 → 0.73 → 0.73 | 18.55s | DOWN @ 0.27 | -0.38 / 0.69 / · |
| 10-03 18:30:55 | XRP | down | 0.47→0.42 | 0.59 → 0.59 → 0.59 | 8.55s | DOWN @ 0.41 | 0.65 / 1.25 / · |
| 10-03 18:30:55 | DOGE | down | 0.55→0.49 | 0.56 → 0.56 → 0.56 | 8.80s | DOWN @ 0.45 | -0.16 / 0.94 / · |
| 10-03 18:30:55 | ETH | down | 0.48→0.43 | 0.53 → 0.53 → 0.53 | 9.05s | DOWN @ 0.48 | 0.34 / 1.46 / · |
| 10-03 18:30:51 | BTC | down | 0.50→0.45 | — → 0.47 → 0.47 | no | — |  |
| 10-03 18:30:50 | SOL | down | 0.38→0.33 | — → 0.36 → 0.36 | no | — |  |
| 10-03 18:28:34 | BNB | down | 0.57→0.41 | 0.48 → 0.48 → 0.59 | no | DOWN @ 0.53 | -1.75 / -2.44 / -5.48 |
| 10-03 18:28:30 | BTC | down | 0.52→0.44 | 0.48 → 0.48 → 0.48 | 7.09s | — |  |
| 10-03 18:28:21 | SOL | down | 0.21→0.12 | 0.03 → 0.03 → 0.12 | no | — |  |
| 10-03 18:28:20 | ETH | down | 0.38→0.30 | 0.06 → 0.06 → 0.18 | no | — |  |
| 10-03 18:28:19 | BNB | up | 0.34→0.56 | 0.34 → 0.34 → 0.48 | 3.09s | — |  |
| 10-03 18:28:06 | SOL | up | 0.07→0.19 | 0.03 → 0.03 → 0.03 | 16.10s | — |  |
| 10-03 18:28:05 | BTC | up | 0.18→0.23 | 0.10 → 0.10 → 0.10 | 16.85s | UP @ 0.11 | -0.31 / 3.45 / -1.17 |
| 10-03 18:28:04 | ETH | up | 0.19→0.24 | 0.08 → 0.08 → 0.06 | 17.35s | UP @ 0.08 | -0.35 / 0.80 / -0.89 |
| 10-03 18:28:03 | XRP | up | 0.41→0.59 | 0.52 → 0.52 → 0.57 | 18.85s | UP @ 0.52 | 0.14 / 3.71 / 4.62 |
| 10-03 18:28:03 | BNB | down | 0.43→0.36 | 0.35 → 0.35 → 0.34 | no | — |  |
| 10-03 18:27:45 | ETH | down | 0.31→0.23 | 0.18 → 0.18 → 0.18 | 7.15s | — |  |
| 10-03 18:27:36 | BTC | down | 0.30→0.20 | 0.15 → 0.15 → 0.14 | no | — |  |
| 10-03 18:27:32 | BNB | up | 0.29→0.38 | 0.28 → 0.28 → 0.27 | 19.65s | UP @ 0.31 | -0.98 / -0.01 / 6.75 |
| 10-03 18:27:24 | XRP | up | 0.39→0.46 | 0.56 → 0.61 → 0.61 | 0.11s | — |  |
| 10-03 18:27:15 | SOL | down | 0.15→0.10 | 0.04 → 0.04 → 0.04 | no | — |  |
| 10-03 18:27:09 | XRP | up | 0.43→0.50 | 0.56 → 0.56 → 0.56 | 13.15s | — |  |
| 10-03 18:26:37 | BNB | down | 0.44→0.38 | 0.66 → 0.47 → 0.47 | 0.37s | DOWN @ 0.54 | -0.46 / 1.17 / -5.58 |
