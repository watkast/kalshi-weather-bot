# Lag Tracker

*Updated Sun Oct 04 06:04 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 563 | 10.8s | 4% | 0% |
| BTC | 442 | 12.0s | 2% | 0% |
| DOGE | 604 | 10.6s | 2% | 0% |
| ETH | 585 | 11.2s | 3% | 0% |
| HYPE | 484 | 11.6s | 4% | 0% |
| NEAR | 545 | 10.8s | 4% | 0% |
| SOL | 1087 | 10.7s | 3% | 0% |
| XRP | 1087 | 10.8s | 4% | 0% |
| ZEC | 704 | 9.8s | 4% | 0% |
| **All** | **6101** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3131 | 862 | $-396.47 | -2.9% | $-178.94 / $-217.53 |
| Sell after 30 sec | 3131 | 1789 | $925.45 | +6.8% | $528.68 / $396.77 |
| Hold to the close | 3116 | 1545 | $1900.01 | +14.0% | $979.39 / $920.62 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **14 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 06:04:41 | XRP | up | 0.29→0.44 | 0.35 → 0.35 → — | no | UP @ 0.36 | · / · / · |
| 10-04 06:04:40 | SOL | up | 0.26→0.32 | 0.28 → 0.28 → — | no | — |  |
| 10-04 06:04:24 | SOL | up | 0.27→0.33 | 0.30 → 0.30 → 0.30 | no | — |  |
| 10-04 06:04:08 | SOL | down | 0.33→0.27 | 0.37 → 0.30 → 0.30 | 0.05s | — |  |
| 10-04 06:04:03 | BNB | down | 0.26→0.21 | 0.41 → 0.41 → 0.38 | 2.31s | DOWN @ 0.59 | -0.04 / 0.78 / · |
| 10-04 06:04:01 | XRP | down | 0.34→0.27 | 0.35 → 0.35 → 0.34 | no | DOWN @ 0.65 | -0.22 / -0.43 / · |
| 10-04 06:03:53 | BTC | down | 0.60→0.54 | 0.54 → 0.54 → 0.54 | no | — |  |
| 10-04 06:03:45 | HYPE | up | 0.30→0.43 | 0.35 → 0.35 → 0.35 | no | UP @ 0.37 | -0.53 / -0.83 / · |
| 10-04 06:03:45 | SOL | down | 0.39→0.33 | 0.35 → 0.35 → 0.35 | 20.82s | — |  |
| 10-04 06:03:43 | XRP | up | 0.26→0.34 | 0.40 → 0.40 → 0.40 | no | — |  |
| 10-04 06:03:28 | XRP | down | 0.35→0.26 | 0.36 → 0.36 → 0.36 | no | — |  |
| 10-04 06:03:18 | SOL | down | 0.36→0.30 | 0.34 → 0.34 → 0.34 | no | — |  |
| 10-04 06:03:10 | ZEC | down | 0.58→0.52 | 0.62 → 0.62 → 0.62 | 10.82s | DOWN @ 0.39 | -0.54 / -0.93 / · |
| 10-04 06:03:03 | XRP | down | 0.45→0.40 | 0.51 → 0.51 → 0.45 | 2.84s | DOWN @ 0.50 | 0.04 / 0.95 / · |
| 10-04 06:03:02 | BNB | down | 0.51→0.43 | 0.69 → 0.69 → 0.59 | 3.59s | DOWN @ 0.32 | 0.47 / 1.56 / · |
| 10-04 06:02:59 | BTC | up | 0.59→0.65 | 0.62 → 0.62 → 0.62 | no | — |  |
| 10-04 06:02:59 | DOGE | down | 0.36→0.28 | 0.41 → 0.41 → 0.41 | 6.34s | DOWN @ 0.59 | 0.06 / 0.98 / · |
| 10-04 06:02:57 | SOL | up | 0.37→0.43 | 0.42 → 0.42 → 0.42 | no | — |  |
| 10-04 06:02:55 | ETH | down | 0.54→0.44 | 0.52 → 0.52 → 0.52 | no | DOWN @ 0.49 | -0.46 / -0.16 / · |
| 10-04 06:02:52 | ZEC | down | 0.67→0.62 | 0.64 → 0.67 → 0.67 | 28.33s | — |  |
| 10-04 06:02:51 | NEAR | down | 0.35→0.30 | 0.41 → 0.41 → 0.41 | 14.59s | DOWN @ 0.60 | -0.44 / 0.37 / · |
| 10-04 06:02:47 | XRP | down | 0.55→0.50 | 0.55 → 0.55 → 0.51 | 3.33s | — |  |
| 10-04 06:02:42 | SOL | down | 0.43→0.37 | 0.43 → 0.43 → 0.43 | 23.60s | DOWN @ 0.57 | -0.36 / 0.56 / · |
| 10-04 06:02:30 | XRP | down | 0.55→0.45 | 0.51 → 0.51 → 0.51 | no | DOWN @ 0.50 | -0.96 / -0.56 / · |
| 10-04 06:02:25 | SOL | up | 0.37→0.43 | 0.42 → 0.42 → 0.42 | no | — |  |
| 10-04 06:02:23 | DOGE | down | 0.41→0.36 | 0.40 → 0.40 → 0.40 | no | — |  |
| 10-04 06:02:21 | ZEC | up | 0.55→0.60 | 0.54 → 0.55 → 0.55 | 14.34s | — |  |
| 10-04 06:02:15 | XRP | down | 0.47→0.40 | 0.51 → 0.51 → 0.51 | no | DOWN @ 0.50 | -0.56 / -0.96 / · |
| 10-04 06:02:09 | SOL | up | 0.37→0.43 | 0.46 → 0.46 → 0.46 | no | — |  |
| 10-04 06:01:54 | SOL | down | 0.46→0.38 | 0.49 → 0.49 → 0.49 | 26.35s | DOWN @ 0.51 | -0.46 / 0.14 / · |
