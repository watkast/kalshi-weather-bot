# Range-Scalp Bot

*Updated Sat Nov 14 03:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58951 | 51432 | 7519 (106) | 0 | $-15950.68 | -4.3% |
| **+10¢** | 44050 | 35260 | 8790 (139) | 0 | $-14907.64 | -5.4% |
| **+15¢** | 36913 | 27438 | 9475 (174) | 0 | $-13524.02 | -5.8% |
| **+20¢** | 32886 | 22938 | 9948 (226) | 0 | $-11908.44 | -5.8% |
| **+10¢ (15¢ stop)** | 71780 | 71642 | 138 (82) | 0 | $-26387.28 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 03:25 | +10 stop | XRP | UP | 0.48 | 0.32 | -1.94 |
| 11-14 03:24 | +10 stop | XRP | DOWN | 0.70 | 0.50 | -2.33 |
| 11-14 03:22 | +10 stop | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 11-14 03:22 | +20 | NEAR | DOWN | 0.68 | 0.93 | 2.24 |
| 11-14 03:22 | +15 | NEAR | DOWN | 0.68 | 0.88 | 1.73 |
| 11-14 03:22 | +10 | NEAR | DOWN | 0.68 | 0.81 | 1.00 |
| 11-14 03:22 | +5 | NEAR | DOWN | 0.68 | 0.74 | 0.29 |
| 11-14 03:22 | +10 stop | DOGE | DOWN | 0.69 | 0.83 | 1.15 |
| 11-14 03:22 | +20 | DOGE | DOWN | 0.69 | 0.91 | 1.97 |
| 11-14 03:22 | +15 | DOGE | DOWN | 0.69 | 0.86 | 1.46 |
| 11-14 03:22 | +10 | DOGE | DOWN | 0.70 | 0.83 | 1.06 |
| 11-14 03:22 | +5 | DOGE | DOWN | 0.70 | 0.77 | 0.42 |
| 11-14 03:22 | +15 | ETH | DOWN | 0.71 | 0.88 | 1.47 |
| 11-14 03:22 | +10 | ETH | DOWN | 0.70 | 0.83 | 1.05 |
| 11-14 03:19 | +10 stop | XRP | DOWN | 0.70 | 0.55 | -1.83 |
| 11-14 03:19 | +10 | XRP | DOWN | 0.70 | 0.85 | 1.26 |
| 11-14 03:19 | +5 | XRP | DOWN | 0.70 | 0.77 | 0.42 |
| 11-14 03:15 | +10 stop | ZEC | DOWN | 0.68 | 0.84 | 1.34 |
| 11-14 03:15 | +20 | ZEC | DOWN | 0.67 | 0.88 | 1.86 |
| 11-14 03:15 | +15 | ZEC | DOWN | 0.67 | 0.84 | 1.44 |
| 11-14 03:15 | +10 | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-14 03:15 | +5 | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-14 03:15 | +10 stop | BTC | DOWN | 0.63 | 0.80 | 1.41 |
| 11-14 03:15 | +20 | BTC | DOWN | 0.63 | 0.87 | 2.15 |
| 11-14 03:15 | +15 | BTC | DOWN | 0.63 | 0.80 | 1.41 |
| 11-14 03:15 | +10 | BTC | DOWN | 0.63 | 0.80 | 1.41 |
| 11-14 03:15 | +5 | BTC | DOWN | 0.63 | 0.69 | 0.28 |
| 11-14 03:15 | +10 stop | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-14 03:15 | +20 | XRP | DOWN | 0.66 | 0.88 | 1.96 |
| 11-14 03:15 | +15 | XRP | DOWN | 0.66 | 0.85 | 1.65 |
| 11-14 03:15 | +10 | XRP | DOWN | 0.66 | 0.77 | 0.81 |
| 11-14 03:15 | +5 | XRP | DOWN | 0.66 | 0.71 | 0.19 |
| 11-14 03:15 | +10 stop | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 11-14 03:15 | +20 | ETH | DOWN | 0.70 | 0.91 | 1.83 |
| 11-14 03:15 | +15 | ETH | DOWN | 0.70 | 0.87 | 1.47 |
| 11-14 03:15 | +10 | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 11-14 03:15 | +5 | ETH | DOWN | 0.70 | 0.78 | 0.52 |
| 11-14 03:12 | +10 stop | BNB | DOWN | 0.67 | 0.88 | 1.86 |
| 11-14 03:12 | +10 stop | BTC | DOWN | 0.68 | 0.89 | 1.87 |
| 11-14 03:12 | +20 | BTC | DOWN | 0.68 | 0.89 | 1.87 |
