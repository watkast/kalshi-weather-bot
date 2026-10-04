# Lag Tracker

*Updated Sun Oct 04 01:53 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 413 | 10.6s | 4% | 0% |
| BTC | 326 | 12.4s | 2% | 0% |
| DOGE | 439 | 10.5s | 2% | 0% |
| ETH | 400 | 11.2s | 3% | 0% |
| HYPE | 320 | 11.6s | 3% | 0% |
| NEAR | 364 | 10.6s | 4% | 0% |
| SOL | 797 | 10.6s | 3% | 0% |
| XRP | 718 | 11.2s | 3% | 0% |
| ZEC | 454 | 9.7s | 5% | 0% |
| **All** | **4231** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2213 | 619 | $-246.32 | -2.6% | $-98.92 / $-147.40 |
| Sell after 30 sec | 2212 | 1289 | $716.41 | +7.5% | $437.37 / $279.04 |
| Hold to the close | 2170 | 1073 | $1409.72 | +15.1% | $959.11 / $450.61 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **39 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 01:53:58 | NEAR | up | 0.48→0.59 | 0.68 → 0.68 → — | no | — |  |
| 10-04 01:53:44 | SOL | down | 0.90→0.84 | 0.82 → 0.82 → 0.82 | no | — |  |
| 10-04 01:53:43 | XRP | down | 0.50→0.43 | 0.47 → 0.47 → 0.47 | no | — |  |
| 10-04 01:53:38 | ZEC | down | 0.54→0.44 | 0.49 → 0.49 → 0.55 | no | — |  |
| 10-04 01:53:30 | NEAR | up | 0.47→0.53 | 0.62 → 0.62 → 0.62 | 9.71s | — |  |
| 10-04 01:53:28 | XRP | down | 0.53→0.47 | 0.59 → 0.59 → 0.59 | 11.46s | DOWN @ 0.41 | -0.44 / · / · |
| 10-04 01:53:24 | DOGE | down | 0.46→0.41 | 0.47 → 0.47 → 0.47 | no | DOWN @ 0.53 | -0.46 / -2.24 / · |
| 10-04 01:53:22 | ETH | up | 0.71→0.84 | 0.80 → 0.80 → 0.80 | 17.71s | UP @ 0.80 | -0.34 / 1.16 / · |
| 10-04 01:53:20 | SOL | up | 0.71→0.77 | 0.86 → 0.82 → 0.84 | no | — |  |
| 10-04 01:53:19 | BTC | up | 0.63→0.69 | 0.72 → 0.71 → 0.71 | 20.46s | — |  |
| 10-04 01:53:15 | NEAR | down | 0.52→0.43 | 0.55 → 0.55 → 0.69 | no | DOWN @ 0.47 | -1.35 / -1.93 / · |
| 10-04 01:53:13 | ZEC | down | 0.52→0.46 | 0.74 → 0.74 → 0.74 | 5.20s | DOWN @ 0.27 | 1.98 / 1.38 / · |
| 10-04 01:53:11 | XRP | down | 0.44→0.38 | 0.43 → 0.43 → 0.43 | no | DOWN @ 0.57 | -0.76 / -0.86 / · |
| 10-04 01:53:09 | DOGE | down | 0.52→0.47 | 0.59 → 0.59 → 0.59 | 8.45s | DOWN @ 0.42 | 0.64 / 0.64 / · |
| 10-04 01:53:03 | ETH | down | 0.80→0.73 | 0.91 → 0.91 → 0.91 | 14.70s | DOWN @ 0.09 | -0.16 / 0.92 / · |
| 10-04 01:52:53 | XRP | up | 0.38→0.44 | 0.54 → 0.54 → 0.54 | no | — |  |
| 10-04 01:52:50 | DOGE | up | 0.42→0.51 | 0.72 → 0.72 → 0.72 | no | — |  |
| 10-04 01:52:46 | NEAR | up | 0.53→0.60 | 0.56 → 0.56 → 0.62 | 1.96s | — |  |
| 10-04 01:52:38 | XRP | up | 0.35→0.44 | 0.46 → 0.46 → 0.46 | 10.21s | — |  |
| 10-04 01:52:31 | NEAR | up | 0.40→0.46 | 0.59 → 0.59 → 0.56 | no | — |  |
| 10-04 01:52:29 | ZEC | down | 0.68→0.60 | 0.79 → 0.79 → 0.78 | 18.46s | DOWN @ 0.22 | -0.26 / 0.91 / · |
| 10-04 01:52:23 | XRP | down | 0.44→0.35 | 0.47 → 0.47 → 0.47 | no | DOWN @ 0.53 | -0.46 / -1.06 / · |
| 10-04 01:52:10 | BTC | up | 0.58→0.65 | 0.72 → 0.72 → 0.72 | no | — |  |
| 10-04 01:52:06 | XRP | down | 0.50→0.44 | 0.59 → 0.59 → 0.59 | 11.46s | DOWN @ 0.42 | -0.65 / 0.74 / · |
| 10-04 01:51:58 | SOL | up | 0.63→0.69 | 0.80 → 0.80 → 0.80 | 20.22s | — |  |
| 10-04 01:51:57 | NEAR | down | 0.48→0.42 | 0.56 → 0.56 → 0.56 | no | DOWN @ 0.45 | -0.85 / -0.95 / · |
| 10-04 01:51:53 | BNB | up | 0.80→0.89 | 0.94 → 0.94 → 0.94 | no | — |  |
| 10-04 01:51:50 | BTC | up | 0.47→0.57 | 0.59 → 0.59 → 0.59 | 12.47s | — |  |
| 10-04 01:51:50 | XRP | up | 0.41→0.47 | 0.47 → 0.47 → 0.47 | 12.47s | — |  |
| 10-04 01:51:42 | NEAR | up | 0.35→0.42 | 0.52 → 0.52 → 0.52 | 5.72s | — |  |
