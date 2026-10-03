# Lag Tracker

*Updated Sat Oct 03 21:53 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 253 | 10.7s | 5% | 0% |
| BTC | 161 | 11.9s | 2% | 0% |
| DOGE | 253 | 10.5s | 2% | 0% |
| ETH | 203 | 11.3s | 3% | 0% |
| HYPE | 181 | 11.2s | 4% | 0% |
| NEAR | 189 | 10.2s | 4% | 0% |
| SOL | 398 | 9.6s | 4% | 0% |
| XRP | 382 | 10.3s | 4% | 0% |
| ZEC | 277 | 9.6s | 5% | 0% |
| **All** | **2297** | **10.6s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1205 | 352 | $-123.57 | -2.4% | $-35.55 / $-88.02 |
| Sell after 30 sec | 1204 | 729 | $447.43 | +8.8% | $295.81 / $151.62 |
| Hold to the close | 1166 | 585 | $891.22 | +18.0% | $575.82 / $315.40 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 21:53:36 | SOL | up | 0.72→0.82 | 0.90 → 0.90 → — | no | — |  |
| 10-03 21:53:34 | NEAR | down | 0.54→0.48 | 0.68 → 0.68 → 0.68 | no | DOWN @ 0.34 | · / · / · |
| 10-03 21:53:31 | XRP | up | 0.43→0.50 | 0.64 → 0.64 → 0.64 | no | — |  |
| 10-03 21:53:21 | SOL | down | 0.79→0.72 | 0.84 → 0.84 → 0.90 | no | DOWN @ 0.17 | -0.87 / · / · |
| 10-03 21:53:16 | XRP | up | 0.43→0.50 | 0.64 → 0.64 → 0.64 | no | — |  |
| 10-03 21:53:06 | SOL | down | 0.78→0.72 | 0.81 → 0.81 → 0.84 | no | DOWN @ 0.20 | -0.71 / -1.19 / · |
| 10-03 21:53:00 | XRP | down | 0.53→0.44 | 0.63 → 0.63 → 0.63 | no | DOWN @ 0.38 | -0.54 / -0.54 / · |
| 10-03 21:52:52 | BNB | up | 0.50→0.57 | 0.57 → 0.57 → 0.59 | 16.98s | — |  |
| 10-03 21:52:45 | XRP | up | 0.47→0.53 | 0.56 → 0.56 → 0.56 | 8.22s | — |  |
| 10-03 21:52:41 | SOL | up | 0.60→0.67 | 0.74 → 0.74 → 0.74 | 12.23s | — |  |
| 10-03 21:52:30 | XRP | down | 0.44→0.39 | 0.51 → 0.51 → 0.51 | no | DOWN @ 0.50 | -1.06 / -1.75 / · |
| 10-03 21:52:29 | NEAR | up | 0.46→0.54 | 0.63 → 0.63 → 0.63 | no | — |  |
| 10-03 21:52:27 | ETH | up | 0.54→0.61 | 0.54 → 0.54 → 0.54 | 11.48s | UP @ 0.54 | -0.46 / 1.27 / · |
| 10-03 21:52:24 | HYPE | down | 0.41→0.32 | 0.57 → 0.42 → 0.42 | 0.19s | DOWN @ 0.60 | -0.75 / -1.65 / · |
| 10-03 21:52:21 | BNB | down | 0.59→0.46 | 0.81 → 0.81 → 0.57 | 2.23s | DOWN @ 0.20 | 1.90 / 1.90 / · |
| 10-03 21:52:14 | XRP | down | 0.59→0.44 | 0.76 → 0.76 → 0.76 | 9.73s | DOWN @ 0.25 | 2.08 / 1.48 / · |
| 10-03 21:52:13 | SOL | down | 0.67→0.56 | 0.80 → 0.80 → 0.80 | 10.48s | DOWN @ 0.21 | -0.34 / 0.14 / · |
| 10-03 21:52:13 | BTC | down | 0.78→0.70 | 0.90 → 0.90 → 0.90 | 10.48s | DOWN @ 0.11 | -0.24 / 0.81 / · |
| 10-03 21:52:13 | DOGE | down | 0.85→0.73 | 0.93 → 0.93 → 0.93 | 10.48s | DOWN @ 0.07 | -0.11 / 0.93 / · |
| 10-03 21:52:13 | NEAR | down | 0.58→0.51 | 0.74 → 0.74 → 0.74 | 10.73s | DOWN @ 0.28 | -0.68 / 0.88 / · |
| 10-03 21:52:12 | ETH | down | 0.82→0.77 | 0.84 → 0.84 → 0.84 | 11.48s | DOWN @ 0.16 | -0.29 / 2.13 / · |
| 10-03 21:51:59 | XRP | down | 0.61→0.56 | 0.74 → 0.74 → 0.74 | 24.74s | DOWN @ 0.27 | -0.67 / 1.88 / · |
| 10-03 21:51:55 | SOL | up | 0.59→0.67 | 0.91 → 0.79 → 0.79 | no | — |  |
| 10-03 21:51:51 | HYPE | up | 0.44→0.50 | 0.56 → 0.56 → 0.55 | no | — |  |
| 10-03 21:51:40 | XRP | down | 0.61→0.56 | 0.72 → 0.72 → 0.72 | no | DOWN @ 0.28 | -0.39 / -0.78 / · |
| 10-03 21:51:40 | SOL | down | 0.79→0.70 | 0.91 → 0.91 → 0.91 | 13.49s | DOWN @ 0.09 | -0.17 / 0.88 / · |
| 10-03 21:51:21 | XRP | down | 0.58→0.53 | 0.70 → 0.70 → 0.69 | no | DOWN @ 0.31 | -0.40 / -0.69 / · |
| 10-03 21:51:12 | NEAR | up | 0.52→0.57 | 0.59 → 0.59 → 0.59 | 11.74s | — |  |
| 10-03 21:51:10 | ETH | up | 0.66→0.71 | 0.74 → 0.76 → 0.76 | 29.00s | — |  |
| 10-03 21:51:06 | XRP | up | 0.53→0.58 | 0.64 → 0.64 → 0.70 | 2.99s | — |  |
