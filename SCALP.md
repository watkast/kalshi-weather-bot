# Range-Scalp Bot

*Updated Fri Oct 23 17:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30677 | 26728 | 3949 (39) | 0 | $-8905.01 | -4.6% |
| **+10¢** | 22960 | 18391 | 4569 (56) | 0 | $-7972.93 | -5.5% |
| **+15¢** | 19212 | 14295 | 4917 (79) | 0 | $-7206.29 | -6.0% |
| **+20¢** | 17018 | 11868 | 5150 (102) | 0 | $-6459.34 | -6.0% |
| **+10¢ (15¢ stop)** | 37632 | 37573 | 59 (32) | 0 | $-14316.47 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 17:24 | +10 stop | NEAR | UP | 0.53 | 0.36 | -2.05 |
| 10-23 17:23 | +10 stop | DOGE | UP | 0.53 | 0.34 | -2.24 |
| 10-23 17:23 | +10 stop | ZEC | UP | 0.67 | 0.39 | -3.13 |
| 10-23 17:22 | +10 | SOL | DOWN | 0.55 | 0.70 | 1.17 |
| 10-23 17:22 | +5 | SOL | DOWN | 0.55 | 0.70 | 1.17 |
| 10-23 17:22 | +10 stop | SOL | DOWN | 0.66 | 0.51 | -1.84 |
| 10-23 17:22 | +10 stop | ZEC | UP | 0.39 | 0.53 | 1.05 |
| 10-23 17:22 | +10 stop | DOGE | DOWN | 0.62 | 0.43 | -2.25 |
| 10-23 17:21 | +10 stop | BTC | DOWN | 0.67 | 0.82 | 1.23 |
| 10-23 17:21 | +10 stop | ZEC | UP | 0.55 | 0.67 | 0.86 |
| 10-23 17:21 | +10 stop | BNB | DOWN | 0.61 | 0.75 | 1.09 |
| 10-23 17:21 | +10 stop | ETH | UP | 0.65 | 0.47 | -2.14 |
| 10-23 17:21 | +10 stop | SOL | UP | 0.69 | 0.48 | -2.43 |
| 10-23 17:21 | +5 | HYPE | DOWN | 0.57 | 0.62 | 0.19 |
| 10-23 17:20 | +10 stop | XRP | UP | 0.63 | 0.48 | -1.85 |
| 10-23 17:20 | +10 stop | BTC | UP | 0.60 | 0.43 | -2.05 |
| 10-23 17:20 | +10 stop | DOGE | UP | 0.57 | 0.37 | -2.35 |
| 10-23 17:18 | +10 stop | BTC | DOWN | 0.60 | 0.37 | -2.64 |
| 10-23 17:18 | +10 stop | XRP | DOWN | 0.48 | 0.32 | -1.94 |
| 10-23 17:17 | +10 stop | NEAR | UP | 0.57 | 0.68 | 0.76 |
| 10-23 17:17 | +10 stop | SOL | DOWN | 0.54 | 0.37 | -2.05 |
| 10-23 17:17 | +20 | SOL | DOWN | 0.54 | 0.78 | 2.09 |
| 10-23 17:17 | +15 | SOL | DOWN | 0.54 | 0.70 | 1.27 |
| 10-23 17:17 | +10 | SOL | DOWN | 0.54 | 0.64 | 0.65 |
| 10-23 17:17 | +5 | SOL | DOWN | 0.54 | 0.64 | 0.65 |
| 10-23 17:17 | +10 stop | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-23 17:17 | +20 | HYPE | DOWN | 0.64 | 0.84 | 1.73 |
| 10-23 17:17 | +15 | HYPE | DOWN | 0.63 | 0.83 | 1.69 |
| 10-23 17:17 | +10 | HYPE | DOWN | 0.63 | 0.74 | 0.75 |
| 10-23 17:17 | +5 | HYPE | DOWN | 0.64 | 0.70 | 0.28 |
| 10-23 17:17 | +5 | ZEC | DOWN | 0.60 | 0.65 | 0.17 |
| 10-23 17:17 | +10 stop | DOGE | DOWN | 0.63 | 0.44 | -2.25 |
| 10-23 17:17 | +20 | DOGE | DOWN | 0.63 | 0.90 | 2.49 |
| 10-23 17:17 | +15 | DOGE | DOWN | 0.63 | 0.81 | 1.52 |
| 10-23 17:17 | +10 | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-23 17:17 | +5 | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-23 17:16 | +10 stop | ZEC | DOWN | 0.63 | 0.47 | -1.95 |
| 10-23 17:16 | +20 | ZEC | DOWN | 0.63 | 0.84 | 1.83 |
| 10-23 17:16 | +15 | ZEC | DOWN | 0.63 | 0.82 | 1.62 |
| 10-23 17:16 | +10 | ZEC | DOWN | 0.63 | 0.75 | 0.89 |
