# Range-Scalp Bot

*Updated Sun Oct 04 00:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 1489 | 1296 | 193 (2) | 5 | $-431.14 | -4.6% |
| **+10¢** | 1145 | 930 | 215 (4) | 5 | $-275.65 | -3.8% |
| **+15¢** | 966 | 735 | 231 (5) | 5 | $-231.71 | -3.8% |
| **+20¢** | 854 | 605 | 249 (7) | 5 | $-246.75 | -4.6% |
| **+10¢ (15¢ stop)** | 1877 | 1876 | 1 (1) | 0 | $-781.11 | -6.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 00:23 | +10 stop | BNB | UP | 0.62 | 0.31 | -3.41 |
| 10-04 00:21 | +10 stop | BTC | UP | 0.70 | 0.84 | 1.15 |
| 10-04 00:21 | +10 stop | NEAR | UP | 0.63 | 0.85 | 1.94 |
| 10-04 00:20 | +10 stop | NEAR | DOWN | 0.29 | 0.56 | 2.37 |
| 10-04 00:18 | +10 stop | NEAR | UP | 0.62 | 0.44 | -2.13 |
| 10-04 00:18 | +10 stop | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 10-04 00:17 | +10 stop | SOL | UP | 0.64 | 0.74 | 0.69 |
| 10-04 00:17 | +10 stop | BNB | UP | 0.67 | 0.48 | -2.24 |
| 10-04 00:17 | +10 stop | BTC | UP | 0.60 | 0.79 | 1.61 |
| 10-04 00:17 | +10 stop | XRP | UP | 0.68 | 0.80 | 0.92 |
| 10-04 00:17 | +20 | XRP | UP | 0.68 | 0.88 | 1.76 |
| 10-04 00:17 | +15 | XRP | UP | 0.68 | 0.84 | 1.34 |
| 10-04 00:17 | +10 | XRP | UP | 0.68 | 0.80 | 0.92 |
| 10-04 00:17 | +5 | XRP | UP | 0.68 | 0.73 | 0.20 |
| 10-04 00:17 | +5 | NEAR | DOWN | 0.58 | open |  |
| 10-04 00:17 | +10 stop | ETH | UP | 0.66 | 0.76 | 0.71 |
| 10-04 00:17 | +20 | ETH | UP | 0.66 | 0.86 | 1.75 |
| 10-04 00:17 | +15 | ETH | UP | 0.66 | 0.85 | 1.65 |
| 10-04 00:17 | +10 | ETH | UP | 0.66 | 0.76 | 0.71 |
| 10-04 00:17 | +5 | ETH | UP | 0.66 | 0.75 | 0.60 |
| 10-04 00:16 | +10 stop | ZEC | DOWN | 0.52 | 0.33 | -2.24 |
| 10-04 00:16 | +20 | ZEC | DOWN | 0.52 | open |  |
| 10-04 00:16 | +15 | ZEC | DOWN | 0.52 | open |  |
| 10-04 00:16 | +10 | ZEC | DOWN | 0.52 | open |  |
| 10-04 00:16 | +5 | ZEC | DOWN | 0.52 | open |  |
| 10-04 00:16 | +10 stop | DOGE | DOWN | 0.56 | 0.39 | -2.07 |
| 10-04 00:16 | +20 | DOGE | DOWN | 0.56 | open |  |
| 10-04 00:16 | +15 | DOGE | DOWN | 0.56 | open |  |
| 10-04 00:16 | +10 | DOGE | DOWN | 0.56 | open |  |
| 10-04 00:16 | +5 | DOGE | DOWN | 0.56 | open |  |
| 10-04 00:15 | +10 stop | NEAR | DOWN | 0.66 | 0.46 | -2.34 |
| 10-04 00:15 | +20 | NEAR | DOWN | 0.66 | open |  |
| 10-04 00:15 | +15 | NEAR | DOWN | 0.66 | open |  |
| 10-04 00:15 | +10 | NEAR | DOWN | 0.66 | open |  |
| 10-04 00:15 | +5 | NEAR | DOWN | 0.65 | 0.73 | 0.48 |
| 10-04 00:15 | +10 stop | BNB | DOWN | 0.67 | 0.42 | -2.84 |
| 10-04 00:15 | +20 | BNB | DOWN | 0.67 | 0.87 | 1.76 |
| 10-04 00:15 | +15 | BNB | DOWN | 0.67 | 0.86 | 1.65 |
| 10-04 00:15 | +10 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-04 00:15 | +5 | BNB | DOWN | 0.67 | 0.72 | 0.19 |
