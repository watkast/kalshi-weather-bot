# Lag Tracker

*Updated Sat Oct 03 23:33 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🟢 **There's a tradable gap.** Buying right after a price jump made money in both halves of the data (hold to the close).

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 314 | 10.7s | 5% | 0% |
| BTC | 238 | 11.7s | 2% | 0% |
| DOGE | 336 | 10.3s | 2% | 0% |
| ETH | 303 | 11.0s | 3% | 0% |
| HYPE | 245 | 11.6s | 3% | 0% |
| NEAR | 274 | 10.4s | 4% | 0% |
| SOL | 577 | 10.0s | 4% | 0% |
| XRP | 526 | 10.3s | 4% | 0% |
| ZEC | 328 | 9.6s | 5% | 0% |
| **All** | **3141** | **10.6s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 1638 | 473 | $-176.28 | -2.5% | $-58.97 / $-117.31 |
| Sell after 30 sec | 1636 | 968 | $549.07 | +7.8% | $356.29 / $192.78 |
| Hold to the close | 1621 | 807 | $1114.09 | +16.0% | $632.02 / $482.07 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **38 ms** · Coinbase price delay: **6 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 23:33:16 | ZEC | up | 0.73→0.80 | 0.71 → 0.71 → 0.71 | 5.00s | UP @ 0.73 | -0.08 / · / · |
| 10-03 23:33:12 | XRP | down | 0.73→0.67 | 0.72 → 0.72 → 0.72 | no | — |  |
| 10-03 23:33:03 | ETH | up | 0.52→0.65 | 0.48 → 0.48 → 0.62 | 3.00s | UP @ 0.49 | 0.95 / · / · |
| 10-03 23:33:02 | DOGE | up | 0.46→0.55 | 0.56 → 0.56 → 0.65 | 3.75s | — |  |
| 10-03 23:32:58 | BTC | up | 0.47→0.55 | 0.57 → 0.57 → 0.57 | no | — |  |
| 10-03 23:32:57 | HYPE | up | 0.43→0.49 | 0.49 → 0.49 → 0.49 | no | — |  |
| 10-03 23:32:56 | ZEC | up | 0.59→0.67 | 0.50 → 0.50 → 0.50 | 9.50s | UP @ 0.51 | 1.57 / 2.08 / · |
| 10-03 23:32:54 | XRP | up | 0.50→0.57 | 0.67 → 0.67 → 0.67 | 12.00s | — |  |
| 10-03 23:32:48 | SOL | down | 0.70→0.61 | 0.73 → 0.73 → 0.73 | 17.26s | DOWN @ 0.27 | -0.38 / 0.99 / · |
| 10-03 23:32:40 | HYPE | down | 0.54→0.43 | 0.47 → 0.47 → 0.47 | no | — |  |
| 10-03 23:32:39 | XRP | up | 0.46→0.57 | 0.67 → 0.67 → 0.67 | 27.01s | — |  |
| 10-03 23:32:34 | ETH | down | 0.56→0.48 | 0.53 → 0.53 → 0.52 | no | — |  |
| 10-03 23:32:34 | BTC | down | 0.47→0.41 | 0.58 → 0.58 → 0.57 | no | DOWN @ 0.42 | -0.36 / -0.36 / · |
| 10-03 23:32:33 | SOL | down | 0.70→0.60 | 0.73 → 0.73 → 0.73 | no | DOWN @ 0.28 | -0.49 / -0.49 / · |
| 10-03 23:32:30 | DOGE | down | 0.55→0.46 | 0.61 → 0.61 → 0.61 | no | DOWN @ 0.40 | -0.44 / -0.05 / · |
| 10-03 23:32:23 | XRP | up | 0.54→0.60 | 0.68 → 0.68 → 0.68 | no | — |  |
| 10-03 23:32:16 | HYPE | down | 0.54→0.49 | 0.57 → 0.57 → 0.62 | 19.51s | DOWN @ 0.43 | -0.95 / 0.54 / · |
| 10-03 23:32:15 | SOL | down | 0.70→0.64 | 0.71 → 0.71 → 0.71 | no | DOWN @ 0.29 | -0.59 / -0.59 / · |
| 10-03 23:32:14 | DOGE | up | 0.42→0.55 | 0.61 → 0.61 → 0.61 | no | — |  |
| 10-03 23:32:08 | XRP | up | 0.47→0.53 | 0.62 → 0.62 → 0.62 | 12.01s | — |  |
| 10-03 23:32:00 | SOL | up | 0.67→0.73 | 0.72 → 0.72 → 0.72 | no | — |  |
| 10-03 23:31:58 | DOGE | up | 0.44→0.51 | 0.60 → 0.60 → 0.60 | no | — |  |
| 10-03 23:31:48 | NEAR | up | 0.53→0.58 | 0.57 → 0.57 → 0.61 | 2.26s | — |  |
| 10-03 23:31:45 | SOL | up | 0.67→0.75 | 0.72 → 0.72 → 0.72 | no | — |  |
| 10-03 23:31:36 | XRP | down | 0.47→0.38 | 0.64 → 0.55 → 0.55 | 0.00s | DOWN @ 0.46 | -0.46 / -1.25 / · |
| 10-03 23:31:35 | ETH | up | 0.56→0.63 | 0.57 → 0.57 → 0.53 | no | UP @ 0.58 | -0.96 / -0.25 / · |
| 10-03 23:31:31 | BTC | up | 0.44→0.55 | 0.56 → 0.56 → 0.57 | no | — |  |
| 10-03 23:31:28 | SOL | down | 0.66→0.60 | 0.70 → 0.70 → 0.70 | no | DOWN @ 0.31 | -0.69 / -0.69 / · |
| 10-03 23:31:19 | DOGE | up | 0.38→0.44 | 0.58 → 0.58 → 0.62 | 1.51s | — |  |
| 10-03 23:31:16 | XRP | up | 0.44→0.53 | 0.64 → 0.64 → 0.64 | no | — |  |
