# Range-Scalp Bot

*Updated Thu Oct 22 06:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28438 | 24785 | 3653 (39) | 1 | $-8149.47 | -4.5% |
| **+10¢** | 21332 | 17105 | 4227 (55) | 3 | $-7253.14 | -5.4% |
| **+15¢** | 17863 | 13316 | 4547 (78) | 4 | $-6479.79 | -5.8% |
| **+20¢** | 15803 | 11033 | 4770 (98) | 4 | $-5868.77 | -5.9% |
| **+10¢ (15¢ stop)** | 34867 | 34808 | 59 (32) | 0 | $-13075.53 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 06:23 | +10 stop | NEAR | DOWN | 0.56 | 0.67 | 0.76 |
| 10-22 06:23 | +10 stop | ZEC | DOWN | 0.63 | 0.79 | 1.31 |
| 10-22 06:23 | +15 | ZEC | DOWN | 0.63 | 0.79 | 1.31 |
| 10-22 06:23 | +10 | ZEC | DOWN | 0.63 | 0.79 | 1.31 |
| 10-22 06:23 | +5 | ZEC | DOWN | 0.63 | 0.79 | 1.31 |
| 10-22 06:22 | +10 stop | SOL | DOWN | 0.65 | 0.87 | 1.96 |
| 10-22 06:22 | +20 | SOL | DOWN | 0.65 | 0.87 | 1.96 |
| 10-22 06:22 | +10 | SOL | DOWN | 0.65 | 0.87 | 1.96 |
| 10-22 06:22 | +5 | SOL | DOWN | 0.65 | 0.71 | 0.29 |
| 10-22 06:22 | +10 stop | HYPE | DOWN | 0.65 | 0.78 | 1.01 |
| 10-22 06:22 | +20 | HYPE | DOWN | 0.65 | 0.87 | 1.96 |
| 10-22 06:22 | +15 | HYPE | DOWN | 0.65 | 0.84 | 1.64 |
| 10-22 06:22 | +10 | HYPE | DOWN | 0.65 | 0.78 | 1.01 |
| 10-22 06:22 | +5 | HYPE | DOWN | 0.65 | 0.72 | 0.39 |
| 10-22 06:21 | +10 stop | NEAR | DOWN | 0.69 | 0.52 | -2.03 |
| 10-22 06:20 | +5 | BNB | DOWN | 0.71 | 0.84 | 1.05 |
| 10-22 06:19 | +15 | SOL | DOWN | 0.70 | 0.87 | 1.48 |
| 10-22 06:19 | +10 | SOL | DOWN | 0.70 | 0.83 | 1.06 |
| 10-22 06:19 | +5 | SOL | DOWN | 0.70 | 0.79 | 0.64 |
| 10-22 06:19 | +5 | HYPE | DOWN | 0.67 | 0.75 | 0.50 |
| 10-22 06:19 | +10 stop | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 10-22 06:19 | +5 | BTC | DOWN | 0.71 | 0.77 | 0.32 |
| 10-22 06:19 | +5 | DOGE | DOWN | 0.66 | 0.79 | 1.02 |
| 10-22 06:19 | +10 stop | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 10-22 06:19 | +10 stop | NEAR | UP | 0.63 | 0.47 | -1.95 |
| 10-22 06:19 | +10 | NEAR | UP | 0.63 | open |  |
| 10-22 06:18 | +5 | NEAR | UP | 0.66 | open |  |
| 10-22 06:18 | +10 stop | SOL | DOWN | 0.58 | 0.73 | 1.18 |
| 10-22 06:18 | +10 | SOL | DOWN | 0.57 | 0.67 | 0.66 |
| 10-22 06:18 | +5 | BNB | DOWN | 0.61 | 0.67 | 0.27 |
| 10-22 06:18 | +5 | SOL | DOWN | 0.59 | 0.67 | 0.47 |
| 10-22 06:18 | +5 | ETH | DOWN | 0.63 | 0.69 | 0.28 |
| 10-22 06:18 | +10 stop | HYPE | DOWN | 0.58 | 0.70 | 0.87 |
| 10-22 06:18 | +20 | HYPE | DOWN | 0.58 | 0.79 | 1.80 |
| 10-22 06:18 | +15 | HYPE | DOWN | 0.58 | 0.75 | 1.38 |
| 10-22 06:18 | +10 | HYPE | DOWN | 0.58 | 0.70 | 0.87 |
| 10-22 06:18 | +5 | HYPE | DOWN | 0.57 | 0.66 | 0.52 |
| 10-22 06:18 | +10 stop | DOGE | DOWN | 0.57 | 0.67 | 0.66 |
| 10-22 06:18 | +10 | DOGE | DOWN | 0.57 | 0.67 | 0.66 |
| 10-22 06:18 | +5 | DOGE | DOWN | 0.57 | 0.62 | 0.15 |
