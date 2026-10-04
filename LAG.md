# Lag Tracker

*Updated Sun Oct 04 05:04 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 530 | 10.8s | 4% | 0% |
| BTC | 412 | 11.9s | 2% | 0% |
| DOGE | 561 | 10.7s | 2% | 0% |
| ETH | 545 | 10.9s | 3% | 0% |
| HYPE | 453 | 11.6s | 4% | 0% |
| NEAR | 506 | 10.7s | 4% | 0% |
| SOL | 1018 | 10.6s | 2% | 0% |
| XRP | 1003 | 10.8s | 4% | 0% |
| ZEC | 672 | 9.8s | 4% | 0% |
| **All** | **5700** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2943 | 825 | $-355.06 | -2.8% | $-160.26 / $-194.80 |
| Sell after 30 sec | 2943 | 1691 | $879.81 | +6.9% | $517.41 / $362.40 |
| Hold to the close | 2926 | 1445 | $1761.91 | +13.9% | $859.47 / $902.44 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **31 ms** · Coinbase price delay: **14 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 05:04:21 | NEAR | up | 0.52→0.57 | 0.58 → 0.58 → 0.56 | no | — |  |
| 10-04 05:04:15 | XRP | down | 0.85→0.79 | 0.79 → 0.79 → 0.79 | no | — |  |
| 10-04 05:04:00 | DOGE | down | 0.87→0.81 | 0.82 → 0.82 → 0.82 | no | — |  |
| 10-04 05:03:45 | DOGE | up | 0.80→0.87 | 0.81 → 0.81 → 0.81 | no | UP @ 0.82 | -0.22 / -0.32 / · |
| 10-04 05:03:42 | BNB | up | 0.67→0.72 | 0.84 → 0.84 → 0.84 | no | — |  |
| 10-04 05:03:27 | ZEC | up | 0.81→0.87 | 0.81 → 0.81 → 0.81 | 25.75s | UP @ 0.83 | -0.52 / 0.11 / · |
| 10-04 05:03:26 | HYPE | down | 0.81→0.76 | 0.84 → 0.84 → 0.84 | 12.24s | DOWN @ 0.16 | -0.29 / 0.47 / · |
| 10-04 05:03:06 | SOL | down | 0.65→0.59 | 0.78 → 0.78 → 0.78 | no | DOWN @ 0.23 | -0.36 / -0.36 / · |
| 10-04 05:03:05 | XRP | down | 0.78→0.71 | 0.76 → 0.76 → 0.65 | 2.49s | — |  |
| 10-04 05:03:02 | NEAR | down | 0.72→0.57 | 0.69 → 0.69 → 0.69 | 5.99s | DOWN @ 0.33 | 0.66 / 0.47 / · |
| 10-04 05:02:52 | ZEC | up | 0.73→0.78 | 0.79 → 0.79 → 0.80 | no | — |  |
| 10-04 05:02:50 | XRP | down | 0.83→0.77 | 0.76 → 0.76 → 0.76 | 17.50s | — |  |
| 10-04 05:02:42 | BNB | down | 0.62→0.51 | 0.80 → 0.80 → 0.80 | no | DOWN @ 0.23 | -0.74 / -0.93 / · |
| 10-04 05:02:31 | ZEC | up | 0.62→0.72 | 0.67 → 0.67 → 0.67 | 7.25s | — |  |
| 10-04 05:02:15 | XRP | down | 0.85→0.77 | 0.80 → 0.80 → 0.80 | 7.75s | — |  |
| 10-04 05:02:12 | ZEC | down | 0.70→0.61 | 0.73 → 0.73 → 0.73 | 10.75s | DOWN @ 0.28 | -0.59 / -1.07 / · |
| 10-04 05:02:02 | DOGE | up | 0.78→0.83 | 0.80 → 0.80 → 0.80 | no | — |  |
| 10-04 05:02:00 | XRP | up | 0.82→0.90 | 0.76 → 0.76 → 0.76 | no | UP @ 0.77 | -0.05 / -0.67 / · |
| 10-04 05:01:58 | SOL | up | 0.52→0.58 | 0.58 → 0.58 → 0.58 | 10.25s | — |  |
| 10-04 05:01:44 | BNB | up | 0.41→0.63 | 0.57 → 0.57 → 0.57 | 9.02s | — |  |
| 10-04 05:01:43 | NEAR | up | 0.62→0.71 | 0.64 → 0.64 → 0.64 | 9.77s | UP @ 0.66 | 0.60 / 0.40 / · |
| 10-04 05:01:35 | ETH | up | 0.74→0.85 | 0.64 → 0.64 → 0.57 | 17.52s | UP @ 0.64 | -1.05 / 1.10 / · |
| 10-04 05:01:31 | XRP | up | 0.75→0.80 | 0.73 → 0.73 → 0.73 | 7.02s | UP @ 0.74 | 0.24 / -0.18 / · |
| 10-04 05:01:29 | BTC | up | 0.63→0.69 | 0.58 → 0.58 → 0.58 | 9.02s | UP @ 0.59 | 1.40 / 1.29 / · |
| 10-04 05:01:29 | BNB | up | 0.30→0.41 | 0.58 → 0.58 → 0.58 | 24.02s | — |  |
| 10-04 05:01:17 | SOL | up | 0.46→0.52 | 0.46 → 0.46 → 0.46 | 6.01s | UP @ 0.46 | 0.04 / 0.34 / · |
| 10-04 05:01:10 | ETH | up | 0.68→0.73 | 0.48 → 0.58 → 0.58 | 0.25s | UP @ 0.59 | -0.45 / -0.55 / · |
| 10-04 05:01:06 | BTC | up | 0.36→0.44 | 0.49 → 0.49 → 0.48 | 17.26s | UP @ 0.50 | -0.56 / 0.44 / · |
| 10-04 05:01:02 | XRP | up | 0.68→0.74 | 0.67 → 0.67 → 0.67 | 21.27s | UP @ 0.68 | -0.42 / 0.20 / · |
| 10-04 05:01:01 | DOGE | up | 0.55→0.70 | 0.68 → 0.68 → 0.68 | 21.77s | UP @ 0.68 | -0.32 / 0.92 / · |
