# Lag Tracker

*Updated Sun Oct 04 05:24 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 539 | 10.8s | 4% | 0% |
| BTC | 421 | 11.9s | 2% | 0% |
| DOGE | 583 | 10.8s | 2% | 0% |
| ETH | 552 | 10.9s | 3% | 0% |
| HYPE | 467 | 11.6s | 3% | 0% |
| NEAR | 530 | 10.8s | 4% | 0% |
| SOL | 1051 | 10.6s | 3% | 0% |
| XRP | 1044 | 10.8s | 4% | 0% |
| ZEC | 690 | 9.7s | 4% | 0% |
| **All** | **5877** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3026 | 842 | $-373.76 | -2.9% | $-169.67 / $-204.09 |
| Sell after 30 sec | 3024 | 1739 | $901.56 | +6.9% | $524.38 / $377.18 |
| Hold to the close | 2981 | 1472 | $1812.17 | +14.0% | $901.73 / $910.44 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **31 ms** · Coinbase price delay: **15 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 05:24:29 | NEAR | down | 0.65→0.59 | 0.81 → 0.81 → 0.81 | no | DOWN @ 0.21 | · / · / · |
| 10-04 05:24:29 | ZEC | down | 0.24→0.16 | 0.20 → 0.20 → 0.20 | no | — |  |
| 10-04 05:24:28 | BNB | up | 0.74→0.89 | 0.90 → 0.90 → 0.90 | no | — |  |
| 10-04 05:24:20 | DOGE | up | 0.67→0.75 | 0.74 → 0.74 → 0.78 | no | — |  |
| 10-04 05:24:13 | BNB | down | 0.85→0.76 | 0.89 → 0.89 → 0.89 | no | DOWN @ 0.12 | -0.43 / · / · |
| 10-04 05:24:10 | XRP | up | 0.81→0.91 | 0.79 → 0.81 → 0.81 | 12.53s | UP @ 0.81 | -0.33 / · / · |
| 10-04 05:24:04 | DOGE | up | 0.58→0.67 | 0.73 → 0.73 → 0.74 | no | — |  |
| 10-04 05:23:55 | ZEC | up | 0.21→0.27 | 0.08 → 0.08 → 0.08 | 12.80s | UP @ 0.10 | -0.37 / 0.65 / · |
| 10-04 05:23:49 | DOGE | up | 0.47→0.58 | 0.64 → 0.64 → 0.73 | 4.03s | — |  |
| 10-04 05:23:48 | SOL | up | 0.62→0.71 | 0.76 → 0.76 → 0.79 | 19.31s | — |  |
| 10-04 05:23:44 | NEAR | up | 0.50→0.59 | 0.70 → 0.70 → 0.70 | 8.28s | — |  |
| 10-04 05:23:29 | XRP | down | 0.83→0.75 | 0.82 → 0.82 → 0.82 | no | — |  |
| 10-04 05:23:20 | SOL | down | 0.68→0.62 | 0.72 → 0.72 → 0.74 | no | DOWN @ 0.29 | -0.69 / -0.78 / · |
| 10-04 05:23:02 | ZEC | down | 0.36→0.30 | 0.21 → 0.21 → 0.21 | 6.03s | — |  |
| 10-04 05:22:54 | SOL | up | 0.58→0.67 | 0.70 → 0.66 → 0.66 | no | — |  |
| 10-04 05:22:53 | HYPE | up | 0.51→0.57 | 0.68 → 0.68 → 0.68 | no | — |  |
| 10-04 05:22:42 | BNB | down | 0.70→0.65 | 0.81 → 0.81 → 0.81 | no | DOWN @ 0.19 | -0.32 / -0.70 / · |
| 10-04 05:22:40 | XRP | down | 0.88→0.77 | 0.81 → 0.81 → 0.81 | no | — |  |
| 10-04 05:22:38 | SOL | down | 0.71→0.58 | 0.81 → 0.70 → 0.70 | 0.02s | DOWN @ 0.31 | -0.60 / -0.79 / · |
| 10-04 05:22:35 | ZEC | down | 0.42→0.34 | 0.43 → 0.43 → 0.28 | 2.28s | DOWN @ 0.57 | 0.76 / 1.69 / · |
| 10-04 05:22:25 | DOGE | down | 0.65→0.58 | 0.71 → 0.71 → 0.71 | 27.54s | DOWN @ 0.29 | -0.40 / 0.68 / · |
| 10-04 05:22:25 | HYPE | down | 0.72→0.66 | 0.78 → 0.79 → 0.79 | 12.53s | DOWN @ 0.22 | -0.45 / 0.62 / · |
| 10-04 05:22:24 | NEAR | up | 0.58→0.65 | 0.73 → 0.74 → 0.74 | 14.03s | — |  |
| 10-04 05:22:23 | SOL | up | 0.75→0.85 | 0.83 → 0.81 → 0.81 | no | — |  |
| 10-04 05:22:08 | SOL | up | 0.78→0.84 | 0.79 → 0.83 → 0.83 | 0.02s | — |  |
| 10-04 05:22:04 | NEAR | up | 0.59→0.65 | 0.72 → 0.72 → 0.73 | no | — |  |
| 10-04 05:22:04 | DOGE | down | 0.65→0.57 | 0.72 → 0.72 → 0.74 | no | DOWN @ 0.29 | -0.69 / -0.40 / · |
| 10-04 05:21:48 | SOL | up | 0.78→0.84 | 0.72 → 0.72 → 0.79 | 4.78s | UP @ 0.74 | 0.13 / 0.55 / · |
| 10-04 05:21:38 | DOGE | down | 0.57→0.49 | 0.61 → 0.57 → 0.57 | no | — |  |
| 10-04 05:21:33 | SOL | up | 0.62→0.70 | 0.70 → 0.70 → 0.72 | 19.78s | UP @ 0.71 | -0.30 / 0.42 / · |
