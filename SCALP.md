# Range-Scalp Bot

*Updated Tue Nov 10 13:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54549 | 47582 | 6967 (91) | 0 | $-14853.95 | -4.3% |
| **+10¢** | 40754 | 32622 | 8132 (121) | 0 | $-13803.19 | -5.4% |
| **+15¢** | 34163 | 25395 | 8768 (155) | 0 | $-12571.13 | -5.9% |
| **+20¢** | 30423 | 21226 | 9197 (204) | 0 | $-10966.91 | -5.7% |
| **+10¢ (15¢ stop)** | 66470 | 66356 | 114 (70) | 0 | $-24580.77 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 13:39 | +10 stop | HYPE | DOWN | 0.69 | 0.53 | -1.93 |
| 11-10 13:38 | +10 stop | NEAR | DOWN | 0.69 | 0.81 | 0.94 |
| 11-10 13:38 | +10 stop | SOL | DOWN | 0.71 | 0.83 | 0.95 |
| 11-10 13:38 | +20 | SOL | DOWN | 0.71 | 0.92 | 1.88 |
| 11-10 13:38 | +15 | SOL | DOWN | 0.71 | 0.86 | 1.26 |
| 11-10 13:38 | +10 | SOL | DOWN | 0.71 | 0.83 | 0.95 |
| 11-10 13:38 | +5 | SOL | DOWN | 0.71 | 0.78 | 0.42 |
| 11-10 13:37 | +10 stop | HYPE | UP | 0.61 | 0.43 | -2.15 |
| 11-10 13:36 | +10 stop | ZEC | DOWN | 0.54 | 0.68 | 1.06 |
| 11-10 13:36 | +20 | ZEC | DOWN | 0.54 | 0.77 | 1.99 |
| 11-10 13:36 | +15 | ZEC | DOWN | 0.54 | 0.77 | 1.99 |
| 11-10 13:36 | +10 | ZEC | DOWN | 0.56 | 0.68 | 0.86 |
| 11-10 13:36 | +5 | ZEC | DOWN | 0.56 | 0.68 | 0.86 |
| 11-10 13:36 | +10 stop | NEAR | DOWN | 0.65 | 0.49 | -1.94 |
| 11-10 13:36 | +20 | NEAR | DOWN | 0.65 | 0.89 | 2.17 |
| 11-10 13:36 | +15 | NEAR | DOWN | 0.64 | 0.81 | 1.42 |
| 11-10 13:36 | +10 | NEAR | DOWN | 0.64 | 0.81 | 1.42 |
| 11-10 13:36 | +5 | NEAR | DOWN | 0.64 | 0.69 | 0.23 |
| 11-10 13:35 | +10 stop | HYPE | DOWN | 0.63 | 0.46 | -2.05 |
| 11-10 13:34 | +10 stop | HYPE | DOWN | 0.68 | 0.53 | -1.84 |
| 11-10 13:34 | +20 | HYPE | DOWN | 0.68 | 0.89 | 1.87 |
| 11-10 13:34 | +15 | HYPE | DOWN | 0.67 | 0.84 | 1.44 |
| 11-10 13:34 | +10 | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-10 13:34 | +5 | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-10 13:24 | +5 | ETH | DOWN | 0.63 | 0.87 | 2.15 |
| 11-10 13:24 | +10 stop | HYPE | DOWN | 0.55 | 0.88 | 3.04 |
| 11-10 13:24 | +5 | ETH | DOWN | 0.57 | 0.65 | 0.46 |
| 11-10 13:24 | +10 stop | NEAR | DOWN | 0.70 | 0.86 | 1.36 |
| 11-10 13:23 | +10 stop | BNB | DOWN | 0.69 | 0.96 | 2.53 |
| 11-10 13:23 | +5 | ZEC | DOWN | 0.68 | 0.79 | 0.77 |
| 11-10 13:22 | +5 | NEAR | DOWN | 0.65 | 0.71 | 0.29 |
| 11-10 13:22 | +10 stop | ETH | DOWN | 0.64 | 0.87 | 2.05 |
| 11-10 13:22 | +20 | ETH | DOWN | 0.64 | 0.87 | 2.05 |
| 11-10 13:22 | +15 | ETH | DOWN | 0.64 | 0.87 | 2.09 |
| 11-10 13:22 | +10 | ETH | DOWN | 0.64 | 0.87 | 2.07 |
| 11-10 13:22 | +5 | ETH | DOWN | 0.64 | 0.71 | 0.40 |
| 11-10 13:21 | +10 stop | HYPE | UP | 0.60 | 0.44 | -1.95 |
| 11-10 13:21 | +10 stop | BNB | DOWN | 0.58 | 0.68 | 0.66 |
| 11-10 13:21 | +10 stop | NEAR | DOWN | 0.53 | 0.67 | 1.06 |
| 11-10 13:21 | +20 | NEAR | DOWN | 0.53 | 0.74 | 1.78 |
