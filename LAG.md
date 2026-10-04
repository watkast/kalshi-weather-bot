# Lag Tracker

*Updated Sun Oct 04 01:13 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 389 | 10.8s | 4% | 0% |
| BTC | 312 | 11.9s | 2% | 0% |
| DOGE | 426 | 10.7s | 2% | 0% |
| ETH | 383 | 11.1s | 3% | 0% |
| HYPE | 299 | 11.8s | 3% | 0% |
| NEAR | 343 | 10.5s | 4% | 0% |
| SOL | 754 | 10.4s | 3% | 0% |
| XRP | 679 | 11.2s | 4% | 0% |
| ZEC | 416 | 9.7s | 4% | 0% |
| **All** | **4001** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2104 | 590 | $-228.17 | -2.5% | $-86.03 / $-142.14 |
| Sell after 30 sec | 2101 | 1231 | $699.35 | +7.7% | $427.12 / $272.23 |
| Hold to the close | 2030 | 1016 | $1425.30 | +16.3% | $815.38 / $609.92 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **38 ms** · Coinbase price delay: **7 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 01:13:43 | DOGE | down | 0.64→0.33 | 0.93 → 0.93 → 0.81 | no | DOWN @ 0.08 | · / · / · |
| 10-04 01:13:34 | NEAR | down | 0.27→0.12 | 0.37 → 0.37 → 0.37 | 11.90s | — |  |
| 10-04 01:13:34 | BTC | down | 0.44→0.17 | 0.68 → 0.68 → 0.68 | 11.90s | DOWN @ 0.33 | -0.42 / · / · |
| 10-04 01:13:34 | XRP | down | 0.97→0.74 | 0.98 → 0.98 → 0.98 | no | — |  |
| 10-04 01:13:33 | ETH | down | 0.93→0.85 | 0.96 → 0.96 → 0.96 | 12.40s | — |  |
| 10-04 01:13:33 | SOL | down | 0.90→0.85 | 0.99 → 0.99 → 0.99 | no | — |  |
| 10-04 01:13:28 | DOGE | down | 0.73→0.49 | 0.84 → 0.84 → 0.93 | no | DOWN @ 0.17 | -1.32 / · / · |
| 10-04 01:13:21 | ZEC | up | 0.09→0.20 | 0.05 → 0.05 → 0.05 | no | UP @ 0.07 | -0.53 / · / · |
| 10-04 01:13:19 | NEAR | up | 0.20→0.29 | 0.33 → 0.33 → 0.33 | 11.91s | — |  |
| 10-04 01:13:13 | SOL | down | 0.86→0.81 | 0.96 → 0.96 → 0.97 | no | — |  |
| 10-04 01:13:09 | DOGE | down | 0.60→0.49 | 0.79 → 0.79 → 0.79 | no | DOWN @ 0.22 | -1.02 / -1.85 / · |
| 10-04 01:12:58 | SOL | down | 0.72→0.65 | 0.95 → 0.95 → 0.96 | no | — |  |
| 10-04 01:12:57 | XRP | up | 0.86→0.92 | 0.97 → 0.97 → 0.97 | no | — |  |
| 10-04 01:12:52 | ZEC | down | 0.15→0.09 | 0.11 → 0.11 → 0.11 | 8.41s | — |  |
| 10-04 01:12:52 | BTC | down | 0.47→0.30 | 0.59 → 0.59 → 0.59 | no | DOWN @ 0.41 | -0.54 / -1.62 / · |
| 10-04 01:12:43 | SOL | down | 0.91→0.83 | 0.96 → 0.96 → 0.95 | no | — |  |
| 10-04 01:12:37 | ZEC | up | 0.16→0.26 | 0.12 → 0.12 → 0.12 | no | UP @ 0.14 | -0.67 / -0.98 / · |
| 10-04 01:12:34 | NEAR | down | 0.31→0.21 | 0.32 → 0.32 → 0.32 | no | — |  |
| 10-04 01:12:18 | SOL | down | 0.94→0.89 | 0.86 → 0.91 → 0.91 | no | — |  |
| 10-04 01:12:09 | DOGE | up | 0.38→0.49 | 0.68 → 0.68 → 0.68 | 6.70s | — |  |
| 10-04 01:12:05 | XRP | up | 0.64→0.81 | 0.90 → 0.90 → 0.90 | no | — |  |
| 10-04 01:12:05 | ZEC | up | 0.06→0.11 | 0.09 → 0.09 → 0.09 | 25.42s | — |  |
| 10-04 01:12:03 | SOL | down | 0.87→0.74 | 0.86 → 0.86 → 0.86 | no | DOWN @ 0.14 | -0.27 / -1.08 / · |
| 10-04 01:11:58 | NEAR | up | 0.25→0.32 | 0.40 → 0.40 → 0.41 | no | — |  |
| 10-04 01:11:56 | BTC | down | 0.53→0.48 | 0.69 → 0.69 → 0.52 | 4.42s | DOWN @ 0.32 | 1.26 / 0.37 / · |
| 10-04 01:11:52 | DOGE | down | 0.49→0.39 | 0.78 → 0.78 → 0.78 | 8.67s | DOWN @ 0.23 | 0.61 / -0.36 / · |
| 10-04 01:11:51 | ETH | down | 0.82→0.77 | 0.83 → 0.83 → 0.83 | 9.17s | DOWN @ 0.17 | -0.01 / -0.68 / · |
| 10-04 01:11:50 | XRP | up | 0.79→0.86 | 0.88 → 0.88 → 0.88 | 25.21s | — |  |
| 10-04 01:11:49 | HYPE | down | 0.94→0.87 | 0.97 → 0.97 → 0.97 | no | — |  |
| 10-04 01:11:42 | SOL | up | 0.86→0.91 | 0.94 → 0.94 → 0.89 | no | — |  |
