# Range-Scalp Bot

*Updated Sun Oct 04 01:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 1555 | 1346 | 209 (2) | 0 | $-500.07 | -5.1% |
| **+10¢** | 1193 | 960 | 233 (4) | 0 | $-353.89 | -4.7% |
| **+15¢** | 1009 | 760 | 249 (5) | 0 | $-307.46 | -4.8% |
| **+20¢** | 893 | 625 | 268 (7) | 0 | $-325.86 | -5.8% |
| **+10¢ (15¢ stop)** | 1949 | 1948 | 1 (1) | 0 | $-823.75 | -6.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 01:22 | +10 stop | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 10-04 01:22 | +20 | HYPE | DOWN | 0.71 | 0.93 | 2.04 |
| 10-04 01:22 | +15 | HYPE | DOWN | 0.71 | 0.87 | 1.37 |
| 10-04 01:22 | +10 | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 10-04 01:22 | +5 | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 10-04 01:21 | +5 | BTC | DOWN | 0.65 | 0.72 | 0.39 |
| 10-04 01:16 | +10 stop | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-04 01:16 | +20 | ZEC | DOWN | 0.66 | 0.91 | 2.27 |
| 10-04 01:16 | +15 | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-04 01:16 | +10 | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-04 01:16 | +5 | ZEC | DOWN | 0.66 | 0.72 | 0.29 |
| 10-04 01:16 | +10 stop | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-04 01:16 | +20 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-04 01:16 | +15 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-04 01:16 | +10 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-04 01:16 | +5 | BTC | DOWN | 0.69 | 0.75 | 0.31 |
| 10-04 01:12 | +10 stop | BTC | UP | 0.62 | 0.74 | 0.89 |
| 10-04 01:12 | +20 | BTC | UP | 0.62 | no | -6.37 |
| 10-04 01:12 | +15 | BTC | UP | 0.62 | no | -6.37 |
| 10-04 01:12 | +10 | BTC | UP | 0.62 | 0.74 | 0.89 |
| 10-04 01:12 | +5 | BTC | UP | 0.62 | 0.74 | 0.89 |
| 10-04 01:11 | +10 stop | NEAR | DOWN | 0.57 | 0.74 | 1.38 |
| 10-04 01:11 | +10 stop | ZEC | UP | 0.57 | 0.24 | -3.63 |
| 10-04 01:10 | +10 stop | ZEC | DOWN | 0.62 | 0.42 | -2.35 |
| 10-04 01:10 | +20 | ZEC | DOWN | 0.62 | 0.89 | 2.46 |
| 10-04 01:10 | +15 | ZEC | DOWN | 0.62 | 0.89 | 2.46 |
| 10-04 01:10 | +10 | ZEC | DOWN | 0.62 | 0.75 | 0.99 |
| 10-04 01:10 | +5 | ZEC | DOWN | 0.62 | 0.75 | 0.99 |
| 10-04 01:08 | +10 stop | SOL | UP | 0.67 | 0.51 | -1.94 |
| 10-04 01:08 | +20 | SOL | UP | 0.67 | 0.89 | 1.97 |
| 10-04 01:08 | +15 | SOL | UP | 0.67 | 0.86 | 1.65 |
| 10-04 01:08 | +10 | SOL | UP | 0.67 | 0.86 | 1.65 |
| 10-04 01:08 | +5 | SOL | UP | 0.67 | 0.86 | 1.65 |
| 10-04 01:08 | +10 stop | ETH | UP | 0.62 | 0.84 | 1.93 |
| 10-04 01:07 | +10 stop | DOGE | DOWN | 0.66 | 0.17 | -5.16 |
| 10-04 01:07 | +10 stop | BTC | DOWN | 0.58 | 0.30 | -3.13 |
| 10-04 01:07 | +5 | BTC | DOWN | 0.58 | 0.64 | 0.25 |
| 10-04 01:07 | +10 | HYPE | UP | 0.64 | 0.76 | 0.90 |
| 10-04 01:07 | +5 | HYPE | UP | 0.63 | 0.71 | 0.48 |
| 10-04 01:07 | +10 stop | XRP | DOWN | 0.62 | 0.80 | 1.53 |
