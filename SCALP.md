# Range-Scalp Bot

*Updated Sun Nov 22 01:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68075 | 59413 | 8662 (138) | 0 | $-18246.92 | -4.3% |
| **+10¢** | 50825 | 40708 | 10117 (181) | 0 | $-16907.71 | -5.3% |
| **+15¢** | 42604 | 31696 | 10908 (230) | 0 | $-15175.90 | -5.7% |
| **+20¢** | 37929 | 26465 | 11464 (288) | 0 | $-13492.85 | -5.7% |
| **+10¢ (15¢ stop)** | 82868 | 82690 | 178 (110) | 0 | $-30416.51 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 01:25 | +5 | BTC | DOWN | 0.67 | 0.82 | 1.23 |
| 11-22 01:24 | +10 stop | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-22 01:24 | +10 | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-22 01:24 | +5 | BTC | DOWN | 0.59 | 0.65 | 0.27 |
| 11-22 01:24 | +10 stop | ETH | UP | 0.67 | 0.80 | 1.02 |
| 11-22 01:20 | +10 stop | BTC | UP | 0.59 | 0.30 | -3.22 |
| 11-22 01:19 | +10 stop | ETH | UP | 0.69 | 0.79 | 0.73 |
| 11-22 01:18 | +5 | SOL | DOWN | 0.65 | 0.70 | 0.19 |
| 11-22 01:17 | +5 | SOL | DOWN | 0.58 | 0.66 | 0.46 |
| 11-22 01:17 | +5 | DOGE | DOWN | 0.63 | 0.71 | 0.48 |
| 11-22 01:17 | +10 stop | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-22 01:17 | +10 | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-22 01:17 | +5 | ZEC | DOWN | 0.67 | 0.72 | 0.19 |
| 11-22 01:17 | +5 | ETH | DOWN | 0.56 | 0.72 | 1.27 |
| 11-22 01:16 | +20 | BNB | DOWN | 0.71 | 0.92 | 1.90 |
| 11-22 01:16 | +15 | BNB | DOWN | 0.71 | 0.87 | 1.37 |
| 11-22 01:16 | +10 | BNB | DOWN | 0.71 | 0.83 | 0.95 |
| 11-22 01:16 | +5 | BNB | DOWN | 0.70 | 0.77 | 0.42 |
| 11-22 01:16 | +10 stop | BTC | DOWN | 0.56 | 0.36 | -2.35 |
| 11-22 01:16 | +20 | BTC | DOWN | 0.57 | 0.82 | 2.21 |
| 11-22 01:16 | +15 | BTC | DOWN | 0.57 | 0.82 | 2.21 |
| 11-22 01:16 | +10 | BTC | DOWN | 0.57 | 0.69 | 0.87 |
| 11-22 01:16 | +5 | BTC | DOWN | 0.57 | 0.69 | 0.87 |
| 11-22 01:16 | +10 stop | NEAR | DOWN | 0.67 | 0.50 | -2.04 |
| 11-22 01:16 | +20 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 11-22 01:16 | +15 | NEAR | DOWN | 0.67 | 0.83 | 1.34 |
| 11-22 01:16 | +10 | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-22 01:16 | +5 | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-22 01:16 | +5 | ETH | DOWN | 0.50 | 0.59 | 0.55 |
| 11-22 01:16 | +10 stop | XRP | DOWN | 0.60 | 0.74 | 1.09 |
| 11-22 01:16 | +20 | XRP | DOWN | 0.55 | 0.75 | 1.68 |
| 11-22 01:16 | +15 | XRP | DOWN | 0.55 | 0.74 | 1.58 |
| 11-22 01:16 | +10 | XRP | DOWN | 0.55 | 0.67 | 0.86 |
| 11-22 01:16 | +5 | XRP | DOWN | 0.55 | 0.60 | 0.15 |
| 11-22 01:15 | +10 stop | ETH | DOWN | 0.58 | 0.43 | -1.86 |
| 11-22 01:15 | +20 | ETH | DOWN | 0.58 | 0.81 | 2.01 |
| 11-22 01:15 | +15 | ETH | DOWN | 0.58 | 0.76 | 1.49 |
| 11-22 01:15 | +10 | ETH | DOWN | 0.58 | 0.72 | 1.07 |
| 11-22 01:15 | +5 | ETH | DOWN | 0.57 | 0.62 | 0.15 |
| 11-22 01:15 | +10 stop | ZEC | DOWN | 0.60 | 0.70 | 0.68 |
