# Lag Tracker

*Updated Sun Oct 04 05:34 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 540 | 10.8s | 4% | 0% |
| BTC | 426 | 11.9s | 2% | 0% |
| DOGE | 590 | 10.9s | 2% | 0% |
| ETH | 556 | 10.9s | 3% | 0% |
| HYPE | 471 | 11.6s | 3% | 0% |
| NEAR | 536 | 10.8s | 4% | 0% |
| SOL | 1066 | 10.6s | 3% | 0% |
| XRP | 1048 | 10.8s | 4% | 0% |
| ZEC | 699 | 9.7s | 4% | 0% |
| **All** | **5932** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3051 | 846 | $-380.28 | -2.9% | $-170.73 / $-209.55 |
| Sell after 30 sec | 3049 | 1746 | $898.70 | +6.8% | $527.25 / $371.45 |
| Hold to the close | 3036 | 1491 | $1782.14 | +13.6% | $961.44 / $820.70 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **31 ms** · Coinbase price delay: **15 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 05:34:34 | SOL | up | 0.46→0.53 | 0.58 → 0.58 → — | no | — |  |
| 10-04 05:34:30 | DOGE | up | 0.25→0.31 | 0.41 → 0.41 → 0.41 | no | — |  |
| 10-04 05:34:29 | XRP | up | 0.29→0.46 | 0.32 → 0.32 → 0.32 | no | UP @ 0.32 | · / · / · |
| 10-04 05:34:29 | BTC | up | 0.68→0.84 | 0.58 → 0.58 → 0.58 | no | UP @ 0.59 | · / · / · |
| 10-04 05:34:29 | NEAR | up | 0.26→0.32 | 0.25 → 0.25 → 0.25 | no | UP @ 0.26 | · / · / · |
| 10-04 05:34:29 | ETH | up | 0.46→0.56 | 0.43 → 0.43 → 0.43 | no | UP @ 0.44 | · / · / · |
| 10-04 05:34:19 | SOL | down | 0.53→0.46 | 0.55 → 0.55 → 0.58 | no | DOWN @ 0.46 | -0.85 / · / · |
| 10-04 05:34:11 | BTC | up | 0.60→0.68 | 0.56 → 0.56 → 0.56 | no | UP @ 0.57 | -0.46 / · / · |
| 10-04 05:34:06 | ETH | down | 0.47→0.30 | 0.42 → 0.42 → 0.43 | no | — |  |
| 10-04 05:34:01 | SOL | up | 0.39→0.46 | 0.46 → 0.46 → 0.46 | 6.06s | — |  |
| 10-04 05:33:56 | DOGE | up | 0.25→0.31 | 0.40 → 0.40 → 0.40 | no | — |  |
| 10-04 05:33:55 | ZEC | up | 0.66→0.71 | 0.73 → 0.73 → 0.73 | 11.81s | — |  |
| 10-04 05:33:52 | HYPE | down | 0.45→0.40 | 0.42 → 0.42 → 0.42 | no | — |  |
| 10-04 05:33:32 | ZEC | up | 0.58→0.66 | 0.60 → 0.60 → 0.60 | 5.06s | UP @ 0.61 | 0.17 / 0.78 / · |
| 10-04 05:33:26 | BTC | down | 0.79→0.71 | 0.57 → 0.57 → 0.57 | 10.82s | — |  |
| 10-04 05:33:24 | SOL | down | 0.50→0.43 | 0.58 → 0.51 → 0.51 | 0.31s | DOWN @ 0.50 | -0.56 / 0.04 / · |
| 10-04 05:33:22 | DOGE | down | 0.32→0.27 | 0.36 → 0.41 → 0.41 | no | DOWN @ 0.60 | -0.55 / -0.34 / · |
| 10-04 05:33:07 | DOGE | up | 0.27→0.32 | 0.37 → 0.36 → 0.36 | 14.59s | — |  |
| 10-04 05:33:02 | NEAR | down | 0.32→0.26 | 0.32 → 0.32 → 0.32 | 19.59s | DOWN @ 0.69 | -0.41 / 0.52 / · |
| 10-04 05:33:00 | SOL | up | 0.46→0.53 | 0.57 → 0.57 → 0.57 | no | — |  |
| 10-04 05:32:53 | BTC | up | 0.59→0.64 | 0.53 → 0.54 → 0.54 | 14.08s | UP @ 0.54 | -0.46 / -0.06 / · |
| 10-04 05:32:32 | XRP | down | 0.46→0.38 | 0.38 → 0.38 → 0.34 | 19.84s | — |  |
| 10-04 05:32:30 | SOL | up | 0.46→0.53 | 0.55 → 0.55 → 0.55 | no | — |  |
| 10-04 05:32:24 | DOGE | down | 0.33→0.27 | 0.36 → 0.36 → 0.36 | no | DOWN @ 0.64 | -0.44 / -0.54 / · |
| 10-04 05:32:13 | NEAR | up | 0.29→0.37 | 0.34 → 0.34 → 0.34 | no | — |  |
| 10-04 05:32:10 | ETH | up | 0.44→0.52 | 0.45 → 0.45 → 0.45 | no | UP @ 0.45 | -0.46 / -0.56 / · |
| 10-04 05:32:10 | SOL | down | 0.53→0.46 | 0.56 → 0.56 → 0.56 | no | DOWN @ 0.45 | -0.46 / -0.46 / · |
| 10-04 05:31:55 | XRP | down | 0.54→0.43 | 0.45 → 0.45 → 0.45 | 11.59s | — |  |
| 10-04 05:31:52 | BTC | up | 0.47→0.53 | 0.54 → 0.53 → 0.53 | no | UP @ 0.53 | -0.46 / -0.46 / · |
| 10-04 05:31:45 | SOL | down | 0.53→0.46 | 0.56 → 0.56 → 0.56 | no | DOWN @ 0.45 | -0.66 / -0.46 / · |
