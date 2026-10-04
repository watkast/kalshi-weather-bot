# Lag Tracker

*Updated Sun Oct 04 03:44 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 478 | 10.7s | 4% | 0% |
| BTC | 387 | 11.9s | 2% | 0% |
| DOGE | 513 | 10.9s | 2% | 0% |
| ETH | 498 | 10.9s | 3% | 0% |
| HYPE | 401 | 11.6s | 4% | 0% |
| NEAR | 453 | 10.7s | 4% | 0% |
| SOL | 961 | 10.6s | 3% | 0% |
| XRP | 884 | 10.9s | 4% | 0% |
| ZEC | 581 | 9.6s | 4% | 0% |
| **All** | **5156** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2699 | 755 | $-317.73 | -2.7% | $-134.68 / $-183.05 |
| Sell after 30 sec | 2699 | 1565 | $826.65 | +7.0% | $493.00 / $333.65 |
| Hold to the close | 2649 | 1318 | $1675.44 | +14.6% | $942.34 / $733.10 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **37 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 03:43:25 | ZEC | up | 0.41→0.53 | 0.76 → 0.76 → 0.68 | no | — |  |
| 10-04 03:43:10 | ZEC | up | 0.61→0.68 | 0.62 → 0.62 → 0.76 | 2.61s | — |  |
| 10-04 03:42:55 | ZEC | down | 0.54→0.47 | 0.77 → 0.77 → 0.62 | 2.61s | — |  |
| 10-04 03:42:52 | NEAR | up | 0.68→0.78 | 0.93 → 0.93 → 0.93 | no | — |  |
| 10-04 03:42:28 | ZEC | down | 0.81→0.74 | 0.85 → 0.84 → 0.84 | 14.87s | — |  |
| 10-04 03:42:02 | ZEC | up | 0.80→0.86 | 0.89 → 0.89 → 0.89 | no | — |  |
| 10-04 03:41:39 | NEAR | down | 0.72→0.66 | 0.95 → 0.95 → 0.92 | no | DOWN @ 0.06 | 0.09 / 0.08 / · |
| 10-04 03:41:35 | ZEC | down | 0.90→0.83 | 0.92 → 0.92 → 0.92 | 7.88s | DOWN @ 0.09 | 0.45 / 0.07 / · |
| 10-04 03:41:24 | NEAR | down | 0.85→0.76 | 0.91 → 0.91 → 0.95 | no | DOWN @ 0.10 | -0.59 / -0.31 / · |
| 10-04 03:41:15 | BNB | down | 0.92→0.84 | 0.99 → 0.99 → 0.99 | no | — |  |
| 10-04 03:41:03 | ZEC | up | 0.71→0.81 | 0.74 → 0.74 → 0.74 | 9.39s | UP @ 0.75 | 1.08 / 1.40 / · |
| 10-04 03:41:03 | NEAR | up | 0.64→0.72 | 0.82 → 0.82 → 0.82 | 9.89s | — |  |
| 10-04 03:40:48 | ZEC | up | 0.60→0.68 | 0.57 → 0.57 → 0.57 | 9.40s | UP @ 0.60 | 0.99 / 2.55 / · |
| 10-04 03:40:37 | NEAR | up | 0.45→0.52 | 0.61 → 0.61 → 0.61 | 5.64s | — |  |
| 10-04 03:40:33 | ZEC | down | 0.56→0.43 | 0.56 → 0.56 → 0.56 | no | DOWN @ 0.45 | -0.85 / -2.32 / · |
| 10-04 03:40:08 | ZEC | down | 0.60→0.53 | 0.58 → 0.58 → 0.43 | 4.65s | — |  |
| 10-04 03:39:56 | BNB | down | 0.82→0.62 | 0.93 → 0.93 → 0.98 | no | — |  |
| 10-04 03:39:49 | ZEC | up | 0.45→0.54 | 0.57 → 0.57 → 0.57 | no | — |  |
| 10-04 03:39:44 | DOGE | down | 0.92→0.76 | 0.90 → 0.88 → 0.88 | 28.66s | DOWN @ 0.13 | -0.35 / 0.69 / · |
| 10-04 03:39:29 | DOGE | up | 0.67→0.75 | 0.88 → 0.90 → 0.90 | no | — |  |
| 10-04 03:39:25 | BNB | up | 0.65→0.83 | 0.91 → 0.91 → 0.91 | no | — |  |
| 10-04 03:38:52 | NEAR | down | 0.55→0.46 | 0.75 → 0.75 → 0.75 | 20.17s | DOWN @ 0.26 | -0.38 / 0.50 / · |
| 10-04 03:38:47 | ZEC | down | 0.69→0.61 | 0.69 → 0.69 → 0.69 | 10.67s | DOWN @ 0.33 | -0.71 / 0.07 / · |
| 10-04 03:38:37 | NEAR | up | 0.51→0.57 | 0.69 → 0.69 → 0.69 | 5.17s | — |  |
| 10-04 03:38:37 | DOGE | up | 0.62→0.77 | 0.82 → 0.82 → 0.82 | no | — |  |
| 10-04 03:38:13 | XRP | up | 0.88→0.94 | 0.86 → 0.86 → 0.86 | 14.43s | UP @ 0.87 | -0.27 / 0.19 / · |
| 10-04 03:37:54 | NEAR | down | 0.62→0.57 | 0.81 → 0.81 → 0.69 | 3.43s | DOWN @ 0.20 | 0.73 / 0.53 / · |
| 10-04 03:37:50 | ZEC | down | 0.65→0.54 | 0.64 → 0.64 → 0.64 | no | — |  |
| 10-04 03:37:31 | ETH | up | 0.79→0.85 | 0.80 → 0.80 → 0.80 | no | — |  |
| 10-04 03:37:29 | NEAR | up | 0.61→0.72 | 0.71 → 0.71 → 0.71 | 13.69s | — |  |
