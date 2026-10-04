# Range-Scalp Bot

*Updated Sun Oct 04 19:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2708 | 2333 | 375 (3) | 3 | $-903.63 | -5.3% |
| **+10¢** | 2111 | 1690 | 421 (4) | 6 | $-732.66 | -5.5% |
| **+15¢** | 1774 | 1333 | 441 (5) | 6 | $-587.89 | -5.3% |
| **+20¢** | 1579 | 1115 | 464 (9) | 7 | $-508.17 | -5.1% |
| **+10¢ (15¢ stop)** | 3374 | 3373 | 1 (1) | 0 | $-1283.38 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 19:41 | +10 stop | NEAR | UP | 0.44 | 0.24 | -2.30 |
| 10-04 19:41 | +20 | NEAR | UP | 0.44 | open |  |
| 10-04 19:41 | +15 | NEAR | UP | 0.44 | open |  |
| 10-04 19:41 | +10 | NEAR | UP | 0.44 | open |  |
| 10-04 19:41 | +5 | NEAR | UP | 0.44 | 0.52 | 0.45 |
| 10-04 19:41 | +10 stop | HYPE | DOWN | 0.65 | 0.83 | 1.54 |
| 10-04 19:41 | +10 stop | BNB | UP | 0.64 | 0.79 | 1.21 |
| 10-04 19:41 | +20 | BNB | UP | 0.64 | open |  |
| 10-04 19:41 | +15 | BNB | UP | 0.64 | 0.79 | 1.21 |
| 10-04 19:41 | +10 | BNB | UP | 0.64 | 0.79 | 1.21 |
| 10-04 19:41 | +5 | BNB | UP | 0.64 | 0.72 | 0.48 |
| 10-04 19:39 | +10 stop | SOL | UP | 0.69 | 0.51 | -2.13 |
| 10-04 19:39 | +20 | SOL | UP | 0.69 | open |  |
| 10-04 19:39 | +15 | SOL | UP | 0.69 | open |  |
| 10-04 19:39 | +10 | SOL | UP | 0.69 | open |  |
| 10-04 19:39 | +5 | SOL | UP | 0.69 | 0.74 | 0.21 |
| 10-04 19:39 | +10 stop | NEAR | DOWN | 0.52 | 0.75 | 1.98 |
| 10-04 19:39 | +5 | ETH | UP | 0.59 | open |  |
| 10-04 19:39 | +10 stop | DOGE | UP | 0.66 | 0.49 | -2.02 |
| 10-04 19:39 | +20 | DOGE | UP | 0.66 | open |  |
| 10-04 19:39 | +15 | DOGE | UP | 0.65 | open |  |
| 10-04 19:39 | +10 | DOGE | UP | 0.65 | open |  |
| 10-04 19:39 | +5 | DOGE | UP | 0.64 | 0.73 | 0.55 |
| 10-04 19:37 | +10 stop | ETH | UP | 0.55 | 0.25 | -3.27 |
| 10-04 19:37 | +10 | ETH | UP | 0.55 | open |  |
| 10-04 19:37 | +5 | ETH | UP | 0.55 | 0.60 | 0.20 |
| 10-04 19:35 | +10 stop | XRP | UP | 0.54 | 0.31 | -2.63 |
| 10-04 19:34 | +10 stop | NEAR | UP | 0.56 | 0.40 | -1.95 |
| 10-04 19:33 | +10 stop | ETH | UP | 0.64 | 0.47 | -2.05 |
| 10-04 19:33 | +10 stop | SOL | UP | 0.71 | 0.56 | -1.83 |
| 10-04 19:33 | +15 | SOL | UP | 0.71 | 0.86 | 1.26 |
| 10-04 19:33 | +10 | SOL | UP | 0.71 | 0.81 | 0.74 |
| 10-04 19:33 | +5 | SOL | UP | 0.71 | 0.79 | 0.53 |
| 10-04 19:33 | +10 stop | XRP | UP | 0.67 | 0.45 | -2.54 |
| 10-04 19:33 | +10 | XRP | UP | 0.67 | open |  |
| 10-04 19:33 | +5 | XRP | UP | 0.67 | open |  |
| 10-04 19:32 | +10 stop | BNB | UP | 0.64 | 0.74 | 0.69 |
| 10-04 19:32 | +20 | BNB | UP | 0.64 | 0.86 | 1.94 |
| 10-04 19:32 | +15 | BNB | UP | 0.64 | 0.86 | 1.94 |
| 10-04 19:32 | +10 | BNB | UP | 0.64 | 0.74 | 0.69 |
