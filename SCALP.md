# Range-Scalp Bot

*Updated Fri Oct 09 00:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8200 | 7092 | 1108 (13) | 0 | $-2687.40 | -5.2% |
| **+10¢** | 6207 | 4896 | 1311 (25) | 1 | $-2660.52 | -6.8% |
| **+15¢** | 5230 | 3851 | 1379 (37) | 1 | $-2169.06 | -6.6% |
| **+20¢** | 4664 | 3232 | 1432 (45) | 1 | $-1778.28 | -6.1% |
| **+10¢ (15¢ stop)** | 9957 | 9927 | 30 (19) | 1 | $-3690.33 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 00:00 | +10 stop | BNB | DOWN | 0.48 | open |  |
| 10-09 00:00 | +20 | BNB | DOWN | 0.48 | open |  |
| 10-09 00:00 | +15 | BNB | DOWN | 0.48 | open |  |
| 10-09 00:00 | +10 | BNB | DOWN | 0.48 | open |  |
| 10-09 00:00 | +5 | BNB | DOWN | 0.48 | 0.58 | 0.60 |
| 10-08 23:56 | +15 | ZEC | DOWN | 0.67 | 0.87 | 1.76 |
| 10-08 23:56 | +10 | ZEC | DOWN | 0.64 | 0.76 | 0.92 |
| 10-08 23:56 | +5 | ZEC | DOWN | 0.64 | 0.73 | 0.55 |
| 10-08 23:54 | +10 stop | ZEC | DOWN | 0.55 | 0.71 | 1.27 |
| 10-08 23:54 | +20 | ZEC | DOWN | 0.55 | 0.77 | 1.89 |
| 10-08 23:54 | +15 | ZEC | DOWN | 0.55 | 0.71 | 1.27 |
| 10-08 23:54 | +10 | ZEC | DOWN | 0.55 | 0.71 | 1.27 |
| 10-08 23:54 | +5 | ZEC | DOWN | 0.55 | 0.71 | 1.27 |
| 10-08 23:53 | +10 stop | NEAR | DOWN | 0.65 | 0.78 | 0.98 |
| 10-08 23:50 | +10 stop | ETH | DOWN | 0.61 | 0.76 | 1.20 |
| 10-08 23:50 | +15 | ETH | DOWN | 0.61 | 0.76 | 1.20 |
| 10-08 23:50 | +10 | ETH | DOWN | 0.61 | 0.76 | 1.20 |
| 10-08 23:50 | +5 | ETH | DOWN | 0.61 | 0.67 | 0.27 |
| 10-08 23:50 | +10 stop | NEAR | UP | 0.50 | 0.32 | -2.14 |
| 10-08 23:49 | +5 | NEAR | UP | 0.57 | no | -5.88 |
| 10-08 23:49 | +10 stop | ZEC | UP | 0.67 | 0.78 | 0.81 |
| 10-08 23:49 | +15 | ZEC | UP | 0.67 | 0.83 | 1.34 |
| 10-08 23:49 | +10 | ZEC | UP | 0.67 | 0.78 | 0.81 |
| 10-08 23:49 | +5 | ZEC | UP | 0.67 | 0.73 | 0.30 |
| 10-08 23:49 | +10 stop | NEAR | UP | 0.70 | 0.54 | -1.93 |
| 10-08 23:48 | +10 stop | ZEC | UP | 0.68 | 0.79 | 0.82 |
| 10-08 23:48 | +10 | ZEC | UP | 0.68 | 0.79 | 0.82 |
| 10-08 23:48 | +5 | ZEC | UP | 0.68 | 0.79 | 0.82 |
| 10-08 23:48 | +10 stop | NEAR | UP | 0.46 | 0.59 | 0.95 |
| 10-08 23:46 | +10 stop | NEAR | DOWN | 0.55 | 0.37 | -2.12 |
| 10-08 23:46 | +5 | ZEC | UP | 0.66 | 0.71 | 0.19 |
| 10-08 23:46 | +10 stop | DOGE | DOWN | 0.67 | 0.86 | 1.65 |
| 10-08 23:46 | +20 | DOGE | DOWN | 0.68 | 0.88 | 1.76 |
| 10-08 23:46 | +15 | DOGE | DOWN | 0.68 | 0.86 | 1.55 |
| 10-08 23:46 | +10 | DOGE | DOWN | 0.68 | 0.86 | 1.55 |
| 10-08 23:46 | +5 | DOGE | DOWN | 0.68 | 0.73 | 0.20 |
| 10-08 23:46 | +10 stop | ETH | DOWN | 0.66 | 0.80 | 1.12 |
| 10-08 23:46 | +20 | ETH | DOWN | 0.66 | 0.86 | 1.75 |
| 10-08 23:46 | +15 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 10-08 23:46 | +10 | ETH | DOWN | 0.68 | 0.80 | 0.92 |
