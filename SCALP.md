# Range-Scalp Bot

*Updated Mon Oct 05 06:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3439 | 2951 | 488 (3) | 4 | $-1255.09 | -5.8% |
| **+10¢** | 2655 | 2099 | 556 (4) | 6 | $-1127.68 | -6.7% |
| **+15¢** | 2233 | 1642 | 591 (6) | 5 | $-1034.26 | -7.4% |
| **+20¢** | 1989 | 1372 | 617 (11) | 6 | $-910.61 | -7.3% |
| **+10¢ (15¢ stop)** | 4272 | 4271 | 1 (1) | 0 | $-1680.75 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 06:42 | +10 stop | SOL | UP | 0.64 | 0.84 | 1.73 |
| 10-05 06:42 | +10 stop | ETH | DOWN | 0.59 | 0.80 | 1.81 |
| 10-05 06:41 | +10 stop | NEAR | UP | 0.60 | 0.34 | -2.93 |
| 10-05 06:41 | +10 stop | SOL | DOWN | 0.66 | 0.30 | -3.91 |
| 10-05 06:41 | +10 | SOL | DOWN | 0.66 | open |  |
| 10-05 06:41 | +5 | SOL | DOWN | 0.66 | open |  |
| 10-05 06:41 | +10 stop | NEAR | DOWN | 0.57 | 0.39 | -2.15 |
| 10-05 06:41 | +10 | NEAR | DOWN | 0.57 | open |  |
| 10-05 06:41 | +5 | NEAR | DOWN | 0.57 | 0.62 | 0.15 |
| 10-05 06:40 | +10 stop | ETH | DOWN | 0.70 | 0.55 | -1.83 |
| 10-05 06:39 | +10 stop | XRP | DOWN | 0.64 | 0.87 | 2.05 |
| 10-05 06:39 | +5 | XRP | DOWN | 0.64 | 0.69 | 0.18 |
| 10-05 06:37 | +10 stop | ETH | UP | 0.67 | 0.40 | -3.03 |
| 10-05 06:37 | +10 stop | SOL | UP | 0.70 | 0.37 | -3.62 |
| 10-05 06:37 | +10 stop | ZEC | UP | 0.63 | 0.31 | -3.52 |
| 10-05 06:37 | +10 stop | BNB | UP | 0.69 | 0.50 | -2.20 |
| 10-05 06:37 | +10 stop | ZEC | DOWN | 0.58 | 0.42 | -1.96 |
| 10-05 06:37 | +5 | ZEC | DOWN | 0.58 | 0.65 | 0.36 |
| 10-05 06:36 | +10 stop | NEAR | UP | 0.53 | 0.35 | -2.14 |
| 10-05 06:35 | +5 | ZEC | DOWN | 0.56 | 0.62 | 0.25 |
| 10-05 06:35 | +10 stop | ETH | DOWN | 0.60 | 0.43 | -2.05 |
| 10-05 06:35 | +10 stop | BNB | DOWN | 0.59 | 0.30 | -3.21 |
| 10-05 06:34 | +10 stop | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 10-05 06:34 | +15 | DOGE | DOWN | 0.68 | 0.84 | 1.34 |
| 10-05 06:34 | +10 | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 10-05 06:34 | +5 | DOGE | DOWN | 0.68 | 0.77 | 0.61 |
| 10-05 06:34 | +10 stop | SOL | UP | 0.56 | 0.67 | 0.76 |
| 10-05 06:34 | +5 | NEAR | DOWN | 0.54 | 0.64 | 0.65 |
| 10-05 06:34 | +10 stop | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 10-05 06:34 | +5 | NEAR | DOWN | 0.50 | 0.61 | 0.75 |
| 10-05 06:34 | +5 | ZEC | DOWN | 0.52 | 0.59 | 0.35 |
| 10-05 06:33 | +10 stop | ETH | DOWN | 0.64 | 0.47 | -2.05 |
| 10-05 06:33 | +10 stop | BNB | DOWN | 0.69 | 0.50 | -2.23 |
| 10-05 06:33 | +20 | XRP | DOWN | 0.71 | 0.92 | 1.88 |
| 10-05 06:33 | +15 | XRP | DOWN | 0.71 | 0.87 | 1.37 |
| 10-05 06:33 | +10 | XRP | DOWN | 0.71 | 0.87 | 1.37 |
| 10-05 06:33 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
| 10-05 06:33 | +10 stop | NEAR | DOWN | 0.64 | 0.40 | -2.72 |
| 10-05 06:33 | +10 stop | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-05 06:33 | +10 stop | ZEC | UP | 0.52 | 0.35 | -2.04 |
