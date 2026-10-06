# Range-Scalp Bot

*Updated Tue Oct 06 11:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4996 | 4322 | 674 (7) | 1 | $-1589.67 | -5.0% |
| **+10¢** | 3834 | 3050 | 784 (11) | 3 | $-1452.79 | -6.0% |
| **+15¢** | 3222 | 2391 | 831 (14) | 3 | $-1252.55 | -6.2% |
| **+20¢** | 2887 | 2020 | 867 (19) | 3 | $-1030.37 | -5.7% |
| **+10¢ (15¢ stop)** | 6112 | 6099 | 13 (8) | 1 | $-2182.82 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 11:22 | +10 stop | DOGE | UP | 0.59 | 0.73 | 1.09 |
| 10-06 11:21 | +10 stop | DOGE | UP | 0.66 | 0.50 | -1.94 |
| 10-06 11:21 | +10 | DOGE | UP | 0.66 | open |  |
| 10-06 11:21 | +5 | DOGE | UP | 0.61 | 0.73 | 0.89 |
| 10-06 11:20 | +10 stop | SOL | DOWN | 0.55 | 0.40 | -1.85 |
| 10-06 11:20 | +10 | SOL | DOWN | 0.55 | open |  |
| 10-06 11:20 | +5 | SOL | DOWN | 0.55 | open |  |
| 10-06 11:20 | +10 stop | BNB | UP | 0.62 | open |  |
| 10-06 11:20 | +20 | BNB | UP | 0.62 | open |  |
| 10-06 11:20 | +15 | BNB | UP | 0.62 | open |  |
| 10-06 11:20 | +10 | BNB | UP | 0.62 | open |  |
| 10-06 11:20 | +5 | BNB | UP | 0.62 | 0.68 | 0.27 |
| 10-06 11:20 | +10 stop | ZEC | UP | 0.60 | 0.71 | 0.78 |
| 10-06 11:20 | +20 | ZEC | UP | 0.60 | 0.81 | 1.82 |
| 10-06 11:20 | +15 | ZEC | UP | 0.60 | 0.77 | 1.40 |
| 10-06 11:20 | +10 | ZEC | UP | 0.60 | 0.71 | 0.78 |
| 10-06 11:20 | +5 | ZEC | UP | 0.60 | 0.71 | 0.78 |
| 10-06 11:20 | +10 stop | DOGE | UP | 0.53 | 0.63 | 0.65 |
| 10-06 11:20 | +10 | DOGE | UP | 0.53 | 0.63 | 0.65 |
| 10-06 11:20 | +5 | DOGE | UP | 0.53 | 0.59 | 0.25 |
| 10-06 11:17 | +5 | SOL | UP | 0.68 | 0.77 | 0.61 |
| 10-06 11:16 | +10 stop | DOGE | UP | 0.70 | 0.80 | 0.73 |
| 10-06 11:16 | +20 | DOGE | UP | 0.70 | open |  |
| 10-06 11:16 | +15 | DOGE | UP | 0.70 | open |  |
| 10-06 11:16 | +10 | DOGE | UP | 0.70 | 0.80 | 0.73 |
| 10-06 11:16 | +5 | DOGE | UP | 0.70 | 0.75 | 0.21 |
| 10-06 11:16 | +10 stop | SOL | UP | 0.65 | 0.77 | 0.91 |
| 10-06 11:16 | +20 | SOL | UP | 0.65 | open |  |
| 10-06 11:16 | +15 | SOL | UP | 0.65 | open |  |
| 10-06 11:16 | +10 | SOL | UP | 0.65 | 0.77 | 0.91 |
| 10-06 11:16 | +5 | SOL | UP | 0.65 | 0.70 | 0.19 |
| 10-06 11:14 | +10 stop | BNB | DOWN | 0.34 | 0.69 | 3.19 |
| 10-06 11:14 | +20 | BNB | DOWN | 0.34 | 0.69 | 3.19 |
| 10-06 11:14 | +15 | BNB | DOWN | 0.34 | 0.69 | 3.19 |
| 10-06 11:14 | +10 | BNB | DOWN | 0.34 | 0.69 | 3.19 |
| 10-06 11:14 | +5 | BNB | DOWN | 0.41 | 0.69 | 2.48 |
| 10-06 11:11 | +10 stop | DOGE | DOWN | 0.48 | 0.62 | 1.05 |
| 10-06 11:08 | +10 stop | BTC | DOWN | 0.63 | 0.76 | 1.00 |
| 10-06 11:08 | +10 stop | ZEC | DOWN | 0.71 | 0.84 | 1.06 |
| 10-06 11:08 | +10 stop | HYPE | DOWN | 0.59 | 0.71 | 0.84 |
