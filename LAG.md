# Lag Tracker

*Updated Sun Oct 04 08:55 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 637 | 11.2s | 3% | 0% |
| BTC | 513 | 11.9s | 3% | 0% |
| DOGE | 706 | 10.4s | 2% | 0% |
| ETH | 685 | 11.2s | 4% | 0% |
| HYPE | 591 | 11.3s | 4% | 0% |
| NEAR | 684 | 10.8s | 4% | 0% |
| SOL | 1257 | 10.8s | 3% | 0% |
| XRP | 1275 | 10.8s | 4% | 0% |
| ZEC | 858 | 9.6s | 4% | 0% |
| **All** | **7206** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3700 | 1045 | $-420.86 | -2.6% | $-199.55 / $-221.31 |
| Sell after 30 sec | 3699 | 2158 | $1200.92 | +7.5% | $597.27 / $603.65 |
| Hold to the close | 3665 | 1813 | $2345.29 | +14.9% | $1485.94 / $859.35 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **31 ms** · Coinbase price delay: **15 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 08:55:12 | XRP | down | 0.13→0.07 | 0.12 → 0.12 → 0.06 | 2.03s | DOWN @ 0.89 | 0.40 / · / · |
| 10-04 08:54:55 | DOGE | up | 0.38→0.44 | 0.45 → 0.45 → 0.46 | 19.03s | — |  |
| 10-04 08:54:44 | BNB | up | 0.88→0.94 | 0.99 → 0.99 → 0.99 | no | — |  |
| 10-04 08:54:40 | DOGE | down | 0.51→0.39 | 0.40 → 0.40 → 0.45 | no | — |  |
| 10-04 08:54:23 | XRP | down | 0.18→0.13 | 0.12 → 0.12 → 0.12 | no | — |  |
| 10-04 08:54:03 | BNB | up | 0.60→0.87 | 0.91 → 0.91 → 0.91 | no | — |  |
| 10-04 08:53:55 | HYPE | down | 0.23→0.17 | 0.17 → 0.17 → 0.12 | 4.03s | — |  |
| 10-04 08:53:54 | DOGE | up | 0.40→0.47 | 0.41 → 0.41 → 0.42 | no | UP @ 0.42 | -0.36 / -0.65 / · |
| 10-04 08:53:50 | SOL | down | 0.29→0.22 | 0.26 → 0.26 → 0.26 | no | — |  |
| 10-04 08:53:24 | ZEC | down | 0.15→0.09 | 0.12 → 0.12 → 0.06 | 4.53s | — |  |
| 10-04 08:52:44 | ZEC | down | 0.19→0.13 | 0.21 → 0.12 → 0.12 | 0.02s | — |  |
| 10-04 08:52:43 | NEAR | down | 0.60→0.54 | 0.76 → 0.76 → 0.73 | no | DOWN @ 0.26 | -0.38 / -0.86 / · |
| 10-04 08:52:29 | ZEC | down | 0.25→0.19 | 0.14 → 0.21 → 0.21 | 29.54s | — |  |
| 10-04 08:52:12 | NEAR | up | 0.54→0.59 | 0.71 → 0.71 → 0.71 | 16.28s | — |  |
| 10-04 08:52:03 | ZEC | up | 0.18→0.23 | 0.20 → 0.20 → 0.20 | no | — |  |
| 10-04 08:51:43 | DOGE | down | 0.58→0.47 | 0.51 → 0.51 → 0.48 | no | — |  |
| 10-04 08:51:32 | HYPE | down | 0.32→0.27 | 0.33 → 0.33 → 0.33 | no | DOWN @ 0.68 | -0.42 / -0.62 / · |
| 10-04 08:51:29 | ETH | down | 0.61→0.53 | 0.69 → 0.61 → 0.61 | 0.03s | DOWN @ 0.39 | -0.44 / 0.25 / · |
| 10-04 08:51:28 | DOGE | up | 0.47→0.58 | 0.51 → 0.51 → 0.51 | no | UP @ 0.51 | -0.46 / -0.66 / · |
| 10-04 08:51:19 | ZEC | up | 0.11→0.16 | 0.10 → 0.10 → 0.10 | 9.55s | UP @ 0.11 | 0.05 / 0.62 / · |
| 10-04 08:51:09 | XRP | down | 0.30→0.25 | 0.28 → 0.28 → 0.28 | 5.05s | — |  |
| 10-04 08:51:08 | ETH | down | 0.64→0.56 | 0.77 → 0.77 → 0.77 | 6.05s | DOWN @ 0.24 | 0.42 / 1.10 / · |
| 10-04 08:51:07 | BTC | down | 0.76→0.71 | 0.86 → 0.86 → 0.86 | 6.80s | DOWN @ 0.14 | 0.68 / 1.07 / · |
| 10-04 08:51:02 | HYPE | down | 0.42→0.35 | 0.42 → 0.42 → 0.42 | 12.05s | DOWN @ 0.59 | -0.55 / 0.47 / · |
| 10-04 08:50:55 | ZEC | up | 0.12→0.21 | 0.12 → 0.12 → 0.11 | no | UP @ 0.13 | -0.45 / -0.45 / · |
| 10-04 08:50:50 | SOL | down | 0.38→0.32 | 0.40 → 0.40 → 0.40 | 23.56s | DOWN @ 0.61 | -0.54 / -0.14 / · |
| 10-04 08:50:35 | XRP | down | 0.39→0.33 | 0.35 → 0.35 → 0.35 | 23.57s | — |  |
| 10-04 08:50:26 | SOL | down | 0.45→0.33 | 0.53 → 0.53 → 0.40 | 2.56s | DOWN @ 0.49 | 0.75 / 0.75 / · |
| 10-04 08:50:22 | ZEC | down | 0.35→0.23 | 0.29 → 0.29 → 0.29 | 21.31s | DOWN @ 0.71 | -0.50 / 1.37 / · |
| 10-04 08:50:11 | DOGE | up | 0.58→0.71 | 0.69 → 0.69 → 0.66 | no | — |  |
