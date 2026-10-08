# Range-Scalp Bot

*Updated Thu Oct 08 15:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7641 | 6626 | 1015 (13) | 2 | $-2347.53 | -4.9% |
| **+10¢** | 5794 | 4595 | 1199 (24) | 4 | $-2281.67 | -6.3% |
| **+15¢** | 4869 | 3607 | 1262 (32) | 4 | $-1863.71 | -6.1% |
| **+20¢** | 4351 | 3042 | 1309 (40) | 4 | $-1449.58 | -5.3% |
| **+10¢ (15¢ stop)** | 9275 | 9246 | 29 (18) | 0 | $-3378.59 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 15:43 | +10 stop | SOL | UP | 0.64 | 0.95 | 2.89 |
| 10-08 15:43 | +10 stop | BNB | UP | 0.69 | 0.92 | 2.04 |
| 10-08 15:43 | +5 | BNB | UP | 0.69 | 0.92 | 2.04 |
| 10-08 15:43 | +10 stop | SOL | DOWN | 0.41 | 0.68 | 2.37 |
| 10-08 15:42 | +10 stop | BNB | UP | 0.40 | 0.53 | 0.95 |
| 10-08 15:42 | +5 | BNB | UP | 0.40 | 0.53 | 0.95 |
| 10-08 15:42 | +10 stop | SOL | DOWN | 0.33 | 0.57 | 2.06 |
| 10-08 15:41 | +10 stop | XRP | DOWN | 0.59 | 0.79 | 1.71 |
| 10-08 15:41 | +10 stop | SOL | UP | 0.62 | 0.38 | -2.74 |
| 10-08 15:41 | +20 | SOL | UP | 0.62 | 0.95 | 3.09 |
| 10-08 15:41 | +10 | SOL | UP | 0.62 | 0.95 | 3.09 |
| 10-08 15:41 | +10 stop | BNB | DOWN | 0.57 | 0.76 | 1.60 |
| 10-08 15:40 | +15 | ZEC | DOWN | 0.70 | 0.97 | 2.54 |
| 10-08 15:40 | +10 | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-08 15:40 | +10 stop | XRP | UP | 0.59 | 0.34 | -2.83 |
| 10-08 15:40 | +10 stop | BNB | UP | 0.51 | 0.61 | 0.65 |
| 10-08 15:40 | +10 stop | BTC | DOWN | 0.68 | 0.88 | 1.76 |
| 10-08 15:39 | +10 stop | XRP | DOWN | 0.69 | 0.54 | -1.83 |
| 10-08 15:39 | +10 stop | BNB | DOWN | 0.67 | 0.41 | -2.93 |
| 10-08 15:39 | +5 | BNB | DOWN | 0.67 | 0.76 | 0.61 |
| 10-08 15:37 | +5 | ZEC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-08 15:37 | +10 stop | ZEC | DOWN | 0.58 | 0.76 | 1.50 |
| 10-08 15:37 | +20 | ZEC | DOWN | 0.58 | 0.80 | 1.90 |
| 10-08 15:37 | +15 | ZEC | DOWN | 0.58 | 0.76 | 1.49 |
| 10-08 15:37 | +10 | ZEC | DOWN | 0.58 | 0.76 | 1.46 |
| 10-08 15:37 | +5 | ZEC | DOWN | 0.58 | 0.66 | 0.43 |
| 10-08 15:36 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 10-08 15:36 | +10 stop | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-08 15:36 | +10 | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-08 15:36 | +10 stop | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-08 15:36 | +10 stop | BNB | DOWN | 0.71 | 0.83 | 0.95 |
| 10-08 15:35 | +10 stop | BTC | DOWN | 0.64 | 0.77 | 1.00 |
| 10-08 15:35 | +10 stop | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 10-08 15:35 | +15 | SOL | DOWN | 0.69 | open |  |
| 10-08 15:35 | +10 | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 10-08 15:34 | +10 stop | ETH | DOWN | 0.62 | 0.73 | 0.79 |
| 10-08 15:34 | +10 stop | XRP | DOWN | 0.62 | 0.76 | 1.10 |
| 10-08 15:34 | +5 | BNB | DOWN | 0.61 | 0.71 | 0.68 |
| 10-08 15:34 | +15 | HYPE | UP | 0.41 | 0.65 | 2.03 |
| 10-08 15:34 | +10 stop | BNB | UP | 0.47 | 0.28 | -2.23 |
