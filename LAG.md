# Lag Tracker

*Updated Sun Oct 04 01:43 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 405 | 10.7s | 4% | 0% |
| BTC | 322 | 12.2s | 2% | 0% |
| DOGE | 435 | 10.6s | 2% | 0% |
| ETH | 393 | 11.1s | 3% | 0% |
| HYPE | 318 | 11.6s | 3% | 0% |
| NEAR | 352 | 10.7s | 4% | 0% |
| SOL | 776 | 10.6s | 3% | 0% |
| XRP | 697 | 11.2s | 3% | 0% |
| ZEC | 445 | 9.7s | 5% | 0% |
| **All** | **4143** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2170 | 610 | $-237.35 | -2.5% | $-96.07 / $-141.28 |
| Sell after 30 sec | 2170 | 1271 | $717.32 | +7.7% | $428.59 / $288.73 |
| Hold to the close | 2119 | 1053 | $1421.98 | +15.6% | $913.69 / $508.29 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **39 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 01:43:41 | DOGE | up | 0.67→0.74 | 0.97 → 0.97 → 0.97 | no | — |  |
| 10-04 01:43:27 | ZEC | down | 0.62→0.49 | 0.62 → 0.62 → 0.44 | 4.32s | — |  |
| 10-04 01:43:12 | ZEC | up | 0.49→0.59 | 0.43 → 0.43 → 0.62 | 4.32s | UP @ 0.45 | 0.94 / -0.75 / · |
| 10-04 01:42:59 | BNB | up | 0.01→0.09 | 0.23 → 0.23 → 0.24 | no | — |  |
| 10-04 01:42:46 | ZEC | up | 0.36→0.46 | 0.32 → 0.32 → 0.31 | 16.08s | UP @ 0.33 | -0.71 / 0.56 / · |
| 10-04 01:42:36 | XRP | down | 0.97→0.89 | 0.98 → 0.98 → 0.98 | no | — |  |
| 10-04 01:42:12 | ZEC | up | 0.34→0.40 | 0.23 → 0.23 → 0.29 | 4.84s | UP @ 0.25 | 0.01 / 0.31 / · |
| 10-04 01:41:40 | BNB | up | 0.14→0.30 | 0.28 → 0.28 → 0.28 | 6.85s | — |  |
| 10-04 01:41:30 | SOL | down | 0.13→0.06 | 0.15 → 0.15 → 0.17 | 16.35s | DOWN @ 0.85 | -0.50 / 0.61 / · |
| 10-04 01:41:26 | ZEC | up | 0.21→0.27 | 0.18 → 0.18 → 0.18 | 20.35s | UP @ 0.20 | -0.62 / -0.14 / · |
| 10-04 01:41:19 | NEAR | down | 0.90→0.82 | 0.97 → 0.97 → 0.97 | no | — |  |
| 10-04 01:41:13 | SOL | up | 0.09→0.14 | 0.17 → 0.17 → 0.15 | no | — |  |
| 10-04 01:41:11 | ZEC | down | 0.32→0.21 | 0.30 → 0.30 → 0.30 | 5.36s | — |  |
| 10-04 01:41:09 | HYPE | down | 0.86→0.79 | 0.84 → 0.84 → 0.84 | no | DOWN @ 0.16 | -0.85 / -1.03 / · |
| 10-04 01:41:00 | DOGE | up | 0.50→0.61 | 0.78 → 0.78 → 0.83 | 2.10s | — |  |
| 10-04 01:40:59 | NEAR | up | 0.78→0.87 | 0.91 → 0.91 → 0.93 | 18.11s | — |  |
| 10-04 01:40:54 | HYPE | up | 0.70→0.86 | 0.79 → 0.79 → 0.79 | 22.86s | — |  |
| 10-04 01:40:39 | ZEC | down | 0.33→0.27 | 0.27 → 0.27 → 0.27 | no | — |  |
| 10-04 01:40:39 | HYPE | up | 0.59→0.69 | 0.56 → 0.56 → 0.56 | 7.86s | UP @ 0.57 | 1.59 / 2.42 / · |
| 10-04 01:40:38 | BNB | up | 0.13→0.19 | 0.30 → 0.30 → 0.30 | no | — |  |
| 10-04 01:40:25 | DOGE | down | 0.55→0.49 | 0.73 → 0.73 → 0.73 | no | DOWN @ 0.29 | -0.69 / -0.98 / · |
| 10-04 01:40:17 | BNB | up | 0.03→0.12 | 0.28 → 0.28 → 0.28 | no | — |  |
| 10-04 01:40:15 | ZEC | up | 0.26→0.36 | 0.19 → 0.19 → 0.21 | 17.12s | UP @ 0.20 | -0.24 / 0.34 / · |
| 10-04 01:40:12 | XRP | down | 0.92→0.86 | 0.91 → 0.91 → 0.91 | no | — |  |
| 10-04 01:39:59 | BTC | down | 0.87→0.80 | 0.91 → 0.91 → 0.92 | 17.62s | DOWN @ 0.09 | -0.24 / 0.22 / · |
| 10-04 01:39:59 | ZEC | down | 0.27→0.21 | 0.26 → 0.26 → 0.19 | 2.87s | — |  |
| 10-04 01:39:42 | ZEC | up | 0.20→0.27 | 0.17 → 0.17 → 0.26 | 4.37s | UP @ 0.18 | 0.26 / -0.22 / · |
| 10-04 01:39:37 | NEAR | down | 0.92→0.86 | 0.93 → 0.93 → 0.93 | 24.88s | DOWN @ 0.08 | -0.23 / 0.03 / · |
| 10-04 01:39:25 | SOL | down | 0.10→0.05 | 0.07 → 0.07 → 0.07 | 21.63s | — |  |
| 10-04 01:39:24 | BNB | up | 0.10→0.19 | 0.36 → 0.36 → 0.36 | no | — |  |
