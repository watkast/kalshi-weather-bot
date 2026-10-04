# Lag Tracker

*Updated Sun Oct 04 08:45 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 634 | 11.2s | 3% | 0% |
| BTC | 511 | 11.9s | 3% | 0% |
| DOGE | 699 | 10.4s | 2% | 0% |
| ETH | 682 | 11.2s | 3% | 0% |
| HYPE | 583 | 11.3s | 4% | 0% |
| NEAR | 676 | 10.8s | 4% | 0% |
| SOL | 1247 | 10.8s | 3% | 0% |
| XRP | 1262 | 10.9s | 4% | 0% |
| ZEC | 847 | 9.6s | 4% | 0% |
| **All** | **7141** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3665 | 1033 | $-416.48 | -2.6% | $-195.71 / $-220.77 |
| Sell after 30 sec | 3665 | 2137 | $1193.04 | +7.6% | $592.77 / $600.27 |
| Hold to the close | 3633 | 1798 | $2330.58 | +14.9% | $1497.98 / $832.60 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **15 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 08:43:34 | XRP | up | 0.13→0.23 | 0.08 → 0.08 → 0.08 | 7.27s | UP @ 0.08 | 0.36 / -0.14 / · |
| 10-04 08:43:19 | XRP | up | 0.05→0.16 | 0.05 → 0.05 → 0.05 | 22.27s | UP @ 0.05 | 0.16 / 0.68 / · |
| 10-04 08:42:51 | XRP | down | 0.14→0.09 | 0.07 → 0.07 → 0.07 | no | — |  |
| 10-04 08:42:09 | BNB | down | 0.23→0.06 | 0.91 → 0.91 → 0.90 | 17.04s | DOWN @ 0.10 | -0.13 / 4.56 / · |
| 10-04 08:42:09 | XRP | down | 0.13→0.06 | 0.10 → 0.10 → 0.08 | 17.29s | — |  |
| 10-04 08:41:30 | XRP | down | 0.19→0.12 | 0.14 → 0.12 → 0.12 | 27.29s | — |  |
| 10-04 08:41:09 | XRP | down | 0.23→0.13 | 0.12 → 0.12 → 0.14 | no | — |  |
| 10-04 08:41:02 | HYPE | up | 0.86→0.92 | 0.93 → 0.93 → 0.93 | 25.04s | — |  |
| 10-04 08:41:00 | ZEC | up | 0.19→0.25 | 0.16 → 0.16 → 0.16 | 12.03s | — |  |
| 10-04 08:40:45 | XRP | up | 0.06→0.14 | 0.04 → 0.04 → 0.04 | 11.53s | — |  |
| 10-04 08:40:31 | ZEC | down | 0.22→0.16 | 0.17 → 0.17 → 0.17 | 11.03s | — |  |
| 10-04 08:40:06 | ZEC | down | 0.27→0.20 | 0.15 → 0.15 → 0.15 | no | — |  |
| 10-04 08:40:05 | BNB | up | 0.24→0.34 | 0.66 → 0.66 → 0.66 | 6.78s | — |  |
| 10-04 08:39:04 | ZEC | down | 0.26→0.21 | 0.17 → 0.17 → 0.17 | no | — |  |
| 10-04 08:38:49 | HYPE | down | 0.89→0.84 | 0.92 → 0.92 → 0.92 | no | DOWN @ 0.08 | -0.21 / -0.24 / · |
| 10-04 08:38:44 | BNB | down | 0.27→0.20 | 0.51 → 0.49 → 0.49 | 28.30s | — |  |
| 10-04 08:38:22 | ZEC | down | 0.32→0.24 | 0.27 → 0.27 → 0.23 | 19.56s | — |  |
| 10-04 08:37:49 | ZEC | down | 0.37→0.29 | 0.25 → 0.25 → 0.25 | no | — |  |
| 10-04 08:37:29 | HYPE | up | 0.80→0.86 | 0.85 → 0.85 → 0.85 | 12.56s | — |  |
| 10-04 08:37:14 | HYPE | down | 0.87→0.79 | 0.85 → 0.85 → 0.85 | no | DOWN @ 0.15 | -0.28 / -0.66 / · |
| 10-04 08:37:05 | ETH | down | 0.20→0.13 | 0.15 → 0.15 → 0.15 | 6.84s | — |  |
| 10-04 08:37:03 | DOGE | down | 0.16→0.08 | 0.09 → 0.09 → 0.09 | 9.09s | — |  |
| 10-04 08:37:03 | XRP | down | 0.29→0.23 | 0.38 → 0.38 → 0.38 | 9.09s | DOWN @ 0.63 | 1.10 / 1.52 / · |
| 10-04 08:36:57 | NEAR | down | 0.37→0.22 | 0.38 → 0.37 → 0.37 | 14.84s | DOWN @ 0.64 | -0.54 / 1.94 / · |
| 10-04 08:36:50 | BNB | up | 0.45→0.55 | 0.73 → 0.73 → 0.73 | no | — |  |
| 10-04 08:36:44 | XRP | up | 0.36→0.45 | 0.38 → 0.38 → 0.38 | no | UP @ 0.39 | -0.64 / -2.00 / · |
| 10-04 08:36:42 | NEAR | up | 0.31→0.37 | 0.39 → 0.38 → 0.38 | no | — |  |
| 10-04 08:36:28 | HYPE | up | 0.80→0.86 | 0.84 → 0.85 → 0.85 | 13.83s | — |  |
| 10-04 08:36:25 | ZEC | up | 0.39→0.45 | 0.28 → 0.28 → 0.37 | 1.58s | UP @ 0.29 | 0.38 / 0.48 / · |
| 10-04 08:36:24 | ETH | up | 0.23→0.29 | 0.14 → 0.14 → 0.15 | 17.58s | UP @ 0.15 | -0.18 / 0.10 / · |
