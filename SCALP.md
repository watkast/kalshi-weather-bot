# Range-Scalp Bot

*Updated Tue Nov 03 19:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46224 | 40247 | 5977 (72) | 3 | $-13318.06 | -4.6% |
| **+10¢** | 34499 | 27573 | 6926 (96) | 4 | $-12189.21 | -5.6% |
| **+15¢** | 28877 | 21430 | 7447 (124) | 5 | $-11130.99 | -6.1% |
| **+20¢** | 25652 | 17845 | 7807 (164) | 5 | $-9876.89 | -6.1% |
| **+10¢ (15¢ stop)** | 56398 | 56305 | 93 (56) | 0 | $-21182.44 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 19:29 | +10 stop | SOL | UP | 0.54 | 0.66 | 0.89 |
| 11-03 19:27 | +10 stop | ZEC | DOWN | 0.41 | 0.55 | 1.05 |
| 11-03 19:26 | +10 stop | SOL | DOWN | 0.66 | 0.43 | -2.64 |
| 11-03 19:26 | +10 stop | ETH | DOWN | 0.52 | 0.36 | -1.95 |
| 11-03 19:26 | +10 | ETH | DOWN | 0.52 | open |  |
| 11-03 19:26 | +5 | ETH | DOWN | 0.51 | 0.57 | 0.24 |
| 11-03 19:26 | +10 stop | DOGE | UP | 0.66 | 0.92 | 2.33 |
| 11-03 19:26 | +10 | DOGE | UP | 0.68 | 0.92 | 2.13 |
| 11-03 19:26 | +10 stop | SOL | DOWN | 0.71 | 0.55 | -1.93 |
| 11-03 19:26 | +15 | SOL | DOWN | 0.71 | open |  |
| 11-03 19:26 | +10 | SOL | DOWN | 0.71 | open |  |
| 11-03 19:26 | +5 | SOL | DOWN | 0.71 | open |  |
| 11-03 19:26 | +10 stop | ZEC | UP | 0.67 | 0.38 | -3.23 |
| 11-03 19:26 | +20 | ZEC | UP | 0.67 | 0.88 | 1.86 |
| 11-03 19:26 | +15 | ZEC | UP | 0.67 | 0.82 | 1.23 |
| 11-03 19:26 | +10 | ZEC | UP | 0.67 | 0.82 | 1.23 |
| 11-03 19:26 | +5 | ZEC | UP | 0.67 | 0.76 | 0.61 |
| 11-03 19:25 | +10 stop | XRP | UP | 0.66 | 0.47 | -2.24 |
| 11-03 19:25 | +10 stop | SOL | DOWN | 0.63 | 0.82 | 1.62 |
| 11-03 19:25 | +10 stop | ETH | UP | 0.62 | 0.46 | -1.95 |
| 11-03 19:25 | +5 | DOGE | UP | 0.59 | 0.72 | 0.98 |
| 11-03 19:24 | +10 stop | DOGE | UP | 0.49 | 0.60 | 0.75 |
| 11-03 19:24 | +5 | DOGE | UP | 0.49 | 0.55 | 0.24 |
| 11-03 19:20 | +10 stop | SOL | UP | 0.71 | 0.81 | 0.74 |
| 11-03 19:18 | +10 stop | XRP | UP | 0.61 | 0.74 | 0.99 |
| 11-03 19:18 | +5 | BTC | UP | 0.56 | 0.69 | 0.97 |
| 11-03 19:18 | +5 | DOGE | UP | 0.65 | 0.71 | 0.29 |
| 11-03 19:18 | +10 stop | ETH | UP | 0.63 | 0.73 | 0.69 |
| 11-03 19:17 | +10 stop | BTC | UP | 0.57 | 0.69 | 0.87 |
| 11-03 19:17 | +20 | BTC | UP | 0.57 | 0.81 | 2.11 |
| 11-03 19:17 | +15 | BTC | UP | 0.57 | 0.75 | 1.48 |
| 11-03 19:17 | +10 | BTC | UP | 0.58 | 0.69 | 0.77 |
| 11-03 19:17 | +5 | BTC | UP | 0.58 | 0.63 | 0.15 |
| 11-03 19:17 | +5 | NEAR | UP | 0.70 | 0.75 | 0.21 |
| 11-03 19:17 | +10 stop | ZEC | UP | 0.69 | 0.82 | 1.04 |
| 11-03 19:17 | +20 | ZEC | UP | 0.69 | 0.92 | 2.14 |
| 11-03 19:17 | +15 | ZEC | UP | 0.68 | 0.85 | 1.45 |
| 11-03 19:17 | +10 | ZEC | UP | 0.68 | 0.82 | 1.13 |
| 11-03 19:17 | +5 | ZEC | UP | 0.68 | 0.73 | 0.20 |
| 11-03 19:16 | +10 stop | XRP | DOWN | 0.57 | 0.39 | -2.15 |
