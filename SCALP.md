# Range-Scalp Bot

*Updated Sat Oct 17 05:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20422 | 17763 | 2659 (29) | 0 | $-6039.21 | -4.7% |
| **+10¢** | 15385 | 12320 | 3065 (41) | 2 | $-5363.99 | -5.5% |
| **+15¢** | 12869 | 9573 | 3296 (60) | 2 | $-4824.49 | -6.0% |
| **+20¢** | 11411 | 7958 | 3453 (79) | 2 | $-4269.08 | -6.0% |
| **+10¢ (15¢ stop)** | 25103 | 25053 | 50 (29) | 0 | $-9495.50 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 05:28 | +10 stop | XRP | DOWN | 0.65 | 0.94 | 2.75 |
| 10-17 05:28 | +10 stop | XRP | UP | 0.37 | 0.67 | 2.67 |
| 10-17 05:27 | +10 stop | XRP | UP | 0.49 | 0.64 | 1.15 |
| 10-17 05:27 | +10 stop | HYPE | DOWN | 0.64 | 0.81 | 1.42 |
| 10-17 05:27 | +20 | HYPE | DOWN | 0.64 | 0.85 | 1.84 |
| 10-17 05:27 | +15 | HYPE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-17 05:27 | +10 | HYPE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-17 05:27 | +5 | HYPE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-17 05:26 | +10 stop | ETH | UP | 0.53 | 0.66 | 0.96 |
| 10-17 05:26 | +20 | ETH | UP | 0.53 | 0.80 | 2.40 |
| 10-17 05:26 | +15 | ETH | UP | 0.53 | 0.80 | 2.40 |
| 10-17 05:26 | +10 | ETH | UP | 0.53 | 0.66 | 0.96 |
| 10-17 05:26 | +5 | ETH | UP | 0.54 | 0.66 | 0.86 |
| 10-17 05:25 | +10 stop | XRP | DOWN | 0.69 | 0.54 | -1.83 |
| 10-17 05:25 | +5 | HYPE | DOWN | 0.59 | 0.75 | 1.29 |
| 10-17 05:24 | +10 stop | HYPE | DOWN | 0.58 | 0.75 | 1.38 |
| 10-17 05:24 | +5 | HYPE | DOWN | 0.56 | 0.66 | 0.66 |
| 10-17 05:24 | +10 stop | HYPE | DOWN | 0.56 | 0.67 | 0.76 |
| 10-17 05:22 | +10 stop | XRP | UP | 0.62 | 0.73 | 0.79 |
| 10-17 05:22 | +10 stop | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 10-17 05:22 | +10 stop | HYPE | UP | 0.64 | 0.49 | -1.88 |
| 10-17 05:22 | +10 stop | XRP | UP | 0.56 | 0.66 | 0.66 |
| 10-17 05:22 | +10 stop | BNB | DOWN | 0.63 | 0.86 | 2.04 |
| 10-17 05:22 | +20 | BNB | DOWN | 0.63 | 0.86 | 2.04 |
| 10-17 05:22 | +15 | BNB | DOWN | 0.63 | 0.86 | 2.04 |
| 10-17 05:22 | +10 | BNB | DOWN | 0.63 | 0.86 | 2.04 |
| 10-17 05:22 | +5 | BNB | DOWN | 0.63 | 0.70 | 0.38 |
| 10-17 05:21 | +10 stop | ETH | UP | 0.62 | 0.72 | 0.68 |
| 10-17 05:21 | +10 stop | HYPE | DOWN | 0.62 | 0.33 | -3.23 |
| 10-17 05:21 | +20 | HYPE | DOWN | 0.62 | 0.82 | 1.72 |
| 10-17 05:21 | +15 | HYPE | DOWN | 0.62 | 0.82 | 1.72 |
| 10-17 05:21 | +10 | HYPE | DOWN | 0.62 | 0.75 | 0.99 |
| 10-17 05:21 | +5 | HYPE | DOWN | 0.62 | 0.67 | 0.17 |
| 10-17 05:21 | +5 | DOGE | DOWN | 0.60 | 0.71 | 0.78 |
| 10-17 05:20 | +10 stop | ZEC | UP | 0.70 | 0.81 | 0.84 |
| 10-17 05:20 | +5 | DOGE | DOWN | 0.53 | 0.61 | 0.45 |
| 10-17 05:20 | +10 stop | DOGE | DOWN | 0.53 | 0.71 | 1.47 |
| 10-17 05:20 | +10 stop | SOL | DOWN | 0.70 | 0.53 | -2.03 |
| 10-17 05:20 | +5 | SOL | DOWN | 0.70 | 0.79 | 0.63 |
| 10-17 05:20 | +5 | BTC | DOWN | 0.61 | 0.67 | 0.27 |
