# Lag Tracker

*Updated Sun Oct 04 07:35 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 609 | 11.1s | 3% | 0% |
| BTC | 472 | 11.9s | 3% | 0% |
| DOGE | 657 | 10.4s | 2% | 0% |
| ETH | 642 | 11.3s | 3% | 0% |
| HYPE | 541 | 11.4s | 4% | 0% |
| NEAR | 620 | 10.8s | 3% | 0% |
| SOL | 1166 | 10.8s | 3% | 0% |
| XRP | 1164 | 10.8s | 3% | 0% |
| ZEC | 772 | 9.6s | 3% | 0% |
| **All** | **6643** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3395 | 949 | $-397.87 | -2.7% | $-180.44 / $-217.43 |
| Sell after 30 sec | 3392 | 1955 | $1052.79 | +7.2% | $562.42 / $490.37 |
| Hold to the close | 3375 | 1684 | $2233.79 | +15.3% | $1180.19 / $1053.60 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **31 ms** · Coinbase price delay: **15 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 07:35:03 | NEAR | down | 0.42→0.35 | 0.50 → 0.47 → — | no | DOWN @ 0.54 | · / · / · |
| 10-04 07:34:57 | ZEC | down | 0.54→0.49 | 0.55 → 0.55 → 0.52 | 4.03s | DOWN @ 0.46 | · / · / · |
| 10-04 07:34:42 | HYPE | down | 0.69→0.49 | 0.69 → 0.69 → 0.71 | 18.54s | DOWN @ 0.32 | -0.71 / · / · |
| 10-04 07:34:40 | SOL | up | 0.10→0.15 | 0.10 → 0.10 → 0.10 | 5.54s | UP @ 0.11 | 0.14 / · / · |
| 10-04 07:34:38 | XRP | up | 0.12→0.18 | 0.12 → 0.12 → 0.12 | 7.79s | UP @ 0.13 | 0.22 / · / · |
| 10-04 07:34:27 | ZEC | down | 0.53→0.45 | 0.56 → 0.56 → 0.51 | 3.55s | DOWN @ 0.44 | 0.14 / -0.36 / · |
| 10-04 07:34:18 | NEAR | down | 0.45→0.35 | 0.26 → 0.31 → 0.31 | no | — |  |
| 10-04 07:34:03 | NEAR | up | 0.23→0.30 | 0.26 → 0.26 → 0.26 | 12.55s | — |  |
| 10-04 07:34:02 | ZEC | down | 0.55→0.46 | 0.59 → 0.55 → 0.55 | 29.06s | DOWN @ 0.46 | -0.56 / -0.06 / · |
| 10-04 07:33:53 | HYPE | down | 0.71→0.66 | 0.68 → 0.68 → 0.68 | no | — |  |
| 10-04 07:33:33 | SOL | down | 0.17→0.12 | 0.15 → 0.14 → 0.14 | 13.06s | — |  |
| 10-04 07:33:32 | BTC | down | 0.20→0.13 | 0.15 → 0.14 → 0.14 | no | — |  |
| 10-04 07:33:06 | ZEC | down | 0.50→0.42 | 0.51 → 0.51 → 0.51 | no | DOWN @ 0.50 | -0.56 / -0.86 / · |
| 10-04 07:32:54 | ETH | up | 0.31→0.38 | 0.24 → 0.24 → 0.24 | 6.82s | UP @ 0.25 | 0.40 / 0.31 / · |
| 10-04 07:32:51 | HYPE | up | 0.53→0.59 | 0.60 → 0.60 → 0.60 | no | — |  |
| 10-04 07:32:39 | ETH | up | 0.26→0.31 | 0.26 → 0.26 → 0.26 | 21.82s | UP @ 0.26 | -0.47 / 0.30 / · |
| 10-04 07:32:32 | XRP | down | 0.20→0.15 | 0.21 → 0.17 → 0.17 | 0.06s | — |  |
| 10-04 07:32:26 | NEAR | down | 0.35→0.23 | 0.39 → 0.39 → 0.39 | 5.10s | DOWN @ 0.62 | 0.58 / 0.58 / · |
| 10-04 07:32:24 | HYPE | down | 0.59→0.53 | 0.58 → 0.58 → 0.58 | 7.10s | — |  |
| 10-04 07:32:20 | ETH | down | 0.36→0.29 | 0.34 → 0.34 → 0.34 | 10.60s | — |  |
| 10-04 07:32:18 | ZEC | down | 0.50→0.45 | 0.47 → 0.47 → 0.47 | no | — |  |
| 10-04 07:32:18 | DOGE | down | 0.33→0.22 | 0.23 → 0.26 → 0.26 | no | — |  |
| 10-04 07:32:11 | NEAR | down | 0.43→0.35 | 0.45 → 0.45 → 0.45 | 5.08s | DOWN @ 0.57 | -0.05 / 1.07 / · |
| 10-04 07:32:02 | ETH | up | 0.38→0.43 | 0.33 → 0.33 → 0.33 | no | UP @ 0.34 | -0.52 / -1.20 / · |
| 10-04 07:31:54 | ZEC | up | 0.40→0.49 | 0.33 → 0.33 → 0.33 | 6.58s | UP @ 0.34 | 0.96 / 0.86 / · |
| 10-04 07:31:54 | HYPE | up | 0.49→0.62 | 0.55 → 0.55 → 0.55 | no | UP @ 0.56 | -0.05 / -0.26 / · |
| 10-04 07:31:54 | DOGE | up | 0.24→0.33 | 0.23 → 0.23 → 0.23 | no | UP @ 0.23 | -0.36 / -0.07 / · |
| 10-04 07:31:54 | SOL | up | 0.26→0.47 | 0.20 → 0.20 → 0.20 | 6.58s | UP @ 0.20 | 0.92 / 0.15 / · |
| 10-04 07:31:54 | BTC | up | 0.23→0.30 | 0.20 → 0.20 → 0.20 | 6.58s | UP @ 0.21 | 0.34 / 0.24 / · |
| 10-04 07:31:54 | XRP | up | 0.25→0.32 | 0.21 → 0.21 → 0.21 | 6.58s | UP @ 0.22 | 0.13 / -0.35 / · |
