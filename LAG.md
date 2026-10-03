# Lag Tracker

*Updated Sat Oct 03 22:52 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 296 | 10.7s | 5% | 0% |
| BTC | 203 | 12.1s | 1% | 0% |
| DOGE | 303 | 10.2s | 2% | 0% |
| ETH | 269 | 11.2s | 3% | 0% |
| HYPE | 215 | 11.6s | 4% | 0% |
| NEAR | 241 | 10.5s | 3% | 0% |
| SOL | 510 | 9.9s | 4% | 0% |
| XRP | 465 | 10.3s | 4% | 0% |
| ZEC | 318 | 9.6s | 5% | 0% |
| **All** | **2820** | **10.6s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1466 | 420 | $-159.98 | -2.6% | $-55.01 / $-104.97 |
| Sell after 30 sec | 1466 | 876 | $512.49 | +8.2% | $325.45 / $187.04 |
| Hold to the close | 1437 | 698 | $862.63 | +14.1% | $579.44 / $283.19 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **37 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 22:51:58 | SOL | up | 0.60→0.67 | 0.69 → 0.69 → 0.69 | no | — |  |
| 10-03 22:51:49 | XRP | down | 0.53→0.47 | 0.49 → 0.49 → 0.56 | 33.09s | — |  |
| 10-03 22:51:43 | HYPE | up | 0.36→0.45 | 0.39 → 0.39 → 0.39 | no | UP @ 0.39 | -0.24 / -0.64 / · |
| 10-03 22:51:42 | ZEC | down | 0.48→0.38 | 0.29 → 0.29 → 0.29 | no | — |  |
| 10-03 22:51:40 | SOL | up | 0.59→0.67 | 0.62 → 0.62 → 0.62 | 11.59s | — |  |
| 10-03 22:51:30 | XRP | up | 0.40→0.47 | 0.28 → 0.28 → 0.28 | 6.84s | UP @ 0.28 | 1.77 / 2.37 / · |
| 10-03 22:51:25 | NEAR | up | 0.13→0.18 | 0.17 → 0.17 → 0.17 | 11.34s | — |  |
| 10-03 22:51:25 | ZEC | up | 0.26→0.33 | 0.18 → 0.18 → 0.18 | 11.34s | UP @ 0.19 | -0.41 / 2.31 / · |
| 10-03 22:51:25 | BTC | up | 0.54→0.67 | 0.54 → 0.54 → 0.54 | 11.34s | UP @ 0.54 | -0.46 / 1.27 / · |
| 10-03 22:51:25 | BNB | up | 0.50→0.64 | 0.74 → 0.74 → 0.74 | 11.34s | — |  |
| 10-03 22:51:25 | ETH | up | 0.38→0.45 | 0.38 → 0.38 → 0.38 | 11.59s | UP @ 0.38 | -0.44 / 1.65 / · |
| 10-03 22:51:25 | SOL | up | 0.32→0.47 | 0.39 → 0.39 → 0.39 | 11.59s | UP @ 0.39 | -0.44 / 2.57 / · |
| 10-03 22:51:25 | DOGE | up | 0.19→0.40 | 0.25 → 0.25 → 0.25 | 11.59s | UP @ 0.26 | -0.47 / 3.09 / · |
| 10-03 22:51:15 | XRP | down | 0.32→0.26 | 0.34 → 0.34 → 0.34 | 6.84s | DOWN @ 0.67 | 0.19 / -2.04 / · |
| 10-03 22:51:00 | BNB | up | 0.48→0.58 | 0.72 → 0.72 → 0.72 | no | — |  |
| 10-03 22:50:55 | XRP | down | 0.38→0.32 | 0.34 → 0.34 → 0.34 | 27.10s | — |  |
| 10-03 22:50:53 | ETH | down | 0.38→0.32 | 0.40 → 0.38 → 0.38 | 14.10s | DOWN @ 0.63 | -0.44 / -0.44 / · |
| 10-03 22:50:50 | NEAR | up | 0.09→0.14 | 0.14 → 0.14 → 0.12 | 16.60s | — |  |
| 10-03 22:50:46 | HYPE | down | 0.37→0.31 | 0.20 → 0.20 → 0.20 | no | — |  |
| 10-03 22:50:40 | XRP | down | 0.44→0.38 | 0.45 → 0.45 → 0.45 | 12.12s | DOWN @ 0.56 | -0.46 / 0.66 / · |
| 10-03 22:50:39 | DOGE | down | 0.31→0.25 | 0.28 → 0.32 → 0.32 | 12.87s | DOWN @ 0.69 | -0.51 / 0.21 / · |
| 10-03 22:50:34 | SOL | up | 0.36→0.44 | 0.39 → 0.39 → 0.39 | no | — |  |
| 10-03 22:50:31 | HYPE | up | 0.23→0.32 | 0.23 → 0.23 → 0.23 | no | UP @ 0.24 | -0.74 / -0.26 / · |
| 10-03 22:50:24 | BNB | up | 0.43→0.52 | 0.69 → 0.69 → 0.69 | no | — |  |
| 10-03 22:50:19 | XRP | up | 0.33→0.41 | 0.43 → 0.43 → 0.30 | no | — |  |
| 10-03 22:50:18 | SOL | up | 0.36→0.44 | 0.56 → 0.56 → 0.39 | no | — |  |
| 10-03 22:50:13 | ZEC | down | 0.30→0.25 | 0.27 → 0.27 → 0.27 | 8.36s | — |  |
| 10-03 22:50:10 | BTC | down | 0.62→0.54 | 0.64 → 0.64 → 0.64 | no | DOWN @ 0.37 | -0.44 / -0.63 / · |
| 10-03 22:50:04 | XRP | up | 0.36→0.41 | 0.47 → 0.47 → 0.43 | no | — |  |
| 10-03 22:49:54 | SOL | up | 0.37→0.44 | 0.34 → 0.34 → 0.34 | 12.36s | UP @ 0.35 | -0.42 / -0.03 / · |
