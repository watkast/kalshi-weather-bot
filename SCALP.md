# Range-Scalp Bot

*Updated Sat Oct 17 03:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20297 | 17653 | 2644 (29) | 2 | $-6018.16 | -4.7% |
| **+10¢** | 15295 | 12243 | 3052 (41) | 1 | $-5377.57 | -5.6% |
| **+15¢** | 12786 | 9503 | 3283 (60) | 0 | $-4859.74 | -6.1% |
| **+20¢** | 11337 | 7899 | 3438 (79) | 1 | $-4296.63 | -6.0% |
| **+10¢ (15¢ stop)** | 24957 | 24907 | 50 (29) | 0 | $-9467.41 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 03:22 | +10 stop | DOGE | UP | 0.49 | 0.69 | 1.68 |
| 10-17 03:22 | +5 | DOGE | UP | 0.49 | 0.54 | 0.15 |
| 10-17 03:21 | +10 stop | NEAR | UP | 0.64 | 0.77 | 1.00 |
| 10-17 03:20 | +10 stop | SOL | UP | 0.63 | 0.73 | 0.69 |
| 10-17 03:20 | +15 | SOL | UP | 0.64 | 0.81 | 1.42 |
| 10-17 03:20 | +10 | SOL | UP | 0.64 | 0.74 | 0.69 |
| 10-17 03:20 | +5 | SOL | UP | 0.64 | 0.73 | 0.59 |
| 10-17 03:20 | +10 stop | NEAR | DOWN | 0.61 | 0.46 | -1.85 |
| 10-17 03:20 | +10 | NEAR | DOWN | 0.61 | open |  |
| 10-17 03:20 | +5 | NEAR | DOWN | 0.61 | open |  |
| 10-17 03:19 | +10 stop | XRP | DOWN | 0.62 | 0.31 | -3.42 |
| 10-17 03:18 | +10 stop | BTC | DOWN | 0.62 | 0.41 | -2.44 |
| 10-17 03:18 | +10 stop | DOGE | DOWN | 0.67 | 0.46 | -2.44 |
| 10-17 03:18 | +10 stop | XRP | DOWN | 0.70 | 0.55 | -1.83 |
| 10-17 03:18 | +5 | XRP | DOWN | 0.71 | open |  |
| 10-17 03:17 | +5 | BNB | UP | 0.64 | 0.69 | 0.23 |
| 10-17 03:17 | +10 stop | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 10-17 03:17 | +10 | NEAR | DOWN | 0.63 | 0.74 | 0.81 |
| 10-17 03:17 | +5 | NEAR | DOWN | 0.63 | 0.71 | 0.50 |
| 10-17 03:17 | +5 | XRP | UP | 0.39 | 0.56 | 1.35 |
| 10-17 03:17 | +10 stop | SOL | DOWN | 0.57 | 0.72 | 1.17 |
| 10-17 03:17 | +20 | SOL | DOWN | 0.57 | open |  |
| 10-17 03:17 | +15 | SOL | DOWN | 0.57 | 0.72 | 1.17 |
| 10-17 03:17 | +10 | SOL | DOWN | 0.57 | 0.72 | 1.17 |
| 10-17 03:17 | +5 | SOL | DOWN | 0.57 | 0.64 | 0.35 |
| 10-17 03:17 | +5 | HYPE | UP | 0.69 | 0.76 | 0.38 |
| 10-17 03:16 | +10 stop | BTC | UP | 0.54 | 0.38 | -1.95 |
| 10-17 03:16 | +20 | BTC | UP | 0.54 | 0.74 | 1.68 |
| 10-17 03:16 | +15 | BTC | UP | 0.54 | 0.74 | 1.68 |
| 10-17 03:16 | +10 | BTC | UP | 0.54 | 0.68 | 1.06 |
| 10-17 03:16 | +5 | BTC | UP | 0.54 | 0.68 | 1.06 |
| 10-17 03:16 | +10 stop | XRP | UP | 0.51 | 0.33 | -2.14 |
| 10-17 03:16 | +20 | XRP | UP | 0.51 | 0.80 | 2.60 |
| 10-17 03:16 | +15 | XRP | UP | 0.51 | 0.68 | 1.36 |
| 10-17 03:16 | +10 | XRP | UP | 0.51 | 0.68 | 1.36 |
| 10-17 03:16 | +5 | XRP | UP | 0.51 | 0.56 | 0.14 |
| 10-17 03:16 | +5 | ZEC | UP | 0.63 | 0.71 | 0.48 |
| 10-17 03:16 | +5 | ETH | UP | 0.66 | 0.74 | 0.50 |
| 10-17 03:16 | +10 stop | NEAR | UP | 0.51 | 0.62 | 0.75 |
| 10-17 03:16 | +20 | NEAR | UP | 0.51 | 0.77 | 2.29 |
