# Lag Tracker

*Updated Sun Oct 04 04:14 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 495 | 10.7s | 4% | 0% |
| BTC | 403 | 11.9s | 2% | 0% |
| DOGE | 530 | 10.6s | 2% | 0% |
| ETH | 516 | 10.9s | 3% | 0% |
| HYPE | 422 | 11.6s | 4% | 0% |
| NEAR | 468 | 10.7s | 4% | 0% |
| SOL | 974 | 10.6s | 3% | 0% |
| XRP | 934 | 11.0s | 4% | 0% |
| ZEC | 618 | 9.7s | 4% | 0% |
| **All** | **5360** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2789 | 783 | $-329.88 | -2.7% | $-146.23 / $-183.65 |
| Sell after 30 sec | 2789 | 1613 | $839.51 | +6.9% | $499.18 / $340.33 |
| Hold to the close | 2739 | 1361 | $1713.01 | +14.4% | $951.65 / $761.36 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **37 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 04:13:41 | XRP | up | 0.01→0.06 | 0.02 → 0.02 → 0.02 | 28.05s | — |  |
| 10-04 04:13:40 | ZEC | up | 0.15→0.24 | 0.09 → 0.09 → 0.09 | 13.54s | UP @ 0.10 | -0.36 / -0.78 / · |
| 10-04 04:13:37 | ETH | up | 0.78→0.84 | 0.90 → 0.90 → 0.92 | 17.04s | — |  |
| 10-04 04:13:36 | HYPE | up | 0.81→0.91 | 0.94 → 0.94 → 0.93 | no | — |  |
| 10-04 04:13:25 | ZEC | down | 0.18→0.08 | 0.10 → 0.22 → 0.22 | no | DOWN @ 0.79 | -0.45 / -0.55 / · |
| 10-04 04:13:19 | ETH | up | 0.69→0.75 | 0.85 → 0.85 → 0.90 | 4.78s | — |  |
| 10-04 04:13:09 | DOGE | down | 0.52→0.23 | 0.28 → 0.28 → 0.28 | no | — |  |
| 10-04 04:13:07 | XRP | down | 0.18→0.12 | 0.24 → 0.24 → 0.14 | 1.29s | DOWN @ 0.76 | 0.68 / 0.89 / · |
| 10-04 04:13:04 | ETH | up | 0.67→0.75 | 0.81 → 0.81 → 0.85 | 19.79s | — |  |
| 10-04 04:12:51 | ZEC | up | 0.04→0.10 | 0.07 → 0.07 → 0.06 | 17.55s | — |  |
| 10-04 04:12:47 | XRP | up | 0.11→0.21 | 0.05 → 0.05 → 0.05 | 6.28s | UP @ 0.06 | 1.68 / 0.72 / · |
| 10-04 04:12:29 | DOGE | up | 0.21→0.35 | 0.32 → 0.32 → 0.32 | no | — |  |
| 10-04 04:12:29 | XRP | down | 0.14→0.07 | 0.14 → 0.14 → 0.14 | 9.82s | DOWN @ 0.87 | 0.63 / -1.42 / · |
| 10-04 04:12:14 | XRP | down | 0.30→0.19 | 0.23 → 0.23 → 0.23 | 9.82s | — |  |
| 10-04 04:11:56 | XRP | down | 0.33→0.26 | 0.26 → 0.22 → 0.22 | 0.02s | — |  |
| 10-04 04:11:41 | BTC | down | 0.15→0.07 | 0.20 → 0.18 → 0.18 | 13.04s | DOWN @ 0.82 | -0.32 / 0.80 / · |
| 10-04 04:11:39 | XRP | down | 0.34→0.24 | 0.33 → 0.26 → 0.26 | 0.02s | — |  |
| 10-04 04:11:39 | ZEC | down | 0.38→0.28 | 0.23 → 0.34 → 0.34 | 29.80s | DOWN @ 0.67 | -0.42 / 1.34 / · |
| 10-04 04:11:36 | DOGE | up | 0.32→0.44 | 0.65 → 0.65 → 0.65 | no | — |  |
| 10-04 04:11:28 | ETH | up | 0.64→0.74 | 0.72 → 0.72 → 0.72 | no | — |  |
| 10-04 04:11:24 | ZEC | up | 0.26→0.38 | 0.29 → 0.23 → 0.23 | no | — |  |
| 10-04 04:11:24 | XRP | down | 0.39→0.34 | 0.30 → 0.33 → 0.33 | 15.04s | — |  |
| 10-04 04:11:09 | XRP | down | 0.40→0.30 | 0.34 → 0.30 → 0.30 | 30.05s | — |  |
| 10-04 04:11:03 | HYPE | up | 0.29→0.36 | 0.52 → 0.52 → 0.52 | 20.55s | — |  |
| 10-04 04:10:49 | XRP | down | 0.45→0.35 | 0.34 → 0.34 → 0.34 | no | — |  |
| 10-04 04:10:41 | ETH | up | 0.60→0.66 | 0.72 → 0.73 → 0.73 | 12.55s | — |  |
| 10-04 04:10:27 | ZEC | up | 0.22→0.28 | 0.33 → 0.33 → 0.33 | 11.35s | — |  |
| 10-04 04:10:05 | ZEC | down | 0.17→0.09 | 0.20 → 0.20 → 0.16 | 3.61s | DOWN @ 0.80 | 0.08 / -1.58 / · |
| 10-04 04:10:05 | XRP | down | 0.33→0.23 | 0.27 → 0.27 → 0.22 | no | — |  |
| 10-04 04:10:04 | SOL | down | 0.11→0.04 | 0.07 → 0.07 → 0.04 | no | DOWN @ 0.93 | 0.25 / 0.08 / · |
