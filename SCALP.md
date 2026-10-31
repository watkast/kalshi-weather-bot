# Range-Scalp Bot

*Updated Sat Oct 31 17:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42541 | 37102 | 5439 (59) | 0 | $-11993.32 | -4.5% |
| **+10¢** | 31721 | 25428 | 6293 (81) | 0 | $-10761.78 | -5.4% |
| **+15¢** | 26531 | 19745 | 6786 (109) | 0 | $-9860.38 | -5.9% |
| **+20¢** | 23563 | 16448 | 7115 (141) | 0 | $-8752.09 | -5.9% |
| **+10¢ (15¢ stop)** | 51895 | 51816 | 79 (44) | 0 | $-19649.94 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 17:26 | +10 stop | XRP | DOWN | 0.61 | 0.86 | 2.24 |
| 10-31 17:26 | +5 | XRP | DOWN | 0.61 | 0.86 | 2.24 |
| 10-31 17:26 | +10 stop | NEAR | UP | 0.59 | 0.34 | -2.83 |
| 10-31 17:26 | +10 stop | BTC | UP | 0.55 | 0.13 | -4.46 |
| 10-31 17:25 | +10 stop | NEAR | DOWN | 0.43 | 0.56 | 0.94 |
| 10-31 17:25 | +10 stop | BTC | DOWN | 0.45 | 0.55 | 0.64 |
| 10-31 17:24 | +10 stop | DOGE | UP | 0.50 | 0.71 | 1.77 |
| 10-31 17:24 | +10 stop | NEAR | UP | 0.55 | 0.37 | -2.15 |
| 10-31 17:24 | +20 | NEAR | UP | 0.55 | no | -5.68 |
| 10-31 17:24 | +15 | NEAR | UP | 0.55 | no | -5.68 |
| 10-31 17:24 | +10 | NEAR | UP | 0.55 | no | -5.68 |
| 10-31 17:24 | +5 | NEAR | UP | 0.55 | no | -5.68 |
| 10-31 17:24 | +10 stop | ZEC | DOWN | 0.61 | 0.45 | -1.95 |
| 10-31 17:24 | +20 | ZEC | DOWN | 0.61 | 0.86 | 2.24 |
| 10-31 17:24 | +15 | ZEC | DOWN | 0.61 | 0.86 | 2.24 |
| 10-31 17:24 | +10 | ZEC | DOWN | 0.61 | 0.86 | 2.24 |
| 10-31 17:24 | +5 | ZEC | DOWN | 0.61 | 0.70 | 0.58 |
| 10-31 17:23 | +10 stop | DOGE | DOWN | 0.63 | 0.47 | -1.95 |
| 10-31 17:23 | +10 | DOGE | DOWN | 0.63 | 0.88 | 2.25 |
| 10-31 17:23 | +5 | DOGE | DOWN | 0.63 | 0.88 | 2.25 |
| 10-31 17:23 | +10 | BTC | DOWN | 0.66 | 0.86 | 1.75 |
| 10-31 17:22 | +10 stop | XRP | DOWN | 0.65 | 0.47 | -2.14 |
| 10-31 17:22 | +10 | XRP | DOWN | 0.65 | 0.86 | 1.85 |
| 10-31 17:22 | +10 stop | BTC | DOWN | 0.67 | 0.52 | -1.84 |
| 10-31 17:22 | +5 | XRP | DOWN | 0.66 | 0.71 | 0.19 |
| 10-31 17:21 | +5 | NEAR | DOWN | 0.66 | 0.72 | 0.29 |
| 10-31 17:21 | +10 stop | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-31 17:21 | +5 | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-31 17:21 | +10 stop | XRP | DOWN | 0.48 | 0.62 | 1.05 |
| 10-31 17:21 | +10 | XRP | DOWN | 0.48 | 0.62 | 1.05 |
| 10-31 17:21 | +5 | XRP | DOWN | 0.48 | 0.54 | 0.24 |
| 10-31 17:21 | +10 stop | BTC | UP | 0.64 | 0.45 | -2.25 |
| 10-31 17:21 | +5 | BTC | UP | 0.64 | no | -6.57 |
| 10-31 17:21 | +10 stop | BNB | UP | 0.58 | 0.71 | 0.97 |
| 10-31 17:21 | +10 stop | DOGE | UP | 0.68 | 0.46 | -2.54 |
| 10-31 17:20 | +10 stop | NEAR | DOWN | 0.56 | 0.67 | 0.76 |
| 10-31 17:20 | +10 stop | ZEC | UP | 0.59 | 0.43 | -1.95 |
| 10-31 17:19 | +10 stop | NEAR | UP | 0.61 | 0.41 | -2.34 |
| 10-31 17:18 | +5 | BTC | UP | 0.70 | 0.82 | 0.94 |
| 10-31 17:17 | +10 stop | BTC | UP | 0.63 | 0.82 | 1.62 |
