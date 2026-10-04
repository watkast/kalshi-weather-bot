# Lag Tracker

*Updated Sun Oct 04 03:34 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 469 | 10.7s | 4% | 0% |
| BTC | 384 | 12.0s | 2% | 0% |
| DOGE | 506 | 10.9s | 2% | 0% |
| ETH | 492 | 11.0s | 3% | 0% |
| HYPE | 396 | 11.6s | 4% | 0% |
| NEAR | 437 | 10.8s | 4% | 0% |
| SOL | 961 | 10.6s | 3% | 0% |
| XRP | 877 | 11.0s | 4% | 0% |
| ZEC | 563 | 9.7s | 4% | 0% |
| **All** | **5085** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2665 | 738 | $-321.59 | -2.8% | $-131.35 / $-190.24 |
| Sell after 30 sec | 2662 | 1538 | $812.41 | +7.0% | $492.53 / $319.88 |
| Hold to the close | 2649 | 1318 | $1675.44 | +14.6% | $942.34 / $733.10 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **38 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 03:34:10 | SOL | down | 0.94→0.89 | 0.88 → 0.88 → 0.91 | no | — |  |
| 10-04 03:34:06 | ETH | up | 0.71→0.79 | 0.72 → 0.72 → 0.72 | 6.81s | UP @ 0.73 | 0.23 / · / · |
| 10-04 03:34:05 | BTC | up | 0.82→0.87 | 0.80 → 0.80 → 0.80 | no | UP @ 0.80 | -0.13 / · / · |
| 10-04 03:34:05 | XRP | up | 0.67→0.76 | 0.74 → 0.74 → 0.74 | 7.81s | — |  |
| 10-04 03:34:01 | NEAR | up | 0.48→0.55 | 0.57 → 0.57 → 0.57 | 11.56s | — |  |
| 10-04 03:34:00 | ZEC | up | 0.51→0.57 | 0.52 → 0.54 → 0.54 | 13.06s | — |  |
| 10-04 03:33:48 | BTC | up | 0.74→0.82 | 0.72 → 0.72 → 0.72 | 9.56s | UP @ 0.73 | 0.34 / · / · |
| 10-04 03:33:39 | DOGE | up | 0.60→0.70 | 0.78 → 0.78 → 0.78 | no | — |  |
| 10-04 03:33:36 | XRP | down | 0.70→0.64 | 0.81 → 0.81 → 0.81 | 6.81s | DOWN @ 0.19 | -0.03 / 0.35 / · |
| 10-04 03:33:31 | ZEC | up | 0.47→0.52 | 0.47 → 0.47 → 0.47 | 11.82s | — |  |
| 10-04 03:33:22 | HYPE | up | 0.42→0.52 | 0.43 → 0.43 → 0.43 | 20.82s | UP @ 0.44 | -0.56 / 0.64 / · |
| 10-04 03:33:21 | SOL | up | 0.81→0.86 | 0.79 → 0.79 → 0.79 | 7.07s | UP @ 0.80 | 0.18 / 0.29 / · |
| 10-04 03:33:20 | XRP | up | 0.57→0.64 | 0.69 → 0.69 → 0.69 | 7.32s | — |  |
| 10-04 03:33:07 | NEAR | down | 0.50→0.42 | 0.56 → 0.56 → 0.56 | no | DOWN @ 0.45 | -0.46 / -0.36 / · |
| 10-04 03:33:06 | SOL | up | 0.76→0.82 | 0.78 → 0.78 → 0.78 | 22.07s | — |  |
| 10-04 03:32:51 | NEAR | up | 0.46→0.53 | 0.51 → 0.51 → 0.51 | 6.32s | — |  |
| 10-04 03:32:51 | ETH | down | 0.68→0.63 | 0.64 → 0.64 → 0.64 | no | — |  |
| 10-04 03:32:48 | XRP | up | 0.53→0.60 | 0.68 → 0.68 → 0.68 | no | — |  |
| 10-04 03:32:46 | ZEC | up | 0.35→0.40 | 0.34 → 0.34 → 0.34 | 11.57s | UP @ 0.34 | -0.42 / 0.56 / · |
| 10-04 03:32:33 | XRP | down | 0.60→0.53 | 0.58 → 0.58 → 0.58 | no | — |  |
| 10-04 03:32:16 | XRP | down | 0.50→0.37 | 0.56 → 0.56 → 0.56 | no | DOWN @ 0.44 | -0.46 / -1.54 / · |
| 10-04 03:32:04 | NEAR | down | 0.48→0.42 | 0.57 → 0.57 → 0.57 | 8.60s | DOWN @ 0.45 | 0.04 / 0.34 / · |
| 10-04 03:32:01 | XRP | down | 0.50→0.43 | 0.56 → 0.56 → 0.56 | no | DOWN @ 0.44 | -0.46 / -0.65 / · |
| 10-04 03:32:00 | SOL | down | 0.76→0.71 | 0.78 → 0.78 → 0.78 | 12.10s | DOWN @ 0.23 | -0.45 / -0.45 / · |
| 10-04 03:31:56 | ZEC | down | 0.36→0.31 | 0.38 → 0.38 → 0.33 | 1.83s | — |  |
| 10-04 03:31:53 | ETH | up | 0.62→0.69 | 0.59 → 0.59 → 0.58 | 19.10s | UP @ 0.60 | -0.55 / -0.04 / · |
| 10-04 03:31:45 | XRP | down | 0.50→0.37 | 0.56 → 0.56 → 0.56 | no | DOWN @ 0.44 | -0.46 / -0.46 / · |
| 10-04 03:31:40 | NEAR | up | 0.37→0.47 | 0.45 → 0.45 → 0.57 | 2.09s | — |  |
| 10-04 03:31:33 | HYPE | down | 0.52→0.43 | 0.51 → 0.51 → 0.51 | 9.09s | DOWN @ 0.51 | 0.34 / 0.14 / · |
| 10-04 03:31:28 | XRP | up | 0.44→0.50 | 0.53 → 0.56 → 0.56 | 0.33s | — |  |
