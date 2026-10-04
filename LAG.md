# Lag Tracker

*Updated Sun Oct 04 04:34 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 512 | 10.7s | 4% | 0% |
| BTC | 404 | 11.9s | 2% | 0% |
| DOGE | 544 | 10.8s | 2% | 0% |
| ETH | 523 | 10.9s | 3% | 0% |
| HYPE | 430 | 11.6s | 4% | 0% |
| NEAR | 489 | 10.7s | 4% | 0% |
| SOL | 989 | 10.6s | 3% | 0% |
| XRP | 948 | 11.0s | 4% | 0% |
| ZEC | 632 | 9.8s | 4% | 0% |
| **All** | **5471** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2837 | 787 | $-346.20 | -2.8% | $-153.87 / $-192.33 |
| Sell after 30 sec | 2833 | 1631 | $841.24 | +6.8% | $496.15 / $345.09 |
| Hold to the close | 2820 | 1408 | $1838.43 | +15.0% | $867.45 / $970.98 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **14 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 04:34:11 | XRP | down | 0.63→0.53 | 0.70 → 0.70 → 0.69 | no | DOWN @ 0.30 | -0.30 / · / · |
| 10-04 04:34:02 | NEAR | down | 0.63→0.56 | 0.80 → 0.80 → 0.80 | 10.99s | DOWN @ 0.21 | -0.34 / · / · |
| 10-04 04:33:57 | HYPE | down | 0.54→0.45 | 0.57 → 0.59 → 0.59 | no | DOWN @ 0.42 | -0.55 / · / · |
| 10-04 04:33:54 | ZEC | down | 0.59→0.45 | 0.53 → 0.53 → 0.53 | no | DOWN @ 0.49 | -0.66 / · / · |
| 10-04 04:33:39 | ZEC | down | 0.49→0.39 | 0.57 → 0.57 → 0.53 | no | DOWN @ 0.45 | -0.26 / -0.26 / · |
| 10-04 04:33:34 | XRP | down | 0.62→0.53 | 0.69 → 0.69 → 0.69 | no | DOWN @ 0.31 | -0.40 / -0.50 / · |
| 10-04 04:33:26 | ETH | down | 0.47→0.42 | 0.46 → 0.46 → 0.46 | 17.25s | — |  |
| 10-04 04:33:25 | BNB | down | 0.30→0.25 | 0.52 → 0.52 → 0.46 | 2.99s | DOWN @ 0.49 | -0.06 / 0.14 / · |
| 10-04 04:33:10 | ZEC | down | 0.56→0.51 | 0.57 → 0.57 → 0.58 | no | DOWN @ 0.43 | -0.55 / -0.55 / · |
| 10-04 04:33:03 | XRP | up | 0.56→0.65 | 0.60 → 0.60 → 0.60 | 10.25s | — |  |
| 10-04 04:33:02 | NEAR | up | 0.57→0.62 | 0.69 → 0.69 → 0.69 | 11.00s | — |  |
| 10-04 04:32:49 | ZEC | down | 0.53→0.47 | 0.57 → 0.57 → 0.57 | no | DOWN @ 0.44 | -0.56 / -0.65 / · |
| 10-04 04:32:38 | BNB | down | 0.38→0.30 | 0.58 → 0.58 → 0.58 | 19.50s | DOWN @ 0.44 | -0.75 / 0.64 / · |
| 10-04 04:32:35 | DOGE | down | 0.62→0.51 | 0.62 → 0.62 → 0.62 | no | DOWN @ 0.38 | -1.12 / -1.22 / · |
| 10-04 04:32:34 | XRP | up | 0.53→0.59 | 0.61 → 0.61 → 0.61 | no | — |  |
| 10-04 04:32:25 | ZEC | down | 0.59→0.54 | 0.61 → 0.61 → 0.59 | 17.77s | DOWN @ 0.40 | -0.44 / -0.24 / · |
| 10-04 04:32:19 | XRP | down | 0.65→0.57 | 0.58 → 0.58 → 0.58 | no | — |  |
| 10-04 04:32:10 | BNB | up | 0.29→0.34 | 0.57 → 0.57 → 0.57 | no | — |  |
| 10-04 04:32:09 | ZEC | down | 0.64→0.55 | 0.65 → 0.65 → 0.61 | 19.01s | — |  |
| 10-04 04:32:09 | DOGE | up | 0.46→0.51 | 0.57 → 0.57 → 0.57 | 19.26s | — |  |
| 10-04 04:32:05 | SOL | down | 0.66→0.60 | 0.77 → 0.77 → 0.77 | 22.76s | DOWN @ 0.24 | -0.46 / 0.90 / · |
| 10-04 04:31:52 | BNB | up | 0.26→0.35 | 0.57 → 0.57 → 0.57 | no | — |  |
| 10-04 04:31:52 | ETH | down | 0.50→0.40 | 0.53 → 0.53 → 0.53 | no | DOWN @ 0.48 | -0.26 / -0.36 / · |
| 10-04 04:31:33 | XRP | down | 0.72→0.64 | 0.67 → 0.67 → 0.67 | no | — |  |
| 10-04 04:31:18 | ZEC | up | 0.52→0.58 | 0.49 → 0.49 → 0.49 | 25.02s | UP @ 0.50 | -0.26 / 0.55 / · |
| 10-04 04:31:02 | NEAR | down | 0.65→0.60 | 0.57 → 0.57 → 0.57 | no | — |  |
| 10-04 04:30:50 | XRP | up | 0.64→0.69 | 0.52 → 0.52 → 0.69 | 2.77s | UP @ 0.53 | 1.16 / 1.16 / · |
| 10-04 04:30:47 | ZEC | down | 0.54→0.48 | 0.52 → 0.52 → 0.52 | no | — |  |
| 10-04 04:30:43 | NEAR | up | 0.41→0.48 | 0.53 → 0.53 → 0.53 | 10.27s | — |  |
| 10-04 04:30:34 | XRP | up | 0.53→0.58 | 0.52 → 0.52 → 0.52 | 18.77s | UP @ 0.53 | -0.56 / 1.16 / · |
