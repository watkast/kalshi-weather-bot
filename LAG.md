# Lag Tracker

*Updated Sat Oct 03 18:52 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 113 | 11.1s | 5% | 0% |
| BTC | 75 | 10.6s | 4% | 0% |
| DOGE | 87 | 9.1s | 5% | 0% |
| ETH | 69 | 11.3s | 3% | 0% |
| HYPE | 55 | 11.6s | 2% | 0% |
| NEAR | 65 | 10.4s | 5% | 0% |
| SOL | 153 | 7.6s | 7% | 0% |
| XRP | 142 | 8.8s | 9% | 0% |
| ZEC | 114 | 8.5s | 6% | 0% |
| **All** | **873** | **9.6s** | **6%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 455 | 164 | $-10.24 | -0.5% | $1.23 / $-11.47 |
| Sell after 30 sec | 455 | 307 | $258.10 | +13.8% | $134.59 / $123.51 |
| Hold to the close | 436 | 230 | $520.26 | +29.2% | $227.95 / $292.31 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 18:52:05 | BNB | up | 0.47→0.55 | 0.54 → 0.54 → 0.54 | 9.08s | — |  |
| 10-03 18:51:27 | SOL | down | 0.23→0.15 | 0.26 → 0.26 → 0.24 | 17.83s | — |  |
| 10-03 18:51:22 | BTC | down | 0.47→0.42 | 0.47 → 0.47 → 0.47 | 7.83s | DOWN @ 0.53 | 1.06 / 1.47 / · |
| 10-03 18:50:58 | SOL | up | 0.28→0.36 | 0.30 → 0.30 → 0.34 | 1.58s | UP @ 0.31 | -0.01 / -0.89 / · |
| 10-03 18:50:40 | SOL | down | 0.33→0.28 | 0.32 → 0.32 → 0.32 | no | — |  |
| 10-03 18:50:24 | ZEC | down | 0.47→0.40 | 0.40 → 0.40 → 0.40 | 6.09s | — |  |
| 10-03 18:50:14 | NEAR | up | 0.20→0.26 | 0.18 → 0.18 → 0.23 | 0.59s | UP @ 0.19 | 0.16 / -0.32 / · |
| 10-03 18:50:07 | BNB | down | 0.65→0.56 | 0.65 → 0.65 → 0.65 | no | DOWN @ 0.36 | -0.43 / -0.53 / · |
| 10-03 18:49:58 | ZEC | down | 0.46→0.41 | 0.35 → 0.35 → 0.33 | no | — |  |
| 10-03 18:49:55 | SOL | down | 0.32→0.25 | 0.34 → 0.34 → 0.34 | 5.10s | DOWN @ 0.66 | 0.50 / -0.22 / · |
| 10-03 18:49:51 | BNB | up | 0.59→0.65 | 0.61 → 0.61 → 0.61 | 8.60s | — |  |
| 10-03 18:49:45 | ETH | down | 0.44→0.36 | 0.41 → 0.40 → 0.40 | 14.85s | — |  |
| 10-03 18:49:15 | SOL | up | 0.31→0.38 | 0.31 → 0.32 → 0.32 | 14.86s | UP @ 0.33 | -0.51 / -0.22 / · |
| 10-03 18:49:08 | NEAR | down | 0.29→0.24 | 0.24 → 0.24 → 0.24 | 21.86s | — |  |
| 10-03 18:48:49 | BNB | up | 0.45→0.50 | 0.56 → 0.56 → 0.56 | 26.37s | — |  |
| 10-03 18:48:47 | SOL | up | 0.28→0.34 | 0.32 → 0.32 → 0.32 | no | — |  |
| 10-03 18:48:39 | ZEC | down | 0.50→0.44 | 0.44 → 0.44 → 0.44 | 6.13s | — |  |
| 10-03 18:48:34 | BNB | down | 0.52→0.47 | 0.56 → 0.56 → 0.56 | no | DOWN @ 0.45 | -0.56 / -0.75 / · |
| 10-03 18:48:34 | NEAR | down | 0.32→0.25 | 0.34 → 0.34 → 0.34 | 11.39s | DOWN @ 0.67 | -0.42 / 0.40 / · |
| 10-03 18:48:29 | HYPE | down | 0.31→0.23 | 0.27 → 0.27 → 0.27 | 16.14s | — |  |
| 10-03 18:47:58 | DOGE | up | 0.13→0.20 | 0.17 → 0.17 → 0.17 | no | — |  |
| 10-03 18:47:49 | SOL | up | 0.29→0.35 | 0.28 → 0.28 → 0.28 | 11.38s | UP @ 0.29 | -0.40 / 0.09 / · |
| 10-03 18:47:46 | BNB | up | 0.48→0.55 | 0.56 → 0.56 → 0.56 | 29.13s | — |  |
| 10-03 18:47:43 | DOGE | down | 0.20→0.13 | 0.18 → 0.18 → 0.17 | no | — |  |
| 10-03 18:47:42 | ZEC | down | 0.49→0.44 | 0.54 → 0.54 → 0.36 | 3.13s | DOWN @ 0.47 | 1.25 / 1.25 / · |
| 10-03 18:47:23 | ZEC | up | 0.51→0.56 | 0.50 → 0.50 → 0.50 | 7.13s | UP @ 0.51 | -0.16 / -1.85 / · |
| 10-03 18:47:21 | ETH | up | 0.43→0.49 | 0.43 → 0.43 → 0.43 | no | UP @ 0.44 | -0.46 / -0.46 / · |
| 10-03 18:47:16 | SOL | up | 0.33→0.41 | 0.33 → 0.33 → 0.33 | 13.89s | UP @ 0.33 | -0.42 / -0.81 / · |
| 10-03 18:47:15 | BNB | up | 0.36→0.42 | 0.40 → 0.38 → 0.38 | 14.64s | — |  |
| 10-03 18:47:06 | XRP | down | 0.29→0.24 | 0.34 → 0.34 → 0.34 | 9.13s | DOWN @ 0.67 | 0.30 / 0.61 / · |
