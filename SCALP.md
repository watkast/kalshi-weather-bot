# Range-Scalp Bot

*Updated Thu Oct 22 23:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29451 | 25632 | 3819 (39) | 0 | $-8707.62 | -4.7% |
| **+10¢** | 22083 | 17660 | 4423 (55) | 0 | $-7865.62 | -5.7% |
| **+15¢** | 18491 | 13743 | 4748 (78) | 0 | $-7037.38 | -6.1% |
| **+20¢** | 16362 | 11385 | 4977 (100) | 0 | $-6386.88 | -6.2% |
| **+10¢ (15¢ stop)** | 36147 | 36088 | 59 (32) | 0 | $-13642.51 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 23:28 | +10 stop | NEAR | DOWN | 0.66 | 0.81 | 1.27 |
| 10-22 23:28 | +10 stop | ZEC | DOWN | 0.69 | 0.80 | 0.83 |
| 10-22 23:27 | +10 stop | BNB | UP | 0.67 | 0.79 | 0.92 |
| 10-22 23:27 | +10 | BNB | UP | 0.67 | 0.79 | 0.92 |
| 10-22 23:27 | +5 | BNB | UP | 0.68 | 0.79 | 0.82 |
| 10-22 23:27 | +10 stop | HYPE | DOWN | 0.68 | 0.41 | -3.03 |
| 10-22 23:27 | +15 | HYPE | DOWN | 0.68 | 0.98 | 2.84 |
| 10-22 23:27 | +10 | HYPE | DOWN | 0.68 | 0.98 | 2.84 |
| 10-22 23:27 | +5 | HYPE | DOWN | 0.68 | 0.98 | 2.84 |
| 10-22 23:27 | +10 stop | ZEC | DOWN | 0.37 | 0.55 | 1.45 |
| 10-22 23:26 | +10 stop | NEAR | DOWN | 0.66 | 0.46 | -2.34 |
| 10-22 23:26 | +5 | NEAR | DOWN | 0.66 | 0.81 | 1.23 |
| 10-22 23:26 | +10 stop | ZEC | UP | 0.62 | 0.47 | -1.85 |
| 10-22 23:25 | +10 stop | HYPE | DOWN | 0.50 | 0.65 | 1.16 |
| 10-22 23:25 | +10 | HYPE | DOWN | 0.50 | 0.65 | 1.16 |
| 10-22 23:25 | +10 stop | ETH | DOWN | 0.71 | 0.56 | -1.83 |
| 10-22 23:25 | +5 | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 10-22 23:24 | +10 stop | DOGE | UP | 0.62 | 0.79 | 1.41 |
| 10-22 23:24 | +5 | HYPE | DOWN | 0.71 | 0.77 | 0.32 |
| 10-22 23:24 | +5 | NEAR | DOWN | 0.64 | 0.72 | 0.48 |
| 10-22 23:23 | +10 stop | BTC | DOWN | 0.64 | 0.78 | 1.10 |
| 10-22 23:23 | +20 | BTC | DOWN | 0.64 | 0.89 | 2.26 |
| 10-22 23:23 | +15 | BTC | DOWN | 0.64 | 0.89 | 2.26 |
| 10-22 23:23 | +10 | BTC | DOWN | 0.64 | 0.78 | 1.10 |
| 10-22 23:23 | +5 | BTC | DOWN | 0.64 | 0.70 | 0.28 |
| 10-22 23:23 | +10 stop | HYPE | DOWN | 0.61 | 0.74 | 0.99 |
| 10-22 23:23 | +15 | HYPE | DOWN | 0.61 | 0.77 | 1.30 |
| 10-22 23:23 | +10 | HYPE | DOWN | 0.61 | 0.74 | 0.99 |
| 10-22 23:23 | +5 | HYPE | DOWN | 0.61 | 0.66 | 0.17 |
| 10-22 23:23 | +5 | BNB | DOWN | 0.69 | 0.77 | 0.52 |
| 10-22 23:23 | +10 stop | NEAR | DOWN | 0.55 | 0.67 | 0.86 |
| 10-22 23:23 | +5 | NEAR | DOWN | 0.55 | 0.61 | 0.25 |
| 10-22 23:22 | +10 stop | DOGE | DOWN | 0.49 | 0.34 | -1.84 |
| 10-22 23:22 | +10 | DOGE | DOWN | 0.49 | yes | -5.08 |
| 10-22 23:21 | +10 stop | ZEC | DOWN | 0.71 | 0.40 | -3.42 |
| 10-22 23:21 | +5 | DOGE | DOWN | 0.62 | yes | -6.37 |
| 10-22 23:21 | +10 stop | ETH | DOWN | 0.66 | 0.47 | -2.24 |
| 10-22 23:21 | +15 | ETH | DOWN | 0.66 | 0.83 | 1.44 |
| 10-22 23:21 | +10 | ETH | DOWN | 0.66 | 0.83 | 1.44 |
| 10-22 23:21 | +5 | ETH | DOWN | 0.66 | 0.71 | 0.19 |
