# Range-Scalp Bot

*Updated Mon Oct 05 16:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3981 | 3415 | 566 (4) | 0 | $-1468.31 | -5.8% |
| **+10¢** | 3081 | 2430 | 651 (5) | 0 | $-1355.52 | -7.0% |
| **+15¢** | 2592 | 1908 | 684 (8) | 0 | $-1164.07 | -7.2% |
| **+20¢** | 2312 | 1599 | 713 (13) | 0 | $-1009.38 | -7.0% |
| **+10¢ (15¢ stop)** | 4921 | 4916 | 5 (2) | 0 | $-1826.63 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 16:18 | +10 stop | NEAR | DOWN | 0.60 | 0.71 | 0.78 |
| 10-05 16:18 | +5 | HYPE | DOWN | 0.66 | 0.74 | 0.50 |
| 10-05 16:17 | +10 stop | NEAR | DOWN | 0.68 | 0.52 | -1.90 |
| 10-05 16:17 | +20 | NEAR | DOWN | 0.68 | 0.88 | 1.80 |
| 10-05 16:17 | +15 | NEAR | DOWN | 0.68 | 0.84 | 1.32 |
| 10-05 16:17 | +10 | NEAR | DOWN | 0.67 | 0.79 | 0.93 |
| 10-05 16:17 | +5 | NEAR | DOWN | 0.67 | 0.79 | 0.93 |
| 10-05 16:16 | +10 stop | HYPE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-05 16:16 | +20 | HYPE | DOWN | 0.66 | 0.88 | 1.96 |
| 10-05 16:16 | +15 | HYPE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-05 16:16 | +10 | HYPE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-05 16:16 | +5 | HYPE | DOWN | 0.66 | 0.72 | 0.29 |
| 10-05 16:15 | +10 stop | ZEC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-05 16:15 | +20 | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 10-05 16:15 | +15 | ZEC | DOWN | 0.63 | 0.78 | 1.20 |
| 10-05 16:15 | +10 | ZEC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-05 16:15 | +5 | ZEC | DOWN | 0.63 | 0.72 | 0.58 |
| 10-05 16:15 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-05 16:15 | +20 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-05 16:15 | +15 | BTC | DOWN | 0.69 | 0.85 | 1.36 |
| 10-05 16:15 | +10 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-05 16:15 | +5 | BTC | DOWN | 0.69 | 0.75 | 0.31 |
| 10-05 16:15 | +10 stop | DOGE | DOWN | 0.60 | 0.74 | 1.09 |
| 10-05 16:15 | +20 | DOGE | DOWN | 0.60 | 0.82 | 1.92 |
| 10-05 16:15 | +15 | DOGE | DOWN | 0.60 | 0.76 | 1.30 |
| 10-05 16:15 | +10 | DOGE | DOWN | 0.60 | 0.74 | 1.09 |
| 10-05 16:15 | +5 | DOGE | DOWN | 0.60 | 0.74 | 1.09 |
| 10-05 16:15 | +10 stop | ETH | DOWN | 0.58 | 0.78 | 1.69 |
| 10-05 16:15 | +20 | ETH | DOWN | 0.58 | 0.78 | 1.69 |
| 10-05 16:15 | +15 | ETH | DOWN | 0.58 | 0.78 | 1.69 |
| 10-05 16:15 | +10 | ETH | DOWN | 0.58 | 0.78 | 1.69 |
| 10-05 16:15 | +5 | ETH | DOWN | 0.58 | 0.78 | 1.69 |
| 10-05 16:13 | +10 stop | BNB | UP | 0.63 | 0.84 | 1.83 |
| 10-05 16:12 | +10 stop | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 10-05 16:11 | +10 stop | ZEC | UP | 0.69 | 0.48 | -2.43 |
| 10-05 16:11 | +5 | ZEC | UP | 0.69 | no | -7.05 |
| 10-05 16:11 | +5 | ETH | DOWN | 0.68 | 0.74 | 0.30 |
| 10-05 16:10 | +10 stop | ETH | UP | 0.48 | 0.32 | -1.94 |
| 10-05 16:10 | +15 | ETH | UP | 0.48 | no | -4.98 |
| 10-05 16:10 | +10 | ETH | UP | 0.48 | no | -4.98 |
