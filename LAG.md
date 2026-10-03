# Lag Tracker

*Updated Sat Oct 03 23:23 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 312 | 10.8s | 5% | 0% |
| BTC | 226 | 11.8s | 2% | 0% |
| DOGE | 323 | 10.3s | 2% | 0% |
| ETH | 292 | 11.1s | 3% | 0% |
| HYPE | 240 | 11.6s | 3% | 0% |
| NEAR | 266 | 10.4s | 4% | 0% |
| SOL | 558 | 10.0s | 4% | 0% |
| XRP | 506 | 10.3s | 4% | 0% |
| ZEC | 326 | 9.6s | 5% | 0% |
| **All** | **3049** | **10.6s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1587 | 455 | $-175.51 | -2.6% | $-52.99 / $-122.52 |
| Sell after 30 sec | 1585 | 945 | $526.69 | +7.7% | $357.72 / $168.97 |
| Hold to the close | 1537 | 758 | $978.57 | +14.8% | $598.04 / $380.53 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **38 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 23:23:20 | XRP | up | 0.65→0.73 | 0.82 → 0.82 → — | no | — |  |
| 10-03 23:23:12 | DOGE | down | 0.49→0.37 | 0.64 → 0.64 → 0.64 | no | DOWN @ 0.37 | -0.44 / · / · |
| 10-03 23:23:05 | XRP | down | 0.80→0.73 | 0.83 → 0.83 → 0.82 | 18.20s | DOWN @ 0.18 | -0.31 / · / · |
| 10-03 23:23:00 | HYPE | down | 0.33→0.26 | 0.24 → 0.24 → 0.24 | no | — |  |
| 10-03 23:22:45 | BNB | up | 0.48→0.58 | 0.80 → 0.80 → 0.80 | no | — |  |
| 10-03 23:22:45 | HYPE | up | 0.21→0.33 | 0.29 → 0.29 → 0.29 | no | — |  |
| 10-03 23:22:44 | DOGE | down | 0.61→0.53 | 0.65 → 0.65 → 0.65 | no | DOWN @ 0.36 | -0.34 / -0.34 / · |
| 10-03 23:22:38 | SOL | down | 0.94→0.88 | 0.58 → 0.85 → 0.85 | no | — |  |
| 10-03 23:22:30 | BNB | up | 0.31→0.48 | 0.49 → 0.49 → 0.49 | 7.70s | — |  |
| 10-03 23:22:29 | NEAR | up | 0.81→0.89 | 0.83 → 0.83 → 0.83 | 23.96s | UP @ 0.84 | 0.12 / 0.70 / · |
| 10-03 23:22:28 | BTC | up | 0.42→0.80 | 0.53 → 0.53 → 0.53 | 9.70s | UP @ 0.53 | 2.30 / 2.93 / · |
| 10-03 23:22:28 | DOGE | up | 0.27→0.61 | 0.23 → 0.23 → 0.23 | 9.70s | UP @ 0.23 | 3.80 / 3.70 / · |
| 10-03 23:22:28 | HYPE | up | 0.12→0.21 | 0.17 → 0.17 → 0.17 | 9.70s | UP @ 0.17 | 0.95 / 0.37 / · |
| 10-03 23:22:24 | XRP | down | 0.55→0.45 | 0.69 → 0.71 → 0.71 | no | DOWN @ 0.29 | -0.40 / -1.55 / · |
| 10-03 23:22:22 | ETH | down | 0.52→0.34 | 0.42 → 0.42 → 0.42 | no | DOWN @ 0.58 | -0.46 / -4.29 / · |
| 10-03 23:22:20 | SOL | down | 0.56→0.50 | 0.57 → 0.57 → 0.58 | no | DOWN @ 0.43 | -0.65 / -3.17 / · |
| 10-03 23:22:14 | NEAR | down | 0.89→0.81 | 0.86 → 0.86 → 0.86 | no | DOWN @ 0.15 | -0.09 / -0.47 / · |
| 10-03 23:22:04 | DOGE | down | 0.23→0.16 | 0.29 → 0.29 → 0.26 | 3.45s | DOWN @ 0.71 | 0.01 / 0.32 / · |
| 10-03 23:22:00 | SOL | up | 0.40→0.55 | 0.56 → 0.56 → 0.56 | no | — |  |
| 10-03 23:22:00 | BTC | up | 0.40→0.55 | 0.47 → 0.47 → 0.47 | no | UP @ 0.48 | 0.24 / 0.04 / · |
| 10-03 23:21:49 | HYPE | down | 0.25→0.17 | 0.28 → 0.28 → 0.24 | 18.96s | DOWN @ 0.73 | -0.08 / 0.65 / · |
| 10-03 23:21:48 | NEAR | down | 0.92→0.84 | 0.90 → 0.90 → 0.90 | 5.21s | DOWN @ 0.11 | 0.43 / 0.05 / · |
| 10-03 23:21:43 | SOL | down | 0.66→0.55 | 0.72 → 0.72 → 0.72 | 10.21s | DOWN @ 0.28 | 1.17 / 1.07 / · |
| 10-03 23:21:33 | BNB | up | 0.20→0.29 | 0.47 → 0.47 → 0.48 | no | — |  |
| 10-03 23:21:25 | HYPE | up | 0.23→0.28 | 0.29 → 0.29 → 0.29 | no | — |  |
| 10-03 23:21:16 | SOL | up | 0.55→0.70 | 0.76 → 0.76 → 0.76 | no | — |  |
| 10-03 23:21:10 | XRP | down | 0.54→0.46 | 0.68 → 0.68 → 0.68 | no | DOWN @ 0.33 | -0.42 / -0.32 / · |
| 10-03 23:21:10 | HYPE | down | 0.32→0.23 | 0.30 → 0.30 → 0.30 | no | DOWN @ 0.70 | -0.40 / -0.10 / · |
| 10-03 23:21:01 | SOL | down | 0.70→0.60 | 0.72 → 0.72 → 0.72 | no | — |  |
| 10-03 23:20:55 | XRP | down | 0.54→0.46 | 0.68 → 0.68 → 0.68 | no | DOWN @ 0.33 | -0.42 / -0.22 / · |
