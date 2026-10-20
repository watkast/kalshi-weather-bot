# Range-Scalp Bot

*Updated Tue Oct 20 01:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24915 | 21695 | 3220 (31) | 1 | $-7258.55 | -4.6% |
| **+10¢** | 18743 | 15020 | 3723 (46) | 1 | $-6457.00 | -5.5% |
| **+15¢** | 15689 | 11679 | 4010 (70) | 1 | $-5823.69 | -5.9% |
| **+20¢** | 13872 | 9673 | 4199 (88) | 1 | $-5235.00 | -6.0% |
| **+10¢ (15¢ stop)** | 30570 | 30518 | 52 (30) | 0 | $-11401.59 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 01:58 | +10 stop | BNB | DOWN | 0.70 | 0.53 | -2.03 |
| 10-20 01:58 | +20 | BNB | DOWN | 0.70 | 0.95 | 2.36 |
| 10-20 01:58 | +15 | BNB | DOWN | 0.70 | 0.95 | 2.36 |
| 10-20 01:58 | +10 | BNB | DOWN | 0.70 | 0.95 | 2.36 |
| 10-20 01:58 | +5 | BNB | DOWN | 0.70 | 0.95 | 2.31 |
| 10-20 01:58 | +20 | DOGE | UP | 0.55 | open |  |
| 10-20 01:58 | +15 | DOGE | UP | 0.69 | open |  |
| 10-20 01:58 | +10 | DOGE | UP | 0.69 | open |  |
| 10-20 01:58 | +5 | DOGE | UP | 0.69 | open |  |
| 10-20 01:58 | +10 stop | DOGE | UP | 0.71 | 0.55 | -1.93 |
| 10-20 01:56 | +10 stop | NEAR | UP | 0.70 | 0.55 | -1.83 |
| 10-20 01:55 | +10 stop | NEAR | DOWN | 0.68 | 0.45 | -2.60 |
| 10-20 01:55 | +20 | NEAR | DOWN | 0.68 | 0.91 | 2.06 |
| 10-20 01:55 | +15 | NEAR | DOWN | 0.68 | 0.91 | 2.06 |
| 10-20 01:55 | +10 | NEAR | DOWN | 0.68 | 0.91 | 2.06 |
| 10-20 01:55 | +5 | NEAR | DOWN | 0.68 | 0.76 | 0.55 |
| 10-20 01:55 | +10 stop | BNB | UP | 0.67 | 0.81 | 1.13 |
| 10-20 01:55 | +10 | BNB | UP | 0.66 | 0.81 | 1.23 |
| 10-20 01:55 | +5 | BNB | UP | 0.66 | 0.71 | 0.19 |
| 10-20 01:53 | +10 stop | NEAR | UP | 0.56 | 0.71 | 1.17 |
| 10-20 01:53 | +10 stop | ZEC | UP | 0.56 | 0.67 | 0.76 |
| 10-20 01:52 | +10 stop | HYPE | UP | 0.63 | 0.79 | 1.31 |
| 10-20 01:52 | +10 | HYPE | UP | 0.63 | 0.79 | 1.31 |
| 10-20 01:52 | +5 | HYPE | UP | 0.63 | 0.79 | 1.31 |
| 10-20 01:52 | +10 stop | DOGE | UP | 0.67 | 0.88 | 1.86 |
| 10-20 01:52 | +15 | DOGE | UP | 0.67 | 0.88 | 1.86 |
| 10-20 01:52 | +10 | DOGE | UP | 0.67 | 0.88 | 1.86 |
| 10-20 01:52 | +5 | DOGE | UP | 0.67 | 0.74 | 0.40 |
| 10-20 01:52 | +10 stop | BNB | DOWN | 0.56 | 0.40 | -1.95 |
| 10-20 01:51 | +5 | ZEC | UP | 0.68 | 0.83 | 1.24 |
| 10-20 01:51 | +10 stop | XRP | UP | 0.54 | 0.65 | 0.76 |
| 10-20 01:51 | +5 | ZEC | UP | 0.62 | 0.67 | 0.17 |
| 10-20 01:51 | +10 stop | ZEC | UP | 0.67 | 0.48 | -2.24 |
| 10-20 01:50 | +10 stop | NEAR | DOWN | 0.58 | 0.42 | -1.96 |
| 10-20 01:50 | +10 stop | XRP | DOWN | 0.57 | 0.41 | -2.00 |
| 10-20 01:49 | +5 | HYPE | UP | 0.64 | 0.73 | 0.59 |
| 10-20 01:49 | +10 stop | BNB | DOWN | 0.64 | 0.47 | -2.07 |
| 10-20 01:49 | +5 | ZEC | UP | 0.55 | 0.65 | 0.66 |
| 10-20 01:49 | +5 | SOL | UP | 0.58 | 0.64 | 0.25 |
| 10-20 01:49 | +10 stop | BTC | UP | 0.68 | 0.79 | 0.82 |
