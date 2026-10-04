# Range-Scalp Bot

*Updated Sun Oct 04 21:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2824 | 2425 | 399 (3) | 0 | $-994.52 | -5.6% |
| **+10¢** | 2211 | 1763 | 448 (4) | 0 | $-817.97 | -5.9% |
| **+15¢** | 1860 | 1385 | 475 (5) | 0 | $-710.22 | -6.1% |
| **+20¢** | 1658 | 1161 | 497 (9) | 0 | $-613.87 | -5.9% |
| **+10¢ (15¢ stop)** | 3527 | 3526 | 1 (1) | 0 | $-1384.94 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 21:25 | +10 stop | HYPE | DOWN | 0.58 | 0.70 | 0.87 |
| 10-04 21:25 | +10 stop | XRP | UP | 0.70 | 0.82 | 0.94 |
| 10-04 21:23 | +10 stop | XRP | DOWN | 0.61 | 0.44 | -2.05 |
| 10-04 21:23 | +20 | XRP | DOWN | 0.61 | yes | -6.27 |
| 10-04 21:23 | +15 | XRP | DOWN | 0.61 | yes | -6.27 |
| 10-04 21:23 | +10 stop | DOGE | UP | 0.60 | 0.77 | 1.40 |
| 10-04 21:21 | +10 stop | DOGE | UP | 0.71 | 0.54 | -2.03 |
| 10-04 21:21 | +5 | DOGE | UP | 0.71 | 0.77 | 0.32 |
| 10-04 21:20 | +10 stop | ETH | DOWN | 0.65 | 0.93 | 2.58 |
| 10-04 21:20 | +10 stop | XRP | UP | 0.53 | 0.24 | -3.16 |
| 10-04 21:19 | +10 stop | DOGE | UP | 0.71 | 0.51 | -2.33 |
| 10-04 21:19 | +20 | DOGE | UP | 0.71 | 0.93 | 1.97 |
| 10-04 21:19 | +15 | DOGE | UP | 0.71 | 0.89 | 1.58 |
| 10-04 21:19 | +10 | DOGE | UP | 0.71 | 0.89 | 1.58 |
| 10-04 21:19 | +5 | DOGE | UP | 0.71 | 0.77 | 0.32 |
| 10-04 21:19 | +10 stop | NEAR | DOWN | 0.67 | 0.81 | 1.13 |
| 10-04 21:19 | +15 | NEAR | DOWN | 0.67 | 0.85 | 1.55 |
| 10-04 21:19 | +10 | NEAR | DOWN | 0.67 | 0.81 | 1.13 |
| 10-04 21:19 | +5 | NEAR | DOWN | 0.67 | 0.73 | 0.30 |
| 10-04 21:19 | +10 stop | ZEC | DOWN | 0.57 | 0.74 | 1.38 |
| 10-04 21:19 | +20 | ZEC | DOWN | 0.57 | 0.83 | 2.32 |
| 10-04 21:19 | +15 | ZEC | DOWN | 0.57 | 0.74 | 1.38 |
| 10-04 21:19 | +10 | ZEC | DOWN | 0.57 | 0.74 | 1.38 |
| 10-04 21:19 | +5 | ZEC | DOWN | 0.57 | 0.74 | 1.38 |
| 10-04 21:17 | +10 stop | SOL | UP | 0.63 | 0.47 | -1.95 |
| 10-04 21:17 | +10 stop | ETH | UP | 0.62 | 0.45 | -2.05 |
| 10-04 21:17 | +20 | ETH | UP | 0.62 | no | -6.37 |
| 10-04 21:17 | +15 | ETH | UP | 0.62 | no | -6.37 |
| 10-04 21:17 | +10 | ETH | UP | 0.62 | no | -6.37 |
| 10-04 21:17 | +5 | ETH | UP | 0.63 | no | -6.47 |
| 10-04 21:17 | +5 | SOL | UP | 0.60 | no | -6.17 |
| 10-04 21:17 | +10 stop | XRP | UP | 0.61 | 0.44 | -2.05 |
| 10-04 21:17 | +10 | XRP | UP | 0.61 | 0.76 | 1.20 |
| 10-04 21:17 | +5 | XRP | UP | 0.61 | 0.76 | 1.20 |
| 10-04 21:17 | +5 | NEAR | DOWN | 0.67 | 0.72 | 0.19 |
| 10-04 21:16 | +10 stop | BTC | UP | 0.52 | 0.28 | -2.73 |
| 10-04 21:16 | +20 | BTC | UP | 0.52 | no | -5.38 |
| 10-04 21:16 | +15 | BTC | UP | 0.52 | no | -5.38 |
| 10-04 21:16 | +10 | BTC | UP | 0.52 | no | -5.38 |
| 10-04 21:16 | +5 | BTC | UP | 0.52 | no | -5.38 |
