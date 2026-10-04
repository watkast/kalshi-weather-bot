# Lag Tracker

*Updated Sun Oct 04 07:45 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 610 | 11.1s | 3% | 0% |
| BTC | 476 | 11.9s | 3% | 0% |
| DOGE | 659 | 10.3s | 2% | 0% |
| ETH | 648 | 11.2s | 3% | 0% |
| HYPE | 549 | 11.3s | 4% | 0% |
| NEAR | 625 | 10.8s | 3% | 0% |
| SOL | 1182 | 10.8s | 3% | 0% |
| XRP | 1174 | 10.8s | 3% | 0% |
| ZEC | 778 | 9.6s | 3% | 0% |
| **All** | **6701** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3430 | 959 | $-399.52 | -2.7% | $-184.83 / $-214.69 |
| Sell after 30 sec | 3430 | 1982 | $1078.00 | +7.3% | $559.78 / $518.22 |
| Hold to the close | 3375 | 1684 | $2233.79 | +15.3% | $1180.19 / $1053.60 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **14 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 07:43:21 | BTC | up | 0.10→0.18 | 0.14 → 0.14 → 0.14 | 24.79s | UP @ 0.14 | -0.46 / 2.53 / · |
| 10-04 07:43:07 | DOGE | down | 0.61→0.48 | 0.93 → 0.93 → 0.93 | 8.55s | DOWN @ 0.08 | 1.04 / 0.76 / · |
| 10-04 07:42:50 | SOL | down | 0.23→0.18 | 0.34 → 0.34 → 0.34 | 10.55s | DOWN @ 0.67 | -0.63 / 2.85 / · |
| 10-04 07:42:50 | XRP | down | 0.21→0.15 | 0.10 → 0.10 → 0.10 | 25.81s | — |  |
| 10-04 07:42:48 | DOGE | up | 0.66→0.77 | 0.91 → 0.91 → 0.91 | no | — |  |
| 10-04 07:42:34 | XRP | up | 0.19→0.29 | 0.14 → 0.14 → 0.14 | no | UP @ 0.15 | -0.28 / -0.79 / · |
| 10-04 07:42:27 | SOL | up | 0.16→0.25 | 0.10 → 0.10 → 0.21 | 4.30s | UP @ 0.11 | 0.81 / 1.97 / · |
| 10-04 07:42:19 | XRP | up | 0.16→0.24 | 0.10 → 0.10 → 0.10 | no | UP @ 0.11 | -0.24 / -0.28 / · |
| 10-04 07:42:14 | HYPE | up | 0.48→0.56 | 0.81 → 0.81 → 0.66 | no | — |  |
| 10-04 07:42:01 | SOL | up | 0.10→0.15 | 0.12 → 0.12 → 0.12 | 29.81s | — |  |
| 10-04 07:41:59 | HYPE | down | 0.80→0.49 | 0.81 → 0.81 → 0.81 | no | DOWN @ 0.22 | -0.73 / 0.62 / · |
| 10-04 07:41:53 | XRP | down | 0.18→0.12 | 0.14 → 0.14 → 0.14 | 7.56s | — |  |
| 10-04 07:41:40 | SOL | down | 0.17→0.11 | 0.13 → 0.13 → 0.13 | no | — |  |
| 10-04 07:41:35 | HYPE | down | 0.86→0.73 | 0.78 → 0.78 → 0.78 | no | — |  |
| 10-04 07:41:32 | BNB | up | 0.03→0.12 | 0.04 → 0.04 → 0.04 | 13.82s | UP @ 0.05 | -0.31 / 0.33 / · |
| 10-04 07:41:14 | SOL | down | 0.19→0.13 | 0.14 → 0.14 → 0.14 | no | — |  |
| 10-04 07:40:59 | ETH | up | 0.85→0.90 | 0.86 → 0.86 → 0.90 | 1.33s | — |  |
| 10-04 07:40:59 | SOL | down | 0.20→0.14 | 0.17 → 0.17 → 0.14 | 16.58s | — |  |
| 10-04 07:40:26 | SOL | up | 0.14→0.22 | 0.09 → 0.09 → 0.09 | 20.09s | UP @ 0.09 | -0.16 / 0.54 / · |
| 10-04 07:40:25 | XRP | up | 0.14→0.19 | 0.09 → 0.09 → 0.09 | 5.83s | UP @ 0.09 | 0.69 / 0.22 / · |
| 10-04 07:40:25 | BTC | up | 0.03→0.11 | 0.06 → 0.06 → 0.06 | 21.09s | UP @ 0.06 | -0.12 / 1.58 / · |
| 10-04 07:40:24 | ETH | up | 0.60→0.69 | 0.64 → 0.64 → 0.64 | 6.33s | UP @ 0.64 | 1.52 / 1.94 / · |
| 10-04 07:40:09 | ETH | down | 0.63→0.57 | 0.67 → 0.67 → 0.67 | 6.59s | DOWN @ 0.34 | -0.13 / -1.96 / · |
| 10-04 07:39:40 | ZEC | down | 0.86→0.80 | 0.89 → 0.89 → 0.89 | no | DOWN @ 0.12 | -0.44 / -0.62 / · |
| 10-04 07:39:38 | HYPE | up | 0.64→0.76 | 0.61 → 0.61 → 0.61 | 7.35s | UP @ 0.63 | 1.10 / 1.10 / · |
| 10-04 07:39:08 | NEAR | down | 0.15→0.04 | 0.15 → 0.15 → 0.15 | 22.91s | DOWN @ 0.86 | -0.70 / 0.74 / · |
| 10-04 07:39:08 | SOL | down | 0.25→0.19 | 0.20 → 0.20 → 0.20 | 22.91s | — |  |
| 10-04 07:38:51 | NEAR | down | 0.26→0.19 | 0.25 → 0.25 → 0.25 | 9.36s | DOWN @ 0.76 | 0.57 / 0.26 / · |
| 10-04 07:38:36 | SOL | down | 0.27→0.21 | 0.18 → 0.18 → 0.18 | no | — |  |
| 10-04 07:38:35 | XRP | up | 0.20→0.25 | 0.14 → 0.14 → 0.14 | 10.86s | UP @ 0.15 | -0.37 / 0.20 / · |
