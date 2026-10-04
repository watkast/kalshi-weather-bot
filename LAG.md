# Lag Tracker

*Updated Sun Oct 04 00:03 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 333 | 10.8s | 5% | 0% |
| BTC | 262 | 11.8s | 2% | 0% |
| DOGE | 364 | 10.4s | 2% | 0% |
| ETH | 324 | 10.9s | 2% | 0% |
| HYPE | 261 | 11.7s | 3% | 0% |
| NEAR | 292 | 10.4s | 4% | 0% |
| SOL | 636 | 10.2s | 3% | 0% |
| XRP | 590 | 11.2s | 4% | 0% |
| ZEC | 356 | 9.5s | 5% | 0% |
| **All** | **3418** | **10.7s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1792 | 515 | $-185.30 | -2.4% | $-68.26 / $-117.04 |
| Sell after 30 sec | 1789 | 1050 | $590.42 | +7.6% | $368.94 / $221.48 |
| Hold to the close | 1771 | 911 | $1472.25 | +19.3% | $515.96 / $956.29 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **38 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 00:03:34 | XRP | up | 0.57→0.63 | 0.66 → 0.66 → — | no | — |  |
| 10-04 00:03:20 | ETH | down | 0.72→0.65 | 0.60 → 0.60 → 0.60 | 10.87s | — |  |
| 10-04 00:03:11 | DOGE | down | 0.87→0.81 | 0.88 → 0.88 → 0.88 | 19.88s | DOWN @ 0.13 | -0.26 / · / · |
| 10-04 00:03:10 | HYPE | up | 0.73→0.90 | 0.72 → 0.72 → 0.72 | 20.38s | UP @ 0.73 | -0.18 / · / · |
| 10-04 00:03:10 | BNB | down | 0.56→0.44 | 0.68 → 0.68 → 0.68 | no | DOWN @ 0.33 | 0.07 / · / · |
| 10-04 00:02:59 | NEAR | up | 0.49→0.56 | 0.54 → 0.54 → 0.53 | 16.13s | — |  |
| 10-04 00:02:44 | XRP | up | 0.56→0.63 | 0.42 → 0.42 → 0.70 | 1.38s | UP @ 0.43 | 2.37 / 2.27 / · |
| 10-04 00:02:38 | DOGE | up | 0.74→0.82 | 0.51 → 0.51 → 0.51 | 7.38s | UP @ 0.51 | 2.71 / 3.34 / · |
| 10-04 00:02:28 | SOL | up | 0.56→0.85 | 0.59 → 0.59 → 0.61 | 17.14s | UP @ 0.60 | -0.34 / 1.92 / · |
| 10-04 00:02:28 | BNB | up | 0.34→0.40 | 0.65 → 0.65 → 0.56 | no | — |  |
| 10-04 00:02:28 | NEAR | up | 0.42→0.48 | 0.38 → 0.38 → 0.43 | 2.88s | UP @ 0.39 | 0.05 / 0.95 / · |
| 10-04 00:02:28 | ZEC | up | 0.53→0.58 | 0.53 → 0.53 → 0.49 | 17.89s | — |  |
| 10-04 00:02:26 | ETH | up | 0.28→0.36 | 0.29 → 0.29 → 0.57 | 4.14s | UP @ 0.30 | 2.37 / 2.58 / · |
| 10-04 00:02:23 | DOGE | down | 0.51→0.39 | 0.55 → 0.55 → 0.55 | no | DOWN @ 0.47 | -0.16 / -3.19 / · |
| 10-04 00:02:22 | XRP | down | 0.31→0.26 | 0.41 → 0.41 → 0.41 | no | DOWN @ 0.60 | -0.65 / -3.42 / · |
| 10-04 00:02:17 | BTC | up | 0.72→0.79 | 0.59 → 0.61 → 0.61 | 13.14s | UP @ 0.62 | -0.44 / 0.99 / · |
| 10-04 00:02:13 | SOL | up | 0.45→0.52 | 0.65 → 0.65 → 0.59 | no | — |  |
| 10-04 00:02:01 | XRP | down | 0.37→0.31 | 0.48 → 0.51 → 0.51 | 14.65s | DOWN @ 0.50 | -0.46 / 0.34 / · |
| 10-04 00:01:58 | SOL | down | 0.60→0.52 | 0.66 → 0.66 → 0.65 | 17.15s | DOWN @ 0.35 | -0.42 / 0.17 / · |
| 10-04 00:01:57 | BTC | up | 0.67→0.72 | 0.54 → 0.54 → 0.59 | 3.14s | UP @ 0.54 | 0.15 / 0.35 / · |
| 10-04 00:01:57 | HYPE | up | 0.66→0.72 | 0.66 → 0.66 → 0.68 | no | UP @ 0.66 | -0.22 / -0.42 / · |
| 10-04 00:01:55 | NEAR | down | 0.48→0.42 | 0.52 → 0.52 → 0.52 | 5.89s | DOWN @ 0.49 | 0.44 / 0.85 / · |
| 10-04 00:01:46 | XRP | up | 0.32→0.37 | 0.47 → 0.48 → 0.48 | 14.65s | — |  |
| 10-04 00:01:32 | BNB | up | 0.38→0.47 | 0.67 → 0.67 → 0.67 | no | — |  |
| 10-04 00:01:31 | XRP | down | 0.36→0.30 | — → 0.47 → 0.47 | no | DOWN @ 0.53 | -0.46 / -0.76 / · |
| 10-04 00:01:24 | BTC | up | 0.51→0.60 | 0.52 → 0.52 → 0.51 | no | UP @ 0.52 | -0.16 / -0.26 / · |
| 10-04 00:01:21 | NEAR | down | 0.54→0.48 | 0.60 → 0.60 → 0.60 | 6.40s | DOWN @ 0.41 | 0.85 / 0.25 / · |
| 10-04 00:01:02 | SOL | up | 0.41→0.52 | 0.51 → 0.51 → 0.51 | 10.16s | UP @ 0.51 | -0.46 / 0.95 / · |
| 10-04 00:00:37 | SOL | down | 0.45→0.38 | 0.47 → 0.47 → 0.47 | no | DOWN @ 0.54 | -0.66 / -0.86 / · |
| 10-03 23:58:44 | ETH | up | 0.01→0.20 | 0.20 → 0.20 → 0.20 | 6.93s | — |  |
