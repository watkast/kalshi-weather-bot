# Lag Tracker

*Updated Sun Oct 04 06:34 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 581 | 10.8s | 3% | 0% |
| BTC | 458 | 11.9s | 3% | 0% |
| DOGE | 636 | 10.4s | 2% | 0% |
| ETH | 607 | 11.2s | 3% | 0% |
| HYPE | 510 | 11.5s | 4% | 0% |
| NEAR | 572 | 10.8s | 4% | 0% |
| SOL | 1125 | 10.8s | 3% | 0% |
| XRP | 1117 | 10.9s | 3% | 0% |
| ZEC | 726 | 9.8s | 4% | 0% |
| **All** | **6332** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3249 | 900 | $-397.96 | -2.8% | $-172.90 / $-225.06 |
| Sell after 30 sec | 3249 | 1863 | $989.30 | +7.0% | $549.84 / $439.46 |
| Hold to the close | 3233 | 1611 | $2062.89 | +14.7% | $1111.67 / $951.22 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **31 ms** · Coinbase price delay: **15 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 06:34:46 | NEAR | down | 0.78→0.72 | 0.85 → 0.85 → — | no | DOWN @ 0.16 | · / · / · |
| 10-04 06:33:12 | ZEC | up | 0.64→0.71 | 0.74 → 0.74 → 0.74 | 26.85s | — |  |
| 10-04 06:33:11 | SOL | up | 0.83→0.89 | 0.83 → 0.84 → 0.84 | 12.60s | — |  |
| 10-04 06:33:11 | NEAR | up | 0.63→0.73 | 0.70 → 0.70 → 0.70 | 12.85s | — |  |
| 10-04 06:32:56 | NEAR | up | 0.53→0.60 | 0.65 → 0.70 → 0.70 | 0.09s | — |  |
| 10-04 06:32:44 | ETH | up | 0.85→0.91 | 0.81 → 0.81 → 0.81 | 9.60s | UP @ 0.81 | 0.09 / -0.22 / · |
| 10-04 06:32:41 | NEAR | down | 0.61→0.53 | 0.65 → 0.65 → 0.65 | no | DOWN @ 0.36 | -0.43 / -1.12 / · |
| 10-04 06:32:28 | SOL | up | 0.67→0.86 | 0.56 → 0.56 → 0.56 | 11.11s | UP @ 0.57 | -0.46 / 2.32 / · |
| 10-04 06:32:26 | XRP | up | 0.38→0.79 | 0.41 → 0.41 → 0.41 | 13.11s | UP @ 0.42 | -0.55 / 3.50 / · |
| 10-04 06:32:25 | HYPE | up | 0.62→0.70 | 0.60 → 0.61 → 0.61 | 13.61s | UP @ 0.62 | -0.44 / 1.30 / · |
| 10-04 06:32:25 | ETH | up | 0.59→0.86 | 0.57 → 0.55 → 0.55 | 13.61s | UP @ 0.56 | -0.56 / 2.52 / · |
| 10-04 06:32:24 | BTC | up | 0.78→0.85 | 0.69 → 0.76 → 0.76 | 0.11s | UP @ 0.76 | -0.37 / 0.68 / · |
| 10-04 06:32:23 | NEAR | up | 0.49→0.56 | 0.58 → 0.58 → 0.57 | 16.36s | — |  |
| 10-04 06:32:23 | ZEC | up | 0.49→0.54 | 0.53 → 0.53 → 0.52 | 16.36s | — |  |
| 10-04 06:32:23 | DOGE | up | 0.46→0.64 | 0.58 → 0.58 → 0.59 | 16.36s | — |  |
| 10-04 06:32:14 | BNB | up | 0.25→0.32 | 0.45 → 0.45 → 0.45 | 25.37s | — |  |
| 10-04 06:32:13 | SOL | down | 0.47→0.42 | 0.56 → 0.56 → 0.56 | no | DOWN @ 0.45 | -0.46 / -2.89 / · |
| 10-04 06:32:11 | XRP | up | 0.29→0.41 | 0.34 → 0.34 → 0.34 | 13.11s | UP @ 0.34 | -0.42 / 3.91 / · |
| 10-04 06:32:09 | BTC | up | 0.72→0.78 | 0.66 → 0.69 → 0.69 | 0.11s | UP @ 0.70 | -0.40 / 0.21 / · |
| 10-04 06:32:06 | HYPE | up | 0.60→0.67 | 0.59 → 0.59 → 0.60 | no | UP @ 0.60 | -0.34 / -0.24 / · |
| 10-04 06:31:50 | XRP | up | 0.30→0.35 | 0.34 → 0.34 → 0.35 | no | — |  |
| 10-04 06:31:44 | HYPE | up | 0.45→0.54 | 0.48 → 0.48 → 0.48 | 9.87s | — |  |
| 10-04 06:31:44 | NEAR | down | 0.59→0.54 | 0.67 → 0.67 → 0.67 | 25.37s | DOWN @ 0.34 | -0.42 / 0.37 / · |
| 10-04 06:31:29 | HYPE | down | 0.54→0.45 | 0.53 → 0.53 → 0.53 | no | DOWN @ 0.48 | -0.26 / -1.15 / · |
| 10-04 06:31:12 | BTC | up | 0.64→0.76 | 0.66 → 0.66 → 0.66 | no | UP @ 0.66 | -0.42 / -0.53 / · |
| 10-04 06:31:09 | BNB | down | 0.37→0.28 | 0.54 → 0.54 → 0.54 | no | DOWN @ 0.47 | -0.46 / -0.26 / · |
| 10-04 06:30:57 | BTC | down | 0.76→0.70 | 0.69 → 0.69 → 0.69 | 11.13s | — |  |
| 10-04 06:30:53 | BNB | down | 0.42→0.36 | 0.54 → 0.54 → 0.54 | 30.13s | DOWN @ 0.47 | -0.46 / -0.46 / · |
| 10-04 06:30:34 | BTC | up | 0.53→0.62 | 0.62 → 0.62 → 0.62 | 18.89s | — |  |
| 10-04 06:28:35 | NEAR | down | 0.35→0.16 | 0.62 → 0.66 → 0.66 | 14.16s | DOWN @ 0.36 | -0.73 / 5.30 / 6.23 |
