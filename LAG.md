# Lag Tracker

*Updated Sun Oct 04 09:05 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 642 | 11.2s | 3% | 0% |
| BTC | 514 | 11.9s | 3% | 0% |
| DOGE | 713 | 10.4s | 2% | 0% |
| ETH | 689 | 11.1s | 4% | 0% |
| HYPE | 595 | 11.2s | 4% | 0% |
| NEAR | 694 | 10.8s | 4% | 0% |
| SOL | 1274 | 10.9s | 3% | 0% |
| XRP | 1284 | 10.8s | 4% | 0% |
| ZEC | 862 | 9.6s | 4% | 0% |
| **All** | **7267** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3731 | 1052 | $-432.52 | -2.7% | $-205.96 / $-226.56 |
| Sell after 30 sec | 3730 | 2176 | $1199.78 | +7.5% | $591.90 / $607.88 |
| Hold to the close | 3708 | 1831 | $2351.02 | +14.7% | $1436.02 / $915.00 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **14 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 09:05:24 | ETH | up | 0.18→0.25 | 0.14 → 0.14 → 0.08 | no | UP @ 0.14 | · / · / · |
| 10-04 09:05:23 | XRP | up | 0.20→0.26 | 0.24 → 0.24 → 0.23 | no | — |  |
| 10-04 09:05:13 | SOL | down | 0.20→0.14 | 0.20 → 0.20 → 0.20 | 11.54s | DOWN @ 0.81 | -0.33 / · / · |
| 10-04 09:05:11 | ZEC | down | 0.18→0.12 | 0.23 → 0.18 → 0.18 | 0.27s | — |  |
| 10-04 09:04:48 | XRP | down | 0.28→0.22 | 0.27 → 0.27 → 0.27 | no | DOWN @ 0.74 | -0.38 / -0.18 / · |
| 10-04 09:04:47 | HYPE | down | 0.28→0.22 | 0.24 → 0.24 → 0.24 | 7.53s | — |  |
| 10-04 09:04:44 | NEAR | down | 0.34→0.25 | 0.40 → 0.40 → 0.40 | 10.53s | DOWN @ 0.61 | -0.44 / 1.30 / · |
| 10-04 09:04:36 | BNB | up | 0.44→0.49 | 0.60 → 0.60 → 0.67 | 3.78s | — |  |
| 10-04 09:04:17 | HYPE | down | 0.30→0.24 | 0.29 → 0.29 → 0.29 | 7.53s | DOWN @ 0.71 | 0.11 / 0.11 / · |
| 10-04 09:04:16 | XRP | down | 0.34→0.28 | 0.33 → 0.33 → 0.33 | 8.53s | — |  |
| 10-04 09:03:55 | XRP | down | 0.36→0.29 | 0.29 → 0.35 → 0.35 | no | DOWN @ 0.65 | -0.43 / -0.22 / · |
| 10-04 09:03:52 | HYPE | up | 0.26→0.33 | 0.24 → 0.24 → 0.29 | 2.53s | UP @ 0.25 | 0.11 / 0.11 / · |
| 10-04 09:03:45 | NEAR | up | 0.27→0.35 | 0.36 → 0.36 → 0.36 | 10.03s | — |  |
| 10-04 09:03:45 | SOL | up | 0.24→0.29 | 0.32 → 0.32 → 0.32 | no | — |  |
| 10-04 09:03:28 | SOL | down | 0.33→0.27 | 0.34 → 0.27 → 0.27 | 0.27s | — |  |
| 10-04 09:03:22 | BNB | up | 0.30→0.43 | 0.39 → 0.39 → 0.46 | 2.77s | — |  |
| 10-04 09:03:08 | XRP | down | 0.30→0.24 | 0.34 → 0.34 → 0.33 | 16.53s | DOWN @ 0.67 | -0.32 / 0.09 / · |
| 10-04 09:03:07 | BTC | down | 0.34→0.28 | 0.26 → 0.26 → 0.24 | 17.78s | — |  |
| 10-04 09:03:07 | SOL | down | 0.40→0.33 | 0.36 → 0.36 → 0.34 | 18.03s | DOWN @ 0.64 | -0.23 / 0.59 / · |
| 10-04 09:03:02 | NEAR | down | 0.35→0.29 | 0.40 → 0.40 → 0.40 | 7.53s | DOWN @ 0.61 | 0.07 / 0.17 / · |
| 10-04 09:02:59 | ZEC | down | 0.21→0.16 | 0.21 → 0.21 → 0.21 | 10.53s | DOWN @ 0.79 | -0.35 / -0.55 / · |
| 10-04 09:02:41 | SOL | down | 0.43→0.38 | 0.41 → 0.43 → 0.43 | 14.28s | DOWN @ 0.57 | -0.46 / 0.46 / · |
| 10-04 09:02:22 | HYPE | down | 0.40→0.30 | 0.41 → 0.41 → 0.42 | no | DOWN @ 0.61 | -0.75 / -0.85 / · |
| 10-04 09:02:20 | XRP | down | 0.42→0.35 | 0.42 → 0.42 → 0.43 | 19.54s | DOWN @ 0.58 | -0.56 / 0.05 / · |
| 10-04 09:02:20 | SOL | down | 0.51→0.46 | 0.54 → 0.54 → 0.41 | 4.54s | DOWN @ 0.47 | 0.85 / 0.54 / · |
| 10-04 09:02:12 | NEAR | down | 0.45→0.39 | 0.48 → 0.48 → 0.48 | 28.04s | DOWN @ 0.53 | -0.56 / -0.06 / · |
| 10-04 09:02:10 | ETH | down | 0.43→0.38 | 0.42 → 0.33 → 0.33 | 0.28s | — |  |
| 10-04 09:02:05 | XRP | down | 0.44→0.38 | 0.50 → 0.50 → 0.50 | 5.04s | DOWN @ 0.51 | 0.24 / 0.14 / · |
| 10-04 09:01:50 | SOL | up | 0.48→0.54 | 0.58 → 0.58 → 0.58 | no | — |  |
| 10-04 09:01:42 | NEAR | up | 0.38→0.44 | 0.46 → 0.46 → 0.46 | no | — |  |
