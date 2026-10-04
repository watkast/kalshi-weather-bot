# Lag Tracker

*Updated Sun Oct 04 00:33 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 365 | 10.7s | 5% | 0% |
| BTC | 275 | 11.8s | 2% | 0% |
| DOGE | 393 | 10.6s | 2% | 0% |
| ETH | 347 | 10.9s | 3% | 0% |
| HYPE | 277 | 11.7s | 3% | 0% |
| NEAR | 316 | 10.2s | 3% | 0% |
| SOL | 668 | 10.2s | 3% | 0% |
| XRP | 627 | 11.2s | 3% | 0% |
| ZEC | 375 | 9.6s | 5% | 0% |
| **All** | **3643** | **10.7s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1906 | 540 | $-205.95 | -2.5% | $-74.98 / $-130.97 |
| Sell after 30 sec | 1904 | 1107 | $607.77 | +7.4% | $394.89 / $212.88 |
| Hold to the close | 1896 | 962 | $1463.70 | +17.9% | $678.82 / $784.88 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **39 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 00:33:42 | BNB | down | 0.43→0.36 | 0.66 → 0.66 → — | no | DOWN @ 0.36 | · / · / · |
| 10-04 00:33:42 | SOL | down | 0.45→0.38 | 0.52 → 0.52 → — | no | DOWN @ 0.50 | · / · / · |
| 10-04 00:33:42 | ETH | down | 0.48→0.40 | 0.52 → 0.52 → — | no | DOWN @ 0.49 | · / · / · |
| 10-04 00:33:42 | ZEC | down | 0.74→0.69 | 0.71 → 0.71 → — | no | — |  |
| 10-04 00:33:35 | XRP | up | 0.31→0.39 | 0.40 → 0.40 → 0.40 | no | — |  |
| 10-04 00:33:22 | BNB | up | 0.35→0.44 | 0.58 → 0.58 → 0.58 | 8.74s | — |  |
| 10-04 00:33:21 | NEAR | down | 0.29→0.24 | 0.30 → 0.30 → 0.30 | 9.49s | DOWN @ 0.71 | 0.22 / · / · |
| 10-04 00:33:15 | XRP | down | 0.36→0.31 | 0.40 → 0.40 → 0.38 | no | DOWN @ 0.61 | -0.24 / · / · |
| 10-04 00:33:15 | BTC | up | 0.43→0.51 | 0.53 → 0.53 → 0.52 | no | — |  |
| 10-04 00:32:57 | ETH | up | 0.41→0.46 | 0.46 → 0.46 → 0.47 | 18.50s | — |  |
| 10-04 00:32:57 | XRP | down | 0.36→0.31 | 0.39 → 0.39 → 0.40 | no | — |  |
| 10-04 00:32:55 | SOL | up | 0.46→0.60 | 0.54 → 0.54 → 0.54 | no | — |  |
| 10-04 00:32:08 | XRP | up | 0.30→0.37 | 0.40 → 0.40 → 0.40 | no | — |  |
| 10-04 00:31:55 | SOL | up | 0.42→0.53 | 0.56 → 0.56 → 0.56 | no | — |  |
| 10-04 00:31:53 | XRP | up | 0.31→0.37 | 0.38 → 0.38 → 0.38 | no | — |  |
| 10-04 00:31:53 | ETH | up | 0.25→0.33 | 0.29 → 0.29 → 0.29 | 8.26s | — |  |
| 10-04 00:31:40 | NEAR | down | 0.33→0.27 | 0.40 → 0.40 → 0.40 | 5.51s | DOWN @ 0.61 | -0.04 / 0.78 / · |
| 10-04 00:31:40 | SOL | down | 0.53→0.46 | 0.57 → 0.57 → 0.57 | no | DOWN @ 0.43 | -0.36 / -0.36 / · |
| 10-04 00:31:36 | ZEC | up | 0.47→0.52 | 0.45 → 0.45 → 0.45 | 9.76s | UP @ 0.45 | 0.04 / 0.94 / · |
| 10-04 00:31:29 | XRP | down | 0.40→0.31 | 0.46 → 0.46 → 0.46 | 16.77s | DOWN @ 0.55 | -0.46 / 0.35 / · |
| 10-04 00:31:28 | HYPE | down | 0.37→0.26 | 0.42 → 0.42 → 0.35 | 2.51s | DOWN @ 0.58 | 0.25 / 0.25 / · |
| 10-04 00:31:23 | NEAR | down | 0.50→0.45 | 0.52 → 0.52 → 0.52 | 7.51s | DOWN @ 0.50 | 0.55 / 1.05 / · |
| 10-04 00:31:21 | SOL | up | 0.49→0.56 | 0.56 → 0.56 → 0.56 | no | — |  |
| 10-04 00:31:19 | ZEC | down | 0.55→0.49 | 0.53 → 0.53 → 0.53 | 11.77s | — |  |
| 10-04 00:31:13 | ETH | down | 0.39→0.32 | 0.42 → 0.42 → 0.36 | 3.26s | DOWN @ 0.58 | 0.15 / 0.25 / · |
| 10-04 00:31:08 | NEAR | down | 0.50→0.45 | 0.51 → 0.51 → 0.51 | 22.52s | — |  |
| 10-04 00:31:07 | XRP | down | 0.42→0.35 | 0.54 → 0.54 → 0.54 | 9.02s | DOWN @ 0.47 | 0.34 / 0.34 / · |
| 10-04 00:31:06 | SOL | down | 0.52→0.46 | 0.57 → 0.57 → 0.57 | no | — |  |
| 10-04 00:28:26 | DOGE | down | 0.98→0.92 | 0.98 → 0.98 → 0.97 | no | — |  |
| 10-04 00:28:23 | HYPE | up | 0.45→0.63 | 0.73 → 0.73 → 0.73 | 8.04s | — |  |
