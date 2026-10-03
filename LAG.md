# Lag Tracker

*Updated Sat Oct 03 19:32 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 172 | 10.7s | 6% | 0% |
| BTC | 92 | 10.7s | 3% | 0% |
| DOGE | 119 | 9.3s | 3% | 0% |
| ETH | 85 | 10.9s | 2% | 0% |
| HYPE | 73 | 11.7s | 3% | 0% |
| NEAR | 109 | 9.2s | 5% | 0% |
| SOL | 214 | 8.9s | 6% | 0% |
| XRP | 183 | 9.3s | 7% | 0% |
| ZEC | 156 | 9.4s | 6% | 0% |
| **All** | **1203** | **9.6s** | **5%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 637 | 213 | $-45.23 | -1.7% | $-9.72 / $-35.51 |
| Sell after 30 sec | 634 | 410 | $290.09 | +11.0% | $175.89 / $114.20 |
| Hold to the close | 628 | 320 | $591.03 | +22.7% | $370.57 / $220.46 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **37 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 19:32:44 | BNB | down | 0.30→0.19 | 0.36 → 0.36 → — | 1.53s | DOWN @ 0.65 | · / · / · |
| 10-03 19:32:43 | XRP | down | 0.42→0.36 | 0.58 → 0.58 → — | 2.78s | DOWN @ 0.42 | · / · / · |
| 10-03 19:32:42 | SOL | down | 0.27→0.22 | 0.39 → 0.39 → 0.27 | 3.53s | DOWN @ 0.62 | · / · / · |
| 10-03 19:32:36 | DOGE | down | 0.45→0.35 | 0.41 → 0.41 → 0.41 | 9.78s | DOWN @ 0.60 | 0.27 / · / · |
| 10-03 19:32:27 | XRP | down | 0.50→0.45 | 0.64 → 0.64 → 0.58 | 4.03s | DOWN @ 0.37 | 0.06 / · / · |
| 10-03 19:32:25 | SOL | down | 0.33→0.27 | 0.38 → 0.38 → 0.38 | 20.28s | DOWN @ 0.63 | -0.54 / · / · |
| 10-03 19:32:21 | DOGE | up | 0.39→0.45 | 0.41 → 0.41 → 0.41 | no | — |  |
| 10-03 19:32:11 | ZEC | down | 0.83→0.76 | 0.68 → 0.68 → 0.68 | no | — |  |
| 10-03 19:32:08 | NEAR | down | 0.49→0.43 | 0.55 → 0.55 → 0.55 | 7.29s | DOWN @ 0.46 | 0.24 / 0.14 / · |
| 10-03 19:32:06 | XRP | up | 0.45→0.50 | 0.59 → 0.59 → 0.59 | 10.04s | — |  |
| 10-03 19:31:53 | NEAR | up | 0.45→0.50 | 0.52 → 0.52 → 0.52 | 7.29s | — |  |
| 10-03 19:31:51 | XRP | down | 0.50→0.45 | 0.59 → 0.59 → 0.59 | no | DOWN @ 0.41 | -0.44 / -0.84 / · |
| 10-03 19:31:46 | ZEC | up | 0.67→0.75 | 0.70 → 0.68 → 0.68 | no | UP @ 0.69 | -0.51 / -0.51 / · |
| 10-03 19:31:41 | ETH | down | 0.37→0.31 | 0.47 → 0.47 → 0.47 | 20.04s | DOWN @ 0.54 | -0.36 / -0.06 / · |
| 10-03 19:31:34 | SOL | down | 0.47→0.40 | 0.55 → 0.55 → 0.55 | 26.29s | DOWN @ 0.46 | -0.56 / 0.95 / · |
| 10-03 19:31:22 | NEAR | up | 0.40→0.45 | 0.41 → 0.41 → 0.41 | 7.29s | — |  |
| 10-03 19:31:22 | XRP | up | 0.50→0.58 | 0.46 → 0.46 → 0.46 | 7.29s | UP @ 0.46 | 0.54 / 0.95 / · |
| 10-03 19:31:07 | XRP | up | 0.32→0.42 | 0.42 → 0.42 → 0.42 | 22.30s | — |  |
| 10-03 19:31:07 | BNB | up | 0.26→0.35 | 0.32 → 0.32 → 0.32 | 8.04s | — |  |
| 10-03 19:30:51 | XRP | up | 0.28→0.35 | 0.40 → 0.40 → 0.40 | 23.80s | — |  |
| 10-03 19:28:43 | XRP | up | 0.07→0.18 | 0.53 → 0.53 → 0.67 | 4.81s | — |  |
| 10-03 19:28:32 | BNB | up | 0.06→0.21 | 0.28 → 0.20 → 0.20 | no | — |  |
| 10-03 19:28:27 | XRP | up | 0.15→0.31 | 0.49 → 0.49 → 0.49 | 20.31s | — |  |
| 10-03 19:28:18 | SOL | down | 0.77→0.67 | 0.90 → 0.90 → 0.90 | no | DOWN @ 0.11 | -0.38 / -0.35 / -1.17 |
| 10-03 19:28:12 | XRP | down | 0.33→0.13 | 0.64 → 0.64 → 0.64 | 5.56s | DOWN @ 0.37 | 0.85 / 0.65 / 6.13 |
| 10-03 19:28:10 | BNB | down | 0.29→0.07 | 0.26 → 0.26 → 0.26 | no | — |  |
| 10-03 19:27:59 | SOL | up | 0.65→0.74 | 0.88 → 0.88 → 0.85 | no | — |  |
| 10-03 19:27:59 | ZEC | down | 0.97→0.91 | 0.83 → 0.83 → 0.90 | no | — |  |
| 10-03 19:27:55 | BNB | up | 0.12→0.31 | 0.38 → 0.38 → 0.38 | no | — |  |
| 10-03 19:27:53 | XRP | up | 0.28→0.35 | 0.55 → 0.55 → 0.55 | 9.31s | — |  |
