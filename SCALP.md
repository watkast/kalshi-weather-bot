# Range-Scalp Bot

*Updated Fri Oct 09 23:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9611 | 8302 | 1309 (18) | 1 | $-3199.95 | -5.3% |
| **+10¢** | 7253 | 5719 | 1534 (30) | 1 | $-3108.23 | -6.8% |
| **+15¢** | 6116 | 4498 | 1618 (43) | 1 | $-2573.05 | -6.7% |
| **+20¢** | 5448 | 3767 | 1681 (55) | 2 | $-2122.52 | -6.2% |
| **+10¢ (15¢ stop)** | 11746 | 11711 | 35 (22) | 1 | $-4480.19 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 23:19 | +10 stop | NEAR | DOWN | 0.67 | open |  |
| 10-09 23:17 | +10 stop | DOGE | DOWN | 0.23 | 0.57 | 3.09 |
| 10-09 23:17 | +20 | DOGE | DOWN | 0.23 | 0.57 | 3.09 |
| 10-09 23:17 | +15 | DOGE | DOWN | 0.23 | 0.57 | 3.09 |
| 10-09 23:17 | +10 | DOGE | DOWN | 0.23 | 0.57 | 3.09 |
| 10-09 23:17 | +5 | DOGE | DOWN | 0.23 | 0.57 | 3.09 |
| 10-09 23:16 | +10 stop | ZEC | UP | 0.70 | 0.55 | -1.83 |
| 10-09 23:16 | +20 | ZEC | UP | 0.70 | open |  |
| 10-09 23:16 | +15 | ZEC | UP | 0.70 | 0.89 | 1.68 |
| 10-09 23:16 | +10 | ZEC | UP | 0.70 | 0.80 | 0.73 |
| 10-09 23:16 | +5 | ZEC | UP | 0.70 | 0.78 | 0.52 |
| 10-09 23:16 | +10 stop | BNB | UP | 0.60 | 0.77 | 1.40 |
| 10-09 23:16 | +20 | BNB | UP | 0.60 | 0.80 | 1.71 |
| 10-09 23:16 | +15 | BNB | UP | 0.60 | 0.77 | 1.40 |
| 10-09 23:16 | +10 | BNB | UP | 0.60 | 0.77 | 1.40 |
| 10-09 23:16 | +5 | BNB | UP | 0.60 | 0.77 | 1.40 |
| 10-09 23:15 | +10 stop | NEAR | UP | 0.58 | 0.00 | -5.98 |
| 10-09 23:15 | +20 | NEAR | UP | 0.58 | open |  |
| 10-09 23:15 | +15 | NEAR | UP | 0.58 | open |  |
| 10-09 23:15 | +10 | NEAR | UP | 0.57 | open |  |
| 10-09 23:15 | +5 | NEAR | UP | 0.57 | open |  |
| 10-09 23:15 | +10 stop | XRP | DOWN | 0.58 | 1.00 | 4.03 |
| 10-09 23:15 | +20 | XRP | DOWN | 0.58 | 1.00 | 4.03 |
| 10-09 23:15 | +15 | XRP | DOWN | 0.58 | 1.00 | 4.03 |
| 10-09 23:15 | +10 | XRP | DOWN | 0.57 | 1.00 | 4.12 |
| 10-09 23:15 | +5 | XRP | DOWN | 0.57 | 1.00 | 4.12 |
| 10-09 23:13 | +10 stop | BNB | UP | 0.48 | 0.68 | 1.66 |
| 10-09 23:10 | +10 stop | BNB | DOWN | 0.63 | 0.78 | 1.20 |
| 10-09 23:09 | +5 | BNB | UP | 0.68 | 0.77 | 0.66 |
| 10-09 23:09 | +10 stop | HYPE | DOWN | 0.63 | 0.80 | 1.41 |
| 10-09 23:09 | +15 | HYPE | DOWN | 0.63 | 0.80 | 1.41 |
| 10-09 23:09 | +10 | HYPE | DOWN | 0.63 | 0.80 | 1.41 |
| 10-09 23:09 | +10 stop | BNB | UP | 0.66 | 0.41 | -2.83 |
| 10-09 23:07 | +10 stop | NEAR | UP | 0.59 | 0.79 | 1.71 |
| 10-09 23:07 | +5 | SOL | DOWN | 0.67 | 0.72 | 0.19 |
| 10-09 23:06 | +10 stop | ZEC | UP | 0.42 | 0.19 | -2.59 |
| 10-09 23:06 | +10 stop | SOL | DOWN | 0.64 | 0.77 | 1.00 |
| 10-09 23:06 | +20 | SOL | DOWN | 0.64 | 0.87 | 2.05 |
| 10-09 23:06 | +15 | SOL | DOWN | 0.65 | 0.87 | 1.96 |
| 10-09 23:06 | +10 | SOL | DOWN | 0.65 | 0.77 | 0.88 |
