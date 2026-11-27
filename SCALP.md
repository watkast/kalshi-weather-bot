# Range-Scalp Bot

*Updated Fri Nov 27 18:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73897 | 64491 | 9406 (171) | 0 | $-19661.73 | -4.2% |
| **+10¢** | 55059 | 44073 | 10986 (216) | 0 | $-18297.18 | -5.3% |
| **+15¢** | 46109 | 34279 | 11830 (274) | 0 | $-16353.87 | -5.7% |
| **+20¢** | 41033 | 28572 | 12461 (341) | 0 | $-14780.71 | -5.7% |
| **+10¢ (15¢ stop)** | 89987 | 89768 | 219 (135) | 0 | $-33319.11 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 18:25 | +5 | BNB | DOWN | 0.57 | 0.62 | 0.15 |
| 11-27 18:24 | +10 stop | BNB | DOWN | 0.56 | 0.73 | 1.38 |
| 11-27 18:24 | +15 | BNB | DOWN | 0.56 | 0.73 | 1.38 |
| 11-27 18:24 | +10 | BNB | DOWN | 0.56 | 0.73 | 1.38 |
| 11-27 18:24 | +5 | BNB | DOWN | 0.56 | 0.61 | 0.15 |
| 11-27 18:21 | +10 stop | XRP | DOWN | 0.70 | 0.83 | 1.05 |
| 11-27 18:21 | +5 | ETH | DOWN | 0.69 | 0.76 | 0.44 |
| 11-27 18:20 | +20 | DOGE | DOWN | 0.68 | 0.90 | 1.97 |
| 11-27 18:20 | +5 | DOGE | DOWN | 0.68 | 0.74 | 0.30 |
| 11-27 18:20 | +10 stop | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 11-27 18:20 | +5 | NEAR | DOWN | 0.68 | 0.74 | 0.26 |
| 11-27 18:19 | +15 | DOGE | DOWN | 0.68 | 0.84 | 1.38 |
| 11-27 18:19 | +10 stop | BNB | DOWN | 0.56 | 0.75 | 1.58 |
| 11-27 18:19 | +5 | SOL | DOWN | 0.70 | 0.75 | 0.21 |
| 11-27 18:19 | +10 stop | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-27 18:19 | +10 | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-27 18:19 | +5 | DOGE | DOWN | 0.62 | 0.67 | 0.17 |
| 11-27 18:19 | +5 | HYPE | DOWN | 0.59 | 0.64 | 0.16 |
| 11-27 18:19 | +10 stop | ETH | DOWN | 0.62 | 0.76 | 1.10 |
| 11-27 18:19 | +20 | ETH | DOWN | 0.62 | 0.83 | 1.83 |
| 11-27 18:19 | +15 | ETH | DOWN | 0.62 | 0.79 | 1.41 |
| 11-27 18:19 | +10 | ETH | DOWN | 0.62 | 0.76 | 1.10 |
| 11-27 18:19 | +5 | ETH | DOWN | 0.62 | 0.68 | 0.27 |
| 11-27 18:19 | +10 stop | NEAR | DOWN | 0.67 | 0.81 | 1.13 |
| 11-27 18:19 | +5 | XRP | UP | 0.62 | no | -6.37 |
| 11-27 18:19 | +10 stop | XRP | UP | 0.61 | 0.39 | -2.54 |
| 11-27 18:19 | +10 | XRP | UP | 0.61 | no | -6.27 |
| 11-27 18:19 | +5 | XRP | UP | 0.61 | 0.66 | 0.17 |
| 11-27 18:19 | +5 | ZEC | DOWN | 0.61 | 0.74 | 0.99 |
| 11-27 18:18 | +5 | HYPE | DOWN | 0.54 | 0.59 | 0.15 |
| 11-27 18:18 | +10 stop | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 11-27 18:18 | +10 | HYPE | DOWN | 0.60 | 0.74 | 1.09 |
| 11-27 18:18 | +5 | HYPE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-27 18:18 | +5 | SOL | DOWN | 0.59 | 0.68 | 0.57 |
| 11-27 18:18 | +5 | ZEC | DOWN | 0.52 | 0.59 | 0.35 |
| 11-27 18:18 | +10 stop | DOGE | DOWN | 0.46 | 0.56 | 0.64 |
| 11-27 18:18 | +20 | DOGE | DOWN | 0.46 | 0.67 | 1.76 |
| 11-27 18:18 | +15 | DOGE | DOWN | 0.46 | 0.61 | 1.15 |
| 11-27 18:18 | +10 | DOGE | DOWN | 0.46 | 0.56 | 0.64 |
| 11-27 18:18 | +5 | DOGE | DOWN | 0.48 | 0.54 | 0.24 |
