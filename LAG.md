# Lag Tracker

*Updated Sat Oct 03 19:42 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 174 | 10.8s | 6% | 0% |
| BTC | 97 | 11.3s | 3% | 0% |
| DOGE | 137 | 9.4s | 3% | 0% |
| ETH | 102 | 10.8s | 3% | 0% |
| HYPE | 84 | 12.0s | 2% | 0% |
| NEAR | 122 | 9.3s | 4% | 0% |
| SOL | 227 | 9.1s | 6% | 0% |
| XRP | 212 | 9.6s | 6% | 0% |
| ZEC | 163 | 9.7s | 6% | 0% |
| **All** | **1318** | **9.9s** | **5%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 698 | 230 | $-49.33 | -1.7% | $-7.30 / $-42.03 |
| Sell after 30 sec | 698 | 456 | $318.68 | +10.8% | $199.37 / $119.31 |
| Hold to the close | 628 | 320 | $591.03 | +22.7% | $370.57 / $220.46 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **37 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 19:42:42 | XRP | down | 0.87→0.72 | 0.92 → 0.92 → 0.93 | no | DOWN @ 0.08 | · / · / · |
| 10-03 19:42:37 | DOGE | up | 0.36→0.54 | 0.52 → 0.52 → 0.52 | no | — |  |
| 10-03 19:42:27 | XRP | up | 0.81→0.89 | 0.93 → 0.93 → 0.92 | no | — |  |
| 10-03 19:42:22 | DOGE | up | 0.45→0.53 | 0.62 → 0.62 → 0.62 | no | — |  |
| 10-03 19:42:10 | XRP | down | 0.84→0.75 | 0.90 → 0.90 → 0.90 | no | DOWN @ 0.10 | -0.36 / -0.34 / · |
| 10-03 19:42:07 | HYPE | up | 0.65→0.82 | 0.65 → 0.65 → 0.65 | 9.31s | UP @ 0.66 | 1.54 / 1.86 / · |
| 10-03 19:42:01 | DOGE | up | 0.38→0.53 | 0.15 → 0.17 → 0.17 | 15.06s | UP @ 0.17 | -0.30 / 4.23 / · |
| 10-03 19:42:00 | SOL | up | 0.00→0.06 | 0.02 → 0.02 → 0.02 | 16.06s | — |  |
| 10-03 19:41:58 | ZEC | up | 0.82→0.93 | 0.88 → 0.88 → 0.90 | 17.56s | — |  |
| 10-03 19:41:58 | ETH | up | 0.63→0.85 | 0.70 → 0.70 → 0.71 | 17.56s | UP @ 0.71 | -0.30 / 2.30 / · |
| 10-03 19:41:48 | XRP | down | 0.27→0.22 | 0.60 → 0.62 → 0.62 | no | DOWN @ 0.39 | -0.54 / -3.40 / · |
| 10-03 19:41:40 | ETH | up | 0.53→0.62 | 0.65 → 0.65 → 0.65 | 5.56s | — |  |
| 10-03 19:41:39 | DOGE | down | 0.20→0.11 | 0.21 → 0.21 → 0.21 | 6.81s | DOWN @ 0.80 | 0.18 / 0.08 / · |
| 10-03 19:41:36 | ZEC | up | 0.78→0.83 | 0.85 → 0.85 → 0.85 | 10.31s | — |  |
| 10-03 19:41:27 | XRP | down | 0.33→0.23 | 0.68 → 0.68 → 0.60 | 4.06s | DOWN @ 0.33 | 0.27 / 0.07 / · |
| 10-03 19:41:22 | ETH | down | 0.60→0.53 | 0.81 → 0.81 → 0.81 | 8.81s | DOWN @ 0.20 | 1.22 / 0.63 / · |
| 10-03 19:41:08 | DOGE | up | 0.25→0.31 | 0.27 → 0.27 → 0.27 | 7.81s | — |  |
| 10-03 19:41:07 | ETH | down | 0.82→0.77 | 0.81 → 0.81 → 0.81 | 23.81s | — |  |
| 10-03 19:41:00 | ZEC | down | 0.87→0.79 | 0.89 → 0.89 → 0.89 | no | DOWN @ 0.12 | -0.25 / 0.13 / · |
| 10-03 19:41:00 | XRP | up | 0.21→0.34 | 0.47 → 0.47 → 0.53 | 16.31s | — |  |
| 10-03 19:40:59 | NEAR | up | 0.89→0.95 | 0.94 → 0.94 → 0.94 | 16.56s | — |  |
| 10-03 19:40:52 | ETH | up | 0.64→0.72 | 0.78 → 0.78 → 0.78 | no | — |  |
| 10-03 19:40:50 | HYPE | down | 0.62→0.36 | 0.60 → 0.60 → 0.60 | no | — |  |
| 10-03 19:40:45 | ZEC | down | 0.91→0.86 | 0.89 → 0.89 → 0.89 | 30.82s | — |  |
| 10-03 19:40:36 | ETH | down | 0.71→0.64 | 0.80 → 0.80 → 0.80 | no | DOWN @ 0.21 | -0.43 / -0.43 / · |
| 10-03 19:40:35 | XRP | down | 0.40→0.31 | 0.68 → 0.68 → 0.68 | 11.31s | DOWN @ 0.33 | -0.42 / 0.96 / · |
| 10-03 19:40:17 | HYPE | up | 0.51→0.61 | 0.76 → 0.63 → 0.63 | no | — |  |
| 10-03 19:40:08 | ETH | up | 0.70→0.75 | 0.78 → 0.78 → 0.78 | 8.31s | — |  |
| 10-03 19:40:03 | XRP | up | 0.36→0.45 | 0.46 → 0.46 → 0.46 | 13.06s | — |  |
| 10-03 19:39:59 | NEAR | up | 0.84→0.89 | 0.93 → 0.93 → 0.91 | no | — |  |
