# Lag Tracker

*Updated Sun Oct 04 03:54 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 485 | 10.7s | 4% | 0% |
| BTC | 394 | 11.9s | 2% | 0% |
| DOGE | 516 | 10.8s | 2% | 0% |
| ETH | 504 | 10.9s | 3% | 0% |
| HYPE | 407 | 11.6s | 4% | 0% |
| NEAR | 458 | 10.7s | 4% | 0% |
| SOL | 967 | 10.6s | 3% | 0% |
| XRP | 898 | 11.0s | 4% | 0% |
| ZEC | 589 | 9.6s | 4% | 0% |
| **All** | **5218** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2729 | 761 | $-324.04 | -2.7% | $-136.48 / $-187.56 |
| Sell after 30 sec | 2729 | 1578 | $830.83 | +7.0% | $501.47 / $329.36 |
| Hold to the close | 2699 | 1339 | $1656.46 | +14.1% | $937.44 / $719.02 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **37 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 03:54:05 | XRP | down | 0.41→0.33 | 0.30 → 0.30 → 0.30 | 11.88s | — |  |
| 10-04 03:53:51 | HYPE | down | 0.31→0.25 | 0.23 → 0.23 → 0.23 | 10.38s | — |  |
| 10-04 03:53:41 | BNB | up | 0.40→0.55 | 0.78 → 0.78 → 0.78 | no | — |  |
| 10-04 03:53:36 | XRP | up | 0.37→0.46 | 0.28 → 0.28 → 0.28 | no | UP @ 0.28 | -0.39 / -0.10 / · |
| 10-04 03:53:15 | HYPE | up | 0.26→0.37 | 0.25 → 0.25 → 0.25 | no | UP @ 0.26 | -0.47 / -0.76 / · |
| 10-04 03:53:01 | BTC | down | 0.16→0.11 | 0.15 → 0.15 → 0.15 | no | — |  |
| 10-04 03:52:58 | NEAR | up | 0.14→0.21 | 0.14 → 0.14 → 0.14 | 12.14s | UP @ 0.15 | -0.28 / -0.71 / · |
| 10-04 03:52:41 | ETH | down | 0.19→0.14 | 0.20 → 0.17 → 0.17 | 13.39s | — |  |
| 10-04 03:52:40 | SOL | down | 0.21→0.13 | 0.12 → 0.18 → 0.18 | no | — |  |
| 10-04 03:52:37 | XRP | down | 0.54→0.46 | 0.51 → 0.51 → 0.41 | 2.64s | — |  |
| 10-04 03:52:34 | NEAR | down | 0.23→0.18 | 0.23 → 0.23 → 0.23 | 21.15s | — |  |
| 10-04 03:52:25 | SOL | up | 0.17→0.22 | 0.14 → 0.12 → 0.12 | 14.40s | UP @ 0.13 | -0.26 / -0.26 / · |
| 10-04 03:52:22 | XRP | up | 0.46→0.54 | 0.53 → 0.53 → 0.51 | no | — |  |
| 10-04 03:52:18 | BTC | down | 0.31→0.26 | 0.29 → 0.29 → 0.29 | 7.15s | — |  |
| 10-04 03:52:10 | ETH | down | 0.31→0.23 | 0.28 → 0.24 → 0.24 | 0.39s | — |  |
| 10-04 03:52:01 | XRP | down | 0.57→0.46 | 0.56 → 0.56 → 0.56 | no | DOWN @ 0.45 | -0.26 / 0.04 / · |
| 10-04 03:52:00 | HYPE | down | 0.49→0.38 | 0.44 → 0.44 → 0.44 | 9.65s | DOWN @ 0.57 | 0.15 / 1.38 / · |
| 10-04 03:51:48 | NEAR | down | 0.24→0.19 | 0.23 → 0.23 → 0.23 | 6.65s | — |  |
| 10-04 03:51:44 | BNB | down | 0.76→0.62 | 0.86 → 0.86 → 0.86 | no | DOWN @ 0.15 | -0.37 / -0.37 / · |
| 10-04 03:51:37 | XRP | down | 0.54→0.46 | 0.58 → 0.58 → 0.56 | no | DOWN @ 0.42 | -0.26 / -0.16 / · |
| 10-04 03:51:32 | ZEC | down | 0.22→0.15 | 0.20 → 0.20 → 0.20 | no | DOWN @ 0.81 | -0.01 / -0.01 / · |
| 10-04 03:51:19 | SOL | up | 0.18→0.25 | 0.16 → 0.16 → 0.16 | no | UP @ 0.17 | -0.39 / -0.20 / · |
| 10-04 03:51:14 | NEAR | up | 0.18→0.25 | 0.12 → 0.12 → 0.12 | 10.66s | UP @ 0.14 | -0.56 / 0.68 / · |
| 10-04 03:51:10 | XRP | up | 0.47→0.53 | 0.36 → 0.52 → 0.52 | 0.15s | — |  |
| 10-04 03:51:08 | BNB | up | 0.59→0.75 | 0.83 → 0.83 → 0.85 | no | — |  |
| 10-04 03:50:55 | XRP | up | 0.43→0.50 | 0.33 → 0.36 → 0.36 | 14.67s | UP @ 0.37 | -0.53 / 1.75 / · |
| 10-04 03:50:50 | BNB | down | 0.75→0.64 | 0.84 → 0.84 → 0.83 | no | DOWN @ 0.16 | -0.20 / -0.39 / · |
| 10-04 03:50:39 | XRP | up | 0.37→0.43 | 0.35 → 0.33 → 0.33 | 30.43s | UP @ 0.34 | -0.52 / -0.22 / · |
| 10-04 03:50:28 | BTC | down | 0.40→0.34 | 0.34 → 0.34 → 0.34 | no | — |  |
| 10-04 03:50:21 | ZEC | down | 0.25→0.18 | 0.24 → 0.24 → 0.21 | no | DOWN @ 0.77 | -0.16 / -0.05 / · |
