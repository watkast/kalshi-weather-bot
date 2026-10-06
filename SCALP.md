# Range-Scalp Bot

*Updated Tue Oct 06 01:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4468 | 3855 | 613 (6) | 1 | $-1486.41 | -5.3% |
| **+10¢** | 3439 | 2727 | 712 (9) | 3 | $-1377.81 | -6.4% |
| **+15¢** | 2886 | 2133 | 753 (12) | 3 | $-1198.76 | -6.6% |
| **+20¢** | 2586 | 1802 | 784 (17) | 3 | $-1001.08 | -6.2% |
| **+10¢ (15¢ stop)** | 5492 | 5481 | 11 (6) | 0 | $-1982.24 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 01:33 | +5 | HYPE | DOWN | 0.66 | 0.74 | 0.50 |
| 10-06 01:33 | +10 stop | NEAR | DOWN | 0.62 | 0.78 | 1.32 |
| 10-06 01:33 | +10 stop | DOGE | UP | 0.66 | 0.44 | -2.54 |
| 10-06 01:33 | +5 | DOGE | UP | 0.66 | 0.72 | 0.29 |
| 10-06 01:33 | +10 stop | XRP | UP | 0.70 | 0.47 | -2.63 |
| 10-06 01:33 | +20 | XRP | UP | 0.70 | open |  |
| 10-06 01:33 | +15 | XRP | UP | 0.70 | open |  |
| 10-06 01:33 | +10 | XRP | UP | 0.70 | open |  |
| 10-06 01:33 | +5 | XRP | UP | 0.70 | 0.75 | 0.21 |
| 10-06 01:33 | +10 stop | ZEC | DOWN | 0.60 | 0.72 | 0.88 |
| 10-06 01:32 | +10 stop | ETH | DOWN | 0.65 | 0.79 | 1.12 |
| 10-06 01:32 | +10 | ETH | DOWN | 0.65 | 0.79 | 1.12 |
| 10-06 01:32 | +5 | ETH | DOWN | 0.65 | 0.79 | 1.12 |
| 10-06 01:32 | +10 stop | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-06 01:32 | +10 stop | HYPE | UP | 0.48 | 0.24 | -2.71 |
| 10-06 01:32 | +20 | HYPE | UP | 0.48 | open |  |
| 10-06 01:32 | +15 | HYPE | UP | 0.48 | open |  |
| 10-06 01:32 | +10 | HYPE | UP | 0.48 | open |  |
| 10-06 01:32 | +5 | HYPE | UP | 0.48 | 0.54 | 0.24 |
| 10-06 01:32 | +10 stop | ETH | DOWN | 0.54 | 0.66 | 0.86 |
| 10-06 01:32 | +10 | ETH | DOWN | 0.54 | 0.66 | 0.86 |
| 10-06 01:32 | +5 | ETH | DOWN | 0.54 | 0.66 | 0.86 |
| 10-06 01:32 | +10 stop | ZEC | UP | 0.67 | 0.42 | -2.84 |
| 10-06 01:32 | +20 | ZEC | UP | 0.67 | open |  |
| 10-06 01:32 | +15 | ZEC | UP | 0.67 | open |  |
| 10-06 01:32 | +10 | ZEC | UP | 0.67 | open |  |
| 10-06 01:32 | +5 | ZEC | UP | 0.67 | open |  |
| 10-06 01:32 | +5 | DOGE | UP | 0.62 | 0.71 | 0.59 |
| 10-06 01:31 | +10 stop | SOL | DOWN | 0.71 | 0.54 | -2.03 |
| 10-06 01:31 | +20 | SOL | DOWN | 0.71 | 0.92 | 1.86 |
| 10-06 01:31 | +15 | SOL | DOWN | 0.71 | 0.87 | 1.37 |
| 10-06 01:31 | +10 | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 10-06 01:31 | +5 | SOL | DOWN | 0.71 | 0.78 | 0.42 |
| 10-06 01:31 | +10 stop | BNB | DOWN | 0.68 | 0.79 | 0.78 |
| 10-06 01:31 | +20 | BNB | DOWN | 0.68 | 0.91 | 2.08 |
| 10-06 01:31 | +15 | BNB | DOWN | 0.68 | 0.91 | 2.08 |
| 10-06 01:31 | +10 | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 10-06 01:31 | +5 | BNB | DOWN | 0.68 | 0.75 | 0.40 |
| 10-06 01:31 | +10 stop | DOGE | DOWN | 0.58 | 0.42 | -1.96 |
| 10-06 01:31 | +20 | DOGE | DOWN | 0.58 | 0.80 | 1.90 |
