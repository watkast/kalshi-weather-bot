# Range-Scalp Bot

*Updated Sun Nov 22 14:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68813 | 60052 | 8761 (142) | 0 | $-18470.17 | -4.3% |
| **+10¢** | 51354 | 41122 | 10232 (186) | 0 | $-17113.48 | -5.3% |
| **+15¢** | 43038 | 32006 | 11032 (237) | 0 | $-15371.54 | -5.7% |
| **+20¢** | 38317 | 26726 | 11591 (295) | 0 | $-13677.33 | -5.7% |
| **+10¢ (15¢ stop)** | 83788 | 83603 | 185 (116) | 0 | $-30852.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 14:25 | +10 stop | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 11-22 14:25 | +10 | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 11-22 14:25 | +5 | BTC | DOWN | 0.71 | 0.79 | 0.53 |
| 11-22 14:23 | +10 stop | ETH | DOWN | 0.50 | 0.67 | 1.36 |
| 11-22 14:22 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 11-22 14:22 | +10 | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 11-22 14:22 | +10 stop | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-22 14:22 | +5 | XRP | DOWN | 0.65 | 0.72 | 0.39 |
| 11-22 14:22 | +10 stop | BNB | DOWN | 0.69 | 0.84 | 1.25 |
| 11-22 14:22 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-22 14:22 | +10 stop | SOL | UP | 0.45 | 0.21 | -2.70 |
| 11-22 14:21 | +10 stop | ETH | UP | 0.64 | 0.42 | -2.55 |
| 11-22 14:21 | +10 stop | XRP | DOWN | 0.47 | 0.65 | 1.47 |
| 11-22 14:21 | +10 | XRP | DOWN | 0.46 | 0.65 | 1.56 |
| 11-22 14:21 | +5 | XRP | DOWN | 0.47 | 0.54 | 0.34 |
| 11-22 14:21 | +5 | BNB | DOWN | 0.55 | 0.66 | 0.76 |
| 11-22 14:21 | +10 stop | ZEC | DOWN | 0.63 | 0.73 | 0.70 |
| 11-22 14:21 | +10 | ZEC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-22 14:21 | +5 | ZEC | DOWN | 0.62 | 0.68 | 0.27 |
| 11-22 14:21 | +5 | DOGE | DOWN | 0.64 | 0.72 | 0.48 |
| 11-22 14:21 | +20 | SOL | DOWN | 0.66 | 0.87 | 1.86 |
| 11-22 14:21 | +15 | SOL | DOWN | 0.67 | 0.84 | 1.44 |
| 11-22 14:21 | +10 | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 11-22 14:21 | +5 | SOL | DOWN | 0.65 | 0.78 | 1.01 |
| 11-22 14:20 | +10 stop | BTC | DOWN | 0.61 | 0.43 | -2.15 |
| 11-22 14:20 | +5 | BTC | DOWN | 0.61 | 0.66 | 0.17 |
| 11-22 14:19 | +10 stop | SOL | DOWN | 0.71 | 0.50 | -2.43 |
| 11-22 14:19 | +5 | DOGE | DOWN | 0.63 | 0.68 | 0.17 |
| 11-22 14:19 | +5 | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-22 14:18 | +10 stop | DOGE | DOWN | 0.66 | 0.51 | -1.84 |
| 11-22 14:18 | +20 | DOGE | DOWN | 0.67 | 0.88 | 1.86 |
| 11-22 14:18 | +15 | DOGE | DOWN | 0.67 | 0.83 | 1.34 |
| 11-22 14:18 | +10 | DOGE | DOWN | 0.67 | 0.79 | 0.92 |
| 11-22 14:18 | +5 | DOGE | DOWN | 0.67 | 0.72 | 0.19 |
| 11-22 14:17 | +5 | ETH | DOWN | 0.64 | 0.75 | 0.79 |
| 11-22 14:17 | +20 | BNB | DOWN | 0.70 | 0.93 | 2.10 |
| 11-22 14:17 | +15 | BNB | DOWN | 0.70 | 0.87 | 1.47 |
| 11-22 14:17 | +10 stop | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-22 14:17 | +20 | XRP | DOWN | 0.65 | 0.86 | 1.85 |
| 11-22 14:17 | +15 | XRP | DOWN | 0.65 | 0.80 | 1.22 |
