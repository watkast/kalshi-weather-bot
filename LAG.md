# Lag Tracker

*Updated Sat Oct 03 17:32 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟡 **Too early.** Collecting data — needs at least 150 paper trades before calling it.

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 27 | 8.3s | 4% | 0% |
| BTC | 12 | 11.9s | 0% | 0% |
| DOGE | 17 | 8.1s | 6% | 0% |
| ETH | 14 | 18.9s | 7% | 0% |
| HYPE | 12 | 6.9s | 8% | 0% |
| NEAR | 16 | 8.9s | 12% | 0% |
| SOL | 30 | 5.9s | 3% | 0% |
| XRP | 23 | 6.1s | 14% | 0% |
| ZEC | 21 | 11.8s | 10% | 0% |
| **All** | **172** | **8.8s** | **7%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 94 | 34 | $-5.82 | -1.6% | $-9.21 / $3.39 |
| Sell after 30 sec | 92 | 65 | $51.93 | +14.4% | $5.84 / $46.09 |
| Hold to the close | 91 | 47 | $117.36 | +33.3% | $-68.79 / $186.15 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **34 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 17:31:49 | SOL | down | 0.27→0.20 | 0.30 → 0.30 → 0.30 | no | DOWN @ 0.70 | -0.61 / · / · |
| 10-03 17:31:36 | BNB | down | 0.45→0.40 | 0.48 → 0.48 → 0.48 | 21.29s | DOWN @ 0.52 | -0.46 / · / · |
| 10-03 17:31:34 | SOL | down | 0.32→0.27 | 0.32 → 0.32 → 0.32 | no | — |  |
| 10-03 17:31:33 | NEAR | down | 0.22→0.17 | 0.21 → 0.21 → 0.21 | 9.04s | — |  |
| 10-03 17:31:30 | ZEC | down | 0.33→0.27 | 0.26 → 0.26 → 0.26 | 12.04s | — |  |
| 10-03 17:31:28 | DOGE | down | 0.26→0.20 | 0.18 → 0.26 → 0.26 | 29.54s | DOWN @ 0.75 | -0.38 / 0.87 / · |
| 10-03 17:31:17 | SOL | up | 0.27→0.35 | 0.35 → 0.35 → 0.35 | no | — |  |
| 10-03 17:28:41 | DOGE | up | 0.08→0.13 | 0.28 → 0.28 → 0.17 | no | — |  |
| 10-03 17:28:35 | BNB | up | 0.32→0.44 | 0.45 → 0.45 → 0.45 | 7.56s | — |  |
| 10-03 17:28:29 | ZEC | down | 0.86→0.71 | 0.90 → 0.87 → 0.87 | 14.06s | — |  |
| 10-03 17:28:17 | DOGE | down | 0.31→0.26 | 0.33 → 0.33 → 0.33 | 11.31s | DOWN @ 0.69 | -0.61 / 1.04 / 2.95 |
| 10-03 17:28:15 | BNB | up | 0.33→0.45 | 0.52 → 0.52 → 0.52 | no | — |  |
| 10-03 17:28:14 | XRP | down | 0.22→0.11 | 0.38 → 0.22 → 0.22 | 0.27s | DOWN @ 0.80 | -0.65 / 1.57 / 1.88 |
| 10-03 17:28:08 | SOL | up | 0.05→0.12 | 0.08 → 0.08 → 0.08 | 5.06s | — |  |
| 10-03 17:28:07 | ZEC | down | 0.85→0.77 | 0.88 → 0.88 → 0.88 | no | — |  |
| 10-03 17:28:07 | NEAR | up | 0.03→0.08 | 0.06 → 0.06 → 0.06 | no | — |  |
| 10-03 17:27:54 | XRP | down | 0.45→0.25 | 0.37 → 0.37 → 0.38 | 19.31s | DOWN @ 0.64 | -0.64 / 0.90 / 3.43 |
| 10-03 17:27:53 | SOL | up | 0.07→0.14 | 0.07 → 0.07 → 0.07 | 20.07s | UP @ 0.07 | -0.01 / 0.54 / -0.77 |
| 10-03 17:27:50 | BNB | up | 0.29→0.42 | 0.52 → 0.52 → 0.52 | no | — |  |
| 10-03 17:27:46 | ZEC | up | 0.80→0.86 | 0.74 → 0.74 → 0.74 | 11.81s | — |  |
| 10-03 17:27:43 | DOGE | up | 0.14→0.36 | 0.20 → 0.42 → 0.42 | 0.30s | — |  |
| 10-03 17:27:40 | ETH | up | 0.01→0.09 | 0.06 → 0.06 → 0.04 | no | UP @ 0.06 | -0.26 / 0.20 / -0.63 |
| 10-03 17:27:39 | XRP | up | 0.31→0.40 | 0.23 → 0.23 → 0.37 | 4.31s | UP @ 0.24 | 0.90 / 1.00 / -2.53 |
| 10-03 17:27:38 | SOL | up | 0.03→0.09 | 0.08 → 0.08 → 0.08 | no | — |  |
| 10-03 17:27:31 | ZEC | up | 0.67→0.73 | 0.77 → 0.77 → 0.77 | 26.82s | — |  |
| 10-03 17:27:31 | BNB | down | 0.39→0.33 | 0.59 → 0.62 → 0.62 | 12.31s | — |  |
| 10-03 17:27:24 | XRP | up | 0.24→0.36 | 0.51 → 0.51 → 0.23 | no | — |  |
| 10-03 17:27:11 | BNB | down | 0.47→0.36 | 0.78 → 0.78 → 0.59 | 2.31s | DOWN @ 0.23 | 1.40 / 0.91 / 7.57 |
| 10-03 17:27:08 | ZEC | down | 0.63→0.58 | 0.86 → 0.86 → 0.72 | 4.56s | — |  |
| 10-03 17:27:06 | ETH | down | 0.16→0.06 | 0.41 → 0.41 → 0.41 | 7.06s | DOWN @ 0.60 | 3.15 / 3.20 / 3.83 |
