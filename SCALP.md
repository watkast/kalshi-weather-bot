# Range-Scalp Bot

*Updated Sun Oct 18 07:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22197 | 19321 | 2876 (29) | 0 | $-6476.21 | -4.6% |
| **+10¢** | 16715 | 13394 | 3321 (42) | 0 | $-5747.66 | -5.5% |
| **+15¢** | 14002 | 10419 | 3583 (62) | 1 | $-5243.80 | -6.0% |
| **+20¢** | 12388 | 8634 | 3754 (80) | 3 | $-4705.67 | -6.1% |
| **+10¢ (15¢ stop)** | 27306 | 27256 | 50 (29) | 0 | $-10422.61 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 07:17 | +5 | SOL | DOWN | 0.68 | 0.74 | 0.30 |
| 10-18 07:17 | +10 stop | NEAR | DOWN | 0.60 | 0.72 | 0.88 |
| 10-18 07:17 | +20 | NEAR | DOWN | 0.60 | open |  |
| 10-18 07:17 | +15 | NEAR | DOWN | 0.60 | 0.75 | 1.19 |
| 10-18 07:17 | +10 | NEAR | DOWN | 0.60 | 0.72 | 0.88 |
| 10-18 07:17 | +5 | NEAR | DOWN | 0.60 | 0.72 | 0.88 |
| 10-18 07:17 | +10 stop | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-18 07:17 | +20 | ZEC | DOWN | 0.65 | open |  |
| 10-18 07:17 | +15 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-18 07:17 | +10 | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-18 07:17 | +5 | ZEC | DOWN | 0.65 | 0.74 | 0.60 |
| 10-18 07:16 | +10 stop | SOL | DOWN | 0.61 | 0.74 | 0.99 |
| 10-18 07:16 | +20 | SOL | DOWN | 0.61 | open |  |
| 10-18 07:16 | +15 | SOL | DOWN | 0.61 | open |  |
| 10-18 07:16 | +10 | SOL | DOWN | 0.62 | 0.74 | 0.89 |
| 10-18 07:16 | +5 | SOL | DOWN | 0.62 | 0.67 | 0.17 |
| 10-18 07:14 | +15 | ETH | UP | 0.70 | no | -7.15 |
| 10-18 07:13 | +5 | SOL | UP | 0.61 | 0.73 | 0.89 |
| 10-18 07:13 | +10 stop | SOL | UP | 0.68 | 0.36 | -3.53 |
| 10-18 07:13 | +20 | SOL | UP | 0.68 | no | -6.96 |
| 10-18 07:13 | +15 | SOL | UP | 0.66 | no | -6.76 |
| 10-18 07:13 | +10 | SOL | UP | 0.61 | 0.73 | 0.89 |
| 10-18 07:12 | +10 stop | DOGE | UP | 0.63 | 0.29 | -3.72 |
| 10-18 07:12 | +10 stop | DOGE | DOWN | 0.40 | 0.60 | 1.64 |
| 10-18 07:11 | +10 stop | DOGE | UP | 0.31 | 0.57 | 2.27 |
| 10-18 07:07 | +10 stop | XRP | UP | 0.50 | 0.66 | 1.26 |
| 10-18 07:07 | +20 | XRP | UP | 0.50 | 0.82 | 2.91 |
| 10-18 07:07 | +15 | XRP | UP | 0.50 | 0.66 | 1.26 |
| 10-18 07:07 | +10 | XRP | UP | 0.50 | 0.66 | 1.26 |
| 10-18 07:07 | +5 | XRP | UP | 0.50 | 0.66 | 1.26 |
| 10-18 07:07 | +10 stop | ETH | UP | 0.52 | 0.68 | 1.26 |
| 10-18 07:07 | +15 | ETH | UP | 0.52 | 0.68 | 1.26 |
| 10-18 07:07 | +10 | ETH | UP | 0.52 | 0.68 | 1.26 |
| 10-18 07:07 | +5 | ETH | UP | 0.52 | 0.68 | 1.26 |
| 10-18 07:06 | +10 stop | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-18 07:05 | +10 stop | DOGE | UP | 0.62 | 0.46 | -1.95 |
| 10-18 07:05 | +20 | DOGE | UP | 0.62 | no | -6.37 |
| 10-18 07:05 | +15 | DOGE | UP | 0.62 | no | -6.37 |
| 10-18 07:05 | +10 | DOGE | UP | 0.62 | no | -6.37 |
| 10-18 07:05 | +5 | DOGE | UP | 0.62 | no | -6.37 |
