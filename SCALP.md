# Range-Scalp Bot

*Updated Wed Nov 04 10:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47092 | 41007 | 6085 (72) | 3 | $-13568.46 | -4.6% |
| **+10¢** | 35183 | 28126 | 7057 (97) | 4 | $-12381.97 | -5.6% |
| **+15¢** | 29463 | 21864 | 7599 (125) | 4 | $-11360.78 | -6.1% |
| **+20¢** | 26174 | 18214 | 7960 (165) | 4 | $-10030.67 | -6.1% |
| **+10¢ (15¢ stop)** | 57391 | 57298 | 93 (56) | 1 | $-21371.80 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 10:23 | +10 stop | DOGE | DOWN | 0.70 | 0.45 | -2.83 |
| 11-04 10:23 | +20 | DOGE | DOWN | 0.70 | open |  |
| 11-04 10:23 | +15 | DOGE | DOWN | 0.70 | open |  |
| 11-04 10:23 | +10 | DOGE | DOWN | 0.70 | open |  |
| 11-04 10:23 | +5 | DOGE | DOWN | 0.70 | 0.76 | 0.32 |
| 11-04 10:23 | +10 stop | BNB | UP | 0.55 | 0.71 | 1.27 |
| 11-04 10:23 | +10 | BNB | UP | 0.55 | 0.71 | 1.27 |
| 11-04 10:23 | +5 | BNB | UP | 0.55 | 0.71 | 1.27 |
| 11-04 10:23 | +10 stop | ZEC | DOWN | 0.25 | 0.59 | 3.09 |
| 11-04 10:22 | +10 | SOL | UP | 0.63 | 0.74 | 0.79 |
| 11-04 10:22 | +5 | SOL | UP | 0.63 | 0.74 | 0.79 |
| 11-04 10:22 | +10 stop | ETH | UP | 0.64 | 0.82 | 1.52 |
| 11-04 10:22 | +10 stop | SOL | UP | 0.64 | 0.74 | 0.69 |
| 11-04 10:22 | +10 stop | BTC | UP | 0.69 | open |  |
| 11-04 10:22 | +10 stop | XRP | UP | 0.68 | 0.92 | 2.25 |
| 11-04 10:22 | +5 | ETH | UP | 0.68 | 0.82 | 1.13 |
| 11-04 10:22 | +10 stop | BNB | DOWN | 0.44 | 0.61 | 1.35 |
| 11-04 10:22 | +10 | BNB | DOWN | 0.44 | 0.61 | 1.35 |
| 11-04 10:22 | +5 | BNB | DOWN | 0.44 | 0.61 | 1.35 |
| 11-04 10:21 | +10 stop | ETH | DOWN | 0.58 | 0.38 | -2.35 |
| 11-04 10:21 | +20 | ETH | DOWN | 0.58 | open |  |
| 11-04 10:21 | +15 | ETH | DOWN | 0.58 | open |  |
| 11-04 10:21 | +10 | ETH | DOWN | 0.58 | open |  |
| 11-04 10:21 | +5 | ETH | DOWN | 0.57 | 0.63 | 0.25 |
| 11-04 10:21 | +10 stop | ZEC | DOWN | 0.66 | 0.48 | -2.14 |
| 11-04 10:19 | +10 stop | SOL | DOWN | 0.59 | 0.70 | 0.78 |
| 11-04 10:18 | +10 stop | SOL | DOWN | 0.67 | 0.46 | -2.44 |
| 11-04 10:18 | +5 | NEAR | DOWN | 0.63 | open |  |
| 11-04 10:17 | +10 stop | BTC | DOWN | 0.67 | 0.40 | -3.03 |
| 11-04 10:17 | +10 stop | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-04 10:17 | +10 stop | XRP | DOWN | 0.62 | 0.39 | -2.64 |
| 11-04 10:17 | +10 stop | HYPE | DOWN | 0.67 | 0.45 | -2.54 |
| 11-04 10:16 | +10 stop | NEAR | UP | 0.48 | 0.74 | 2.28 |
| 11-04 10:16 | +20 | NEAR | UP | 0.48 | 0.74 | 2.28 |
| 11-04 10:16 | +15 | NEAR | UP | 0.48 | 0.74 | 2.28 |
| 11-04 10:16 | +10 | NEAR | UP | 0.48 | 0.74 | 2.28 |
| 11-04 10:16 | +5 | NEAR | UP | 0.48 | 0.56 | 0.44 |
| 11-04 10:16 | +10 stop | SOL | UP | 0.55 | 0.38 | -2.05 |
| 11-04 10:16 | +20 | SOL | UP | 0.55 | 0.81 | 2.31 |
| 11-04 10:16 | +15 | SOL | UP | 0.55 | 0.74 | 1.58 |
