# Range-Scalp Bot

*Updated Fri Oct 16 06:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18782 | 16311 | 2471 (28) | 1 | $-5723.52 | -4.8% |
| **+10¢** | 14156 | 11297 | 2859 (40) | 1 | $-5196.63 | -5.8% |
| **+15¢** | 11869 | 8791 | 3078 (59) | 1 | $-4712.60 | -6.3% |
| **+20¢** | 10542 | 7321 | 3221 (78) | 1 | $-4138.18 | -6.3% |
| **+10¢ (15¢ stop)** | 23128 | 23078 | 50 (29) | 0 | $-8927.12 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 06:31 | +10 stop | HYPE | UP | 0.66 | 0.78 | 0.91 |
| 10-16 06:31 | +20 | HYPE | UP | 0.66 | 0.88 | 1.96 |
| 10-16 06:31 | +15 | HYPE | UP | 0.66 | 0.81 | 1.23 |
| 10-16 06:31 | +10 | HYPE | UP | 0.66 | 0.78 | 0.91 |
| 10-16 06:31 | +5 | HYPE | UP | 0.66 | 0.71 | 0.19 |
| 10-16 06:31 | +10 stop | XRP | UP | 0.70 | 0.81 | 0.84 |
| 10-16 06:31 | +20 | XRP | UP | 0.70 | 0.93 | 2.12 |
| 10-16 06:31 | +15 | XRP | UP | 0.70 | 0.89 | 1.68 |
| 10-16 06:31 | +10 | XRP | UP | 0.70 | 0.81 | 0.84 |
| 10-16 06:31 | +5 | XRP | UP | 0.70 | 0.77 | 0.42 |
| 10-16 06:31 | +10 stop | DOGE | UP | 0.67 | 0.77 | 0.71 |
| 10-16 06:31 | +20 | DOGE | UP | 0.67 | 0.87 | 1.76 |
| 10-16 06:31 | +15 | DOGE | UP | 0.67 | 0.87 | 1.76 |
| 10-16 06:31 | +10 | DOGE | UP | 0.67 | 0.77 | 0.71 |
| 10-16 06:31 | +5 | DOGE | UP | 0.67 | 0.72 | 0.19 |
| 10-16 06:31 | +5 | NEAR | UP | 0.71 | 0.79 | 0.53 |
| 10-16 06:31 | +10 stop | SOL | UP | 0.71 | 0.81 | 0.78 |
| 10-16 06:31 | +20 | SOL | UP | 0.70 | 0.92 | 1.91 |
| 10-16 06:31 | +15 | SOL | UP | 0.70 | 0.86 | 1.32 |
| 10-16 06:31 | +10 | SOL | UP | 0.70 | 0.81 | 0.81 |
| 10-16 06:31 | +5 | SOL | UP | 0.70 | 0.80 | 0.70 |
| 10-16 06:31 | +10 stop | ZEC | DOWN | 0.56 | 0.35 | -2.44 |
| 10-16 06:31 | +20 | ZEC | DOWN | 0.56 | open |  |
| 10-16 06:31 | +15 | ZEC | DOWN | 0.56 | open |  |
| 10-16 06:31 | +10 | ZEC | DOWN | 0.56 | open |  |
| 10-16 06:31 | +5 | ZEC | DOWN | 0.56 | open |  |
| 10-16 06:28 | +10 stop | BNB | UP | 0.62 | 0.20 | -4.49 |
| 10-16 06:28 | +20 | BNB | UP | 0.62 | no | -6.37 |
| 10-16 06:28 | +15 | BNB | UP | 0.62 | no | -6.37 |
| 10-16 06:28 | +10 | BNB | UP | 0.62 | no | -6.37 |
| 10-16 06:28 | +5 | BNB | UP | 0.62 | no | -6.37 |
| 10-16 06:26 | +10 stop | BNB | UP | 0.65 | 0.80 | 1.22 |
| 10-16 06:26 | +10 | BNB | UP | 0.63 | 0.80 | 1.41 |
| 10-16 06:26 | +5 | BNB | UP | 0.63 | 0.68 | 0.17 |
| 10-16 06:24 | +10 stop | BNB | UP | 0.46 | 0.60 | 1.06 |
| 10-16 06:24 | +5 | BNB | UP | 0.46 | 0.60 | 1.06 |
| 10-16 06:23 | +10 stop | NEAR | DOWN | 0.69 | 0.52 | -2.02 |
| 10-16 06:23 | +10 | NEAR | DOWN | 0.69 | 0.79 | 0.74 |
| 10-16 06:23 | +5 | NEAR | DOWN | 0.69 | 0.74 | 0.22 |
| 10-16 06:23 | +10 stop | NEAR | UP | 0.47 | 0.57 | 0.68 |
