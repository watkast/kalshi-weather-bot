# Range-Scalp Bot

*Updated Mon Nov 23 04:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69596 | 60728 | 8868 (146) | 2 | $-18724.09 | -4.3% |
| **+10¢** | 51935 | 41575 | 10360 (189) | 2 | $-17415.56 | -5.3% |
| **+15¢** | 43520 | 32358 | 11162 (244) | 2 | $-15570.79 | -5.7% |
| **+20¢** | 38756 | 27017 | 11739 (308) | 3 | $-13892.93 | -5.7% |
| **+10¢ (15¢ stop)** | 84748 | 84558 | 190 (118) | 0 | $-31155.73 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 04:26 | +10 stop | DOGE | UP | 0.54 | 0.30 | -2.73 |
| 11-23 04:26 | +10 stop | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-23 04:26 | +10 stop | NEAR | UP | 0.46 | 0.59 | 0.95 |
| 11-23 04:23 | +10 stop | ZEC | UP | 0.67 | 0.31 | -3.89 |
| 11-23 04:22 | +10 stop | ETH | UP | 0.65 | 0.43 | -2.54 |
| 11-23 04:21 | +10 stop | ZEC | UP | 0.70 | 0.83 | 1.06 |
| 11-23 04:20 | +10 stop | BNB | UP | 0.64 | 0.77 | 1.00 |
| 11-23 04:20 | +10 stop | SOL | UP | 0.64 | 0.76 | 0.90 |
| 11-23 04:20 | +10 stop | DOGE | UP | 0.66 | 0.84 | 1.54 |
| 11-23 04:20 | +10 stop | BTC | UP | 0.60 | 0.74 | 1.09 |
| 11-23 04:20 | +10 stop | NEAR | DOWN | 0.61 | 0.41 | -2.34 |
| 11-23 04:20 | +10 | NEAR | DOWN | 0.61 | 0.80 | 1.61 |
| 11-23 04:20 | +5 | NEAR | DOWN | 0.61 | 0.67 | 0.27 |
| 11-23 04:20 | +10 stop | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 11-23 04:18 | +10 stop | ZEC | UP | 0.52 | 0.63 | 0.75 |
| 11-23 04:18 | +10 stop | BTC | DOWN | 0.68 | 0.52 | -1.94 |
| 11-23 04:18 | +20 | BTC | DOWN | 0.68 | 0.94 | 2.44 |
| 11-23 04:18 | +15 | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-23 04:18 | +10 | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-23 04:18 | +5 | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-23 04:18 | +10 stop | XRP | UP | 0.64 | 0.74 | 0.69 |
| 11-23 04:18 | +10 stop | SOL | DOWN | 0.70 | 0.50 | -2.33 |
| 11-23 04:18 | +20 | SOL | DOWN | 0.70 | open |  |
| 11-23 04:18 | +15 | SOL | DOWN | 0.70 | 0.86 | 1.36 |
| 11-23 04:18 | +10 | SOL | DOWN | 0.70 | 0.86 | 1.36 |
| 11-23 04:18 | +5 | SOL | DOWN | 0.70 | 0.86 | 1.36 |
| 11-23 04:18 | +10 stop | DOGE | DOWN | 0.70 | 0.47 | -2.63 |
| 11-23 04:18 | +20 | DOGE | DOWN | 0.70 | 0.97 | 2.50 |
| 11-23 04:18 | +15 | DOGE | DOWN | 0.70 | 0.97 | 2.50 |
| 11-23 04:18 | +10 | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-23 04:18 | +5 | DOGE | DOWN | 0.70 | 0.78 | 0.52 |
| 11-23 04:18 | +10 stop | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 11-23 04:18 | +15 | NEAR | DOWN | 0.65 | 0.80 | 1.22 |
| 11-23 04:18 | +10 | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 11-23 04:18 | +10 stop | ETH | DOWN | 0.68 | 0.49 | -2.24 |
| 11-23 04:18 | +20 | ETH | DOWN | 0.68 | 0.93 | 2.25 |
| 11-23 04:18 | +15 | ETH | DOWN | 0.68 | 0.87 | 1.66 |
| 11-23 04:18 | +10 | ETH | DOWN | 0.68 | 0.87 | 1.66 |
| 11-23 04:18 | +5 | ETH | DOWN | 0.68 | 0.76 | 0.51 |
| 11-23 04:17 | +10 stop | BNB | DOWN | 0.62 | 0.43 | -2.25 |
