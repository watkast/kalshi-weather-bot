# Range-Scalp Bot

*Updated Fri Oct 23 03:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29724 | 25870 | 3854 (39) | 1 | $-8798.73 | -4.7% |
| **+10¢** | 22282 | 17821 | 4461 (55) | 1 | $-7927.27 | -5.7% |
| **+15¢** | 18662 | 13873 | 4789 (78) | 1 | $-7097.00 | -6.1% |
| **+20¢** | 16516 | 11498 | 5018 (100) | 1 | $-6420.52 | -6.2% |
| **+10¢ (15¢ stop)** | 36469 | 36410 | 59 (32) | 1 | $-13739.18 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 03:55 | +10 stop | NEAR | DOWN | 0.65 | open |  |
| 10-23 03:53 | +10 stop | NEAR | DOWN | 0.58 | 0.69 | 0.73 |
| 10-23 03:52 | +10 stop | NEAR | DOWN | 0.55 | 0.37 | -2.15 |
| 10-23 03:51 | +10 stop | DOGE | UP | 0.70 | 0.84 | 1.15 |
| 10-23 03:51 | +10 | DOGE | UP | 0.70 | 0.84 | 1.15 |
| 10-23 03:51 | +5 | DOGE | UP | 0.70 | 0.84 | 1.15 |
| 10-23 03:49 | +5 | SOL | UP | 0.60 | 0.80 | 1.71 |
| 10-23 03:49 | +10 stop | NEAR | DOWN | 0.63 | 0.73 | 0.69 |
| 10-23 03:49 | +5 | SOL | UP | 0.62 | 0.69 | 0.38 |
| 10-23 03:47 | +5 | DOGE | UP | 0.66 | 0.75 | 0.60 |
| 10-23 03:46 | +10 stop | DOGE | UP | 0.63 | 0.75 | 0.89 |
| 10-23 03:46 | +20 | DOGE | UP | 0.63 | 0.84 | 1.83 |
| 10-23 03:46 | +15 | DOGE | UP | 0.63 | 0.84 | 1.83 |
| 10-23 03:46 | +10 | DOGE | UP | 0.63 | 0.75 | 0.89 |
| 10-23 03:46 | +5 | DOGE | UP | 0.63 | 0.68 | 0.17 |
| 10-23 03:46 | +10 stop | NEAR | UP | 0.69 | 0.47 | -2.53 |
| 10-23 03:46 | +20 | NEAR | UP | 0.69 | open |  |
| 10-23 03:46 | +15 | NEAR | UP | 0.69 | open |  |
| 10-23 03:46 | +10 | NEAR | UP | 0.69 | open |  |
| 10-23 03:46 | +5 | NEAR | UP | 0.69 | open |  |
| 10-23 03:45 | +10 stop | SOL | UP | 0.66 | 0.50 | -1.94 |
| 10-23 03:45 | +20 | SOL | UP | 0.66 | 0.90 | 2.20 |
| 10-23 03:45 | +15 | SOL | UP | 0.66 | 0.81 | 1.23 |
| 10-23 03:45 | +10 | SOL | UP | 0.66 | 0.80 | 1.12 |
| 10-23 03:45 | +5 | SOL | UP | 0.66 | 0.71 | 0.19 |
| 10-23 03:45 | +10 stop | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 10-23 03:45 | +20 | HYPE | UP | 0.65 | 0.89 | 2.17 |
| 10-23 03:45 | +15 | HYPE | UP | 0.65 | 0.83 | 1.54 |
| 10-23 03:45 | +10 | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 10-23 03:45 | +5 | HYPE | UP | 0.65 | 0.70 | 0.19 |
| 10-23 03:43 | +10 stop | ZEC | DOWN | 0.07 | 0.58 | 4.88 |
| 10-23 03:41 | +10 stop | NEAR | DOWN | 0.42 | 0.59 | 1.31 |
| 10-23 03:41 | +10 stop | ZEC | UP | 0.59 | 0.25 | -3.71 |
| 10-23 03:41 | +10 | ZEC | UP | 0.59 | 0.95 | 3.35 |
| 10-23 03:41 | +5 | ZEC | UP | 0.61 | 0.95 | 3.16 |
| 10-23 03:41 | +10 stop | ETH | DOWN | 0.59 | 0.72 | 0.98 |
| 10-23 03:40 | +5 | ETH | DOWN | 0.64 | 0.72 | 0.48 |
| 10-23 03:40 | +10 stop | HYPE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-23 03:39 | +10 stop | DOGE | DOWN | 0.68 | 0.44 | -2.74 |
| 10-23 03:39 | +5 | DOGE | DOWN | 0.68 | yes | -6.96 |
