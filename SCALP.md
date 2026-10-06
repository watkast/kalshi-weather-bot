# Range-Scalp Bot

*Updated Tue Oct 06 01:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4455 | 3842 | 613 (6) | 0 | $-1493.64 | -5.3% |
| **+10¢** | 3431 | 2719 | 712 (9) | 0 | $-1385.18 | -6.4% |
| **+15¢** | 2880 | 2127 | 753 (12) | 0 | $-1208.62 | -6.7% |
| **+20¢** | 2580 | 1796 | 784 (17) | 0 | $-1012.38 | -6.2% |
| **+10¢ (15¢ stop)** | 5477 | 5466 | 11 (6) | 0 | $-1972.61 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 01:23 | +5 | NEAR | DOWN | 0.65 | 0.80 | 1.22 |
| 10-06 01:22 | +10 stop | NEAR | DOWN | 0.67 | 0.80 | 1.02 |
| 10-06 01:20 | +10 stop | NEAR | DOWN | 0.62 | 0.47 | -1.85 |
| 10-06 01:20 | +15 | NEAR | DOWN | 0.62 | 0.80 | 1.51 |
| 10-06 01:20 | +10 | NEAR | DOWN | 0.62 | 0.80 | 1.51 |
| 10-06 01:20 | +5 | NEAR | DOWN | 0.62 | 0.70 | 0.48 |
| 10-06 01:16 | +5 | BNB | DOWN | 0.63 | 0.81 | 1.52 |
| 10-06 01:16 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-06 01:16 | +20 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-06 01:16 | +15 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-06 01:16 | +10 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-06 01:16 | +5 | BTC | DOWN | 0.69 | 0.75 | 0.31 |
| 10-06 01:16 | +10 stop | ETH | DOWN | 0.63 | 0.78 | 1.20 |
| 10-06 01:16 | +20 | ETH | DOWN | 0.63 | 0.83 | 1.73 |
| 10-06 01:16 | +15 | ETH | DOWN | 0.63 | 0.78 | 1.20 |
| 10-06 01:16 | +10 | ETH | DOWN | 0.63 | 0.78 | 1.20 |
| 10-06 01:16 | +5 | ETH | DOWN | 0.63 | 0.68 | 0.17 |
| 10-06 01:15 | +10 stop | DOGE | DOWN | 0.56 | 0.70 | 1.08 |
| 10-06 01:15 | +20 | DOGE | DOWN | 0.55 | 0.81 | 2.31 |
| 10-06 01:15 | +15 | DOGE | DOWN | 0.55 | 0.70 | 1.17 |
| 10-06 01:15 | +10 | DOGE | DOWN | 0.55 | 0.70 | 1.17 |
| 10-06 01:15 | +5 | DOGE | DOWN | 0.55 | 0.64 | 0.55 |
| 10-06 01:15 | +10 stop | NEAR | DOWN | 0.59 | 0.71 | 0.85 |
| 10-06 01:15 | +20 | NEAR | DOWN | 0.59 | 0.80 | 1.78 |
| 10-06 01:15 | +15 | NEAR | DOWN | 0.59 | 0.79 | 1.68 |
| 10-06 01:15 | +10 | NEAR | DOWN | 0.59 | 0.71 | 0.85 |
| 10-06 01:15 | +5 | NEAR | DOWN | 0.59 | 0.69 | 0.65 |
| 10-06 01:15 | +10 stop | ZEC | DOWN | 0.58 | 0.70 | 0.87 |
| 10-06 01:15 | +20 | ZEC | DOWN | 0.58 | 0.83 | 2.22 |
| 10-06 01:15 | +15 | ZEC | DOWN | 0.58 | 0.75 | 1.38 |
| 10-06 01:15 | +10 | ZEC | DOWN | 0.58 | 0.70 | 0.87 |
| 10-06 01:15 | +5 | ZEC | DOWN | 0.58 | 0.70 | 0.87 |
| 10-06 01:15 | +10 stop | SOL | DOWN | 0.54 | 0.64 | 0.65 |
| 10-06 01:15 | +20 | SOL | DOWN | 0.54 | 0.74 | 1.68 |
| 10-06 01:15 | +15 | SOL | DOWN | 0.54 | 0.73 | 1.58 |
| 10-06 01:15 | +10 | SOL | DOWN | 0.54 | 0.64 | 0.65 |
| 10-06 01:15 | +5 | SOL | DOWN | 0.54 | 0.64 | 0.65 |
| 10-06 01:15 | +10 stop | BNB | DOWN | 0.54 | 0.67 | 0.96 |
| 10-06 01:15 | +20 | BNB | DOWN | 0.54 | 0.81 | 2.41 |
| 10-06 01:15 | +15 | BNB | DOWN | 0.54 | 0.81 | 2.41 |
