# Lag Tracker

*Updated Sun Oct 04 00:13 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 345 | 10.8s | 5% | 0% |
| BTC | 266 | 11.8s | 2% | 0% |
| DOGE | 377 | 10.5s | 2% | 0% |
| ETH | 340 | 10.9s | 3% | 0% |
| HYPE | 261 | 11.7s | 3% | 0% |
| NEAR | 297 | 10.5s | 4% | 0% |
| SOL | 652 | 10.2s | 3% | 0% |
| XRP | 615 | 11.2s | 3% | 0% |
| ZEC | 366 | 9.5s | 5% | 0% |
| **All** | **3519** | **10.6s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1847 | 523 | $-199.72 | -2.5% | $-73.18 / $-126.54 |
| Sell after 30 sec | 1846 | 1073 | $591.60 | +7.4% | $374.01 / $217.59 |
| Hold to the close | 1771 | 911 | $1472.25 | +19.3% | $515.96 / $956.29 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **38 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 00:13:37 | DOGE | down | 0.98→0.81 | 0.96 → 0.96 → — | no | — |  |
| 10-04 00:13:26 | XRP | up | 0.05→0.29 | 0.38 → 0.38 → 0.35 | no | — |  |
| 10-04 00:13:24 | ETH | up | 0.26→0.39 | 0.23 → 0.23 → 0.23 | 6.64s | UP @ 0.25 | 2.18 / · / · |
| 10-04 00:13:14 | DOGE | up | 0.49→0.76 | 0.91 → 0.91 → 0.93 | no | — |  |
| 10-04 00:12:59 | XRP | up | 0.12→0.17 | 0.50 → 0.50 → 0.48 | no | — |  |
| 10-04 00:12:59 | DOGE | down | 0.74→0.55 | 0.90 → 0.90 → 0.91 | no | DOWN @ 0.11 | -0.34 / -0.68 / · |
| 10-04 00:12:45 | ETH | up | 0.22→0.28 | 0.26 → 0.26 → 0.27 | 15.67s | — |  |
| 10-04 00:12:37 | XRP | up | 0.07→0.15 | 0.37 → 0.37 → 0.37 | 8.65s | — |  |
| 10-04 00:12:28 | ETH | up | 0.24→0.37 | 0.29 → 0.29 → 0.26 | no | UP @ 0.30 | -0.79 / -0.69 / · |
| 10-04 00:12:22 | ZEC | up | 0.80→0.87 | 0.81 → 0.81 → 0.81 | 8.40s | — |  |
| 10-04 00:12:22 | XRP | down | 0.17→0.09 | 0.41 → 0.41 → 0.41 | no | DOWN @ 0.60 | -0.14 / -1.45 / · |
| 10-04 00:12:08 | ETH | down | 0.31→0.24 | 0.28 → 0.28 → 0.28 | no | — |  |
| 10-04 00:12:04 | XRP | down | 0.18→0.10 | 0.45 → 0.45 → 0.45 | 26.41s | DOWN @ 0.57 | -0.76 / 0.15 / · |
| 10-04 00:12:04 | ZEC | down | 0.89→0.80 | 0.96 → 0.96 → 0.96 | 11.41s | — |  |
| 10-04 00:11:51 | ETH | down | 0.32→0.23 | 0.32 → 0.32 → 0.32 | no | DOWN @ 0.69 | -0.10 / -0.20 / · |
| 10-04 00:11:40 | ZEC | up | 0.74→0.87 | 0.89 → 0.89 → 0.89 | 6.16s | — |  |
| 10-04 00:11:38 | XRP | up | 0.06→0.20 | 0.26 → 0.26 → 0.26 | 8.17s | — |  |
| 10-04 00:11:36 | ETH | up | 0.24→0.30 | 0.28 → 0.28 → 0.28 | 9.42s | — |  |
| 10-04 00:11:24 | ZEC | down | 0.83→0.73 | 0.88 → 0.88 → 0.88 | no | DOWN @ 0.13 | -0.35 / -1.08 / · |
| 10-04 00:11:24 | SOL | down | 0.94→0.88 | 0.92 → 0.92 → 0.92 | no | DOWN @ 0.08 | -0.53 / -0.61 / · |
| 10-04 00:11:10 | XRP | up | 0.05→0.11 | 0.23 → 0.23 → 0.23 | no | — |  |
| 10-04 00:11:08 | ETH | up | 0.25→0.30 | 0.34 → 0.34 → 0.34 | no | — |  |
| 10-04 00:10:56 | DOGE | up | 0.38→0.44 | 0.56 → 0.56 → 0.56 | 19.43s | — |  |
| 10-04 00:10:54 | SOL | up | 0.77→0.86 | 0.93 → 0.93 → 0.93 | no | — |  |
| 10-04 00:10:45 | ETH | up | 0.24→0.31 | 0.24 → 0.36 → 0.36 | 0.43s | — |  |
| 10-04 00:10:41 | DOGE | down | 0.44→0.33 | 0.56 → 0.56 → 0.56 | no | DOWN @ 0.45 | -0.56 / -0.56 / · |
| 10-04 00:10:38 | SOL | down | 0.91→0.77 | 0.94 → 0.94 → 0.94 | no | DOWN @ 0.06 | -0.09 / 0.22 / · |
| 10-04 00:10:15 | DOGE | down | 0.58→0.46 | 0.80 → 0.69 → 0.69 | 0.18s | DOWN @ 0.32 | -0.51 / 0.76 / · |
| 10-04 00:10:06 | ETH | up | 0.38→0.43 | 0.42 → 0.42 → 0.42 | no | — |  |
| 10-04 00:09:58 | XRP | down | 0.21→0.14 | 0.46 → 0.46 → 0.41 | 2.68s | DOWN @ 0.56 | -0.16 / 1.58 / · |
