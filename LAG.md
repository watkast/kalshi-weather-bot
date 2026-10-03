# Lag Tracker

*Updated Sat Oct 03 23:03 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 304 | 10.7s | 5% | 0% |
| BTC | 213 | 11.8s | 2% | 0% |
| DOGE | 312 | 10.3s | 2% | 0% |
| ETH | 273 | 11.2s | 3% | 0% |
| HYPE | 218 | 11.6s | 4% | 0% |
| NEAR | 245 | 10.5s | 3% | 0% |
| SOL | 520 | 9.9s | 4% | 0% |
| XRP | 475 | 10.3s | 4% | 0% |
| ZEC | 320 | 9.6s | 5% | 0% |
| **All** | **2880** | **10.6s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1496 | 430 | $-162.39 | -2.5% | $-60.34 / $-102.05 |
| Sell after 30 sec | 1493 | 889 | $516.96 | +8.1% | $327.57 / $189.39 |
| Hold to the close | 1484 | 722 | $891.57 | +14.1% | $598.03 / $293.54 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **38 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 23:03:12 | HYPE | down | 0.58→0.53 | 0.70 → 0.70 → 0.70 | no | DOWN @ 0.30 | · / · / · |
| 10-03 23:03:09 | ETH | down | 0.56→0.50 | 0.47 → 0.47 → 0.47 | no | — |  |
| 10-03 23:03:07 | DOGE | down | 0.38→0.31 | 0.41 → 0.41 → 0.41 | no | DOWN @ 0.59 | -0.45 / · / · |
| 10-03 23:03:05 | SOL | down | 0.40→0.34 | 0.44 → 0.44 → 0.43 | no | DOWN @ 0.57 | -0.46 / · / · |
| 10-03 23:02:56 | BNB | up | 0.28→0.40 | 0.49 → 0.49 → 0.49 | no | — |  |
| 10-03 23:02:54 | ETH | up | 0.47→0.54 | 0.49 → 0.49 → 0.49 | no | — |  |
| 10-03 23:02:49 | NEAR | down | 0.61→0.54 | 0.72 → 0.72 → 0.72 | no | DOWN @ 0.30 | -0.69 / · / · |
| 10-03 23:02:42 | SOL | down | 0.41→0.35 | 0.43 → 0.43 → 0.43 | no | DOWN @ 0.57 | -0.56 / -0.46 / · |
| 10-03 23:02:41 | BNB | up | 0.21→0.28 | 0.48 → 0.48 → 0.48 | no | — |  |
| 10-03 23:02:32 | HYPE | up | 0.55→0.63 | 0.56 → 0.56 → 0.67 | 3.26s | UP @ 0.57 | 0.56 / 0.15 / · |
| 10-03 23:02:26 | BNB | down | 0.33→0.22 | 0.46 → 0.46 → 0.46 | no | DOWN @ 0.55 | -0.76 / -0.86 / · |
| 10-03 23:02:25 | NEAR | down | 0.69→0.64 | 0.72 → 0.72 → 0.72 | no | DOWN @ 0.30 | -0.69 / -0.69 / · |
| 10-03 23:02:16 | XRP | up | 0.42→0.47 | 0.49 → 0.49 → 0.56 | 4.02s | — |  |
| 10-03 23:02:16 | HYPE | up | 0.60→0.73 | 0.56 → 0.56 → 0.56 | 19.76s | UP @ 0.56 | -0.36 / 0.66 / · |
| 10-03 23:02:13 | SOL | down | 0.44→0.38 | 0.47 → 0.47 → 0.47 | no | DOWN @ 0.54 | -0.36 / -0.16 / · |
| 10-03 23:01:58 | SOL | down | 0.44→0.38 | 0.46 → 0.46 → 0.46 | no | DOWN @ 0.56 | -0.66 / -0.56 / · |
| 10-03 23:01:50 | DOGE | down | 0.39→0.32 | 0.41 → 0.45 → 0.45 | no | DOWN @ 0.56 | -0.46 / -0.16 / · |
| 10-03 23:01:43 | SOL | up | 0.38→0.44 | 0.48 → 0.48 → 0.48 | no | — |  |
| 10-03 23:01:41 | NEAR | down | 0.75→0.68 | 0.71 → 0.71 → 0.71 | no | — |  |
| 10-03 23:01:35 | DOGE | up | 0.37→0.42 | 0.41 → 0.41 → 0.41 | 14.52s | — |  |
| 10-03 23:01:32 | ZEC | down | 0.65→0.57 | 0.65 → 0.65 → 0.64 | no | DOWN @ 0.36 | -0.43 / -1.12 / · |
| 10-03 23:01:28 | SOL | up | 0.38→0.44 | 0.45 → 0.45 → 0.45 | 7.02s | — |  |
| 10-03 23:01:22 | NEAR | up | 0.68→0.74 | — → 0.76 → 0.76 | no | — |  |
| 10-03 22:58:37 | BTC | down | 0.72→0.45 | 0.72 → 0.72 → 0.72 | no | DOWN @ 0.28 | -0.30 / -0.68 / 7.05 |
| 10-03 22:58:21 | BTC | down | 0.58→0.53 | 0.65 → 0.65 → 0.65 | no | DOWN @ 0.36 | -1.21 / -1.12 / 6.23 |
| 10-03 22:58:08 | DOGE | up | 0.01→0.09 | 0.01 → 0.01 → 0.01 | no | — |  |
| 10-03 22:57:51 | BTC | up | 0.50→0.56 | 0.56 → 0.56 → 0.56 | 6.28s | — |  |
| 10-03 22:57:21 | BTC | down | 0.70→0.54 | 0.56 → 0.56 → 0.56 | no | — |  |
| 10-03 22:57:12 | BNB | down | 0.70→0.57 | 0.96 → 0.95 → 0.95 | no | DOWN @ 0.05 | -0.10 / -0.26 / -0.57 |
| 10-03 22:57:06 | DOGE | down | 0.11→0.04 | 0.07 → 0.07 → 0.07 | 20.55s | — |  |
