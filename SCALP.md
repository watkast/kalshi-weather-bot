# Range-Scalp Bot

*Updated Fri Oct 16 08:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18965 | 16478 | 2487 (28) | 0 | $-5722.27 | -4.8% |
| **+10¢** | 14287 | 11409 | 2878 (40) | 0 | $-5197.86 | -5.8% |
| **+15¢** | 11972 | 8879 | 3093 (59) | 0 | $-4666.57 | -6.2% |
| **+20¢** | 10623 | 7381 | 3242 (78) | 0 | $-4143.99 | -6.2% |
| **+10¢ (15¢ stop)** | 23332 | 23282 | 50 (29) | 0 | $-9012.86 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 08:27 | +10 stop | XRP | UP | 0.68 | 0.97 | 2.73 |
| 10-16 08:27 | +15 | XRP | UP | 0.68 | 0.97 | 2.73 |
| 10-16 08:27 | +10 stop | BNB | DOWN | 0.51 | 0.32 | -2.23 |
| 10-16 08:27 | +15 | BNB | DOWN | 0.51 | 0.75 | 2.09 |
| 10-16 08:27 | +10 | BNB | DOWN | 0.51 | 0.75 | 2.09 |
| 10-16 08:27 | +5 | BNB | DOWN | 0.52 | 0.75 | 2.03 |
| 10-16 08:26 | +10 stop | DOGE | UP | 0.48 | 0.63 | 1.15 |
| 10-16 08:26 | +20 | DOGE | UP | 0.48 | 0.94 | 4.39 |
| 10-16 08:26 | +15 | DOGE | UP | 0.48 | 0.63 | 1.15 |
| 10-16 08:26 | +10 | DOGE | UP | 0.48 | 0.63 | 1.15 |
| 10-16 08:26 | +5 | DOGE | UP | 0.48 | 0.63 | 1.15 |
| 10-16 08:26 | +10 stop | ETH | DOWN | 0.54 | 0.65 | 0.76 |
| 10-16 08:26 | +20 | ETH | DOWN | 0.54 | yes | -5.58 |
| 10-16 08:26 | +15 | ETH | DOWN | 0.54 | 0.72 | 1.47 |
| 10-16 08:26 | +10 | ETH | DOWN | 0.54 | 0.65 | 0.76 |
| 10-16 08:26 | +5 | ETH | DOWN | 0.54 | 0.65 | 0.76 |
| 10-16 08:25 | +10 stop | BNB | DOWN | 0.41 | 0.56 | 1.15 |
| 10-16 08:25 | +15 | BNB | DOWN | 0.41 | 0.56 | 1.15 |
| 10-16 08:25 | +10 | BNB | DOWN | 0.41 | 0.56 | 1.15 |
| 10-16 08:25 | +5 | BNB | DOWN | 0.41 | 0.56 | 1.15 |
| 10-16 08:25 | +10 stop | NEAR | DOWN | 0.48 | 0.31 | -2.03 |
| 10-16 08:24 | +10 stop | HYPE | DOWN | 0.60 | 0.25 | -3.85 |
| 10-16 08:24 | +10 stop | HYPE | UP | 0.43 | 0.54 | 0.74 |
| 10-16 08:23 | +10 stop | SOL | UP | 0.62 | 0.80 | 1.51 |
| 10-16 08:23 | +10 stop | NEAR | DOWN | 0.52 | 0.63 | 0.75 |
| 10-16 08:23 | +10 stop | ZEC | DOWN | 0.69 | 0.80 | 0.80 |
| 10-16 08:23 | +10 stop | XRP | DOWN | 0.64 | 0.46 | -2.15 |
| 10-16 08:22 | +5 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 10-16 08:22 | +10 stop | HYPE | UP | 0.70 | 0.54 | -1.93 |
| 10-16 08:21 | +10 stop | SOL | DOWN | 0.70 | 0.53 | -2.03 |
| 10-16 08:21 | +15 | SOL | DOWN | 0.70 | yes | -7.15 |
| 10-16 08:21 | +10 | SOL | DOWN | 0.70 | yes | -7.15 |
| 10-16 08:21 | +5 | SOL | DOWN | 0.70 | yes | -7.15 |
| 10-16 08:21 | +10 stop | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 10-16 08:21 | +10 | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 10-16 08:21 | +5 | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 10-16 08:21 | +10 stop | XRP | DOWN | 0.71 | 0.48 | -2.63 |
| 10-16 08:21 | +10 | XRP | DOWN | 0.71 | yes | -7.25 |
| 10-16 08:21 | +5 | XRP | DOWN | 0.71 | yes | -7.25 |
| 10-16 08:21 | +10 stop | NEAR | DOWN | 0.66 | 0.45 | -2.41 |
