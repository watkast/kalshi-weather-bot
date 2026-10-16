# Range-Scalp Bot

*Updated Fri Oct 16 04:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18689 | 16227 | 2462 (28) | 2 | $-5726.72 | -4.9% |
| **+10¢** | 14085 | 11240 | 2845 (40) | 2 | $-5167.98 | -5.8% |
| **+15¢** | 11815 | 8752 | 3063 (59) | 1 | $-4683.14 | -6.3% |
| **+20¢** | 10495 | 7289 | 3206 (78) | 1 | $-4109.72 | -6.2% |
| **+10¢ (15¢ stop)** | 23032 | 22982 | 50 (29) | 0 | $-8922.50 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 04:55 | +10 stop | HYPE | DOWN | 0.50 | 0.66 | 1.22 |
| 10-16 04:53 | +10 stop | XRP | DOWN | 0.57 | 0.40 | -2.05 |
| 10-16 04:53 | +10 stop | DOGE | UP | 0.63 | 0.76 | 1.00 |
| 10-16 04:53 | +5 | DOGE | UP | 0.63 | 0.76 | 1.00 |
| 10-16 04:53 | +5 | ETH | UP | 0.71 | 0.76 | 0.22 |
| 10-16 04:52 | +10 stop | BTC | UP | 0.67 | 0.83 | 1.34 |
| 10-16 04:52 | +5 | BTC | UP | 0.67 | 0.73 | 0.30 |
| 10-16 04:52 | +10 stop | BNB | UP | 0.53 | 0.70 | 1.38 |
| 10-16 04:52 | +10 stop | ETH | UP | 0.59 | 0.72 | 0.98 |
| 10-16 04:52 | +5 | ETH | UP | 0.59 | 0.64 | 0.16 |
| 10-16 04:52 | +10 stop | SOL | UP | 0.63 | 0.83 | 1.73 |
| 10-16 04:52 | +5 | SOL | UP | 0.63 | 0.72 | 0.58 |
| 10-16 04:52 | +10 stop | DOGE | UP | 0.54 | 0.66 | 0.86 |
| 10-16 04:52 | +10 stop | HYPE | DOWN | 0.63 | 0.81 | 1.52 |
| 10-16 04:52 | +10 stop | XRP | DOWN | 0.67 | 0.51 | -1.94 |
| 10-16 04:52 | +10 | XRP | DOWN | 0.67 | open |  |
| 10-16 04:52 | +5 | XRP | DOWN | 0.67 | open |  |
| 10-16 04:52 | +10 stop | NEAR | UP | 0.67 | 0.79 | 0.92 |
| 10-16 04:51 | +10 stop | DOGE | DOWN | 0.47 | 0.66 | 1.56 |
| 10-16 04:51 | +10 stop | ETH | DOWN | 0.59 | 0.28 | -3.42 |
| 10-16 04:51 | +10 stop | SOL | DOWN | 0.61 | 0.34 | -3.03 |
| 10-16 04:51 | +5 | NEAR | DOWN | 0.63 | open |  |
| 10-16 04:50 | +10 stop | BTC | DOWN | 0.61 | 0.46 | -1.85 |
| 10-16 04:50 | +10 stop | BNB | DOWN | 0.55 | 0.37 | -2.15 |
| 10-16 04:50 | +10 stop | SOL | DOWN | 0.50 | 0.63 | 0.95 |
| 10-16 04:50 | +10 stop | DOGE | DOWN | 0.52 | 0.69 | 1.37 |
| 10-16 04:49 | +10 stop | HYPE | DOWN | 0.63 | 0.74 | 0.75 |
| 10-16 04:49 | +10 stop | XRP | DOWN | 0.67 | 0.80 | 1.02 |
| 10-16 04:49 | +10 | XRP | DOWN | 0.67 | 0.80 | 1.02 |
| 10-16 04:49 | +5 | XRP | DOWN | 0.67 | 0.74 | 0.40 |
| 10-16 04:49 | +10 stop | ZEC | UP | 0.62 | 0.44 | -2.17 |
| 10-16 04:49 | +10 | ZEC | UP | 0.62 | 0.74 | 0.89 |
| 10-16 04:49 | +5 | ZEC | UP | 0.62 | 0.74 | 0.89 |
| 10-16 04:48 | +5 | HYPE | UP | 0.63 | 0.75 | 0.89 |
| 10-16 04:48 | +5 | ETH | UP | 0.60 | 0.71 | 0.78 |
| 10-16 04:48 | +10 | ETH | UP | 0.62 | 0.72 | 0.68 |
| 10-16 04:48 | +5 | SOL | UP | 0.57 | 0.65 | 0.46 |
| 10-16 04:48 | +5 | DOGE | UP | 0.61 | 0.66 | 0.17 |
| 10-16 04:48 | +10 stop | ETH | UP | 0.63 | 0.40 | -2.64 |
| 10-16 04:48 | +5 | ETH | UP | 0.63 | 0.69 | 0.28 |
