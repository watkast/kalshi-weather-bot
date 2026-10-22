# Range-Scalp Bot

*Updated Thu Oct 22 02:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28093 | 24479 | 3614 (39) | 0 | $-8071.21 | -4.6% |
| **+10¢** | 21105 | 16929 | 4176 (55) | 2 | $-7120.05 | -5.4% |
| **+15¢** | 17680 | 13188 | 4492 (78) | 2 | $-6331.90 | -5.7% |
| **+20¢** | 15647 | 10939 | 4708 (98) | 2 | $-5674.41 | -5.8% |
| **+10¢ (15¢ stop)** | 34492 | 34433 | 59 (32) | 0 | $-12895.48 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 02:13 | +10 stop | NEAR | DOWN | 0.71 | 0.53 | -2.13 |
| 10-22 02:13 | +15 | NEAR | DOWN | 0.70 | open |  |
| 10-22 02:13 | +10 | NEAR | DOWN | 0.70 | open |  |
| 10-22 02:13 | +5 | NEAR | DOWN | 0.70 | 0.79 | 0.63 |
| 10-22 02:12 | +10 stop | NEAR | UP | 0.48 | 0.66 | 1.46 |
| 10-22 02:12 | +20 | NEAR | UP | 0.48 | 0.69 | 1.77 |
| 10-22 02:12 | +15 | NEAR | UP | 0.48 | 0.66 | 1.46 |
| 10-22 02:12 | +10 | NEAR | UP | 0.48 | 0.66 | 1.46 |
| 10-22 02:12 | +5 | NEAR | UP | 0.48 | 0.66 | 1.46 |
| 10-22 02:11 | +15 | SOL | DOWN | 0.59 | 0.86 | 2.44 |
| 10-22 02:10 | +10 stop | SOL | DOWN | 0.61 | 0.44 | -2.02 |
| 10-22 02:10 | +10 | SOL | DOWN | 0.70 | 0.86 | 1.36 |
| 10-22 02:10 | +5 | SOL | DOWN | 0.71 | 0.86 | 1.26 |
| 10-22 02:10 | +10 stop | BNB | UP | 0.55 | 0.65 | 0.66 |
| 10-22 02:10 | +10 stop | ZEC | UP | 0.71 | 0.85 | 1.16 |
| 10-22 02:10 | +10 | ZEC | UP | 0.71 | 0.85 | 1.16 |
| 10-22 02:10 | +5 | ZEC | UP | 0.71 | 0.77 | 0.32 |
| 10-22 02:10 | +10 stop | NEAR | UP | 0.68 | 0.78 | 0.71 |
| 10-22 02:09 | +10 stop | SOL | DOWN | 0.47 | 0.57 | 0.64 |
| 10-22 02:09 | +20 | SOL | DOWN | 0.47 | 0.69 | 1.87 |
| 10-22 02:09 | +15 | SOL | DOWN | 0.47 | 0.64 | 1.35 |
| 10-22 02:09 | +10 | SOL | DOWN | 0.46 | 0.56 | 0.64 |
| 10-22 02:09 | +5 | SOL | DOWN | 0.46 | 0.54 | 0.44 |
| 10-22 02:09 | +10 stop | XRP | DOWN | 0.59 | 0.79 | 1.71 |
| 10-22 02:09 | +20 | XRP | DOWN | 0.59 | 0.79 | 1.71 |
| 10-22 02:09 | +15 | XRP | DOWN | 0.59 | 0.79 | 1.71 |
| 10-22 02:09 | +10 | XRP | DOWN | 0.59 | 0.79 | 1.71 |
| 10-22 02:09 | +5 | XRP | DOWN | 0.59 | 0.79 | 1.71 |
| 10-22 02:09 | +5 | BNB | DOWN | 0.68 | 0.84 | 1.34 |
| 10-22 02:09 | +10 stop | ZEC | UP | 0.55 | 0.67 | 0.86 |
| 10-22 02:09 | +20 | ZEC | UP | 0.55 | 0.77 | 1.89 |
| 10-22 02:09 | +10 | ZEC | UP | 0.55 | 0.67 | 0.86 |
| 10-22 02:09 | +5 | ZEC | UP | 0.55 | 0.67 | 0.86 |
| 10-22 02:07 | +10 stop | NEAR | DOWN | 0.67 | 0.40 | -3.03 |
| 10-22 02:06 | +10 stop | NEAR | DOWN | 0.64 | 0.79 | 1.26 |
| 10-22 02:06 | +5 | ZEC | DOWN | 0.67 | 0.72 | 0.19 |
| 10-22 02:05 | +15 | ZEC | DOWN | 0.71 | 0.87 | 1.37 |
| 10-22 02:05 | +10 stop | BNB | DOWN | 0.70 | 0.53 | -2.03 |
| 10-22 02:05 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 10-22 02:04 | +5 | BNB | DOWN | 0.57 | 0.68 | 0.76 |
