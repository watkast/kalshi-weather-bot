# Range-Scalp Bot

*Updated Fri Oct 09 19:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9388 | 8102 | 1286 (17) | 2 | $-3181.54 | -5.4% |
| **+10¢** | 7083 | 5576 | 1507 (29) | 4 | $-3107.13 | -7.0% |
| **+15¢** | 5970 | 4384 | 1586 (42) | 3 | $-2562.01 | -6.8% |
| **+20¢** | 5314 | 3666 | 1648 (53) | 3 | $-2148.97 | -6.4% |
| **+10¢ (15¢ stop)** | 11499 | 11467 | 32 (20) | 2 | $-4432.77 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 19:26 | +10 stop | ZEC | DOWN | 0.56 | open |  |
| 10-09 19:26 | +15 | ZEC | DOWN | 0.56 | open |  |
| 10-09 19:26 | +5 | ZEC | DOWN | 0.56 | open |  |
| 10-09 19:24 | +10 stop | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 10-09 19:24 | +15 | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 10-09 19:24 | +10 | SOL | DOWN | 0.68 | 0.82 | 1.15 |
| 10-09 19:24 | +5 | SOL | DOWN | 0.68 | 0.73 | 0.22 |
| 10-09 19:24 | +5 | DOGE | DOWN | 0.59 | 0.75 | 1.29 |
| 10-09 19:23 | +5 | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 10-09 19:23 | +10 stop | XRP | UP | 0.71 | open |  |
| 10-09 19:23 | +10 stop | DOGE | DOWN | 0.56 | 0.75 | 1.58 |
| 10-09 19:23 | +10 stop | ETH | DOWN | 0.53 | 0.78 | 2.19 |
| 10-09 19:23 | +5 | DOGE | DOWN | 0.53 | 0.58 | 0.14 |
| 10-09 19:23 | +10 stop | ZEC | UP | 0.55 | 0.34 | -2.44 |
| 10-09 19:22 | +10 stop | ETH | UP | 0.56 | 0.37 | -2.25 |
| 10-09 19:22 | +10 stop | DOGE | UP | 0.56 | 0.37 | -2.25 |
| 10-09 19:22 | +10 | DOGE | UP | 0.56 | open |  |
| 10-09 19:22 | +5 | DOGE | UP | 0.56 | 0.65 | 0.56 |
| 10-09 19:22 | +10 stop | DOGE | DOWN | 0.54 | 0.65 | 0.76 |
| 10-09 19:22 | +15 | DOGE | DOWN | 0.54 | 0.75 | 1.78 |
| 10-09 19:22 | +10 | DOGE | DOWN | 0.54 | 0.65 | 0.76 |
| 10-09 19:22 | +5 | DOGE | DOWN | 0.54 | 0.65 | 0.76 |
| 10-09 19:22 | +10 stop | SOL | DOWN | 0.64 | 0.47 | -2.09 |
| 10-09 19:22 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-09 19:22 | +5 | BTC | DOWN | 0.64 | 0.71 | 0.38 |
| 10-09 19:21 | +5 | NEAR | DOWN | 0.57 | 0.74 | 1.34 |
| 10-09 19:21 | +10 stop | ZEC | UP | 0.62 | 0.74 | 0.89 |
| 10-09 19:21 | +10 stop | SOL | UP | 0.34 | 0.54 | 1.66 |
| 10-09 19:21 | +10 stop | XRP | UP | 0.54 | 0.72 | 1.47 |
| 10-09 19:21 | +10 stop | BTC | UP | 0.36 | 0.54 | 1.45 |
| 10-09 19:21 | +10 stop | ETH | UP | 0.45 | 0.60 | 1.15 |
| 10-09 19:21 | +5 | BTC | UP | 0.36 | 0.54 | 1.45 |
| 10-09 19:21 | +10 stop | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 10-09 19:21 | +10 stop | NEAR | DOWN | 0.51 | 0.74 | 1.98 |
| 10-09 19:21 | +10 | NEAR | DOWN | 0.51 | 0.74 | 1.98 |
| 10-09 19:21 | +5 | NEAR | DOWN | 0.51 | 0.60 | 0.55 |
| 10-09 19:20 | +10 stop | BNB | UP | 0.55 | 0.74 | 1.57 |
| 10-09 19:19 | +5 | BNB | UP | 0.59 | 0.74 | 1.19 |
| 10-09 19:19 | +5 | SOL | DOWN | 0.69 | 0.76 | 0.42 |
| 10-09 19:18 | +10 stop | ETH | DOWN | 0.70 | 0.52 | -2.13 |
