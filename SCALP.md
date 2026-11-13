# Range-Scalp Bot

*Updated Fri Nov 13 07:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57969 | 50573 | 7396 (102) | 2 | $-15701.38 | -4.3% |
| **+10¢** | 43307 | 34664 | 8643 (134) | 3 | $-14665.08 | -5.4% |
| **+15¢** | 36304 | 26999 | 9305 (168) | 3 | $-13227.22 | -5.8% |
| **+20¢** | 32341 | 22573 | 9768 (219) | 3 | $-11611.29 | -5.7% |
| **+10¢ (15¢ stop)** | 70640 | 70511 | 129 (79) | 1 | $-25993.29 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 07:41 | +5 | NEAR | DOWN | 0.58 | open |  |
| 11-13 07:40 | +10 stop | NEAR | DOWN | 0.57 | open |  |
| 11-13 07:40 | +5 | NEAR | DOWN | 0.57 | 0.65 | 0.46 |
| 11-13 07:40 | +10 stop | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 11-13 07:40 | +20 | HYPE | UP | 0.66 | 0.94 | 2.67 |
| 11-13 07:40 | +15 | HYPE | UP | 0.65 | 0.82 | 1.43 |
| 11-13 07:40 | +10 | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 11-13 07:40 | +5 | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 11-13 07:38 | +10 stop | DOGE | UP | 0.59 | 0.22 | -4.05 |
| 11-13 07:37 | +10 stop | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 11-13 07:37 | +10 stop | NEAR | UP | 0.62 | 0.47 | -1.85 |
| 11-13 07:37 | +15 | NEAR | UP | 0.62 | open |  |
| 11-13 07:37 | +10 | NEAR | UP | 0.62 | open |  |
| 11-13 07:34 | +10 stop | DOGE | DOWN | 0.63 | 0.47 | -1.95 |
| 11-13 07:34 | +10 | DOGE | DOWN | 0.63 | 0.76 | 1.00 |
| 11-13 07:34 | +5 | DOGE | DOWN | 0.63 | 0.76 | 1.00 |
| 11-13 07:34 | +10 stop | ETH | DOWN | 0.65 | 0.79 | 1.12 |
| 11-13 07:34 | +10 stop | SOL | DOWN | 0.65 | 0.81 | 1.33 |
| 11-13 07:34 | +5 | SOL | DOWN | 0.65 | 0.71 | 0.29 |
| 11-13 07:34 | +10 stop | XRP | DOWN | 0.67 | 0.79 | 0.92 |
| 11-13 07:34 | +10 | XRP | DOWN | 0.67 | 0.79 | 0.92 |
| 11-13 07:34 | +5 | XRP | DOWN | 0.67 | 0.79 | 0.92 |
| 11-13 07:34 | +5 | HYPE | UP | 0.54 | 0.64 | 0.65 |
| 11-13 07:34 | +5 | NEAR | DOWN | 0.65 | 0.70 | 0.19 |
| 11-13 07:33 | +5 | HYPE | DOWN | 0.53 | 0.58 | 0.14 |
| 11-13 07:32 | +5 | SOL | DOWN | 0.58 | 0.64 | 0.25 |
| 11-13 07:31 | +10 stop | XRP | DOWN | 0.67 | 0.77 | 0.71 |
| 11-13 07:31 | +20 | XRP | DOWN | 0.67 | 0.93 | 2.34 |
| 11-13 07:31 | +15 | XRP | DOWN | 0.67 | 0.82 | 1.23 |
| 11-13 07:31 | +10 | XRP | DOWN | 0.67 | 0.77 | 0.71 |
| 11-13 07:31 | +5 | XRP | DOWN | 0.67 | 0.74 | 0.40 |
| 11-13 07:31 | +5 | NEAR | DOWN | 0.61 | 0.66 | 0.17 |
| 11-13 07:31 | +10 stop | DOGE | DOWN | 0.68 | 0.80 | 0.88 |
| 11-13 07:31 | +20 | DOGE | DOWN | 0.67 | 0.90 | 2.07 |
| 11-13 07:31 | +15 | DOGE | DOWN | 0.66 | 0.90 | 2.17 |
| 11-13 07:31 | +10 | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 11-13 07:31 | +5 | DOGE | DOWN | 0.66 | 0.72 | 0.29 |
| 11-13 07:31 | +10 stop | ZEC | DOWN | 0.60 | 0.76 | 1.30 |
| 11-13 07:31 | +20 | ZEC | DOWN | 0.60 | 0.80 | 1.71 |
| 11-13 07:31 | +15 | ZEC | DOWN | 0.60 | 0.76 | 1.30 |
