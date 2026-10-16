# Range-Scalp Bot

*Updated Fri Oct 16 12:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19238 | 16713 | 2525 (29) | 0 | $-5823.82 | -4.8% |
| **+10¢** | 14507 | 11588 | 2919 (41) | 0 | $-5255.44 | -5.8% |
| **+15¢** | 12144 | 9001 | 3143 (60) | 0 | $-4776.82 | -6.3% |
| **+20¢** | 10774 | 7479 | 3295 (79) | 0 | $-4262.39 | -6.3% |
| **+10¢ (15¢ stop)** | 23661 | 23611 | 50 (29) | 0 | $-9112.90 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 12:46 | +10 stop | NEAR | DOWN | 0.55 | 0.67 | 0.86 |
| 10-16 12:46 | +20 | NEAR | DOWN | 0.55 | 0.79 | 2.10 |
| 10-16 12:46 | +15 | NEAR | DOWN | 0.55 | 0.79 | 2.10 |
| 10-16 12:46 | +10 | NEAR | DOWN | 0.55 | 0.67 | 0.86 |
| 10-16 12:46 | +5 | NEAR | DOWN | 0.54 | 0.67 | 0.96 |
| 10-16 12:46 | +10 stop | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-16 12:46 | +20 | BTC | DOWN | 0.66 | 0.87 | 1.86 |
| 10-16 12:46 | +15 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-16 12:46 | +10 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-16 12:46 | +5 | BTC | DOWN | 0.66 | 0.73 | 0.40 |
| 10-16 12:46 | +10 stop | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-16 12:46 | +20 | BNB | DOWN | 0.69 | 0.90 | 1.92 |
| 10-16 12:46 | +15 | BNB | DOWN | 0.69 | 0.85 | 1.36 |
| 10-16 12:46 | +10 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-16 12:46 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 10-16 12:42 | +10 stop | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 10-16 12:42 | +10 | XRP | DOWN | 0.69 | 0.86 | 1.46 |
| 10-16 12:42 | +5 | XRP | DOWN | 0.69 | 0.77 | 0.52 |
| 10-16 12:42 | +15 | DOGE | UP | 0.52 | no | -5.38 |
| 10-16 12:41 | +10 stop | BTC | DOWN | 0.70 | 0.93 | 2.10 |
| 10-16 12:41 | +20 | BTC | DOWN | 0.71 | 0.93 | 2.00 |
| 10-16 12:41 | +15 | BTC | DOWN | 0.71 | 0.93 | 2.00 |
| 10-16 12:41 | +10 | BTC | DOWN | 0.71 | 0.93 | 2.00 |
| 10-16 12:41 | +5 | BTC | DOWN | 0.71 | 0.93 | 2.00 |
| 10-16 12:41 | +10 stop | DOGE | UP | 0.58 | 0.19 | -4.19 |
| 10-16 12:41 | +5 | DOGE | UP | 0.58 | 0.67 | 0.56 |
| 10-16 12:41 | +10 stop | ETH | DOWN | 0.54 | 0.69 | 1.17 |
| 10-16 12:41 | +20 | ETH | DOWN | 0.54 | 0.94 | 3.75 |
| 10-16 12:41 | +15 | ETH | DOWN | 0.54 | 0.69 | 1.17 |
| 10-16 12:41 | +10 | ETH | DOWN | 0.54 | 0.69 | 1.17 |
| 10-16 12:41 | +10 stop | DOGE | UP | 0.43 | 0.62 | 1.55 |
| 10-16 12:41 | +5 | DOGE | UP | 0.43 | 0.62 | 1.55 |
| 10-16 12:40 | +10 stop | BTC | DOWN | 0.51 | 0.76 | 2.19 |
| 10-16 12:40 | +20 | BTC | DOWN | 0.51 | 0.76 | 2.19 |
| 10-16 12:40 | +15 | BTC | DOWN | 0.51 | 0.76 | 2.19 |
| 10-16 12:40 | +10 | BTC | DOWN | 0.51 | 0.76 | 2.19 |
| 10-16 12:40 | +5 | BTC | DOWN | 0.52 | 0.57 | 0.14 |
| 10-16 12:40 | +10 stop | BNB | DOWN | 0.59 | 0.80 | 1.81 |
| 10-16 12:39 | +5 | ZEC | DOWN | 0.66 | 0.79 | 1.02 |
| 10-16 12:38 | +10 stop | DOGE | DOWN | 0.67 | 0.47 | -2.34 |
