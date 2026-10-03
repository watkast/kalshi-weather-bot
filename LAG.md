# Lag Tracker

*Updated Sat Oct 03 23:53 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 326 | 10.8s | 5% | 0% |
| BTC | 250 | 11.8s | 2% | 0% |
| DOGE | 360 | 10.4s | 2% | 0% |
| ETH | 312 | 11.0s | 3% | 0% |
| HYPE | 255 | 11.6s | 3% | 0% |
| NEAR | 285 | 10.5s | 4% | 0% |
| SOL | 622 | 10.0s | 3% | 0% |
| XRP | 572 | 10.9s | 4% | 0% |
| ZEC | 345 | 9.5s | 5% | 0% |
| **All** | **3327** | **10.6s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1738 | 498 | $-190.72 | -2.5% | $-63.25 / $-127.47 |
| Sell after 30 sec | 1737 | 1014 | $558.76 | +7.5% | $364.23 / $194.53 |
| Hold to the close | 1698 | 850 | $1200.37 | +16.4% | $546.15 / $654.22 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **38 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 23:53:33 | SOL | up | 0.27→0.43 | 0.64 → 0.64 → — | no | — |  |
| 10-03 23:53:33 | DOGE | up | 0.27→0.32 | 0.39 → 0.39 → — | no | — |  |
| 10-03 23:53:18 | SOL | up | 0.39→0.49 | 0.64 → 0.64 → 0.64 | no | — |  |
| 10-03 23:53:18 | DOGE | up | 0.19→0.27 | 0.42 → 0.42 → 0.39 | no | — |  |
| 10-03 23:53:13 | XRP | up | 0.27→0.36 | 0.56 → 0.56 → 0.56 | no | — |  |
| 10-03 23:53:09 | NEAR | down | 0.76→0.69 | 0.86 → 0.86 → 0.86 | 12.29s | DOWN @ 0.15 | -0.47 / · / · |
| 10-03 23:53:02 | SOL | down | 0.49→0.44 | 0.62 → 0.62 → 0.62 | no | DOWN @ 0.38 | -0.54 / -0.54 / · |
| 10-03 23:52:58 | XRP | down | 0.45→0.36 | 0.56 → 0.58 → 0.58 | 22.79s | DOWN @ 0.42 | -0.45 / 0.24 / · |
| 10-03 23:52:43 | XRP | up | 0.36→0.45 | 0.56 → 0.56 → 0.56 | no | — |  |
| 10-03 23:52:35 | ETH | down | 0.49→0.33 | 0.41 → 0.41 → 0.41 | no | DOWN @ 0.60 | -0.85 / -0.85 / · |
| 10-03 23:52:28 | XRP | up | 0.32→0.41 | 0.69 → 0.69 → 0.69 | no | — |  |
| 10-03 23:52:27 | BNB | up | 0.21→0.27 | 0.41 → 0.41 → 0.41 | 29.05s | — |  |
| 10-03 23:52:25 | SOL | down | 0.54→0.44 | 0.54 → 0.54 → 0.60 | no | DOWN @ 0.48 | -1.25 / -0.96 / · |
| 10-03 23:52:25 | BTC | down | 0.20→0.10 | 0.30 → 0.30 → 0.32 | no | DOWN @ 0.70 | -0.51 / -0.61 / · |
| 10-03 23:52:25 | DOGE | down | 0.38→0.28 | 0.55 → 0.55 → 0.53 | 15.79s | DOWN @ 0.46 | -0.26 / 0.64 / · |
| 10-03 23:52:13 | XRP | down | 0.59→0.46 | 0.74 → 0.74 → 0.74 | 27.80s | DOWN @ 0.26 | -0.38 / 1.38 / · |
| 10-03 23:52:03 | DOGE | down | 0.49→0.37 | 0.56 → 0.56 → 0.56 | no | DOWN @ 0.45 | -0.36 / -0.16 / · |
| 10-03 23:51:55 | BNB | down | 0.40→0.31 | 0.43 → 0.43 → 0.41 | no | DOWN @ 0.58 | -0.25 / -0.36 / · |
| 10-03 23:51:53 | NEAR | up | 0.62→0.67 | 0.76 → 0.76 → 0.78 | 17.79s | — |  |
| 10-03 23:51:48 | DOGE | up | 0.29→0.49 | 0.56 → 0.56 → 0.56 | no | — |  |
| 10-03 23:51:34 | XRP | up | 0.46→0.54 | 0.69 → 0.69 → 0.69 | 21.79s | — |  |
| 10-03 23:51:30 | DOGE | down | 0.49→0.44 | 0.57 → 0.57 → 0.57 | no | DOWN @ 0.43 | -0.46 / -0.36 / · |
| 10-03 23:51:19 | XRP | down | 0.54→0.46 | 0.68 → 0.68 → 0.68 | no | DOWN @ 0.33 | -0.51 / -0.61 / · |
| 10-03 23:51:15 | SOL | up | 0.45→0.54 | 0.48 → 0.48 → 0.48 | 11.04s | — |  |
| 10-03 23:51:12 | DOGE | down | 0.44→0.30 | 0.77 → 0.56 → 0.56 | 0.02s | DOWN @ 0.44 | -0.46 / -0.46 / · |
| 10-03 23:51:08 | BNB | down | 0.30→0.21 | 0.42 → 0.42 → 0.38 | no | DOWN @ 0.58 | -0.25 / -0.46 / · |
| 10-03 23:51:04 | XRP | up | 0.46→0.54 | 0.64 → 0.64 → 0.64 | 21.79s | — |  |
| 10-03 23:51:01 | ETH | down | 0.57→0.33 | 0.56 → 0.56 → 0.56 | 24.79s | DOWN @ 0.45 | 0.74 / 1.05 / · |
| 10-03 23:51:00 | BTC | down | 0.25→0.12 | 0.30 → 0.30 → 0.30 | 11.04s | DOWN @ 0.70 | -0.40 / -0.10 / · |
| 10-03 23:50:50 | NEAR | up | 0.49→0.54 | 0.53 → 0.53 → 0.53 | 6.03s | — |  |
