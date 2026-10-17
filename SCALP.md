# Range-Scalp Bot

*Updated Sat Oct 17 03:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20324 | 17677 | 2647 (29) | 0 | $-6023.84 | -4.7% |
| **+10¢** | 15315 | 12261 | 3054 (41) | 0 | $-5372.18 | -5.6% |
| **+15¢** | 12804 | 9520 | 3284 (60) | 0 | $-4841.66 | -6.0% |
| **+20¢** | 11355 | 7915 | 3440 (79) | 0 | $-4278.39 | -6.0% |
| **+10¢ (15¢ stop)** | 24990 | 24940 | 50 (29) | 0 | $-9471.68 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 03:54 | +10 stop | ZEC | DOWN | 0.61 | 0.78 | 1.40 |
| 10-17 03:54 | +5 | ZEC | DOWN | 0.61 | 0.66 | 0.17 |
| 10-17 03:53 | +10 stop | HYPE | DOWN | 0.69 | 0.80 | 0.83 |
| 10-17 03:53 | +10 | HYPE | DOWN | 0.69 | 0.80 | 0.83 |
| 10-17 03:53 | +5 | BNB | DOWN | 0.71 | 0.77 | 0.32 |
| 10-17 03:52 | +5 | HYPE | DOWN | 0.63 | 0.74 | 0.75 |
| 10-17 03:50 | +5 | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 10-17 03:50 | +10 stop | ZEC | UP | 0.53 | 0.26 | -3.02 |
| 10-17 03:48 | +10 stop | ZEC | DOWN | 0.57 | 0.40 | -2.05 |
| 10-17 03:46 | +10 stop | BNB | DOWN | 0.65 | 0.77 | 0.92 |
| 10-17 03:46 | +20 | BNB | DOWN | 0.65 | 0.90 | 2.29 |
| 10-17 03:46 | +15 | BNB | DOWN | 0.65 | 0.80 | 1.23 |
| 10-17 03:46 | +10 | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 10-17 03:46 | +5 | BNB | DOWN | 0.64 | 0.69 | 0.18 |
| 10-17 03:46 | +10 stop | BTC | DOWN | 0.64 | 0.49 | -1.85 |
| 10-17 03:46 | +20 | BTC | DOWN | 0.64 | 0.85 | 1.84 |
| 10-17 03:46 | +15 | BTC | DOWN | 0.64 | 0.81 | 1.42 |
| 10-17 03:46 | +10 | BTC | DOWN | 0.64 | 0.76 | 0.90 |
| 10-17 03:46 | +5 | BTC | DOWN | 0.64 | 0.76 | 0.90 |
| 10-17 03:46 | +10 stop | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 10-17 03:46 | +20 | SOL | DOWN | 0.67 | 0.87 | 1.76 |
| 10-17 03:46 | +15 | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 10-17 03:46 | +10 | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 10-17 03:46 | +5 | SOL | DOWN | 0.67 | 0.72 | 0.19 |
| 10-17 03:46 | +10 stop | ETH | DOWN | 0.70 | 0.83 | 1.05 |
| 10-17 03:46 | +20 | ETH | DOWN | 0.70 | 0.91 | 1.88 |
| 10-17 03:46 | +15 | ETH | DOWN | 0.70 | 0.89 | 1.68 |
| 10-17 03:46 | +10 | ETH | DOWN | 0.70 | 0.83 | 1.05 |
| 10-17 03:46 | +5 | ETH | DOWN | 0.69 | 0.74 | 0.21 |
| 10-17 03:46 | +10 stop | ZEC | DOWN | 0.66 | 0.47 | -2.24 |
| 10-17 03:46 | +20 | ZEC | DOWN | 0.66 | 0.89 | 2.07 |
| 10-17 03:46 | +15 | ZEC | DOWN | 0.64 | 0.80 | 1.31 |
| 10-17 03:46 | +10 | ZEC | DOWN | 0.64 | 0.78 | 1.10 |
| 10-17 03:46 | +5 | ZEC | DOWN | 0.64 | 0.70 | 0.28 |
| 10-17 03:46 | +10 stop | HYPE | DOWN | 0.56 | 0.67 | 0.76 |
| 10-17 03:46 | +20 | HYPE | DOWN | 0.56 | 0.80 | 2.10 |
| 10-17 03:46 | +15 | HYPE | DOWN | 0.56 | 0.74 | 1.48 |
| 10-17 03:46 | +10 | HYPE | DOWN | 0.56 | 0.67 | 0.76 |
| 10-17 03:46 | +5 | HYPE | DOWN | 0.56 | 0.63 | 0.35 |
| 10-17 03:41 | +10 stop | BTC | UP | 0.69 | 0.79 | 0.73 |
