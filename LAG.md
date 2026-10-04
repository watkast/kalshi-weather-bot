# Lag Tracker

*Updated Sun Oct 04 01:23 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 390 | 10.7s | 4% | 0% |
| BTC | 314 | 11.9s | 2% | 0% |
| DOGE | 426 | 10.7s | 2% | 0% |
| ETH | 385 | 11.2s | 3% | 0% |
| HYPE | 304 | 11.8s | 3% | 0% |
| NEAR | 345 | 10.6s | 3% | 0% |
| SOL | 755 | 10.4s | 3% | 0% |
| XRP | 684 | 11.2s | 4% | 0% |
| ZEC | 420 | 9.8s | 4% | 0% |
| **All** | **4023** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2117 | 594 | $-229.42 | -2.5% | $-87.58 / $-141.84 |
| Sell after 30 sec | 2117 | 1241 | $706.67 | +7.8% | $428.48 / $278.19 |
| Hold to the close | 2105 | 1044 | $1402.49 | +15.5% | $908.22 / $494.27 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **39 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 01:23:08 | HYPE | up | 0.24→0.30 | 0.31 → 0.31 → 0.31 | no | — |  |
| 10-04 01:22:58 | XRP | down | 0.21→0.15 | 0.20 → 0.20 → 0.18 | 15.68s | DOWN @ 0.81 | -0.22 / 0.62 / · |
| 10-04 01:22:46 | HYPE | up | 0.26→0.32 | 0.30 → 0.30 → 0.30 | no | — |  |
| 10-04 01:22:25 | XRP | up | 0.14→0.20 | 0.15 → 0.15 → 0.18 | 3.42s | — |  |
| 10-04 01:22:00 | XRP | up | 0.13→0.20 | 0.12 → 0.15 → 0.15 | 28.68s | — |  |
| 10-04 01:21:48 | HYPE | up | 0.25→0.33 | 0.33 → 0.33 → 0.33 | no | — |  |
| 10-04 01:20:57 | HYPE | up | 0.17→0.26 | 0.15 → 0.15 → 0.23 | 1.93s | UP @ 0.16 | 0.47 / 0.57 / · |
| 10-04 01:20:15 | NEAR | up | 0.11→0.18 | 0.06 → 0.06 → 0.06 | 13.96s | UP @ 0.07 | -0.20 / 0.69 / · |
| 10-04 01:19:59 | ZEC | up | 0.06→0.13 | 0.06 → 0.04 → 0.04 | 14.45s | UP @ 0.05 | -0.17 / 0.28 / · |
| 10-04 01:18:44 | NEAR | down | 0.19→0.14 | 0.12 → 0.12 → 0.12 | 14.96s | — |  |
| 10-04 01:18:17 | ETH | down | 0.21→0.15 | 0.14 → 0.14 → 0.14 | no | — |  |
| 10-04 01:18:17 | XRP | down | 0.15→0.10 | 0.17 → 0.17 → 0.17 | no | DOWN @ 0.84 | -0.41 / -0.09 / · |
| 10-04 01:18:16 | ZEC | down | 0.32→0.27 | 0.28 → 0.26 → 0.26 | 12.72s | — |  |
| 10-04 01:18:02 | ETH | down | 0.27→0.21 | 0.21 → 0.21 → 0.21 | 11.47s | — |  |
| 10-04 01:17:58 | BTC | down | 0.26→0.20 | 0.38 → 0.38 → 0.35 | 15.72s | DOWN @ 0.63 | -0.24 / 0.07 / · |
| 10-04 01:17:56 | SOL | down | 0.26→0.21 | 0.27 → 0.27 → 0.28 | no | DOWN @ 0.74 | -0.69 / -0.18 / · |
| 10-04 01:17:45 | ZEC | up | 0.29→0.34 | 0.26 → 0.26 → 0.26 | no | UP @ 0.28 | -0.68 / -0.59 / · |
| 10-04 01:17:45 | XRP | down | 0.19→0.14 | 0.21 → 0.20 → 0.20 | 13.72s | DOWN @ 0.80 | -0.34 / -0.03 / · |
| 10-04 01:17:06 | ZEC | up | 0.36→0.41 | 0.36 → 0.36 → 0.36 | no | — |  |
| 10-04 01:15:55 | HYPE | down | 0.37→0.28 | 0.42 → 0.42 → 0.35 | 3.49s | DOWN @ 0.59 | 0.16 / 1.92 / · |
| 10-04 01:15:52 | BTC | down | 0.32→0.25 | 0.42 → 0.42 → 0.42 | 21.86s | DOWN @ 0.58 | -0.15 / 0.25 / · |
| 10-04 01:15:52 | BNB | down | 0.21→0.13 | 0.39 → 0.39 → 0.39 | 6.99s | DOWN @ 0.62 | 0.58 / 0.99 / · |
| 10-04 01:13:43 | DOGE | down | 0.64→0.33 | 0.93 → 0.93 → 0.81 | no | DOWN @ 0.08 | 0.64 / 0.07 / -0.86 |
| 10-04 01:13:34 | NEAR | down | 0.27→0.12 | 0.37 → 0.37 → 0.37 | 11.90s | — |  |
| 10-04 01:13:34 | BTC | down | 0.44→0.17 | 0.68 → 0.68 → 0.68 | 11.90s | DOWN @ 0.33 | -0.42 / 3.70 / 6.54 |
| 10-04 01:13:34 | XRP | down | 0.97→0.74 | 0.98 → 0.98 → 0.98 | no | — |  |
| 10-04 01:13:33 | ETH | down | 0.93→0.85 | 0.96 → 0.96 → 0.96 | 12.40s | — |  |
| 10-04 01:13:33 | SOL | down | 0.90→0.85 | 0.99 → 0.99 → 0.99 | no | — |  |
| 10-04 01:13:28 | DOGE | down | 0.73→0.49 | 0.84 → 0.84 → 0.93 | no | DOWN @ 0.17 | -1.32 / -0.30 / -1.80 |
| 10-04 01:13:21 | ZEC | up | 0.09→0.20 | 0.05 → 0.05 → 0.05 | no | UP @ 0.07 | -0.53 / -0.65 / -0.74 |
