# Range-Scalp Bot

*Updated Fri Oct 09 08:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8818 | 7629 | 1189 (13) | 2 | $-2883.88 | -5.2% |
| **+10¢** | 6679 | 5281 | 1398 (25) | 2 | $-2780.54 | -6.6% |
| **+15¢** | 5632 | 4159 | 1473 (37) | 1 | $-2263.90 | -6.4% |
| **+20¢** | 5014 | 3486 | 1528 (45) | 2 | $-1853.06 | -5.9% |
| **+10¢ (15¢ stop)** | 10756 | 10726 | 30 (19) | 0 | $-4005.12 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 08:39 | +10 stop | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-09 08:39 | +20 | DOGE | DOWN | 0.68 | 0.89 | 1.87 |
| 10-09 08:39 | +15 | DOGE | DOWN | 0.68 | 0.89 | 1.87 |
| 10-09 08:39 | +10 | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-09 08:39 | +5 | DOGE | DOWN | 0.68 | 0.77 | 0.61 |
| 10-09 08:39 | +20 | XRP | DOWN | 0.66 | 0.87 | 1.86 |
| 10-09 08:39 | +10 stop | XRP | DOWN | 0.64 | 0.48 | -1.95 |
| 10-09 08:39 | +15 | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-09 08:39 | +10 stop | BNB | DOWN | 0.49 | 0.61 | 0.85 |
| 10-09 08:38 | +10 stop | ZEC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-09 08:38 | +5 | BNB | DOWN | 0.60 | 0.68 | 0.48 |
| 10-09 08:38 | +10 stop | XRP | UP | 0.58 | 0.40 | -2.15 |
| 10-09 08:38 | +10 | XRP | UP | 0.58 | open |  |
| 10-09 08:38 | +5 | XRP | UP | 0.58 | open |  |
| 10-09 08:38 | +5 | BTC | DOWN | 0.68 | 0.82 | 1.13 |
| 10-09 08:38 | +10 stop | DOGE | DOWN | 0.63 | 0.75 | 0.93 |
| 10-09 08:38 | +15 | DOGE | DOWN | 0.63 | 0.79 | 1.35 |
| 10-09 08:38 | +10 | DOGE | DOWN | 0.62 | 0.75 | 0.95 |
| 10-09 08:38 | +5 | DOGE | DOWN | 0.62 | 0.75 | 0.95 |
| 10-09 08:37 | +5 | ETH | DOWN | 0.68 | 0.77 | 0.63 |
| 10-09 08:37 | +10 stop | XRP | UP | 0.46 | 0.56 | 0.64 |
| 10-09 08:37 | +10 | XRP | UP | 0.46 | 0.56 | 0.64 |
| 10-09 08:37 | +5 | XRP | UP | 0.46 | 0.56 | 0.64 |
| 10-09 08:37 | +10 stop | SOL | UP | 0.48 | 0.62 | 1.05 |
| 10-09 08:37 | +5 | BNB | DOWN | 0.62 | 0.67 | 0.17 |
| 10-09 08:37 | +10 stop | DOGE | DOWN | 0.55 | 0.71 | 1.27 |
| 10-09 08:37 | +20 | DOGE | DOWN | 0.55 | 0.75 | 1.68 |
| 10-09 08:37 | +15 | DOGE | DOWN | 0.55 | 0.71 | 1.27 |
| 10-09 08:37 | +10 | DOGE | DOWN | 0.55 | 0.71 | 1.27 |
| 10-09 08:37 | +5 | DOGE | DOWN | 0.55 | 0.61 | 0.25 |
| 10-09 08:36 | +10 stop | XRP | DOWN | 0.43 | 0.56 | 0.94 |
| 10-09 08:36 | +20 | XRP | DOWN | 0.43 | 0.69 | 2.27 |
| 10-09 08:36 | +15 | XRP | DOWN | 0.43 | 0.58 | 1.14 |
| 10-09 08:36 | +10 | XRP | DOWN | 0.43 | 0.56 | 0.94 |
| 10-09 08:36 | +5 | XRP | DOWN | 0.43 | 0.56 | 0.94 |
| 10-09 08:36 | +10 stop | ZEC | UP | 0.65 | 0.35 | -3.32 |
| 10-09 08:36 | +10 stop | NEAR | UP | 0.62 | 0.80 | 1.47 |
| 10-09 08:36 | +10 stop | SOL | UP | 0.49 | 0.61 | 0.85 |
| 10-09 08:35 | +5 | NEAR | DOWN | 0.54 | open |  |
| 10-09 08:35 | +10 stop | BTC | DOWN | 0.67 | 0.82 | 1.23 |
