# Lag Tracker

*Updated Sun Oct 04 07:04 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 597 | 10.9s | 3% | 0% |
| BTC | 462 | 11.9s | 3% | 0% |
| DOGE | 641 | 10.4s | 2% | 0% |
| ETH | 622 | 11.2s | 3% | 0% |
| HYPE | 529 | 11.4s | 4% | 0% |
| NEAR | 600 | 10.7s | 4% | 0% |
| SOL | 1139 | 10.8s | 3% | 0% |
| XRP | 1126 | 11.0s | 3% | 0% |
| ZEC | 745 | 9.7s | 4% | 0% |
| **All** | **6461** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3302 | 918 | $-399.54 | -2.8% | $-177.18 / $-222.36 |
| Sell after 30 sec | 3302 | 1890 | $1007.41 | +7.0% | $557.25 / $450.16 |
| Hold to the close | 3286 | 1645 | $2185.09 | +15.3% | $1156.82 / $1028.27 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **31 ms** · Coinbase price delay: **14 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 07:04:33 | ETH | down | 0.42→0.34 | 0.33 → 0.33 → 0.42 | no | — |  |
| 10-04 07:04:15 | ZEC | down | 0.58→0.49 | 0.66 → 0.66 → 0.66 | 6.17s | DOWN @ 0.36 | 0.25 / 2.06 / · |
| 10-04 07:04:14 | ETH | up | 0.37→0.43 | 0.33 → 0.33 → 0.33 | 22.17s | UP @ 0.33 | -0.42 / 0.47 / · |
| 10-04 07:04:08 | DOGE | up | 0.62→0.67 | 0.71 → 0.76 → 0.76 | 0.16s | — |  |
| 10-04 07:04:08 | SOL | down | 0.58→0.51 | 0.71 → 0.71 → 0.71 | 13.17s | DOWN @ 0.29 | -0.40 / 0.09 / · |
| 10-04 07:03:58 | ZEC | down | 0.76→0.60 | 0.81 → 0.81 → 0.81 | 7.42s | DOWN @ 0.20 | 1.02 / 1.90 / · |
| 10-04 07:03:58 | ETH | up | 0.39→0.45 | 0.38 → 0.38 → 0.38 | no | — |  |
| 10-04 07:03:43 | ETH | down | 0.41→0.35 | 0.38 → 0.38 → 0.38 | 22.43s | — |  |
| 10-04 07:03:19 | SOL | up | 0.58→0.64 | 0.61 → 0.61 → 0.62 | 16.93s | — |  |
| 10-04 07:03:17 | ZEC | up | 0.55→0.63 | 0.54 → 0.54 → 0.69 | 3.43s | UP @ 0.54 | 1.17 / 2.09 / · |
| 10-04 07:03:15 | NEAR | down | 0.24→0.18 | 0.24 → 0.24 → 0.24 | 20.94s | DOWN @ 0.76 | -0.37 / -0.06 / · |
| 10-04 07:03:14 | HYPE | up | 0.29→0.34 | 0.34 → 0.34 → 0.34 | 6.68s | — |  |
| 10-04 07:03:00 | NEAR | up | 0.21→0.26 | 0.20 → 0.20 → 0.20 | 5.93s | UP @ 0.22 | -0.06 / -0.35 / · |
| 10-04 07:02:57 | ZEC | up | 0.48→0.56 | 0.49 → 0.49 → 0.49 | 8.94s | UP @ 0.50 | -0.06 / 1.57 / · |
| 10-04 07:02:36 | ZEC | down | 0.49→0.44 | 0.51 → 0.52 → 0.52 | no | DOWN @ 0.49 | -0.56 / -0.66 / · |
| 10-04 07:02:18 | XRP | up | 0.65→0.73 | 0.66 → 0.66 → 0.76 | 2.95s | UP @ 0.66 | 0.60 / 0.50 / · |
| 10-04 07:02:03 | XRP | down | 0.67→0.62 | 0.71 → 0.71 → 0.66 | 3.20s | DOWN @ 0.29 | 0.19 / -0.78 / · |
| 10-04 07:01:55 | ETH | down | 0.45→0.35 | 0.45 → 0.45 → 0.45 | 10.45s | DOWN @ 0.56 | -0.56 / 0.25 / · |
| 10-04 07:01:20 | XRP | up | 0.58→0.66 | 0.57 → 0.57 → 0.56 | 16.21s | UP @ 0.58 | -0.66 / 0.77 / · |
| 10-04 07:01:18 | SOL | up | 0.55→0.61 | 0.58 → 0.58 → 0.59 | 17.71s | — |  |
| 10-04 07:01:18 | ZEC | down | 0.56→0.49 | 0.60 → 0.60 → 0.57 | 18.21s | DOWN @ 0.41 | -0.34 / -0.05 / · |
| 10-04 07:01:10 | HYPE | down | 0.41→0.33 | 0.43 → 0.43 → 0.43 | 25.71s | DOWN @ 0.57 | -0.46 / 0.66 / · |
| 10-04 07:01:03 | ETH | down | 0.50→0.44 | 0.46 → 0.46 → 0.47 | no | — |  |
| 10-04 07:01:00 | BNB | down | 0.46→0.40 | 0.61 → 0.61 → 0.61 | 20.97s | DOWN @ 0.39 | -0.44 / -0.05 / · |
| 10-04 06:58:41 | NEAR | down | 0.76→0.68 | 0.97 → 0.97 → 0.97 | no | — |  |
| 10-04 06:58:33 | ZEC | down | 0.20→0.06 | 0.20 → 0.20 → 0.20 | 20.74s | DOWN @ 0.80 | -0.34 / 1.18 / 1.88 |
| 10-04 06:58:27 | BNB | down | 0.95→0.81 | 0.99 → 0.99 → 0.99 | no | — |  |
| 10-04 06:58:18 | ZEC | down | 0.22→0.15 | 0.55 → 0.55 → 0.55 | 5.74s | DOWN @ 0.46 | 3.00 / 3.00 / 5.22 |
| 10-04 06:58:17 | NEAR | up | 0.78→0.84 | 0.97 → 0.97 → 0.97 | no | — |  |
| 10-04 06:58:03 | BNB | up | 0.84→0.95 | 0.99 → 0.99 → 0.99 | no | — |  |
