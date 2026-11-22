# Range-Scalp Bot

*Updated Sun Nov 22 05:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68297 | 59597 | 8700 (138) | 0 | $-18385.33 | -4.3% |
| **+10¢** | 51000 | 40840 | 10160 (181) | 0 | $-17043.25 | -5.3% |
| **+15¢** | 42750 | 31796 | 10954 (231) | 0 | $-15300.49 | -5.7% |
| **+20¢** | 38056 | 26543 | 11513 (289) | 0 | $-13640.62 | -5.7% |
| **+10¢ (15¢ stop)** | 83163 | 82984 | 179 (111) | 0 | $-30535.46 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 05:16 | +10 stop | BTC | DOWN | 0.67 | 0.81 | 1.13 |
| 11-22 05:16 | +20 | BTC | DOWN | 0.67 | 0.88 | 1.86 |
| 11-22 05:16 | +15 | BTC | DOWN | 0.67 | 0.86 | 1.65 |
| 11-22 05:16 | +10 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-22 05:16 | +5 | BTC | DOWN | 0.66 | 0.71 | 0.19 |
| 11-22 05:16 | +10 | DOGE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-22 05:16 | +5 | DOGE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-22 05:16 | +10 stop | DOGE | DOWN | 0.70 | 0.83 | 1.05 |
| 11-22 05:16 | +20 | DOGE | DOWN | 0.70 | 0.96 | 2.39 |
| 11-22 05:16 | +15 | DOGE | DOWN | 0.71 | 0.87 | 1.37 |
| 11-22 05:16 | +10 stop | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 11-22 05:16 | +20 | XRP | DOWN | 0.69 | 0.89 | 1.78 |
| 11-22 05:16 | +15 | XRP | DOWN | 0.69 | 0.87 | 1.57 |
| 11-22 05:16 | +10 | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 11-22 05:16 | +5 | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 11-22 05:16 | +10 stop | ETH | DOWN | 0.68 | 0.81 | 1.03 |
| 11-22 05:16 | +20 | ETH | DOWN | 0.71 | 0.94 | 2.11 |
| 11-22 05:16 | +15 | ETH | DOWN | 0.71 | 0.87 | 1.37 |
| 11-22 05:16 | +10 | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 11-22 05:16 | +5 | ETH | DOWN | 0.71 | 0.76 | 0.22 |
| 11-22 05:16 | +10 stop | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 11-22 05:16 | +20 | SOL | DOWN | 0.67 | 0.87 | 1.76 |
| 11-22 05:16 | +15 | SOL | DOWN | 0.67 | 0.83 | 1.34 |
| 11-22 05:16 | +10 | SOL | DOWN | 0.66 | 0.79 | 1.02 |
| 11-22 05:16 | +5 | SOL | DOWN | 0.66 | 0.75 | 0.60 |
| 11-22 05:12 | +10 stop | ZEC | DOWN | 0.52 | 0.63 | 0.78 |
| 11-22 05:12 | +10 | ZEC | DOWN | 0.51 | 0.63 | 0.85 |
| 11-22 05:12 | +5 | ZEC | DOWN | 0.50 | 0.63 | 0.95 |
| 11-22 05:11 | +10 stop | NEAR | UP | 0.61 | 0.86 | 2.21 |
| 11-22 05:10 | +10 stop | NEAR | DOWN | 0.67 | 0.43 | -2.74 |
| 11-22 05:10 | +10 stop | ZEC | DOWN | 0.60 | 0.74 | 1.09 |
| 11-22 05:10 | +15 | ZEC | DOWN | 0.62 | yes | -6.37 |
| 11-22 05:10 | +10 | ZEC | DOWN | 0.61 | 0.74 | 0.99 |
| 11-22 05:10 | +5 | ZEC | DOWN | 0.62 | 0.74 | 0.89 |
| 11-22 05:08 | +10 stop | NEAR | DOWN | 0.68 | 0.51 | -2.04 |
| 11-22 05:05 | +10 stop | NEAR | DOWN | 0.68 | 0.53 | -1.84 |
| 11-22 05:05 | +20 | NEAR | DOWN | 0.68 | yes | -6.96 |
| 11-22 05:05 | +15 | NEAR | DOWN | 0.68 | yes | -6.96 |
| 11-22 05:05 | +10 | NEAR | DOWN | 0.68 | yes | -6.96 |
| 11-22 05:05 | +5 | NEAR | DOWN | 0.69 | yes | -7.05 |
