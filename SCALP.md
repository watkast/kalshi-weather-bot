# Range-Scalp Bot

*Updated Fri Oct 16 23:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19992 | 17390 | 2602 (29) | 4 | $-5906.52 | -4.7% |
| **+10¢** | 15058 | 12050 | 3008 (41) | 4 | $-5302.94 | -5.6% |
| **+15¢** | 12595 | 9360 | 3235 (60) | 4 | $-4792.21 | -6.1% |
| **+20¢** | 11171 | 7783 | 3388 (79) | 4 | $-4227.80 | -6.0% |
| **+10¢ (15¢ stop)** | 24563 | 24513 | 50 (29) | 2 | $-9334.06 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 23:07 | +10 stop | SOL | UP | 0.53 | open |  |
| 10-16 23:07 | +10 | SOL | UP | 0.53 | open |  |
| 10-16 23:07 | +5 | SOL | UP | 0.53 | open |  |
| 10-16 23:06 | +10 stop | BNB | DOWN | 0.69 | open |  |
| 10-16 23:06 | +10 stop | ETH | UP | 0.63 | 0.47 | -1.95 |
| 10-16 23:06 | +20 | ETH | UP | 0.63 | open |  |
| 10-16 23:06 | +15 | ETH | UP | 0.63 | open |  |
| 10-16 23:06 | +10 | ETH | UP | 0.63 | open |  |
| 10-16 23:06 | +5 | ETH | UP | 0.63 | open |  |
| 10-16 23:04 | +5 | BNB | UP | 0.66 | open |  |
| 10-16 23:03 | +5 | BTC | UP | 0.70 | open |  |
| 10-16 23:01 | +10 stop | NEAR | UP | 0.67 | 0.82 | 1.23 |
| 10-16 23:01 | +20 | NEAR | UP | 0.67 | 0.87 | 1.76 |
| 10-16 23:01 | +15 | NEAR | UP | 0.67 | 0.82 | 1.23 |
| 10-16 23:01 | +10 | NEAR | UP | 0.67 | 0.82 | 1.23 |
| 10-16 23:01 | +5 | NEAR | UP | 0.67 | 0.82 | 1.23 |
| 10-16 23:01 | +10 stop | SOL | UP | 0.70 | 0.80 | 0.73 |
| 10-16 23:01 | +20 | SOL | UP | 0.70 | open |  |
| 10-16 23:01 | +15 | SOL | UP | 0.70 | open |  |
| 10-16 23:01 | +10 | SOL | UP | 0.71 | 0.81 | 0.74 |
| 10-16 23:01 | +5 | SOL | UP | 0.71 | 0.79 | 0.53 |
| 10-16 23:01 | +10 stop | BNB | UP | 0.67 | 0.48 | -2.24 |
| 10-16 23:01 | +20 | BNB | UP | 0.67 | open |  |
| 10-16 23:01 | +15 | BNB | UP | 0.67 | open |  |
| 10-16 23:01 | +10 | BNB | UP | 0.67 | open |  |
| 10-16 23:01 | +5 | BNB | UP | 0.67 | 0.72 | 0.19 |
| 10-16 23:01 | +10 stop | DOGE | UP | 0.68 | 0.84 | 1.34 |
| 10-16 23:01 | +20 | DOGE | UP | 0.68 | 0.88 | 1.76 |
| 10-16 23:01 | +15 | DOGE | UP | 0.68 | 0.84 | 1.34 |
| 10-16 23:01 | +10 | DOGE | UP | 0.68 | 0.84 | 1.34 |
| 10-16 23:01 | +5 | DOGE | UP | 0.68 | 0.73 | 0.20 |
| 10-16 23:01 | +10 stop | BTC | UP | 0.63 | 0.48 | -1.85 |
| 10-16 23:01 | +20 | BTC | UP | 0.63 | open |  |
| 10-16 23:01 | +15 | BTC | UP | 0.63 | open |  |
| 10-16 23:01 | +10 | BTC | UP | 0.63 | open |  |
| 10-16 23:01 | +5 | BTC | UP | 0.63 | 0.68 | 0.17 |
| 10-16 22:59 | +10 stop | BTC | DOWN | 0.14 | 0.58 | 4.13 |
| 10-16 22:59 | +20 | BTC | DOWN | 0.15 | 0.58 | 4.03 |
| 10-16 22:59 | +15 | BTC | DOWN | 0.15 | 0.58 | 4.03 |
| 10-16 22:59 | +10 | BTC | DOWN | 0.16 | 0.58 | 3.92 |
