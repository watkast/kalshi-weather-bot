# Range-Scalp Bot

*Updated Tue Nov 03 06:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45679 | 39775 | 5904 (69) | 2 | $-13171.32 | -4.6% |
| **+10¢** | 34098 | 27255 | 6843 (91) | 2 | $-12070.75 | -5.6% |
| **+15¢** | 28538 | 21176 | 7362 (119) | 2 | $-11057.34 | -6.2% |
| **+20¢** | 25345 | 17631 | 7714 (154) | 3 | $-9840.44 | -6.2% |
| **+10¢ (15¢ stop)** | 55729 | 55640 | 89 (53) | 2 | $-20977.97 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 06:21 | +10 stop | SOL | UP | 0.58 | 0.79 | 1.80 |
| 11-03 06:20 | +10 stop | ZEC | DOWN | 0.61 | open |  |
| 11-03 06:20 | +10 stop | NEAR | DOWN | 0.60 | open |  |
| 11-03 06:20 | +10 stop | DOGE | UP | 0.64 | 0.78 | 1.10 |
| 11-03 06:20 | +20 | DOGE | UP | 0.64 | 0.85 | 1.84 |
| 11-03 06:20 | +15 | DOGE | UP | 0.64 | 0.81 | 1.42 |
| 11-03 06:20 | +10 | DOGE | UP | 0.64 | 0.78 | 1.10 |
| 11-03 06:20 | +5 | DOGE | UP | 0.64 | 0.69 | 0.18 |
| 11-03 06:20 | +10 stop | SOL | DOWN | 0.60 | 0.42 | -2.15 |
| 11-03 06:19 | +15 | SOL | UP | 0.57 | 0.79 | 1.90 |
| 11-03 06:19 | +5 | NEAR | UP | 0.63 | open |  |
| 11-03 06:18 | +5 | ZEC | UP | 0.68 | open |  |
| 11-03 06:17 | +10 stop | SOL | UP | 0.66 | 0.49 | -2.04 |
| 11-03 06:17 | +10 | SOL | UP | 0.66 | 0.79 | 1.02 |
| 11-03 06:17 | +5 | SOL | UP | 0.68 | 0.79 | 0.82 |
| 11-03 06:16 | +10 stop | ZEC | UP | 0.59 | 0.39 | -2.34 |
| 11-03 06:16 | +20 | ZEC | UP | 0.59 | open |  |
| 11-03 06:16 | +15 | ZEC | UP | 0.59 | open |  |
| 11-03 06:16 | +10 | ZEC | UP | 0.59 | open |  |
| 11-03 06:16 | +5 | ZEC | UP | 0.58 | 0.64 | 0.25 |
| 11-03 06:16 | +10 stop | SOL | UP | 0.56 | 0.67 | 0.76 |
| 11-03 06:16 | +20 | SOL | UP | 0.56 | 0.79 | 2.00 |
| 11-03 06:16 | +15 | SOL | UP | 0.56 | 0.71 | 1.17 |
| 11-03 06:16 | +10 | SOL | UP | 0.56 | 0.67 | 0.76 |
| 11-03 06:16 | +5 | SOL | UP | 0.56 | 0.63 | 0.35 |
| 11-03 06:16 | +10 stop | NEAR | UP | 0.67 | 0.43 | -2.74 |
| 11-03 06:16 | +20 | NEAR | UP | 0.67 | open |  |
| 11-03 06:16 | +15 | NEAR | UP | 0.67 | open |  |
| 11-03 06:16 | +10 | NEAR | UP | 0.67 | open |  |
| 11-03 06:16 | +5 | NEAR | UP | 0.67 | 0.73 | 0.30 |
| 11-03 06:16 | +10 stop | XRP | UP | 0.69 | 0.83 | 1.15 |
| 11-03 06:16 | +20 | XRP | UP | 0.69 | open |  |
| 11-03 06:16 | +15 | XRP | UP | 0.69 | 0.84 | 1.25 |
| 11-03 06:16 | +10 | XRP | UP | 0.69 | 0.83 | 1.15 |
| 11-03 06:16 | +5 | XRP | UP | 0.69 | 0.75 | 0.31 |
| 11-03 06:11 | +15 | HYPE | UP | 0.70 | no | -7.15 |
| 11-03 06:11 | +10 | HYPE | UP | 0.70 | no | -7.15 |
| 11-03 06:11 | +5 | HYPE | UP | 0.71 | no | -7.25 |
| 11-03 06:11 | +10 stop | HYPE | UP | 0.70 | 0.26 | -4.73 |
| 11-03 06:11 | +5 | ZEC | DOWN | 0.68 | 0.86 | 1.55 |
