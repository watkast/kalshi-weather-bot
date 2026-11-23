# Range-Scalp Bot

*Updated Mon Nov 23 10:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69789 | 60898 | 8891 (146) | 5 | $-18778.87 | -4.3% |
| **+10¢** | 52074 | 41689 | 10385 (189) | 7 | $-17446.94 | -5.3% |
| **+15¢** | 43641 | 32454 | 11187 (244) | 7 | $-15582.29 | -5.7% |
| **+20¢** | 38860 | 27090 | 11770 (309) | 7 | $-13927.25 | -5.7% |
| **+10¢ (15¢ stop)** | 84997 | 84807 | 190 (118) | 1 | $-31215.90 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 10:09 | +10 stop | DOGE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-23 10:09 | +5 | DOGE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-23 10:09 | +10 stop | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 11-23 10:07 | +10 stop | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 11-23 10:07 | +5 | DOGE | DOWN | 0.70 | 0.75 | 0.21 |
| 11-23 10:07 | +10 stop | ZEC | DOWN | 0.67 | 0.78 | 0.81 |
| 11-23 10:07 | +10 stop | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 11-23 10:06 | +10 stop | SOL | UP | 0.70 | 0.46 | -2.73 |
| 11-23 10:06 | +10 stop | XRP | UP | 0.67 | 0.77 | 0.71 |
| 11-23 10:06 | +20 | XRP | UP | 0.67 | 0.89 | 1.97 |
| 11-23 10:06 | +5 | XRP | UP | 0.69 | 0.76 | 0.42 |
| 11-23 10:06 | +10 stop | BTC | DOWN | 0.48 | 0.61 | 0.95 |
| 11-23 10:06 | +10 stop | NEAR | UP | 0.67 | 0.82 | 1.23 |
| 11-23 10:06 | +5 | NEAR | UP | 0.67 | 0.75 | 0.50 |
| 11-23 10:05 | +10 stop | HYPE | DOWN | 0.63 | 0.78 | 1.20 |
| 11-23 10:05 | +5 | HYPE | DOWN | 0.63 | 0.72 | 0.58 |
| 11-23 10:05 | +15 | XRP | UP | 0.69 | 0.86 | 1.46 |
| 11-23 10:05 | +10 | XRP | UP | 0.69 | 0.82 | 1.04 |
| 11-23 10:05 | +10 stop | ETH | UP | 0.64 | open |  |
| 11-23 10:05 | +10 stop | XRP | UP | 0.62 | 0.73 | 0.79 |
| 11-23 10:04 | +5 | XRP | UP | 0.63 | 0.69 | 0.28 |
| 11-23 10:04 | +10 stop | SOL | UP | 0.61 | 0.72 | 0.78 |
| 11-23 10:04 | +10 stop | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-23 10:04 | +5 | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-23 10:04 | +10 stop | NEAR | UP | 0.67 | 0.77 | 0.71 |
| 11-23 10:04 | +10 stop | BNB | DOWN | 0.65 | 0.78 | 1.01 |
| 11-23 10:04 | +10 stop | BTC | DOWN | 0.57 | 0.40 | -2.05 |
| 11-23 10:04 | +5 | HYPE | DOWN | 0.58 | 0.72 | 1.07 |
| 11-23 10:03 | +10 stop | BTC | DOWN | 0.58 | 0.68 | 0.66 |
| 11-23 10:03 | +10 stop | ETH | DOWN | 0.61 | 0.40 | -2.44 |
| 11-23 10:03 | +5 | ETH | DOWN | 0.59 | open |  |
| 11-23 10:02 | +10 stop | DOGE | DOWN | 0.59 | 0.72 | 0.98 |
| 11-23 10:02 | +10 stop | HYPE | DOWN | 0.56 | 0.72 | 1.28 |
| 11-23 10:02 | +10 stop | SOL | UP | 0.53 | 0.36 | -2.05 |
| 11-23 10:02 | +5 | DOGE | DOWN | 0.59 | 0.72 | 0.98 |
| 11-23 10:02 | +5 | HYPE | DOWN | 0.56 | 0.62 | 0.26 |
| 11-23 10:02 | +10 stop | BNB | DOWN | 0.58 | 0.68 | 0.66 |
| 11-23 10:02 | +10 stop | XRP | UP | 0.46 | 0.56 | 0.64 |
| 11-23 10:02 | +20 | XRP | UP | 0.46 | 0.69 | 1.97 |
| 11-23 10:02 | +15 | XRP | UP | 0.46 | 0.63 | 1.35 |
