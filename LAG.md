# Lag Tracker

*Updated Sun Oct 04 04:44 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 519 | 10.8s | 4% | 0% |
| BTC | 406 | 11.9s | 2% | 0% |
| DOGE | 548 | 10.8s | 2% | 0% |
| ETH | 524 | 10.9s | 3% | 0% |
| HYPE | 440 | 11.6s | 4% | 0% |
| NEAR | 498 | 10.8s | 4% | 0% |
| SOL | 995 | 10.6s | 3% | 0% |
| XRP | 967 | 11.0s | 4% | 0% |
| ZEC | 644 | 9.8s | 4% | 0% |
| **All** | **5541** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2861 | 793 | $-351.40 | -2.8% | $-153.39 / $-198.01 |
| Sell after 30 sec | 2861 | 1641 | $846.48 | +6.8% | $502.28 / $344.20 |
| Hold to the close | 2820 | 1408 | $1838.43 | +15.0% | $867.45 / $970.98 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **14 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 04:43:39 | BNB | down | 0.21→0.16 | 0.93 → 0.93 → 0.94 | no | — |  |
| 10-04 04:43:32 | HYPE | up | 0.75→0.86 | 0.86 → 0.86 → 0.86 | 11.16s | — |  |
| 10-04 04:43:15 | BNB | down | 0.52→0.26 | 0.83 → 0.83 → 0.83 | no | — |  |
| 10-04 04:42:21 | DOGE | up | 0.04→0.10 | 0.02 → 0.02 → 0.02 | no | — |  |
| 10-04 04:42:12 | XRP | up | 0.05→0.11 | 0.05 → 0.05 → 0.03 | no | UP @ 0.05 | -0.28 / -0.36 / · |
| 10-04 04:41:38 | XRP | down | 0.18→0.07 | 0.09 → 0.09 → 0.07 | no | — |  |
| 10-04 04:41:11 | NEAR | down | 0.98→0.92 | 0.97 → 0.97 → 0.95 | no | — |  |
| 10-04 04:40:51 | HYPE | down | 0.63→0.48 | 0.58 → 0.58 → 0.58 | no | DOWN @ 0.43 | -1.53 / -0.55 / · |
| 10-04 04:40:44 | BTC | down | 0.24→0.19 | 0.38 → 0.33 → 0.33 | 0.19s | DOWN @ 0.68 | -0.42 / -0.11 / · |
| 10-04 04:40:41 | XRP | down | 0.22→0.14 | 0.10 → 0.10 → 0.11 | no | — |  |
| 10-04 04:40:32 | HYPE | down | 0.63→0.56 | 0.58 → 0.58 → 0.58 | no | — |  |
| 10-04 04:40:23 | XRP | down | 0.22→0.15 | 0.15 → 0.15 → 0.10 | 4.95s | — |  |
| 10-04 04:40:08 | XRP | down | 0.28→0.19 | 0.17 → 0.17 → 0.17 | 20.21s | — |  |
| 10-04 04:40:00 | SOL | down | 0.16→0.08 | 0.12 → 0.12 → 0.12 | 12.46s | — |  |
| 10-04 04:39:54 | DOGE | down | 0.18→0.12 | 0.10 → 0.10 → 0.09 | no | — |  |
| 10-04 04:39:52 | BNB | up | 0.38→0.50 | 0.79 → 0.79 → 0.79 | no | — |  |
| 10-04 04:39:32 | XRP | up | 0.20→0.29 | 0.33 → 0.33 → 0.33 | no | — |  |
| 10-04 04:39:24 | HYPE | up | 0.42→0.55 | 0.35 → 0.35 → 0.54 | 3.97s | UP @ 0.36 | 1.25 / 2.46 / · |
| 10-04 04:39:17 | XRP | up | 0.18→0.29 | 0.18 → 0.18 → 0.18 | 10.73s | UP @ 0.19 | -0.41 / -0.03 / · |
| 10-04 04:38:57 | BNB | up | 0.24→0.41 | 0.66 → 0.66 → 0.70 | 16.00s | — |  |
| 10-04 04:38:47 | XRP | down | 0.26→0.19 | 0.18 → 0.18 → 0.18 | no | — |  |
| 10-04 04:38:38 | NEAR | up | 0.69→0.77 | 0.77 → 0.77 → 0.81 | 19.98s | — |  |
| 10-04 04:38:34 | BTC | down | 0.35→0.29 | 0.41 → 0.41 → 0.41 | no | DOWN @ 0.59 | -0.34 / -0.34 / · |
| 10-04 04:38:26 | ZEC | up | 0.80→0.86 | 0.81 → 0.81 → 0.90 | 1.48s | — |  |
| 10-04 04:38:17 | XRP | down | 0.27→0.20 | 0.20 → 0.20 → 0.20 | no | — |  |
| 10-04 04:38:13 | HYPE | up | 0.37→0.43 | 0.52 → 0.47 → 0.47 | no | — |  |
| 10-04 04:38:01 | NEAR | down | 0.65→0.58 | 0.76 → 0.76 → 0.76 | 11.48s | DOWN @ 0.26 | -0.67 / -0.76 / · |
| 10-04 04:37:57 | HYPE | up | 0.43→0.55 | 0.48 → 0.52 → 0.52 | no | — |  |
| 10-04 04:37:56 | XRP | up | 0.20→0.28 | 0.23 → 0.23 → 0.21 | no | — |  |
| 10-04 04:37:54 | DOGE | down | 0.30→0.20 | 0.18 → 0.18 → 0.17 | no | — |  |
