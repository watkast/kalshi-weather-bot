# Lag Tracker

*Updated Sun Oct 04 01:03 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 385 | 10.8s | 4% | 0% |
| BTC | 298 | 11.8s | 2% | 0% |
| DOGE | 414 | 10.6s | 2% | 0% |
| ETH | 372 | 11.1s | 3% | 0% |
| HYPE | 290 | 11.8s | 3% | 0% |
| NEAR | 334 | 10.4s | 4% | 0% |
| SOL | 723 | 10.4s | 3% | 0% |
| XRP | 662 | 11.2s | 3% | 0% |
| ZEC | 399 | 9.7s | 5% | 0% |
| **All** | **3877** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2042 | 576 | $-213.30 | -2.4% | $-82.36 / $-130.94 |
| Sell after 30 sec | 2042 | 1196 | $681.74 | +7.8% | $422.08 / $259.66 |
| Hold to the close | 2030 | 1016 | $1425.30 | +16.3% | $815.38 / $609.92 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **38 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 01:03:46 | SOL | down | 0.65→0.59 | 0.72 → 0.72 → — | no | DOWN @ 0.28 | · / · / · |
| 10-04 01:03:44 | XRP | down | 0.31→0.25 | 0.30 → 0.30 → — | no | DOWN @ 0.70 | · / · / · |
| 10-04 01:03:35 | DOGE | up | 0.39→0.50 | 0.49 → 0.49 → 0.49 | no | — |  |
| 10-04 01:03:17 | SOL | up | 0.62→0.68 | 0.67 → 0.68 → 0.68 | 13.93s | — |  |
| 10-04 01:03:15 | ZEC | up | 0.19→0.24 | 0.16 → 0.16 → 0.16 | 15.93s | UP @ 0.17 | -0.39 / 0.56 / · |
| 10-04 01:03:02 | SOL | up | 0.62→0.68 | 0.67 → 0.67 → 0.67 | 28.94s | — |  |
| 10-04 01:02:59 | XRP | down | 0.32→0.26 | 0.31 → 0.31 → 0.29 | no | — |  |
| 10-04 01:02:54 | DOGE | down | 0.50→0.43 | 0.53 → 0.53 → 0.53 | 6.97s | DOWN @ 0.48 | 0.24 / 0.04 / · |
| 10-04 01:02:53 | NEAR | down | 0.36→0.30 | 0.35 → 0.35 → 0.35 | 7.72s | DOWN @ 0.65 | 0.09 / 0.50 / · |
| 10-04 01:02:47 | SOL | up | 0.62→0.68 | 0.67 → 0.67 → 0.67 | no | — |  |
| 10-04 01:02:29 | SOL | up | 0.59→0.65 | 0.60 → 0.60 → 0.67 | 1.94s | — |  |
| 10-04 01:02:14 | SOL | down | 0.59→0.53 | 0.58 → 0.58 → 0.60 | no | — |  |
| 10-04 01:02:04 | XRP | up | 0.27→0.32 | 0.29 → 0.29 → 0.29 | 12.19s | — |  |
| 10-04 01:02:02 | HYPE | down | 0.57→0.49 | 0.62 → 0.62 → 0.62 | no | DOWN @ 0.38 | -0.44 / -0.14 / · |
| 10-04 01:02:01 | ETH | up | 0.29→0.35 | 0.35 → 0.30 → 0.30 | no | — |  |
| 10-04 01:01:58 | SOL | down | 0.59→0.53 | 0.68 → 0.68 → 0.58 | 2.94s | DOWN @ 0.33 | 0.37 / 0.27 / · |
| 10-04 01:01:54 | ZEC | down | 0.28→0.21 | 0.27 → 0.27 → 0.27 | 7.45s | — |  |
| 10-04 01:01:50 | BNB | down | 0.41→0.35 | 0.51 → 0.51 → 0.51 | 11.45s | DOWN @ 0.50 | -0.46 / 0.55 / · |
| 10-04 01:01:43 | SOL | down | 0.69→0.62 | 0.69 → 0.69 → 0.68 | 18.20s | DOWN @ 0.32 | -0.32 / 0.47 / · |
| 10-04 01:01:35 | DOGE | down | 0.57→0.46 | 0.64 → 0.64 → 0.64 | 10.70s | DOWN @ 0.37 | -0.53 / 0.95 / · |
| 10-04 01:01:34 | NEAR | down | 0.52→0.46 | 0.57 → 0.57 → 0.57 | 11.95s | DOWN @ 0.44 | -0.65 / 0.64 / · |
| 10-04 01:01:34 | ETH | down | 0.52→0.46 | 0.54 → 0.54 → 0.54 | 12.45s | DOWN @ 0.47 | -0.56 / 1.87 / · |
| 10-04 01:01:21 | XRP | down | 0.57→0.50 | 0.62 → 0.62 → 0.62 | 7.70s | DOWN @ 0.38 | -0.04 / 1.76 / · |
| 10-04 01:01:18 | BNB | down | 0.54→0.41 | 0.68 → 0.68 → 0.68 | 11.20s | DOWN @ 0.33 | -0.42 / 1.26 / · |
| 10-04 01:01:00 | BNB | up | 0.48→0.54 | 0.55 → 0.55 → 0.55 | 13.95s | — |  |
| 10-04 01:00:57 | XRP | up | 0.43→0.50 | 0.48 → 0.48 → 0.49 | 16.71s | — |  |
| 10-04 01:00:39 | XRP | up | 0.41→0.48 | 0.48 → 0.48 → 0.48 | no | — |  |
| 10-04 00:58:35 | BNB | up | 0.17→0.28 | 0.59 → 0.59 → 0.90 | 2.73s | — |  |
| 10-04 00:58:31 | ZEC | up | 0.03→0.12 | 0.03 → 0.03 → 0.03 | 22.24s | — |  |
| 10-04 00:58:12 | BNB | down | 0.38→0.24 | 0.81 → 0.81 → 0.81 | 10.74s | — |  |
