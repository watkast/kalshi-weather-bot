# Lag Tracker

*Updated Sat Oct 03 17:18 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (sell after 30 sec).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 8 | 9.0s | 0% | -0% |
| BTC | 10 | 14.0s | 0% | -0% |
| DOGE | 6 | 9.5s | 0% | -0% |
| ETH | 6 | 18.9s | 0% | 0% |
| HYPE | 12 | 6.9s | 8% | -0% |
| NEAR | 6 | 11.1s | 0% | 0% |
| SOL | 8 | 4.2s | 12% | 0% |
| XRP | 9 | 1.7s | 25% | 0% |
| ZEC | 5 | 5.8s | 0% | -0% |
| **All** | **70** | **8.8s** | **6%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 37 | 11 | $-7.10 | -4.4% | $-4.55 / $-2.55 |
| Sell after 30 sec | 35 | 23 | $10.78 | +7.2% | $3.31 / $7.47 |
| Hold to the close | 7 | 0 | $-9.82 | -100.0% | $-4.72 / $-5.10 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **48 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 17:18:45 | ZEC | up | 0.54→0.60 | 0.56 → 0.56 → 0.56 | no | — |  |
| 10-03 17:18:44 | NEAR | up | 0.29→0.37 | 0.28 → 0.28 → 0.28 | no | UP @ 0.29 | · / · / · |
| 10-03 17:18:43 | DOGE | up | 0.43→0.50 | 0.47 → 0.47 → 0.47 | no | — |  |
| 10-03 17:18:38 | XRP | up | 0.45→0.55 | 0.48 → 0.48 → 0.51 | no | UP @ 0.49 | -0.26 / · / · |
| 10-03 17:18:37 | SOL | up | 0.69→0.74 | 0.74 → 0.74 → 0.76 | no | — |  |
| 10-03 17:18:32 | ETH | up | 0.40→0.46 | 0.47 → 0.47 → 0.47 | 8.74s | UP @ 0.48 | -0.06 / · / · |
| 10-03 17:18:32 | BNB | up | 0.41→0.46 | 0.50 → 0.50 → 0.50 | 8.99s | — |  |
| 10-03 17:18:30 | ZEC | down | 0.59→0.54 | 0.54 → 0.54 → 0.54 | no | — |  |
| 10-03 17:18:23 | XRP | up | 0.41→0.48 | 0.40 → 0.40 → 0.48 | 2.99s | UP @ 0.41 | 0.35 / 0.55 / · |
| 10-03 17:18:19 | HYPE | up | 0.19→0.32 | 0.28 → 0.28 → 0.28 | no | — |  |
| 10-03 17:18:17 | BNB | down | 0.55→0.49 | 0.47 → 0.47 → 0.47 | no | — |  |
| 10-03 17:18:14 | ETH | up | 0.40→0.46 | 0.48 → 0.48 → 0.48 | 27.00s | — |  |
| 10-03 17:18:13 | NEAR | up | 0.21→0.29 | 0.19 → 0.19 → 0.19 | 12.75s | UP @ 0.20 | -0.43 / 0.34 / · |
| 10-03 17:18:12 | DOGE | up | 0.27→0.43 | 0.47 → 0.47 → 0.47 | no | — |  |
| 10-03 17:18:08 | XRP | up | 0.39→0.45 | 0.39 → 0.39 → 0.40 | 18.00s | UP @ 0.39 | -0.34 / 0.55 / · |
| 10-03 17:18:06 | SOL | up | 0.55→0.65 | 0.58 → 0.58 → 0.68 | 4.25s | UP @ 0.59 | 0.47 / 1.19 / · |
| 10-03 17:18:05 | ZEC | up | 0.48→0.56 | 0.48 → 0.48 → 0.48 | 5.75s | UP @ 0.49 | 0.14 / -0.06 / · |
| 10-03 17:18:02 | HYPE | down | 0.30→0.23 | 0.30 → 0.30 → 0.30 | no | DOWN @ 0.70 | -0.20 / -0.30 / · |
| 10-03 17:18:02 | BNB | up | 0.36→0.42 | 0.51 → 0.51 → 0.51 | no | — |  |
| 10-03 17:17:53 | XRP | down | 0.37→0.29 | 0.41 → 0.41 → 0.39 | no | DOWN @ 0.60 | -0.24 / -0.44 / · |
| 10-03 17:17:51 | SOL | up | 0.55→0.62 | 0.51 → 0.51 → 0.58 | 4.75s | UP @ 0.51 | 0.34 / 1.26 / · |
| 10-03 17:17:51 | DOGE | down | 0.38→0.33 | 0.38 → 0.38 → 0.38 | no | — |  |
| 10-03 17:17:47 | BNB | down | 0.60→0.48 | 0.54 → 0.54 → 0.54 | 24.00s | — |  |
| 10-03 17:17:36 | ETH | up | 0.34→0.42 | 0.40 → 0.40 → 0.43 | 19.26s | — |  |
| 10-03 17:17:36 | SOL | up | 0.47→0.62 | 0.53 → 0.53 → 0.51 | no | UP @ 0.53 | -0.66 / 0.14 / · |
| 10-03 17:17:35 | XRP | up | 0.31→0.37 | 0.40 → 0.40 → 0.40 | no | — |  |
| 10-03 17:17:32 | BNB | down | 0.56→0.51 | 0.51 → 0.51 → 0.51 | no | — |  |
| 10-03 17:17:28 | NEAR | down | 0.32→0.26 | 0.40 → 0.38 → 0.38 | 13.01s | DOWN @ 0.64 | -0.64 / 1.00 / · |
| 10-03 17:17:22 | HYPE | down | 0.38→0.31 | 0.39 → 0.39 → 0.36 | 18.26s | DOWN @ 0.63 | -0.34 / 0.17 / · |
| 10-03 17:17:11 | XRP | down | 0.55→0.46 | 0.61 → 0.49 → 0.49 | 0.50s | DOWN @ 0.51 | -0.46 / 0.45 / · |
