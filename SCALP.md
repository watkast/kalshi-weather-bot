# Range-Scalp Bot

*Updated Sun Oct 04 10:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2146 | 1854 | 292 (3) | 1 | $-698.07 | -5.1% |
| **+10¢** | 1671 | 1346 | 325 (4) | 1 | $-511.61 | -4.8% |
| **+15¢** | 1401 | 1055 | 346 (5) | 2 | $-449.81 | -5.1% |
| **+20¢** | 1238 | 874 | 364 (8) | 2 | $-392.83 | -5.0% |
| **+10¢ (15¢ stop)** | 2656 | 2655 | 1 (1) | 0 | $-994.49 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 10:39 | +10 stop | SOL | UP | 0.55 | 0.33 | -2.54 |
| 10-04 10:38 | +10 stop | DOGE | DOWN | 0.59 | 0.77 | 1.50 |
| 10-04 10:38 | +10 | DOGE | DOWN | 0.59 | 0.77 | 1.50 |
| 10-04 10:38 | +5 | DOGE | DOWN | 0.59 | 0.77 | 1.50 |
| 10-04 10:36 | +5 | DOGE | DOWN | 0.71 | 0.77 | 0.32 |
| 10-04 10:36 | +5 | NEAR | UP | 0.64 | 0.75 | 0.79 |
| 10-04 10:36 | +10 stop | DOGE | DOWN | 0.62 | 0.73 | 0.79 |
| 10-04 10:36 | +10 | DOGE | DOWN | 0.62 | 0.73 | 0.79 |
| 10-04 10:36 | +5 | DOGE | DOWN | 0.61 | 0.68 | 0.33 |
| 10-04 10:35 | +5 | NEAR | UP | 0.65 | 0.73 | 0.51 |
| 10-04 10:34 | +10 stop | SOL | DOWN | 0.67 | 0.50 | -2.04 |
| 10-04 10:34 | +10 stop | DOGE | UP | 0.53 | 0.69 | 1.27 |
| 10-04 10:34 | +10 | DOGE | UP | 0.53 | 0.69 | 1.27 |
| 10-04 10:34 | +5 | DOGE | UP | 0.53 | 0.69 | 1.27 |
| 10-04 10:34 | +10 stop | SOL | UP | 0.59 | 0.43 | -1.95 |
| 10-04 10:34 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-04 10:34 | +20 | ETH | DOWN | 0.71 | 0.93 | 1.96 |
| 10-04 10:34 | +15 | ETH | DOWN | 0.71 | 0.87 | 1.37 |
| 10-04 10:34 | +10 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-04 10:34 | +5 | ETH | DOWN | 0.71 | 0.78 | 0.42 |
| 10-04 10:34 | +10 stop | XRP | UP | 0.51 | 0.34 | -2.04 |
| 10-04 10:34 | +10 stop | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 10-04 10:34 | +15 | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 10-04 10:34 | +10 | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 10-04 10:34 | +5 | BTC | DOWN | 0.71 | 0.78 | 0.42 |
| 10-04 10:33 | +10 stop | SOL | DOWN | 0.54 | 0.35 | -2.24 |
| 10-04 10:33 | +10 stop | XRP | DOWN | 0.54 | 0.36 | -2.15 |
| 10-04 10:33 | +10 | XRP | DOWN | 0.54 | 0.65 | 0.76 |
| 10-04 10:33 | +5 | XRP | DOWN | 0.54 | 0.65 | 0.76 |
| 10-04 10:33 | +10 stop | NEAR | UP | 0.70 | 0.83 | 1.05 |
| 10-04 10:33 | +10 | NEAR | UP | 0.70 | 0.83 | 1.05 |
| 10-04 10:33 | +5 | NEAR | UP | 0.70 | 0.77 | 0.42 |
| 10-04 10:32 | +5 | ZEC | DOWN | 0.71 | 0.77 | 0.32 |
| 10-04 10:32 | +10 stop | DOGE | UP | 0.63 | 0.75 | 0.89 |
| 10-04 10:32 | +20 | DOGE | UP | 0.63 | open |  |
| 10-04 10:32 | +15 | DOGE | UP | 0.63 | open |  |
| 10-04 10:32 | +10 | DOGE | UP | 0.63 | 0.75 | 0.89 |
| 10-04 10:32 | +5 | DOGE | UP | 0.63 | 0.75 | 0.89 |
| 10-04 10:32 | +5 | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 10-04 10:31 | +10 stop | ZEC | DOWN | 0.56 | 0.69 | 1.02 |
