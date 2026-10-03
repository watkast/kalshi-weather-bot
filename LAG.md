# Lag Tracker

*Updated Sat Oct 03 17:52 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 48 | 11.1s | 6% | 0% |
| BTC | 37 | 11.2s | 3% | 0% |
| DOGE | 36 | 9.5s | 6% | 0% |
| ETH | 40 | 9.6s | 2% | 0% |
| HYPE | 29 | 10.6s | 3% | 0% |
| NEAR | 22 | 8.9s | 9% | 0% |
| SOL | 67 | 6.1s | 6% | 0% |
| XRP | 61 | 7.7s | 13% | 0% |
| ZEC | 56 | 9.9s | 7% | 0% |
| **All** | **396** | **9.2s** | **7%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 208 | 74 | $-10.95 | -1.3% | $-4.26 / $-6.69 |
| Sell after 30 sec | 207 | 141 | $110.59 | +13.1% | $56.92 / $53.67 |
| Hold to the close | 166 | 82 | $159.60 | +24.2% | $101.63 / $57.97 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **34 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 17:52:07 | XRP | up | 0.37→0.42 | 0.47 → 0.47 → — | no | — |  |
| 10-03 17:52:05 | ZEC | down | 0.68→0.62 | 0.74 → 0.74 → — | 3.35s | DOWN @ 0.26 | · / · / · |
| 10-03 17:52:01 | BTC | down | 0.59→0.50 | 0.54 → 0.54 → 0.54 | no | — |  |
| 10-03 17:51:50 | ZEC | down | 0.76→0.70 | 0.58 → 0.58 → 0.74 | no | — |  |
| 10-03 17:51:49 | SOL | down | 0.35→0.29 | 0.26 → 0.26 → 0.26 | no | — |  |
| 10-03 17:51:47 | XRP | down | 0.44→0.38 | 0.33 → 0.33 → 0.33 | no | — |  |
| 10-03 17:51:45 | DOGE | up | 0.47→0.60 | 0.60 → 0.60 → 0.60 | no | — |  |
| 10-03 17:51:42 | BTC | up | 0.53→0.59 | 0.46 → 0.46 → 0.46 | 11.87s | UP @ 0.46 | -0.46 / · / · |
| 10-03 17:51:37 | ETH | up | 0.79→0.85 | 0.81 → 0.81 → 0.77 | 16.63s | — |  |
| 10-03 17:51:34 | HYPE | down | 0.69→0.54 | 0.81 → 0.81 → 0.78 | no | DOWN @ 0.20 | -0.14 / -0.05 / · |
| 10-03 17:51:32 | SOL | down | 0.30→0.25 | 0.35 → 0.35 → 0.35 | 6.61s | DOWN @ 0.66 | 0.50 / -0.12 / · |
| 10-03 17:51:31 | ZEC | down | 0.62→0.55 | 0.58 → 0.58 → 0.58 | no | — |  |
| 10-03 17:51:26 | BTC | down | 0.59→0.47 | 0.57 → 0.57 → 0.57 | 13.11s | DOWN @ 0.43 | -0.46 / -0.06 / · |
| 10-03 17:51:26 | DOGE | down | 0.59→0.54 | 0.68 → 0.68 → 0.68 | 13.11s | DOWN @ 0.33 | -0.42 / 0.07 / · |
| 10-03 17:51:26 | XRP | down | 0.44→0.35 | 0.53 → 0.41 → 0.41 | 0.07s | DOWN @ 0.60 | -0.44 / -1.05 / · |
| 10-03 17:51:19 | HYPE | up | 0.71→0.76 | 0.79 → 0.79 → 0.81 | no | — |  |
| 10-03 17:51:16 | ZEC | up | 0.62→0.68 | 0.48 → 0.48 → 0.48 | 8.11s | UP @ 0.49 | 0.54 / 0.54 / · |
| 10-03 17:51:14 | SOL | down | 0.44→0.36 | 0.43 → 0.43 → 0.43 | 9.86s | DOWN @ 0.57 | 0.25 / 1.38 / · |
| 10-03 17:51:14 | NEAR | down | 0.30→0.22 | 0.28 → 0.28 → 0.28 | 25.12s | DOWN @ 0.73 | -0.39 / 0.34 / · |
| 10-03 17:51:08 | BTC | down | 0.65→0.59 | 0.59 → 0.59 → 0.65 | no | — |  |
| 10-03 17:51:06 | XRP | up | 0.42→0.48 | 0.41 → 0.41 → 0.53 | 2.36s | UP @ 0.42 | 0.64 / -0.55 / · |
| 10-03 17:51:00 | ZEC | up | 0.44→0.54 | 0.27 → 0.27 → 0.27 | 9.12s | UP @ 0.27 | 1.78 / 2.78 / · |
| 10-03 17:50:53 | HYPE | up | 0.61→0.70 | 0.69 → 0.69 → 0.70 | 15.87s | — |  |
| 10-03 17:50:52 | SOL | down | 0.42→0.36 | 0.43 → 0.43 → 0.41 | no | DOWN @ 0.58 | -0.46 / -0.56 / · |
| 10-03 17:50:51 | XRP | up | 0.37→0.42 | 0.43 → 0.43 → 0.41 | 17.37s | — |  |
| 10-03 17:50:48 | BTC | down | 0.64→0.58 | 0.57 → 0.57 → 0.57 | no | — |  |
| 10-03 17:50:48 | DOGE | down | 0.63→0.54 | 0.73 → 0.73 → 0.73 | no | DOWN @ 0.27 | -0.28 / 0.01 / · |
| 10-03 17:50:45 | ZEC | down | 0.30→0.24 | 0.16 → 0.16 → 0.16 | no | — |  |
| 10-03 17:50:37 | SOL | down | 0.53→0.47 | 0.26 → 0.26 → 0.43 | no | — |  |
| 10-03 17:50:36 | XRP | down | 0.54→0.48 | 0.23 → 0.23 → 0.43 | no | — |  |
