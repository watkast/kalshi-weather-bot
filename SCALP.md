# Range-Scalp Bot

*Updated Fri Oct 16 15:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19423 | 16878 | 2545 (29) | 0 | $-5850.30 | -4.8% |
| **+10¢** | 14643 | 11703 | 2940 (41) | 0 | $-5254.85 | -5.7% |
| **+15¢** | 12255 | 9090 | 3165 (60) | 0 | $-4773.94 | -6.2% |
| **+20¢** | 10871 | 7554 | 3317 (79) | 0 | $-4249.81 | -6.2% |
| **+10¢ (15¢ stop)** | 23876 | 23826 | 50 (29) | 0 | $-9162.63 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 15:01 | +10 stop | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 10-16 15:01 | +20 | ZEC | DOWN | 0.70 | 0.94 | 2.15 |
| 10-16 15:01 | +15 | ZEC | DOWN | 0.67 | 0.82 | 1.23 |
| 10-16 15:01 | +10 | ZEC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-16 15:01 | +5 | ZEC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-16 15:01 | +10 stop | BNB | DOWN | 0.67 | 0.80 | 1.02 |
| 10-16 15:01 | +20 | BNB | DOWN | 0.67 | 0.87 | 1.76 |
| 10-16 15:01 | +15 | BNB | DOWN | 0.67 | 0.84 | 1.44 |
| 10-16 15:01 | +10 | BNB | DOWN | 0.67 | 0.80 | 1.02 |
| 10-16 15:01 | +5 | BNB | DOWN | 0.67 | 0.80 | 1.02 |
| 10-16 15:01 | +10 stop | SOL | DOWN | 0.68 | 0.79 | 0.82 |
| 10-16 15:01 | +20 | SOL | DOWN | 0.68 | 0.92 | 2.16 |
| 10-16 15:01 | +15 | SOL | DOWN | 0.67 | 0.92 | 2.26 |
| 10-16 15:01 | +10 | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 10-16 15:01 | +5 | SOL | DOWN | 0.67 | 0.73 | 0.30 |
| 10-16 15:01 | +10 stop | BTC | DOWN | 0.60 | 0.74 | 1.09 |
| 10-16 15:01 | +20 | BTC | DOWN | 0.58 | 0.78 | 1.69 |
| 10-16 15:01 | +15 | BTC | DOWN | 0.57 | 0.74 | 1.38 |
| 10-16 15:01 | +10 | BTC | DOWN | 0.57 | 0.74 | 1.38 |
| 10-16 15:01 | +5 | BTC | DOWN | 0.56 | 0.64 | 0.45 |
| 10-16 15:01 | +10 stop | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-16 15:01 | +20 | ETH | DOWN | 0.63 | 0.89 | 2.36 |
| 10-16 15:01 | +15 | ETH | DOWN | 0.63 | 0.82 | 1.62 |
| 10-16 15:01 | +10 | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-16 15:01 | +5 | ETH | DOWN | 0.63 | 0.72 | 0.58 |
| 10-16 15:01 | +10 stop | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 10-16 15:01 | +20 | DOGE | DOWN | 0.63 | 0.83 | 1.73 |
| 10-16 15:01 | +15 | DOGE | DOWN | 0.63 | 0.82 | 1.62 |
| 10-16 15:01 | +10 | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 10-16 15:01 | +5 | DOGE | DOWN | 0.63 | 0.72 | 0.58 |
| 10-16 15:01 | +10 stop | HYPE | DOWN | 0.64 | 0.78 | 1.10 |
| 10-16 15:01 | +20 | HYPE | DOWN | 0.64 | 0.85 | 1.84 |
| 10-16 15:01 | +15 | HYPE | DOWN | 0.64 | 0.81 | 1.42 |
| 10-16 15:01 | +10 | HYPE | DOWN | 0.64 | 0.78 | 1.10 |
| 10-16 15:01 | +5 | HYPE | DOWN | 0.65 | 0.78 | 1.01 |
| 10-16 14:52 | +10 | BNB | DOWN | 0.64 | 0.75 | 0.79 |
| 10-16 14:52 | +10 stop | ETH | DOWN | 0.64 | 0.76 | 0.90 |
| 10-16 14:52 | +5 | BNB | DOWN | 0.61 | 0.66 | 0.20 |
| 10-16 14:52 | +10 stop | NEAR | DOWN | 0.50 | 0.66 | 1.26 |
| 10-16 14:52 | +10 stop | BTC | DOWN | 0.67 | 0.78 | 0.81 |
