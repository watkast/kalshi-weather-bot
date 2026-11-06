# Range-Scalp Bot

*Updated Fri Nov 06 15:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49654 | 43279 | 6375 (76) | 4 | $-13976.25 | -4.5% |
| **+10¢** | 37064 | 29649 | 7415 (101) | 5 | $-12867.40 | -5.5% |
| **+15¢** | 31045 | 23056 | 7989 (130) | 5 | $-11765.39 | -6.0% |
| **+20¢** | 27598 | 19223 | 8375 (171) | 6 | $-10403.26 | -6.0% |
| **+10¢ (15¢ stop)** | 60495 | 60398 | 97 (57) | 2 | $-22356.27 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 15:24 | +10 stop | BTC | DOWN | 0.68 | open |  |
| 11-06 15:23 | +10 stop | DOGE | UP | 0.60 | open |  |
| 11-06 15:23 | +15 | DOGE | UP | 0.60 | open |  |
| 11-06 15:23 | +10 | DOGE | UP | 0.60 | open |  |
| 11-06 15:23 | +5 | DOGE | UP | 0.60 | open |  |
| 11-06 15:22 | +5 | NEAR | UP | 0.65 | open |  |
| 11-06 15:22 | +5 | ZEC | DOWN | 0.62 | 0.68 | 0.27 |
| 11-06 15:22 | +10 stop | BNB | DOWN | 0.62 | 0.75 | 0.99 |
| 11-06 15:22 | +10 | BNB | DOWN | 0.62 | 0.75 | 0.99 |
| 11-06 15:22 | +5 | BNB | DOWN | 0.63 | 0.70 | 0.38 |
| 11-06 15:22 | +10 stop | SOL | DOWN | 0.57 | 0.70 | 0.97 |
| 11-06 15:22 | +10 stop | XRP | DOWN | 0.57 | 0.74 | 1.38 |
| 11-06 15:22 | +5 | XRP | DOWN | 0.56 | 0.65 | 0.56 |
| 11-06 15:22 | +10 stop | ZEC | DOWN | 0.63 | 0.85 | 1.94 |
| 11-06 15:22 | +10 stop | XRP | DOWN | 0.58 | 0.69 | 0.77 |
| 11-06 15:22 | +5 | XRP | DOWN | 0.58 | 0.69 | 0.77 |
| 11-06 15:22 | +10 stop | DOGE | DOWN | 0.59 | 0.37 | -2.54 |
| 11-06 15:21 | +5 | NEAR | UP | 0.48 | 0.61 | 0.95 |
| 11-06 15:21 | +10 stop | SOL | DOWN | 0.58 | 0.72 | 1.07 |
| 11-06 15:21 | +5 | XRP | DOWN | 0.60 | 0.66 | 0.27 |
| 11-06 15:20 | +10 stop | HYPE | DOWN | 0.69 | 0.82 | 0.99 |
| 11-06 15:20 | +10 stop | NEAR | UP | 0.56 | 0.32 | -2.74 |
| 11-06 15:20 | +5 | NEAR | UP | 0.56 | 0.64 | 0.41 |
| 11-06 15:20 | +10 stop | BTC | DOWN | 0.61 | 0.42 | -2.25 |
| 11-06 15:20 | +5 | ETH | DOWN | 0.69 | 0.75 | 0.31 |
| 11-06 15:19 | +10 stop | SOL | UP | 0.52 | 0.37 | -1.85 |
| 11-06 15:18 | +10 stop | ZEC | UP | 0.70 | 0.54 | -1.93 |
| 11-06 15:18 | +10 stop | ETH | DOWN | 0.59 | 0.75 | 1.29 |
| 11-06 15:18 | +10 | ETH | DOWN | 0.59 | 0.75 | 1.29 |
| 11-06 15:18 | +5 | ETH | DOWN | 0.60 | 0.67 | 0.37 |
| 11-06 15:18 | +10 stop | HYPE | DOWN | 0.61 | 0.46 | -1.85 |
| 11-06 15:18 | +20 | HYPE | DOWN | 0.61 | 0.82 | 1.82 |
| 11-06 15:18 | +15 | HYPE | DOWN | 0.61 | 0.82 | 1.82 |
| 11-06 15:18 | +10 | HYPE | DOWN | 0.61 | 0.73 | 0.89 |
| 11-06 15:18 | +5 | HYPE | DOWN | 0.61 | 0.73 | 0.89 |
| 11-06 15:18 | +10 stop | SOL | DOWN | 0.61 | 0.41 | -2.34 |
| 11-06 15:17 | +10 stop | DOGE | DOWN | 0.65 | 0.44 | -2.44 |
| 11-06 15:17 | +5 | ETH | DOWN | 0.61 | 0.70 | 0.58 |
| 11-06 15:17 | +10 stop | BTC | DOWN | 0.50 | 0.60 | 0.65 |
| 11-06 15:17 | +10 stop | ZEC | DOWN | 0.60 | 0.43 | -2.05 |
