# Lag Tracker

*Updated Sat Oct 03 23:13 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 307 | 10.8s | 5% | 0% |
| BTC | 219 | 11.8s | 2% | 0% |
| DOGE | 315 | 10.4s | 2% | 0% |
| ETH | 285 | 11.1s | 3% | 0% |
| HYPE | 227 | 11.6s | 4% | 0% |
| NEAR | 255 | 10.5s | 3% | 0% |
| SOL | 537 | 10.0s | 4% | 0% |
| XRP | 489 | 10.3s | 4% | 0% |
| ZEC | 323 | 9.6s | 5% | 0% |
| **All** | **2957** | **10.6s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1537 | 440 | $-172.39 | -2.6% | $-62.44 / $-109.95 |
| Sell after 30 sec | 1537 | 921 | $530.21 | +8.0% | $340.46 / $189.75 |
| Hold to the close | 1484 | 722 | $891.57 | +14.1% | $598.03 / $293.54 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **38 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 23:13:12 | BTC | up | 0.05→0.12 | 0.15 → 0.15 → 0.12 | no | — |  |
| 10-03 23:13:10 | HYPE | down | 0.27→0.20 | 0.10 → 0.10 → 0.10 | no | — |  |
| 10-03 23:13:07 | SOL | up | 0.01→0.07 | 0.05 → 0.05 → 0.05 | no | — |  |
| 10-03 23:12:58 | ETH | down | 0.29→0.21 | 0.07 → 0.07 → 0.05 | no | — |  |
| 10-03 23:12:41 | ETH | up | 0.19→0.25 | 0.08 → 0.08 → 0.07 | no | UP @ 0.08 | -0.31 / -0.51 / · |
| 10-03 23:12:23 | XRP | down | 0.10→0.04 | 0.17 → 0.17 → 0.17 | 7.29s | DOWN @ 0.83 | 0.32 / 0.11 / · |
| 10-03 23:12:22 | ETH | down | 0.31→0.20 | 0.16 → 0.16 → 0.16 | 8.29s | — |  |
| 10-03 23:12:08 | XRP | down | 0.14→0.08 | 0.17 → 0.17 → 0.17 | 22.30s | — |  |
| 10-03 23:12:06 | SOL | down | 0.15→0.07 | 0.14 → 0.14 → 0.14 | 24.80s | — |  |
| 10-03 23:11:51 | SOL | up | 0.08→0.16 | 0.17 → 0.17 → 0.17 | no | — |  |
| 10-03 23:11:48 | XRP | down | 0.16→0.09 | 0.28 → 0.23 → 0.23 | 0.27s | DOWN @ 0.77 | -0.36 / 0.26 / · |
| 10-03 23:11:36 | SOL | up | 0.09→0.17 | 0.18 → 0.18 → 0.18 | no | — |  |
| 10-03 23:11:07 | HYPE | up | 0.14→0.22 | 0.12 → 0.12 → 0.12 | no | UP @ 0.13 | -0.35 / -0.16 / · |
| 10-03 23:11:02 | DOGE | up | 0.05→0.11 | 0.15 → 0.15 → 0.15 | no | — |  |
| 10-03 23:10:30 | ETH | up | 0.29→0.36 | 0.20 → 0.20 → 0.28 | 0.78s | UP @ 0.21 | 0.43 / 0.34 / · |
| 10-03 23:10:28 | XRP | up | 0.15→0.22 | 0.20 → 0.20 → 0.23 | no | — |  |
| 10-03 23:10:25 | NEAR | up | 0.84→0.94 | 0.92 → 0.92 → 0.92 | 5.28s | — |  |
| 10-03 23:10:22 | HYPE | down | 0.32→0.20 | 0.26 → 0.26 → 0.26 | 8.29s | DOWN @ 0.75 | 0.35 / 0.24 / · |
| 10-03 23:10:14 | ETH | up | 0.23→0.28 | 0.21 → 0.21 → 0.20 | 17.04s | UP @ 0.22 | -0.45 / 0.32 / · |
| 10-03 23:10:12 | SOL | down | 0.18→0.10 | 0.21 → 0.21 → 0.20 | no | DOWN @ 0.80 | -0.34 / -0.34 / · |
| 10-03 23:10:12 | BTC | up | 0.22→0.28 | 0.28 → 0.28 → 0.30 | 19.04s | — |  |
| 10-03 23:09:49 | NEAR | up | 0.60→0.66 | 0.77 → 0.77 → 0.77 | 11.80s | — |  |
| 10-03 23:09:48 | XRP | up | 0.05→0.20 | 0.14 → 0.14 → 0.14 | 12.55s | UP @ 0.15 | -0.37 / 0.29 / · |
| 10-03 23:09:47 | SOL | up | 0.06→0.15 | 0.07 → 0.07 → 0.07 | 13.55s | UP @ 0.07 | -0.11 / 1.09 / · |
| 10-03 23:09:36 | ETH | up | 0.10→0.20 | 0.08 → 0.08 → 0.08 | 10.05s | UP @ 0.09 | -0.32 / 0.90 / · |
| 10-03 23:09:21 | NEAR | up | 0.45→0.52 | 0.64 → 0.64 → 0.64 | 25.05s | — |  |
| 10-03 23:09:16 | SOL | up | 0.03→0.12 | 0.09 → 0.07 → 0.07 | no | UP @ 0.08 | -0.15 / -0.13 / · |
| 10-03 23:09:05 | NEAR | up | 0.33→0.45 | 0.51 → 0.51 → 0.51 | 10.56s | — |  |
| 10-03 23:08:43 | NEAR | down | 0.45→0.37 | 0.62 → 0.62 → 0.61 | 17.75s | DOWN @ 0.39 | -0.44 / 0.55 / · |
| 10-03 23:08:36 | BTC | down | 0.31→0.25 | 0.34 → 0.34 → 0.34 | 10.25s | DOWN @ 0.67 | -0.42 / 0.09 / · |
