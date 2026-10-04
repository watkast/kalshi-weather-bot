# Lag Tracker

*Updated Sun Oct 04 07:55 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 617 | 10.8s | 3% | 0% |
| BTC | 479 | 11.9s | 3% | 0% |
| DOGE | 663 | 10.3s | 2% | 0% |
| ETH | 651 | 11.2s | 3% | 0% |
| HYPE | 557 | 11.3s | 4% | 0% |
| NEAR | 639 | 10.8s | 3% | 0% |
| SOL | 1192 | 10.8s | 3% | 0% |
| XRP | 1185 | 10.9s | 3% | 0% |
| ZEC | 795 | 9.6s | 4% | 0% |
| **All** | **6778** | **10.8s** | **3%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 3470 | 965 | $-410.67 | -2.7% | $-189.26 / $-221.41 |
| Sell after 30 sec | 3468 | 1997 | $1077.13 | +7.2% | $559.91 / $517.22 |
| Hold to the close | 3430 | 1706 | $2266.30 | +15.3% | $1289.24 / $977.06 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **31 ms** · Coinbase price delay: **16 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-04 07:55:08 | NEAR | up | 0.40→0.51 | 0.64 → 0.64 → — | no | — |  |
| 10-04 07:55:08 | SOL | up | 0.26→0.33 | 0.54 → 0.54 → — | no | — |  |
| 10-04 07:55:06 | XRP | up | 0.76→0.83 | 0.90 → 0.90 → — | no | — |  |
| 10-04 07:54:53 | SOL | down | 0.48→0.40 | 0.66 → 0.66 → 0.54 | 4.29s | DOWN @ 0.35 | 0.56 / · / · |
| 10-04 07:54:45 | XRP | down | 0.89→0.83 | 0.92 → 0.92 → 0.92 | no | DOWN @ 0.08 | -0.16 / · / · |
| 10-04 07:54:28 | ZEC | down | 0.21→0.13 | 0.20 → 0.15 → 0.15 | 0.29s | — |  |
| 10-04 07:54:21 | DOGE | down | 0.73→0.66 | 0.89 → 0.89 → 0.89 | no | DOWN @ 0.12 | -0.45 / -0.25 / · |
| 10-04 07:54:14 | NEAR | down | 0.43→0.37 | 0.54 → 0.54 → 0.54 | no | DOWN @ 0.48 | -0.66 / -1.25 / · |
| 10-04 07:54:13 | BNB | down | 0.25→0.18 | 0.46 → 0.34 → 0.34 | 0.05s | DOWN @ 0.66 | -0.42 / 0.50 / · |
| 10-04 07:54:12 | SOL | down | 0.48→0.41 | 0.56 → 0.56 → 0.58 | no | DOWN @ 0.44 | -0.65 / -0.36 / · |
| 10-04 07:54:10 | XRP | up | 0.82→0.88 | 0.92 → 0.92 → 0.92 | no | — |  |
| 10-04 07:54:04 | ZEC | up | 0.23→0.34 | 0.20 → 0.20 → 0.20 | no | UP @ 0.21 | -0.53 / -0.91 / · |
| 10-04 07:53:55 | DOGE | up | 0.47→0.66 | 0.90 → 0.90 → 0.84 | no | — |  |
| 10-04 07:53:55 | NEAR | up | 0.32→0.45 | 0.55 → 0.55 → 0.54 | no | — |  |
| 10-04 07:53:50 | SOL | up | 0.35→0.48 | 0.72 → 0.72 → 0.72 | no | — |  |
| 10-04 07:53:40 | ZEC | down | 0.26→0.19 | 0.17 → 0.17 → 0.27 | no | — |  |
| 10-04 07:53:40 | NEAR | down | 0.38→0.30 | 0.57 → 0.57 → 0.55 | 17.81s | DOWN @ 0.43 | -0.26 / -0.06 / · |
| 10-04 07:53:40 | XRP | down | 0.92→0.81 | 0.95 → 0.95 → 0.93 | no | DOWN @ 0.05 | 0.11 / 0.19 / · |
| 10-04 07:53:39 | BNB | down | 0.41→0.29 | 0.42 → 0.42 → 0.41 | no | DOWN @ 0.58 | -0.36 / -0.76 / · |
| 10-04 07:53:35 | SOL | down | 0.62→0.52 | 0.68 → 0.68 → 0.68 | 22.07s | DOWN @ 0.33 | -0.90 / 0.66 / · |
| 10-04 07:53:25 | NEAR | down | 0.43→0.38 | 0.55 → 0.55 → 0.57 | no | DOWN @ 0.47 | -0.86 / -0.66 / · |
| 10-04 07:53:16 | DOGE | up | 0.54→0.67 | 0.89 → 0.89 → 0.89 | no | — |  |
| 10-04 07:53:14 | ZEC | up | 0.15→0.20 | 0.22 → 0.22 → 0.22 | 28.83s | — |  |
| 10-04 07:53:00 | NEAR | up | 0.36→0.41 | 0.54 → 0.54 → 0.54 | 27.08s | — |  |
| 10-04 07:52:58 | ZEC | down | 0.38→0.25 | 0.38 → 0.29 → 0.29 | 0.31s | — |  |
| 10-04 07:52:41 | BNB | down | 0.25→0.13 | 0.33 → 0.33 → 0.33 | no | DOWN @ 0.69 | -0.51 / -0.71 / · |
| 10-04 07:52:25 | NEAR | down | 0.50→0.41 | 0.70 → 0.70 → 0.65 | 1.58s | DOWN @ 0.32 | -0.22 / 0.57 / · |
| 10-04 07:52:16 | XRP | down | 0.92→0.86 | 0.94 → 0.94 → 0.94 | 11.08s | DOWN @ 0.06 | -0.13 / -0.01 / · |
| 10-04 07:52:15 | HYPE | up | 0.38→0.50 | 0.42 → 0.42 → 0.42 | no | UP @ 0.43 | -0.46 / -0.46 / · |
| 10-04 07:52:10 | ETH | down | 0.98→0.92 | 0.90 → 0.90 → 0.91 | no | — |  |
