# Range-Scalp Bot

*Updated Mon Oct 12 09:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13368 | 11564 | 1804 (25) | 0 | $-4265.62 | -5.1% |
| **+10¢** | 10127 | 8036 | 2091 (37) | 0 | $-3977.26 | -6.2% |
| **+15¢** | 8521 | 6287 | 2234 (55) | 1 | $-3482.55 | -6.5% |
| **+20¢** | 7584 | 5254 | 2330 (70) | 1 | $-2956.86 | -6.2% |
| **+10¢ (15¢ stop)** | 16446 | 16405 | 41 (25) | 0 | $-6404.79 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 09:26 | +10 stop | ETH | DOWN | 0.63 | 0.84 | 1.80 |
| 10-12 09:26 | +20 | ETH | DOWN | 0.64 | 0.84 | 1.78 |
| 10-12 09:26 | +15 | ETH | DOWN | 0.64 | 0.84 | 1.78 |
| 10-12 09:26 | +10 | ETH | DOWN | 0.63 | 0.84 | 1.83 |
| 10-12 09:26 | +5 | ETH | DOWN | 0.63 | 0.84 | 1.83 |
| 10-12 09:21 | +10 stop | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 10-12 09:21 | +5 | SOL | DOWN | 0.71 | 0.78 | 0.42 |
| 10-12 09:21 | +5 | XRP | DOWN | 0.67 | 0.82 | 1.23 |
| 10-12 09:21 | +10 stop | NEAR | UP | 0.63 | 0.87 | 2.15 |
| 10-12 09:21 | +10 | NEAR | UP | 0.63 | 0.87 | 2.15 |
| 10-12 09:21 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-12 09:21 | +20 | DOGE | DOWN | 0.64 | 0.88 | 2.15 |
| 10-12 09:21 | +15 | DOGE | DOWN | 0.64 | 0.81 | 1.42 |
| 10-12 09:21 | +10 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-12 09:21 | +5 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-12 09:21 | +5 | NEAR | UP | 0.69 | 0.87 | 1.57 |
| 10-12 09:20 | +10 stop | ZEC | DOWN | 0.66 | 0.79 | 1.02 |
| 10-12 09:20 | +10 stop | SOL | DOWN | 0.61 | 0.45 | -1.95 |
| 10-12 09:20 | +20 | SOL | DOWN | 0.61 | 0.82 | 1.81 |
| 10-12 09:20 | +15 | SOL | DOWN | 0.61 | 0.78 | 1.39 |
| 10-12 09:20 | +10 | SOL | DOWN | 0.61 | 0.73 | 0.89 |
| 10-12 09:20 | +5 | SOL | DOWN | 0.61 | 0.66 | 0.17 |
| 10-12 09:20 | +10 stop | ETH | DOWN | 0.69 | 0.83 | 1.15 |
| 10-12 09:20 | +20 | ETH | DOWN | 0.69 | 0.96 | 2.51 |
| 10-12 09:20 | +15 | ETH | DOWN | 0.69 | 0.85 | 1.36 |
| 10-12 09:20 | +10 | ETH | DOWN | 0.69 | 0.83 | 1.15 |
| 10-12 09:20 | +5 | ETH | DOWN | 0.69 | 0.76 | 0.42 |
| 10-12 09:20 | +10 stop | XRP | DOWN | 0.65 | 0.82 | 1.43 |
| 10-12 09:20 | +20 | XRP | DOWN | 0.65 | 0.86 | 1.85 |
| 10-12 09:20 | +15 | XRP | DOWN | 0.65 | 0.82 | 1.43 |
| 10-12 09:20 | +10 | XRP | DOWN | 0.65 | 0.82 | 1.43 |
| 10-12 09:20 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
| 10-12 09:20 | +10 stop | NEAR | UP | 0.52 | 0.69 | 1.37 |
| 10-12 09:20 | +10 | NEAR | UP | 0.52 | 0.69 | 1.37 |
| 10-12 09:20 | +5 | NEAR | UP | 0.52 | 0.60 | 0.45 |
| 10-12 09:19 | +5 | ZEC | DOWN | 0.60 | 0.66 | 0.27 |
| 10-12 09:19 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 10-12 09:18 | +5 | ZEC | DOWN | 0.59 | 0.68 | 0.53 |
| 10-12 09:17 | +5 | SOL | DOWN | 0.57 | 0.70 | 0.97 |
| 10-12 09:17 | +5 | ETH | DOWN | 0.57 | 0.72 | 1.17 |
