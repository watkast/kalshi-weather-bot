# Range-Scalp Bot

*Updated Sun Nov 22 00:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68046 | 59392 | 8654 (138) | 1 | $-18204.44 | -4.3% |
| **+10¢** | 50804 | 40695 | 10109 (181) | 1 | $-16867.44 | -5.3% |
| **+15¢** | 42584 | 31685 | 10899 (230) | 2 | $-15135.79 | -5.7% |
| **+20¢** | 37909 | 26454 | 11455 (288) | 2 | $-13458.17 | -5.7% |
| **+10¢ (15¢ stop)** | 82828 | 82650 | 178 (110) | 0 | $-30400.86 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 00:57 | +10 stop | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 11-22 00:57 | +20 | ETH | DOWN | 0.70 | 0.92 | 1.98 |
| 11-22 00:57 | +15 | ETH | DOWN | 0.70 | 0.92 | 1.98 |
| 11-22 00:57 | +10 | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 11-22 00:57 | +5 | ETH | DOWN | 0.70 | 0.79 | 0.63 |
| 11-22 00:56 | +10 stop | ZEC | UP | 0.68 | 0.79 | 0.86 |
| 11-22 00:56 | +10 | ZEC | UP | 0.68 | 0.79 | 0.86 |
| 11-22 00:56 | +5 | ZEC | UP | 0.68 | 0.73 | 0.24 |
| 11-22 00:53 | +10 stop | DOGE | DOWN | 0.61 | 0.71 | 0.68 |
| 11-22 00:52 | +10 stop | BNB | DOWN | 0.69 | 0.51 | -2.15 |
| 11-22 00:52 | +10 stop | ETH | DOWN | 0.66 | 0.50 | -1.94 |
| 11-22 00:52 | +10 stop | ZEC | UP | 0.63 | 0.75 | 0.89 |
| 11-22 00:52 | +20 | ZEC | UP | 0.63 | 0.97 | 3.18 |
| 11-22 00:52 | +15 | ZEC | UP | 0.63 | 0.79 | 1.31 |
| 11-22 00:52 | +10 | ZEC | UP | 0.65 | 0.75 | 0.70 |
| 11-22 00:52 | +5 | ZEC | UP | 0.65 | 0.71 | 0.29 |
| 11-22 00:51 | +10 | BNB | UP | 0.61 | open |  |
| 11-22 00:51 | +10 stop | ETH | UP | 0.59 | 0.43 | -1.95 |
| 11-22 00:50 | +5 | SOL | DOWN | 0.66 | 0.86 | 1.75 |
| 11-22 00:50 | +10 stop | BNB | UP | 0.61 | 0.32 | -3.23 |
| 11-22 00:50 | +5 | BNB | UP | 0.61 | open |  |
| 11-22 00:50 | +10 stop | DOGE | DOWN | 0.52 | 0.65 | 1.00 |
| 11-22 00:49 | +10 stop | BTC | DOWN | 0.63 | 0.78 | 1.20 |
| 11-22 00:49 | +15 | BTC | DOWN | 0.63 | 0.78 | 1.20 |
| 11-22 00:49 | +10 | BTC | DOWN | 0.63 | 0.78 | 1.20 |
| 11-22 00:49 | +5 | BTC | DOWN | 0.63 | 0.70 | 0.38 |
| 11-22 00:49 | +10 stop | SOL | DOWN | 0.67 | 0.86 | 1.65 |
| 11-22 00:49 | +20 | SOL | DOWN | 0.67 | 0.87 | 1.76 |
| 11-22 00:49 | +15 | SOL | DOWN | 0.67 | 0.86 | 1.65 |
| 11-22 00:49 | +10 | SOL | DOWN | 0.67 | 0.86 | 1.65 |
| 11-22 00:49 | +5 | SOL | DOWN | 0.67 | 0.74 | 0.40 |
| 11-22 00:49 | +10 stop | ETH | DOWN | 0.67 | 0.49 | -2.14 |
| 11-22 00:49 | +10 | ETH | DOWN | 0.67 | 0.80 | 1.02 |
| 11-22 00:49 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 11-22 00:48 | +10 stop | DOGE | DOWN | 0.62 | 0.46 | -1.95 |
| 11-22 00:48 | +10 | DOGE | DOWN | 0.62 | 0.75 | 0.99 |
| 11-22 00:48 | +5 | DOGE | DOWN | 0.62 | 0.71 | 0.58 |
| 11-22 00:48 | +5 | XRP | DOWN | 0.61 | 0.74 | 0.99 |
| 11-22 00:48 | +10 stop | ZEC | UP | 0.59 | 0.72 | 1.00 |
| 11-22 00:48 | +10 | ZEC | UP | 0.59 | 0.72 | 1.00 |
