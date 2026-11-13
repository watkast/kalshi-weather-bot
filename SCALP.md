# Range-Scalp Bot

*Updated Fri Nov 13 03:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57766 | 50388 | 7378 (101) | 0 | $-15702.71 | -4.3% |
| **+10¢** | 43166 | 34550 | 8616 (133) | 0 | $-14629.89 | -5.4% |
| **+15¢** | 36190 | 26918 | 9272 (167) | 0 | $-13155.74 | -5.8% |
| **+20¢** | 32239 | 22509 | 9730 (217) | 0 | $-11522.62 | -5.7% |
| **+10¢ (15¢ stop)** | 70416 | 70288 | 128 (78) | 0 | $-25945.66 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 03:39 | +10 stop | HYPE | DOWN | 0.71 | 0.90 | 1.72 |
| 11-13 03:38 | +10 stop | XRP | DOWN | 0.68 | 0.81 | 1.04 |
| 11-13 03:38 | +10 stop | HYPE | DOWN | 0.52 | 0.65 | 0.96 |
| 11-13 03:38 | +10 stop | ZEC | DOWN | 0.64 | 0.77 | 1.02 |
| 11-13 03:38 | +5 | ZEC | DOWN | 0.64 | 0.77 | 1.02 |
| 11-13 03:38 | +10 stop | NEAR | DOWN | 0.62 | 0.77 | 1.16 |
| 11-13 03:37 | +10 | NEAR | UP | 0.54 | no | -5.58 |
| 11-13 03:36 | +10 stop | HYPE | UP | 0.68 | 0.40 | -3.17 |
| 11-13 03:36 | +5 | HYPE | UP | 0.68 | no | -7.00 |
| 11-13 03:36 | +10 stop | ETH | DOWN | 0.62 | 0.79 | 1.41 |
| 11-13 03:36 | +10 | ETH | DOWN | 0.62 | 0.79 | 1.41 |
| 11-13 03:36 | +5 | ETH | DOWN | 0.62 | 0.69 | 0.38 |
| 11-13 03:36 | +10 stop | NEAR | UP | 0.58 | 0.39 | -2.25 |
| 11-13 03:36 | +10 stop | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 11-13 03:36 | +10 stop | BNB | DOWN | 0.58 | 0.68 | 0.66 |
| 11-13 03:35 | +5 | ETH | DOWN | 0.69 | 0.75 | 0.31 |
| 11-13 03:35 | +10 stop | HYPE | UP | 0.55 | 0.67 | 0.86 |
| 11-13 03:35 | +10 stop | ZEC | UP | 0.49 | 0.30 | -2.23 |
| 11-13 03:35 | +10 stop | NEAR | UP | 0.49 | 0.63 | 1.05 |
| 11-13 03:35 | +10 stop | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-13 03:35 | +20 | BTC | DOWN | 0.61 | 0.81 | 1.72 |
| 11-13 03:35 | +10 | BTC | DOWN | 0.63 | 0.76 | 1.00 |
| 11-13 03:35 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-13 03:35 | +10 stop | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 11-13 03:35 | +20 | DOGE | DOWN | 0.58 | 0.80 | 1.90 |
| 11-13 03:35 | +15 | DOGE | DOWN | 0.58 | 0.76 | 1.49 |
| 11-13 03:35 | +10 | DOGE | DOWN | 0.57 | 0.76 | 1.59 |
| 11-13 03:35 | +5 | DOGE | DOWN | 0.56 | 0.65 | 0.56 |
| 11-13 03:35 | +10 stop | ETH | DOWN | 0.64 | 0.75 | 0.79 |
| 11-13 03:35 | +20 | ETH | DOWN | 0.64 | 0.85 | 1.84 |
| 11-13 03:35 | +15 | ETH | DOWN | 0.64 | 0.79 | 1.21 |
| 11-13 03:35 | +10 | ETH | DOWN | 0.64 | 0.75 | 0.79 |
| 11-13 03:35 | +5 | ETH | DOWN | 0.64 | 0.69 | 0.18 |
| 11-13 03:34 | +20 | ZEC | DOWN | 0.62 | 0.83 | 1.83 |
| 11-13 03:34 | +5 | ZEC | DOWN | 0.62 | 0.68 | 0.27 |
| 11-13 03:34 | +10 stop | NEAR | DOWN | 0.56 | 0.40 | -1.95 |
| 11-13 03:34 | +10 stop | BNB | DOWN | 0.68 | 0.53 | -1.84 |
| 11-13 03:34 | +5 | BNB | DOWN | 0.68 | 0.76 | 0.51 |
| 11-13 03:34 | +5 | NEAR | DOWN | 0.59 | 0.66 | 0.37 |
| 11-13 03:34 | +10 stop | XRP | DOWN | 0.67 | 0.51 | -1.94 |
