# Range-Scalp Bot

*Updated Thu Oct 08 23:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8122 | 7021 | 1101 (13) | 0 | $-2684.13 | -5.2% |
| **+10¢** | 6151 | 4850 | 1301 (25) | 0 | $-2649.39 | -6.8% |
| **+15¢** | 5180 | 3811 | 1369 (37) | 0 | $-2169.11 | -6.7% |
| **+20¢** | 4626 | 3206 | 1420 (45) | 0 | $-1753.82 | -6.0% |
| **+10¢ (15¢ stop)** | 9868 | 9838 | 30 (19) | 0 | $-3641.56 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 22:57 | +10 stop | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 10-08 22:56 | +10 stop | NEAR | UP | 0.47 | 0.29 | -2.13 |
| 10-08 22:54 | +10 stop | ZEC | DOWN | 0.59 | 0.71 | 0.88 |
| 10-08 22:54 | +20 | ZEC | DOWN | 0.59 | yes | -6.07 |
| 10-08 22:54 | +15 | ZEC | DOWN | 0.59 | 0.78 | 1.60 |
| 10-08 22:54 | +10 | ZEC | DOWN | 0.65 | 0.78 | 0.99 |
| 10-08 22:54 | +5 | ZEC | DOWN | 0.65 | 0.71 | 0.26 |
| 10-08 22:54 | +10 stop | NEAR | UP | 0.66 | 0.51 | -1.84 |
| 10-08 22:53 | +10 stop | DOGE | DOWN | 0.66 | 0.51 | -1.84 |
| 10-08 22:53 | +10 stop | BNB | DOWN | 0.63 | 0.46 | -2.05 |
| 10-08 22:51 | +10 stop | DOGE | DOWN | 0.53 | 0.63 | 0.65 |
| 10-08 22:51 | +10 stop | BNB | DOWN | 0.51 | 0.63 | 0.85 |
| 10-08 22:50 | +10 stop | BTC | DOWN | 0.66 | 0.79 | 1.02 |
| 10-08 22:50 | +10 stop | ZEC | DOWN | 0.70 | 0.83 | 1.06 |
| 10-08 22:50 | +10 stop | DOGE | UP | 0.46 | 0.56 | 0.64 |
| 10-08 22:49 | +10 stop | ETH | DOWN | 0.57 | 0.74 | 1.38 |
| 10-08 22:49 | +5 | XRP | DOWN | 0.56 | 0.73 | 1.38 |
| 10-08 22:49 | +10 stop | DOGE | UP | 0.51 | 0.63 | 0.85 |
| 10-08 22:48 | +10 stop | NEAR | UP | 0.68 | 0.46 | -2.50 |
| 10-08 22:48 | +10 stop | XRP | UP | 0.51 | 0.26 | -2.82 |
| 10-08 22:48 | +20 | XRP | UP | 0.50 | no | -5.19 |
| 10-08 22:48 | +15 | XRP | UP | 0.50 | no | -5.19 |
| 10-08 22:48 | +10 | XRP | UP | 0.50 | 0.60 | 0.65 |
| 10-08 22:48 | +5 | XRP | UP | 0.50 | 0.55 | 0.14 |
| 10-08 22:48 | +10 stop | SOL | DOWN | 0.57 | 0.78 | 1.79 |
| 10-08 22:48 | +5 | BNB | UP | 0.68 | no | -6.97 |
| 10-08 22:47 | +10 stop | ZEC | DOWN | 0.60 | 0.44 | -1.95 |
| 10-08 22:47 | +20 | ZEC | DOWN | 0.60 | 0.83 | 2.03 |
| 10-08 22:47 | +15 | ZEC | DOWN | 0.60 | 0.75 | 1.19 |
| 10-08 22:47 | +10 | ZEC | DOWN | 0.60 | 0.74 | 1.09 |
| 10-08 22:47 | +5 | ZEC | DOWN | 0.60 | 0.68 | 0.47 |
| 10-08 22:46 | +10 stop | BNB | UP | 0.68 | 0.43 | -2.84 |
| 10-08 22:46 | +20 | BNB | UP | 0.68 | no | -6.96 |
| 10-08 22:46 | +15 | BNB | UP | 0.68 | no | -6.96 |
| 10-08 22:46 | +10 | BNB | UP | 0.68 | no | -6.96 |
| 10-08 22:46 | +5 | BNB | UP | 0.68 | 0.73 | 0.20 |
| 10-08 22:46 | +10 stop | NEAR | UP | 0.71 | 0.56 | -1.83 |
| 10-08 22:46 | +20 | NEAR | UP | 0.71 | no | -7.25 |
| 10-08 22:46 | +15 | NEAR | UP | 0.71 | no | -7.25 |
| 10-08 22:46 | +10 | NEAR | UP | 0.71 | no | -7.25 |
