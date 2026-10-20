# Range-Scalp Bot

*Updated Tue Oct 20 01:18 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24869 | 21649 | 3220 (31) | 0 | $-7289.27 | -4.7% |
| **+10¢** | 18708 | 14987 | 3721 (46) | 1 | $-6483.95 | -5.5% |
| **+15¢** | 15659 | 11651 | 4008 (70) | 1 | $-5856.41 | -6.0% |
| **+20¢** | 13842 | 9645 | 4197 (88) | 5 | $-5278.40 | -6.1% |
| **+10¢ (15¢ stop)** | 30522 | 30470 | 52 (30) | 1 | $-11406.11 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 01:17 | +10 stop | ZEC | UP | 0.58 | 0.72 | 1.07 |
| 10-20 01:17 | +20 | ZEC | UP | 0.58 | open |  |
| 10-20 01:17 | +15 | ZEC | UP | 0.56 | 0.72 | 1.27 |
| 10-20 01:17 | +10 | ZEC | UP | 0.56 | 0.67 | 0.76 |
| 10-20 01:17 | +5 | ZEC | UP | 0.56 | 0.65 | 0.56 |
| 10-20 01:17 | +10 stop | HYPE | UP | 0.70 | open |  |
| 10-20 01:17 | +20 | HYPE | UP | 0.70 | open |  |
| 10-20 01:17 | +15 | HYPE | UP | 0.69 | open |  |
| 10-20 01:17 | +10 | HYPE | UP | 0.69 | open |  |
| 10-20 01:17 | +5 | HYPE | UP | 0.68 | 0.74 | 0.26 |
| 10-20 01:16 | +10 stop | BNB | UP | 0.67 | 0.80 | 1.02 |
| 10-20 01:16 | +10 stop | XRP | UP | 0.70 | 0.87 | 1.43 |
| 10-20 01:16 | +20 | XRP | UP | 0.71 | open |  |
| 10-20 01:16 | +15 | XRP | UP | 0.71 | 0.87 | 1.37 |
| 10-20 01:16 | +10 | XRP | UP | 0.71 | 0.87 | 1.37 |
| 10-20 01:16 | +5 | XRP | UP | 0.70 | 0.77 | 0.42 |
| 10-20 01:16 | +10 stop | DOGE | UP | 0.70 | 0.83 | 1.05 |
| 10-20 01:16 | +20 | DOGE | UP | 0.70 | open |  |
| 10-20 01:16 | +15 | DOGE | UP | 0.70 | 0.86 | 1.36 |
| 10-20 01:16 | +10 | DOGE | UP | 0.70 | 0.83 | 1.05 |
| 10-20 01:16 | +5 | DOGE | UP | 0.69 | 0.83 | 1.15 |
| 10-20 01:16 | +10 stop | SOL | UP | 0.63 | 0.74 | 0.79 |
| 10-20 01:16 | +20 | SOL | UP | 0.64 | open |  |
| 10-20 01:16 | +15 | SOL | UP | 0.64 | 0.80 | 1.34 |
| 10-20 01:16 | +10 | SOL | UP | 0.63 | 0.74 | 0.81 |
| 10-20 01:16 | +5 | SOL | UP | 0.63 | 0.74 | 0.81 |
| 10-20 01:15 | +10 stop | NEAR | UP | 0.65 | 0.84 | 1.64 |
| 10-20 01:15 | +20 | NEAR | UP | 0.65 | 0.88 | 2.06 |
| 10-20 01:15 | +15 | NEAR | UP | 0.67 | 0.84 | 1.45 |
| 10-20 01:15 | +10 | NEAR | UP | 0.68 | 0.84 | 1.34 |
| 10-20 01:15 | +5 | NEAR | UP | 0.68 | 0.84 | 1.34 |
| 10-20 01:15 | +10 stop | BNB | UP | 0.66 | 0.49 | -2.04 |
| 10-20 01:15 | +20 | BNB | UP | 0.66 | 0.87 | 1.86 |
| 10-20 01:15 | +15 | BNB | UP | 0.66 | 0.87 | 1.86 |
| 10-20 01:15 | +10 | BNB | UP | 0.66 | 0.80 | 1.12 |
| 10-20 01:15 | +5 | BNB | UP | 0.66 | 0.72 | 0.29 |
| 10-20 01:07 | +10 stop | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 10-20 01:06 | +10 stop | NEAR | DOWN | 0.69 | 0.36 | -3.62 |
| 10-20 01:06 | +20 | NEAR | DOWN | 0.69 | 0.91 | 1.93 |
| 10-20 01:06 | +15 | NEAR | DOWN | 0.69 | 0.86 | 1.46 |
