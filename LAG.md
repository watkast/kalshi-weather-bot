# Lag Tracker

*Updated Sun Oct 04 05:44 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 548 | 10.8s | 3% | 0% |
| BTC | 426 | 11.9s | 2% | 0% |
| DOGE | 600 | 10.7s | 2% | 0% |
| ETH | 569 | 11.1s | 3% | 0% |
| HYPE | 476 | 11.6s | 3% | 0% |
| NEAR | 544 | 10.8s | 4% | 0% |
| SOL | 1072 | 10.6s | 3% | 0% |
| XRP | 1059 | 10.8s | 4% | 0% |
| ZEC | 701 | 9.7s | 4% | 0% |
| **All** | **5995** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3079 | 853 | $-384.73 | -2.9% | $-173.61 / $-211.12 |
| Sell after 30 sec | 3079 | 1763 | $910.35 | +6.8% | $529.19 / $381.16 |
| Hold to the close | 3036 | 1491 | $1782.14 | +13.6% | $961.44 / $820.70 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **31 ms** · Coinbase price delay: **13 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 05:43:31 | BNB | up | 0.30→0.59 | 1.00 → 1.00 → 1.00 | no | — |  |
| 10-04 05:43:15 | BNB | down | 0.69→0.34 | 0.99 → 0.99 → 0.99 | no | — |  |
| 10-04 05:42:46 | ETH | down | 0.98→0.90 | 0.81 → 0.81 → 0.81 | no | — |  |
| 10-04 05:42:28 | ETH | down | 0.90→0.73 | 0.76 → 0.76 → 0.76 | no | — |  |
| 10-04 05:42:21 | BNB | down | 0.27→0.09 | 0.91 → 0.91 → 0.84 | no | — |  |
| 10-04 05:42:11 | ETH | down | 0.95→0.88 | 0.67 → 0.67 → 0.67 | no | — |  |
| 10-04 05:41:35 | BNB | up | 0.22→0.29 | 0.79 → 0.79 → 0.87 | 2.03s | — |  |
| 10-04 05:41:24 | DOGE | up | 0.89→0.96 | 0.94 → 0.98 → 0.98 | 0.14s | — |  |
| 10-04 05:41:11 | HYPE | up | 0.91→0.97 | 0.99 → 0.99 → 0.99 | no | — |  |
| 10-04 05:41:03 | ETH | up | 0.52→0.70 | 0.38 → 0.38 → 0.38 | 18.53s | UP @ 0.40 | -0.64 / 3.82 / · |
| 10-04 05:40:55 | DOGE | up | 0.81→0.88 | 0.94 → 0.94 → 0.94 | no | — |  |
| 10-04 05:40:31 | DOGE | up | 0.84→0.95 | 0.95 → 0.95 → 0.95 | no | — |  |
| 10-04 05:40:24 | BNB | down | 0.30→0.16 | 0.47 → 0.47 → 0.47 | no | — |  |
| 10-04 05:40:05 | ETH | up | 0.35→0.53 | 0.36 → 0.36 → 0.38 | no | UP @ 0.37 | -0.34 / -0.34 / · |
| 10-04 05:39:56 | BNB | down | 0.18→0.03 | 0.41 → 0.41 → 0.41 | no | DOWN @ 0.59 | -0.45 / -1.25 / · |
| 10-04 05:39:55 | XRP | down | 0.95→0.88 | 0.89 → 0.89 → 0.89 | no | — |  |
| 10-04 05:39:48 | HYPE | up | 0.77→0.82 | 0.92 → 0.92 → 0.91 | 19.03s | — |  |
| 10-04 05:39:40 | ETH | down | 0.71→0.41 | 0.56 → 0.56 → 0.56 | 11.79s | DOWN @ 0.46 | -0.66 / 1.25 / · |
| 10-04 05:39:37 | XRP | down | 0.98→0.88 | 0.84 → 0.92 → 0.92 | no | DOWN @ 0.09 | -0.13 / 0.12 / · |
| 10-04 05:39:12 | XRP | down | 0.94→0.87 | 0.91 → 0.91 → 0.91 | 10.03s | DOWN @ 0.09 | -0.13 / -0.19 / · |
| 10-04 05:39:07 | NEAR | up | 0.89→0.95 | 0.95 → 0.95 → 0.95 | no | — |  |
| 10-04 05:39:02 | DOGE | down | 0.85→0.67 | 0.84 → 0.84 → 0.89 | no | DOWN @ 0.16 | -0.67 / -0.39 / · |
| 10-04 05:38:55 | ETH | down | 0.69→0.63 | 0.59 → 0.59 → 0.59 | 11.78s | — |  |
| 10-04 05:38:36 | ETH | up | 0.60→0.67 | 0.54 → 0.54 → 0.56 | 15.53s | UP @ 0.54 | -0.16 / 0.15 / · |
| 10-04 05:38:19 | XRP | up | 0.85→0.90 | 0.85 → 0.85 → 0.85 | 17.12s | UP @ 0.86 | -0.28 / 0.26 / · |
| 10-04 05:38:12 | NEAR | up | 0.79→0.84 | 0.89 → 0.89 → 0.89 | 9.28s | — |  |
| 10-04 05:38:07 | ETH | up | 0.49→0.60 | 0.53 → 0.53 → 0.53 | no | UP @ 0.53 | -0.46 / -0.06 / · |
| 10-04 05:38:03 | DOGE | down | 0.51→0.43 | 0.61 → 0.61 → 0.61 | no | DOWN @ 0.40 | -0.54 / -2.48 / · |
| 10-04 05:38:01 | XRP | up | 0.76→0.84 | 0.81 → 0.81 → 0.81 | 5.78s | — |  |
| 10-04 05:38:00 | SOL | up | 0.77→0.85 | 0.88 → 0.88 → 0.88 | 21.28s | — |  |
