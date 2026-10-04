# Lag Tracker

*Updated Sun Oct 04 03:24 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 466 | 10.7s | 4% | 0% |
| BTC | 379 | 12.0s | 2% | 0% |
| DOGE | 498 | 10.8s | 2% | 0% |
| ETH | 485 | 10.9s | 3% | 0% |
| HYPE | 392 | 11.6s | 4% | 0% |
| NEAR | 424 | 10.8s | 4% | 0% |
| SOL | 944 | 10.6s | 3% | 0% |
| XRP | 867 | 11.0s | 3% | 0% |
| ZEC | 553 | 9.7s | 4% | 0% |
| **All** | **5008** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2635 | 732 | $-310.82 | -2.7% | $-129.50 / $-181.32 |
| Sell after 30 sec | 2630 | 1523 | $818.50 | +7.2% | $488.76 / $329.74 |
| Hold to the close | 2590 | 1285 | $1627.22 | +14.5% | $982.53 / $644.69 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **38 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 03:24:05 | DOGE | down | 0.59→0.44 | 0.57 → 0.57 → 0.57 | no | DOWN @ 0.43 | -0.75 / · / · |
| 10-04 03:23:58 | NEAR | down | 0.59→0.54 | 0.71 → 0.71 → 0.71 | 13.34s | DOWN @ 0.29 | -0.40 / · / · |
| 10-04 03:23:53 | SOL | up | 0.57→0.64 | 0.72 → 0.72 → 0.75 | no | — |  |
| 10-04 03:23:53 | ETH | up | 0.69→0.77 | 0.58 → 0.58 → 0.62 | 18.60s | UP @ 0.59 | -0.14 / · / · |
| 10-04 03:23:51 | ZEC | up | 0.28→0.38 | 0.29 → 0.29 → 0.29 | 6.31s | UP @ 0.32 | 1.26 / · / · |
| 10-04 03:23:50 | XRP | down | 0.16→0.10 | 0.20 → 0.20 → 0.20 | 21.60s | DOWN @ 0.82 | -0.43 / · / · |
| 10-04 03:23:50 | DOGE | down | 0.44→0.39 | 0.43 → 0.43 → 0.43 | no | — |  |
| 10-04 03:23:38 | SOL | up | 0.53→0.60 | 0.79 → 0.79 → 0.72 | no | — |  |
| 10-04 03:23:32 | XRP | down | 0.17→0.11 | 0.23 → 0.23 → 0.23 | 9.81s | DOWN @ 0.77 | -0.16 / 0.05 / · |
| 10-04 03:23:31 | HYPE | down | 0.65→0.53 | 0.69 → 0.69 → 0.69 | no | DOWN @ 0.33 | -0.61 / -0.51 / · |
| 10-04 03:23:23 | SOL | down | 0.73→0.67 | 0.81 → 0.81 → 0.79 | 19.07s | DOWN @ 0.19 | -0.13 / 0.45 / · |
| 10-04 03:23:12 | XRP | down | 0.21→0.10 | 0.26 → 0.23 → 0.23 | 30.32s | DOWN @ 0.77 | -0.36 / -0.36 / · |
| 10-04 03:23:06 | NEAR | down | 0.61→0.53 | 0.67 → 0.67 → 0.67 | no | DOWN @ 0.34 | -0.42 / -1.49 / · |
| 10-04 03:22:55 | DOGE | down | 0.46→0.40 | 0.53 → 0.53 → 0.55 | no | DOWN @ 0.48 | -0.66 / -0.76 / · |
| 10-04 03:22:42 | SOL | up | 0.56→0.62 | 0.55 → 0.72 → 0.72 | 0.32s | — |  |
| 10-04 03:22:40 | NEAR | up | 0.45→0.50 | 0.65 → 0.65 → 0.61 | no | — |  |
| 10-04 03:22:40 | BTC | up | 0.66→0.74 | 0.62 → 0.62 → 0.77 | 1.58s | UP @ 0.63 | 1.00 / 1.00 / · |
| 10-04 03:22:40 | DOGE | up | 0.31→0.44 | 0.46 → 0.46 → 0.53 | 1.58s | — |  |
| 10-04 03:22:29 | HYPE | down | 0.63→0.58 | 0.68 → 0.68 → 0.68 | 13.08s | DOWN @ 0.34 | -0.71 / -0.03 / · |
| 10-04 03:22:29 | XRP | up | 0.07→0.13 | 0.23 → 0.20 → 0.20 | no | — |  |
| 10-04 03:22:26 | SOL | up | 0.42→0.52 | 0.54 → 0.54 → 0.55 | 15.58s | — |  |
| 10-04 03:22:24 | NEAR | down | 0.49→0.44 | 0.68 → 0.68 → 0.65 | 3.33s | DOWN @ 0.34 | -0.32 / -0.03 / · |
| 10-04 03:22:07 | ETH | up | 0.67→0.73 | 0.58 → 0.58 → 0.66 | 4.84s | UP @ 0.59 | 0.27 / 0.16 / · |
| 10-04 03:22:04 | NEAR | up | 0.44→0.55 | 0.59 → 0.59 → 0.59 | 7.59s | — |  |
| 10-04 03:22:00 | SOL | up | 0.33→0.46 | 0.45 → 0.45 → 0.45 | 11.59s | — |  |
| 10-04 03:21:49 | NEAR | up | 0.38→0.43 | 0.51 → 0.51 → 0.51 | 8.09s | — |  |
| 10-04 03:21:47 | DOGE | down | 0.28→0.22 | 0.33 → 0.33 → 0.33 | no | DOWN @ 0.68 | -0.42 / -0.73 / · |
| 10-04 03:21:32 | ZEC | up | 0.26→0.33 | 0.21 → 0.21 → 0.21 | 10.09s | UP @ 0.22 | -0.35 / 0.42 / · |
| 10-04 03:21:31 | ETH | up | 0.36→0.61 | 0.30 → 0.30 → 0.30 | 10.85s | UP @ 0.31 | -0.40 / 2.37 / · |
| 10-04 03:21:30 | SOL | up | 0.18→0.33 | 0.21 → 0.21 → 0.21 | 11.60s | UP @ 0.22 | -0.35 / 1.89 / · |
