# Lag Tracker

*Updated Sat Oct 03 21:03 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 219 | 10.6s | 6% | 0% |
| BTC | 139 | 11.6s | 2% | 0% |
| DOGE | 218 | 10.1s | 2% | 0% |
| ETH | 155 | 10.8s | 3% | 0% |
| HYPE | 141 | 11.6s | 4% | 0% |
| NEAR | 152 | 9.5s | 4% | 0% |
| SOL | 326 | 9.1s | 4% | 0% |
| XRP | 335 | 10.1s | 5% | 0% |
| ZEC | 225 | 9.7s | 5% | 0% |
| **All** | **1910** | **10.2s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 982 | 309 | $-83.32 | -2.0% | $-15.35 / $-67.97 |
| Sell after 30 sec | 977 | 613 | $395.72 | +9.5% | $270.96 / $124.76 |
| Hold to the close | 965 | 480 | $690.07 | +16.8% | $534.41 / $155.66 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 21:03:12 | HYPE | down | 0.83→0.75 | 0.83 → 0.83 → 0.83 | no | DOWN @ 0.18 | · / · / · |
| 10-03 21:03:05 | BNB | down | 0.76→0.70 | 0.82 → 0.82 → 0.82 | 14.30s | DOWN @ 0.18 | -0.31 / · / · |
| 10-03 21:03:00 | ETH | down | 0.64→0.56 | 0.64 → 0.64 → 0.59 | 4.53s | DOWN @ 0.37 | -0.04 / · / · |
| 10-03 21:03:00 | XRP | down | 0.55→0.48 | 0.61 → 0.61 → 0.61 | 19.55s | DOWN @ 0.40 | -0.54 / · / · |
| 10-03 21:03:00 | NEAR | down | 0.63→0.58 | 0.74 → 0.74 → 0.72 | 19.80s | DOWN @ 0.28 | -0.39 / · / · |
| 10-03 21:02:59 | SOL | down | 0.66→0.60 | 0.71 → 0.71 → 0.71 | 21.05s | DOWN @ 0.29 | -0.30 / · / · |
| 10-03 21:02:52 | DOGE | up | 0.30→0.40 | 0.46 → 0.46 → 0.46 | no | — |  |
| 10-03 21:02:37 | DOGE | down | 0.43→0.30 | 0.47 → 0.45 → 0.45 | no | DOWN @ 0.56 | -0.46 / -0.56 / · |
| 10-03 21:02:25 | SOL | down | 0.65→0.60 | 0.67 → 0.67 → 0.67 | no | DOWN @ 0.34 | -0.52 / -0.91 / · |
| 10-03 21:02:21 | XRP | down | 0.62→0.55 | 0.67 → 0.67 → 0.67 | 13.78s | DOWN @ 0.34 | -0.42 / 0.07 / · |
| 10-03 21:02:04 | ETH | down | 0.75→0.60 | 0.72 → 0.76 → 0.76 | 15.54s | DOWN @ 0.25 | -0.37 / 0.60 / · |
| 10-03 21:02:04 | HYPE | down | 0.91→0.82 | 0.89 → 0.89 → 0.90 | no | DOWN @ 0.12 | -0.35 / -0.35 / · |
| 10-03 21:02:02 | BNB | down | 0.77→0.71 | 0.79 → 0.79 → 0.82 | no | DOWN @ 0.22 | -0.73 / -0.64 / · |
| 10-03 21:02:02 | BTC | down | 0.69→0.54 | 0.74 → 0.74 → 0.77 | 18.04s | DOWN @ 0.26 | -0.57 / 1.28 / · |
| 10-03 21:02:02 | XRP | down | 0.72→0.54 | 0.79 → 0.79 → 0.78 | 18.04s | DOWN @ 0.22 | -0.26 / 0.81 / · |
| 10-03 21:02:02 | ZEC | down | 0.78→0.69 | 0.83 → 0.83 → 0.85 | 18.04s | DOWN @ 0.18 | -0.60 / 0.36 / · |
| 10-03 21:02:02 | SOL | down | 0.76→0.70 | 0.79 → 0.79 → 0.60 | 3.03s | DOWN @ 0.22 | 1.40 / 0.81 / · |
| 10-03 21:01:57 | DOGE | up | 0.40→0.47 | 0.51 → 0.51 → 0.51 | 7.29s | — |  |
| 10-03 21:01:57 | NEAR | up | 0.62→0.68 | 0.80 → 0.80 → 0.80 | no | — |  |
| 10-03 21:01:44 | ZEC | up | 0.72→0.79 | 0.74 → 0.74 → 0.74 | 5.79s | — |  |
| 10-03 21:01:42 | BTC | up | 0.63→0.69 | 0.70 → 0.70 → 0.70 | 7.29s | — |  |
| 10-03 21:01:42 | NEAR | up | 0.57→0.63 | 0.61 → 0.61 → 0.61 | 7.79s | — |  |
| 10-03 21:01:42 | SOL | up | 0.65→0.74 | 0.70 → 0.70 → 0.70 | 7.79s | — |  |
| 10-03 21:01:42 | DOGE | up | 0.41→0.50 | 0.49 → 0.49 → 0.49 | 23.04s | — |  |
| 10-03 21:01:42 | ETH | up | 0.59→0.66 | 0.61 → 0.61 → 0.61 | 8.04s | — |  |
| 10-03 21:01:36 | XRP | up | 0.62→0.68 | 0.74 → 0.74 → 0.74 | 13.29s | — |  |
| 10-03 21:01:35 | HYPE | up | 0.63→0.77 | 0.77 → 0.75 → 0.75 | 14.79s | — |  |
| 10-03 21:01:24 | NEAR | up | 0.49→0.56 | 0.59 → 0.59 → 0.59 | 25.79s | — |  |
| 10-03 21:01:20 | SOL | down | 0.65→0.59 | 0.69 → 0.69 → 0.69 | no | DOWN @ 0.31 | -0.40 / -1.27 / · |
| 10-03 21:01:01 | XRP | up | 0.48→0.54 | 0.55 → 0.55 → 0.56 | 18.30s | — |  |
