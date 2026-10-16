# Range-Scalp Bot

*Updated Fri Oct 16 17:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19551 | 16987 | 2564 (29) | 0 | $-5908.84 | -4.8% |
| **+10¢** | 14741 | 11779 | 2962 (41) | 0 | $-5316.63 | -5.7% |
| **+15¢** | 12337 | 9152 | 3185 (60) | 0 | $-4800.60 | -6.2% |
| **+20¢** | 10948 | 7611 | 3337 (79) | 0 | $-4256.57 | -6.2% |
| **+10¢ (15¢ stop)** | 24043 | 23993 | 50 (29) | 0 | $-9203.85 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 17:17 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-16 17:17 | +20 | SOL | DOWN | 0.70 | 0.91 | 1.85 |
| 10-16 17:17 | +15 | SOL | DOWN | 0.70 | 0.88 | 1.57 |
| 10-16 17:17 | +10 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-16 17:11 | +10 stop | HYPE | DOWN | 0.65 | 0.82 | 1.39 |
| 10-16 17:11 | +15 | HYPE | DOWN | 0.65 | 0.82 | 1.43 |
| 10-16 17:11 | +10 | HYPE | DOWN | 0.65 | 0.82 | 1.43 |
| 10-16 17:11 | +5 | HYPE | DOWN | 0.65 | 0.82 | 1.43 |
| 10-16 17:10 | +10 stop | ZEC | DOWN | 0.60 | 0.71 | 0.78 |
| 10-16 17:10 | +20 | ZEC | DOWN | 0.59 | 0.79 | 1.71 |
| 10-16 17:10 | +15 | ZEC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-16 17:10 | +10 | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-16 17:10 | +5 | ZEC | DOWN | 0.61 | 0.66 | 0.17 |
| 10-16 17:04 | +10 stop | ZEC | DOWN | 0.60 | 0.81 | 1.82 |
| 10-16 17:04 | +10 stop | DOGE | DOWN | 0.63 | 0.76 | 1.00 |
| 10-16 17:04 | +10 stop | NEAR | DOWN | 0.67 | 0.84 | 1.44 |
| 10-16 17:03 | +5 | BNB | DOWN | 0.68 | 0.78 | 0.71 |
| 10-16 17:03 | +10 stop | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-16 17:03 | +10 | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-16 17:03 | +5 | BTC | DOWN | 0.71 | 0.77 | 0.32 |
| 10-16 17:03 | +5 | BNB | DOWN | 0.58 | 0.67 | 0.56 |
| 10-16 17:02 | +10 stop | DOGE | DOWN | 0.64 | 0.48 | -1.95 |
| 10-16 17:02 | +10 | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-16 17:02 | +5 | NEAR | DOWN | 0.58 | 0.66 | 0.46 |
| 10-16 17:02 | +5 | XRP | DOWN | 0.66 | 0.79 | 1.02 |
| 10-16 17:02 | +5 | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-16 17:02 | +10 stop | ETH | DOWN | 0.70 | 0.81 | 0.84 |
| 10-16 17:02 | +20 | ETH | DOWN | 0.70 | 0.93 | 2.12 |
| 10-16 17:02 | +15 | ETH | DOWN | 0.70 | 0.89 | 1.68 |
| 10-16 17:02 | +10 | ETH | DOWN | 0.70 | 0.81 | 0.84 |
| 10-16 17:02 | +5 | SOL | DOWN | 0.66 | 0.72 | 0.27 |
| 10-16 17:02 | +5 | ETH | DOWN | 0.71 | 0.77 | 0.32 |
| 10-16 17:02 | +10 stop | ZEC | DOWN | 0.66 | 0.42 | -2.76 |
| 10-16 17:02 | +20 | ZEC | DOWN | 0.66 | 0.87 | 1.84 |
| 10-16 17:02 | +15 | ZEC | DOWN | 0.66 | 0.83 | 1.42 |
| 10-16 17:02 | +10 | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-16 17:02 | +5 | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-16 17:01 | +10 stop | XRP | DOWN | 0.56 | 0.69 | 0.97 |
| 10-16 17:01 | +20 | XRP | DOWN | 0.56 | 0.79 | 2.00 |
| 10-16 17:01 | +15 | XRP | DOWN | 0.56 | 0.79 | 2.00 |
