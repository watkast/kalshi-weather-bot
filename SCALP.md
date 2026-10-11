# Range-Scalp Bot

*Updated Sun Oct 11 20:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12451 | 10748 | 1703 (25) | 1 | $-4103.21 | -5.2% |
| **+10¢** | 9451 | 7478 | 1973 (37) | 1 | $-3859.97 | -6.5% |
| **+15¢** | 7958 | 5861 | 2097 (55) | 2 | $-3296.23 | -6.6% |
| **+20¢** | 7091 | 4906 | 2185 (69) | 2 | $-2789.27 | -6.3% |
| **+10¢ (15¢ stop)** | 15338 | 15297 | 41 (25) | 0 | $-6035.30 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 20:12 | +10 stop | BNB | UP | 0.67 | 0.77 | 0.71 |
| 10-11 20:12 | +5 | BNB | UP | 0.67 | 0.77 | 0.71 |
| 10-11 20:12 | +5 | HYPE | UP | 0.62 | 0.85 | 2.05 |
| 10-11 20:12 | +10 stop | HYPE | UP | 0.56 | 0.85 | 2.63 |
| 10-11 20:12 | +10 stop | ETH | UP | 0.65 | 0.78 | 1.01 |
| 10-11 20:12 | +10 | ETH | UP | 0.67 | 0.78 | 0.83 |
| 10-11 20:12 | +5 | ETH | UP | 0.67 | 0.78 | 0.81 |
| 10-11 20:11 | +10 stop | DOGE | UP | 0.62 | 0.80 | 1.51 |
| 10-11 20:11 | +20 | DOGE | UP | 0.62 | 0.87 | 2.25 |
| 10-11 20:11 | +15 | DOGE | UP | 0.62 | 0.80 | 1.51 |
| 10-11 20:11 | +10 | DOGE | UP | 0.62 | 0.80 | 1.51 |
| 10-11 20:11 | +5 | DOGE | UP | 0.62 | 0.67 | 0.17 |
| 10-11 20:11 | +10 stop | HYPE | DOWN | 0.41 | 0.68 | 2.37 |
| 10-11 20:10 | +10 stop | ZEC | DOWN | 0.55 | 0.20 | -3.80 |
| 10-11 20:09 | +10 stop | HYPE | UP | 0.50 | 0.24 | -2.91 |
| 10-11 20:09 | +5 | HYPE | UP | 0.51 | 0.56 | 0.14 |
| 10-11 20:09 | +5 | BTC | UP | 0.61 | 0.68 | 0.37 |
| 10-11 20:09 | +5 | ETH | DOWN | 0.63 | 0.78 | 1.20 |
| 10-11 20:09 | +10 stop | ZEC | UP | 0.67 | 0.52 | -1.84 |
| 10-11 20:08 | +10 stop | HYPE | DOWN | 0.66 | 0.48 | -2.16 |
| 10-11 20:08 | +10 stop | BTC | UP | 0.60 | 0.79 | 1.61 |
| 10-11 20:08 | +15 | BTC | UP | 0.60 | 0.79 | 1.61 |
| 10-11 20:08 | +10 | BTC | UP | 0.60 | 0.79 | 1.61 |
| 10-11 20:08 | +5 | BTC | UP | 0.60 | 0.68 | 0.47 |
| 10-11 20:07 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-11 20:07 | +20 | ETH | DOWN | 0.71 | open |  |
| 10-11 20:07 | +15 | ETH | DOWN | 0.71 | open |  |
| 10-11 20:07 | +10 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-11 20:07 | +5 | ETH | DOWN | 0.71 | 0.76 | 0.22 |
| 10-11 20:07 | +10 stop | BNB | DOWN | 0.71 | 0.51 | -2.33 |
| 10-11 20:07 | +5 | BNB | DOWN | 0.71 | 0.77 | 0.32 |
| 10-11 20:07 | +10 stop | NEAR | DOWN | 0.67 | 0.79 | 0.92 |
| 10-11 20:07 | +10 | NEAR | DOWN | 0.69 | 0.79 | 0.73 |
| 10-11 20:07 | +10 stop | DOGE | UP | 0.54 | 0.31 | -2.63 |
| 10-11 20:07 | +5 | NEAR | DOWN | 0.70 | 0.79 | 0.63 |
| 10-11 20:07 | +10 stop | ZEC | UP | 0.69 | 0.46 | -2.63 |
| 10-11 20:07 | +5 | BNB | UP | 0.48 | 0.53 | 0.15 |
| 10-11 20:06 | +10 stop | BNB | DOWN | 0.50 | 0.61 | 0.75 |
| 10-11 20:06 | +5 | BNB | DOWN | 0.50 | 0.59 | 0.55 |
| 10-11 20:06 | +20 | HYPE | UP | 0.66 | 0.96 | 2.86 |
