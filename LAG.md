# Lag Tracker

*Updated Sun Oct 04 02:24 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 437 | 10.6s | 4% | 0% |
| BTC | 350 | 12.2s | 2% | 0% |
| DOGE | 466 | 10.5s | 2% | 0% |
| ETH | 432 | 11.2s | 3% | 0% |
| HYPE | 346 | 11.6s | 3% | 0% |
| NEAR | 390 | 10.7s | 4% | 0% |
| SOL | 847 | 10.8s | 3% | 0% |
| XRP | 764 | 11.2s | 3% | 0% |
| ZEC | 486 | 9.7s | 5% | 0% |
| **All** | **4518** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2362 | 659 | $-268.40 | -2.6% | $-120.26 / $-148.14 |
| Sell after 30 sec | 2357 | 1371 | $755.74 | +7.4% | $438.68 / $317.06 |
| Hold to the close | 2301 | 1154 | $1662.62 | +16.8% | $929.35 / $733.27 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **38 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 02:24:02 | BNB | down | 0.38→0.25 | 0.53 → 0.53 → — | no | DOWN @ 0.49 | · / · / · |
| 10-04 02:24:00 | XRP | down | 0.39→0.29 | 0.48 → 0.48 → — | no | DOWN @ 0.52 | · / · / · |
| 10-04 02:23:54 | SOL | down | 0.28→0.20 | 0.33 → 0.33 → 0.33 | no | DOWN @ 0.68 | · / · / · |
| 10-04 02:23:53 | HYPE | down | 0.84→0.79 | 0.90 → 0.90 → 0.90 | no | DOWN @ 0.10 | -0.15 / · / · |
| 10-04 02:23:53 | ZEC | down | 0.77→0.72 | 0.82 → 0.82 → 0.82 | no | DOWN @ 0.19 | -0.51 / · / · |
| 10-04 02:23:49 | ETH | down | 0.73→0.62 | 0.79 → 0.79 → 0.70 | 1.53s | DOWN @ 0.22 | 0.42 / · / · |
| 10-04 02:23:44 | XRP | down | 0.50→0.39 | 0.59 → 0.59 → 0.59 | 6.53s | DOWN @ 0.41 | 0.65 / · / · |
| 10-04 02:23:41 | BTC | down | 0.85→0.73 | 0.84 → 0.84 → 0.84 | no | DOWN @ 0.16 | 0.18 / · / · |
| 10-04 02:23:34 | SOL | up | 0.25→0.33 | 0.47 → 0.47 → 0.39 | no | — |  |
| 10-04 02:23:25 | XRP | down | 0.60→0.53 | 0.70 → 0.70 → 0.70 | 11.04s | DOWN @ 0.31 | -0.50 / 1.67 / · |
| 10-04 02:23:19 | SOL | down | 0.38→0.29 | 0.23 → 0.23 → 0.47 | no | — |  |
| 10-04 02:23:12 | HYPE | up | 0.85→0.92 | 0.91 → 0.91 → 0.91 | 23.79s | — |  |
| 10-04 02:23:10 | XRP | up | 0.53→0.60 | 0.49 → 0.49 → 0.49 | 11.05s | UP @ 0.50 | -0.46 / 0.55 / · |
| 10-04 02:23:04 | BTC | up | 0.63→0.77 | 0.72 → 0.72 → 0.73 | 17.06s | UP @ 0.73 | -0.28 / 0.76 / · |
| 10-04 02:23:04 | SOL | up | 0.12→0.22 | 0.23 → 0.23 → 0.23 | 17.31s | — |  |
| 10-04 02:23:03 | ETH | up | 0.54→0.72 | 0.59 → 0.59 → 0.57 | 17.56s | UP @ 0.60 | -0.65 / 1.30 / · |
| 10-04 02:23:03 | BNB | up | 0.17→0.31 | 0.26 → 0.26 → 0.39 | 3.03s | — |  |
| 10-04 02:22:55 | XRP | up | 0.40→0.47 | 0.47 → 0.47 → 0.47 | 26.06s | — |  |
| 10-04 02:22:39 | XRP | down | 0.40→0.31 | 0.42 → 0.42 → 0.42 | no | DOWN @ 0.58 | -0.46 / -1.16 / · |
| 10-04 02:22:33 | BNB | up | 0.22→0.29 | 0.20 → 0.20 → 0.32 | 3.03s | UP @ 0.21 | 0.73 / -0.05 / · |
| 10-04 02:22:19 | ETH | up | 0.41→0.48 | 0.47 → 0.47 → 0.41 | 16.54s | — |  |
| 10-04 02:22:18 | BNB | up | 0.06→0.22 | 0.22 → 0.22 → 0.20 | 18.04s | — |  |
| 10-04 02:22:17 | XRP | up | 0.34→0.40 | 0.40 → 0.40 → 0.41 | 18.79s | — |  |
| 10-04 02:22:17 | BTC | up | 0.47→0.62 | 0.51 → 0.51 → 0.51 | 19.04s | UP @ 0.51 | -0.46 / 0.75 / · |
| 10-04 02:22:17 | SOL | up | 0.09→0.16 | 0.14 → 0.14 → 0.20 | 4.03s | — |  |
| 10-04 02:22:14 | ZEC | up | 0.55→0.61 | 0.57 → 0.57 → 0.57 | 7.28s | — |  |
| 10-04 02:22:04 | ETH | down | 0.48→0.41 | 0.51 → 0.51 → 0.47 | 1.53s | DOWN @ 0.50 | -0.06 / 0.44 / · |
| 10-04 02:21:59 | XRP | up | 0.41→0.47 | 0.41 → 0.41 → 0.41 | no | UP @ 0.42 | -0.65 / -0.45 / · |
| 10-04 02:21:58 | BNB | down | 0.13→0.07 | 0.23 → 0.23 → 0.23 | no | DOWN @ 0.78 | -0.36 / -0.15 / · |
| 10-04 02:21:57 | ZEC | down | 0.56→0.50 | 0.58 → 0.58 → 0.58 | no | DOWN @ 0.44 | -0.56 / -2.12 / · |
