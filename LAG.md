# Lag Tracker

*Updated Sun Oct 04 06:54 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 589 | 10.8s | 3% | 0% |
| BTC | 462 | 11.9s | 3% | 0% |
| DOGE | 640 | 10.4s | 2% | 0% |
| ETH | 616 | 11.2s | 3% | 0% |
| HYPE | 520 | 11.5s | 4% | 0% |
| NEAR | 592 | 10.7s | 4% | 0% |
| SOL | 1135 | 10.8s | 3% | 0% |
| XRP | 1123 | 11.0s | 3% | 0% |
| ZEC | 732 | 9.8s | 4% | 0% |
| **All** | **6409** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3277 | 908 | $-402.76 | -2.8% | $-176.28 / $-226.48 |
| Sell after 30 sec | 3277 | 1872 | $987.23 | +6.9% | $549.33 / $437.90 |
| Hold to the close | 3263 | 1633 | $2150.08 | +15.2% | $1141.70 / $1008.38 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **31 ms** · Coinbase price delay: **14 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 06:54:35 | HYPE | up | 0.71→0.79 | 0.79 → 0.79 → 0.89 | 3.79s | — |  |
| 10-04 06:54:25 | BNB | up | 0.75→0.84 | 0.96 → 0.97 → 0.97 | no | — |  |
| 10-04 06:54:23 | SOL | up | 0.83→0.92 | 0.85 → 0.85 → 0.84 | 16.04s | UP @ 0.87 | -0.48 / 0.49 / · |
| 10-04 06:54:03 | SOL | up | 0.75→0.80 | 0.85 → 0.85 → 0.85 | no | — |  |
| 10-04 06:53:44 | NEAR | up | 0.87→0.92 | 0.95 → 0.95 → 0.95 | no | — |  |
| 10-04 06:53:44 | HYPE | up | 0.60→0.68 | 0.74 → 0.74 → 0.74 | 9.55s | — |  |
| 10-04 06:53:23 | ZEC | up | 0.79→0.86 | 0.81 → 0.81 → 0.81 | 15.30s | — |  |
| 10-04 06:53:21 | SOL | up | 0.76→0.84 | 0.88 → 0.88 → 0.89 | no | — |  |
| 10-04 06:52:58 | ETH | up | 0.80→0.86 | 0.86 → 0.86 → 0.86 | 10.81s | — |  |
| 10-04 06:52:53 | NEAR | up | 0.70→0.75 | 0.88 → 0.88 → 0.86 | 16.06s | — |  |
| 10-04 06:51:57 | ZEC | up | 0.70→0.76 | 0.69 → 0.69 → 0.69 | 11.82s | UP @ 0.71 | -0.71 / 0.95 / · |
| 10-04 06:51:44 | SOL | down | 0.81→0.75 | 0.94 → 0.94 → 0.94 | 9.82s | DOWN @ 0.06 | 0.64 / 0.64 / · |
| 10-04 06:51:40 | ZEC | up | 0.65→0.71 | 0.54 → 0.72 → 0.72 | 0.31s | — |  |
| 10-04 06:51:39 | HYPE | up | 0.36→0.44 | 0.56 → 0.56 → 0.56 | 29.58s | — |  |
| 10-04 06:51:30 | ETH | up | 0.68→0.74 | 0.68 → 0.68 → 0.68 | 8.32s | UP @ 0.68 | 0.30 / 0.30 / · |
| 10-04 06:51:26 | BTC | up | 0.77→0.88 | 0.81 → 0.86 → 0.86 | 0.07s | — |  |
| 10-04 06:51:23 | ZEC | up | 0.45→0.50 | 0.49 → 0.49 → 0.54 | 0.58s | — |  |
| 10-04 06:51:11 | BTC | up | 0.71→0.76 | 0.80 → 0.81 → 0.81 | 13.08s | — |  |
| 10-04 06:51:10 | SOL | up | 0.75→0.80 | 0.85 → 0.88 → 0.88 | 13.58s | — |  |
| 10-04 06:51:04 | XRP | up | 0.73→0.79 | 0.85 → 0.85 → 0.85 | 20.09s | — |  |
| 10-04 06:50:41 | ETH | down | 0.67→0.61 | 0.69 → 0.69 → 0.69 | 12.34s | DOWN @ 0.32 | -0.41 / -0.02 / · |
| 10-04 06:50:26 | BNB | down | 0.62→0.54 | 0.84 → 0.84 → 0.84 | no | DOWN @ 0.17 | -0.39 / -0.58 / · |
| 10-04 06:50:24 | BTC | down | 0.75→0.70 | 0.80 → 0.80 → 0.80 | 14.84s | DOWN @ 0.21 | -0.34 / -0.34 / · |
| 10-04 06:50:06 | NEAR | down | 0.80→0.74 | 0.90 → 0.90 → 0.89 | no | DOWN @ 0.11 | -0.33 / -0.42 / · |
| 10-04 06:49:39 | HYPE | up | 0.28→0.34 | 0.42 → 0.41 → 0.41 | no | — |  |
| 10-04 06:49:21 | NEAR | down | 0.68→0.62 | 0.79 → 0.79 → 0.82 | no | DOWN @ 0.22 | -0.73 / -1.21 / · |
| 10-04 06:49:00 | SOL | up | 0.53→0.62 | 0.66 → 0.66 → 0.66 | 23.37s | — |  |
| 10-04 06:48:48 | NEAR | up | 0.58→0.64 | 0.76 → 0.76 → 0.76 | 20.87s | — |  |
| 10-04 06:48:44 | DOGE | up | 0.65→0.75 | 0.82 → 0.82 → 0.82 | 9.87s | — |  |
| 10-04 06:48:25 | SOL | down | 0.57→0.50 | 0.65 → 0.65 → 0.65 | no | DOWN @ 0.36 | -0.43 / -0.53 / · |
