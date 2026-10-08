# Range-Scalp Bot

*Updated Thu Oct 08 23:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8159 | 7053 | 1106 (13) | 1 | $-2696.20 | -5.2% |
| **+10¢** | 6177 | 4870 | 1307 (25) | 1 | $-2663.02 | -6.8% |
| **+15¢** | 5203 | 3828 | 1375 (37) | 1 | $-2178.68 | -6.7% |
| **+20¢** | 4644 | 3217 | 1427 (45) | 1 | $-1774.46 | -6.1% |
| **+10¢ (15¢ stop)** | 9918 | 9888 | 30 (19) | 1 | $-3688.41 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 23:30 | +10 stop | BTC | UP | 0.68 | open |  |
| 10-08 23:30 | +20 | BTC | UP | 0.68 | open |  |
| 10-08 23:30 | +15 | BTC | UP | 0.68 | open |  |
| 10-08 23:30 | +10 | BTC | UP | 0.67 | open |  |
| 10-08 23:30 | +5 | BTC | UP | 0.67 | open |  |
| 10-08 23:28 | +5 | DOGE | UP | 0.42 | 0.51 | 0.54 |
| 10-08 23:28 | +10 stop | DOGE | UP | 0.54 | 0.37 | -2.05 |
| 10-08 23:27 | +10 stop | NEAR | UP | 0.67 | 0.51 | -1.94 |
| 10-08 23:27 | +10 | NEAR | UP | 0.67 | 0.97 | 2.83 |
| 10-08 23:27 | +5 | NEAR | UP | 0.67 | 0.97 | 2.83 |
| 10-08 23:27 | +5 | DOGE | UP | 0.55 | 0.63 | 0.45 |
| 10-08 23:26 | +10 stop | DOGE | UP | 0.59 | 0.43 | -1.95 |
| 10-08 23:26 | +15 | DOGE | UP | 0.59 | no | -6.07 |
| 10-08 23:26 | +10 | DOGE | UP | 0.59 | no | -6.07 |
| 10-08 23:26 | +5 | DOGE | UP | 0.59 | 0.66 | 0.37 |
| 10-08 23:24 | +10 stop | NEAR | UP | 0.65 | 0.49 | -1.94 |
| 10-08 23:24 | +15 | NEAR | UP | 0.65 | 0.97 | 3.03 |
| 10-08 23:24 | +10 stop | DOGE | UP | 0.52 | 0.35 | -2.04 |
| 10-08 23:24 | +20 | DOGE | UP | 0.51 | no | -5.28 |
| 10-08 23:24 | +15 | DOGE | UP | 0.51 | 0.70 | 1.57 |
| 10-08 23:24 | +10 | DOGE | UP | 0.52 | 0.70 | 1.47 |
| 10-08 23:24 | +5 | DOGE | UP | 0.52 | 0.61 | 0.55 |
| 10-08 23:21 | +10 stop | NEAR | UP | 0.71 | 0.81 | 0.74 |
| 10-08 23:21 | +10 stop | BNB | UP | 0.66 | 0.82 | 1.33 |
| 10-08 23:20 | +10 stop | NEAR | DOWN | 0.53 | 0.34 | -2.23 |
| 10-08 23:20 | +10 | NEAR | DOWN | 0.53 | 0.64 | 0.76 |
| 10-08 23:20 | +5 | NEAR | DOWN | 0.53 | 0.64 | 0.75 |
| 10-08 23:20 | +10 stop | HYPE | UP | 0.61 | 0.78 | 1.40 |
| 10-08 23:19 | +10 stop | SOL | DOWN | 0.50 | 0.30 | -2.33 |
| 10-08 23:19 | +10 stop | ETH | DOWN | 0.50 | 0.23 | -3.01 |
| 10-08 23:19 | +10 stop | BTC | DOWN | 0.54 | 0.33 | -2.44 |
| 10-08 23:19 | +5 | NEAR | UP | 0.65 | 0.73 | 0.50 |
| 10-08 23:19 | +10 stop | BNB | DOWN | 0.68 | 0.52 | -1.94 |
| 10-08 23:19 | +20 | BNB | DOWN | 0.68 | yes | -6.96 |
| 10-08 23:19 | +15 | BNB | DOWN | 0.68 | yes | -6.96 |
| 10-08 23:19 | +10 | BNB | DOWN | 0.68 | yes | -6.96 |
| 10-08 23:19 | +5 | BNB | DOWN | 0.68 | yes | -6.96 |
| 10-08 23:18 | +5 | XRP | UP | 0.71 | 0.76 | 0.22 |
| 10-08 23:17 | +10 stop | BTC | UP | 0.62 | 0.44 | -2.15 |
| 10-08 23:17 | +20 | BTC | UP | 0.62 | 0.83 | 1.83 |
