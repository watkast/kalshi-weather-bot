# Lag Tracker

*Updated Sun Oct 04 06:14 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 574 | 10.8s | 3% | 0% |
| BTC | 447 | 12.0s | 2% | 0% |
| DOGE | 617 | 10.5s | 2% | 0% |
| ETH | 593 | 11.2s | 3% | 0% |
| HYPE | 491 | 11.6s | 3% | 0% |
| NEAR | 551 | 10.8s | 4% | 0% |
| SOL | 1104 | 10.8s | 3% | 0% |
| XRP | 1110 | 10.8s | 3% | 0% |
| ZEC | 709 | 9.8s | 4% | 0% |
| **All** | **6196** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3176 | 876 | $-401.22 | -2.9% | $-175.35 / $-225.87 |
| Sell after 30 sec | 3176 | 1816 | $937.05 | +6.8% | $526.09 / $410.96 |
| Hold to the close | 3116 | 1545 | $1900.01 | +14.0% | $979.39 / $920.62 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **14 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 06:13:31 | SOL | up | 0.37→0.48 | 0.69 → 0.69 → 0.66 | 19.39s | — |  |
| 10-04 06:13:18 | XRP | down | 0.12→0.06 | 0.23 → 0.23 → 0.10 | 2.89s | DOWN @ 0.79 | 0.81 / 0.94 / · |
| 10-04 06:13:15 | SOL | up | 0.59→0.68 | 0.90 → 0.90 → 0.90 | no | — |  |
| 10-04 06:13:10 | BNB | down | 0.27→0.21 | 0.85 → 0.85 → 0.85 | no | DOWN @ 0.16 | -0.39 / -0.39 / · |
| 10-04 06:13:03 | XRP | down | 0.24→0.14 | 0.26 → 0.26 → 0.23 | 17.90s | DOWN @ 0.76 | -0.26 / 1.10 / · |
| 10-04 06:13:01 | ZEC | down | 0.82→0.75 | 0.89 → 0.89 → 0.87 | no | — |  |
| 10-04 06:13:00 | SOL | up | 0.58→0.67 | 0.89 → 0.89 → 0.89 | no | — |  |
| 10-04 06:12:46 | XRP | up | 0.10→0.25 | 0.27 → 0.27 → 0.26 | no | — |  |
| 10-04 06:12:40 | SOL | down | 0.72→0.65 | 0.90 → 0.90 → 0.90 | no | DOWN @ 0.10 | -0.17 / -0.12 / · |
| 10-04 06:12:34 | ZEC | down | 0.93→0.83 | 0.99 → 0.99 → 0.98 | 16.66s | — |  |
| 10-04 06:12:32 | BNB | up | 0.12→0.49 | 0.81 → 0.81 → 0.89 | no | — |  |
| 10-04 06:12:31 | XRP | down | 0.38→0.27 | 0.28 → 0.28 → 0.27 | no | — |  |
| 10-04 06:12:13 | XRP | down | 0.39→0.29 | 0.32 → 0.32 → 0.32 | 22.41s | — |  |
| 10-04 06:12:09 | BNB | down | 0.26→0.12 | 0.74 → 0.74 → 0.74 | no | DOWN @ 0.26 | -0.38 / -1.81 / · |
| 10-04 06:12:04 | HYPE | up | 0.17→0.23 | 0.23 → 0.23 → 0.19 | no | — |  |
| 10-04 06:11:59 | DOGE | down | 0.73→0.37 | 0.92 → 0.92 → 0.92 | no | DOWN @ 0.09 | 1.31 / 1.21 / · |
| 10-04 06:11:51 | NEAR | down | 0.09→0.04 | 0.11 → 0.08 → 0.08 | 0.15s | DOWN @ 0.92 | -0.14 / 0.32 / · |
| 10-04 06:11:51 | XRP | up | 0.24→0.31 | 0.67 → 0.63 → 0.63 | no | — |  |
| 10-04 06:11:50 | BTC | down | 0.87→0.67 | 0.81 → 0.81 → 0.83 | no | DOWN @ 0.19 | -0.51 / 0.26 / · |
| 10-04 06:11:49 | HYPE | down | 0.30→0.19 | 0.27 → 0.27 → 0.23 | 16.66s | DOWN @ 0.75 | -0.38 / 0.14 / · |
| 10-04 06:11:49 | SOL | down | 0.87→0.68 | 0.96 → 0.96 → 0.97 | 16.91s | — |  |
| 10-04 06:11:43 | ETH | down | 0.55→0.41 | 0.51 → 0.51 → 0.51 | 22.17s | DOWN @ 0.51 | -0.96 / 3.65 / · |
| 10-04 06:11:36 | XRP | up | 0.50→0.60 | 0.69 → 0.67 → 0.67 | no | UP @ 0.67 | -0.42 / -3.91 / · |
| 10-04 06:11:31 | SOL | up | 0.82→0.89 | 0.95 → 0.95 → 0.96 | no | — |  |
| 10-04 06:11:21 | XRP | down | 0.68→0.50 | 0.69 → 0.69 → 0.69 | no | — |  |
| 10-04 06:11:18 | BTC | up | 0.84→0.91 | 0.80 → 0.80 → 0.79 | no | UP @ 0.80 | -0.45 / -0.13 / · |
| 10-04 06:11:15 | SOL | up | 0.77→0.85 | 0.92 → 0.92 → 0.92 | 20.42s | — |  |
| 10-04 06:11:11 | BNB | down | 0.44→0.22 | 0.84 → 0.84 → 0.84 | no | DOWN @ 0.18 | -0.12 / 0.45 / · |
| 10-04 06:11:06 | HYPE | down | 0.27→0.22 | 0.27 → 0.28 → 0.28 | no | — |  |
| 10-04 06:11:05 | XRP | up | 0.50→0.75 | 0.70 → 0.72 → 0.72 | no | — |  |
