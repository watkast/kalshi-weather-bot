# Lag Tracker

*Updated Sat Oct 03 20:23 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 200 | 10.7s | 7% | 0% |
| BTC | 125 | 11.3s | 2% | 0% |
| DOGE | 178 | 9.8s | 2% | 0% |
| ETH | 125 | 10.8s | 2% | 0% |
| HYPE | 110 | 11.8s | 4% | 0% |
| NEAR | 138 | 9.2s | 4% | 0% |
| SOL | 284 | 9.2s | 5% | 0% |
| XRP | 266 | 9.8s | 5% | 0% |
| ZEC | 190 | 9.9s | 6% | 0% |
| **All** | **1616** | **10.0s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 855 | 279 | $-56.32 | -1.5% | $-13.44 / $-42.88 |
| Sell after 30 sec | 851 | 544 | $365.02 | +10.1% | $239.49 / $125.53 |
| Hold to the close | 809 | 408 | $626.50 | +18.1% | $465.15 / $161.35 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **34 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 20:22:58 | SOL | up | 0.25→0.32 | 0.76 → 0.76 → 0.76 | no | — |  |
| 10-03 20:22:50 | BTC | up | 0.38→0.44 | 0.88 → 0.88 → 0.88 | no | — |  |
| 10-03 20:22:46 | ZEC | down | 0.94→0.86 | 0.92 → 0.92 → 0.89 | 17.53s | DOWN @ 0.09 | -0.08 / · / · |
| 10-03 20:22:45 | DOGE | down | 0.63→0.49 | 0.83 → 0.83 → 0.49 | 4.05s | DOWN @ 0.18 | 2.91 / · / · |
| 10-03 20:22:45 | ETH | down | 0.83→0.63 | 0.82 → 0.82 → 0.48 | 4.05s | DOWN @ 0.19 | 2.91 / · / · |
| 10-03 20:22:42 | SOL | up | 0.56→0.65 | 0.75 → 0.75 → 0.75 | no | — |  |
| 10-03 20:22:40 | XRP | up | 0.47→0.53 | 0.63 → 0.63 → 0.63 | no | — |  |
| 10-03 20:22:39 | HYPE | down | 0.25→0.18 | 0.41 → 0.35 → 0.35 | 0.24s | DOWN @ 0.66 | 1.23 / · / · |
| 10-03 20:22:35 | BTC | up | 0.78→0.86 | 0.85 → 0.85 → 0.88 | no | — |  |
| 10-03 20:22:19 | XRP | up | 0.47→0.53 | 0.68 → 0.68 → 0.59 | no | — |  |
| 10-03 20:22:19 | DOGE | down | 0.78→0.68 | 0.83 → 0.83 → 0.82 | 29.81s | DOWN @ 0.17 | -0.30 / 3.02 / · |
| 10-03 20:22:04 | XRP | down | 0.56→0.50 | 0.73 → 0.73 → 0.68 | 3.31s | DOWN @ 0.27 | 0.20 / 0.99 / · |
| 10-03 20:22:03 | SOL | down | 0.79→0.72 | 0.87 → 0.87 → 0.82 | 4.81s | DOWN @ 0.14 | 0.11 / 1.16 / · |
| 10-03 20:21:49 | XRP | down | 0.62→0.50 | 0.78 → 0.78 → 0.73 | 18.31s | DOWN @ 0.23 | 0.03 / 0.61 / · |
| 10-03 20:21:48 | SOL | down | 0.81→0.75 | 0.83 → 0.83 → 0.83 | no | DOWN @ 0.17 | -0.68 / -0.20 / · |
| 10-03 20:21:43 | DOGE | up | 0.66→0.81 | 0.91 → 0.91 → 0.91 | no | — |  |
| 10-03 20:21:42 | ETH | up | 0.78→0.83 | 0.78 → 0.78 → 0.78 | no | UP @ 0.79 | -0.45 / -0.45 / · |
| 10-03 20:21:42 | BTC | up | 0.68→0.77 | 0.76 → 0.76 → 0.76 | 10.56s | — |  |
| 10-03 20:21:31 | HYPE | up | 0.35→0.44 | 0.42 → 0.42 → 0.42 | 7.06s | — |  |
| 10-03 20:21:30 | XRP | down | 0.69→0.64 | 0.79 → 0.79 → 0.79 | 22.82s | DOWN @ 0.22 | -0.26 / 0.13 / · |
| 10-03 20:21:28 | DOGE | down | 0.79→0.66 | 0.90 → 0.90 → 0.90 | no | DOWN @ 0.11 | -0.33 / -0.31 / · |
| 10-03 20:21:11 | XRP | up | 0.61→0.69 | 0.77 → 0.77 → 0.77 | no | — |  |
| 10-03 20:21:10 | SOL | down | 0.77→0.71 | 0.79 → 0.79 → 0.79 | no | DOWN @ 0.22 | -0.35 / -0.83 / · |
| 10-03 20:20:39 | ETH | up | 0.63→0.68 | 0.65 → 0.67 → 0.67 | 14.06s | — |  |
| 10-03 20:20:36 | HYPE | up | 0.25→0.36 | 0.38 → 0.38 → 0.41 | no | — |  |
| 10-03 20:20:34 | XRP | down | 0.56→0.50 | 0.62 → 0.62 → 0.63 | no | DOWN @ 0.39 | -0.64 / -2.09 / · |
| 10-03 20:20:33 | SOL | up | 0.63→0.70 | 0.69 → 0.69 → 0.78 | 4.81s | — |  |
| 10-03 20:20:14 | XRP | up | 0.50→0.63 | 0.68 → 0.68 → 0.68 | no | — |  |
| 10-03 20:20:14 | HYPE | up | 0.16→0.29 | 0.27 → 0.27 → 0.27 | 8.56s | — |  |
| 10-03 20:20:09 | SOL | down | 0.73→0.59 | 0.76 → 0.76 → 0.76 | no | DOWN @ 0.25 | -0.37 / -0.57 / · |
