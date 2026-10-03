# Lag Tracker

*Updated Sat Oct 03 22:33 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 284 | 10.7s | 5% | 0% |
| BTC | 197 | 11.9s | 2% | 0% |
| DOGE | 291 | 10.1s | 2% | 0% |
| ETH | 251 | 11.0s | 3% | 0% |
| HYPE | 211 | 11.6s | 4% | 0% |
| NEAR | 235 | 10.4s | 3% | 0% |
| SOL | 474 | 9.6s | 4% | 0% |
| XRP | 443 | 10.3s | 4% | 0% |
| ZEC | 302 | 9.6s | 5% | 0% |
| **All** | **2688** | **10.5s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1407 | 407 | $-150.15 | -2.5% | $-50.48 / $-99.67 |
| Sell after 30 sec | 1405 | 842 | $494.79 | +8.2% | $317.52 / $177.27 |
| Hold to the close | 1388 | 686 | $931.38 | +15.7% | $591.86 / $339.52 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **37 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 22:33:41 | HYPE | up | 0.77→0.82 | 0.77 → 0.77 → 0.85 | 3.90s | UP @ 0.77 | 0.58 / · / · |
| 10-03 22:33:39 | SOL | up | 0.43→0.50 | 0.49 → 0.49 → 0.49 | 5.65s | — |  |
| 10-03 22:33:35 | NEAR | up | 0.61→0.72 | 0.63 → 0.63 → 0.63 | 10.40s | UP @ 0.64 | -0.54 / · / · |
| 10-03 22:33:33 | XRP | up | 0.55→0.65 | 0.64 → 0.67 → 0.67 | 12.40s | — |  |
| 10-03 22:33:23 | SOL | up | 0.37→0.43 | 0.44 → 0.44 → 0.44 | 6.65s | — |  |
| 10-03 22:33:20 | HYPE | up | 0.55→0.61 | 0.68 → 0.68 → 0.68 | 10.15s | — |  |
| 10-03 22:33:15 | XRP | down | 0.58→0.53 | 0.70 → 0.64 → 0.64 | 0.16s | DOWN @ 0.37 | -0.44 / -1.70 / · |
| 10-03 22:33:14 | NEAR | down | 0.66→0.57 | 0.69 → 0.69 → 0.73 | 15.65s | DOWN @ 0.31 | -0.79 / 0.18 / · |
| 10-03 22:33:13 | DOGE | down | 0.57→0.49 | 0.66 → 0.66 → 0.58 | 2.41s | DOWN @ 0.35 | 0.27 / 0.17 / · |
| 10-03 22:33:07 | ETH | down | 0.42→0.33 | 0.43 → 0.43 → 0.43 | no | DOWN @ 0.57 | -0.36 / -0.26 / · |
| 10-03 22:33:05 | SOL | down | 0.43→0.37 | 0.42 → 0.42 → 0.42 | no | — |  |
| 10-03 22:33:05 | BTC | down | 0.55→0.49 | 0.56 → 0.56 → 0.56 | 10.42s | DOWN @ 0.44 | -0.46 / -0.16 / · |
| 10-03 22:32:56 | BNB | up | 0.43→0.49 | 0.68 → 0.68 → 0.72 | 3.91s | — |  |
| 10-03 22:32:55 | XRP | up | 0.58→0.65 | 0.61 → 0.61 → 0.70 | 4.91s | — |  |
| 10-03 22:32:51 | NEAR | up | 0.60→0.67 | 0.70 → 0.70 → 0.70 | no | — |  |
| 10-03 22:32:47 | SOL | up | 0.37→0.44 | 0.41 → 0.41 → 0.41 | no | — |  |
| 10-03 22:32:41 | BNB | down | 0.49→0.43 | 0.69 → 0.69 → 0.68 | no | DOWN @ 0.32 | -0.32 / -0.80 / · |
| 10-03 22:32:32 | DOGE | down | 0.57→0.49 | 0.65 → 0.65 → 0.65 | no | DOWN @ 0.37 | -0.63 / -0.63 / · |
| 10-03 22:32:21 | SOL | down | 0.41→0.35 | 0.42 → 0.42 → 0.42 | no | DOWN @ 0.58 | -0.76 / -0.36 / · |
| 10-03 22:32:12 | XRP | up | 0.50→0.57 | 0.47 → 0.47 → 0.53 | 2.91s | UP @ 0.47 | 0.14 / 0.64 / · |
| 10-03 22:32:12 | DOGE | up | 0.49→0.54 | 0.59 → 0.59 → 0.61 | 18.17s | — |  |
| 10-03 22:32:12 | ZEC | up | 0.57→0.64 | 0.57 → 0.57 → 0.63 | 3.41s | UP @ 0.58 | 0.05 / 0.36 / · |
| 10-03 22:32:10 | BNB | down | 0.38→0.33 | 0.55 → 0.55 → 0.56 | no | DOWN @ 0.46 | -0.66 / -1.83 / · |
| 10-03 22:32:06 | SOL | down | 0.41→0.35 | 0.42 → 0.42 → 0.42 | no | DOWN @ 0.59 | -0.55 / -0.85 / · |
| 10-03 22:32:03 | NEAR | up | 0.59→0.64 | 0.65 → 0.65 → 0.65 | 11.92s | — |  |
| 10-03 22:31:47 | SOL | up | 0.35→0.41 | 0.41 → 0.41 → 0.41 | no | — |  |
| 10-03 22:31:45 | BNB | down | 0.38→0.30 | 0.54 → 0.55 → 0.55 | no | DOWN @ 0.46 | -0.46 / -0.66 / · |
| 10-03 22:31:39 | ETH | down | 0.44→0.39 | 0.47 → 0.47 → 0.47 | 5.67s | DOWN @ 0.53 | -0.16 / 0.14 / · |
| 10-03 22:31:37 | HYPE | down | 0.46→0.41 | 0.53 → 0.53 → 0.53 | no | DOWN @ 0.48 | -0.66 / -0.36 / · |
| 10-03 22:31:32 | DOGE | down | 0.48→0.41 | 0.56 → 0.55 → 0.55 | no | DOWN @ 0.46 | -0.56 / -0.95 / · |
