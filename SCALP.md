# Range-Scalp Bot

*Updated Mon Oct 05 00:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3028 | 2598 | 430 (3) | 5 | $-1100.28 | -5.7% |
| **+10¢** | 2353 | 1868 | 485 (4) | 5 | $-941.25 | -6.3% |
| **+15¢** | 1982 | 1470 | 512 (5) | 5 | $-815.45 | -6.5% |
| **+20¢** | 1769 | 1235 | 534 (10) | 5 | $-682.21 | -6.1% |
| **+10¢ (15¢ stop)** | 3798 | 3797 | 1 (1) | 0 | $-1531.28 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 00:41 | +10 stop | ZEC | UP | 0.59 | 0.83 | 2.13 |
| 10-05 00:39 | +10 stop | ETH | UP | 0.67 | 0.81 | 1.13 |
| 10-05 00:39 | +5 | ETH | UP | 0.67 | 0.81 | 1.13 |
| 10-05 00:38 | +10 stop | XRP | UP | 0.62 | 0.74 | 0.89 |
| 10-05 00:38 | +10 stop | BTC | UP | 0.70 | 0.86 | 1.36 |
| 10-05 00:38 | +10 stop | ZEC | UP | 0.65 | 0.45 | -2.31 |
| 10-05 00:38 | +10 stop | ETH | DOWN | 0.54 | 0.39 | -1.85 |
| 10-05 00:38 | +10 stop | NEAR | UP | 0.65 | 0.75 | 0.70 |
| 10-05 00:37 | +5 | ETH | UP | 0.53 | 0.59 | 0.25 |
| 10-05 00:37 | +10 stop | BNB | UP | 0.70 | 0.84 | 1.15 |
| 10-05 00:37 | +20 | BNB | UP | 0.70 | 0.90 | 1.78 |
| 10-05 00:37 | +15 | BNB | UP | 0.70 | 0.90 | 1.78 |
| 10-05 00:37 | +10 | BNB | UP | 0.70 | 0.84 | 1.15 |
| 10-05 00:37 | +5 | BNB | UP | 0.70 | 0.76 | 0.32 |
| 10-05 00:37 | +10 stop | ZEC | UP | 0.69 | 0.53 | -1.98 |
| 10-05 00:36 | +10 stop | BTC | UP | 0.66 | 0.51 | -1.84 |
| 10-05 00:36 | +10 stop | SOL | UP | 0.57 | 0.69 | 0.87 |
| 10-05 00:36 | +10 stop | XRP | UP | 0.69 | 0.54 | -1.83 |
| 10-05 00:36 | +10 stop | ZEC | DOWN | 0.47 | 0.27 | -2.32 |
| 10-05 00:36 | +10 stop | NEAR | UP | 0.66 | 0.77 | 0.81 |
| 10-05 00:35 | +10 stop | HYPE | UP | 0.62 | 0.41 | -2.44 |
| 10-05 00:35 | +5 | HYPE | UP | 0.62 | 0.67 | 0.17 |
| 10-05 00:35 | +10 stop | BTC | DOWN | 0.59 | 0.43 | -1.95 |
| 10-05 00:35 | +5 | ETH | UP | 0.64 | 0.71 | 0.38 |
| 10-05 00:34 | +10 stop | ZEC | UP | 0.60 | 0.28 | -3.52 |
| 10-05 00:34 | +10 stop | SOL | UP | 0.64 | 0.46 | -2.15 |
| 10-05 00:34 | +10 stop | XRP | UP | 0.63 | 0.48 | -1.85 |
| 10-05 00:33 | +10 stop | XRP | UP | 0.52 | 0.63 | 0.75 |
| 10-05 00:33 | +5 | BNB | UP | 0.61 | 0.66 | 0.17 |
| 10-05 00:33 | +10 stop | BNB | UP | 0.62 | 0.72 | 0.68 |
| 10-05 00:33 | +10 stop | ZEC | DOWN | 0.66 | 0.44 | -2.49 |
| 10-05 00:33 | +20 | ZEC | DOWN | 0.66 | open |  |
| 10-05 00:33 | +15 | ZEC | DOWN | 0.66 | open |  |
| 10-05 00:33 | +10 stop | NEAR | UP | 0.70 | 0.54 | -1.90 |
| 10-05 00:33 | +10 stop | ETH | UP | 0.66 | 0.42 | -2.74 |
| 10-05 00:33 | +20 | ETH | UP | 0.66 | 0.95 | 2.67 |
| 10-05 00:33 | +15 | ETH | UP | 0.66 | 0.81 | 1.23 |
| 10-05 00:33 | +10 | ETH | UP | 0.66 | 0.81 | 1.23 |
| 10-05 00:33 | +5 | ETH | UP | 0.66 | 0.71 | 0.19 |
| 10-05 00:32 | +10 stop | DOGE | UP | 0.61 | 0.72 | 0.78 |
