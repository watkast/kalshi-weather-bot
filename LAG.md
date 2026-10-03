# Lag Tracker

*Updated Sat Oct 03 20:33 UTC. Paper money. Coin prices arrive live from Coinbase and Kraken; Kalshi's 15-minute crypto prices are checked every 0.5 seconds. When a coin move shifts the fair chance of UP by 5¢+ within 3 seconds, we time how long Kalshi takes to follow, and paper-buy the favored side if it's still 3¢+ cheap after fees.*

[← Back to all bots](README.md)

## Verdict

🔴 **No profitable gap yet.** Kalshi sometimes lags, but not by enough to beat the fees.

## How fast does Kalshi follow?

| Coin | Events | Kalshi catches up in (median) | Already moved before we could buy | Share of the move Kalshi made within 2 sec |
|---|---|---|---|---|
| BNB | 203 | 10.7s | 6% | 0% |
| BTC | 129 | 11.5s | 2% | 0% |
| DOGE | 187 | 9.8s | 2% | 0% |
| ETH | 128 | 10.8s | 2% | 0% |
| HYPE | 114 | 11.8s | 4% | 0% |
| NEAR | 139 | 9.2s | 4% | 0% |
| SOL | 300 | 9.0s | 5% | 0% |
| XRP | 288 | 9.8s | 5% | 0% |
| ZEC | 201 | 9.9s | 5% | 0% |
| **All** | **1689** | **9.9s** | **4%** | **0%** |

*"Catches up" = Kalshi's price moved at least half as far as our fair value did. "Already moved" = that had happened by the first Kalshi price we saw after the jump — those are moves the pros beat us to. Kalshi is checked every 0.5 seconds, so 0.5s is the fastest we can measure.*

## Paper trades on the gap

| Exit | Trades | Won | P&L | Return | Earlier / later half |
|---|---|---|---|---|---|
| Sell after 10 sec | 882 | 284 | $-65.40 | -1.8% | $-10.14 / $-55.26 |
| Sell after 30 sec | 882 | 557 | $363.54 | +9.8% | $260.33 / $103.21 |
| Hold to the close | 874 | 420 | $511.46 | +13.9% | $515.18 / $-3.72 |

*Same buys scored three ways. 10 contracts at Kalshi's quoted ask (a little optimistic — order-book depth isn't checked).*

## Feed speed

Kalshi price check round trip: **30 ms** · Coinbase price delay: **33 ms**

## Latest events

| Time (UTC) | Coin | Move | Fair | Kalshi before → at entry → 5s | Caught up | Trade | P&L (10s / 30s / close) |
|---|---|---|---|---|---|---|---|
| 10-03 20:33:06 | XRP | up | 0.29→0.35 | 0.34 → 0.34 → — | no | — |  |
| 10-03 20:32:52 | ZEC | down | 0.36→0.30 | 0.28 → 0.28 → 0.28 | 9.04s | — |  |
| 10-03 20:32:38 | DOGE | up | 0.24→0.30 | 0.32 → 0.32 → 0.32 | 22.54s | — |  |
| 10-03 20:32:38 | XRP | up | 0.24→0.29 | 0.28 → 0.28 → 0.28 | 8.28s | — |  |
| 10-03 20:32:30 | HYPE | down | 0.54→0.44 | 0.56 → 0.56 → 0.47 | 0.80s | DOWN @ 0.45 | 0.34 / -0.16 / · |
| 10-03 20:32:23 | DOGE | down | 0.30→0.25 | 0.34 → 0.34 → 0.34 | no | DOWN @ 0.67 | -0.22 / -0.32 / · |
| 10-03 20:32:12 | ZEC | down | 0.44→0.37 | 0.31 → 0.31 → 0.27 | 4.03s | — |  |
| 10-03 20:32:05 | XRP | down | 0.38→0.32 | 0.35 → 0.35 → 0.35 | 10.78s | — |  |
| 10-03 20:32:04 | SOL | down | 0.41→0.36 | 0.28 → 0.28 → 0.28 | no | — |  |
| 10-03 20:32:00 | HYPE | up | 0.44→0.54 | 0.42 → 0.42 → 0.47 | 15.54s | UP @ 0.43 | -0.06 / 0.84 / · |
| 10-03 20:32:00 | BNB | up | 0.26→0.36 | 0.34 → 0.34 → 0.34 | no | — |  |
| 10-03 20:31:50 | ZEC | up | 0.33→0.41 | 0.25 → 0.25 → 0.25 | 10.79s | UP @ 0.26 | -0.47 / -0.38 / · |
| 10-03 20:31:50 | XRP | up | 0.31→0.36 | 0.33 → 0.33 → 0.33 | 11.29s | — |  |
| 10-03 20:31:48 | SOL | up | 0.28→0.38 | 0.27 → 0.27 → 0.27 | 27.54s | UP @ 0.27 | -0.38 / 0.30 / · |
| 10-03 20:31:41 | BNB | down | 0.32→0.27 | 0.41 → 0.41 → 0.34 | 4.79s | DOWN @ 0.59 | 0.37 / 0.37 / · |
| 10-03 20:31:29 | BTC | down | 0.43→0.37 | 0.41 → 0.41 → 0.41 | 16.54s | — |  |
| 10-03 20:31:28 | SOL | down | 0.36→0.31 | 0.27 → 0.27 → 0.27 | no | — |  |
| 10-03 20:31:26 | BNB | down | 0.39→0.32 | 0.42 → 0.42 → 0.41 | 19.79s | DOWN @ 0.59 | -0.45 / 0.37 / · |
| 10-03 20:31:20 | NEAR | up | 0.28→0.33 | 0.31 → 0.31 → 0.31 | 26.04s | — |  |
| 10-03 20:31:10 | HYPE | down | 0.44→0.38 | 0.49 → 0.49 → 0.49 | 6.06s | DOWN @ 0.51 | 0.14 / 0.45 / · |
| 10-03 20:28:37 | BTC | down | 0.64→0.56 | 0.79 → 0.79 → 0.79 | no | DOWN @ 0.22 | -0.35 / -1.69 / -2.33 |
| 10-03 20:28:32 | XRP | down | 0.85→0.79 | 0.94 → 0.94 → 0.96 | no | DOWN @ 0.08 | -0.53 / -0.59 / -0.86 |
| 10-03 20:28:14 | XRP | up | 0.63→0.70 | 0.89 → 0.89 → 0.94 | 4.56s | — |  |
| 10-03 20:28:14 | ETH | up | 0.73→0.79 | 0.82 → 0.82 → 0.86 | 4.81s | — |  |
| 10-03 20:28:06 | SOL | up | 0.84→0.95 | 0.95 → 0.97 → 0.97 | no | — |  |
| 10-03 20:27:59 | XRP | up | 0.56→0.62 | 0.82 → 0.82 → 0.89 | 4.56s | — |  |
| 10-03 20:27:51 | SOL | up | 0.82→0.91 | 0.95 → 0.95 → 0.95 | no | — |  |
| 10-03 20:27:44 | XRP | up | 0.44→0.50 | 0.78 → 0.78 → 0.82 | 4.56s | — |  |
| 10-03 20:27:36 | SOL | up | 0.80→0.85 | 0.94 → 0.96 → 0.96 | no | — |  |
| 10-03 20:27:29 | XRP | up | 0.50→0.55 | 0.73 → 0.73 → 0.78 | 4.56s | — |  |
