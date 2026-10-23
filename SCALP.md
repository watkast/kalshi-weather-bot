# Range-Scalp Bot

*Updated Fri Oct 23 08:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30037 | 26155 | 3882 (39) | 3 | $-8799.72 | -4.7% |
| **+10¢** | 22518 | 18023 | 4495 (55) | 3 | $-7912.37 | -5.6% |
| **+15¢** | 18854 | 14022 | 4832 (78) | 5 | $-7121.29 | -6.0% |
| **+20¢** | 16692 | 11631 | 5061 (101) | 5 | $-6408.44 | -6.1% |
| **+10¢ (15¢ stop)** | 36843 | 36784 | 59 (32) | 1 | $-13848.77 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 08:56 | +20 | BNB | DOWN | 0.67 | open |  |
| 10-23 08:56 | +15 | BNB | DOWN | 0.67 | open |  |
| 10-23 08:56 | +10 stop | SOL | DOWN | 0.71 | 0.53 | -2.13 |
| 10-23 08:56 | +10 stop | HYPE | UP | 0.67 | 0.79 | 0.92 |
| 10-23 08:56 | +20 | HYPE | UP | 0.67 | 0.95 | 2.57 |
| 10-23 08:56 | +15 | HYPE | UP | 0.66 | 0.95 | 2.67 |
| 10-23 08:56 | +10 | HYPE | UP | 0.66 | 0.79 | 1.02 |
| 10-23 08:56 | +5 | HYPE | UP | 0.66 | 0.79 | 1.02 |
| 10-23 08:56 | +10 stop | BNB | DOWN | 0.65 | open |  |
| 10-23 08:56 | +10 | BNB | DOWN | 0.65 | open |  |
| 10-23 08:56 | +10 stop | SOL | UP | 0.42 | 0.55 | 0.94 |
| 10-23 08:55 | +5 | BNB | UP | 0.56 | open |  |
| 10-23 08:55 | +5 | ZEC | DOWN | 0.53 | 0.66 | 0.96 |
| 10-23 08:55 | +10 stop | ZEC | DOWN | 0.62 | 0.73 | 0.79 |
| 10-23 08:55 | +10 | ZEC | DOWN | 0.62 | 0.73 | 0.79 |
| 10-23 08:55 | +5 | ZEC | DOWN | 0.62 | 0.68 | 0.27 |
| 10-23 08:54 | +10 stop | BNB | UP | 0.62 | 0.41 | -2.44 |
| 10-23 08:54 | +5 | BNB | UP | 0.62 | 0.67 | 0.17 |
| 10-23 08:53 | +10 stop | ZEC | DOWN | 0.54 | 0.65 | 0.76 |
| 10-23 08:53 | +10 | ZEC | DOWN | 0.55 | 0.65 | 0.66 |
| 10-23 08:53 | +5 | ZEC | DOWN | 0.55 | 0.65 | 0.66 |
| 10-23 08:53 | +10 stop | SOL | UP | 0.69 | 0.53 | -1.93 |
| 10-23 08:53 | +20 | SOL | UP | 0.69 | open |  |
| 10-23 08:53 | +15 | SOL | UP | 0.70 | open |  |
| 10-23 08:53 | +10 | SOL | UP | 0.64 | open |  |
| 10-23 08:53 | +5 | SOL | UP | 0.64 | open |  |
| 10-23 08:53 | +10 stop | NEAR | UP | 0.58 | 0.35 | -2.64 |
| 10-23 08:53 | +20 | NEAR | UP | 0.58 | open |  |
| 10-23 08:53 | +15 | NEAR | UP | 0.57 | open |  |
| 10-23 08:53 | +10 | NEAR | UP | 0.57 | open |  |
| 10-23 08:53 | +5 | NEAR | UP | 0.57 | open |  |
| 10-23 08:53 | +10 stop | BNB | UP | 0.56 | 0.68 | 0.86 |
| 10-23 08:53 | +5 | BNB | UP | 0.56 | 0.68 | 0.86 |
| 10-23 08:51 | +5 | ETH | UP | 0.64 | 0.70 | 0.28 |
| 10-23 08:50 | +10 stop | ZEC | UP | 0.71 | 0.83 | 0.95 |
| 10-23 08:50 | +20 | ZEC | UP | 0.71 | open |  |
| 10-23 08:50 | +15 | ZEC | UP | 0.71 | open |  |
| 10-23 08:50 | +10 | ZEC | UP | 0.71 | 0.83 | 0.95 |
| 10-23 08:50 | +5 | ZEC | UP | 0.71 | 0.83 | 0.95 |
| 10-23 08:49 | +5 | BNB | UP | 0.66 | 0.74 | 0.50 |
