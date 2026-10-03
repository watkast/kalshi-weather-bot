# Lag Tracker

*Updated Sat Oct 03 21:33 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 241 | 10.5s | 5% | 0% |
| BTC | 151 | 11.8s | 2% | 0% |
| DOGE | 233 | 10.2s | 3% | 0% |
| ETH | 179 | 10.8s | 4% | 0% |
| HYPE | 169 | 11.4s | 4% | 0% |
| NEAR | 173 | 9.5s | 4% | 0% |
| SOL | 353 | 9.4s | 4% | 0% |
| XRP | 353 | 10.1s | 4% | 0% |
| ZEC | 253 | 9.5s | 5% | 0% |
| **All** | **2105** | **10.3s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1100 | 334 | $-99.69 | -2.1% | $-21.78 / $-77.91 |
| Sell after 30 sec | 1100 | 675 | $429.46 | +9.1% | $286.90 / $142.56 |
| Hold to the close | 1090 | 562 | $961.46 | +20.6% | $571.25 / $390.21 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 21:33:33 | SOL | down | 0.40→0.32 | 0.45 → 0.45 → — | no | DOWN @ 0.56 | · / · / · |
| 10-03 21:33:21 | ZEC | down | 0.47→0.41 | 0.42 → 0.42 → 0.42 | no | — |  |
| 10-03 21:32:50 | XRP | up | 0.38→0.45 | 0.52 → 0.52 → 0.52 | no | — |  |
| 10-03 21:32:48 | SOL | down | 0.41→0.35 | 0.47 → 0.47 → 0.47 | no | DOWN @ 0.54 | -0.56 / -0.66 / · |
| 10-03 21:32:43 | BNB | down | 0.49→0.36 | 0.52 → 0.53 → 0.53 | no | DOWN @ 0.48 | -0.46 / -0.86 / · |
| 10-03 21:32:28 | BNB | up | 0.40→0.49 | 0.53 → 0.52 → 0.52 | no | — |  |
| 10-03 21:32:15 | NEAR | up | 0.63→0.70 | 0.79 → 0.80 → 0.80 | 12.93s | — |  |
| 10-03 21:32:07 | XRP | up | 0.36→0.43 | 0.53 → 0.53 → 0.53 | no | — |  |
| 10-03 21:32:05 | ETH | down | 0.42→0.36 | 0.46 → 0.46 → 0.46 | 7.68s | DOWN @ 0.55 | 0.25 / 0.45 / · |
| 10-03 21:32:01 | BTC | down | 0.50→0.45 | 0.54 → 0.54 → 0.54 | 11.93s | DOWN @ 0.47 | -0.46 / 0.44 / · |
| 10-03 21:32:00 | SOL | down | 0.47→0.41 | 0.48 → 0.47 → 0.47 | 12.43s | DOWN @ 0.54 | -0.66 / -0.26 / · |
| 10-03 21:31:57 | ZEC | up | 0.46→0.52 | 0.42 → 0.43 → 0.43 | no | UP @ 0.44 | -0.56 / -0.46 / · |
| 10-03 21:31:35 | SOL | up | 0.41→0.47 | 0.47 → 0.47 → 0.47 | no | — |  |
| 10-03 21:31:32 | NEAR | up | 0.52→0.58 | 0.61 → 0.61 → 0.61 | 11.19s | — |  |
| 10-03 21:31:30 | ETH | up | 0.39→0.47 | 0.39 → 0.39 → 0.39 | 12.69s | UP @ 0.39 | -0.44 / 0.25 / · |
| 10-03 21:31:27 | DOGE | down | 0.54→0.44 | 0.56 → 0.56 → 0.56 | no | DOWN @ 0.45 | -0.46 / -0.56 / · |
| 10-03 21:31:14 | HYPE | down | 0.47→0.40 | 0.50 → 0.46 → 0.46 | 0.15s | — |  |
| 10-03 21:31:08 | SOL | down | 0.44→0.38 | 0.48 → 0.48 → 0.48 | no | DOWN @ 0.53 | -0.56 / -0.46 / · |
| 10-03 21:30:47 | ZEC | down | 0.49→0.42 | 0.52 → 0.52 → 0.52 | no | DOWN @ 0.49 | -0.46 / -0.16 / · |
| 10-03 21:30:44 | BNB | down | 0.50→0.42 | — → 0.55 → 0.55 | no | — |  |
| 10-03 21:28:41 | BTC | up | 0.72→0.81 | 0.88 → 0.88 → 0.91 | 17.48s | — |  |
| 10-03 21:28:28 | HYPE | down | 0.78→0.71 | 0.88 → 0.94 → 0.94 | no | DOWN @ 0.07 | -0.26 / -0.56 / -0.77 |
| 10-03 21:27:36 | HYPE | down | 0.91→0.71 | 0.96 → 0.96 → 0.96 | 7.99s | — |  |
| 10-03 21:27:33 | SOL | down | 0.12→0.06 | 0.14 → 0.14 → 0.14 | 10.99s | DOWN @ 0.88 | -0.47 / 0.95 / 1.12 |
| 10-03 21:27:31 | BTC | down | 0.79→0.65 | 0.86 → 0.86 → 0.86 | 12.49s | DOWN @ 0.14 | -0.27 / 0.68 / -1.49 |
| 10-03 21:27:26 | ETH | down | 0.14→0.07 | 0.28 → 0.28 → 0.06 | 2.74s | DOWN @ 0.72 | 1.96 / 2.10 / 2.65 |
| 10-03 21:27:20 | BNB | down | 0.11→0.03 | 0.10 → 0.10 → 0.10 | no | DOWN @ 0.91 | -0.21 / -0.02 / 0.84 |
| 10-03 21:27:17 | NEAR | down | 0.09→0.03 | 0.04 → 0.04 → 0.04 | 26.50s | — |  |
| 10-03 21:27:13 | BTC | down | 0.90→0.82 | 0.95 → 0.95 → 0.95 | 15.25s | — |  |
| 10-03 21:27:04 | HYPE | up | 0.68→0.85 | 0.93 → 0.93 → 0.93 | no | — |  |
