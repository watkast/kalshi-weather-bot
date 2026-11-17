# Range-Scalp Bot

*Updated Tue Nov 17 14:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62863 | 54832 | 8031 (117) | 0 | $-17123.63 | -4.3% |
| **+10¢** | 46950 | 37553 | 9397 (159) | 0 | $-16003.50 | -5.4% |
| **+15¢** | 39354 | 29219 | 10135 (201) | 0 | $-14549.72 | -5.9% |
| **+20¢** | 35069 | 24442 | 10627 (256) | 1 | $-12723.37 | -5.8% |
| **+10¢ (15¢ stop)** | 76497 | 76341 | 156 (92) | 0 | $-28185.67 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 14:13 | +10 stop | NEAR | DOWN | 0.63 | 0.47 | -1.95 |
| 11-17 14:13 | +10 stop | ZEC | UP | 0.57 | 0.83 | 2.32 |
| 11-17 14:12 | +10 stop | NEAR | DOWN | 0.38 | 0.56 | 1.45 |
| 11-17 14:12 | +20 | NEAR | DOWN | 0.54 | 0.91 | 3.43 |
| 11-17 14:12 | +15 | NEAR | DOWN | 0.54 | 0.70 | 1.27 |
| 11-17 14:12 | +10 | NEAR | DOWN | 0.54 | 0.70 | 1.27 |
| 11-17 14:12 | +5 | NEAR | DOWN | 0.54 | 0.70 | 1.27 |
| 11-17 14:12 | +10 stop | HYPE | UP | 0.67 | 0.80 | 1.02 |
| 11-17 14:12 | +15 | HYPE | UP | 0.67 | 0.90 | 2.11 |
| 11-17 14:12 | +10 | HYPE | UP | 0.67 | 0.80 | 1.02 |
| 11-17 14:12 | +5 | HYPE | UP | 0.67 | 0.80 | 1.02 |
| 11-17 14:12 | +10 stop | BNB | DOWN | 0.69 | 0.41 | -3.12 |
| 11-17 14:12 | +20 | BNB | DOWN | 0.69 | 0.95 | 2.46 |
| 11-17 14:12 | +15 | BNB | DOWN | 0.69 | 0.95 | 2.46 |
| 11-17 14:12 | +10 | BNB | DOWN | 0.69 | 0.95 | 2.46 |
| 11-17 14:12 | +5 | BNB | DOWN | 0.69 | 0.95 | 2.46 |
| 11-17 14:12 | +10 stop | ZEC | DOWN | 0.62 | 0.45 | -2.05 |
| 11-17 14:12 | +20 | ZEC | DOWN | 0.62 | 0.99 | 3.52 |
| 11-17 14:12 | +15 | ZEC | DOWN | 0.62 | 0.99 | 3.52 |
| 11-17 14:12 | +10 | ZEC | DOWN | 0.62 | 0.75 | 0.99 |
| 11-17 14:12 | +5 | ZEC | DOWN | 0.62 | 0.75 | 0.99 |
| 11-17 14:11 | +10 stop | HYPE | DOWN | 0.45 | 0.59 | 1.05 |
| 11-17 14:11 | +20 | HYPE | DOWN | 0.45 | open |  |
| 11-17 14:11 | +15 | HYPE | DOWN | 0.44 | 0.59 | 1.15 |
| 11-17 14:11 | +10 | HYPE | DOWN | 0.44 | 0.59 | 1.15 |
| 11-17 14:11 | +5 | HYPE | DOWN | 0.44 | 0.59 | 1.15 |
| 11-17 14:11 | +10 stop | DOGE | UP | 0.68 | 0.53 | -1.84 |
| 11-17 14:11 | +15 | DOGE | UP | 0.68 | 0.83 | 1.24 |
| 11-17 14:11 | +10 | DOGE | UP | 0.68 | 0.83 | 1.24 |
| 11-17 14:11 | +5 | DOGE | UP | 0.68 | 0.83 | 1.24 |
| 11-17 14:10 | +10 stop | SOL | UP | 0.71 | 0.81 | 0.74 |
| 11-17 14:10 | +20 | SOL | UP | 0.71 | 0.94 | 2.13 |
| 11-17 14:10 | +15 | SOL | UP | 0.71 | 0.91 | 1.75 |
| 11-17 14:10 | +10 | SOL | UP | 0.71 | 0.81 | 0.74 |
| 11-17 14:10 | +5 | SOL | UP | 0.71 | 0.76 | 0.22 |
| 11-17 14:09 | +10 stop | DOGE | UP | 0.60 | 0.70 | 0.68 |
| 11-17 14:09 | +20 | DOGE | UP | 0.60 | 0.83 | 2.03 |
| 11-17 14:09 | +15 | DOGE | UP | 0.61 | 0.76 | 1.20 |
| 11-17 14:09 | +10 | DOGE | UP | 0.58 | 0.70 | 0.87 |
| 11-17 14:09 | +5 | DOGE | UP | 0.58 | 0.70 | 0.87 |
