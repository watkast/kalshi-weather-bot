# Lag Tracker

*Updated Sun Oct 04 04:04 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 491 | 10.7s | 4% | 0% |
| BTC | 395 | 12.0s | 2% | 0% |
| DOGE | 520 | 10.6s | 2% | 0% |
| ETH | 506 | 10.9s | 3% | 0% |
| HYPE | 411 | 11.6s | 4% | 0% |
| NEAR | 461 | 10.7s | 4% | 0% |
| SOL | 969 | 10.6s | 3% | 0% |
| XRP | 912 | 11.0s | 4% | 0% |
| ZEC | 600 | 9.6s | 4% | 0% |
| **All** | **5265** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2750 | 766 | $-329.96 | -2.8% | $-139.74 / $-190.22 |
| Sell after 30 sec | 2748 | 1587 | $830.15 | +7.0% | $503.25 / $326.90 |
| Hold to the close | 2739 | 1361 | $1713.01 | +14.4% | $951.65 / $761.36 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **37 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 04:04:13 | ZEC | up | 0.47→0.52 | 0.53 → 0.53 → 0.53 | no | UP @ 0.55 | -0.76 / · / · |
| 10-04 04:03:58 | ZEC | up | 0.40→0.52 | 0.47 → 0.47 → 0.47 | 10.80s | UP @ 0.47 | -0.46 / · / · |
| 10-04 04:03:53 | BNB | down | 0.62→0.53 | 0.69 → 0.69 → 0.74 | no | DOWN @ 0.33 | -1.10 / -1.19 / · |
| 10-04 04:03:52 | HYPE | up | 0.72→0.79 | 0.72 → 0.72 → 0.72 | 16.55s | UP @ 0.73 | -0.49 / 0.03 / · |
| 10-04 04:03:48 | DOGE | up | 0.51→0.60 | 0.60 → 0.60 → 0.60 | 5.30s | — |  |
| 10-04 04:03:45 | XRP | up | 0.73→0.81 | 0.79 → 0.79 → 0.79 | 23.30s | — |  |
| 10-04 04:03:45 | BTC | up | 0.46→0.52 | 0.53 → 0.53 → 0.53 | 23.80s | — |  |
| 10-04 04:03:45 | ETH | up | 0.69→0.74 | 0.71 → 0.71 → 0.71 | 8.80s | — |  |
| 10-04 04:03:44 | NEAR | up | 0.40→0.45 | 0.51 → 0.51 → 0.51 | 9.55s | — |  |
| 10-04 04:03:38 | ZEC | down | 0.46→0.41 | 0.45 → 0.45 → 0.43 | no | — |  |
| 10-04 04:03:38 | BNB | up | 0.47→0.54 | 0.69 → 0.69 → 0.69 | 15.55s | — |  |
| 10-04 04:03:34 | SOL | up | 0.45→0.51 | 0.40 → 0.40 → 0.48 | 4.55s | UP @ 0.41 | 0.25 / 1.66 / · |
| 10-04 04:03:26 | XRP | down | 0.73→0.68 | 0.79 → 0.79 → 0.79 | no | DOWN @ 0.22 | -0.45 / -0.54 / · |
| 10-04 04:03:23 | ZEC | up | 0.39→0.46 | 0.47 → 0.47 → 0.45 | no | — |  |
| 10-04 04:03:12 | HYPE | up | 0.68→0.75 | 0.71 → 0.71 → 0.71 | no | — |  |
| 10-04 04:03:02 | XRP | up | 0.67→0.72 | 0.69 → 0.69 → 0.69 | 6.56s | — |  |
| 10-04 04:02:59 | DOGE | up | 0.45→0.51 | 0.56 → 0.56 → 0.56 | no | — |  |
| 10-04 04:02:47 | XRP | up | 0.59→0.67 | 0.65 → 0.65 → 0.65 | 6.56s | — |  |
| 10-04 04:02:34 | SOL | down | 0.49→0.43 | 0.38 → 0.38 → 0.39 | no | — |  |
| 10-04 04:02:32 | XRP | down | 0.72→0.64 | 0.64 → 0.64 → 0.64 | no | — |  |
| 10-04 04:02:24 | HYPE | up | 0.68→0.74 | 0.72 → 0.68 → 0.68 | no | UP @ 0.69 | -0.51 / -0.41 / · |
| 10-04 04:02:17 | ZEC | up | 0.39→0.44 | 0.42 → 0.42 → 0.42 | 6.57s | — |  |
| 10-04 04:02:17 | XRP | up | 0.50→0.72 | 0.59 → 0.59 → 0.59 | no | UP @ 0.60 | -0.14 / 0.06 / · |
| 10-04 04:01:40 | DOGE | up | 0.48→0.67 | 0.53 → 0.53 → 0.53 | no | UP @ 0.53 | -0.46 / -0.46 / · |
| 10-04 04:01:33 | ETH | up | 0.55→0.63 | 0.56 → 0.56 → 0.64 | 4.58s | UP @ 0.57 | 0.25 / 0.25 / · |
| 10-04 04:01:30 | NEAR | up | 0.38→0.43 | 0.53 → 0.53 → 0.53 | no | — |  |
| 10-04 04:00:51 | NEAR | down | 0.48→0.38 | 0.69 → 0.69 → 0.56 | 2.34s | DOWN @ 0.32 | 0.76 / 1.26 / · |
| 10-04 04:00:47 | HYPE | down | 0.70→0.63 | 0.68 → 0.68 → 0.68 | no | — |  |
| 10-04 03:57:59 | BNB | up | 0.22→0.30 | 0.76 → 0.76 → 0.76 | 17.63s | — |  |
| 10-04 03:57:45 | XRP | down | 0.16→0.08 | 0.11 → 0.11 → 0.05 | 1.88s | — |  |
