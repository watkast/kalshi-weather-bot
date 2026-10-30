# Range-Scalp Bot

*Updated Fri Oct 30 02:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40051 | 34989 | 5062 (51) | 1 | $-10947.99 | -4.3% |
| **+10¢** | 29845 | 23987 | 5858 (74) | 3 | $-9694.80 | -5.2% |
| **+15¢** | 24961 | 18657 | 6304 (101) | 4 | $-8682.71 | -5.5% |
| **+20¢** | 22147 | 15536 | 6611 (130) | 5 | $-7613.12 | -5.5% |
| **+10¢ (15¢ stop)** | 48862 | 48792 | 70 (37) | 3 | $-18464.79 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 02:07 | +5 | BNB | UP | 0.51 | open |  |
| 10-30 02:07 | +10 stop | XRP | UP | 0.51 | 0.67 | 1.26 |
| 10-30 02:07 | +5 | XRP | UP | 0.51 | 0.67 | 1.26 |
| 10-30 02:07 | +10 stop | SOL | DOWN | 0.70 | open |  |
| 10-30 02:07 | +20 | SOL | DOWN | 0.70 | open |  |
| 10-30 02:07 | +15 | SOL | DOWN | 0.70 | open |  |
| 10-30 02:06 | +5 | BNB | UP | 0.53 | 0.67 | 1.06 |
| 10-30 02:06 | +10 stop | ZEC | DOWN | 0.65 | open |  |
| 10-30 02:06 | +5 | ZEC | DOWN | 0.65 | 0.71 | 0.29 |
| 10-30 02:05 | +10 stop | BNB | DOWN | 0.46 | open |  |
| 10-30 02:05 | +15 | BNB | DOWN | 0.46 | open |  |
| 10-30 02:05 | +10 | BNB | DOWN | 0.46 | open |  |
| 10-30 02:05 | +5 | BNB | DOWN | 0.46 | 0.54 | 0.44 |
| 10-30 02:05 | +10 stop | XRP | DOWN | 0.60 | 0.31 | -3.22 |
| 10-30 02:04 | +5 | ETH | DOWN | 0.69 | 0.74 | 0.21 |
| 10-30 02:03 | +10 stop | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-30 02:03 | +20 | ZEC | DOWN | 0.71 | open |  |
| 10-30 02:03 | +15 | ZEC | DOWN | 0.71 | open |  |
| 10-30 02:03 | +10 | ZEC | DOWN | 0.71 | open |  |
| 10-30 02:03 | +5 | ZEC | DOWN | 0.71 | 0.78 | 0.42 |
| 10-30 02:02 | +5 | BNB | DOWN | 0.66 | 0.72 | 0.29 |
| 10-30 02:02 | +5 | SOL | DOWN | 0.61 | 0.66 | 0.17 |
| 10-30 02:02 | +5 | BTC | DOWN | 0.68 | 0.77 | 0.61 |
| 10-30 02:02 | +10 stop | ETH | DOWN | 0.60 | 0.73 | 0.99 |
| 10-30 02:02 | +20 | ETH | DOWN | 0.60 | 0.80 | 1.71 |
| 10-30 02:02 | +15 | ETH | DOWN | 0.61 | 0.80 | 1.61 |
| 10-30 02:02 | +10 | ETH | DOWN | 0.61 | 0.73 | 0.89 |
| 10-30 02:02 | +5 | ETH | DOWN | 0.62 | 0.69 | 0.38 |
| 10-30 02:02 | +10 stop | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-30 02:02 | +20 | DOGE | DOWN | 0.63 | 0.86 | 2.04 |
| 10-30 02:02 | +15 | DOGE | DOWN | 0.63 | 0.78 | 1.20 |
| 10-30 02:02 | +10 | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-30 02:02 | +5 | DOGE | DOWN | 0.62 | 0.73 | 0.79 |
| 10-30 02:02 | +10 stop | NEAR | DOWN | 0.60 | 0.78 | 1.50 |
| 10-30 02:02 | +20 | NEAR | DOWN | 0.60 | 0.82 | 1.92 |
| 10-30 02:02 | +15 | NEAR | DOWN | 0.60 | 0.78 | 1.50 |
| 10-30 02:02 | +10 | NEAR | DOWN | 0.60 | 0.78 | 1.50 |
| 10-30 02:02 | +5 | NEAR | DOWN | 0.60 | 0.69 | 0.58 |
| 10-30 02:01 | +10 stop | SOL | DOWN | 0.58 | 0.70 | 0.87 |
| 10-30 02:01 | +20 | SOL | DOWN | 0.58 | 0.80 | 1.90 |
