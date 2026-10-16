# Range-Scalp Bot

*Updated Fri Oct 16 06:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18774 | 16306 | 2468 (28) | 3 | $-5707.92 | -4.8% |
| **+10¢** | 14149 | 11293 | 2856 (40) | 3 | $-5182.27 | -5.8% |
| **+15¢** | 11861 | 8787 | 3074 (59) | 4 | $-4696.12 | -6.3% |
| **+20¢** | 10534 | 7317 | 3217 (78) | 4 | $-4123.56 | -6.2% |
| **+10¢ (15¢ stop)** | 23123 | 23073 | 50 (29) | 0 | $-8927.92 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 06:28 | +10 stop | BNB | UP | 0.62 | 0.20 | -4.49 |
| 10-16 06:28 | +20 | BNB | UP | 0.62 | open |  |
| 10-16 06:28 | +15 | BNB | UP | 0.62 | open |  |
| 10-16 06:28 | +10 | BNB | UP | 0.62 | open |  |
| 10-16 06:28 | +5 | BNB | UP | 0.62 | open |  |
| 10-16 06:26 | +10 stop | BNB | UP | 0.65 | 0.80 | 1.22 |
| 10-16 06:26 | +10 | BNB | UP | 0.63 | 0.80 | 1.41 |
| 10-16 06:26 | +5 | BNB | UP | 0.63 | 0.68 | 0.17 |
| 10-16 06:24 | +10 stop | BNB | UP | 0.46 | 0.60 | 1.06 |
| 10-16 06:24 | +5 | BNB | UP | 0.46 | 0.60 | 1.06 |
| 10-16 06:23 | +10 stop | NEAR | DOWN | 0.69 | 0.52 | -2.02 |
| 10-16 06:23 | +10 | NEAR | DOWN | 0.69 | 0.79 | 0.74 |
| 10-16 06:23 | +5 | NEAR | DOWN | 0.69 | 0.74 | 0.22 |
| 10-16 06:23 | +10 stop | NEAR | UP | 0.47 | 0.57 | 0.68 |
| 10-16 06:23 | +20 | NEAR | UP | 0.47 | open |  |
| 10-16 06:23 | +15 | NEAR | UP | 0.47 | open |  |
| 10-16 06:23 | +10 | NEAR | UP | 0.47 | 0.57 | 0.68 |
| 10-16 06:23 | +5 | NEAR | UP | 0.47 | 0.57 | 0.68 |
| 10-16 06:23 | +10 stop | BNB | UP | 0.51 | 0.68 | 1.36 |
| 10-16 06:20 | +10 stop | BNB | DOWN | 0.61 | 0.71 | 0.68 |
| 10-16 06:19 | +10 stop | ETH | UP | 0.62 | 0.82 | 1.72 |
| 10-16 06:19 | +10 stop | ZEC | UP | 0.67 | 0.78 | 0.81 |
| 10-16 06:19 | +10 stop | BTC | UP | 0.59 | 0.70 | 0.78 |
| 10-16 06:19 | +10 stop | SOL | UP | 0.69 | 0.80 | 0.83 |
| 10-16 06:19 | +10 | SOL | UP | 0.69 | 0.80 | 0.83 |
| 10-16 06:19 | +5 | SOL | UP | 0.69 | 0.76 | 0.42 |
| 10-16 06:18 | +5 | XRP | UP | 0.64 | 0.81 | 1.42 |
| 10-16 06:18 | +5 | XRP | UP | 0.54 | 0.69 | 1.17 |
| 10-16 06:18 | +10 stop | BTC | UP | 0.69 | 0.54 | -1.83 |
| 10-16 06:18 | +5 | ETH | UP | 0.67 | 0.82 | 1.23 |
| 10-16 06:18 | +10 stop | HYPE | UP | 0.62 | 0.74 | 0.89 |
| 10-16 06:18 | +10 stop | DOGE | UP | 0.63 | 0.83 | 1.73 |
| 10-16 06:18 | +20 | DOGE | UP | 0.63 | 0.83 | 1.73 |
| 10-16 06:18 | +15 | DOGE | UP | 0.63 | 0.83 | 1.73 |
| 10-16 06:18 | +10 | DOGE | UP | 0.63 | 0.83 | 1.73 |
| 10-16 06:18 | +5 | DOGE | UP | 0.63 | 0.83 | 1.73 |
| 10-16 06:17 | +10 stop | BNB | UP | 0.62 | 0.44 | -2.15 |
| 10-16 06:17 | +20 | BNB | UP | 0.62 | 0.83 | 1.83 |
| 10-16 06:17 | +15 | BNB | UP | 0.62 | 0.80 | 1.51 |
| 10-16 06:17 | +10 | BNB | UP | 0.62 | 0.72 | 0.68 |
