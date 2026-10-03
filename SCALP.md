# Range-Scalp Bot

*Updated Sat Oct 03 15:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 902 | 788 | 114 (2) | 0 | $-237.56 | -4.2% |
| **+10¢** | 687 | 562 | 125 (4) | 0 | $-123.41 | -2.8% |
| **+15¢** | 581 | 445 | 136 (5) | 1 | $-108.48 | -3.0% |
| **+20¢** | 508 | 365 | 143 (5) | 2 | $-101.35 | -3.2% |
| **+10¢ (15¢ stop)** | 1142 | 1141 | 1 (1) | 0 | $-559.49 | -7.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 15:06 | +10 stop | NEAR | DOWN | 0.67 | 0.83 | 1.34 |
| 10-03 15:06 | +20 | NEAR | DOWN | 0.67 | open |  |
| 10-03 15:06 | +15 | NEAR | DOWN | 0.67 | 0.83 | 1.34 |
| 10-03 15:06 | +10 | NEAR | DOWN | 0.67 | 0.83 | 1.34 |
| 10-03 15:06 | +5 | NEAR | DOWN | 0.68 | 0.83 | 1.24 |
| 10-03 15:05 | +10 stop | BNB | UP | 0.62 | 0.74 | 0.89 |
| 10-03 15:02 | +10 stop | BNB | DOWN | 0.63 | 0.45 | -2.19 |
| 10-03 15:02 | +20 | BNB | DOWN | 0.63 | open |  |
| 10-03 15:02 | +15 | BNB | DOWN | 0.63 | open |  |
| 10-03 15:02 | +10 | BNB | DOWN | 0.63 | 0.76 | 0.98 |
| 10-03 15:02 | +5 | BNB | DOWN | 0.63 | 0.76 | 0.98 |
| 10-03 15:00 | +10 stop | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 10-03 15:00 | +20 | NEAR | DOWN | 0.62 | 0.82 | 1.72 |
| 10-03 15:00 | +15 | NEAR | DOWN | 0.62 | 0.82 | 1.72 |
| 10-03 15:00 | +10 | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 10-03 15:00 | +5 | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 10-03 14:50 | +10 stop | BNB | UP | 0.71 | 0.83 | 0.95 |
| 10-03 14:50 | +10 | BNB | UP | 0.71 | 0.83 | 0.95 |
| 10-03 14:50 | +5 | BNB | UP | 0.71 | 0.83 | 0.95 |
| 10-03 14:46 | +10 stop | BNB | UP | 0.60 | 0.73 | 0.94 |
| 10-03 14:46 | +20 | BNB | UP | 0.60 | 0.83 | 1.98 |
| 10-03 14:46 | +15 | BNB | UP | 0.60 | 0.83 | 1.98 |
| 10-03 14:46 | +10 | BNB | UP | 0.60 | 0.73 | 0.94 |
| 10-03 14:46 | +5 | BNB | UP | 0.60 | 0.69 | 0.53 |
| 10-03 14:45 | +10 stop | SOL | UP | 0.70 | 0.82 | 0.94 |
| 10-03 14:45 | +20 | SOL | UP | 0.70 | 0.91 | 1.86 |
| 10-03 14:45 | +15 | SOL | UP | 0.70 | 0.85 | 1.26 |
| 10-03 14:45 | +10 | SOL | UP | 0.70 | 0.82 | 0.94 |
| 10-03 14:45 | +5 | SOL | UP | 0.70 | 0.77 | 0.42 |
| 10-03 14:42 | +5 | DOGE | UP | 0.56 | 0.65 | 0.51 |
| 10-03 14:41 | +10 stop | DOGE | UP | 0.56 | 0.69 | 0.97 |
| 10-03 14:41 | +10 stop | XRP | UP | 0.62 | 0.73 | 0.79 |
| 10-03 14:41 | +15 | XRP | UP | 0.62 | 0.83 | 1.83 |
| 10-03 14:41 | +10 | XRP | UP | 0.63 | 0.73 | 0.70 |
| 10-03 14:41 | +5 | XRP | UP | 0.63 | 0.69 | 0.28 |
| 10-03 14:40 | +10 stop | BNB | UP | 0.31 | 0.63 | 2.90 |
| 10-03 14:40 | +5 | NEAR | UP | 0.68 | 0.77 | 0.62 |
| 10-03 14:39 | +10 stop | NEAR | UP | 0.60 | 0.77 | 1.40 |
| 10-03 14:39 | +10 stop | XRP | DOWN | 0.50 | 0.62 | 0.85 |
| 10-03 14:39 | +15 | XRP | DOWN | 0.50 | 0.71 | 1.77 |
