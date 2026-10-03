# Lag Tracker

*Updated Sat Oct 03 19:02 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 125 | 11.1s | 6% | 0% |
| BTC | 85 | 10.7s | 4% | 0% |
| DOGE | 91 | 8.9s | 4% | 0% |
| ETH | 74 | 11.2s | 3% | 0% |
| HYPE | 63 | 11.6s | 2% | 0% |
| NEAR | 77 | 9.5s | 4% | 0% |
| SOL | 169 | 7.9s | 7% | 0% |
| XRP | 142 | 8.8s | 9% | 0% |
| ZEC | 122 | 8.6s | 6% | 0% |
| **All** | **948** | **9.6s** | **5%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 494 | 174 | $-15.66 | -0.8% | $0.09 / $-15.75 |
| Sell after 30 sec | 493 | 333 | $275.17 | +13.7% | $139.73 / $135.44 |
| Hold to the close | 482 | 249 | $534.41 | +27.3% | $210.64 / $323.77 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 19:02:32 | HYPE | down | 0.37→0.26 | 0.34 → 0.34 → — | no | DOWN @ 0.67 | · / · / · |
| 10-03 19:02:21 | DOGE | down | 0.29→0.24 | 0.39 → 0.39 → 0.39 | no | DOWN @ 0.62 | -0.44 / · / · |
| 10-03 19:02:05 | SOL | down | 0.27→0.20 | 0.23 → 0.23 → 0.23 | 20.54s | — |  |
| 10-03 19:02:02 | DOGE | up | 0.34→0.40 | 0.38 → 0.38 → 0.38 | no | — |  |
| 10-03 19:01:54 | BNB | down | 0.57→0.50 | 0.61 → 0.61 → 0.58 | 16.79s | DOWN @ 0.39 | -0.14 / 0.05 / · |
| 10-03 19:01:35 | BTC | down | 0.37→0.30 | 0.38 → 0.34 → 0.34 | 20.54s | — |  |
| 10-03 19:01:34 | ETH | down | 0.40→0.33 | 0.41 → 0.41 → 0.34 | 2.04s | DOWN @ 0.60 | 0.27 / 0.88 / · |
| 10-03 19:01:33 | DOGE | down | 0.53→0.47 | 0.59 → 0.59 → 0.52 | 2.29s | DOWN @ 0.42 | 0.24 / 1.55 / · |
| 10-03 19:01:20 | NEAR | down | 0.53→0.47 | 0.40 → 0.40 → 0.55 | 21.04s | — |  |
| 10-03 19:01:20 | SOL | down | 0.41→0.35 | 0.41 → 0.41 → 0.41 | 15.54s | DOWN @ 0.60 | -0.55 / 0.58 / · |
| 10-03 19:01:20 | BNB | up | 0.54→0.59 | 0.55 → 0.55 → 0.62 | 1.04s | — |  |
| 10-03 19:01:05 | BTC | down | 0.39→0.30 | 0.35 → 0.35 → 0.38 | no | — |  |
| 10-03 19:01:00 | NEAR | up | 0.39→0.48 | 0.36 → 0.36 → 0.36 | 20.55s | UP @ 0.37 | -0.24 / 1.15 / · |
| 10-03 19:00:59 | DOGE | up | 0.47→0.53 | 0.47 → 0.47 → 0.47 | 6.31s | UP @ 0.47 | 0.44 / 0.74 / · |
| 10-03 19:00:58 | SOL | up | 0.30→0.38 | 0.47 → 0.47 → 0.47 | no | — |  |
| 10-03 19:00:57 | BNB | down | 0.52→0.44 | 0.49 → 0.49 → 0.49 | no | — |  |
| 10-03 19:00:45 | ETH | down | 0.53→0.43 | 0.55 → 0.55 → 0.55 | 21.07s | DOWN @ 0.46 | -0.36 / 0.74 / · |
| 10-03 19:00:44 | NEAR | down | 0.47→0.39 | 0.53 → 0.53 → 0.53 | 6.30s | DOWN @ 0.48 | 1.15 / 0.75 / · |
| 10-03 19:00:44 | BTC | down | 0.49→0.43 | 0.48 → 0.48 → 0.48 | 6.55s | DOWN @ 0.52 | 0.85 / 0.65 / · |
| 10-03 19:00:43 | SOL | down | 0.47→0.41 | 0.53 → 0.53 → 0.53 | 7.80s | DOWN @ 0.48 | -0.06 / 0.75 / · |
| 10-03 19:00:38 | BNB | up | 0.46→0.54 | 0.47 → 0.47 → 0.47 | 27.57s | UP @ 0.48 | -0.46 / 0.24 / · |
| 10-03 18:58:42 | SOL | up | 0.10→0.16 | 0.41 → 0.41 → 0.49 | 2.30s | — |  |
| 10-03 18:58:42 | BTC | down | 0.85→0.57 | 0.94 → 0.94 → 0.95 | 17.81s | DOWN @ 0.06 | -0.15 / 3.99 / -0.63 |
| 10-03 18:58:29 | ZEC | up | 0.49→0.54 | 0.33 → 0.33 → 0.26 | no | UP @ 0.33 | -1.29 / -1.29 / 6.54 |
| 10-03 18:58:27 | SOL | up | 0.21→0.39 | 0.28 → 0.28 → 0.41 | 2.30s | UP @ 0.30 | 0.58 / 1.47 / -3.15 |
| 10-03 18:58:12 | SOL | down | 0.40→0.23 | 0.32 → 0.32 → 0.28 | no | DOWN @ 0.69 | -0.20 / -1.53 / 2.95 |
| 10-03 18:58:07 | ZEC | down | 0.52→0.40 | 0.33 → 0.33 → 0.33 | 23.06s | — |  |
| 10-03 18:57:57 | SOL | down | 0.33→0.25 | 0.34 → 0.34 → 0.32 | 17.31s | DOWN @ 0.67 | -0.22 / -0.01 / 3.14 |
| 10-03 18:57:55 | NEAR | up | 0.58→0.73 | 0.81 → 0.81 → 0.81 | 5.06s | — |  |
| 10-03 18:57:54 | BTC | down | 0.77→0.67 | 0.84 → 0.84 → 0.84 | no | DOWN @ 0.16 | -0.58 / -1.15 / -1.70 |
