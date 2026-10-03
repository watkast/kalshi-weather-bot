# Lag Tracker

*Updated Sat Oct 03 22:03 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 262 | 10.7s | 5% | 0% |
| BTC | 171 | 12.4s | 2% | 0% |
| DOGE | 268 | 10.2s | 2% | 0% |
| ETH | 225 | 11.3s | 3% | 0% |
| HYPE | 190 | 11.2s | 4% | 0% |
| NEAR | 199 | 10.5s | 4% | 0% |
| SOL | 421 | 9.4s | 4% | 0% |
| XRP | 404 | 10.3s | 4% | 0% |
| ZEC | 283 | 9.6s | 5% | 0% |
| **All** | **2423** | **10.6s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1267 | 372 | $-120.55 | -2.3% | $-45.26 / $-75.29 |
| Sell after 30 sec | 1264 | 766 | $482.11 | +9.1% | $290.79 / $191.32 |
| Hold to the close | 1243 | 623 | $1014.71 | +19.5% | $581.00 / $433.71 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **38 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 22:03:36 | DOGE | up | 0.35→0.45 | 0.31 → 0.31 → 0.31 | no | UP @ 0.32 | · / · / · |
| 10-03 22:03:36 | SOL | up | 0.24→0.30 | 0.39 → 0.39 → 0.39 | no | — |  |
| 10-03 22:03:35 | BTC | up | 0.56→0.61 | 0.62 → 0.62 → 0.62 | no | — |  |
| 10-03 22:03:35 | XRP | down | 0.50→0.40 | 0.43 → 0.43 → 0.43 | no | — |  |
| 10-03 22:03:34 | ETH | down | 0.61→0.53 | 0.54 → 0.54 → 0.54 | no | — |  |
| 10-03 22:03:21 | BNB | up | 0.49→0.61 | 0.56 → 0.56 → 0.56 | 9.87s | — |  |
| 10-03 22:03:20 | SOL | up | 0.20→0.27 | 0.32 → 0.32 → 0.32 | 10.37s | — |  |
| 10-03 22:03:20 | NEAR | up | 0.39→0.46 | 0.54 → 0.54 → 0.54 | no | — |  |
| 10-03 22:03:19 | ETH | up | 0.48→0.56 | 0.35 → 0.35 → 0.35 | 11.87s | UP @ 0.36 | -0.43 / · / · |
| 10-03 22:03:19 | DOGE | up | 0.22→0.32 | 0.34 → 0.34 → 0.34 | no | — |  |
| 10-03 22:03:18 | XRP | up | 0.19→0.27 | 0.17 → 0.17 → 0.17 | 12.37s | UP @ 0.17 | -0.30 / · / · |
| 10-03 22:03:18 | BTC | up | 0.49→0.58 | 0.49 → 0.49 → 0.49 | 12.37s | UP @ 0.50 | -0.46 / · / · |
| 10-03 22:03:06 | BNB | down | 0.63→0.52 | 0.60 → 0.60 → 0.60 | no | DOWN @ 0.40 | -0.05 / -1.32 / · |
| 10-03 22:03:05 | NEAR | down | 0.49→0.43 | 0.57 → 0.57 → 0.57 | 10.62s | DOWN @ 0.44 | -0.65 / -0.36 / · |
| 10-03 22:03:03 | SOL | up | 0.14→0.43 | 0.30 → 0.30 → 0.30 | no | — |  |
| 10-03 22:03:03 | XRP | down | 0.31→0.25 | 0.40 → 0.41 → 0.41 | 12.37s | DOWN @ 0.59 | -0.45 / -0.65 / · |
| 10-03 22:03:03 | ETH | up | 0.40→0.47 | 0.48 → 0.48 → 0.48 | 27.38s | — |  |
| 10-03 22:03:03 | BTC | up | 0.46→0.53 | 0.51 → 0.51 → 0.51 | 27.38s | — |  |
| 10-03 22:03:03 | DOGE | up | 0.25→0.33 | 0.29 → 0.29 → 0.29 | no | — |  |
| 10-03 22:02:47 | ZEC | down | 0.14→0.09 | 0.16 → 0.14 → 0.14 | 13.62s | — |  |
| 10-03 22:02:45 | BNB | down | 0.65→0.56 | 0.71 → 0.71 → 0.71 | 16.12s | DOWN @ 0.29 | -0.40 / 0.68 / · |
| 10-03 22:02:42 | NEAR | down | 0.57→0.49 | 0.69 → 0.69 → 0.56 | 3.39s | DOWN @ 0.33 | 0.56 / 0.47 / · |
| 10-03 22:02:42 | SOL | down | 0.58→0.49 | 0.67 → 0.67 → 0.67 | 18.62s | DOWN @ 0.34 | -0.42 / 3.19 / · |
| 10-03 22:02:42 | ETH | down | 0.69→0.58 | 0.73 → 0.73 → 0.41 | 3.64s | DOWN @ 0.27 | 2.89 / 2.08 / · |
| 10-03 22:02:42 | BTC | down | 0.66→0.49 | 0.71 → 0.71 → 0.68 | 18.62s | DOWN @ 0.29 | -0.01 / 1.67 / · |
| 10-03 22:02:40 | XRP | up | 0.57→0.63 | 0.72 → 0.72 → 0.72 | no | — |  |
| 10-03 22:02:35 | DOGE | down | 0.61→0.55 | 0.64 → 0.64 → 0.64 | 10.89s | DOWN @ 0.37 | -0.53 / 2.98 / · |
| 10-03 22:02:31 | HYPE | up | 0.64→0.70 | 0.69 → 0.69 → 0.69 | no | — |  |
| 10-03 22:02:21 | ETH | down | 0.76→0.69 | 0.76 → 0.76 → 0.76 | 24.90s | DOWN @ 0.25 | -0.18 / 3.09 / · |
| 10-03 22:02:20 | ZEC | down | 0.25→0.19 | 0.23 → 0.23 → 0.23 | 10.63s | — |  |
