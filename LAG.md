# Lag Tracker

*Updated Sun Oct 04 06:44 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 586 | 10.8s | 3% | 0% |
| BTC | 458 | 11.9s | 3% | 0% |
| DOGE | 636 | 10.4s | 2% | 0% |
| ETH | 611 | 11.2s | 3% | 0% |
| HYPE | 514 | 11.6s | 4% | 0% |
| NEAR | 583 | 10.7s | 4% | 0% |
| SOL | 1126 | 10.8s | 3% | 0% |
| XRP | 1119 | 10.9s | 3% | 0% |
| ZEC | 727 | 9.8s | 4% | 0% |
| **All** | **6360** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3263 | 905 | $-397.99 | -2.8% | $-177.05 / $-220.94 |
| Sell after 30 sec | 3263 | 1867 | $989.85 | +7.0% | $546.90 / $442.95 |
| Hold to the close | 3233 | 1611 | $2062.89 | +14.7% | $1111.67 / $951.22 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **31 ms** · Coinbase price delay: **14 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 06:43:22 | NEAR | down | 0.10→0.04 | 0.27 → 0.27 → 0.28 | 16.57s | — |  |
| 10-04 06:43:07 | NEAR | up | 0.11→0.20 | 0.32 → 0.32 → 0.27 | no | — |  |
| 10-04 06:42:47 | NEAR | down | 0.19→0.13 | 0.60 → 0.60 → 0.60 | 6.83s | DOWN @ 0.42 | 2.06 / 2.47 / · |
| 10-04 06:42:32 | NEAR | down | 0.29→0.24 | 0.67 → 0.67 → 0.67 | 6.83s | — |  |
| 10-04 06:42:08 | NEAR | down | 0.39→0.32 | 0.72 → 0.72 → 0.74 | 15.84s | — |  |
| 10-04 06:41:37 | NEAR | down | 0.47→0.41 | 0.82 → 0.82 → 0.76 | 1.34s | DOWN @ 0.20 | 0.05 / 0.15 / · |
| 10-04 06:41:30 | ETH | down | 0.90→0.79 | 0.93 → 0.93 → 0.93 | no | DOWN @ 0.07 | -0.22 / 0.07 / · |
| 10-04 06:41:01 | NEAR | up | 0.52→0.62 | 0.78 → 0.78 → 0.78 | no | — |  |
| 10-04 06:40:25 | BNB | up | 0.12→0.20 | 0.33 → 0.33 → 0.33 | no | — |  |
| 10-04 06:39:44 | ETH | up | 0.82→0.89 | 0.89 → 0.89 → 0.89 | no | — |  |
| 10-04 06:39:36 | BNB | down | 0.20→0.13 | 0.32 → 0.32 → 0.30 | no | DOWN @ 0.70 | -0.51 / -1.12 / · |
| 10-04 06:39:05 | SOL | down | 0.95→0.89 | 0.94 → 0.94 → 0.94 | no | DOWN @ 0.06 | -0.12 / -0.12 / · |
| 10-04 06:38:50 | NEAR | down | 0.58→0.52 | 0.67 → 0.67 → 0.66 | 19.13s | DOWN @ 0.36 | -0.82 / -0.43 / · |
| 10-04 06:38:37 | ETH | up | 0.74→0.81 | 0.79 → 0.79 → 0.83 | 2.38s | — |  |
| 10-04 06:38:35 | HYPE | down | 0.15→0.10 | 0.18 → 0.18 → 0.18 | no | DOWN @ 0.83 | -0.52 / -0.52 / · |
| 10-04 06:38:21 | XRP | down | 0.94→0.88 | 0.93 → 0.93 → 0.91 | no | DOWN @ 0.07 | 0.12 / -0.00 / · |
| 10-04 06:38:17 | NEAR | down | 0.61→0.52 | 0.71 → 0.71 → 0.71 | no | — |  |
| 10-04 06:38:15 | ETH | down | 0.85→0.74 | 0.83 → 0.83 → 0.83 | no | DOWN @ 0.17 | 0.18 / -0.30 / · |
| 10-04 06:38:01 | NEAR | up | 0.55→0.62 | 0.68 → 0.68 → 0.68 | 8.39s | — |  |
| 10-04 06:37:44 | NEAR | down | 0.63→0.54 | 0.74 → 0.74 → 0.74 | 9.65s | DOWN @ 0.28 | 0.00 / -0.49 / · |
| 10-04 06:37:43 | ZEC | down | 0.84→0.78 | 0.92 → 0.92 → 0.92 | no | DOWN @ 0.08 | -0.17 / -0.06 / · |
| 10-04 06:37:43 | XRP | down | 0.97→0.92 | 0.95 → 0.95 → 0.95 | no | — |  |
| 10-04 06:37:42 | HYPE | down | 0.40→0.28 | 0.43 → 0.39 → 0.39 | 12.40s | — |  |
| 10-04 06:37:31 | BNB | down | 0.45→0.35 | 0.72 → 0.72 → 0.72 | 7.65s | DOWN @ 0.28 | 0.19 / 1.57 / · |
| 10-04 06:36:57 | BNB | up | 0.51→0.58 | 0.76 → 0.76 → 0.76 | no | — |  |
| 10-04 06:35:40 | BNB | up | 0.43→0.49 | 0.69 → 0.69 → 0.69 | no | — |  |
| 10-04 06:35:20 | HYPE | down | 0.45→0.36 | 0.44 → 0.44 → 0.41 | no | DOWN @ 0.57 | -0.26 / -0.66 / · |
| 10-04 06:34:58 | HYPE | down | 0.48→0.42 | 0.46 → 0.46 → 0.46 | 25.70s | — |  |
| 10-04 06:34:46 | NEAR | down | 0.78→0.72 | 0.85 → 0.85 → 0.85 | 7.58s | DOWN @ 0.16 | -0.01 / -0.01 / · |
| 10-04 06:33:12 | ZEC | up | 0.64→0.71 | 0.74 → 0.74 → 0.74 | 26.85s | — |  |
