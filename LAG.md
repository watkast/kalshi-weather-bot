# Lag Tracker

*Updated Sat Oct 03 18:22 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 75 | 10.9s | 4% | 0% |
| BTC | 66 | 10.7s | 5% | 0% |
| DOGE | 69 | 9.7s | 4% | 0% |
| ETH | 59 | 11.3s | 3% | 0% |
| HYPE | 47 | 11.5s | 2% | 0% |
| NEAR | 48 | 9.9s | 6% | 0% |
| SOL | 114 | 7.6s | 6% | 0% |
| XRP | 109 | 8.4s | 8% | 0% |
| ZEC | 92 | 9.1s | 5% | 0% |
| **All** | **679** | **9.3s** | **5%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 357 | 129 | $-9.13 | -0.6% | $-7.12 / $-2.01 |
| Sell after 30 sec | 357 | 245 | $200.95 | +13.6% | $95.55 / $105.40 |
| Hold to the close | 336 | 176 | $385.16 | +28.0% | $146.86 / $238.30 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **29 ms** · Coinbase price delay: **34 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 18:21:46 | BNB | down | 0.45→0.39 | 0.45 → 0.45 → 0.45 | 10.83s | — |  |
| 10-03 18:21:19 | DOGE | up | 0.12→0.18 | 0.17 → 0.17 → 0.17 | no | — |  |
| 10-03 18:21:17 | BNB | up | 0.40→0.45 | 0.46 → 0.46 → 0.46 | no | — |  |
| 10-03 18:21:14 | XRP | down | 0.36→0.30 | 0.32 → 0.32 → 0.32 | no | — |  |
| 10-03 18:21:10 | BTC | up | 0.23→0.33 | 0.20 → 0.20 → 0.18 | 16.84s | UP @ 0.20 | -0.43 / 0.34 / · |
| 10-03 18:20:26 | SOL | down | 0.29→0.23 | 0.30 → 0.30 → 0.28 | 1.10s | DOWN @ 0.70 | -0.10 / 0.42 / · |
| 10-03 18:20:18 | BNB | up | 0.39→0.44 | 0.37 → 0.37 → 0.37 | 23.35s | UP @ 0.38 | -0.63 / 0.25 / · |
| 10-03 18:20:16 | NEAR | down | 0.15→0.10 | 0.20 → 0.20 → 0.20 | 10.85s | — |  |
| 10-03 18:20:01 | NEAR | up | 0.09→0.15 | 0.15 → 0.15 → 0.15 | 10.85s | — |  |
| 10-03 18:19:46 | XRP | up | 0.30→0.35 | 0.30 → 0.30 → 0.30 | no | — |  |
| 10-03 18:19:42 | ETH | up | 0.39→0.48 | 0.36 → 0.35 → 0.35 | 14.86s | UP @ 0.36 | -0.43 / 0.65 / · |
| 10-03 18:19:31 | XRP | down | 0.33→0.27 | 0.32 → 0.32 → 0.32 | no | — |  |
| 10-03 18:19:16 | BTC | down | 0.33→0.20 | 0.28 → 0.28 → 0.28 | no | DOWN @ 0.72 | -0.40 / 0.12 / · |
| 10-03 18:19:02 | DOGE | down | 0.21→0.15 | 0.23 → 0.23 → 0.23 | 9.87s | DOWN @ 0.78 | -0.05 / 0.06 / · |
| 10-03 18:18:56 | ETH | up | 0.33→0.38 | 0.34 → 0.34 → 0.29 | 30.87s | — |  |
| 10-03 18:18:50 | BNB | down | 0.45→0.39 | 0.43 → 0.43 → 0.43 | 6.62s | — |  |
| 10-03 18:18:48 | NEAR | down | 0.21→0.16 | 0.18 → 0.18 → 0.18 | 24.12s | — |  |
| 10-03 18:18:48 | ZEC | down | 0.30→0.18 | 0.21 → 0.21 → 0.21 | 9.12s | — |  |
| 10-03 18:18:37 | XRP | up | 0.37→0.43 | 0.36 → 0.36 → 0.41 | 4.87s | — |  |
| 10-03 18:18:35 | SOL | up | 0.29→0.34 | 0.24 → 0.24 → 0.24 | 6.37s | UP @ 0.25 | 0.21 / -0.57 / · |
| 10-03 18:18:21 | BNB | down | 0.43→0.38 | 0.43 → 0.43 → 0.43 | 6.12s | — |  |
| 10-03 18:18:12 | ZEC | down | 0.34→0.28 | 0.26 → 0.26 → 0.26 | 15.13s | — |  |
| 10-03 18:18:08 | XRP | down | 0.43→0.38 | 0.39 → 0.39 → 0.34 | 4.13s | — |  |
| 10-03 18:18:06 | SOL | down | 0.34→0.26 | 0.32 → 0.32 → 0.32 | 20.38s | DOWN @ 0.69 | 0.00 / 0.31 / · |
| 10-03 18:18:06 | BNB | down | 0.49→0.43 | 0.53 → 0.53 → 0.53 | 6.13s | DOWN @ 0.48 | 0.34 / 0.75 / · |
| 10-03 18:17:35 | HYPE | down | 0.27→0.21 | 0.26 → 0.26 → 0.26 | 21.40s | — |  |
| 10-03 18:17:35 | BTC | down | 0.47→0.41 | 0.53 → 0.53 → 0.53 | 6.89s | DOWN @ 0.48 | 0.04 / 0.95 / · |
| 10-03 18:17:35 | XRP | down | 0.55→0.46 | 0.57 → 0.57 → 0.57 | 7.14s | DOWN @ 0.43 | 0.94 / 1.45 / · |
| 10-03 18:17:31 | SOL | down | 0.42→0.37 | 0.43 → 0.43 → 0.43 | 11.14s | DOWN @ 0.57 | -0.46 / 0.76 / · |
| 10-03 18:17:30 | ETH | down | 0.49→0.44 | 0.52 → 0.52 → 0.52 | 11.39s | DOWN @ 0.49 | -0.46 / 1.26 / · |
