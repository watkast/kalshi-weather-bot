# Lag Tracker

*Updated Sun Oct 04 02:44 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 451 | 10.6s | 4% | 0% |
| BTC | 363 | 12.4s | 2% | 0% |
| DOGE | 482 | 10.5s | 2% | 0% |
| ETH | 454 | 11.2s | 3% | 0% |
| HYPE | 364 | 11.8s | 3% | 0% |
| NEAR | 397 | 10.8s | 4% | 0% |
| SOL | 885 | 10.6s | 3% | 0% |
| XRP | 804 | 11.1s | 4% | 0% |
| ZEC | 509 | 9.8s | 5% | 0% |
| **All** | **4709** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2475 | 693 | $-281.64 | -2.6% | $-121.65 / $-159.99 |
| Sell after 30 sec | 2474 | 1434 | $776.45 | +7.3% | $459.54 / $316.91 |
| Hold to the close | 2395 | 1212 | $1764.87 | +17.0% | $959.99 / $804.88 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **39 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 02:43:38 | SOL | down | 0.75→0.63 | 0.80 → 0.92 → 0.92 | no | DOWN @ 0.10 | -0.51 / · / · |
| 10-04 02:43:30 | XRP | down | 0.97→0.91 | 0.94 → 0.94 → 0.94 | no | — |  |
| 10-04 02:43:22 | SOL | up | 0.61→0.73 | 0.91 → 0.91 → 0.80 | no | — |  |
| 10-04 02:43:13 | XRP | up | 0.88→0.95 | 0.92 → 0.92 → 0.92 | no | — |  |
| 10-04 02:43:13 | ZEC | up | 0.87→0.93 | 0.93 → 0.93 → 0.93 | 9.79s | — |  |
| 10-04 02:43:00 | ETH | down | 0.10→0.05 | 0.09 → 0.09 → 0.09 | 22.54s | — |  |
| 10-04 02:42:56 | XRP | down | 0.93→0.86 | 0.93 → 0.93 → 0.93 | no | DOWN @ 0.08 | -0.29 / -0.47 / · |
| 10-04 02:42:51 | HYPE | down | 0.66→0.58 | 0.66 → 0.66 → 0.76 | no | DOWN @ 0.35 | -1.39 / -1.39 / · |
| 10-04 02:42:51 | ZEC | down | 0.95→0.89 | 0.99 → 0.99 → 0.99 | 16.79s | — |  |
| 10-04 02:42:50 | SOL | up | 0.68→0.84 | 0.81 → 0.81 → 0.86 | 17.79s | — |  |
| 10-04 02:42:38 | BTC | down | 0.11→0.04 | 0.03 → 0.10 → 0.10 | no | DOWN @ 0.90 | -0.24 / 0.42 / · |
| 10-04 02:42:35 | SOL | up | 0.58→0.82 | 0.34 → 0.34 → 0.81 | 2.78s | UP @ 0.35 | 4.33 / 4.64 / · |
| 10-04 02:42:28 | ETH | down | 0.29→0.21 | 0.08 → 0.08 → 0.08 | no | — |  |
| 10-04 02:42:20 | NEAR | up | 0.05→0.12 | 0.06 → 0.06 → 0.05 | 17.29s | UP @ 0.06 | -0.17 / 1.31 / · |
| 10-04 02:42:20 | BTC | up | 0.01→0.15 | 0.03 → 0.03 → 0.03 | 17.29s | — |  |
| 10-04 02:42:20 | HYPE | up | 0.32→0.51 | 0.38 → 0.38 → 0.37 | 17.29s | — |  |
| 10-04 02:42:20 | XRP | up | 0.43→0.76 | 0.53 → 0.53 → 0.81 | 2.28s | UP @ 0.53 | 2.40 / 3.58 / · |
| 10-04 02:42:20 | SOL | down | 0.26→0.20 | 0.35 → 0.35 → 0.34 | no | — |  |
| 10-04 02:42:20 | ZEC | up | 0.83→0.89 | 0.83 → 0.83 → 0.92 | 3.03s | UP @ 0.86 | 0.14 / 1.20 / · |
| 10-04 02:42:12 | ETH | up | 0.02→0.07 | 0.03 → 0.03 → 0.03 | 10.54s | — |  |
| 10-04 02:42:02 | SOL | up | 0.21→0.27 | 0.43 → 0.43 → 0.43 | no | — |  |
| 10-04 02:42:00 | XRP | down | 0.44→0.32 | 0.49 → 0.49 → 0.49 | no | DOWN @ 0.52 | -0.86 / -3.59 / · |
| 10-04 02:41:53 | HYPE | down | 0.51→0.39 | 0.41 → 0.40 → 0.40 | no | — |  |
| 10-04 02:41:52 | ZEC | down | 0.69→0.64 | 0.78 → 0.79 → 0.79 | no | DOWN @ 0.23 | -0.55 / -1.12 / · |
| 10-04 02:41:42 | SOL | down | 0.49→0.42 | 0.58 → 0.58 → 0.58 | 10.29s | DOWN @ 0.44 | -0.75 / 1.65 / · |
| 10-04 02:41:37 | ZEC | down | 0.76→0.70 | 0.65 → 0.78 → 0.78 | no | DOWN @ 0.24 | -0.55 / -0.65 / · |
| 10-04 02:41:35 | XRP | up | 0.38→0.56 | 0.51 → 0.51 → 0.67 | 2.78s | UP @ 0.51 | 1.16 / -0.66 / · |
| 10-04 02:41:34 | DOGE | up | 0.69→0.92 | 0.70 → 0.70 → 0.72 | no | UP @ 0.71 | -0.40 / 0.63 / · |
| 10-04 02:41:23 | ETH | down | 0.17→0.11 | 0.15 → 0.12 → 0.12 | 15.04s | — |  |
| 10-04 02:41:22 | ZEC | up | 0.54→0.64 | 0.70 → 0.65 → 0.65 | 15.29s | — |  |
