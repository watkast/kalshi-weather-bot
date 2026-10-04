# Lag Tracker

*Updated Sun Oct 04 06:24 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 578 | 10.8s | 3% | 0% |
| BTC | 450 | 12.0s | 2% | 0% |
| DOGE | 626 | 10.4s | 2% | 0% |
| ETH | 605 | 11.2s | 3% | 0% |
| HYPE | 498 | 11.6s | 3% | 0% |
| NEAR | 558 | 10.8s | 4% | 0% |
| SOL | 1121 | 10.8s | 3% | 0% |
| XRP | 1114 | 10.8s | 3% | 0% |
| ZEC | 718 | 9.8s | 4% | 0% |
| **All** | **6268** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3213 | 889 | $-395.28 | -2.8% | $-169.38 / $-225.90 |
| Sell after 30 sec | 3211 | 1839 | $954.57 | +6.8% | $538.05 / $416.52 |
| Hold to the close | 3176 | 1573 | $1894.99 | +13.7% | $1025.21 / $869.78 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **16 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 06:24:28 | NEAR | down | 0.56→0.49 | 0.69 → 0.69 → 0.69 | 10.34s | DOWN @ 0.32 | -0.61 / · / · |
| 10-04 06:24:19 | DOGE | down | 0.70→0.62 | 0.79 → 0.79 → 0.75 | 4.61s | DOWN @ 0.22 | -0.06 / · / · |
| 10-04 06:24:17 | ZEC | down | 0.48→0.43 | 0.65 → 0.65 → 0.65 | 6.61s | DOWN @ 0.37 | 1.05 / 1.25 / · |
| 10-04 06:24:17 | SOL | up | 0.15→0.20 | 0.32 → 0.32 → 0.32 | no | — |  |
| 10-04 06:23:58 | ETH | down | 0.32→0.19 | 0.39 → 0.39 → 0.39 | 10.87s | DOWN @ 0.62 | -0.44 / 1.62 / · |
| 10-04 06:23:57 | SOL | down | 0.30→0.18 | 0.43 → 0.43 → 0.43 | 11.37s | DOWN @ 0.57 | -0.46 / 0.56 / · |
| 10-04 06:23:47 | HYPE | up | 0.72→0.85 | 0.66 → 0.66 → 0.66 | 6.62s | UP @ 0.67 | 1.13 / 0.61 / · |
| 10-04 06:23:41 | ETH | up | 0.22→0.35 | 0.32 → 0.32 → 0.32 | 12.62s | — |  |
| 10-04 06:23:38 | ZEC | up | 0.50→0.57 | 0.42 → 0.49 → 0.49 | 0.37s | UP @ 0.51 | -0.76 / 0.75 / · |
| 10-04 06:23:37 | SOL | down | 0.35→0.27 | 0.46 → 0.46 → 0.43 | no | DOWN @ 0.55 | -0.26 / -0.26 / · |
| 10-04 06:23:32 | HYPE | down | 0.67→0.49 | 0.66 → 0.66 → 0.66 | no | DOWN @ 0.35 | -0.52 / -1.97 / · |
| 10-04 06:23:24 | DOGE | up | 0.71→0.82 | 0.73 → 0.78 → 0.78 | 29.88s | — |  |
| 10-04 06:23:24 | ETH | up | 0.22→0.31 | 0.46 → 0.28 → 0.28 | no | — |  |
| 10-04 06:23:23 | ZEC | up | 0.45→0.52 | 0.46 → 0.42 → 0.42 | 30.38s | UP @ 0.44 | -0.75 / -0.06 / · |
| 10-04 06:23:20 | SOL | down | 0.35→0.28 | 0.49 → 0.49 → 0.46 | 3.87s | DOWN @ 0.51 | -0.06 / 0.14 / · |
| 10-04 06:23:08 | DOGE | up | 0.76→0.81 | 0.81 → 0.81 → 0.73 | no | — |  |
| 10-04 06:23:05 | SOL | up | 0.26→0.35 | 0.56 → 0.56 → 0.49 | no | — |  |
| 10-04 06:23:04 | ETH | up | 0.37→0.47 | 0.52 → 0.52 → 0.46 | no | — |  |
| 10-04 06:23:02 | ZEC | up | 0.36→0.42 | 0.40 → 0.40 → 0.40 | 6.63s | — |  |
| 10-04 06:22:53 | DOGE | down | 0.92→0.85 | 0.90 → 0.90 → 0.81 | 0.63s | — |  |
| 10-04 06:22:49 | SOL | down | 0.55→0.47 | 0.74 → 0.74 → 0.56 | 4.38s | DOWN @ 0.27 | 1.38 / 1.98 / · |
| 10-04 06:22:49 | ETH | up | 0.32→0.53 | 0.84 → 0.84 → 0.52 | no | — |  |
| 10-04 06:22:47 | HYPE | down | 0.78→0.63 | 0.82 → 0.82 → 0.82 | 21.88s | DOWN @ 0.18 | 0.16 / 1.13 / · |
| 10-04 06:22:34 | ZEC | down | 0.50→0.43 | 0.74 → 0.74 → 0.46 | 4.63s | DOWN @ 0.27 | 2.38 / 2.99 / · |
| 10-04 06:22:34 | SOL | down | 0.78→0.63 | 0.73 → 0.73 → 0.74 | 19.89s | DOWN @ 0.27 | -0.48 / 1.38 / · |
| 10-04 06:22:34 | ETH | down | 0.97→0.92 | 0.80 → 0.80 → 0.84 | 19.89s | — |  |
| 10-04 06:22:31 | NEAR | down | 0.57→0.45 | 0.83 → 0.83 → 0.83 | 7.63s | DOWN @ 0.17 | 2.32 / 2.72 / · |
| 10-04 06:22:27 | HYPE | down | 0.91→0.86 | 0.95 → 0.95 → 0.95 | 11.39s | DOWN @ 0.05 | -0.20 / 1.49 / · |
| 10-04 06:22:17 | DOGE | down | 1.00→0.91 | 0.95 → 0.95 → 0.95 | 6.89s | DOWN @ 0.05 | 0.46 / 0.36 / · |
| 10-04 06:22:16 | SOL | down | 0.99→0.67 | 0.92 → 0.92 → 0.92 | 7.64s | DOWN @ 0.09 | 1.51 / 1.41 / · |
