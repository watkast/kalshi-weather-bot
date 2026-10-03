# Lag Tracker

*Updated Sat Oct 03 23:43 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 321 | 10.8s | 5% | 0% |
| BTC | 243 | 11.8s | 2% | 0% |
| DOGE | 348 | 10.3s | 2% | 0% |
| ETH | 310 | 10.9s | 3% | 0% |
| HYPE | 253 | 11.6s | 3% | 0% |
| NEAR | 281 | 10.4s | 4% | 0% |
| SOL | 606 | 10.0s | 3% | 0% |
| XRP | 552 | 10.3s | 4% | 0% |
| ZEC | 340 | 9.5s | 5% | 0% |
| **All** | **3254** | **10.6s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1695 | 489 | $-181.10 | -2.5% | $-63.33 / $-117.77 |
| Sell after 30 sec | 1693 | 999 | $560.43 | +7.7% | $359.44 / $200.99 |
| Hold to the close | 1621 | 807 | $1114.09 | +16.0% | $632.02 / $482.07 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **38 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 23:43:29 | HYPE | down | 0.12→0.06 | 0.12 → 0.12 → — | no | DOWN @ 0.89 | · / · / · |
| 10-03 23:43:28 | XRP | up | 0.73→0.94 | 0.94 → 0.94 → — | no | — |  |
| 10-03 23:43:24 | ZEC | down | 0.41→0.34 | 0.25 → 0.25 → 0.25 | no | — |  |
| 10-03 23:43:20 | ETH | down | 0.95→0.85 | 0.95 → 0.95 → 0.89 | 0.58s | DOWN @ 0.06 | · / · / · |
| 10-03 23:43:15 | SOL | down | 0.36→0.25 | 0.33 → 0.33 → 0.33 | no | DOWN @ 0.69 | -1.12 / · / · |
| 10-03 23:43:11 | XRP | up | 0.60→0.70 | 0.93 → 0.93 → 0.93 | no | — |  |
| 10-03 23:43:03 | ZEC | up | 0.23→0.29 | 0.05 → 0.05 → 0.11 | 2.59s | UP @ 0.06 | 0.24 / · / · |
| 10-03 23:42:58 | SOL | down | 0.28→0.13 | 0.46 → 0.46 → 0.46 | 7.34s | DOWN @ 0.55 | 0.76 / 0.25 / · |
| 10-03 23:42:56 | XRP | up | 0.59→0.69 | 0.92 → 0.92 → 0.92 | no | — |  |
| 10-03 23:42:48 | BNB | up | 0.25→0.35 | 0.84 → 0.84 → 0.89 | 17.34s | — |  |
| 10-03 23:42:43 | SOL | down | 0.38→0.29 | 0.48 → 0.48 → 0.48 | 22.35s | DOWN @ 0.52 | -0.26 / 1.06 / · |
| 10-03 23:42:41 | XRP | up | 0.59→0.67 | 0.90 → 0.90 → 0.90 | no | — |  |
| 10-03 23:42:32 | ETH | up | 0.84→0.90 | 0.83 → 0.83 → 0.90 | 3.35s | UP @ 0.84 | 0.43 / 0.69 / · |
| 10-03 23:42:28 | DOGE | up | 0.22→0.63 | 0.78 → 0.78 → 0.78 | no | — |  |
| 10-03 23:42:26 | XRP | up | 0.58→0.66 | 0.89 → 0.89 → 0.89 | no | — |  |
| 10-03 23:42:24 | BNB | up | 0.03→0.18 | 0.19 → 0.19 → 0.19 | 11.85s | — |  |
| 10-03 23:42:18 | NEAR | up | 0.09→0.15 | 0.04 → 0.04 → 0.05 | no | — |  |
| 10-03 23:42:17 | SOL | up | 0.24→0.39 | 0.26 → 0.26 → 0.49 | 3.60s | UP @ 0.27 | 1.78 / 1.78 / · |
| 10-03 23:42:15 | ZEC | down | 0.17→0.10 | 0.01 → 0.01 → 0.01 | no | — |  |
| 10-03 23:42:11 | XRP | up | 0.58→0.65 | 0.88 → 0.88 → 0.88 | no | — |  |
| 10-03 23:42:02 | SOL | down | 0.26→0.20 | 0.28 → 0.28 → 0.26 | no | DOWN @ 0.73 | -0.28 / -2.62 / · |
| 10-03 23:41:59 | ETH | up | 0.61→0.80 | 0.60 → 0.60 → 0.60 | 6.86s | UP @ 0.61 | 1.72 / 1.82 / · |
| 10-03 23:41:56 | XRP | down | 0.64→0.57 | 0.79 → 0.79 → 0.79 | no | DOWN @ 0.22 | -1.21 / -1.30 / · |
| 10-03 23:41:51 | DOGE | down | 0.25→0.18 | 0.68 → 0.65 → 0.65 | 15.12s | DOWN @ 0.36 | -0.43 / -0.43 / · |
| 10-03 23:41:43 | SOL | up | 0.21→0.27 | 0.34 → 0.34 → 0.34 | no | — |  |
| 10-03 23:41:36 | XRP | down | 0.64→0.57 | 0.80 → 0.80 → 0.80 | no | DOWN @ 0.21 | -0.34 / -1.10 / · |
| 10-03 23:41:30 | HYPE | down | 0.17→0.07 | 0.18 → 0.18 → 0.18 | 21.11s | DOWN @ 0.82 | -0.01 / 0.31 / · |
| 10-03 23:41:28 | SOL | up | 0.22→0.28 | 0.31 → 0.31 → 0.31 | no | — |  |
| 10-03 23:41:26 | ETH | down | 0.86→0.76 | 0.77 → 0.77 → 0.77 | 9.61s | — |  |
| 10-03 23:41:12 | SOL | down | 0.35→0.23 | 0.33 → 0.33 → 0.33 | no | DOWN @ 0.69 | -0.41 / -0.61 / · |
