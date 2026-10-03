# Lag Tracker

*Updated Sat Oct 03 21:13 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 225 | 10.4s | 6% | 0% |
| BTC | 142 | 11.6s | 2% | 0% |
| DOGE | 220 | 10.2s | 2% | 0% |
| ETH | 163 | 10.8s | 3% | 0% |
| HYPE | 155 | 11.6s | 4% | 0% |
| NEAR | 165 | 9.3s | 4% | 0% |
| SOL | 331 | 9.3s | 4% | 0% |
| XRP | 340 | 10.2s | 4% | 0% |
| ZEC | 239 | 9.6s | 5% | 0% |
| **All** | **1980** | **10.2s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1023 | 321 | $-81.77 | -1.9% | $-17.07 / $-64.70 |
| Sell after 30 sec | 1022 | 639 | $420.46 | +9.7% | $277.24 / $143.22 |
| Hold to the close | 965 | 480 | $690.07 | +16.8% | $534.41 / $155.66 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 21:13:15 | ETH | up | 0.27→0.37 | 0.24 → 0.24 → 0.24 | 7.56s | UP @ 0.25 | 0.99 / · / · |
| 10-03 21:13:00 | ZEC | down | 0.13→0.04 | 0.05 → 0.05 → 0.05 | no | — |  |
| 10-03 21:12:54 | ETH | down | 0.29→0.21 | 0.09 → 0.28 → 0.28 | no | DOWN @ 0.72 | -0.40 / -1.62 / · |
| 10-03 21:12:39 | ETH | up | 0.08→0.15 | 0.09 → 0.09 → 0.09 | 13.06s | UP @ 0.09 | -0.17 / 1.18 / · |
| 10-03 21:12:23 | ETH | up | 0.03→0.10 | 0.02 → 0.08 → 0.08 | 0.27s | — |  |
| 10-03 21:12:23 | ZEC | down | 0.25→0.20 | 0.04 → 0.07 → 0.07 | no | — |  |
| 10-03 21:12:11 | HYPE | up | 0.82→0.93 | 0.88 → 0.95 → 0.95 | 0.27s | — |  |
| 10-03 21:11:59 | NEAR | down | 0.90→0.84 | 0.96 → 0.96 → 0.96 | no | — |  |
| 10-03 21:11:57 | ZEC | up | 0.12→0.17 | 0.02 → 0.02 → 0.02 | 26.32s | — |  |
| 10-03 21:11:52 | HYPE | up | 0.64→0.81 | 0.86 → 0.86 → 0.88 | 16.06s | — |  |
| 10-03 21:11:41 | ZEC | up | 0.11→0.16 | 0.03 → 0.03 → 0.03 | no | — |  |
| 10-03 21:11:15 | HYPE | up | 0.58→0.67 | 0.78 → 0.78 → 0.78 | 22.81s | — |  |
| 10-03 21:10:41 | NEAR | up | 0.64→0.72 | 0.80 → 0.80 → 0.80 | 11.12s | — |  |
| 10-03 21:10:22 | NEAR | up | 0.53→0.67 | 0.56 → 0.56 → 0.77 | 0.56s | UP @ 0.57 | 1.48 / 1.79 / · |
| 10-03 21:09:48 | HYPE | up | 0.68→0.81 | 0.80 → 0.80 → 0.81 | no | — |  |
| 10-03 21:09:48 | NEAR | down | 0.49→0.43 | 0.60 → 0.60 → 0.60 | 20.07s | DOWN @ 0.41 | -0.44 / -0.15 / · |
| 10-03 21:09:33 | HYPE | down | 0.75→0.68 | 0.78 → 0.78 → 0.80 | no | DOWN @ 0.24 | -0.74 / -0.84 / · |
| 10-03 21:09:10 | HYPE | down | 0.84→0.74 | 0.83 → 0.83 → 0.83 | 12.58s | DOWN @ 0.17 | -0.30 / -0.01 / · |
| 10-03 21:09:05 | NEAR | down | 0.70→0.65 | 0.81 → 0.81 → 0.77 | 3.33s | DOWN @ 0.20 | -0.05 / 2.20 / · |
| 10-03 21:09:02 | BNB | down | 0.14→0.08 | 0.26 → 0.26 → 0.26 | 6.33s | DOWN @ 0.75 | 1.19 / 1.69 / · |
| 10-03 21:08:45 | NEAR | down | 0.74→0.69 | 0.84 → 0.84 → 0.84 | 7.84s | DOWN @ 0.18 | -0.22 / 0.16 / · |
| 10-03 21:08:31 | BNB | down | 0.45→0.39 | 0.45 → 0.45 → 0.45 | 21.84s | — |  |
| 10-03 21:08:25 | NEAR | up | 0.73→0.82 | 0.81 → 0.85 → 0.85 | no | — |  |
| 10-03 21:08:18 | ZEC | down | 0.17→0.12 | 0.09 → 0.09 → 0.06 | 4.59s | — |  |
| 10-03 21:08:08 | BNB | up | 0.25→0.42 | 0.36 → 0.36 → 0.36 | no | — |  |
| 10-03 21:08:03 | NEAR | up | 0.69→0.76 | 0.79 → 0.79 → 0.81 | 19.60s | — |  |
| 10-03 21:08:03 | ZEC | up | 0.12→0.18 | 0.10 → 0.10 → 0.09 | no | UP @ 0.11 | -0.30 / -0.66 / · |
| 10-03 21:08:02 | HYPE | up | 0.66→0.72 | 0.70 → 0.70 → 0.70 | 6.10s | — |  |
| 10-03 21:07:20 | ZEC | down | 0.19→0.14 | 0.10 → 0.10 → 0.14 | no | — |  |
| 10-03 21:07:13 | HYPE | down | 0.73→0.65 | 0.62 → 0.62 → 0.62 | no | — |  |
