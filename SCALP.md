# Range-Scalp Bot

*Updated Sat Oct 24 17:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32197 | 28072 | 4125 (40) | 0 | $-9203.61 | -4.5% |
| **+10¢** | 24102 | 19326 | 4776 (58) | 0 | $-8232.33 | -5.4% |
| **+15¢** | 20181 | 15044 | 5137 (81) | 0 | $-7376.83 | -5.8% |
| **+20¢** | 17878 | 12501 | 5377 (103) | 0 | $-6542.47 | -5.8% |
| **+10¢ (15¢ stop)** | 39568 | 39509 | 59 (32) | 0 | $-15141.30 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 15:50 | +10 stop | NEAR | UP | 0.68 | 0.87 | 1.66 |
| 10-24 15:50 | +5 | DOGE | UP | 0.69 | 0.78 | 0.62 |
| 10-24 15:49 | +10 stop | NEAR | DOWN | 0.57 | 0.38 | -2.25 |
| 10-24 15:49 | +20 | NEAR | DOWN | 0.57 | yes | -5.88 |
| 10-24 15:49 | +15 | NEAR | DOWN | 0.57 | yes | -5.88 |
| 10-24 15:49 | +10 | NEAR | DOWN | 0.57 | yes | -5.88 |
| 10-24 15:49 | +5 | NEAR | DOWN | 0.57 | yes | -5.88 |
| 10-24 15:49 | +10 stop | HYPE | DOWN | 0.54 | 0.36 | -2.19 |
| 10-24 15:49 | +20 | HYPE | DOWN | 0.54 | yes | -5.62 |
| 10-24 15:49 | +15 | HYPE | DOWN | 0.54 | yes | -5.62 |
| 10-24 15:49 | +10 | HYPE | DOWN | 0.55 | yes | -5.72 |
| 10-24 15:49 | +5 | HYPE | DOWN | 0.57 | yes | -5.88 |
| 10-24 15:48 | +5 | ZEC | UP | 0.61 | 0.69 | 0.48 |
| 10-24 15:48 | +10 stop | DOGE | UP | 0.60 | 0.78 | 1.50 |
| 10-24 15:48 | +20 | DOGE | UP | 0.60 | 0.86 | 2.34 |
| 10-24 15:48 | +15 | DOGE | UP | 0.58 | 0.78 | 1.69 |
| 10-24 15:48 | +10 | DOGE | UP | 0.58 | 0.78 | 1.69 |
| 10-24 15:48 | +5 | DOGE | UP | 0.58 | 0.63 | 0.15 |
| 10-24 15:48 | +10 stop | ZEC | UP | 0.63 | 0.79 | 1.31 |
| 10-24 15:48 | +20 | ZEC | UP | 0.63 | 0.92 | 2.67 |
| 10-24 15:48 | +15 | ZEC | UP | 0.63 | 0.79 | 1.31 |
| 10-24 15:48 | +10 | ZEC | UP | 0.63 | 0.79 | 1.31 |
| 10-24 15:48 | +5 | ZEC | UP | 0.63 | 0.68 | 0.17 |
| 10-24 15:43 | +10 stop | BNB | UP | 0.68 | 0.49 | -2.24 |
| 10-24 15:43 | +15 | BNB | UP | 0.64 | 0.82 | 1.51 |
| 10-24 15:43 | +10 | BNB | UP | 0.64 | 0.82 | 1.51 |
| 10-24 15:42 | +10 stop | BNB | DOWN | 0.42 | 0.59 | 1.33 |
| 10-24 15:42 | +15 | BNB | DOWN | 0.43 | 0.59 | 1.29 |
| 10-24 15:42 | +10 | BNB | DOWN | 0.41 | 0.59 | 1.46 |
| 10-24 15:42 | +10 stop | XRP | DOWN | 0.22 | 0.65 | 4.01 |
| 10-24 15:42 | +5 | XRP | DOWN | 0.25 | 0.65 | 3.70 |
| 10-24 15:41 | +10 stop | NEAR | UP | 0.56 | 0.73 | 1.38 |
| 10-24 15:41 | +5 | NEAR | UP | 0.56 | 0.63 | 0.35 |
| 10-24 15:41 | +10 stop | BNB | DOWN | 0.54 | 0.69 | 1.17 |
| 10-24 15:41 | +10 stop | BTC | UP | 0.64 | 0.49 | -1.85 |
| 10-24 15:41 | +15 | BTC | UP | 0.64 | 0.89 | 2.26 |
| 10-24 15:41 | +10 | BTC | UP | 0.64 | 0.89 | 2.26 |
| 10-24 15:41 | +5 | BTC | UP | 0.64 | 0.73 | 0.59 |
| 10-24 15:41 | +10 stop | XRP | UP | 0.50 | 0.31 | -2.23 |
| 10-24 15:41 | +10 | XRP | UP | 0.50 | 0.86 | 3.33 |
