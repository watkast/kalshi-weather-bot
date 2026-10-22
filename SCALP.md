# Range-Scalp Bot

*Updated Thu Oct 22 00:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27984 | 24379 | 3605 (39) | 0 | $-8073.34 | -4.6% |
| **+10¢** | 21024 | 16861 | 4163 (55) | 0 | $-7110.80 | -5.4% |
| **+15¢** | 17612 | 13132 | 4480 (78) | 0 | $-6340.30 | -5.7% |
| **+20¢** | 15590 | 10895 | 4695 (98) | 0 | $-5678.22 | -5.8% |
| **+10¢ (15¢ stop)** | 34364 | 34305 | 59 (32) | 0 | $-12838.98 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 00:42 | +5 | NEAR | DOWN | 0.29 | 0.54 | 2.17 |
| 10-22 00:42 | +10 stop | HYPE | UP | 0.66 | 0.76 | 0.71 |
| 10-22 00:41 | +10 stop | DOGE | UP | 0.57 | 0.86 | 2.63 |
| 10-22 00:41 | +10 stop | NEAR | UP | 0.44 | 0.81 | 3.41 |
| 10-22 00:41 | +15 | NEAR | UP | 0.44 | 0.81 | 3.41 |
| 10-22 00:41 | +10 | NEAR | UP | 0.44 | 0.81 | 3.41 |
| 10-22 00:41 | +5 | NEAR | UP | 0.44 | 0.53 | 0.54 |
| 10-22 00:40 | +10 stop | BNB | DOWN | 0.43 | 0.57 | 1.00 |
| 10-22 00:39 | +10 stop | HYPE | UP | 0.67 | 0.80 | 1.02 |
| 10-22 00:39 | +10 stop | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 10-22 00:39 | +10 stop | ETH | UP | 0.68 | 0.83 | 1.24 |
| 10-22 00:38 | +10 stop | NEAR | DOWN | 0.61 | 0.75 | 1.11 |
| 10-22 00:38 | +10 | NEAR | DOWN | 0.61 | 0.75 | 1.11 |
| 10-22 00:38 | +5 | NEAR | DOWN | 0.61 | 0.67 | 0.29 |
| 10-22 00:37 | +10 stop | SOL | UP | 0.61 | 0.73 | 0.92 |
| 10-22 00:37 | +10 stop | DOGE | UP | 0.60 | 0.41 | -2.24 |
| 10-22 00:37 | +10 stop | XRP | UP | 0.67 | 0.49 | -2.14 |
| 10-22 00:36 | +10 stop | ZEC | DOWN | 0.64 | 0.78 | 1.10 |
| 10-22 00:36 | +15 | ZEC | DOWN | 0.64 | 0.87 | 2.05 |
| 10-22 00:36 | +10 | ZEC | DOWN | 0.64 | 0.78 | 1.10 |
| 10-22 00:36 | +5 | ZEC | DOWN | 0.64 | 0.72 | 0.48 |
| 10-22 00:36 | +10 stop | BNB | DOWN | 0.60 | 0.45 | -1.89 |
| 10-22 00:36 | +10 stop | ETH | UP | 0.59 | 0.70 | 0.78 |
| 10-22 00:35 | +10 stop | ZEC | DOWN | 0.48 | 0.66 | 1.46 |
| 10-22 00:35 | +20 | ZEC | DOWN | 0.48 | 0.72 | 2.07 |
| 10-22 00:35 | +15 | ZEC | DOWN | 0.48 | 0.66 | 1.46 |
| 10-22 00:35 | +10 | ZEC | DOWN | 0.48 | 0.66 | 1.46 |
| 10-22 00:35 | +5 | ZEC | DOWN | 0.48 | 0.66 | 1.46 |
| 10-22 00:35 | +10 stop | NEAR | DOWN | 0.58 | 0.68 | 0.66 |
| 10-22 00:35 | +15 | NEAR | DOWN | 0.58 | 0.75 | 1.38 |
| 10-22 00:35 | +10 | NEAR | DOWN | 0.58 | 0.68 | 0.66 |
| 10-22 00:35 | +5 | NEAR | DOWN | 0.58 | 0.68 | 0.66 |
| 10-22 00:35 | +10 stop | SOL | UP | 0.69 | 0.50 | -2.23 |
| 10-22 00:35 | +10 stop | DOGE | UP | 0.67 | 0.48 | -2.22 |
| 10-22 00:35 | +10 stop | HYPE | UP | 0.71 | 0.56 | -1.83 |
| 10-22 00:35 | +10 stop | BTC | UP | 0.63 | 0.74 | 0.79 |
| 10-22 00:34 | +10 stop | XRP | DOWN | 0.55 | 0.36 | -2.25 |
| 10-22 00:34 | +10 stop | HYPE | DOWN | 0.57 | 0.42 | -1.86 |
| 10-22 00:34 | +10 stop | DOGE | DOWN | 0.58 | 0.38 | -2.35 |
| 10-22 00:34 | +10 stop | BNB | DOWN | 0.69 | 0.52 | -2.03 |
