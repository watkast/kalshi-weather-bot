# Range-Scalp Bot

*Updated Fri Oct 23 06:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29841 | 25976 | 3865 (39) | 0 | $-8806.37 | -4.7% |
| **+10¢** | 22371 | 17897 | 4474 (55) | 0 | $-7921.56 | -5.6% |
| **+15¢** | 18739 | 13934 | 4805 (78) | 0 | $-7092.76 | -6.0% |
| **+20¢** | 16586 | 11552 | 5034 (101) | 2 | $-6396.94 | -6.1% |
| **+10¢ (15¢ stop)** | 36633 | 36574 | 59 (32) | 0 | $-13808.45 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 06:00 | +10 stop | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-23 06:00 | +20 | ZEC | DOWN | 0.71 | open |  |
| 10-23 06:00 | +15 | ZEC | DOWN | 0.71 | 0.86 | 1.26 |
| 10-23 06:00 | +10 | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-23 06:00 | +5 | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-23 06:00 | +10 stop | SOL | DOWN | 0.67 | 0.81 | 1.09 |
| 10-23 06:00 | +20 | SOL | DOWN | 0.67 | 0.89 | 1.93 |
| 10-23 06:00 | +15 | SOL | DOWN | 0.67 | 0.83 | 1.30 |
| 10-23 06:00 | +10 | SOL | DOWN | 0.67 | 0.81 | 1.09 |
| 10-23 06:00 | +5 | SOL | DOWN | 0.67 | 0.76 | 0.57 |
| 10-23 06:00 | +10 stop | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 10-23 06:00 | +20 | NEAR | DOWN | 0.68 | open |  |
| 10-23 06:00 | +15 | NEAR | DOWN | 0.67 | 0.83 | 1.30 |
| 10-23 06:00 | +10 | NEAR | DOWN | 0.67 | 0.79 | 0.88 |
| 10-23 06:00 | +5 | NEAR | DOWN | 0.67 | 0.79 | 0.88 |
| 10-23 06:00 | +10 stop | BNB | DOWN | 0.70 | 0.84 | 1.16 |
| 10-23 06:00 | +20 | BNB | DOWN | 0.70 | 0.90 | 1.82 |
| 10-23 06:00 | +15 | BNB | DOWN | 0.70 | 0.87 | 1.48 |
| 10-23 06:00 | +10 | BNB | DOWN | 0.70 | 0.84 | 1.16 |
| 10-23 06:00 | +5 | BNB | DOWN | 0.69 | 0.76 | 0.42 |
| 10-23 05:57 | +10 stop | SOL | UP | 0.62 | 0.87 | 2.25 |
| 10-23 05:56 | +10 stop | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-23 05:56 | +10 stop | SOL | DOWN | 0.59 | 0.36 | -2.64 |
| 10-23 05:55 | +5 | NEAR | DOWN | 0.65 | 0.75 | 0.69 |
| 10-23 05:55 | +10 stop | SOL | UP | 0.52 | 0.62 | 0.65 |
| 10-23 05:55 | +10 stop | DOGE | UP | 0.62 | 0.45 | -2.05 |
| 10-23 05:55 | +10 stop | NEAR | UP | 0.43 | 0.25 | -2.12 |
| 10-23 05:55 | +20 | NEAR | UP | 0.43 | no | -4.48 |
| 10-23 05:55 | +15 | NEAR | UP | 0.43 | no | -4.48 |
| 10-23 05:55 | +10 | NEAR | UP | 0.43 | no | -4.48 |
| 10-23 05:55 | +5 | NEAR | UP | 0.43 | 0.50 | 0.34 |
| 10-23 05:54 | +10 stop | XRP | DOWN | 0.69 | 0.85 | 1.36 |
| 10-23 05:54 | +10 | XRP | DOWN | 0.69 | 0.85 | 1.36 |
| 10-23 05:54 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 10-23 05:54 | +5 | SOL | DOWN | 0.66 | yes | -6.76 |
| 10-23 05:54 | +10 stop | DOGE | UP | 0.69 | 0.51 | -2.13 |
| 10-23 05:54 | +20 | DOGE | UP | 0.69 | no | -7.05 |
| 10-23 05:54 | +15 | DOGE | UP | 0.69 | no | -7.05 |
| 10-23 05:54 | +10 | DOGE | UP | 0.69 | no | -7.05 |
| 10-23 05:54 | +5 | DOGE | UP | 0.69 | no | -7.05 |
