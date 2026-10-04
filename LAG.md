# Lag Tracker

*Updated Sun Oct 04 01:33 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 393 | 10.7s | 4% | 0% |
| BTC | 314 | 11.9s | 2% | 0% |
| DOGE | 427 | 10.7s | 2% | 0% |
| ETH | 385 | 11.2s | 3% | 0% |
| HYPE | 309 | 11.6s | 3% | 0% |
| NEAR | 347 | 10.6s | 4% | 0% |
| SOL | 762 | 10.5s | 3% | 0% |
| XRP | 688 | 11.2s | 4% | 0% |
| ZEC | 424 | 9.8s | 5% | 0% |
| **All** | **4049** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2128 | 597 | $-231.19 | -2.5% | $-89.40 / $-141.79 |
| Sell after 30 sec | 2127 | 1243 | $704.93 | +7.7% | $427.66 / $277.27 |
| Hold to the close | 2119 | 1053 | $1421.98 | +15.6% | $913.69 / $508.29 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **39 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 01:33:50 | SOL | down | 0.43→0.38 | 0.48 → 0.48 → — | no | DOWN @ 0.53 | · / · / · |
| 10-04 01:33:34 | ZEC | up | 0.28→0.34 | 0.28 → 0.28 → 0.28 | 10.75s | UP @ 0.28 | -0.39 / · / · |
| 10-04 01:33:34 | DOGE | up | 0.23→0.29 | 0.29 → 0.29 → 0.29 | no | — |  |
| 10-04 01:33:17 | NEAR | up | 0.69→0.75 | 0.81 → 0.85 → 0.85 | 0.48s | — |  |
| 10-04 01:32:41 | XRP | down | 0.57→0.50 | 0.61 → 0.61 → 0.51 | 3.75s | DOWN @ 0.40 | 0.55 / -0.34 / · |
| 10-04 01:32:37 | ZEC | up | 0.35→0.41 | 0.30 → 0.30 → 0.30 | no | UP @ 0.31 | -0.21 / -0.89 / · |
| 10-04 01:32:15 | ZEC | down | 0.39→0.34 | 0.45 → 0.30 → 0.30 | 0.01s | — |  |
| 10-04 01:32:12 | BNB | down | 0.37→0.24 | 0.52 → 0.52 → 0.43 | 3.01s | DOWN @ 0.49 | 0.24 / 1.36 / · |
| 10-04 01:32:06 | SOL | down | 0.54→0.49 | 0.52 → 0.52 → 0.52 | 23.77s | — |  |
| 10-04 01:32:00 | ZEC | down | 0.46→0.40 | 0.51 → 0.45 → 0.45 | 0.26s | — |  |
| 10-04 01:31:53 | HYPE | down | 0.52→0.46 | 0.57 → 0.57 → 0.57 | 7.26s | DOWN @ 0.43 | -0.06 / -0.16 / · |
| 10-04 01:31:46 | SOL | up | 0.49→0.54 | 0.52 → 0.52 → 0.52 | no | — |  |
| 10-04 01:31:38 | XRP | up | 0.46→0.52 | 0.57 → 0.57 → 0.57 | 21.77s | — |  |
| 10-04 01:31:30 | SOL | down | 0.49→0.44 | 0.53 → 0.54 → 0.54 | no | DOWN @ 0.47 | -0.46 / -0.36 / · |
| 10-04 01:31:30 | BNB | down | 0.38→0.28 | 0.48 → 0.51 → 0.51 | no | DOWN @ 0.51 | -0.66 / -0.66 / · |
| 10-04 01:31:22 | XRP | up | 0.44→0.52 | 0.54 → 0.54 → 0.54 | no | — |  |
| 10-04 01:31:19 | NEAR | up | 0.57→0.64 | 0.72 → 0.72 → 0.72 | 11.27s | — |  |
| 10-04 01:31:11 | SOL | down | 0.49→0.44 | 0.53 → 0.53 → 0.53 | no | DOWN @ 0.49 | -0.56 / -0.66 / · |
| 10-04 01:31:09 | BNB | down | 0.36→0.23 | 0.47 → 0.47 → 0.47 | no | DOWN @ 0.54 | -0.66 / -0.96 / · |
| 10-04 01:27:15 | HYPE | down | 0.11→0.06 | 0.06 → 0.04 → 0.04 | no | — |  |
| 10-04 01:26:40 | SOL | up | 0.03→0.09 | 0.03 → 0.03 → 0.02 | no | — |  |
| 10-04 01:26:18 | HYPE | up | 0.12→0.19 | 0.10 → 0.10 → 0.10 | no | UP @ 0.11 | -0.24 / -0.26 / -1.17 |
| 10-04 01:25:19 | HYPE | up | 0.19→0.26 | 0.28 → 0.28 → 0.28 | 9.33s | — |  |
| 10-04 01:25:13 | SOL | up | 0.05→0.12 | 0.04 → 0.04 → 0.04 | no | — |  |
| 10-04 01:24:36 | HYPE | down | 0.35→0.27 | 0.41 → 0.41 → 0.41 | 7.84s | DOWN @ 0.60 | 0.68 / 1.19 / 3.83 |
| 10-04 01:24:07 | XRP | up | 0.06→0.11 | 0.08 → 0.08 → 0.08 | 22.10s | — |  |
| 10-04 01:23:08 | HYPE | up | 0.24→0.30 | 0.31 → 0.31 → 0.31 | no | — |  |
| 10-04 01:22:58 | XRP | down | 0.21→0.15 | 0.20 → 0.20 → 0.18 | 15.68s | DOWN @ 0.81 | -0.22 / 0.62 / 1.79 |
| 10-04 01:22:46 | HYPE | up | 0.26→0.32 | 0.30 → 0.30 → 0.30 | no | — |  |
| 10-04 01:22:25 | XRP | up | 0.14→0.20 | 0.15 → 0.15 → 0.18 | 3.42s | — |  |
