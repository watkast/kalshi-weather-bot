# Range-Scalp Bot

*Updated Thu Oct 22 11:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28654 | 24969 | 3685 (39) | 3 | $-8239.94 | -4.6% |
| **+10¢** | 21507 | 17242 | 4265 (55) | 3 | $-7338.52 | -5.4% |
| **+15¢** | 18005 | 13418 | 4587 (78) | 1 | $-6560.46 | -5.8% |
| **+20¢** | 15930 | 11119 | 4811 (100) | 1 | $-5916.33 | -5.9% |
| **+10¢ (15¢ stop)** | 35155 | 35096 | 59 (32) | 0 | $-13169.82 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 11:27 | +10 stop | NEAR | DOWN | 0.69 | 0.29 | -4.30 |
| 10-22 11:27 | +10 | NEAR | DOWN | 0.69 | open |  |
| 10-22 11:27 | +5 | NEAR | DOWN | 0.69 | open |  |
| 10-22 11:27 | +10 stop | NEAR | UP | 0.52 | 0.65 | 0.96 |
| 10-22 11:27 | +20 | NEAR | UP | 0.52 | 0.96 | 4.20 |
| 10-22 11:27 | +15 | NEAR | UP | 0.52 | 0.67 | 1.16 |
| 10-22 11:27 | +10 | NEAR | UP | 0.53 | 0.65 | 0.84 |
| 10-22 11:27 | +5 | NEAR | UP | 0.52 | 0.65 | 0.96 |
| 10-22 11:23 | +5 | ZEC | DOWN | 0.63 | open |  |
| 10-22 11:23 | +10 stop | HYPE | DOWN | 0.69 | 0.84 | 1.27 |
| 10-22 11:23 | +20 | HYPE | DOWN | 0.69 | 0.99 | 2.90 |
| 10-22 11:23 | +15 | HYPE | DOWN | 0.69 | 0.84 | 1.27 |
| 10-22 11:22 | +10 stop | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-22 11:22 | +20 | XRP | DOWN | 0.71 | 0.92 | 1.91 |
| 10-22 11:22 | +15 | XRP | DOWN | 0.71 | 0.88 | 1.47 |
| 10-22 11:22 | +10 | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-22 11:22 | +5 | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-22 11:22 | +10 stop | SOL | DOWN | 0.65 | 0.84 | 1.64 |
| 10-22 11:22 | +5 | SOL | DOWN | 0.65 | 0.70 | 0.19 |
| 10-22 11:21 | +10 stop | DOGE | UP | 0.56 | 0.71 | 1.17 |
| 10-22 11:21 | +20 | DOGE | UP | 0.56 | 0.78 | 1.89 |
| 10-22 11:21 | +15 | DOGE | UP | 0.56 | 0.71 | 1.17 |
| 10-22 11:21 | +10 | DOGE | UP | 0.56 | 0.71 | 1.17 |
| 10-22 11:21 | +5 | DOGE | UP | 0.56 | 0.71 | 1.17 |
| 10-22 11:21 | +10 stop | ZEC | DOWN | 0.67 | 0.51 | -1.94 |
| 10-22 11:20 | +10 stop | NEAR | DOWN | 0.66 | 0.76 | 0.71 |
| 10-22 11:20 | +10 stop | SOL | UP | 0.64 | 0.42 | -2.55 |
| 10-22 11:20 | +10 stop | BNB | DOWN | 0.69 | 0.83 | 1.15 |
| 10-22 11:20 | +15 | BNB | DOWN | 0.69 | 0.88 | 1.67 |
| 10-22 11:20 | +10 | BNB | DOWN | 0.69 | 0.83 | 1.15 |
| 10-22 11:20 | +5 | BNB | DOWN | 0.69 | 0.76 | 0.42 |
| 10-22 11:20 | +10 stop | ETH | UP | 0.49 | 0.33 | -1.94 |
| 10-22 11:18 | +10 stop | HYPE | UP | 0.61 | 0.44 | -2.05 |
| 10-22 11:18 | +10 | HYPE | UP | 0.61 | open |  |
| 10-22 11:18 | +5 | HYPE | UP | 0.61 | open |  |
| 10-22 11:18 | +10 stop | NEAR | DOWN | 0.56 | 0.40 | -1.95 |
| 10-22 11:17 | +10 stop | DOGE | UP | 0.58 | 0.71 | 0.97 |
| 10-22 11:17 | +20 | DOGE | UP | 0.59 | 0.79 | 1.71 |
| 10-22 11:17 | +15 | DOGE | UP | 0.59 | 0.75 | 1.29 |
| 10-22 11:17 | +10 | DOGE | UP | 0.59 | 0.71 | 0.88 |
