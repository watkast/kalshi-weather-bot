# Lag Tracker

*Updated Sat Oct 03 18:12 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 63 | 11.1s | 5% | 0% |
| BTC | 57 | 11.2s | 4% | 0% |
| DOGE | 65 | 10.1s | 3% | 0% |
| ETH | 55 | 10.9s | 4% | 0% |
| HYPE | 46 | 11.3s | 2% | 0% |
| NEAR | 42 | 9.2s | 7% | 0% |
| SOL | 107 | 7.6s | 7% | 0% |
| XRP | 98 | 8.4s | 9% | 0% |
| ZEC | 87 | 9.1s | 6% | 0% |
| **All** | **620** | **9.3s** | **6%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 330 | 120 | $-7.24 | -0.5% | $-9.43 / $2.19 |
| Sell after 30 sec | 330 | 225 | $194.23 | +14.3% | $91.26 / $102.97 |
| Hold to the close | 257 | 129 | $230.87 | +21.8% | $122.77 / $108.10 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **34 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 18:12:11 | BNB | down | 0.55→0.38 | 0.74 → 0.74 → 0.74 | 5.06s | DOWN @ 0.27 | · / · / · |
| 10-03 18:12:08 | HYPE | down | 0.95→0.89 | 0.93 → 0.93 → 0.93 | no | — |  |
| 10-03 18:12:07 | XRP | down | 0.13→0.08 | 0.10 → 0.10 → 0.10 | no | — |  |
| 10-03 18:12:07 | BTC | down | 0.20→0.14 | 0.17 → 0.17 → 0.17 | no | — |  |
| 10-03 18:12:07 | NEAR | down | 0.15→0.10 | 0.10 → 0.10 → 0.10 | 8.56s | — |  |
| 10-03 18:12:07 | ZEC | down | 0.18→0.13 | 0.08 → 0.08 → 0.08 | 8.56s | — |  |
| 10-03 18:11:42 | BNB | up | 0.52→0.58 | 0.78 → 0.78 → 0.66 | no | — |  |
| 10-03 18:11:33 | ZEC | down | 0.33→0.24 | 0.20 → 0.20 → 0.20 | 12.56s | — |  |
| 10-03 18:11:23 | NEAR | up | 0.14→0.21 | 0.06 → 0.06 → 0.06 | 7.56s | UP @ 0.07 | 0.79 / 0.60 / · |
| 10-03 18:11:22 | HYPE | up | 0.80→0.93 | 0.88 → 0.88 → 0.88 | no | UP @ 0.89 | -0.14 / 0.15 / · |
| 10-03 18:11:20 | XRP | down | 0.26→0.20 | 0.26 → 0.26 → 0.26 | 10.31s | — |  |
| 10-03 18:11:17 | BNB | down | 0.59→0.49 | 0.71 → 0.71 → 0.71 | 28.32s | DOWN @ 0.29 | -0.40 / 0.09 / · |
| 10-03 18:11:12 | ZEC | up | 0.19→0.27 | 0.28 → 0.28 → 0.16 | no | — |  |
| 10-03 18:11:04 | HYPE | up | 0.82→0.87 | 0.91 → 0.91 → 0.91 | no | — |  |
| 10-03 18:11:03 | XRP | down | 0.31→0.23 | 0.29 → 0.38 → 0.38 | 27.82s | DOWN @ 0.63 | -0.44 / 1.31 / · |
| 10-03 18:11:02 | NEAR | down | 0.17→0.09 | 0.15 → 0.09 → 0.09 | 0.03s | — |  |
| 10-03 18:10:57 | SOL | up | 0.06→0.14 | 0.09 → 0.09 → 0.14 | 4.08s | UP @ 0.09 | 0.24 / 0.05 / · |
| 10-03 18:10:57 | ZEC | up | 0.28→0.33 | 0.47 → 0.47 → 0.28 | no | — |  |
| 10-03 18:10:57 | BNB | down | 0.74→0.69 | 0.85 → 0.85 → 0.84 | 19.09s | DOWN @ 0.15 | -0.18 / 1.06 / · |
| 10-03 18:10:45 | XRP | up | 0.26→0.34 | 0.71 → 0.29 → 0.29 | no | UP @ 0.30 | -0.40 / 0.38 / · |
| 10-03 18:10:42 | DOGE | down | 0.49→0.08 | 0.61 → 0.61 → 0.63 | 18.58s | DOWN @ 0.40 | -0.74 / 4.45 / · |
| 10-03 18:10:42 | HYPE | down | 0.94→0.86 | 0.93 → 0.93 → 0.94 | no | DOWN @ 0.07 | -0.24 / -0.02 / · |
| 10-03 18:10:42 | BTC | down | 0.64→0.19 | 0.69 → 0.69 → 0.73 | 19.08s | DOWN @ 0.31 | -0.79 / 3.50 / · |
| 10-03 18:10:42 | SOL | down | 0.19→0.06 | 0.40 → 0.40 → 0.09 | 4.07s | DOWN @ 0.62 | 2.65 / 2.14 / · |
| 10-03 18:10:42 | NEAR | down | 0.35→0.24 | 0.41 → 0.41 → 0.15 | 4.07s | DOWN @ 0.60 | 2.13 / 2.86 / · |
| 10-03 18:10:42 | ZEC | down | 0.48→0.40 | 0.53 → 0.53 → 0.47 | 4.07s | DOWN @ 0.49 | -0.16 / 1.77 / · |
| 10-03 18:10:42 | BNB | down | 0.81→0.75 | 0.90 → 0.90 → 0.85 | 4.07s | DOWN @ 0.10 | 0.27 / 0.37 / · |
| 10-03 18:10:32 | ETH | down | 0.35→0.29 | 0.34 → 0.29 → 0.29 | 0.28s | — |  |
| 10-03 18:10:30 | XRP | down | 0.64→0.57 | 0.69 → 0.71 → 0.71 | 15.32s | DOWN @ 0.29 | -0.40 / 3.80 / · |
| 10-03 18:10:25 | SOL | down | 0.35→0.28 | 0.38 → 0.38 → 0.38 | 20.33s | DOWN @ 0.63 | -0.85 / 2.55 / · |
