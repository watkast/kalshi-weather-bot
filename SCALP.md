# Range-Scalp Bot

*Updated Tue Oct 06 09:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4854 | 4198 | 656 (7) | 1 | $-1541.60 | -5.0% |
| **+10¢** | 3730 | 2965 | 765 (11) | 1 | $-1429.43 | -6.1% |
| **+15¢** | 3134 | 2324 | 810 (14) | 1 | $-1231.09 | -6.3% |
| **+20¢** | 2807 | 1962 | 845 (19) | 1 | $-1017.37 | -5.8% |
| **+10¢ (15¢ stop)** | 5944 | 5931 | 13 (8) | 0 | $-2119.85 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 09:21 | +10 stop | NEAR | DOWN | 0.50 | 0.60 | 0.66 |
| 10-06 09:19 | +10 stop | NEAR | DOWN | 0.63 | 0.82 | 1.63 |
| 10-06 09:18 | +10 stop | NEAR | DOWN | 0.70 | 0.54 | -1.93 |
| 10-06 09:18 | +10 stop | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 10-06 09:18 | +20 | DOGE | UP | 0.63 | 0.83 | 1.73 |
| 10-06 09:18 | +15 | DOGE | UP | 0.63 | 0.79 | 1.31 |
| 10-06 09:18 | +10 | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 10-06 09:18 | +5 | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 10-06 09:18 | +10 stop | HYPE | UP | 0.64 | 0.76 | 0.87 |
| 10-06 09:18 | +20 | HYPE | UP | 0.64 | 0.88 | 2.12 |
| 10-06 09:18 | +15 | HYPE | UP | 0.64 | 0.82 | 1.49 |
| 10-06 09:18 | +10 | HYPE | UP | 0.64 | 0.76 | 0.87 |
| 10-06 09:18 | +5 | HYPE | UP | 0.64 | 0.73 | 0.56 |
| 10-06 09:17 | +5 | SOL | UP | 0.63 | 0.74 | 0.79 |
| 10-06 09:17 | +10 stop | NEAR | UP | 0.62 | 0.46 | -1.94 |
| 10-06 09:17 | +20 | NEAR | UP | 0.62 | open |  |
| 10-06 09:17 | +15 | NEAR | UP | 0.62 | open |  |
| 10-06 09:17 | +10 | NEAR | UP | 0.62 | open |  |
| 10-06 09:17 | +5 | NEAR | UP | 0.62 | open |  |
| 10-06 09:16 | +10 stop | SOL | UP | 0.65 | 0.75 | 0.70 |
| 10-06 09:16 | +20 | SOL | UP | 0.65 | 0.85 | 1.75 |
| 10-06 09:16 | +15 | SOL | UP | 0.65 | 0.84 | 1.64 |
| 10-06 09:16 | +10 | SOL | UP | 0.65 | 0.75 | 0.70 |
| 10-06 09:16 | +5 | SOL | UP | 0.65 | 0.70 | 0.19 |
| 10-06 09:15 | +10 stop | BNB | UP | 0.70 | 0.84 | 1.15 |
| 10-06 09:15 | +20 | BNB | UP | 0.70 | 0.90 | 1.81 |
| 10-06 09:15 | +15 | BNB | UP | 0.70 | 0.86 | 1.36 |
| 10-06 09:15 | +10 | BNB | UP | 0.70 | 0.84 | 1.15 |
| 10-06 09:15 | +5 | BNB | UP | 0.70 | 0.79 | 0.63 |
| 10-06 09:15 | +10 stop | XRP | UP | 0.69 | 0.79 | 0.73 |
| 10-06 09:15 | +20 | XRP | UP | 0.69 | 0.95 | 2.37 |
| 10-06 09:15 | +15 | XRP | UP | 0.69 | 0.85 | 1.36 |
| 10-06 09:15 | +10 | XRP | UP | 0.69 | 0.79 | 0.73 |
| 10-06 09:15 | +5 | XRP | UP | 0.69 | 0.78 | 0.62 |
| 10-06 09:11 | +10 stop | DOGE | DOWN | 0.37 | 0.62 | 2.19 |
| 10-06 09:11 | +15 | DOGE | DOWN | 0.37 | 0.62 | 2.19 |
| 10-06 09:11 | +10 | DOGE | DOWN | 0.37 | 0.62 | 2.19 |
| 10-06 09:11 | +5 | DOGE | DOWN | 0.36 | 0.62 | 2.26 |
| 10-06 09:10 | +10 stop | XRP | UP | 0.70 | 0.92 | 2.00 |
| 10-06 09:10 | +20 | XRP | UP | 0.70 | 0.92 | 2.00 |
