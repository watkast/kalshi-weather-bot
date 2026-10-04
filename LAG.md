# Lag Tracker

*Updated Sun Oct 04 08:05 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 619 | 10.8s | 3% | 0% |
| BTC | 485 | 11.9s | 3% | 0% |
| DOGE | 676 | 10.3s | 2% | 0% |
| ETH | 661 | 11.2s | 3% | 0% |
| HYPE | 566 | 11.3s | 4% | 0% |
| NEAR | 650 | 10.8s | 4% | 0% |
| SOL | 1210 | 10.8s | 3% | 0% |
| XRP | 1201 | 10.9s | 3% | 0% |
| ZEC | 809 | 9.5s | 4% | 0% |
| **All** | **6877** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3526 | 989 | $-405.09 | -2.7% | $-186.62 / $-218.47 |
| Sell after 30 sec | 3525 | 2044 | $1138.43 | +7.5% | $571.47 / $566.96 |
| Hold to the close | 3485 | 1731 | $2286.19 | +15.2% | $1412.20 / $873.99 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **31 ms** · Coinbase price delay: **15 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 08:05:01 | NEAR | up | 0.62→0.69 | 0.78 → 0.71 → 0.71 | no | — |  |
| 10-04 08:05:01 | XRP | up | 0.42→0.50 | 0.41 → 0.41 → 0.41 | no | UP @ 0.41 | -0.44 / · / · |
| 10-04 08:04:53 | ZEC | down | 0.29→0.23 | 0.26 → 0.26 → 0.26 | no | — |  |
| 10-04 08:04:43 | SOL | down | 0.55→0.50 | 0.55 → 0.55 → 0.56 | 15.98s | — |  |
| 10-04 08:04:40 | ETH | down | 0.14→0.07 | 0.23 → 0.23 → 0.21 | no | DOWN @ 0.78 | -0.26 / -0.15 / · |
| 10-04 08:04:36 | HYPE | up | 0.71→0.81 | 0.78 → 0.78 → 0.78 | 22.23s | — |  |
| 10-04 08:04:25 | ZEC | up | 0.26→0.32 | 0.28 → 0.28 → 0.28 | no | — |  |
| 10-04 08:04:22 | XRP | down | 0.50→0.43 | 0.47 → 0.47 → 0.47 | no | — |  |
| 10-04 08:04:21 | HYPE | up | 0.65→0.71 | 0.68 → 0.68 → 0.68 | 7.23s | — |  |
| 10-04 08:04:14 | NEAR | up | 0.48→0.56 | 0.68 → 0.68 → 0.68 | 29.74s | — |  |
| 10-04 08:04:03 | ETH | up | 0.16→0.22 | 0.23 → 0.23 → 0.23 | 10.74s | — |  |
| 10-04 08:04:02 | XRP | up | 0.41→0.47 | 0.38 → 0.38 → 0.38 | 11.74s | UP @ 0.38 | -0.44 / 0.45 / · |
| 10-04 08:03:53 | BTC | down | 0.60→0.52 | 0.68 → 0.68 → 0.68 | no | DOWN @ 0.33 | -0.03 / -0.61 / · |
| 10-04 08:03:48 | SOL | down | 0.59→0.52 | 0.59 → 0.59 → 0.59 | 10.74s | DOWN @ 0.41 | -0.44 / 0.05 / · |
| 10-04 08:03:47 | ETH | down | 0.30→0.16 | 0.35 → 0.35 → 0.35 | 11.24s | DOWN @ 0.66 | -0.53 / 0.09 / · |
| 10-04 08:03:44 | XRP | up | 0.40→0.46 | 0.67 → 0.48 → 0.48 | no | — |  |
| 10-04 08:03:40 | HYPE | up | 0.54→0.65 | 0.59 → 0.59 → 0.59 | no | UP @ 0.60 | -0.55 / -0.44 / · |
| 10-04 08:03:34 | NEAR | down | 0.67→0.57 | 0.79 → 0.79 → 0.79 | 9.49s | DOWN @ 0.23 | 1.79 / 1.40 / · |
| 10-04 08:03:34 | ZEC | down | 0.43→0.33 | 0.45 → 0.45 → 0.45 | 9.74s | DOWN @ 0.56 | 0.97 / 1.27 / · |
| 10-04 08:03:34 | DOGE | down | 0.43→0.32 | 0.42 → 0.42 → 0.42 | 9.99s | DOWN @ 0.58 | 0.97 / 1.38 / · |
| 10-04 08:03:32 | ETH | down | 0.37→0.31 | 0.39 → 0.39 → 0.39 | 11.24s | DOWN @ 0.62 | -0.44 / 1.10 / · |
| 10-04 08:03:32 | BTC | down | 0.82→0.75 | 0.82 → 0.82 → 0.82 | 11.99s | DOWN @ 0.18 | -0.31 / 1.52 / · |
| 10-04 08:03:31 | SOL | down | 0.77→0.72 | 0.70 → 0.74 → 0.74 | 12.99s | — |  |
| 10-04 08:03:29 | XRP | down | 0.64→0.59 | 0.60 → 0.67 → 0.67 | 14.49s | DOWN @ 0.34 | -0.52 / 2.47 / · |
| 10-04 08:03:16 | HYPE | up | 0.48→0.59 | 0.60 → 0.60 → 0.60 | no | — |  |
| 10-04 08:03:12 | ZEC | up | 0.33→0.40 | 0.31 → 0.31 → 0.37 | 1.74s | UP @ 0.32 | 0.07 / 0.86 / · |
| 10-04 08:03:07 | NEAR | up | 0.49→0.61 | 0.62 → 0.62 → 0.62 | 6.99s | — |  |
| 10-04 08:03:06 | DOGE | up | 0.30→0.43 | 0.28 → 0.28 → 0.28 | 7.99s | UP @ 0.28 | 0.68 / 1.07 / · |
| 10-04 08:03:01 | SOL | up | 0.68→0.75 | 0.68 → 0.68 → 0.68 | 27.25s | UP @ 0.68 | -0.42 / 0.30 / · |
| 10-04 08:03:01 | XRP | up | 0.51→0.60 | 0.48 → 0.48 → 0.48 | 12.75s | UP @ 0.49 | -0.46 / 1.36 / · |
