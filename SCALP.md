# Range-Scalp Bot

*Updated Fri Oct 23 01:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29597 | 25759 | 3838 (39) | 1 | $-8752.85 | -4.7% |
| **+10¢** | 22199 | 17757 | 4442 (55) | 1 | $-7874.51 | -5.6% |
| **+15¢** | 18586 | 13817 | 4769 (78) | 1 | $-7056.56 | -6.0% |
| **+20¢** | 16450 | 11452 | 4998 (100) | 1 | $-6385.43 | -6.2% |
| **+10¢ (15¢ stop)** | 36349 | 36290 | 59 (32) | 0 | $-13721.33 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 01:43 | +10 stop | DOGE | UP | 0.70 | 0.93 | 2.13 |
| 10-23 01:43 | +20 | DOGE | UP | 0.70 | 0.93 | 2.13 |
| 10-23 01:43 | +15 | DOGE | UP | 0.70 | 0.93 | 2.13 |
| 10-23 01:43 | +10 | DOGE | UP | 0.71 | 0.93 | 2.03 |
| 10-23 01:43 | +5 | DOGE | UP | 0.71 | 0.93 | 2.03 |
| 10-23 01:43 | +10 stop | BNB | UP | 0.63 | 0.73 | 0.69 |
| 10-23 01:43 | +10 | BNB | UP | 0.63 | 0.73 | 0.69 |
| 10-23 01:43 | +5 | BNB | UP | 0.63 | 0.73 | 0.69 |
| 10-23 01:42 | +10 stop | BTC | DOWN | 0.66 | 0.86 | 1.75 |
| 10-23 01:42 | +20 | BTC | DOWN | 0.66 | 0.86 | 1.75 |
| 10-23 01:42 | +15 | BTC | DOWN | 0.66 | 0.86 | 1.75 |
| 10-23 01:42 | +10 | BTC | DOWN | 0.66 | 0.86 | 1.75 |
| 10-23 01:42 | +5 | BTC | DOWN | 0.66 | 0.86 | 1.75 |
| 10-23 01:42 | +10 stop | BNB | UP | 0.56 | 0.66 | 0.66 |
| 10-23 01:42 | +20 | BNB | UP | 0.56 | 0.92 | 3.37 |
| 10-23 01:42 | +15 | BNB | UP | 0.56 | 0.73 | 1.38 |
| 10-23 01:42 | +10 | BNB | UP | 0.56 | 0.66 | 0.66 |
| 10-23 01:42 | +5 | BNB | UP | 0.56 | 0.66 | 0.66 |
| 10-23 01:42 | +5 | SOL | UP | 0.66 | 0.78 | 0.94 |
| 10-23 01:42 | +10 stop | SOL | UP | 0.70 | 0.86 | 1.36 |
| 10-23 01:42 | +20 | SOL | UP | 0.70 | 0.94 | 2.21 |
| 10-23 01:42 | +15 | SOL | UP | 0.70 | 0.86 | 1.36 |
| 10-23 01:42 | +10 | SOL | UP | 0.70 | 0.86 | 1.36 |
| 10-23 01:41 | +10 stop | HYPE | DOWN | 0.68 | 0.37 | -3.43 |
| 10-23 01:41 | +20 | HYPE | DOWN | 0.65 | open |  |
| 10-23 01:41 | +15 | HYPE | DOWN | 0.65 | open |  |
| 10-23 01:41 | +10 | HYPE | DOWN | 0.65 | open |  |
| 10-23 01:41 | +5 | HYPE | DOWN | 0.65 | open |  |
| 10-23 01:33 | +10 stop | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 10-23 01:33 | +20 | NEAR | DOWN | 0.65 | 0.93 | 2.54 |
| 10-23 01:33 | +15 | NEAR | DOWN | 0.65 | 0.93 | 2.54 |
| 10-23 01:33 | +10 | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 10-23 01:33 | +5 | NEAR | DOWN | 0.65 | 0.71 | 0.29 |
| 10-23 01:33 | +10 stop | ZEC | DOWN | 0.69 | 0.80 | 0.83 |
| 10-23 01:32 | +10 stop | BNB | DOWN | 0.70 | 0.83 | 1.03 |
| 10-23 01:32 | +10 | BNB | DOWN | 0.70 | 0.80 | 0.73 |
| 10-23 01:32 | +5 | BNB | DOWN | 0.70 | 0.80 | 0.73 |
| 10-23 01:31 | +10 stop | ZEC | UP | 0.61 | 0.44 | -2.05 |
| 10-23 01:31 | +20 | ZEC | UP | 0.61 | 0.82 | 1.82 |
| 10-23 01:31 | +15 | ZEC | UP | 0.61 | 0.82 | 1.82 |
