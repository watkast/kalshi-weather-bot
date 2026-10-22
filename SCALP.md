# Range-Scalp Bot

*Updated Thu Oct 22 06:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28460 | 24806 | 3654 (39) | 3 | $-8141.12 | -4.5% |
| **+10¢** | 21351 | 17121 | 4230 (55) | 4 | $-7252.71 | -5.4% |
| **+15¢** | 17875 | 13324 | 4551 (78) | 5 | $-6487.84 | -5.8% |
| **+20¢** | 15812 | 11038 | 4774 (98) | 6 | $-5878.92 | -5.9% |
| **+10¢ (15¢ stop)** | 34910 | 34851 | 59 (32) | 0 | $-13109.53 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 06:43 | +10 stop | DOGE | UP | 0.43 | 0.69 | 2.27 |
| 10-22 06:43 | +10 | DOGE | UP | 0.43 | 0.69 | 2.27 |
| 10-22 06:43 | +5 | DOGE | UP | 0.43 | 0.52 | 0.54 |
| 10-22 06:42 | +10 stop | NEAR | DOWN | 0.61 | 0.83 | 1.93 |
| 10-22 06:42 | +20 | NEAR | DOWN | 0.62 | 0.83 | 1.78 |
| 10-22 06:42 | +15 | NEAR | DOWN | 0.63 | 0.83 | 1.76 |
| 10-22 06:42 | +10 | NEAR | DOWN | 0.63 | 0.83 | 1.76 |
| 10-22 06:42 | +5 | NEAR | DOWN | 0.63 | 0.83 | 1.74 |
| 10-22 06:42 | +10 stop | DOGE | DOWN | 0.45 | 0.56 | 0.74 |
| 10-22 06:42 | +15 | DOGE | DOWN | 0.45 | open |  |
| 10-22 06:42 | +10 | DOGE | DOWN | 0.45 | 0.56 | 0.74 |
| 10-22 06:42 | +5 | DOGE | DOWN | 0.46 | 0.56 | 0.64 |
| 10-22 06:42 | +5 | XRP | UP | 0.28 | 0.56 | 2.47 |
| 10-22 06:41 | +10 stop | SOL | UP | 0.59 | 0.16 | -4.57 |
| 10-22 06:41 | +10 | SOL | UP | 0.59 | open |  |
| 10-22 06:41 | +10 stop | XRP | UP | 0.68 | 0.24 | -4.69 |
| 10-22 06:41 | +10 stop | BNB | DOWN | 0.65 | 0.86 | 1.85 |
| 10-22 06:40 | +10 stop | SOL | DOWN | 0.66 | 0.38 | -3.13 |
| 10-22 06:40 | +5 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 10-22 06:40 | +10 stop | XRP | DOWN | 0.63 | 0.42 | -2.42 |
| 10-22 06:40 | +10 stop | ZEC | UP | 0.64 | 0.76 | 0.90 |
| 10-22 06:40 | +20 | ZEC | UP | 0.64 | 0.88 | 2.15 |
| 10-22 06:40 | +15 | ZEC | UP | 0.64 | 0.81 | 1.42 |
| 10-22 06:40 | +10 | ZEC | UP | 0.64 | 0.76 | 0.90 |
| 10-22 06:40 | +5 | ZEC | UP | 0.64 | 0.73 | 0.59 |
| 10-22 06:40 | +10 stop | DOGE | UP | 0.52 | 0.64 | 0.85 |
| 10-22 06:40 | +10 | DOGE | UP | 0.52 | 0.64 | 0.85 |
| 10-22 06:40 | +5 | DOGE | UP | 0.52 | 0.64 | 0.85 |
| 10-22 06:39 | +10 | SOL | UP | 0.56 | 0.71 | 1.17 |
| 10-22 06:39 | +5 | SOL | UP | 0.55 | 0.64 | 0.55 |
| 10-22 06:39 | +5 | XRP | UP | 0.55 | 0.60 | 0.15 |
| 10-22 06:39 | +10 stop | BNB | UP | 0.30 | 0.59 | 2.58 |
| 10-22 06:38 | +10 stop | SOL | UP | 0.70 | 0.48 | -2.53 |
| 10-22 06:37 | +10 stop | NEAR | UP | 0.70 | 0.82 | 0.94 |
| 10-22 06:37 | +10 | NEAR | UP | 0.70 | 0.82 | 0.94 |
| 10-22 06:37 | +5 | NEAR | UP | 0.70 | 0.77 | 0.42 |
| 10-22 06:37 | +10 stop | XRP | UP | 0.65 | 0.37 | -3.13 |
| 10-22 06:37 | +10 stop | DOGE | UP | 0.64 | 0.80 | 1.31 |
| 10-22 06:36 | +10 stop | HYPE | UP | 0.65 | 0.80 | 1.22 |
| 10-22 06:35 | +10 stop | HYPE | DOWN | 0.70 | 0.54 | -1.93 |
