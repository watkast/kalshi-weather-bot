# Lag Tracker

*Updated Sun Oct 04 08:35 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 629 | 11.2s | 3% | 0% |
| BTC | 511 | 11.9s | 3% | 0% |
| DOGE | 698 | 10.5s | 2% | 0% |
| ETH | 680 | 11.2s | 3% | 0% |
| HYPE | 578 | 11.2s | 4% | 0% |
| NEAR | 672 | 10.8s | 4% | 0% |
| SOL | 1245 | 10.8s | 3% | 0% |
| XRP | 1250 | 10.9s | 3% | 0% |
| ZEC | 840 | 9.6s | 4% | 0% |
| **All** | **7103** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3651 | 1028 | $-416.32 | -2.6% | $-196.05 / $-220.27 |
| Sell after 30 sec | 3649 | 2125 | $1184.19 | +7.5% | $591.79 / $592.40 |
| Hold to the close | 3633 | 1798 | $2330.58 | +14.9% | $1497.98 / $832.60 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **31 ms** · Coinbase price delay: **15 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 08:35:07 | SOL | down | 0.33→0.27 | 0.35 → 0.35 → 0.35 | no | DOWN @ 0.65 | -0.43 / · / · |
| 10-04 08:35:07 | ETH | down | 0.33→0.27 | 0.27 → 0.27 → 0.27 | 5.13s | — |  |
| 10-04 08:35:07 | BTC | down | 0.12→0.05 | 0.10 → 0.10 → 0.10 | no | DOWN @ 0.90 | -0.14 / · / · |
| 10-04 08:34:37 | ETH | up | 0.26→0.33 | 0.19 → 0.19 → 0.19 | 20.15s | UP @ 0.20 | -0.14 / 0.34 / · |
| 10-04 08:34:37 | SOL | up | 0.26→0.33 | 0.24 → 0.24 → 0.24 | 5.14s | UP @ 0.25 | 0.79 / 0.70 / · |
| 10-04 08:34:36 | HYPE | up | 0.72→0.84 | 0.71 → 0.71 → 0.71 | 6.14s | UP @ 0.72 | 0.64 / 0.74 / · |
| 10-04 08:34:34 | NEAR | up | 0.10→0.15 | 0.07 → 0.07 → 0.07 | 7.64s | UP @ 0.07 | 0.11 / 1.54 / · |
| 10-04 08:34:23 | XRP | down | 0.34→0.29 | 0.28 → 0.28 → 0.32 | no | — |  |
| 10-04 08:34:04 | HYPE | up | 0.63→0.70 | 0.70 → 0.70 → 0.70 | no | — |  |
| 10-04 08:34:03 | ZEC | down | 0.38→0.31 | 0.28 → 0.28 → 0.28 | 23.66s | — |  |
| 10-04 08:33:54 | XRP | down | 0.29→0.24 | 0.23 → 0.23 → 0.28 | no | — |  |
| 10-04 08:33:48 | ZEC | up | 0.30→0.38 | 0.28 → 0.28 → 0.28 | 23.66s | UP @ 0.29 | -0.40 / -0.01 / · |
| 10-04 08:33:41 | SOL | up | 0.17→0.22 | 0.29 → 0.29 → 0.18 | no | — |  |
| 10-04 08:33:40 | BNB | up | 0.22→0.30 | 0.47 → 0.47 → 0.39 | no | — |  |
| 10-04 08:33:34 | BTC | down | 0.13→0.07 | 0.15 → 0.15 → 0.15 | 7.66s | DOWN @ 0.85 | 0.46 / 0.47 / · |
| 10-04 08:33:30 | ETH | down | 0.31→0.25 | 0.23 → 0.23 → 0.23 | 11.66s | — |  |
| 10-04 08:33:30 | XRP | down | 0.37→0.28 | 0.45 → 0.45 → 0.45 | 11.66s | DOWN @ 0.56 | -0.46 / 1.27 / · |
| 10-04 08:33:28 | DOGE | down | 0.19→0.12 | 0.14 → 0.13 → 0.13 | 13.91s | — |  |
| 10-04 08:33:24 | SOL | down | 0.33→0.28 | 0.33 → 0.33 → 0.29 | 3.19s | — |  |
| 10-04 08:33:08 | HYPE | up | 0.52→0.61 | 0.54 → 0.54 → 0.57 | 18.44s | — |  |
| 10-04 08:32:42 | HYPE | down | 0.60→0.52 | 0.62 → 0.62 → 0.62 | 14.42s | DOWN @ 0.38 | -0.44 / 0.05 / · |
| 10-04 08:32:31 | XRP | up | 0.43→0.48 | 0.38 → 0.38 → 0.38 | 11.18s | UP @ 0.38 | -0.44 / 0.75 / · |
| 10-04 08:32:26 | HYPE | up | 0.50→0.58 | 0.46 → 0.46 → 0.56 | 0.92s | UP @ 0.47 | 0.44 / 1.15 / · |
| 10-04 08:32:15 | ZEC | up | 0.19→0.24 | 0.17 → 0.17 → 0.17 | 27.18s | UP @ 0.19 | -0.51 / 0.06 / · |
| 10-04 08:31:33 | HYPE | up | 0.41→0.52 | 0.43 → 0.43 → 0.43 | 8.94s | UP @ 0.44 | 0.04 / -0.06 / · |
| 10-04 08:31:13 | DOGE | down | 0.30→0.21 | 0.30 → 0.28 → 0.28 | 13.22s | DOWN @ 0.72 | -0.40 / 1.06 / · |
| 10-04 08:31:13 | SOL | down | 0.43→0.31 | 0.40 → 0.40 → 0.40 | 13.22s | DOWN @ 0.61 | -0.44 / 1.09 / · |
| 10-04 08:31:13 | BTC | down | 0.25→0.18 | 0.15 → 0.15 → 0.15 | no | — |  |
| 10-04 08:31:04 | XRP | up | 0.37→0.43 | 0.35 → 0.35 → 0.35 | 6.94s | UP @ 0.36 | -0.04 / -1.21 / · |
| 10-04 08:30:44 | SOL | down | 0.50→0.43 | 0.48 → 0.48 → 0.48 | 11.45s | — |  |
