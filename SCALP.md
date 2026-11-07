# Range-Scalp Bot

*Updated Sat Nov 07 05:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50485 | 44001 | 6484 (76) | 0 | $-14239.50 | -4.5% |
| **+10¢** | 37680 | 30130 | 7550 (102) | 0 | $-13176.58 | -5.6% |
| **+15¢** | 31549 | 23414 | 8135 (131) | 0 | $-12095.15 | -6.1% |
| **+20¢** | 28052 | 19524 | 8528 (173) | 0 | $-10695.07 | -6.1% |
| **+10¢ (15¢ stop)** | 61473 | 61374 | 99 (58) | 0 | $-22768.48 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 04:57 | +10 stop | ZEC | DOWN | 0.67 | 0.94 | 2.53 |
| 11-07 04:55 | +10 stop | ZEC | DOWN | 0.58 | 0.79 | 1.80 |
| 11-07 04:54 | +10 | DOGE | UP | 0.66 | 0.76 | 0.71 |
| 11-07 04:54 | +10 | ZEC | UP | 0.71 | no | -7.25 |
| 11-07 04:54 | +5 | DOGE | UP | 0.64 | 0.71 | 0.38 |
| 11-07 04:53 | +5 | ZEC | UP | 0.66 | no | -6.71 |
| 11-07 04:53 | +10 stop | DOGE | UP | 0.58 | 0.71 | 0.97 |
| 11-07 04:53 | +10 stop | ZEC | UP | 0.66 | 0.36 | -3.33 |
| 11-07 04:53 | +10 stop | NEAR | UP | 0.70 | 0.86 | 1.36 |
| 11-07 04:53 | +10 stop | DOGE | DOWN | 0.52 | 0.65 | 0.96 |
| 11-07 04:51 | +10 stop | ZEC | DOWN | 0.63 | 0.47 | -1.95 |
| 11-07 04:51 | +5 | BTC | DOWN | 0.68 | yes | -6.96 |
| 11-07 04:50 | +10 stop | NEAR | DOWN | 0.70 | 0.54 | -1.93 |
| 11-07 04:50 | +10 | NEAR | DOWN | 0.70 | yes | -7.15 |
| 11-07 04:50 | +10 stop | SOL | DOWN | 0.61 | 0.45 | -1.95 |
| 11-07 04:49 | +5 | NEAR | DOWN | 0.66 | yes | -6.80 |
| 11-07 04:49 | +10 stop | XRP | UP | 0.60 | 0.78 | 1.50 |
| 11-07 04:49 | +5 | XRP | UP | 0.60 | 0.65 | 0.17 |
| 11-07 04:49 | +10 stop | NEAR | DOWN | 0.53 | 0.67 | 1.06 |
| 11-07 04:49 | +20 | NEAR | DOWN | 0.53 | yes | -5.48 |
| 11-07 04:49 | +15 | NEAR | DOWN | 0.53 | yes | -5.48 |
| 11-07 04:49 | +10 | NEAR | DOWN | 0.53 | 0.67 | 1.06 |
| 11-07 04:49 | +5 | NEAR | DOWN | 0.53 | 0.59 | 0.25 |
| 11-07 04:49 | +10 stop | ETH | DOWN | 0.63 | 0.32 | -3.43 |
| 11-07 04:49 | +10 stop | BTC | DOWN | 0.64 | 0.40 | -2.74 |
| 11-07 04:49 | +5 | BTC | DOWN | 0.64 | 0.73 | 0.59 |
| 11-07 04:48 | +10 stop | DOGE | DOWN | 0.62 | 0.76 | 1.10 |
| 11-07 04:47 | +5 | SOL | DOWN | 0.65 | yes | -6.66 |
| 11-07 04:47 | +10 stop | XRP | UP | 0.56 | 0.73 | 1.38 |
| 11-07 04:47 | +10 stop | DOGE | DOWN | 0.67 | 0.52 | -1.84 |
| 11-07 04:47 | +10 stop | BNB | DOWN | 0.62 | 0.80 | 1.51 |
| 11-07 04:47 | +20 | BNB | DOWN | 0.62 | 0.82 | 1.72 |
| 11-07 04:47 | +15 | BNB | DOWN | 0.62 | 0.80 | 1.51 |
| 11-07 04:47 | +10 | BNB | DOWN | 0.62 | 0.80 | 1.51 |
| 11-07 04:47 | +5 | BNB | DOWN | 0.62 | 0.70 | 0.48 |
| 11-07 04:46 | +10 stop | SOL | DOWN | 0.66 | 0.49 | -2.04 |
| 11-07 04:46 | +10 | SOL | DOWN | 0.66 | yes | -6.76 |
| 11-07 04:46 | +5 | SOL | DOWN | 0.66 | 0.72 | 0.29 |
| 11-07 04:46 | +10 stop | ETH | DOWN | 0.68 | 0.47 | -2.44 |
| 11-07 04:46 | +20 | ETH | DOWN | 0.68 | yes | -6.96 |
