# Range-Scalp Bot

*Updated Tue Nov 17 08:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62839 | 54808 | 8031 (117) | 0 | $-17143.66 | -4.3% |
| **+10¢** | 46929 | 37532 | 9397 (159) | 0 | $-16027.43 | -5.4% |
| **+15¢** | 39335 | 29200 | 10135 (201) | 0 | $-14580.59 | -5.9% |
| **+20¢** | 35054 | 24427 | 10627 (256) | 0 | $-12755.76 | -5.8% |
| **+10¢ (15¢ stop)** | 76462 | 76306 | 156 (92) | 0 | $-28160.01 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 08:33 | +10 stop | NEAR | DOWN | 0.64 | 0.75 | 0.79 |
| 11-17 08:33 | +20 | NEAR | DOWN | 0.64 | 0.91 | 2.43 |
| 11-17 08:33 | +15 | NEAR | DOWN | 0.64 | 0.91 | 2.43 |
| 11-17 08:33 | +10 | NEAR | DOWN | 0.64 | 0.75 | 0.79 |
| 11-17 08:33 | +5 | NEAR | DOWN | 0.64 | 0.75 | 0.79 |
| 11-17 08:28 | +10 stop | ZEC | DOWN | 0.62 | 0.75 | 0.99 |
| 11-17 08:26 | +10 stop | ZEC | UP | 0.66 | 0.77 | 0.81 |
| 11-17 08:25 | +10 stop | XRP | DOWN | 0.62 | 0.37 | -2.84 |
| 11-17 08:24 | +10 stop | ZEC | DOWN | 0.66 | 0.41 | -2.83 |
| 11-17 08:24 | +10 stop | BTC | DOWN | 0.69 | 0.86 | 1.46 |
| 11-17 08:24 | +10 | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 11-17 08:24 | +5 | BTC | DOWN | 0.71 | 0.77 | 0.32 |
| 11-17 08:24 | +10 stop | ETH | DOWN | 0.61 | 0.72 | 0.78 |
| 11-17 08:24 | +5 | ETH | DOWN | 0.61 | 0.67 | 0.27 |
| 11-17 08:23 | +10 stop | BNB | UP | 0.67 | 0.79 | 0.92 |
| 11-17 08:23 | +20 | BNB | UP | 0.67 | 0.87 | 1.76 |
| 11-17 08:23 | +15 | BNB | UP | 0.67 | 0.87 | 1.76 |
| 11-17 08:23 | +10 | BNB | UP | 0.67 | 0.79 | 0.92 |
| 11-17 08:23 | +5 | BNB | UP | 0.67 | 0.79 | 0.92 |
| 11-17 08:22 | +10 stop | ZEC | DOWN | 0.52 | 0.65 | 0.96 |
| 11-17 08:22 | +10 stop | NEAR | UP | 0.71 | 0.88 | 1.47 |
| 11-17 08:22 | +10 stop | BTC | DOWN | 0.61 | 0.73 | 0.89 |
| 11-17 08:22 | +10 | BTC | DOWN | 0.61 | 0.73 | 0.89 |
| 11-17 08:22 | +5 | BTC | DOWN | 0.61 | 0.73 | 0.89 |
| 11-17 08:22 | +10 stop | ETH | DOWN | 0.53 | 0.70 | 1.37 |
| 11-17 08:22 | +10 stop | XRP | DOWN | 0.58 | 0.71 | 0.97 |
| 11-17 08:22 | +10 stop | HYPE | UP | 0.65 | 0.43 | -2.52 |
| 11-17 08:21 | +10 stop | ETH | UP | 0.44 | 0.66 | 1.86 |
| 11-17 08:21 | +10 stop | DOGE | DOWN | 0.68 | 0.53 | -1.84 |
| 11-17 08:21 | +15 | DOGE | DOWN | 0.69 | 0.86 | 1.46 |
| 11-17 08:21 | +10 | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-17 08:21 | +5 | DOGE | DOWN | 0.63 | 0.72 | 0.58 |
| 11-17 08:21 | +10 stop | SOL | DOWN | 0.51 | 0.66 | 1.16 |
| 11-17 08:21 | +10 | SOL | DOWN | 0.51 | 0.66 | 1.16 |
| 11-17 08:21 | +5 | SOL | DOWN | 0.50 | 0.66 | 1.26 |
| 11-17 08:21 | +20 | ZEC | DOWN | 0.65 | yes | -6.66 |
| 11-17 08:21 | +10 stop | NEAR | UP | 0.55 | 0.70 | 1.20 |
| 11-17 08:21 | +10 stop | ETH | DOWN | 0.65 | 0.43 | -2.54 |
| 11-17 08:21 | +20 | ETH | DOWN | 0.65 | 0.86 | 1.85 |
| 11-17 08:21 | +15 | ETH | DOWN | 0.65 | 0.86 | 1.85 |
