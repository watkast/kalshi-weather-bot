# Range-Scalp Bot

*Updated Tue Oct 13 20:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14894 | 12882 | 2012 (27) | 8 | $-4827.15 | -5.1% |
| **+10¢** | 11271 | 8938 | 2333 (39) | 8 | $-4498.62 | -6.3% |
| **+15¢** | 9470 | 6975 | 2495 (57) | 8 | $-3995.18 | -6.7% |
| **+20¢** | 8426 | 5824 | 2602 (73) | 9 | $-3453.78 | -6.5% |
| **+10¢ (15¢ stop)** | 18296 | 18246 | 50 (29) | 2 | $-7109.43 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 20:09 | +10 stop | DOGE | UP | 0.63 | open |  |
| 10-13 20:09 | +5 | DOGE | UP | 0.63 | open |  |
| 10-13 20:08 | +10 stop | NEAR | UP | 0.53 | 0.65 | 0.86 |
| 10-13 20:08 | +10 stop | BTC | UP | 0.65 | open |  |
| 10-13 20:08 | +10 stop | SOL | UP | 0.64 | 0.47 | -2.05 |
| 10-13 20:07 | +10 stop | ETH | UP | 0.53 | 0.66 | 0.96 |
| 10-13 20:07 | +10 stop | HYPE | UP | 0.54 | 0.69 | 1.17 |
| 10-13 20:07 | +10 stop | NEAR | DOWN | 0.70 | 0.41 | -3.22 |
| 10-13 20:07 | +15 | NEAR | DOWN | 0.70 | open |  |
| 10-13 20:07 | +10 | NEAR | DOWN | 0.70 | open |  |
| 10-13 20:06 | +10 stop | DOGE | UP | 0.66 | 0.77 | 0.86 |
| 10-13 20:06 | +10 stop | SOL | UP | 0.70 | 0.49 | -2.39 |
| 10-13 20:06 | +5 | ZEC | UP | 0.68 | 0.73 | 0.20 |
| 10-13 20:06 | +10 stop | BTC | DOWN | 0.71 | 0.55 | -1.93 |
| 10-13 20:06 | +10 stop | DOGE | UP | 0.54 | 0.64 | 0.65 |
| 10-13 20:05 | +10 stop | BTC | DOWN | 0.54 | 0.67 | 0.96 |
| 10-13 20:05 | +10 stop | NEAR | DOWN | 0.53 | 0.67 | 1.06 |
| 10-13 20:04 | +10 stop | DOGE | UP | 0.66 | 0.49 | -2.04 |
| 10-13 20:04 | +10 stop | NEAR | DOWN | 0.57 | 0.68 | 0.76 |
| 10-13 20:04 | +10 stop | SOL | UP | 0.57 | 0.67 | 0.66 |
| 10-13 20:04 | +10 stop | BTC | UP | 0.64 | 0.40 | -2.74 |
| 10-13 20:04 | +10 stop | HYPE | UP | 0.67 | 0.52 | -1.88 |
| 10-13 20:03 | +10 stop | BNB | UP | 0.69 | 0.85 | 1.36 |
| 10-13 20:03 | +10 stop | ETH | UP | 0.65 | 0.49 | -1.94 |
| 10-13 20:03 | +5 | DOGE | UP | 0.70 | 0.77 | 0.42 |
| 10-13 20:03 | +10 stop | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 10-13 20:03 | +20 | ZEC | UP | 0.69 | open |  |
| 10-13 20:03 | +15 | ZEC | UP | 0.68 | 0.83 | 1.24 |
| 10-13 20:03 | +10 | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 10-13 20:03 | +5 | ZEC | UP | 0.69 | 0.75 | 0.31 |
| 10-13 20:03 | +10 stop | NEAR | DOWN | 0.58 | 0.41 | -2.05 |
| 10-13 20:03 | +10 | NEAR | DOWN | 0.60 | 0.73 | 1.00 |
| 10-13 20:02 | +5 | NEAR | DOWN | 0.70 | open |  |
| 10-13 20:02 | +10 stop | DOGE | DOWN | 0.54 | 0.33 | -2.44 |
| 10-13 20:02 | +10 | DOGE | DOWN | 0.54 | open |  |
| 10-13 20:02 | +5 | DOGE | DOWN | 0.54 | 0.59 | 0.15 |
| 10-13 20:02 | +5 | SOL | DOWN | 0.58 | open |  |
| 10-13 20:02 | +10 stop | BNB | DOWN | 0.65 | 0.37 | -3.15 |
| 10-13 20:02 | +20 | BNB | DOWN | 0.65 | open |  |
| 10-13 20:02 | +15 | BNB | DOWN | 0.65 | open |  |
