# Range-Scalp Bot

*Updated Tue Nov 17 14:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62898 | 54861 | 8037 (117) | 0 | $-17151.26 | -4.3% |
| **+10¢** | 46977 | 37573 | 9404 (159) | 0 | $-16030.75 | -5.4% |
| **+15¢** | 39374 | 29232 | 10142 (201) | 0 | $-14573.37 | -5.9% |
| **+20¢** | 35089 | 24454 | 10635 (256) | 0 | $-12747.05 | -5.8% |
| **+10¢ (15¢ stop)** | 76552 | 76396 | 156 (92) | 0 | $-28239.46 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 14:43 | +10 stop | HYPE | DOWN | 0.61 | 0.26 | -3.81 |
| 11-17 14:41 | +10 stop | ZEC | DOWN | 0.33 | 0.52 | 1.56 |
| 11-17 14:41 | +10 | ZEC | DOWN | 0.36 | 0.52 | 1.21 |
| 11-17 14:41 | +5 | ZEC | DOWN | 0.37 | 0.52 | 1.15 |
| 11-17 14:41 | +10 stop | ZEC | UP | 0.46 | 0.56 | 0.64 |
| 11-17 14:41 | +10 | ZEC | UP | 0.43 | 0.56 | 0.94 |
| 11-17 14:41 | +5 | ZEC | UP | 0.43 | 0.56 | 0.93 |
| 11-17 14:37 | +10 stop | XRP | UP | 0.63 | 0.83 | 1.73 |
| 11-17 14:37 | +10 stop | NEAR | DOWN | 0.42 | 0.61 | 1.55 |
| 11-17 14:37 | +10 stop | ZEC | DOWN | 0.64 | 0.26 | -4.11 |
| 11-17 14:37 | +10 stop | HYPE | UP | 0.43 | 0.54 | 0.72 |
| 11-17 14:37 | +10 stop | ETH | UP | 0.45 | 0.62 | 1.35 |
| 11-17 14:37 | +10 stop | DOGE | UP | 0.45 | 0.61 | 1.22 |
| 11-17 14:37 | +5 | DOGE | UP | 0.45 | 0.61 | 1.27 |
| 11-17 14:36 | +10 stop | ZEC | UP | 0.65 | 0.36 | -3.23 |
| 11-17 14:36 | +10 | ZEC | UP | 0.67 | 0.77 | 0.71 |
| 11-17 14:36 | +5 | ZEC | UP | 0.67 | 0.72 | 0.19 |
| 11-17 14:35 | +10 stop | NEAR | DOWN | 0.50 | 0.67 | 1.36 |
| 11-17 14:35 | +10 stop | DOGE | DOWN | 0.57 | 0.37 | -2.35 |
| 11-17 14:35 | +5 | DOGE | DOWN | 0.57 | 0.66 | 0.56 |
| 11-17 14:34 | +10 stop | XRP | DOWN | 0.66 | 0.38 | -3.13 |
| 11-17 14:34 | +10 stop | ZEC | DOWN | 0.58 | 0.71 | 0.97 |
| 11-17 14:34 | +20 | ZEC | DOWN | 0.58 | 0.86 | 2.53 |
| 11-17 14:34 | +15 | ZEC | DOWN | 0.58 | 0.86 | 2.53 |
| 11-17 14:34 | +10 | ZEC | DOWN | 0.58 | 0.71 | 0.97 |
| 11-17 14:34 | +5 | ZEC | DOWN | 0.58 | 0.71 | 0.97 |
| 11-17 14:34 | +10 stop | ETH | DOWN | 0.67 | 0.51 | -1.93 |
| 11-17 14:34 | +10 stop | DOGE | UP | 0.47 | 0.59 | 0.85 |
| 11-17 14:34 | +5 | DOGE | UP | 0.47 | 0.59 | 0.85 |
| 11-17 14:34 | +10 stop | HYPE | UP | 0.65 | 0.42 | -2.64 |
| 11-17 14:34 | +10 stop | SOL | UP | 0.60 | 0.75 | 1.19 |
| 11-17 14:33 | +10 stop | BNB | UP | 0.61 | 0.41 | -2.36 |
| 11-17 14:33 | +20 | BNB | UP | 0.62 | 0.87 | 2.25 |
| 11-17 14:33 | +15 | BNB | UP | 0.62 | 0.87 | 2.25 |
| 11-17 14:33 | +10 | BNB | UP | 0.61 | 0.72 | 0.76 |
| 11-17 14:33 | +10 stop | BTC | UP | 0.66 | 0.50 | -1.94 |
| 11-17 14:33 | +5 | BNB | UP | 0.61 | 0.72 | 0.78 |
| 11-17 14:33 | +10 stop | NEAR | UP | 0.64 | 0.44 | -2.33 |
| 11-17 14:33 | +5 | BNB | DOWN | 0.50 | 0.58 | 0.44 |
| 11-17 14:33 | +10 stop | ETH | DOWN | 0.67 | 0.50 | -2.04 |
