# Lag Tracker

*Updated Sat Oct 03 19:22 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 156 | 10.8s | 6% | 0% |
| BTC | 91 | 10.7s | 3% | 0% |
| DOGE | 103 | 9.3s | 4% | 0% |
| ETH | 84 | 10.8s | 2% | 0% |
| HYPE | 73 | 11.7s | 3% | 0% |
| NEAR | 105 | 9.2s | 5% | 0% |
| SOL | 191 | 8.4s | 6% | 0% |
| XRP | 156 | 9.2s | 8% | 0% |
| ZEC | 141 | 9.4s | 6% | 0% |
| **All** | **1100** | **9.6s** | **5%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 584 | 201 | $-28.03 | -1.2% | $-7.28 / $-20.75 |
| Sell after 30 sec | 582 | 387 | $298.00 | +12.4% | $151.76 / $146.24 |
| Hold to the close | 521 | 269 | $550.81 | +25.7% | $229.07 / $321.74 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 19:22:40 | ZEC | up | 0.69→0.81 | 0.69 → 0.69 → — | no | UP @ 0.70 | · / · / · |
| 10-03 19:22:38 | SOL | down | 0.48→0.34 | 0.49 → 0.49 → — | no | DOWN @ 0.51 | · / · / · |
| 10-03 19:22:38 | HYPE | down | 0.22→0.15 | 0.20 → 0.20 → — | no | — |  |
| 10-03 19:22:34 | BNB | up | 0.73→0.82 | 0.68 → 0.71 → 0.71 | no | UP @ 0.72 | · / · / · |
| 10-03 19:22:30 | XRP | down | 0.23→0.16 | 0.32 → 0.32 → 0.33 | no | DOWN @ 0.69 | -0.61 / · / · |
| 10-03 19:22:30 | NEAR | up | 0.86→0.92 | 0.90 → 0.90 → 0.92 | no | — |  |
| 10-03 19:22:20 | SOL | up | 0.39→0.48 | 0.51 → 0.51 → 0.51 | no | — |  |
| 10-03 19:22:15 | HYPE | down | 0.20→0.14 | 0.20 → 0.20 → 0.20 | no | DOWN @ 0.81 | -0.33 / · / · |
| 10-03 19:22:05 | ZEC | up | 0.67→0.72 | 0.65 → 0.69 → 0.69 | 0.02s | — |  |
| 10-03 19:22:04 | SOL | down | 0.48→0.39 | 0.51 → 0.51 → 0.51 | no | DOWN @ 0.50 | -0.46 / -0.36 / · |
| 10-03 19:21:52 | BNB | up | 0.54→0.71 | 0.61 → 0.61 → 0.61 | no | UP @ 0.62 | -0.54 / 0.17 / · |
| 10-03 19:21:41 | ZEC | down | 0.64→0.59 | 0.47 → 0.47 → 0.47 | no | — |  |
| 10-03 19:21:38 | SOL | up | 0.39→0.48 | 0.51 → 0.51 → 0.51 | no | — |  |
| 10-03 19:21:37 | BNB | down | 0.89→0.80 | 0.90 → 0.90 → 0.90 | 10.61s | DOWN @ 0.11 | -0.24 / 1.68 / · |
| 10-03 19:21:26 | NEAR | up | 0.76→0.85 | 0.76 → 0.76 → 0.76 | 6.81s | UP @ 0.77 | 0.37 / 0.26 / · |
| 10-03 19:21:23 | SOL | down | 0.61→0.48 | 0.59 → 0.59 → 0.59 | 9.56s | DOWN @ 0.41 | 0.45 / 0.35 / · |
| 10-03 19:21:21 | ZEC | up | 0.47→0.53 | 0.55 → 0.55 → 0.55 | 26.87s | — |  |
| 10-03 19:21:06 | ZEC | up | 0.42→0.48 | 0.42 → 0.42 → 0.42 | 11.81s | UP @ 0.43 | -0.55 / -0.06 / · |
| 10-03 19:21:05 | SOL | down | 0.56→0.48 | 0.59 → 0.59 → 0.59 | 28.07s | DOWN @ 0.41 | -0.44 / 0.45 / · |
| 10-03 19:21:04 | BNB | up | 0.70→0.79 | 0.62 → 0.72 → 0.72 | 0.02s | UP @ 0.73 | -0.39 / 1.39 / · |
| 10-03 19:20:58 | NEAR | up | 0.67→0.72 | 0.70 → 0.70 → 0.76 | 4.14s | — |  |
| 10-03 19:20:56 | XRP | up | 0.21→0.27 | 0.33 → 0.33 → 0.33 | 6.64s | — |  |
| 10-03 19:20:51 | ZEC | down | 0.54→0.47 | 0.55 → 0.55 → 0.55 | 11.39s | DOWN @ 0.47 | -0.66 / -0.56 / · |
| 10-03 19:20:49 | SOL | down | 0.60→0.52 | 0.59 → 0.59 → 0.59 | no | DOWN @ 0.41 | -0.44 / -0.44 / · |
| 10-03 19:20:46 | BNB | down | 0.68→0.62 | 0.64 → 0.64 → 0.62 | no | — |  |
| 10-03 19:20:46 | HYPE | down | 0.30→0.23 | 0.30 → 0.30 → 0.31 | 16.40s | DOWN @ 0.70 | -0.51 / 0.01 / · |
| 10-03 19:20:43 | DOGE | down | 0.54→0.47 | 0.49 → 0.49 → 0.49 | no | — |  |
| 10-03 19:20:41 | ETH | down | 0.20→0.14 | 0.26 → 0.26 → 0.26 | no | DOWN @ 0.75 | -0.07 / -0.28 / · |
| 10-03 19:20:33 | NEAR | down | 0.67→0.61 | 0.71 → 0.71 → 0.71 | no | DOWN @ 0.29 | -0.40 / -0.88 / · |
| 10-03 19:20:32 | SOL | up | 0.60→0.68 | 0.59 → 0.59 → 0.62 | no | UP @ 0.60 | -0.14 / -0.44 / · |
