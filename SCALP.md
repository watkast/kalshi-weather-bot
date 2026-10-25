# Range-Scalp Bot

*Updated Sun Oct 25 04:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32582 | 28410 | 4172 (42) | 3 | $-9284.61 | -4.5% |
| **+10¢** | 24388 | 19556 | 4832 (60) | 2 | $-8317.43 | -5.4% |
| **+15¢** | 20420 | 15222 | 5198 (83) | 2 | $-7465.35 | -5.8% |
| **+20¢** | 18089 | 12649 | 5440 (105) | 2 | $-6607.36 | -5.8% |
| **+10¢ (15¢ stop)** | 40033 | 39973 | 60 (32) | 0 | $-15309.89 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 04:37 | +10 stop | XRP | UP | 0.69 | 0.79 | 0.73 |
| 10-25 04:37 | +5 | XRP | UP | 0.68 | 0.79 | 0.82 |
| 10-25 04:37 | +5 | XRP | DOWN | 0.43 | 0.59 | 1.25 |
| 10-25 04:36 | +10 stop | NEAR | UP | 0.63 | 0.81 | 1.52 |
| 10-25 04:36 | +15 | NEAR | UP | 0.63 | 0.81 | 1.52 |
| 10-25 04:36 | +10 | NEAR | UP | 0.63 | 0.81 | 1.52 |
| 10-25 04:36 | +10 stop | XRP | DOWN | 0.60 | 0.41 | -2.24 |
| 10-25 04:36 | +20 | XRP | DOWN | 0.60 | open |  |
| 10-25 04:36 | +15 | XRP | DOWN | 0.60 | open |  |
| 10-25 04:36 | +10 | XRP | DOWN | 0.60 | open |  |
| 10-25 04:36 | +5 | XRP | DOWN | 0.60 | 0.65 | 0.17 |
| 10-25 04:35 | +10 stop | ZEC | DOWN | 0.58 | 0.32 | -2.94 |
| 10-25 04:34 | +10 stop | SOL | DOWN | 0.60 | 0.38 | -2.51 |
| 10-25 04:34 | +5 | NEAR | DOWN | 0.57 | open |  |
| 10-25 04:34 | +5 | SOL | DOWN | 0.60 | open |  |
| 10-25 04:34 | +5 | SOL | UP | 0.40 | 0.57 | 1.35 |
| 10-25 04:34 | +10 stop | BNB | UP | 0.59 | 0.73 | 1.09 |
| 10-25 04:34 | +10 stop | NEAR | UP | 0.46 | 0.61 | 1.15 |
| 10-25 04:34 | +20 | NEAR | UP | 0.46 | 0.81 | 3.21 |
| 10-25 04:34 | +15 | NEAR | UP | 0.46 | 0.61 | 1.15 |
| 10-25 04:34 | +10 | NEAR | UP | 0.46 | 0.61 | 1.15 |
| 10-25 04:34 | +5 | NEAR | UP | 0.46 | 0.53 | 0.34 |
| 10-25 04:33 | +10 stop | BNB | DOWN | 0.61 | 0.45 | -1.95 |
| 10-25 04:33 | +20 | BNB | DOWN | 0.61 | open |  |
| 10-25 04:33 | +15 | BNB | DOWN | 0.61 | open |  |
| 10-25 04:33 | +10 | BNB | DOWN | 0.61 | open |  |
| 10-25 04:33 | +5 | BNB | DOWN | 0.61 | open |  |
| 10-25 04:32 | +10 stop | BTC | UP | 0.58 | 0.70 | 0.87 |
| 10-25 04:32 | +5 | DOGE | UP | 0.64 | 0.72 | 0.48 |
| 10-25 04:32 | +10 stop | ETH | UP | 0.59 | 0.77 | 1.50 |
| 10-25 04:31 | +10 stop | BTC | UP | 0.71 | 0.56 | -1.83 |
| 10-25 04:31 | +20 | BTC | UP | 0.71 | 0.93 | 1.95 |
| 10-25 04:31 | +15 | BTC | UP | 0.71 | 0.86 | 1.26 |
| 10-25 04:31 | +10 | BTC | UP | 0.71 | 0.85 | 1.16 |
| 10-25 04:31 | +5 | BTC | UP | 0.71 | 0.77 | 0.32 |
| 10-25 04:31 | +10 stop | SOL | UP | 0.53 | 0.38 | -1.85 |
| 10-25 04:31 | +20 | SOL | UP | 0.53 | 0.86 | 3.03 |
| 10-25 04:31 | +15 | SOL | UP | 0.53 | 0.70 | 1.37 |
| 10-25 04:31 | +10 | SOL | UP | 0.53 | 0.70 | 1.37 |
| 10-25 04:31 | +5 | SOL | UP | 0.53 | 0.59 | 0.25 |
