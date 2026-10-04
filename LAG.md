# Lag Tracker

*Updated Sun Oct 04 05:14 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 530 | 10.8s | 4% | 0% |
| BTC | 414 | 11.9s | 2% | 0% |
| DOGE | 570 | 10.9s | 2% | 0% |
| ETH | 546 | 11.0s | 3% | 0% |
| HYPE | 463 | 11.6s | 3% | 0% |
| NEAR | 521 | 10.8s | 4% | 0% |
| SOL | 1035 | 10.8s | 2% | 0% |
| XRP | 1026 | 10.8s | 4% | 0% |
| ZEC | 681 | 9.7s | 4% | 0% |
| **All** | **5786** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2981 | 831 | $-364.93 | -2.8% | $-160.03 / $-204.90 |
| Sell after 30 sec | 2981 | 1711 | $886.38 | +6.9% | $518.13 / $368.25 |
| Hold to the close | 2926 | 1445 | $1761.91 | +13.9% | $859.47 / $902.44 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **31 ms** · Coinbase price delay: **14 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 05:13:44 | DOGE | down | 0.22→0.08 | 0.75 → 0.75 → 0.75 | 23.29s | DOWN @ 0.26 | -0.57 / 0.21 / · |
| 10-04 05:13:41 | SOL | up | 0.60→0.74 | 0.95 → 0.95 → 0.95 | no | — |  |
| 10-04 05:13:27 | XRP | up | 0.02→0.08 | 0.20 → 0.20 → 0.20 | no | — |  |
| 10-04 05:13:26 | SOL | down | 0.70→0.59 | 0.96 → 0.96 → 0.96 | no | — |  |
| 10-04 05:13:23 | NEAR | down | 0.34→0.17 | 0.65 → 0.69 → 0.69 | 15.03s | DOWN @ 0.32 | -0.51 / 1.56 / · |
| 10-04 05:13:12 | DOGE | up | 0.18→0.66 | 0.41 → 0.41 → 0.41 | 10.53s | UP @ 0.43 | -0.75 / 2.78 / · |
| 10-04 05:13:11 | SOL | up | 0.75→0.85 | 0.94 → 0.94 → 0.94 | no | — |  |
| 10-04 05:13:11 | XRP | down | 0.27→0.18 | 0.28 → 0.28 → 0.28 | 12.03s | DOWN @ 0.74 | -0.59 / 1.88 / · |
| 10-04 05:12:56 | SOL | down | 0.73→0.65 | 0.94 → 0.94 → 0.94 | no | DOWN @ 0.06 | -0.09 / -0.29 / · |
| 10-04 05:12:55 | XRP | down | 0.13→0.08 | 0.17 → 0.13 → 0.13 | 0.02s | — |  |
| 10-04 05:12:46 | ZEC | down | 0.87→0.80 | 0.88 → 0.88 → 0.88 | no | DOWN @ 0.14 | -1.39 / -1.41 / · |
| 10-04 05:12:45 | NEAR | up | 0.26→0.32 | 0.63 → 0.63 → 0.63 | no | — |  |
| 10-04 05:12:42 | HYPE | up | 0.27→0.32 | 0.27 → 0.27 → 0.27 | no | UP @ 0.27 | -0.38 / -0.67 / · |
| 10-04 05:12:40 | SOL | up | 0.71→0.85 | 0.94 → 0.94 → 0.94 | no | — |  |
| 10-04 05:12:40 | XRP | down | 0.15→0.10 | 0.17 → 0.17 → 0.17 | 12.53s | — |  |
| 10-04 05:12:31 | ZEC | up | 0.77→0.85 | 0.89 → 0.89 → 0.89 | 21.28s | — |  |
| 10-04 05:12:27 | HYPE | down | 0.33→0.28 | 0.28 → 0.28 → 0.28 | 25.79s | — |  |
| 10-04 05:12:25 | XRP | down | 0.24→0.17 | 0.25 → 0.17 → 0.17 | 0.27s | — |  |
| 10-04 05:12:23 | SOL | down | 0.70→0.55 | 0.85 → 0.85 → 0.85 | no | DOWN @ 0.16 | -0.39 / -1.17 / · |
| 10-04 05:12:21 | NEAR | up | 0.21→0.28 | 0.48 → 0.48 → 0.46 | 16.03s | — |  |
| 10-04 05:12:09 | XRP | down | 0.33→0.25 | 0.43 → 0.25 → 0.25 | 0.02s | — |  |
| 10-04 05:12:00 | ZEC | down | 0.80→0.71 | 0.83 → 0.83 → 0.83 | no | DOWN @ 0.19 | -0.98 / -1.18 / · |
| 10-04 05:12:00 | SOL | up | 0.62→0.75 | 0.90 → 0.90 → 0.90 | no | — |  |
| 10-04 05:11:54 | XRP | down | 0.34→0.27 | 0.06 → 0.43 → 0.43 | no | DOWN @ 0.57 | -0.46 / 2.21 / · |
| 10-04 05:11:45 | SOL | up | 0.54→0.61 | 0.69 → 0.69 → 0.69 | 8.03s | — |  |
| 10-04 05:11:45 | HYPE | up | 0.31→0.40 | 0.29 → 0.29 → 0.29 | no | — |  |
| 10-04 05:11:37 | XRP | down | 0.13→0.08 | 0.26 → 0.26 → 0.06 | 1.28s | DOWN @ 0.75 | 1.58 / -2.22 / · |
| 10-04 05:11:33 | ZEC | up | 0.64→0.70 | 0.86 → 0.86 → 0.81 | no | — |  |
| 10-04 05:11:27 | SOL | down | 0.67→0.60 | 0.85 → 0.85 → 0.85 | 11.28s | DOWN @ 0.15 | -0.28 / -0.68 / · |
| 10-04 05:11:24 | BTC | down | 1.00→0.87 | 0.96 → 0.96 → 0.96 | 13.53s | — |  |
