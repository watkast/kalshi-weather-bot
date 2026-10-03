# Lag Tracker

*Updated Sat Oct 03 22:13 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 268 | 10.7s | 5% | 0% |
| BTC | 182 | 11.9s | 2% | 0% |
| DOGE | 283 | 10.2s | 2% | 0% |
| ETH | 230 | 11.1s | 3% | 0% |
| HYPE | 203 | 11.6s | 4% | 0% |
| NEAR | 210 | 10.0s | 3% | 0% |
| SOL | 439 | 9.6s | 4% | 0% |
| XRP | 423 | 10.3s | 4% | 0% |
| ZEC | 283 | 9.6s | 5% | 0% |
| **All** | **2521** | **10.5s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1315 | 386 | $-128.26 | -2.3% | $-49.32 / $-78.94 |
| Sell after 30 sec | 1315 | 791 | $488.76 | +8.8% | $293.13 / $195.63 |
| Hold to the close | 1243 | 623 | $1014.71 | +19.5% | $581.00 / $433.71 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **37 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 22:13:30 | HYPE | down | 0.93→0.81 | 0.97 → 0.97 → 0.97 | 16.07s | — |  |
| 10-03 22:13:10 | NEAR | up | 0.17→0.25 | 0.63 → 0.63 → 0.63 | no | — |  |
| 10-03 22:13:03 | HYPE | up | 0.76→0.88 | 0.90 → 0.94 → 0.94 | 12.33s | — |  |
| 10-03 22:12:55 | NEAR | down | 0.40→0.25 | 0.57 → 0.57 → 0.57 | 20.33s | DOWN @ 0.45 | -1.34 / 2.58 / · |
| 10-03 22:12:38 | NEAR | up | 0.08→0.34 | 0.04 → 0.04 → 0.04 | 8.08s | — |  |
| 10-03 22:12:09 | HYPE | up | 0.57→0.76 | 0.90 → 0.90 → 0.90 | no | — |  |
| 10-03 22:11:45 | HYPE | down | 0.63→0.56 | 0.79 → 0.79 → 0.76 | no | — |  |
| 10-03 22:11:02 | HYPE | up | 0.56→0.72 | 0.62 → 0.64 → 0.64 | 13.06s | UP @ 0.66 | -0.73 / 0.71 / · |
| 10-03 22:10:47 | HYPE | down | 0.55→0.45 | 0.62 → 0.62 → 0.62 | no | — |  |
| 10-03 22:10:37 | DOGE | up | 0.73→0.78 | 0.87 → 0.87 → 0.87 | 8.06s | — |  |
| 10-03 22:10:22 | SOL | up | 0.89→0.95 | 0.90 → 0.90 → 0.90 | 23.06s | UP @ 0.91 | -0.18 / 0.40 / · |
| 10-03 22:10:22 | DOGE | up | 0.58→0.66 | 0.80 → 0.80 → 0.80 | 9.31s | — |  |
| 10-03 22:10:15 | HYPE | up | 0.45→0.54 | 0.73 → 0.73 → 0.53 | no | — |  |
| 10-03 22:09:58 | NEAR | down | 0.14→0.08 | 0.15 → 0.15 → 0.09 | 3.06s | DOWN @ 0.87 | 0.16 / 0.55 / · |
| 10-03 22:09:43 | XRP | down | 0.88→0.82 | 0.90 → 0.90 → 0.89 | no | DOWN @ 0.11 | -0.14 / -0.24 / · |
| 10-03 22:09:27 | XRP | down | 0.93→0.86 | 0.85 → 0.85 → 0.90 | no | — |  |
| 10-03 22:09:27 | NEAR | down | 0.26→0.18 | 0.28 → 0.28 → 0.16 | 4.32s | DOWN @ 0.74 | 0.66 / 0.66 / · |
| 10-03 22:09:26 | BTC | down | 0.97→0.90 | 0.93 → 0.93 → 0.82 | 4.57s | — |  |
| 10-03 22:09:18 | DOGE | up | 0.73→0.80 | 0.81 → 0.88 → 0.88 | 0.02s | — |  |
| 10-03 22:09:03 | SOL | up | 0.79→0.84 | 0.88 → 0.88 → 0.88 | 13.06s | — |  |
| 10-03 22:08:57 | BTC | up | 0.81→0.89 | 0.89 → 0.89 → 0.90 | 19.31s | — |  |
| 10-03 22:08:48 | SOL | up | 0.75→0.81 | 0.81 → 0.82 → 0.82 | 13.06s | — |  |
| 10-03 22:08:48 | XRP | up | 0.75→0.80 | 0.74 → 0.74 → 0.74 | 13.06s | UP @ 0.75 | -0.38 / 0.77 / · |
| 10-03 22:08:47 | DOGE | down | 0.65→0.57 | 0.71 → 0.71 → 0.71 | no | DOWN @ 0.29 | -0.40 / -2.02 / · |
| 10-03 22:08:35 | HYPE | up | 0.62→0.69 | 0.74 → 0.74 → 0.74 | 26.06s | — |  |
| 10-03 22:08:21 | DOGE | down | 0.61→0.48 | 0.70 → 0.70 → 0.70 | no | DOWN @ 0.30 | -0.40 / -0.50 / · |
| 10-03 22:08:20 | HYPE | down | 0.72→0.61 | 0.72 → 0.72 → 0.72 | no | DOWN @ 0.29 | -0.49 / -0.88 / · |
| 10-03 22:08:07 | XRP | down | 0.79→0.73 | 0.76 → 0.76 → 0.76 | no | — |  |
| 10-03 22:08:00 | BNB | down | 0.90→0.84 | 0.95 → 0.95 → 0.96 | no | DOWN @ 0.06 | -0.28 / -0.28 / · |
| 10-03 22:07:54 | SOL | down | 0.73→0.66 | 0.77 → 0.77 → 0.77 | no | DOWN @ 0.24 | -0.26 / -0.46 / · |
