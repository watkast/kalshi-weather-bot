# Lag Tracker

*Updated Sun Oct 04 04:54 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 524 | 10.8s | 4% | 0% |
| BTC | 409 | 11.9s | 2% | 0% |
| DOGE | 553 | 10.7s | 2% | 0% |
| ETH | 538 | 10.9s | 3% | 0% |
| HYPE | 452 | 11.4s | 4% | 0% |
| NEAR | 503 | 10.8s | 4% | 0% |
| SOL | 1009 | 10.6s | 2% | 0% |
| XRP | 986 | 10.8s | 3% | 0% |
| ZEC | 657 | 9.8s | 4% | 0% |
| **All** | **5631** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2908 | 813 | $-350.24 | -2.8% | $-157.33 / $-192.91 |
| Sell after 30 sec | 2906 | 1670 | $867.64 | +6.9% | $502.37 / $365.27 |
| Hold to the close | 2861 | 1426 | $1847.51 | +14.9% | $849.00 / $998.51 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **31 ms** · Coinbase price delay: **15 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 04:54:15 | DOGE | down | 0.45→0.37 | 0.66 → 0.66 → 0.66 | no | DOWN @ 0.35 | -0.42 / · / · |
| 10-04 04:54:12 | BNB | up | 0.32→0.42 | 0.77 → 0.77 → 0.77 | no | — |  |
| 10-04 04:54:11 | HYPE | up | 0.02→0.08 | 0.21 → 0.21 → 0.21 | no | — |  |
| 10-04 04:54:10 | XRP | down | 0.19→0.09 | 0.14 → 0.15 → 0.15 | no | DOWN @ 0.85 | -0.29 / · / · |
| 10-04 04:54:10 | ETH | down | 0.18→0.12 | 0.23 → 0.14 → 0.14 | 0.03s | — |  |
| 10-04 04:53:51 | HYPE | down | 0.25→0.20 | 0.24 → 0.24 → 0.19 | 4.03s | — |  |
| 10-04 04:53:43 | XRP | down | 0.28→0.20 | 0.28 → 0.28 → 0.28 | 12.03s | DOWN @ 0.72 | -0.40 / 0.95 / · |
| 10-04 04:53:42 | SOL | up | 0.64→0.71 | 0.80 → 0.79 → 0.79 | no | — |  |
| 10-04 04:53:39 | ZEC | down | 0.50→0.40 | 0.56 → 0.56 → 0.42 | 0.78s | DOWN @ 0.46 | 0.64 / 0.84 / · |
| 10-04 04:53:33 | HYPE | down | 0.31→0.13 | 0.52 → 0.52 → 0.52 | 6.28s | DOWN @ 0.49 | 2.18 / 2.70 / · |
| 10-04 04:53:32 | ETH | up | 0.28→0.35 | 0.32 → 0.32 → 0.32 | no | — |  |
| 10-04 04:53:19 | DOGE | down | 0.68→0.53 | 0.83 → 0.83 → 0.83 | 20.28s | DOWN @ 0.17 | -0.30 / 1.83 / · |
| 10-04 04:53:19 | BNB | up | 0.20→0.35 | 0.58 → 0.58 → 0.58 | no | — |  |
| 10-04 04:53:17 | XRP | up | 0.34→0.39 | 0.47 → 0.47 → 0.47 | no | — |  |
| 10-04 04:53:17 | ETH | down | 0.39→0.29 | 0.41 → 0.41 → 0.41 | 7.78s | DOWN @ 0.60 | 0.47 / 1.19 / · |
| 10-04 04:53:15 | BTC | up | 0.22→0.29 | 0.47 → 0.47 → 0.47 | no | — |  |
| 10-04 04:53:02 | XRP | down | 0.45→0.34 | 0.57 → 0.57 → 0.57 | 7.53s | DOWN @ 0.44 | 0.54 / 1.35 / · |
| 10-04 04:52:59 | ZEC | down | 0.68→0.60 | 0.69 → 0.69 → 0.69 | 11.03s | DOWN @ 0.33 | -0.61 / 0.47 / · |
| 10-04 04:52:56 | SOL | down | 0.66→0.59 | 0.76 → 0.76 → 0.76 | no | DOWN @ 0.25 | -0.37 / -0.85 / · |
| 10-04 04:52:50 | HYPE | down | 0.63→0.24 | 0.57 → 0.57 → 0.53 | no | DOWN @ 0.43 | 0.04 / 0.24 / · |
| 10-04 04:52:48 | ETH | down | 0.44→0.35 | 0.45 → 0.45 → 0.45 | 7.03s | DOWN @ 0.56 | 0.05 / -0.05 / · |
| 10-04 04:52:47 | DOGE | down | 0.74→0.68 | 0.86 → 0.86 → 0.86 | 8.03s | DOWN @ 0.14 | 0.11 / 0.01 / · |
| 10-04 04:52:46 | XRP | up | 0.39→0.45 | 0.54 → 0.54 → 0.54 | 8.78s | — |  |
| 10-04 04:52:38 | SOL | down | 0.76→0.66 | 0.86 → 0.86 → 0.69 | 1.77s | DOWN @ 0.14 | 1.36 / 0.78 / · |
| 10-04 04:52:36 | ZEC | down | 0.81→0.76 | 0.86 → 0.86 → 0.79 | 3.28s | DOWN @ 0.15 | 0.10 / 1.26 / · |
| 10-04 04:52:35 | BNB | up | 0.29→0.40 | 0.63 → 0.63 → 0.63 | no | — |  |
| 10-04 04:52:31 | DOGE | up | 0.67→0.73 | 0.85 → 0.85 → 0.85 | no | — |  |
| 10-04 04:52:26 | XRP | down | 0.45→0.40 | 0.56 → 0.58 → 0.58 | no | DOWN @ 0.42 | -0.45 / -0.36 / · |
| 10-04 04:52:20 | ZEC | down | 0.86→0.80 | 0.88 → 0.88 → 0.88 | 20.03s | — |  |
| 10-04 04:51:52 | HYPE | down | 0.58→0.47 | 0.60 → 0.60 → 0.60 | no | DOWN @ 0.40 | -0.44 / -0.74 / · |
