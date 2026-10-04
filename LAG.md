# Lag Tracker

*Updated Sun Oct 04 00:53 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 376 | 10.8s | 5% | 0% |
| BTC | 291 | 11.7s | 2% | 0% |
| DOGE | 409 | 10.6s | 2% | 0% |
| ETH | 364 | 10.9s | 2% | 0% |
| HYPE | 288 | 11.8s | 3% | 0% |
| NEAR | 331 | 10.4s | 4% | 0% |
| SOL | 707 | 10.4s | 3% | 0% |
| XRP | 655 | 11.2s | 3% | 0% |
| ZEC | 392 | 9.6s | 5% | 0% |
| **All** | **3813** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2011 | 569 | $-203.73 | -2.4% | $-78.86 / $-124.87 |
| Sell after 30 sec | 2010 | 1174 | $666.88 | +7.7% | $418.18 / $248.70 |
| Hold to the close | 1968 | 991 | $1463.56 | +17.3% | $761.04 / $702.52 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **38 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 00:53:44 | SOL | down | 0.76→0.65 | 0.78 → 0.78 → — | no | DOWN @ 0.23 | · / · / · |
| 10-04 00:53:39 | ZEC | down | 0.61→0.49 | 0.57 → 0.59 → 0.59 | no | DOWN @ 0.42 | · / · / · |
| 10-04 00:53:28 | SOL | down | 0.76→0.69 | 0.77 → 0.77 → 0.77 | no | DOWN @ 0.24 | -0.55 / · / · |
| 10-04 00:53:12 | SOL | up | 0.68→0.75 | 0.45 → 0.45 → 0.76 | 4.79s | UP @ 0.45 | 2.68 / 2.89 / · |
| 10-04 00:53:07 | BTC | up | 0.75→0.85 | 0.71 → 0.71 → 0.71 | 15.54s | UP @ 0.72 | 0.01 / 0.53 / · |
| 10-04 00:53:07 | HYPE | up | 0.04→0.10 | 0.07 → 0.07 → 0.07 | no | — |  |
| 10-04 00:53:06 | XRP | up | 0.16→0.23 | 0.17 → 0.17 → 0.17 | 10.79s | UP @ 0.18 | -0.31 / 0.26 / · |
| 10-04 00:53:06 | ETH | up | 0.56→0.69 | 0.64 → 0.64 → 0.64 | 11.29s | UP @ 0.64 | -0.44 / 0.90 / · |
| 10-04 00:53:02 | ZEC | up | 0.55→0.61 | 0.50 → 0.47 → 0.47 | 14.54s | UP @ 0.48 | -0.46 / 0.54 / · |
| 10-04 00:52:57 | SOL | up | 0.32→0.40 | 0.33 → 0.33 → 0.45 | 4.79s | UP @ 0.34 | 0.66 / 3.91 / · |
| 10-04 00:52:47 | ZEC | up | 0.49→0.55 | 0.50 → 0.50 → 0.50 | 29.55s | — |  |
| 10-04 00:52:47 | BNB | up | 0.47→0.52 | 0.64 → 0.64 → 0.64 | 15.29s | — |  |
| 10-04 00:52:45 | DOGE | up | 0.10→0.15 | 0.10 → 0.10 → 0.12 | no | UP @ 0.10 | -0.04 / -0.19 / · |
| 10-04 00:52:45 | ETH | up | 0.45→0.53 | 0.52 → 0.52 → 0.47 | 17.04s | — |  |
| 10-04 00:52:28 | SOL | down | 0.37→0.29 | 0.33 → 0.33 → 0.35 | no | — |  |
| 10-04 00:52:27 | ZEC | down | 0.67→0.55 | 0.64 → 0.64 → 0.64 | 5.03s | DOWN @ 0.37 | 0.75 / 0.85 / · |
| 10-04 00:52:12 | ZEC | up | 0.64→0.72 | 0.66 → 0.66 → 0.66 | no | UP @ 0.67 | -0.73 / -2.04 / · |
| 10-04 00:52:10 | SOL | down | 0.41→0.30 | 0.42 → 0.42 → 0.42 | 6.53s | DOWN @ 0.58 | 0.46 / 0.25 / · |
| 10-04 00:51:51 | SOL | down | 0.45→0.37 | 0.42 → 0.42 → 0.42 | 26.04s | — |  |
| 10-04 00:51:36 | SOL | up | 0.34→0.41 | 0.42 → 0.42 → 0.42 | no | — |  |
| 10-04 00:51:25 | BNB | up | 0.29→0.34 | 0.44 → 0.44 → 0.44 | 6.79s | — |  |
| 10-04 00:51:21 | SOL | down | 0.41→0.34 | 0.42 → 0.42 → 0.42 | no | DOWN @ 0.58 | -0.46 / -0.46 / · |
| 10-04 00:51:09 | XRP | down | 0.29→0.22 | 0.28 → 0.28 → 0.28 | 23.04s | — |  |
| 10-04 00:51:05 | ZEC | down | 0.74→0.64 | 0.74 → 0.74 → 0.74 | 11.79s | DOWN @ 0.27 | -0.57 / 0.20 / · |
| 10-04 00:50:51 | SOL | up | 0.35→0.41 | 0.35 → 0.35 → 0.35 | 11.08s | UP @ 0.36 | -0.43 / 0.25 / · |
| 10-04 00:50:47 | XRP | down | 0.25→0.19 | 0.40 → 0.28 → 0.28 | 0.27s | — |  |
| 10-04 00:50:31 | SOL | down | 0.45→0.32 | 0.47 → 0.47 → 0.45 | 16.04s | DOWN @ 0.54 | -0.26 / 0.65 / · |
| 10-04 00:50:29 | XRP | down | 0.34→0.25 | 0.41 → 0.41 → 0.40 | 17.29s | DOWN @ 0.60 | -0.44 / 0.88 / · |
| 10-04 00:50:28 | BNB | down | 0.33→0.26 | 0.48 → 0.48 → 0.49 | 18.54s | DOWN @ 0.53 | -0.66 / 0.25 / · |
| 10-04 00:50:25 | ETH | up | 0.55→0.64 | 0.54 → 0.54 → 0.54 | no | UP @ 0.55 | -0.36 / -0.46 / · |
