# Lag Tracker

*Updated Sat Oct 03 19:52 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 184 | 10.7s | 6% | 0% |
| BTC | 101 | 11.4s | 3% | 0% |
| DOGE | 148 | 9.8s | 3% | 0% |
| ETH | 107 | 11.1s | 3% | 0% |
| HYPE | 94 | 11.8s | 2% | 0% |
| NEAR | 129 | 9.3s | 4% | 0% |
| SOL | 247 | 9.1s | 5% | 0% |
| XRP | 229 | 9.6s | 6% | 0% |
| ZEC | 171 | 9.6s | 6% | 0% |
| **All** | **1410** | **9.9s** | **5%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 750 | 246 | $-59.50 | -1.9% | $-13.14 / $-46.36 |
| Sell after 30 sec | 749 | 485 | $326.98 | +10.2% | $208.25 / $118.73 |
| Hold to the close | 702 | 355 | $591.68 | +20.0% | $412.78 / $178.90 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 19:52:42 | SOL | down | 0.56→0.46 | 0.60 → 0.60 → 0.60 | 7.31s | DOWN @ 0.40 | 0.15 / · / · |
| 10-03 19:52:42 | DOGE | up | 0.27→0.36 | 0.39 → 0.39 → 0.39 | no | — |  |
| 10-03 19:52:38 | ETH | up | 0.35→0.42 | 0.46 → 0.46 → 0.46 | 11.31s | — |  |
| 10-03 19:52:36 | XRP | up | 0.16→0.25 | 0.34 → 0.34 → 0.34 | no | — |  |
| 10-03 19:52:15 | SOL | up | 0.51→0.60 | 0.58 → 0.58 → 0.60 | no | — |  |
| 10-03 19:52:10 | HYPE | up | 0.52→0.68 | 0.68 → 0.68 → 0.68 | no | — |  |
| 10-03 19:52:10 | BTC | up | 0.27→0.36 | 0.27 → 0.27 → 0.27 | 9.61s | UP @ 0.27 | 0.69 / 0.50 / · |
| 10-03 19:52:10 | BNB | up | 0.55→0.60 | 0.61 → 0.61 → 0.61 | 9.86s | — |  |
| 10-03 19:51:59 | SOL | down | 0.55→0.46 | 0.58 → 0.58 → 0.58 | no | DOWN @ 0.42 | -0.45 / -0.65 / · |
| 10-03 19:51:47 | DOGE | down | 0.37→0.29 | 0.41 → 0.41 → 0.41 | no | DOWN @ 0.60 | -0.55 / -0.44 / · |
| 10-03 19:51:45 | XRP | down | 0.23→0.18 | 0.29 → 0.29 → 0.34 | no | DOWN @ 0.72 | -1.01 / -0.91 / · |
| 10-03 19:51:42 | SOL | up | 0.46→0.55 | 0.57 → 0.57 → 0.57 | no | — |  |
| 10-03 19:51:30 | XRP | up | 0.12→0.23 | 0.28 → 0.28 → 0.29 | 19.81s | — |  |
| 10-03 19:51:25 | SOL | down | 0.55→0.42 | 0.57 → 0.57 → 0.57 | no | DOWN @ 0.43 | -0.46 / -0.55 / · |
| 10-03 19:51:23 | ZEC | up | 0.83→0.90 | 0.82 → 0.82 → 0.82 | 27.07s | UP @ 0.83 | -0.31 / 0.32 / · |
| 10-03 19:51:19 | DOGE | up | 0.29→0.37 | 0.41 → 0.44 → 0.44 | no | — |  |
| 10-03 19:51:10 | SOL | up | 0.46→0.55 | 0.56 → 0.56 → 0.56 | no | — |  |
| 10-03 19:51:08 | XRP | up | 0.12→0.19 | 0.29 → 0.29 → 0.29 | no | — |  |
| 10-03 19:51:06 | ZEC | down | 0.84→0.75 | 0.85 → 0.85 → 0.85 | no | — |  |
| 10-03 19:51:03 | BNB | down | 0.59→0.50 | 0.57 → 0.57 → 0.59 | no | DOWN @ 0.43 | -0.65 / -0.65 / · |
| 10-03 19:50:55 | SOL | down | 0.55→0.47 | 0.56 → 0.56 → 0.56 | no | DOWN @ 0.45 | -0.56 / -0.66 / · |
| 10-03 19:50:47 | NEAR | up | 0.34→0.40 | 0.38 → 0.38 → 0.39 | no | — |  |
| 10-03 19:50:43 | HYPE | up | 0.51→0.59 | 0.53 → 0.53 → 0.53 | no | UP @ 0.54 | -0.36 / -0.16 / · |
| 10-03 19:50:39 | SOL | down | 0.55→0.47 | 0.54 → 0.54 → 0.54 | no | DOWN @ 0.47 | -0.46 / -0.76 / · |
| 10-03 19:50:32 | NEAR | down | 0.38→0.31 | 0.46 → 0.46 → 0.38 | 2.31s | DOWN @ 0.55 | 0.25 / 0.25 / · |
| 10-03 19:50:28 | HYPE | down | 0.59→0.51 | 0.52 → 0.52 → 0.52 | no | — |  |
| 10-03 19:50:23 | BNB | up | 0.45→0.55 | 0.46 → 0.46 → 0.46 | 11.81s | UP @ 0.46 | -0.46 / 0.74 / · |
| 10-03 19:50:21 | ETH | up | 0.24→0.38 | 0.28 → 0.28 → 0.28 | 13.56s | UP @ 0.28 | -0.39 / 1.07 / · |
| 10-03 19:50:21 | BTC | up | 0.16→0.22 | 0.17 → 0.17 → 0.17 | 13.56s | UP @ 0.18 | -0.31 / 0.94 / · |
| 10-03 19:50:20 | XRP | up | 0.12→0.17 | 0.24 → 0.23 → 0.23 | no | — |  |
