# Lag Tracker

*Updated Sat Oct 03 21:23 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 231 | 10.4s | 6% | 0% |
| BTC | 145 | 11.6s | 2% | 0% |
| DOGE | 227 | 10.2s | 3% | 0% |
| ETH | 169 | 10.8s | 4% | 0% |
| HYPE | 160 | 11.6s | 4% | 0% |
| NEAR | 168 | 9.3s | 4% | 0% |
| SOL | 339 | 9.4s | 4% | 0% |
| XRP | 350 | 10.2s | 4% | 0% |
| ZEC | 246 | 9.6s | 5% | 0% |
| **All** | **2035** | **10.3s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1057 | 327 | $-88.23 | -2.0% | $-16.38 / $-71.85 |
| Sell after 30 sec | 1055 | 659 | $428.49 | +9.6% | $279.75 / $148.74 |
| Hold to the close | 1023 | 517 | $817.80 | +18.8% | $561.18 / $256.62 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 21:23:27 | DOGE | up | 0.29→0.37 | 0.35 → 0.35 → — | no | — |  |
| 10-03 21:23:26 | NEAR | down | 0.32→0.25 | 0.32 → 0.32 → — | no | — |  |
| 10-03 21:23:19 | XRP | down | 0.28→0.21 | 0.47 → 0.47 → 0.47 | 9.92s | DOWN @ 0.54 | · / · / · |
| 10-03 21:23:18 | ETH | down | 0.71→0.64 | 0.71 → 0.71 → 0.71 | no | DOWN @ 0.29 | -0.40 / · / · |
| 10-03 21:23:16 | SOL | down | 0.42→0.31 | 0.52 → 0.52 → 0.52 | no | DOWN @ 0.49 | -0.46 / · / · |
| 10-03 21:23:04 | XRP | up | 0.26→0.34 | 0.41 → 0.41 → 0.41 | 9.93s | — |  |
| 10-03 21:22:54 | ZEC | down | 0.29→0.20 | 0.25 → 0.25 → 0.24 | 19.68s | — |  |
| 10-03 21:22:51 | BTC | up | 0.71→0.77 | 0.79 → 0.79 → 0.79 | 7.68s | — |  |
| 10-03 21:22:51 | SOL | up | 0.35→0.58 | 0.40 → 0.40 → 0.40 | 22.93s | UP @ 0.40 | -0.05 / 0.75 / · |
| 10-03 21:22:51 | ETH | up | 0.60→0.71 | 0.61 → 0.61 → 0.61 | 22.93s | UP @ 0.62 | -0.34 / 0.58 / · |
| 10-03 21:22:51 | DOGE | up | 0.26→0.41 | 0.25 → 0.25 → 0.25 | 22.93s | UP @ 0.26 | -0.95 / 0.60 / · |
| 10-03 21:22:51 | NEAR | down | 0.34→0.29 | 0.28 → 0.28 → 0.28 | no | — |  |
| 10-03 21:22:46 | HYPE | down | 0.81→0.74 | 0.85 → 0.85 → 0.85 | no | DOWN @ 0.15 | -0.28 / -0.82 / · |
| 10-03 21:22:31 | ZEC | up | 0.26→0.34 | 0.17 → 0.17 → 0.17 | 12.93s | UP @ 0.19 | -0.70 / 0.26 / · |
| 10-03 21:22:18 | ETH | up | 0.54→0.63 | 0.64 → 0.64 → 0.57 | no | — |  |
| 10-03 21:21:57 | DOGE | down | 0.38→0.31 | 0.27 → 0.27 → 0.27 | no | — |  |
| 10-03 21:21:41 | DOGE | up | 0.31→0.38 | 0.28 → 0.28 → 0.28 | no | UP @ 0.29 | -0.59 / -0.78 / · |
| 10-03 21:21:41 | ETH | down | 0.58→0.51 | 0.65 → 0.65 → 0.65 | no | DOWN @ 0.36 | -0.43 / -0.34 / · |
| 10-03 21:21:39 | SOL | down | 0.33→0.28 | 0.36 → 0.36 → 0.36 | no | DOWN @ 0.64 | -0.44 / -0.64 / · |
| 10-03 21:21:31 | ZEC | down | 0.37→0.31 | 0.35 → 0.35 → 0.27 | 3.96s | — |  |
| 10-03 21:21:12 | ZEC | up | 0.33→0.39 | 0.25 → 0.25 → 0.25 | 7.72s | UP @ 0.26 | 0.50 / -0.28 / · |
| 10-03 21:20:18 | ZEC | down | 0.40→0.32 | 0.39 → 0.39 → 0.23 | 1.23s | — |  |
| 10-03 21:20:06 | SOL | down | 0.41→0.35 | 0.51 → 0.49 → 0.49 | 13.23s | DOWN @ 0.52 | -0.66 / 0.24 / · |
| 10-03 21:20:02 | XRP | up | 0.32→0.38 | 0.39 → 0.39 → 0.41 | no | — |  |
| 10-03 21:19:57 | BNB | up | 0.10→0.15 | 0.20 → 0.20 → 0.20 | no | — |  |
| 10-03 21:19:51 | BTC | up | 0.62→0.67 | 0.70 → 0.66 → 0.66 | no | — |  |
| 10-03 21:19:46 | XRP | up | 0.32→0.38 | 0.38 → 0.38 → 0.39 | no | — |  |
| 10-03 21:19:39 | BNB | down | 0.17→0.10 | 0.23 → 0.23 → 0.23 | 10.74s | DOWN @ 0.77 | -0.36 / -0.16 / · |
| 10-03 21:19:25 | SOL | down | 0.47→0.38 | 0.54 → 0.54 → 0.54 | no | DOWN @ 0.47 | -0.16 / -0.16 / · |
| 10-03 21:19:24 | XRP | down | 0.43→0.33 | 0.49 → 0.49 → 0.49 | 11.00s | DOWN @ 0.52 | -0.56 / 0.55 / · |
