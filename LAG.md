# Lag Tracker

*Updated Sun Oct 04 03:04 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 458 | 10.6s | 4% | 0% |
| BTC | 370 | 12.4s | 2% | 0% |
| DOGE | 488 | 10.6s | 2% | 0% |
| ETH | 468 | 11.2s | 3% | 0% |
| HYPE | 374 | 11.7s | 3% | 0% |
| NEAR | 410 | 10.8s | 4% | 0% |
| SOL | 909 | 10.6s | 3% | 0% |
| XRP | 840 | 11.1s | 3% | 0% |
| ZEC | 532 | 9.7s | 5% | 0% |
| **All** | **4849** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 2549 | 708 | $-298.22 | -2.7% | $-118.45 / $-179.77 |
| Sell after 30 sec | 2547 | 1476 | $797.97 | +7.2% | $488.46 / $309.51 |
| Hold to the close | 2534 | 1259 | $1631.97 | +14.9% | $991.84 / $640.13 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **38 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 03:04:08 | BNB | down | 0.24→0.16 | 0.27 → 0.27 → — | no | DOWN @ 0.75 | · / · / · |
| 10-04 03:03:59 | SOL | down | 0.28→0.22 | 0.34 → 0.32 → 0.32 | no | DOWN @ 0.69 | -0.51 / · / · |
| 10-04 03:03:54 | ZEC | down | 0.23→0.16 | 0.18 → 0.18 → 0.18 | no | — |  |
| 10-04 03:03:50 | BNB | down | 0.24→0.16 | 0.29 → 0.29 → 0.29 | no | — |  |
| 10-04 03:03:44 | NEAR | down | 0.25→0.19 | 0.32 → 0.32 → 0.28 | 1.03s | DOWN @ 0.70 | -0.30 / · / · |
| 10-04 03:03:38 | SOL | down | 0.31→0.25 | 0.33 → 0.33 → 0.33 | no | DOWN @ 0.68 | -0.62 / -0.42 / · |
| 10-04 03:03:35 | ETH | up | 0.32→0.45 | 0.30 → 0.30 → 0.30 | 10.03s | UP @ 0.31 | -0.40 / 0.38 / · |
| 10-04 03:03:23 | SOL | up | 0.23→0.28 | 0.32 → 0.32 → 0.32 | no | — |  |
| 10-04 03:03:08 | SOL | up | 0.23→0.28 | 0.34 → 0.34 → 0.34 | no | — |  |
| 10-04 03:03:02 | ETH | down | 0.41→0.33 | 0.36 → 0.36 → 0.36 | 12.79s | — |  |
| 10-04 03:03:01 | XRP | down | 0.33→0.17 | 0.38 → 0.39 → 0.39 | 13.29s | DOWN @ 0.62 | -0.44 / 1.20 / · |
| 10-04 03:03:00 | BNB | down | 0.32→0.26 | 0.34 → 0.34 → 0.34 | 14.29s | DOWN @ 0.66 | -0.42 / 0.19 / · |
| 10-04 03:02:47 | NEAR | up | 0.26→0.34 | 0.29 → 0.29 → 0.29 | 12.79s | — |  |
| 10-04 03:02:27 | SOL | down | 0.30→0.25 | 0.41 → 0.41 → 0.41 | 17.55s | DOWN @ 0.59 | -0.45 / 0.16 / · |
| 10-04 03:02:20 | HYPE | down | 0.49→0.42 | 0.49 → 0.49 → 0.49 | 24.30s | DOWN @ 0.52 | -0.46 / 0.75 / · |
| 10-04 03:02:16 | ZEC | down | 0.38→0.32 | 0.36 → 0.37 → 0.37 | 13.29s | — |  |
| 10-04 03:02:04 | SOL | down | 0.40→0.33 | 0.50 → 0.50 → 0.50 | 10.04s | DOWN @ 0.51 | -0.56 / 0.34 / · |
| 10-04 03:01:58 | XRP | down | 0.39→0.31 | 0.41 → 0.41 → 0.42 | no | DOWN @ 0.59 | -0.55 / -0.34 / · |
| 10-04 03:01:54 | ZEC | down | 0.40→0.34 | 0.44 → 0.44 → 0.44 | 5.53s | DOWN @ 0.57 | 0.25 / 0.15 / · |
| 10-04 03:01:49 | SOL | down | 0.49→0.40 | 0.62 → 0.62 → 0.62 | 10.79s | DOWN @ 0.38 | -0.44 / 1.65 / · |
| 10-04 03:01:39 | XRP | down | 0.37→0.30 | 0.40 → 0.40 → 0.41 | no | DOWN @ 0.61 | -0.65 / -0.75 / · |
| 10-04 03:01:15 | DOGE | down | 0.39→0.15 | 0.44 → 0.44 → 0.44 | 12.04s | DOWN @ 0.57 | -0.56 / 0.66 / · |
| 10-04 03:01:13 | ETH | up | 0.42→0.48 | 0.48 → 0.48 → 0.48 | 28.55s | — |  |
| 10-04 03:01:05 | ZEC | up | 0.37→0.43 | 0.35 → 0.35 → 0.35 | 7.04s | UP @ 0.36 | -0.04 / -0.43 / · |
| 10-04 02:58:40 | XRP | down | 0.13→0.07 | 0.13 → 0.13 → 0.13 | 10.07s | DOWN @ 0.88 | -0.37 / 0.55 / 1.12 |
| 10-04 02:58:28 | NEAR | up | 0.49→0.55 | 0.85 → 0.85 → 0.85 | 6.58s | — |  |
| 10-04 02:58:28 | HYPE | down | 0.81→0.53 | 0.86 → 0.86 → 0.86 | 6.83s | DOWN @ 0.15 | 2.53 / 2.34 / -1.59 |
| 10-04 02:58:27 | ETH | up | 0.59→0.66 | 0.78 → 0.78 → 0.78 | 8.08s | — |  |
| 10-04 02:58:22 | XRP | up | 0.08→0.17 | 0.14 → 0.12 → 0.12 | no | — |  |
| 10-04 02:58:17 | BTC | up | 0.35→0.43 | 0.47 → 0.47 → 0.55 | 2.83s | — |  |
