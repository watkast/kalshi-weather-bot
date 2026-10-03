# Lag Tracker

*Updated Sat Oct 03 20:02 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 188 | 10.7s | 6% | 0% |
| BTC | 108 | 11.1s | 3% | 0% |
| DOGE | 158 | 9.8s | 3% | 0% |
| ETH | 113 | 11.0s | 3% | 0% |
| HYPE | 104 | 11.8s | 3% | 0% |
| NEAR | 135 | 9.2s | 4% | 0% |
| SOL | 264 | 9.3s | 5% | 0% |
| XRP | 243 | 9.6s | 5% | 0% |
| ZEC | 174 | 9.6s | 6% | 0% |
| **All** | **1487** | **9.9s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 791 | 259 | $-53.11 | -1.6% | $-17.14 / $-35.97 |
| Sell after 30 sec | 791 | 512 | $357.76 | +10.5% | $221.69 / $136.07 |
| Hold to the close | 784 | 399 | $633.36 | +18.9% | $431.82 / $201.54 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 20:02:09 | HYPE | up | 0.83→0.90 | 0.72 → 0.72 → 0.72 | 9.37s | UP @ 0.73 | 1.18 / 1.39 / · |
| 10-03 20:02:08 | ETH | up | 0.73→0.79 | 0.77 → 0.77 → 0.77 | no | — |  |
| 10-03 20:02:07 | ZEC | up | 0.70→0.79 | 0.62 → 0.62 → 0.62 | 26.38s | UP @ 0.63 | -0.54 / 0.07 / · |
| 10-03 20:01:52 | ZEC | down | 0.69→0.61 | 0.61 → 0.61 → 0.61 | no | — |  |
| 10-03 20:01:50 | HYPE | up | 0.69→0.77 | 0.65 → 0.71 → 0.71 | 0.09s | UP @ 0.72 | -0.40 / 1.27 / · |
| 10-03 20:01:39 | ETH | up | 0.57→0.65 | 0.56 → 0.56 → 0.56 | 9.88s | UP @ 0.57 | 1.28 / 1.59 / · |
| 10-03 20:01:36 | DOGE | up | 0.60→0.66 | 0.74 → 0.74 → 0.74 | 12.38s | — |  |
| 10-03 20:01:35 | HYPE | up | 0.62→0.71 | 0.72 → 0.65 → 0.65 | no | UP @ 0.66 | -0.63 / 0.29 / · |
| 10-03 20:01:32 | SOL | up | 0.71→0.78 | 0.78 → 0.78 → 0.77 | no | — |  |
| 10-03 20:01:31 | XRP | up | 0.78→0.86 | 0.81 → 0.81 → 0.79 | no | UP @ 0.81 | -0.54 / -0.33 / · |
| 10-03 20:01:28 | NEAR | up | 0.68→0.73 | 0.73 → 0.73 → 0.73 | no | — |  |
| 10-03 20:01:25 | BNB | down | 0.69→0.63 | 0.67 → 0.67 → 0.67 | no | — |  |
| 10-03 20:01:16 | HYPE | up | 0.55→0.62 | 0.69 → 0.69 → 0.72 | no | — |  |
| 10-03 20:00:36 | HYPE | up | 0.65→0.71 | 0.62 → 0.62 → 0.62 | 22.40s | UP @ 0.63 | -0.44 / 0.38 / · |
| 10-03 19:58:36 | XRP | up | 0.28→0.50 | 0.80 → 0.80 → 0.80 | no | — |  |
| 10-03 19:58:17 | SOL | up | 0.89→0.96 | 0.96 → 0.96 → 0.97 | no | — |  |
| 10-03 19:58:11 | XRP | down | 0.18→0.12 | 0.39 → 0.39 → 0.39 | 8.93s | DOWN @ 0.63 | -0.13 / -4.68 / 3.53 |
| 10-03 19:58:01 | SOL | up | 0.80→0.91 | 0.92 → 0.92 → 0.96 | no | — |  |
| 10-03 19:57:47 | XRP | up | 0.12→0.21 | 0.30 → 0.30 → 0.36 | 2.69s | — |  |
| 10-03 19:57:45 | SOL | down | 0.84→0.78 | 0.81 → 0.81 → 0.92 | no | — |  |
| 10-03 19:57:27 | SOL | down | 0.60→0.52 | 0.82 → 0.82 → 0.82 | no | DOWN @ 0.19 | -0.22 / -1.33 / -2.01 |
| 10-03 19:57:12 | SOL | down | 0.68→0.51 | 0.85 → 0.85 → 0.85 | no | DOWN @ 0.16 | -0.10 / 0.09 / -1.70 |
| 10-03 19:57:05 | NEAR | down | 0.12→0.06 | 0.11 → 0.09 → 0.09 | 14.95s | — |  |
| 10-03 19:57:02 | BTC | up | 0.88→0.93 | 0.88 → 0.88 → 0.92 | 2.44s | — |  |
| 10-03 19:56:54 | SOL | up | 0.59→0.67 | 0.79 → 0.79 → 0.79 | 10.45s | — |  |
| 10-03 19:56:47 | DOGE | down | 0.29→0.20 | 0.34 → 0.34 → 0.32 | no | DOWN @ 0.67 | -0.22 / -0.22 / 3.14 |
| 10-03 19:56:39 | SOL | up | 0.66→0.78 | 0.77 → 0.77 → 0.77 | 25.45s | — |  |
| 10-03 19:56:27 | DOGE | up | 0.24→0.30 | 0.48 → 0.48 → 0.48 | no | — |  |
| 10-03 19:56:23 | SOL | down | 0.77→0.65 | 0.83 → 0.83 → 0.83 | 11.21s | DOWN @ 0.18 | -0.41 / -0.03 / -1.91 |
| 10-03 19:56:23 | XRP | down | 0.39→0.23 | 0.56 → 0.56 → 0.56 | 11.96s | DOWN @ 0.44 | -0.46 / 0.64 / 5.42 |
