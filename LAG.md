# Lag Tracker

*Updated Sun Oct 04 04:23 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 503 | 10.7s | 4% | 0% |
| BTC | 404 | 11.9s | 2% | 0% |
| DOGE | 539 | 10.7s | 2% | 0% |
| ETH | 521 | 10.9s | 3% | 0% |
| HYPE | 427 | 11.6s | 4% | 0% |
| NEAR | 477 | 10.7s | 4% | 0% |
| SOL | 982 | 10.6s | 3% | 0% |
| XRP | 940 | 11.0s | 4% | 0% |
| ZEC | 622 | 9.8s | 4% | 0% |
| **All** | **5415** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2813 | 785 | $-338.33 | -2.8% | $-150.73 / $-187.60 |
| Sell after 30 sec | 2813 | 1623 | $842.49 | +6.9% | $496.84 / $345.65 |
| Hold to the close | 2789 | 1395 | $1811.20 | +14.9% | $899.61 / $911.59 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **36 ms** · Coinbase price delay: **5 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 04:23:15 | NEAR | up | 0.60→0.66 | 0.73 → 0.73 → 0.73 | no | — |  |
| 10-04 04:23:12 | SOL | up | 0.39→0.45 | 0.43 → 0.43 → 0.43 | 10.29s | — |  |
| 10-04 04:22:53 | HYPE | up | 0.29→0.51 | 0.30 → 0.30 → 0.30 | 13.30s | UP @ 0.32 | -0.71 / 3.69 / · |
| 10-04 04:22:49 | NEAR | down | 0.73→0.61 | 0.89 → 0.89 → 0.80 | 2.80s | DOWN @ 0.12 | 0.41 / 1.08 / · |
| 10-04 04:22:48 | SOL | up | 0.40→0.45 | 0.45 → 0.45 → 0.43 | 34.06s | — |  |
| 10-04 04:22:42 | DOGE | up | 0.67→0.76 | 0.87 → 0.87 → 0.87 | no | — |  |
| 10-04 04:22:37 | XRP | down | 0.92→0.87 | 0.90 → 0.89 → 0.89 | no | — |  |
| 10-04 04:22:33 | HYPE | down | 0.34→0.25 | 0.36 → 0.36 → 0.34 | 18.56s | DOWN @ 0.65 | -0.32 / -0.02 / · |
| 10-04 04:22:27 | NEAR | down | 0.84→0.76 | 0.89 → 0.89 → 0.89 | 24.31s | DOWN @ 0.12 | -0.25 / 0.41 / · |
| 10-04 04:22:19 | ETH | down | 0.34→0.27 | 0.20 → 0.20 → 0.20 | 17.82s | — |  |
| 10-04 04:22:10 | SOL | up | 0.40→0.48 | 0.27 → 0.27 → 0.27 | 11.82s | UP @ 0.27 | -0.38 / 1.38 / · |
| 10-04 04:22:09 | BNB | up | 0.54→0.66 | 0.80 → 0.81 → 0.81 | no | — |  |
| 10-04 04:21:54 | DOGE | up | 0.55→0.72 | 0.81 → 0.81 → 0.81 | no | — |  |
| 10-04 04:21:40 | XRP | up | 0.84→0.89 | 0.85 → 0.85 → 0.85 | no | — |  |
| 10-04 04:21:39 | DOGE | down | 0.64→0.55 | 0.81 → 0.81 → 0.81 | no | DOWN @ 0.20 | -0.33 / -0.52 / · |
| 10-04 04:21:18 | SOL | down | 0.43→0.36 | 0.39 → 0.39 → 0.41 | no | — |  |
| 10-04 04:21:17 | BNB | down | 0.63→0.57 | 0.82 → 0.82 → 0.77 | 4.32s | DOWN @ 0.18 | 0.16 / -0.12 / · |
| 10-04 04:21:12 | NEAR | up | 0.70→0.79 | 0.80 → 0.80 → 0.80 | no | — |  |
| 10-04 04:21:00 | DOGE | down | 0.67→0.60 | 0.76 → 0.76 → 0.76 | no | DOWN @ 0.26 | -0.57 / -0.67 / · |
| 10-04 04:21:00 | BNB | up | 0.58→0.71 | 0.76 → 0.76 → 0.76 | no | — |  |
| 10-04 04:20:40 | ZEC | up | 0.83→0.90 | 0.86 → 0.86 → 0.86 | 11.83s | — |  |
| 10-04 04:20:32 | NEAR | down | 0.86→0.80 | 0.89 → 0.89 → 0.85 | 4.34s | DOWN @ 0.12 | -0.06 / -0.06 / · |
| 10-04 04:20:25 | ETH | down | 0.41→0.30 | 0.36 → 0.36 → 0.36 | 11.35s | DOWN @ 0.64 | -0.44 / 0.59 / · |
| 10-04 04:20:19 | XRP | down | 0.87→0.82 | 0.85 → 0.85 → 0.84 | 17.85s | — |  |
| 10-04 04:20:13 | NEAR | down | 0.86→0.80 | 0.90 → 0.90 → 0.90 | 24.10s | DOWN @ 0.12 | -0.43 / -0.06 / · |
| 10-04 04:20:10 | BNB | down | 0.61→0.52 | 0.64 → 0.64 → 0.64 | no | DOWN @ 0.37 | -0.53 / -1.41 / · |
| 10-04 04:20:08 | ZEC | down | 0.80→0.74 | 0.81 → 0.81 → 0.81 | no | DOWN @ 0.20 | -0.33 / -0.90 / · |
| 10-04 04:20:07 | ETH | up | 0.36→0.42 | 0.29 → 0.29 → 0.29 | 14.60s | UP @ 0.30 | -0.40 / -0.59 / · |
| 10-04 04:20:03 | BTC | up | 0.42→0.54 | 0.56 → 0.56 → 0.55 | 18.86s | — |  |
| 10-04 04:19:55 | BNB | up | 0.44→0.53 | 0.61 → 0.61 → 0.61 | 26.86s | — |  |
