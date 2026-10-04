# Lag Tracker

*Updated Sun Oct 04 05:54 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 557 | 10.9s | 3% | 0% |
| BTC | 433 | 11.9s | 3% | 0% |
| DOGE | 602 | 10.6s | 2% | 0% |
| ETH | 582 | 11.2s | 3% | 0% |
| HYPE | 482 | 11.6s | 4% | 0% |
| NEAR | 544 | 10.8s | 4% | 0% |
| SOL | 1075 | 10.6s | 3% | 0% |
| XRP | 1073 | 10.8s | 4% | 0% |
| ZEC | 701 | 9.7s | 4% | 0% |
| **All** | **6049** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3106 | 856 | $-392.81 | -2.9% | $-175.46 / $-217.35 |
| Sell after 30 sec | 3105 | 1774 | $913.96 | +6.8% | $530.32 / $383.64 |
| Hold to the close | 3079 | 1515 | $1816.74 | +13.6% | $977.51 / $839.23 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **14 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 05:54:37 | XRP | down | 0.17→0.10 | 0.23 → 0.23 → — | no | DOWN @ 0.78 | · / · / · |
| 10-04 05:54:11 | BTC | up | 0.61→0.71 | 0.55 → 0.66 → 0.66 | 0.02s | UP @ 0.66 | -0.42 / · / · |
| 10-04 05:53:58 | HYPE | up | 0.08→0.15 | 0.04 → 0.04 → 0.04 | no | — |  |
| 10-04 05:53:35 | BNB | down | 0.52→0.44 | 0.79 → 0.79 → 0.79 | no | DOWN @ 0.22 | -0.45 / -0.64 / · |
| 10-04 05:53:30 | XRP | down | 0.19→0.12 | 0.23 → 0.23 → 0.23 | no | DOWN @ 0.78 | -0.15 / -0.46 / · |
| 10-04 05:53:25 | BTC | up | 0.42→0.49 | 0.47 → 0.47 → 0.47 | 14.03s | — |  |
| 10-04 05:53:13 | ETH | down | 0.31→0.25 | 0.28 → 0.28 → 0.28 | 11.03s | — |  |
| 10-04 05:53:01 | XRP | down | 0.17→0.11 | 0.26 → 0.26 → 0.26 | 23.04s | DOWN @ 0.75 | -0.38 / -0.07 / · |
| 10-04 05:52:56 | ETH | down | 0.27→0.21 | 0.23 → 0.20 → 0.20 | no | — |  |
| 10-04 05:52:43 | BTC | up | 0.29→0.40 | 0.39 → 0.39 → 0.39 | no | — |  |
| 10-04 05:52:41 | ETH | up | 0.20→0.29 | 0.24 → 0.23 → 0.23 | no | UP @ 0.23 | -0.36 / 0.22 / · |
| 10-04 05:52:26 | BNB | up | 0.41→0.51 | 0.72 → 0.72 → 0.72 | 27.79s | — |  |
| 10-04 05:52:14 | ETH | up | 0.18→0.29 | 0.23 → 0.23 → 0.23 | no | UP @ 0.24 | -0.36 / -0.46 / · |
| 10-04 05:52:11 | BNB | up | 0.26→0.41 | 0.65 → 0.65 → 0.65 | 28.04s | — |  |
| 10-04 05:51:48 | BNB | down | 0.36→0.27 | 0.62 → 0.62 → 0.62 | no | DOWN @ 0.40 | -0.93 / -1.03 / · |
| 10-04 05:51:41 | XRP | down | 0.20→0.14 | 0.23 → 0.24 → 0.24 | no | — |  |
| 10-04 05:51:25 | XRP | up | 0.14→0.20 | 0.23 → 0.23 → 0.23 | no | — |  |
| 10-04 05:51:12 | ETH | down | 0.37→0.22 | 0.39 → 0.39 → 0.39 | 11.78s | DOWN @ 0.62 | -0.44 / 1.51 / · |
| 10-04 05:51:11 | HYPE | down | 0.26→0.20 | 0.14 → 0.14 → 0.14 | 13.28s | — |  |
| 10-04 05:50:57 | ETH | up | 0.30→0.35 | 0.29 → 0.29 → 0.29 | 11.78s | UP @ 0.30 | -0.40 / -1.27 / · |
| 10-04 05:50:34 | BNB | up | 0.33→0.38 | 0.52 → 0.52 → 0.52 | 20.03s | — |  |
| 10-04 05:50:33 | ETH | up | 0.30→0.38 | 0.30 → 0.30 → 0.30 | no | UP @ 0.31 | -0.60 / -0.50 / · |
| 10-04 05:50:32 | XRP | down | 0.25→0.18 | 0.28 → 0.28 → 0.28 | no | — |  |
| 10-04 05:50:26 | HYPE | down | 0.25→0.19 | 0.14 → 0.15 → 0.15 | no | — |  |
| 10-04 05:50:17 | XRP | up | 0.22→0.29 | 0.28 → 0.28 → 0.28 | no | — |  |
| 10-04 05:50:16 | BNB | up | 0.27→0.33 | 0.32 → 0.32 → 0.32 | 7.54s | — |  |
| 10-04 05:50:04 | BTC | up | 0.26→0.32 | 0.36 → 0.36 → 0.36 | 5.03s | — |  |
| 10-04 05:49:54 | ETH | up | 0.20→0.28 | 0.12 → 0.12 → 0.12 | 14.53s | UP @ 0.13 | -0.26 / 1.47 / · |
| 10-04 05:49:53 | XRP | up | 0.16→0.22 | 0.23 → 0.23 → 0.23 | 15.78s | — |  |
| 10-04 05:48:41 | ETH | down | 0.33→0.22 | 0.29 → 0.28 → 0.28 | 12.78s | DOWN @ 0.72 | -0.40 / 1.27 / · |
