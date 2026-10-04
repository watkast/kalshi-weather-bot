# Lag Tracker

*Updated Sun Oct 04 08:25 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 627 | 11.1s | 3% | 0% |
| BTC | 501 | 11.8s | 3% | 0% |
| DOGE | 689 | 10.3s | 2% | 0% |
| ETH | 671 | 11.1s | 3% | 0% |
| HYPE | 570 | 11.2s | 4% | 0% |
| NEAR | 665 | 10.8s | 4% | 0% |
| SOL | 1236 | 10.8s | 3% | 0% |
| XRP | 1237 | 10.9s | 3% | 0% |
| ZEC | 828 | 9.6s | 4% | 0% |
| **All** | **7024** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3610 | 1018 | $-409.24 | -2.6% | $-188.95 / $-220.29 |
| Sell after 30 sec | 3608 | 2095 | $1165.99 | +7.5% | $593.71 / $572.28 |
| Hold to the close | 3564 | 1766 | $2287.01 | +14.9% | $1483.63 / $803.38 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **15 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 08:25:18 | XRP | down | 0.62→0.56 | 0.58 → 0.58 → — | no | — |  |
| 10-04 08:25:06 | DOGE | up | 0.26→0.49 | 0.24 → 0.24 → 0.24 | no | UP @ 0.25 | -0.28 / · / · |
| 10-04 08:25:05 | ZEC | down | 0.33→0.26 | 0.25 → 0.25 → 0.25 | no | — |  |
| 10-04 08:25:00 | XRP | up | 0.41→0.50 | 0.40 → 0.40 → 0.40 | 12.28s | UP @ 0.40 | -0.44 / · / · |
| 10-04 08:24:40 | BTC | down | 0.44→0.38 | 0.43 → 0.43 → 0.29 | 2.53s | DOWN @ 0.57 | 0.97 / 0.56 / · |
| 10-04 08:24:40 | BNB | down | 0.24→0.15 | 0.47 → 0.47 → 0.46 | 17.78s | DOWN @ 0.54 | -0.36 / 0.45 / · |
| 10-04 08:24:38 | ETH | down | 0.29→0.23 | 0.20 → 0.20 → 0.20 | 5.03s | — |  |
| 10-04 08:24:15 | XRP | up | 0.35→0.42 | 0.36 → 0.36 → 0.36 | 12.58s | UP @ 0.37 | -0.44 / -0.24 / · |
| 10-04 08:24:14 | SOL | up | 0.32→0.39 | 0.32 → 0.32 → 0.32 | 14.08s | UP @ 0.33 | -0.51 / 1.16 / · |
| 10-04 08:24:00 | NEAR | up | 0.22→0.29 | 0.23 → 0.23 → 0.23 | no | — |  |
| 10-04 08:23:59 | DOGE | down | 0.38→0.32 | 0.31 → 0.30 → 0.30 | 13.31s | — |  |
| 10-04 08:23:56 | ZEC | up | 0.17→0.22 | 0.26 → 0.26 → 0.26 | no | — |  |
| 10-04 08:23:55 | SOL | up | 0.26→0.32 | 0.29 → 0.29 → 0.28 | no | — |  |
| 10-04 08:23:40 | HYPE | down | 0.92→0.86 | 0.91 → 0.91 → 0.89 | no | DOWN @ 0.10 | -0.02 / -0.02 / · |
| 10-04 08:23:35 | DOGE | up | 0.32→0.39 | 0.28 → 0.28 → 0.28 | 7.58s | UP @ 0.28 | -0.20 / -0.30 / · |
| 10-04 08:23:26 | XRP | down | 0.47→0.40 | 0.43 → 0.43 → 0.43 | 16.83s | — |  |
| 10-04 08:23:19 | ETH | up | 0.11→0.16 | 0.09 → 0.09 → 0.09 | 8.57s | UP @ 0.09 | 0.29 / 0.48 / · |
| 10-04 08:23:17 | SOL | down | 0.34→0.29 | 0.29 → 0.29 → 0.29 | no | — |  |
| 10-04 08:23:12 | ZEC | up | 0.23→0.32 | 0.20 → 0.20 → 0.19 | 15.82s | UP @ 0.21 | -0.62 / 0.24 / · |
| 10-04 08:23:06 | NEAR | down | 0.35→0.27 | 0.33 → 0.33 → 0.33 | 6.32s | DOWN @ 0.68 | 0.09 / -0.42 / · |
| 10-04 08:22:57 | DOGE | up | 0.24→0.36 | 0.23 → 0.23 → 0.23 | no | UP @ 0.23 | -0.36 / -0.07 / · |
| 10-04 08:22:55 | XRP | down | 0.50→0.45 | 0.45 → 0.45 → 0.46 | no | — |  |
| 10-04 08:22:51 | NEAR | up | 0.28→0.35 | 0.33 → 0.33 → 0.33 | no | — |  |
| 10-04 08:22:45 | BNB | down | 0.51→0.38 | 0.69 → 0.69 → 0.69 | 12.83s | DOWN @ 0.31 | -0.40 / -0.01 / · |
| 10-04 08:22:40 | SOL | down | 0.35→0.30 | 0.34 → 0.34 → 0.32 | 17.33s | — |  |
| 10-04 08:22:40 | XRP | up | 0.43→0.50 | 0.24 → 0.24 → 0.45 | 2.33s | UP @ 0.25 | 1.58 / 1.68 / · |
| 10-04 08:22:38 | BTC | up | 0.39→0.45 | 0.28 → 0.28 → 0.40 | 4.33s | UP @ 0.29 | 0.68 / 1.17 / · |
| 10-04 08:22:30 | BNB | up | 0.25→0.35 | 0.47 → 0.48 → 0.48 | 12.83s | — |  |
| 10-04 08:22:25 | XRP | up | 0.30→0.36 | 0.23 → 0.23 → 0.24 | 17.33s | UP @ 0.23 | -0.16 / 1.79 / · |
| 10-04 08:22:23 | BTC | up | 0.29→0.37 | 0.28 → 0.28 → 0.28 | 19.33s | UP @ 0.28 | -0.30 / 0.78 / · |
