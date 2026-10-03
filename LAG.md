# Lag Tracker

*Updated Sat Oct 03 20:13 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 197 | 10.6s | 6% | 0% |
| BTC | 117 | 11.3s | 3% | 0% |
| DOGE | 167 | 9.8s | 2% | 0% |
| ETH | 116 | 11.0s | 3% | 0% |
| HYPE | 104 | 11.8s | 3% | 0% |
| NEAR | 135 | 9.2s | 4% | 0% |
| SOL | 265 | 9.3s | 5% | 0% |
| XRP | 252 | 9.6s | 5% | 0% |
| ZEC | 179 | 9.7s | 6% | 0% |
| **All** | **1532** | **9.9s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 809 | 263 | $-56.40 | -1.6% | $-16.43 / $-39.97 |
| Sell after 30 sec | 808 | 520 | $358.39 | +10.4% | $224.51 / $133.88 |
| Hold to the close | 784 | 399 | $633.36 | +18.9% | $431.82 / $201.54 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 20:12:52 | DOGE | down | 0.86→0.69 | 0.92 → 0.92 → 0.92 | no | DOWN @ 0.09 | -0.38 / · / · |
| 10-03 20:12:49 | BNB | up | 0.74→0.83 | 0.96 → 0.97 → 0.97 | no | — |  |
| 10-03 20:12:30 | XRP | down | 0.99→0.67 | 0.95 → 0.95 → 0.97 | no | DOWN @ 0.06 | -0.33 / -0.33 / · |
| 10-03 20:12:30 | DOGE | down | 0.82→0.69 | 0.97 → 0.97 → 0.81 | 4.05s | — |  |
| 10-03 20:12:30 | BTC | down | 0.99→0.91 | 0.98 → 0.98 → 0.99 | no | — |  |
| 10-03 20:11:59 | DOGE | up | 0.80→0.90 | 0.95 → 0.95 → 0.95 | no | — |  |
| 10-03 20:11:34 | BTC | up | 0.89→0.96 | 0.92 → 0.93 → 0.93 | 15.31s | — |  |
| 10-03 20:11:24 | XRP | down | 0.91→0.83 | 0.90 → 0.90 → 0.90 | no | — |  |
| 10-03 20:11:19 | BNB | up | 0.51→0.63 | 0.74 → 0.85 → 0.85 | 0.27s | — |  |
| 10-03 20:11:09 | DOGE | up | 0.65→0.71 | 0.83 → 0.83 → 0.83 | 24.83s | — |  |
| 10-03 20:10:59 | ETH | down | 0.96→0.90 | 0.98 → 0.98 → 0.98 | no | — |  |
| 10-03 20:10:55 | BNB | down | 0.62→0.54 | 0.77 → 0.77 → 0.77 | no | — |  |
| 10-03 20:10:54 | XRP | down | 0.97→0.91 | 0.94 → 0.94 → 0.94 | 9.81s | DOWN @ 0.07 | 0.20 / 0.20 / · |
| 10-03 20:10:54 | DOGE | down | 0.70→0.64 | 0.92 → 0.92 → 0.92 | 9.81s | DOWN @ 0.08 | 0.64 / 0.45 / · |
| 10-03 20:10:53 | ZEC | down | 0.91→0.82 | 0.93 → 0.93 → 0.93 | 11.06s | DOWN @ 0.07 | -0.18 / -0.10 / · |
| 10-03 20:10:53 | BTC | down | 0.93→0.85 | 0.94 → 0.94 → 0.94 | 11.06s | DOWN @ 0.06 | -0.09 / 0.09 / · |
| 10-03 20:09:36 | BNB | down | 0.57→0.45 | 0.58 → 0.58 → 0.58 | 13.31s | DOWN @ 0.42 | -0.45 / 0.14 / · |
| 10-03 20:09:21 | XRP | down | 0.95→0.87 | 0.91 → 0.91 → 0.91 | no | — |  |
| 10-03 20:09:15 | BNB | down | 0.64→0.59 | 0.82 → 0.82 → 0.74 | 4.32s | DOWN @ 0.18 | 0.45 / 2.02 / · |
| 10-03 20:08:45 | BNB | up | 0.54→0.63 | 0.65 → 0.65 → 0.80 | 3.58s | — |  |
| 10-03 20:07:46 | ZEC | up | 0.82→0.92 | 0.89 → 0.89 → 0.90 | 17.84s | — |  |
| 10-03 20:07:24 | XRP | down | 0.96→0.88 | 0.88 → 0.88 → 0.88 | no | — |  |
| 10-03 20:07:02 | XRP | up | 0.85→0.90 | 0.84 → 0.84 → 0.85 | 16.35s | UP @ 0.85 | -0.18 / 0.03 / · |
| 10-03 20:06:44 | DOGE | down | 0.73→0.67 | 0.84 → 0.84 → 0.87 | no | DOWN @ 0.16 | -0.58 / -0.58 / · |
| 10-03 20:06:43 | BTC | up | 0.73→0.81 | 0.81 → 0.81 → 0.81 | no | — |  |
| 10-03 20:06:31 | XRP | up | 0.82→0.88 | 0.85 → 0.85 → 0.82 | no | — |  |
| 10-03 20:06:24 | BTC | down | 0.81→0.73 | 0.81 → 0.81 → 0.81 | no | DOWN @ 0.19 | -0.32 / -0.41 / · |
| 10-03 20:06:21 | ETH | down | 0.93→0.86 | 0.95 → 0.96 → 0.96 | 13.11s | — |  |
| 10-03 20:06:17 | BNB | down | 0.51→0.44 | 0.54 → 0.54 → 0.53 | no | DOWN @ 0.47 | -0.36 / -0.26 / · |
| 10-03 20:06:16 | XRP | down | 0.89→0.84 | 0.84 → 0.84 → 0.85 | no | — |  |
