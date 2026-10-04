# Lag Tracker

*Updated Sun Oct 04 08:15 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 622 | 11.1s | 3% | 0% |
| BTC | 493 | 11.9s | 3% | 0% |
| DOGE | 679 | 10.3s | 2% | 0% |
| ETH | 668 | 11.2s | 3% | 0% |
| HYPE | 566 | 11.3s | 4% | 0% |
| NEAR | 658 | 10.8s | 4% | 0% |
| SOL | 1223 | 10.8s | 3% | 0% |
| XRP | 1222 | 10.9s | 3% | 0% |
| ZEC | 816 | 9.5s | 4% | 0% |
| **All** | **6947** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3564 | 1008 | $-402.58 | -2.6% | $-191.28 / $-211.30 |
| Sell after 30 sec | 3564 | 2072 | $1158.14 | +7.5% | $585.97 / $572.17 |
| Hold to the close | 3546 | 1759 | $2287.01 | +14.9% | $1471.39 / $815.62 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **31 ms** · Coinbase price delay: **15 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 08:13:38 | XRP | down | 0.37→0.25 | 0.20 → 0.20 → 0.20 | 5.78s | — |  |
| 10-04 08:13:23 | XRP | up | 0.33→0.39 | 0.12 → 0.12 → 0.12 | 5.78s | UP @ 0.14 | 0.30 / -0.46 / · |
| 10-04 08:13:04 | SOL | down | 0.25→0.16 | 0.22 → 0.22 → 0.22 | 9.78s | DOWN @ 0.79 | 1.00 / -0.45 / · |
| 10-04 08:12:59 | XRP | down | 0.24→0.14 | 0.07 → 0.10 → 0.10 | no | — |  |
| 10-04 08:12:40 | XRP | up | 0.20→0.26 | 0.10 → 0.10 → 0.07 | no | UP @ 0.10 | -0.45 / -0.14 / · |
| 10-04 08:12:34 | SOL | up | 0.06→0.20 | 0.06 → 0.06 → 0.06 | 9.53s | UP @ 0.07 | 0.89 / 1.27 / · |
| 10-04 08:12:20 | XRP | up | 0.16→0.22 | 0.32 → 0.32 → 0.32 | no | — |  |
| 10-04 08:12:15 | SOL | down | 0.22→0.15 | 0.18 → 0.20 → 0.20 | 13.53s | DOWN @ 0.80 | -0.34 / -0.03 / · |
| 10-04 08:12:05 | XRP | down | 0.39→0.29 | 0.27 → 0.27 → 0.27 | 23.79s | — |  |
| 10-04 08:11:50 | XRP | down | 0.40→0.30 | 0.36 → 0.36 → 0.36 | 8.78s | DOWN @ 0.65 | 0.39 / -0.02 / · |
| 10-04 08:11:50 | DOGE | down | 0.28→0.09 | 0.06 → 0.06 → 0.06 | no | — |  |
| 10-04 08:11:37 | SOL | up | 0.12→0.21 | 0.12 → 0.12 → 0.12 | 6.53s | UP @ 0.13 | 0.41 / 0.22 / · |
| 10-04 08:11:25 | XRP | down | 0.47→0.40 | 0.47 → 0.47 → 0.48 | 18.53s | — |  |
| 10-04 08:11:22 | SOL | down | 0.22→0.16 | 0.26 → 0.26 → 0.26 | 6.54s | DOWN @ 0.76 | 0.89 / -0.06 / · |
| 10-04 08:11:10 | XRP | down | 0.59→0.47 | 0.56 → 0.56 → 0.47 | 3.53s | DOWN @ 0.45 | 0.34 / 0.24 / · |
| 10-04 08:11:06 | SOL | down | 0.34→0.26 | 0.27 → 0.27 → 0.27 | 22.55s | — |  |
| 10-04 08:10:55 | ZEC | down | 0.22→0.08 | 0.27 → 0.27 → 0.24 | 18.53s | DOWN @ 0.74 | -0.18 / 1.29 / · |
| 10-04 08:10:52 | XRP | up | 0.56→0.62 | 0.57 → 0.57 → 0.57 | no | — |  |
| 10-04 08:10:51 | SOL | up | 0.21→0.27 | 0.22 → 0.22 → 0.22 | 7.53s | — |  |
| 10-04 08:10:37 | XRP | up | 0.56→0.61 | 0.47 → 0.47 → 0.47 | 6.78s | UP @ 0.47 | 0.64 / 0.44 / · |
| 10-04 08:10:20 | SOL | up | 0.11→0.22 | 0.14 → 0.14 → 0.14 | 23.78s | UP @ 0.15 | 0.01 / 0.39 / · |
| 10-04 08:10:20 | ETH | up | 0.11→0.16 | 0.14 → 0.14 → 0.14 | 24.28s | — |  |
| 10-04 08:10:17 | XRP | up | 0.39→0.45 | 0.32 → 0.32 → 0.32 | 12.03s | UP @ 0.32 | -0.41 / 2.16 / · |
| 10-04 08:10:11 | NEAR | up | 0.87→0.94 | 0.92 → 0.92 → 0.97 | 3.28s | — |  |
| 10-04 08:10:10 | DOGE | up | 0.13→0.20 | 0.06 → 0.06 → 0.08 | 19.03s | UP @ 0.07 | 0.01 / 0.80 / · |
| 10-04 08:10:03 | ZEC | up | 0.10→0.16 | 0.09 → 0.09 → 0.09 | 11.28s | UP @ 0.10 | -0.40 / 1.50 / · |
| 10-04 08:10:00 | SOL | up | 0.09→0.16 | 0.09 → 0.09 → 0.09 | 14.03s | UP @ 0.09 | -0.19 / 0.65 / · |
| 10-04 08:09:59 | BTC | up | 0.42→0.72 | 0.52 → 0.52 → 0.52 | 14.78s | UP @ 0.52 | -0.46 / 3.82 / · |
| 10-04 08:09:59 | XRP | up | 0.29→0.37 | 0.18 → 0.23 → 0.23 | 0.03s | UP @ 0.24 | -0.36 / 0.42 / -2.53 |
| 10-04 08:09:29 | NEAR | up | 0.69→0.83 | 0.74 → 0.89 → 0.89 | 0.27s | — |  |
