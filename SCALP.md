# Range-Scalp Bot

*Updated Sun Nov 08 17:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52564 | 45824 | 6740 (83) | 2 | $-14591.01 | -4.4% |
| **+10¢** | 39243 | 31389 | 7854 (108) | 2 | $-13571.52 | -5.5% |
| **+15¢** | 32878 | 24412 | 8466 (139) | 1 | $-12434.91 | -6.0% |
| **+20¢** | 29249 | 20377 | 8872 (183) | 1 | $-10931.07 | -6.0% |
| **+10¢ (15¢ stop)** | 64034 | 63928 | 106 (63) | 0 | $-23733.70 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 17:26 | +10 stop | SOL | UP | 0.57 | 0.36 | -2.45 |
| 11-08 17:26 | +10 stop | ETH | UP | 0.58 | 0.30 | -3.13 |
| 11-08 17:26 | +10 stop | DOGE | UP | 0.34 | 0.55 | 1.76 |
| 11-08 17:26 | +10 stop | BTC | UP | 0.55 | 0.34 | -2.44 |
| 11-08 17:26 | +10 | BTC | UP | 0.55 | open |  |
| 11-08 17:26 | +5 | BTC | UP | 0.55 | open |  |
| 11-08 17:24 | +10 stop | XRP | DOWN | 0.65 | 0.81 | 1.34 |
| 11-08 17:24 | +10 stop | HYPE | UP | 0.55 | 0.39 | -1.97 |
| 11-08 17:23 | +10 stop | BTC | UP | 0.69 | 0.80 | 0.83 |
| 11-08 17:23 | +10 stop | BNB | UP | 0.58 | 0.74 | 1.28 |
| 11-08 17:23 | +15 | HYPE | DOWN | 0.63 | 0.78 | 1.20 |
| 11-08 17:23 | +5 | HYPE | DOWN | 0.63 | 0.78 | 1.20 |
| 11-08 17:23 | +10 stop | XRP | DOWN | 0.69 | 0.48 | -2.43 |
| 11-08 17:23 | +10 | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 11-08 17:23 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 11-08 17:22 | +10 stop | DOGE | UP | 0.68 | 0.79 | 0.82 |
| 11-08 17:22 | +10 stop | BNB | UP | 0.49 | 0.63 | 1.05 |
| 11-08 17:22 | +10 stop | BTC | UP | 0.51 | 0.64 | 0.95 |
| 11-08 17:21 | +10 stop | HYPE | DOWN | 0.63 | 0.42 | -2.47 |
| 11-08 17:21 | +10 stop | BNB | UP | 0.67 | 0.52 | -1.84 |
| 11-08 17:21 | +10 stop | XRP | DOWN | 0.56 | 0.70 | 1.08 |
| 11-08 17:21 | +10 stop | ETH | UP | 0.58 | 0.73 | 1.18 |
| 11-08 17:20 | +10 stop | BTC | UP | 0.63 | 0.48 | -1.85 |
| 11-08 17:20 | +10 | BTC | UP | 0.63 | 0.80 | 1.41 |
| 11-08 17:20 | +5 | BTC | UP | 0.63 | 0.80 | 1.41 |
| 11-08 17:20 | +10 stop | ZEC | DOWN | 0.62 | 0.74 | 0.89 |
| 11-08 17:20 | +10 stop | XRP | UP | 0.68 | 0.52 | -1.94 |
| 11-08 17:20 | +10 stop | HYPE | UP | 0.48 | 0.33 | -1.84 |
| 11-08 17:18 | +10 stop | BNB | UP | 0.68 | 0.79 | 0.82 |
| 11-08 17:18 | +10 stop | HYPE | DOWN | 0.64 | 0.46 | -2.15 |
| 11-08 17:18 | +10 | HYPE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-08 17:18 | +5 | HYPE | DOWN | 0.65 | 0.70 | 0.19 |
| 11-08 17:17 | +10 stop | SOL | UP | 0.56 | 0.67 | 0.76 |
| 11-08 17:17 | +10 stop | BNB | UP | 0.56 | 0.68 | 0.86 |
| 11-08 17:17 | +10 stop | XRP | UP | 0.62 | 0.75 | 0.95 |
| 11-08 17:17 | +10 stop | DOGE | UP | 0.55 | 0.85 | 2.73 |
| 11-08 17:17 | +10 stop | ETH | UP | 0.57 | 0.73 | 1.28 |
| 11-08 17:17 | +10 stop | BTC | UP | 0.62 | 0.73 | 0.79 |
| 11-08 17:17 | +10 | BTC | UP | 0.62 | 0.73 | 0.79 |
| 11-08 17:17 | +5 | BTC | UP | 0.62 | 0.73 | 0.79 |
