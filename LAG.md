# Lag Tracker

*Updated Sun Oct 04 03:14 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 463 | 10.7s | 4% | 0% |
| BTC | 372 | 12.3s | 2% | 0% |
| DOGE | 489 | 10.6s | 2% | 0% |
| ETH | 477 | 11.0s | 3% | 0% |
| HYPE | 385 | 11.6s | 4% | 0% |
| NEAR | 411 | 10.8s | 4% | 0% |
| SOL | 929 | 10.6s | 3% | 0% |
| XRP | 858 | 11.0s | 4% | 0% |
| ZEC | 549 | 9.7s | 4% | 0% |
| **All** | **4933** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2590 | 723 | $-300.43 | -2.7% | $-121.54 / $-178.89 |
| Sell after 30 sec | 2590 | 1500 | $812.65 | +7.2% | $487.83 / $324.82 |
| Hold to the close | 2534 | 1259 | $1631.97 | +14.9% | $991.84 / $640.13 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **38 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 03:13:39 | ETH | down | 0.62→0.48 | 0.72 → 0.72 → 0.72 | 6.28s | DOWN @ 0.29 | 2.78 / -0.40 / · |
| 10-04 03:13:38 | BTC | down | 0.46→0.39 | 0.71 → 0.71 → 0.71 | 7.28s | DOWN @ 0.29 | 0.68 / -0.98 / · |
| 10-04 03:13:33 | XRP | down | 0.75→0.30 | 0.78 → 0.78 → 0.78 | no | DOWN @ 0.23 | -0.45 / -0.83 / · |
| 10-04 03:13:32 | ZEC | down | 0.73→0.50 | 0.73 → 0.73 → 0.73 | 12.78s | — |  |
| 10-04 03:13:17 | BNB | down | 0.34→0.04 | 0.26 → 0.18 → 0.18 | no | — |  |
| 10-04 03:13:07 | ZEC | up | 0.68→0.77 | 0.78 → 0.78 → 0.78 | 7.54s | — |  |
| 10-04 03:13:06 | XRP | up | 0.61→0.79 | 0.80 → 0.80 → 0.80 | no | — |  |
| 10-04 03:12:57 | ETH | up | 0.45→0.58 | 0.34 → 0.34 → 0.41 | 3.03s | UP @ 0.35 | 0.17 / 3.19 / · |
| 10-04 03:12:55 | BNB | up | 0.24→0.36 | 0.17 → 0.17 → 0.17 | 5.28s | — |  |
| 10-04 03:12:52 | ZEC | up | 0.61→0.68 | 0.80 → 0.80 → 0.80 | 22.54s | — |  |
| 10-04 03:12:51 | XRP | down | 0.50→0.40 | 0.68 → 0.68 → 0.68 | no | DOWN @ 0.33 | -1.58 / -2.43 / · |
| 10-04 03:12:42 | ETH | up | 0.37→0.47 | 0.51 → 0.51 → 0.34 | no | — |  |
| 10-04 03:12:37 | ZEC | down | 0.77→0.58 | 0.72 → 0.72 → 0.72 | no | DOWN @ 0.29 | -1.45 / -1.26 / · |
| 10-04 03:12:36 | XRP | up | 0.41→0.50 | 0.67 → 0.67 → 0.67 | 23.54s | — |  |
| 10-04 03:12:27 | ETH | down | 0.44→0.39 | 0.54 → 0.54 → 0.51 | 3.03s | DOWN @ 0.47 | -0.26 / 1.46 / · |
| 10-04 03:12:21 | XRP | down | 0.58→0.42 | 0.64 → 0.64 → 0.64 | no | DOWN @ 0.38 | -0.83 / -0.93 / · |
| 10-04 03:12:18 | SOL | up | 0.24→0.29 | 0.32 → 0.32 → 0.32 | no | — |  |
| 10-04 03:12:16 | ZEC | up | 0.46→0.70 | 0.40 → 0.40 → 0.40 | 13.54s | UP @ 0.42 | -0.75 / 3.09 / · |
| 10-04 03:12:05 | XRP | down | 0.58→0.50 | 0.69 → 0.69 → 0.69 | 9.79s | DOWN @ 0.31 | 0.09 / -0.11 / · |
| 10-04 03:12:03 | SOL | up | 0.21→0.30 | 0.32 → 0.32 → 0.32 | no | — |  |
| 10-04 03:12:01 | ZEC | up | 0.40→0.47 | 0.42 → 0.42 → 0.42 | 28.55s | — |  |
| 10-04 03:12:00 | HYPE | up | 0.69→0.75 | 0.79 → 0.82 → 0.82 | 15.04s | — |  |
| 10-04 03:11:49 | XRP | down | 0.62→0.56 | 0.71 → 0.71 → 0.71 | 25.54s | DOWN @ 0.30 | -0.59 / 0.19 / · |
| 10-04 03:11:48 | SOL | down | 0.31→0.26 | 0.34 → 0.34 → 0.34 | 26.29s | DOWN @ 0.68 | -0.83 / -0.42 / · |
| 10-04 03:11:45 | HYPE | down | 0.86→0.68 | 0.76 → 0.79 → 0.79 | no | DOWN @ 0.22 | -0.45 / -0.83 / · |
| 10-04 03:11:34 | XRP | up | 0.44→0.62 | 0.51 → 0.51 → 0.51 | 10.53s | UP @ 0.51 | -0.46 / 1.47 / · |
| 10-04 03:11:29 | ZEC | up | 0.38→0.48 | 0.42 → 0.42 → 0.29 | 15.79s | — |  |
| 10-04 03:11:29 | SOL | up | 0.19→0.28 | 0.35 → 0.35 → 0.21 | no | — |  |
| 10-04 03:11:18 | ETH | up | 0.38→0.50 | 0.47 → 0.47 → 0.47 | no | — |  |
| 10-04 03:11:18 | XRP | down | 0.44→0.38 | 0.48 → 0.48 → 0.48 | no | — |  |
