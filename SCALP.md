# Range-Scalp Bot

*Updated Tue Oct 13 12:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14628 | 12650 | 1978 (27) | 0 | $-4726.80 | -5.1% |
| **+10¢** | 11074 | 8777 | 2297 (39) | 0 | $-4430.66 | -6.4% |
| **+15¢** | 9308 | 6849 | 2459 (57) | 0 | $-3960.12 | -6.8% |
| **+20¢** | 8281 | 5720 | 2561 (72) | 0 | $-3417.34 | -6.6% |
| **+10¢ (15¢ stop)** | 17962 | 17913 | 49 (29) | 0 | $-6984.22 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 12:27 | +10 stop | XRP | UP | 0.64 | 0.87 | 2.05 |
| 10-13 12:27 | +5 | NEAR | UP | 0.62 | 0.80 | 1.46 |
| 10-13 12:27 | +5 | SOL | UP | 0.54 | 0.92 | 3.57 |
| 10-13 12:26 | +10 stop | NEAR | UP | 0.53 | 0.80 | 2.40 |
| 10-13 12:26 | +10 | NEAR | UP | 0.53 | 0.80 | 2.40 |
| 10-13 12:26 | +5 | NEAR | UP | 0.54 | 0.62 | 0.45 |
| 10-13 12:26 | +10 stop | SOL | UP | 0.57 | 0.92 | 3.29 |
| 10-13 12:26 | +20 | SOL | UP | 0.57 | 0.92 | 3.30 |
| 10-13 12:26 | +15 | SOL | UP | 0.57 | 0.92 | 3.31 |
| 10-13 12:26 | +10 | SOL | UP | 0.57 | 0.92 | 3.28 |
| 10-13 12:26 | +5 | SOL | UP | 0.57 | 0.63 | 0.26 |
| 10-13 12:26 | +10 stop | NEAR | DOWN | 0.37 | 0.51 | 1.05 |
| 10-13 12:26 | +20 | NEAR | DOWN | 0.37 | yes | -3.87 |
| 10-13 12:26 | +15 | NEAR | DOWN | 0.37 | yes | -3.87 |
| 10-13 12:26 | +10 | NEAR | DOWN | 0.37 | 0.51 | 1.05 |
| 10-13 12:26 | +5 | NEAR | DOWN | 0.37 | 0.51 | 1.05 |
| 10-13 12:25 | +5 | XRP | UP | 0.70 | 0.87 | 1.47 |
| 10-13 12:25 | +10 stop | XRP | UP | 0.71 | 0.55 | -1.93 |
| 10-13 12:25 | +20 | XRP | UP | 0.71 | 0.91 | 1.81 |
| 10-13 12:25 | +15 | XRP | UP | 0.71 | 0.87 | 1.37 |
| 10-13 12:25 | +10 | XRP | UP | 0.71 | 0.87 | 1.37 |
| 10-13 12:24 | +10 stop | ETH | DOWN | 0.34 | 0.60 | 2.27 |
| 10-13 12:24 | +10 | ETH | DOWN | 0.34 | 0.60 | 2.27 |
| 10-13 12:24 | +5 | ETH | DOWN | 0.34 | 0.60 | 2.27 |
| 10-13 12:24 | +10 stop | BTC | DOWN | 0.56 | 0.31 | -2.83 |
| 10-13 12:24 | +20 | BTC | DOWN | 0.56 | yes | -5.78 |
| 10-13 12:24 | +15 | BTC | DOWN | 0.55 | yes | -5.68 |
| 10-13 12:24 | +10 | BTC | DOWN | 0.55 | yes | -5.68 |
| 10-13 12:24 | +5 | BTC | DOWN | 0.55 | 0.61 | 0.25 |
| 10-13 12:23 | +5 | DOGE | DOWN | 0.48 | 0.60 | 0.85 |
| 10-13 12:21 | +10 stop | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 10-13 12:21 | +15 | ZEC | DOWN | 0.68 | yes | -6.96 |
| 10-13 12:21 | +10 stop | DOGE | DOWN | 0.67 | 0.45 | -2.54 |
| 10-13 12:21 | +15 | DOGE | DOWN | 0.67 | yes | -6.86 |
| 10-13 12:21 | +10 | DOGE | DOWN | 0.67 | yes | -6.86 |
| 10-13 12:21 | +5 | DOGE | DOWN | 0.69 | 0.74 | 0.21 |
| 10-13 12:21 | +10 | ZEC | DOWN | 0.62 | 0.79 | 1.41 |
| 10-13 12:21 | +5 | ZEC | DOWN | 0.62 | 0.70 | 0.48 |
| 10-13 12:17 | +10 stop | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 10-13 12:17 | +20 | DOGE | DOWN | 0.65 | yes | -6.66 |
