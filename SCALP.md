# Range-Scalp Bot

*Updated Fri Oct 16 07:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18794 | 16322 | 2472 (28) | 0 | $-5723.05 | -4.8% |
| **+10¢** | 14162 | 11302 | 2860 (40) | 1 | $-5197.46 | -5.8% |
| **+15¢** | 11875 | 8796 | 3079 (59) | 1 | $-4707.43 | -6.3% |
| **+20¢** | 10548 | 7326 | 3222 (78) | 1 | $-4132.48 | -6.2% |
| **+10¢ (15¢ stop)** | 23143 | 23093 | 50 (29) | 0 | $-8940.46 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 06:57 | +10 stop | NEAR | DOWN | 0.70 | 0.97 | 2.58 |
| 10-16 06:57 | +10 stop | DOGE | DOWN | 0.59 | 0.84 | 2.23 |
| 10-16 06:57 | +5 | DOGE | DOWN | 0.59 | 0.67 | 0.47 |
| 10-16 06:56 | +10 stop | ZEC | UP | 0.67 | 0.79 | 0.92 |
| 10-16 06:56 | +5 | ZEC | UP | 0.67 | 0.79 | 0.92 |
| 10-16 06:56 | +10 stop | XRP | UP | 0.53 | 0.33 | -2.35 |
| 10-16 06:55 | +10 stop | NEAR | UP | 0.57 | 0.70 | 1.01 |
| 10-16 06:55 | +5 | DOGE | UP | 0.64 | 0.75 | 0.79 |
| 10-16 06:55 | +10 stop | XRP | DOWN | 0.61 | 0.36 | -2.84 |
| 10-16 06:55 | +5 | XRP | DOWN | 0.61 | 0.74 | 0.99 |
| 10-16 06:55 | +10 stop | DOGE | UP | 0.59 | 0.75 | 1.27 |
| 10-16 06:55 | +5 | DOGE | UP | 0.59 | 0.69 | 0.66 |
| 10-16 06:53 | +10 stop | XRP | UP | 0.68 | 0.38 | -3.33 |
| 10-16 06:47 | +10 stop | NEAR | UP | 0.71 | 0.82 | 0.84 |
| 10-16 06:46 | +10 stop | BNB | UP | 0.69 | 0.80 | 0.83 |
| 10-16 06:46 | +20 | BNB | UP | 0.69 | 0.92 | 2.10 |
| 10-16 06:46 | +15 | BNB | UP | 0.69 | 0.87 | 1.57 |
| 10-16 06:46 | +10 | BNB | UP | 0.69 | 0.80 | 0.83 |
| 10-16 06:46 | +5 | BNB | UP | 0.69 | 0.74 | 0.21 |
| 10-16 06:46 | +10 stop | DOGE | DOWN | 0.57 | 0.26 | -3.42 |
| 10-16 06:46 | +20 | DOGE | DOWN | 0.57 | 0.84 | 2.42 |
| 10-16 06:46 | +15 | DOGE | DOWN | 0.57 | 0.84 | 2.42 |
| 10-16 06:46 | +10 | DOGE | DOWN | 0.57 | 0.67 | 0.66 |
| 10-16 06:46 | +5 | DOGE | DOWN | 0.57 | 0.63 | 0.25 |
| 10-16 06:46 | +10 stop | SOL | DOWN | 0.51 | 0.26 | -2.82 |
| 10-16 06:46 | +20 | SOL | DOWN | 0.51 | open |  |
| 10-16 06:46 | +15 | SOL | DOWN | 0.51 | open |  |
| 10-16 06:46 | +10 | SOL | DOWN | 0.51 | open |  |
| 10-16 06:46 | +5 | SOL | DOWN | 0.51 | 0.57 | 0.24 |
| 10-16 06:46 | +10 stop | XRP | DOWN | 0.51 | 0.26 | -2.82 |
| 10-16 06:46 | +20 | XRP | DOWN | 0.52 | 0.74 | 1.88 |
| 10-16 06:46 | +15 | XRP | DOWN | 0.52 | 0.74 | 1.88 |
| 10-16 06:46 | +10 | XRP | DOWN | 0.52 | 0.63 | 0.75 |
| 10-16 06:46 | +5 | XRP | DOWN | 0.52 | 0.59 | 0.35 |
| 10-16 06:46 | +10 stop | ZEC | DOWN | 0.54 | 0.31 | -2.63 |
| 10-16 06:46 | +20 | ZEC | DOWN | 0.54 | 0.76 | 1.89 |
| 10-16 06:46 | +15 | ZEC | DOWN | 0.54 | 0.76 | 1.89 |
| 10-16 06:46 | +10 | ZEC | DOWN | 0.54 | 0.76 | 1.89 |
| 10-16 06:46 | +5 | ZEC | DOWN | 0.54 | 0.63 | 0.55 |
| 10-16 06:45 | +10 stop | NEAR | DOWN | 0.64 | 0.39 | -2.81 |
