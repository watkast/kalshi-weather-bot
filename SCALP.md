# Range-Scalp Bot

*Updated Fri Oct 16 13:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19255 | 16730 | 2525 (29) | 3 | $-5815.74 | -4.8% |
| **+10¢** | 14514 | 11595 | 2919 (41) | 4 | $-5246.99 | -5.7% |
| **+15¢** | 12151 | 9008 | 3143 (60) | 4 | $-4766.60 | -6.3% |
| **+20¢** | 10779 | 7484 | 3295 (79) | 5 | $-4251.68 | -6.3% |
| **+10¢ (15¢ stop)** | 23687 | 23637 | 50 (29) | 0 | $-9134.06 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 13:12 | +5 | ETH | UP | 0.65 | 0.74 | 0.60 |
| 10-16 13:12 | +10 stop | NEAR | DOWN | 0.58 | 0.37 | -2.46 |
| 10-16 13:12 | +20 | NEAR | DOWN | 0.57 | open |  |
| 10-16 13:12 | +15 | NEAR | DOWN | 0.57 | open |  |
| 10-16 13:12 | +10 | NEAR | DOWN | 0.57 | open |  |
| 10-16 13:12 | +5 | NEAR | DOWN | 0.57 | open |  |
| 10-16 13:12 | +10 stop | ETH | DOWN | 0.49 | 0.60 | 0.75 |
| 10-16 13:12 | +5 | ETH | DOWN | 0.49 | 0.58 | 0.54 |
| 10-16 13:09 | +10 stop | NEAR | DOWN | 0.71 | 0.89 | 1.58 |
| 10-16 13:09 | +15 | NEAR | DOWN | 0.71 | 0.89 | 1.58 |
| 10-16 13:09 | +10 | NEAR | DOWN | 0.71 | 0.89 | 1.58 |
| 10-16 13:07 | +10 stop | ETH | DOWN | 0.68 | 0.80 | 0.92 |
| 10-16 13:07 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 10-16 13:07 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 10-16 13:07 | +10 stop | NEAR | UP | 0.46 | 0.25 | -2.42 |
| 10-16 13:07 | +10 stop | DOGE | UP | 0.47 | 0.63 | 1.25 |
| 10-16 13:06 | +5 | NEAR | DOWN | 0.70 | 0.76 | 0.32 |
| 10-16 13:05 | +10 stop | BTC | DOWN | 0.69 | 0.50 | -2.23 |
| 10-16 13:05 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-16 13:05 | +10 stop | XRP | DOWN | 0.68 | 0.49 | -2.24 |
| 10-16 13:04 | +10 stop | DOGE | DOWN | 0.65 | 0.44 | -2.44 |
| 10-16 13:04 | +5 | NEAR | DOWN | 0.61 | 0.68 | 0.39 |
| 10-16 13:03 | +10 stop | ETH | DOWN | 0.59 | 0.72 | 0.98 |
| 10-16 13:03 | +10 stop | DOGE | DOWN | 0.53 | 0.68 | 1.16 |
| 10-16 13:03 | +10 stop | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-16 13:03 | +5 | ETH | DOWN | 0.60 | 0.72 | 0.83 |
| 10-16 13:03 | +10 stop | NEAR | DOWN | 0.60 | 0.30 | -3.32 |
| 10-16 13:03 | +10 stop | SOL | DOWN | 0.61 | 0.73 | 0.89 |
| 10-16 13:03 | +20 | SOL | DOWN | 0.61 | 0.81 | 1.72 |
| 10-16 13:03 | +15 | SOL | DOWN | 0.60 | 0.77 | 1.40 |
| 10-16 13:03 | +10 | SOL | DOWN | 0.60 | 0.73 | 0.99 |
| 10-16 13:03 | +5 | SOL | DOWN | 0.60 | 0.73 | 0.99 |
| 10-16 13:03 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-16 13:03 | +10 stop | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-16 13:03 | +10 stop | NEAR | UP | 0.45 | 0.59 | 1.05 |
| 10-16 13:03 | +10 stop | ZEC | DOWN | 0.61 | 0.75 | 1.05 |
| 10-16 13:02 | +5 | BTC | UP | 0.51 | 0.57 | 0.24 |
| 10-16 13:02 | +10 stop | DOGE | UP | 0.66 | 0.42 | -2.74 |
| 10-16 13:02 | +20 | DOGE | UP | 0.66 | open |  |
| 10-16 13:02 | +15 | DOGE | UP | 0.66 | 0.85 | 1.66 |
