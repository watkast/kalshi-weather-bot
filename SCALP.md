# Range-Scalp Bot

*Updated Wed Oct 14 20:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16491 | 14288 | 2203 (28) | 2 | $-5209.89 | -5.0% |
| **+10¢** | 12478 | 9924 | 2554 (40) | 1 | $-4789.03 | -6.1% |
| **+15¢** | 10488 | 7748 | 2740 (59) | 0 | $-4277.29 | -6.5% |
| **+20¢** | 9320 | 6447 | 2873 (76) | 4 | $-3801.91 | -6.5% |
| **+10¢ (15¢ stop)** | 20316 | 20266 | 50 (29) | 0 | $-7856.72 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 20:36 | +5 | XRP | DOWN | 0.67 | 0.73 | 0.30 |
| 10-14 20:35 | +10 stop | ETH | DOWN | 0.57 | 0.76 | 1.59 |
| 10-14 20:35 | +5 | ETH | DOWN | 0.57 | 0.62 | 0.15 |
| 10-14 20:35 | +10 stop | DOGE | DOWN | 0.57 | 0.70 | 0.97 |
| 10-14 20:35 | +15 | DOGE | DOWN | 0.57 | 0.73 | 1.28 |
| 10-14 20:35 | +10 stop | BTC | DOWN | 0.63 | 0.76 | 1.00 |
| 10-14 20:35 | +10 | BTC | DOWN | 0.63 | 0.76 | 1.00 |
| 10-14 20:35 | +10 stop | XRP | DOWN | 0.54 | 0.66 | 0.86 |
| 10-14 20:35 | +5 | XRP | DOWN | 0.54 | 0.59 | 0.15 |
| 10-14 20:35 | +10 stop | SOL | DOWN | 0.70 | 0.83 | 1.05 |
| 10-14 20:35 | +10 stop | HYPE | DOWN | 0.69 | 0.81 | 0.90 |
| 10-14 20:35 | +10 stop | BNB | DOWN | 0.60 | 0.71 | 0.78 |
| 10-14 20:35 | +10 stop | DOGE | UP | 0.57 | 0.34 | -2.64 |
| 10-14 20:35 | +10 | DOGE | UP | 0.57 | open |  |
| 10-14 20:35 | +5 | DOGE | UP | 0.57 | open |  |
| 10-14 20:34 | +10 stop | ETH | UP | 0.64 | 0.38 | -2.94 |
| 10-14 20:34 | +10 stop | BTC | UP | 0.62 | 0.34 | -3.13 |
| 10-14 20:34 | +10 stop | SOL | UP | 0.64 | 0.40 | -2.74 |
| 10-14 20:34 | +5 | NEAR | DOWN | 0.58 | 0.78 | 1.69 |
| 10-14 20:34 | +5 | BTC | UP | 0.64 | open |  |
| 10-14 20:33 | +10 stop | BNB | DOWN | 0.57 | 0.40 | -2.05 |
| 10-14 20:33 | +20 | BNB | DOWN | 0.57 | 0.80 | 2.00 |
| 10-14 20:33 | +15 | BNB | DOWN | 0.57 | 0.74 | 1.38 |
| 10-14 20:33 | +10 | BNB | DOWN | 0.57 | 0.71 | 1.07 |
| 10-14 20:33 | +5 | BNB | DOWN | 0.57 | 0.71 | 1.07 |
| 10-14 20:33 | +5 | ETH | DOWN | 0.53 | 0.61 | 0.45 |
| 10-14 20:33 | +10 stop | ETH | DOWN | 0.57 | 0.29 | -3.13 |
| 10-14 20:33 | +20 | ETH | DOWN | 0.57 | open |  |
| 10-14 20:33 | +15 | ETH | DOWN | 0.57 | 0.76 | 1.59 |
| 10-14 20:33 | +10 | ETH | DOWN | 0.57 | 0.76 | 1.59 |
| 10-14 20:33 | +5 | ETH | DOWN | 0.57 | 0.64 | 0.35 |
| 10-14 20:33 | +10 stop | NEAR | DOWN | 0.67 | 0.78 | 0.81 |
| 10-14 20:33 | +20 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 10-14 20:33 | +15 | NEAR | DOWN | 0.67 | 0.82 | 1.23 |
| 10-14 20:33 | +10 | NEAR | DOWN | 0.67 | 0.78 | 0.81 |
| 10-14 20:33 | +5 | NEAR | DOWN | 0.67 | 0.73 | 0.30 |
| 10-14 20:33 | +10 stop | SOL | DOWN | 0.62 | 0.43 | -2.25 |
| 10-14 20:33 | +20 | SOL | DOWN | 0.62 | 0.83 | 1.83 |
| 10-14 20:33 | +15 | SOL | DOWN | 0.62 | 0.83 | 1.83 |
| 10-14 20:33 | +10 | SOL | DOWN | 0.62 | 0.76 | 1.10 |
