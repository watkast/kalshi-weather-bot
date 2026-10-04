# Range-Scalp Bot

*Updated Sun Oct 04 14:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2348 | 2027 | 321 (3) | 3 | $-769.73 | -5.2% |
| **+10¢** | 1832 | 1475 | 357 (4) | 4 | $-572.87 | -4.9% |
| **+15¢** | 1537 | 1160 | 377 (5) | 4 | $-472.12 | -4.9% |
| **+20¢** | 1362 | 965 | 397 (9) | 4 | $-400.79 | -4.7% |
| **+10¢ (15¢ stop)** | 2903 | 2902 | 1 (1) | 4 | $-1078.64 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 14:01 | +10 stop | ETH | DOWN | 0.68 | open |  |
| 10-04 14:01 | +20 | ETH | DOWN | 0.68 | open |  |
| 10-04 14:01 | +15 | ETH | DOWN | 0.68 | open |  |
| 10-04 14:01 | +10 | ETH | DOWN | 0.68 | open |  |
| 10-04 14:01 | +5 | ETH | DOWN | 0.68 | open |  |
| 10-04 14:00 | +10 stop | HYPE | UP | 0.68 | open |  |
| 10-04 14:00 | +20 | HYPE | UP | 0.68 | open |  |
| 10-04 14:00 | +15 | HYPE | UP | 0.68 | open |  |
| 10-04 14:00 | +10 | HYPE | UP | 0.68 | open |  |
| 10-04 14:00 | +5 | HYPE | UP | 0.68 | open |  |
| 10-04 14:00 | +10 stop | BNB | UP | 0.49 | open |  |
| 10-04 14:00 | +20 | BNB | UP | 0.49 | open |  |
| 10-04 14:00 | +15 | BNB | UP | 0.50 | open |  |
| 10-04 14:00 | +10 | BNB | UP | 0.51 | open |  |
| 10-04 14:00 | +5 | BNB | UP | 0.49 | 0.54 | 0.14 |
| 10-04 14:00 | +10 stop | NEAR | UP | 0.49 | open |  |
| 10-04 14:00 | +20 | NEAR | UP | 0.49 | open |  |
| 10-04 14:00 | +15 | NEAR | UP | 0.49 | open |  |
| 10-04 14:00 | +10 | NEAR | UP | 0.49 | open |  |
| 10-04 14:00 | +5 | NEAR | UP | 0.51 | open |  |
| 10-04 13:56 | +10 stop | BNB | DOWN | 0.61 | 0.81 | 1.72 |
| 10-04 13:56 | +10 stop | XRP | UP | 0.67 | 0.84 | 1.44 |
| 10-04 13:56 | +20 | XRP | UP | 0.67 | 0.88 | 1.86 |
| 10-04 13:56 | +15 | XRP | UP | 0.67 | 0.84 | 1.44 |
| 10-04 13:56 | +10 | XRP | UP | 0.67 | 0.84 | 1.44 |
| 10-04 13:56 | +5 | XRP | UP | 0.67 | 0.73 | 0.30 |
| 10-04 13:53 | +10 stop | BNB | UP | 0.58 | 0.42 | -1.96 |
| 10-04 13:51 | +10 stop | BNB | DOWN | 0.56 | 0.38 | -2.14 |
| 10-04 13:51 | +10 stop | ETH | UP | 0.67 | 0.77 | 0.71 |
| 10-04 13:51 | +15 | ETH | UP | 0.67 | 0.83 | 1.34 |
| 10-04 13:51 | +10 | ETH | UP | 0.67 | 0.77 | 0.71 |
| 10-04 13:51 | +5 | ETH | UP | 0.67 | 0.77 | 0.71 |
| 10-04 13:50 | +10 stop | NEAR | DOWN | 0.59 | 0.75 | 1.29 |
| 10-04 13:50 | +10 stop | BNB | UP | 0.65 | 0.48 | -2.04 |
| 10-04 13:50 | +10 | BNB | UP | 0.65 | no | -6.66 |
| 10-04 13:50 | +5 | BNB | UP | 0.65 | no | -6.66 |
| 10-04 13:48 | +10 stop | BNB | DOWN | 0.58 | 0.43 | -1.86 |
| 10-04 13:48 | +10 stop | DOGE | UP | 0.70 | 0.84 | 1.16 |
| 10-04 13:48 | +20 | DOGE | UP | 0.70 | 0.91 | 1.93 |
| 10-04 13:48 | +15 | DOGE | UP | 0.70 | 0.86 | 1.37 |
