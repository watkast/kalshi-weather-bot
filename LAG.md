# Lag Tracker

*Updated Sun Oct 04 02:34 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 447 | 10.5s | 4% | 0% |
| BTC | 356 | 12.4s | 2% | 0% |
| DOGE | 473 | 10.5s | 2% | 0% |
| ETH | 442 | 11.2s | 3% | 0% |
| HYPE | 353 | 11.8s | 3% | 0% |
| NEAR | 392 | 10.7s | 4% | 0% |
| SOL | 861 | 10.7s | 3% | 0% |
| XRP | 779 | 11.2s | 3% | 0% |
| ZEC | 498 | 9.7s | 5% | 0% |
| **All** | **4601** | **10.9s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2409 | 670 | $-276.92 | -2.7% | $-122.70 / $-154.22 |
| Sell after 30 sec | 2409 | 1398 | $763.95 | +7.3% | $447.43 / $316.52 |
| Hold to the close | 2384 | 1210 | $1793.93 | +17.4% | $958.79 / $835.14 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **38 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 02:33:58 | BNB | down | 0.62→0.36 | 0.65 → 0.65 → 0.65 | no | DOWN @ 0.36 | · / · / · |
| 10-04 02:33:43 | BNB | up | 0.56→0.62 | 0.58 → 0.58 → 0.58 | 9.83s | — |  |
| 10-04 02:33:40 | NEAR | up | 0.59→0.64 | 0.60 → 0.72 → 0.72 | 0.06s | — |  |
| 10-04 02:33:33 | HYPE | up | 0.59→0.67 | 0.59 → 0.59 → 0.60 | 19.58s | UP @ 0.60 | -0.34 / 0.37 / · |
| 10-04 02:33:32 | XRP | up | 0.58→0.66 | 0.66 → 0.66 → 0.66 | 6.08s | — |  |
| 10-04 02:33:31 | SOL | up | 0.61→0.79 | 0.66 → 0.66 → 0.66 | 7.08s | UP @ 0.66 | 0.60 / 1.02 / · |
| 10-04 02:33:31 | ETH | up | 0.54→0.62 | 0.54 → 0.54 → 0.54 | 7.33s | UP @ 0.54 | 1.99 / 1.78 / · |
| 10-04 02:33:30 | BTC | up | 0.50→0.59 | 0.56 → 0.56 → 0.56 | 8.08s | — |  |
| 10-04 02:33:26 | BNB | up | 0.23→0.45 | 0.43 → 0.43 → 0.43 | 12.08s | — |  |
| 10-04 02:33:17 | XRP | down | 0.58→0.53 | 0.62 → 0.62 → 0.62 | no | DOWN @ 0.39 | -0.83 / -1.42 / · |
| 10-04 02:33:15 | BTC | up | 0.40→0.52 | 0.48 → 0.48 → 0.48 | 8.08s | — |  |
| 10-04 02:33:15 | SOL | up | 0.57→0.64 | 0.61 → 0.61 → 0.61 | 8.33s | — |  |
| 10-04 02:32:52 | XRP | up | 0.50→0.55 | 0.58 → 0.58 → 0.59 | 16.34s | — |  |
| 10-04 02:32:48 | BNB | up | 0.16→0.46 | 0.43 → 0.43 → 0.46 | no | — |  |
| 10-04 02:32:48 | ZEC | up | 0.66→0.72 | 0.69 → 0.69 → 0.69 | 5.34s | — |  |
| 10-04 02:32:41 | SOL | up | 0.57→0.63 | 0.63 → 0.63 → 0.63 | no | — |  |
| 10-04 02:32:24 | XRP | down | 0.53→0.47 | 0.60 → 0.60 → 0.60 | no | DOWN @ 0.41 | -0.54 / -0.44 / · |
| 10-04 02:32:20 | BTC | up | 0.35→0.47 | 0.43 → 0.43 → 0.47 | no | — |  |
| 10-04 02:32:16 | BNB | down | 0.37→0.26 | 0.48 → 0.48 → 0.48 | no | DOWN @ 0.52 | 0.04 / 0.04 / · |
| 10-04 02:31:57 | SOL | up | 0.57→0.63 | 0.62 → 0.62 → 0.62 | no | — |  |
| 10-04 02:31:53 | DOGE | down | 0.56→0.39 | 0.49 → 0.52 → 0.52 | no | DOWN @ 0.49 | -0.56 / -0.66 / · |
| 10-04 02:31:36 | DOGE | up | 0.49→0.56 | 0.45 → 0.45 → 0.49 | 1.60s | UP @ 0.45 | -0.06 / 0.24 / · |
| 10-04 02:31:23 | HYPE | up | 0.48→0.55 | 0.54 → 0.53 → 0.53 | 29.86s | — |  |
| 10-04 02:31:17 | BNB | up | 0.23→0.34 | 0.56 → 0.56 → 0.56 | no | — |  |
| 10-04 02:31:17 | NEAR | down | 0.51→0.44 | 0.58 → 0.58 → 0.58 | no | DOWN @ 0.44 | -0.85 / -0.85 / · |
| 10-04 02:31:17 | DOGE | down | 0.46→0.33 | 0.49 → 0.49 → 0.49 | no | DOWN @ 0.51 | 0.04 / -0.46 / · |
| 10-04 02:31:17 | ETH | down | 0.58→0.43 | 0.51 → 0.51 → 0.51 | no | DOWN @ 0.50 | -0.46 / -0.66 / · |
| 10-04 02:31:16 | ZEC | down | 0.67→0.60 | 0.73 → 0.73 → 0.73 | no | DOWN @ 0.28 | -0.39 / -0.30 / · |
| 10-04 02:31:15 | SOL | down | 0.63→0.56 | 0.71 → 0.71 → 0.71 | 7.86s | DOWN @ 0.29 | 0.58 / 0.38 / · |
| 10-04 02:31:15 | XRP | down | 0.59→0.50 | 0.65 → 0.65 → 0.65 | no | DOWN @ 0.36 | -0.14 / -0.34 / · |
