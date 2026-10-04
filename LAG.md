# Lag Tracker

*Updated Sun Oct 04 02:04 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 416 | 10.6s | 4% | 0% |
| BTC | 333 | 12.5s | 2% | 0% |
| DOGE | 448 | 10.6s | 2% | 0% |
| ETH | 405 | 11.2s | 3% | 0% |
| HYPE | 327 | 11.6s | 3% | 0% |
| NEAR | 376 | 10.6s | 4% | 0% |
| SOL | 802 | 10.6s | 3% | 0% |
| XRP | 732 | 11.2s | 3% | 0% |
| ZEC | 465 | 9.7s | 5% | 0% |
| **All** | **4304** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2241 | 624 | $-254.42 | -2.6% | $-97.21 / $-157.21 |
| Sell after 30 sec | 2241 | 1304 | $719.11 | +7.5% | $442.38 / $276.73 |
| Hold to the close | 2229 | 1103 | $1456.24 | +15.2% | $959.33 / $496.91 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **39 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 02:03:59 | ETH | down | 0.67→0.62 | 0.67 → 0.67 → — | no | — |  |
| 10-04 02:03:57 | SOL | down | 0.82→0.72 | 0.81 → 0.81 → — | no | DOWN @ 0.19 | · / · / · |
| 10-04 02:03:42 | SOL | up | 0.76→0.82 | 0.81 → 0.81 → 0.81 | no | — |  |
| 10-04 02:03:24 | BNB | up | 0.14→0.20 | 0.28 → 0.28 → 0.28 | 9.50s | — |  |
| 10-04 02:03:16 | BTC | up | 0.59→0.64 | 0.68 → 0.68 → 0.68 | 17.76s | — |  |
| 10-04 02:03:16 | SOL | up | 0.66→0.75 | 0.70 → 0.70 → 0.75 | 3.00s | — |  |
| 10-04 02:03:15 | ETH | up | 0.54→0.61 | 0.49 → 0.49 → 0.64 | 3.50s | UP @ 0.50 | 0.95 / 0.85 / · |
| 10-04 02:03:02 | HYPE | up | 0.51→0.56 | 0.52 → 0.52 → 0.55 | 2.25s | — |  |
| 10-04 02:02:51 | NEAR | up | 0.67→0.72 | 0.76 → 0.76 → 0.76 | no | — |  |
| 10-04 02:02:46 | BNB | down | 0.21→0.15 | 0.32 → 0.32 → 0.33 | 17.51s | DOWN @ 0.70 | -0.71 / 0.01 / · |
| 10-04 02:02:45 | SOL | down | 0.71→0.63 | 0.70 → 0.70 → 0.77 | no | DOWN @ 0.30 | -0.98 / -0.40 / · |
| 10-04 02:02:42 | HYPE | down | 0.53→0.48 | 0.56 → 0.56 → 0.56 | 7.01s | DOWN @ 0.45 | -0.16 / -0.36 / · |
| 10-04 02:02:33 | ETH | up | 0.40→0.49 | 0.51 → 0.51 → 0.39 | no | — |  |
| 10-04 02:02:32 | DOGE | down | 0.62→0.56 | 0.76 → 0.76 → 0.64 | 2.26s | DOWN @ 0.25 | 0.70 / 0.31 / · |
| 10-04 02:02:20 | HYPE | up | 0.45→0.51 | 0.56 → 0.56 → 0.56 | no | — |  |
| 10-04 02:02:16 | DOGE | down | 0.68→0.62 | 0.76 → 0.76 → 0.76 | 18.01s | DOWN @ 0.25 | -0.37 / 0.70 / · |
| 10-04 02:02:16 | ETH | down | 0.53→0.47 | 0.51 → 0.51 → 0.51 | 18.01s | — |  |
| 10-04 02:02:16 | SOL | down | 0.72→0.63 | 0.82 → 0.82 → 0.68 | 3.01s | DOWN @ 0.18 | 1.13 / 0.84 / · |
| 10-04 02:02:16 | XRP | down | 0.84→0.75 | 0.83 → 0.83 → 0.83 | no | DOWN @ 0.17 | -0.30 / -0.11 / · |
| 10-04 02:02:16 | BTC | down | 0.71→0.63 | 0.69 → 0.69 → 0.70 | 18.26s | DOWN @ 0.31 | -0.50 / 0.18 / · |
| 10-04 02:02:05 | HYPE | down | 0.53→0.43 | 0.76 → 0.76 → 0.76 | 13.76s | DOWN @ 0.26 | -0.67 / 1.28 / · |
| 10-04 02:01:55 | DOGE | down | 0.68→0.62 | 0.74 → 0.74 → 0.74 | no | DOWN @ 0.26 | -0.57 / -0.47 / · |
| 10-04 02:01:50 | NEAR | up | 0.67→0.75 | 0.61 → 0.81 → 0.81 | 0.26s | — |  |
| 10-04 02:01:44 | HYPE | up | 0.69→0.75 | 0.80 → 0.80 → 0.80 | no | — |  |
| 10-04 02:01:40 | BTC | up | 0.66→0.75 | 0.69 → 0.69 → 0.69 | no | — |  |
| 10-04 02:01:34 | NEAR | up | 0.64→0.70 | — → 0.61 → 0.61 | no | UP @ 0.62 | -0.54 / 0.99 / · |
| 10-04 01:58:28 | ZEC | down | 0.96→0.90 | 0.99 → 0.99 → 0.99 | 12.06s | — |  |
| 10-04 01:58:18 | BTC | up | 0.89→0.96 | 0.94 → 0.94 → 0.94 | 21.56s | — |  |
| 10-04 01:58:18 | XRP | up | 0.05→0.42 | 0.04 → 0.04 → 0.04 | no | — |  |
| 10-04 01:58:04 | ZEC | down | 0.97→0.91 | 0.98 → 0.98 → 0.98 | no | — |  |
