# Lag Tracker

*Updated Sun Oct 04 02:14 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 422 | 10.7s | 4% | 0% |
| BTC | 339 | 12.5s | 2% | 0% |
| DOGE | 463 | 10.5s | 2% | 0% |
| ETH | 424 | 11.2s | 3% | 0% |
| HYPE | 338 | 11.6s | 3% | 0% |
| NEAR | 388 | 10.7s | 4% | 0% |
| SOL | 826 | 10.6s | 3% | 0% |
| XRP | 743 | 11.2s | 4% | 0% |
| ZEC | 475 | 9.8s | 5% | 0% |
| **All** | **4418** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2301 | 643 | $-255.82 | -2.6% | $-107.35 / $-148.47 |
| Sell after 30 sec | 2300 | 1343 | $751.26 | +7.6% | $447.22 / $304.04 |
| Hold to the close | 2229 | 1103 | $1456.24 | +15.2% | $959.33 / $496.91 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **38 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 02:13:39 | DOGE | down | 0.57→0.42 | 0.84 → 0.84 → 0.84 | no | DOWN @ 0.16 | -0.48 / · / · |
| 10-04 02:13:36 | SOL | up | 0.07→0.22 | 0.33 → 0.33 → 0.33 | 12.29s | — |  |
| 10-04 02:13:30 | NEAR | up | 0.28→0.43 | 0.69 → 0.69 → 0.66 | 18.54s | — |  |
| 10-04 02:13:24 | DOGE | down | 0.77→0.56 | 0.98 → 0.98 → 0.98 | 9.28s | — |  |
| 10-04 02:13:22 | XRP | down | 0.98→0.92 | 0.97 → 0.97 → 0.97 | no | — |  |
| 10-04 02:13:11 | ETH | down | 0.24→0.09 | 0.28 → 0.28 → 0.28 | 7.79s | DOWN @ 0.72 | 0.32 / 2.13 / · |
| 10-04 02:13:08 | SOL | down | 0.27→0.19 | 0.46 → 0.46 → 0.46 | 10.54s | DOWN @ 0.56 | -0.76 / 0.76 / · |
| 10-04 02:13:08 | NEAR | down | 0.50→0.37 | 0.82 → 0.82 → 0.82 | 11.04s | DOWN @ 0.19 | -0.51 / 1.23 / · |
| 10-04 02:12:56 | ETH | up | 0.18→0.30 | 0.28 → 0.28 → 0.28 | no | — |  |
| 10-04 02:12:56 | DOGE | down | 0.86→0.80 | 0.97 → 0.97 → 0.97 | no | — |  |
| 10-04 02:12:51 | SOL | down | 0.17→0.10 | 0.56 → 0.38 → 0.38 | 0.27s | DOWN @ 0.64 | -0.64 / -0.54 / · |
| 10-04 02:12:49 | NEAR | down | 0.19→0.12 | 0.46 → 0.39 → 0.39 | 0.27s | DOWN @ 0.62 | -0.44 / -3.62 / · |
| 10-04 02:12:48 | XRP | down | 0.98→0.93 | 0.95 → 0.95 → 0.95 | no | — |  |
| 10-04 02:12:41 | ETH | up | 0.22→0.37 | 0.27 → 0.27 → 0.27 | no | UP @ 0.27 | -0.19 / -0.19 / · |
| 10-04 02:12:34 | NEAR | down | 0.27→0.20 | 0.33 → 0.46 → 0.46 | no | DOWN @ 0.55 | -0.46 / -4.18 / · |
| 10-04 02:12:32 | SOL | up | 0.25→0.32 | 0.58 → 0.58 → 0.56 | no | — |  |
| 10-04 02:12:25 | ETH | down | 0.48→0.39 | 0.76 → 0.76 → 0.76 | 8.78s | DOWN @ 0.25 | 4.52 / 4.31 / · |
| 10-04 02:12:17 | SOL | down | 0.48→0.40 | 0.17 → 0.17 → 0.58 | no | — |  |
| 10-04 02:12:07 | ETH | up | 0.60→0.79 | 0.61 → 0.61 → 0.61 | 11.78s | UP @ 0.62 | -0.44 / -3.91 / · |
| 10-04 02:12:01 | DOGE | down | 0.88→0.78 | 0.92 → 0.92 → 0.92 | no | DOWN @ 0.09 | -0.17 / -0.50 / · |
| 10-04 02:12:00 | SOL | up | 0.13→0.28 | 0.24 → 0.24 → 0.17 | 18.54s | — |  |
| 10-04 02:11:52 | ETH | down | 0.57→0.48 | 0.52 → 0.52 → 0.52 | no | — |  |
| 10-04 02:11:47 | NEAR | down | 0.25→0.20 | 0.40 → 0.40 → 0.34 | 2.03s | DOWN @ 0.61 | -0.04 / 0.37 / · |
| 10-04 02:11:44 | SOL | up | 0.11→0.18 | 0.25 → 0.25 → 0.24 | no | — |  |
| 10-04 02:11:29 | SOL | down | 0.24→0.09 | 0.40 → 0.40 → 0.25 | 4.53s | DOWN @ 0.61 | 0.99 / 1.09 / · |
| 10-04 02:11:28 | HYPE | down | 0.30→0.22 | 0.38 → 0.38 → 0.38 | 5.53s | — |  |
| 10-04 02:11:16 | ETH | down | 0.64→0.56 | 0.60 → 0.60 → 0.56 | 17.54s | — |  |
| 10-04 02:11:07 | SOL | up | 0.14→0.26 | 0.34 → 0.34 → 0.34 | 11.54s | — |  |
| 10-04 02:11:02 | NEAR | up | 0.20→0.25 | 0.33 → 0.33 → 0.29 | 16.29s | — |  |
| 10-04 02:10:59 | BTC | up | 0.91→0.96 | 0.90 → 0.90 → 0.95 | 4.28s | UP @ 0.90 | 0.34 / 0.29 / · |
