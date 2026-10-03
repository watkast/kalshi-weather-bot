# Range-Scalp Bot

*Updated Sat Oct 03 11:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 687 | 594 | 93 (1) | 1 | $-225.66 | -5.2% |
| **+10¢** | 524 | 420 | 104 (2) | 0 | $-178.80 | -5.4% |
| **+15¢** | 445 | 334 | 111 (3) | 0 | $-160.14 | -5.7% |
| **+20¢** | 387 | 273 | 114 (3) | 0 | $-142.66 | -5.9% |
| **+10¢ (15¢ stop)** | 893 | 892 | 1 (1) | 0 | $-480.87 | -8.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 11:28 | +10 stop | XRP | DOWN | 0.36 | 0.65 | 2.57 |
| 10-03 11:28 | +20 | XRP | DOWN | 0.36 | 0.65 | 2.57 |
| 10-03 11:28 | +15 | XRP | DOWN | 0.36 | 0.65 | 2.57 |
| 10-03 11:28 | +10 | XRP | DOWN | 0.36 | 0.65 | 2.57 |
| 10-03 11:28 | +5 | XRP | DOWN | 0.34 | 0.65 | 2.78 |
| 10-03 11:27 | +10 stop | ZEC | UP | 0.55 | 0.72 | 1.42 |
| 10-03 11:27 | +20 | ZEC | UP | 0.55 | 0.79 | 2.15 |
| 10-03 11:27 | +15 | ZEC | UP | 0.55 | 0.72 | 1.42 |
| 10-03 11:27 | +10 | ZEC | UP | 0.55 | 0.72 | 1.42 |
| 10-03 11:27 | +5 | ZEC | UP | 0.55 | 0.62 | 0.40 |
| 10-03 11:27 | +10 stop | ETH | UP | 0.70 | 0.84 | 1.15 |
| 10-03 11:27 | +5 | ETH | UP | 0.70 | 0.84 | 1.15 |
| 10-03 11:25 | +10 stop | ETH | UP | 0.51 | 0.68 | 1.36 |
| 10-03 11:25 | +10 stop | ZEC | UP | 0.67 | 0.80 | 1.02 |
| 10-03 11:25 | +10 | ZEC | UP | 0.67 | 0.80 | 1.02 |
| 10-03 11:25 | +5 | ZEC | UP | 0.67 | 0.80 | 1.02 |
| 10-03 11:24 | +10 stop | SOL | DOWN | 0.60 | 0.78 | 1.50 |
| 10-03 11:24 | +10 stop | ETH | DOWN | 0.60 | 0.44 | -1.95 |
| 10-03 11:24 | +10 stop | HYPE | DOWN | 0.57 | 0.73 | 1.28 |
| 10-03 11:24 | +10 stop | ZEC | UP | 0.58 | 0.69 | 0.77 |
| 10-03 11:24 | +10 | ZEC | UP | 0.58 | 0.69 | 0.77 |
| 10-03 11:24 | +5 | ZEC | UP | 0.58 | 0.66 | 0.46 |
| 10-03 11:23 | +5 | BTC | UP | 0.65 | 0.70 | 0.19 |
| 10-03 11:23 | +10 stop | SOL | UP | 0.58 | 0.41 | -2.05 |
| 10-03 11:22 | +10 stop | HYPE | DOWN | 0.43 | 0.56 | 0.94 |
| 10-03 11:22 | +5 | NEAR | DOWN | 0.68 | 0.77 | 0.61 |
| 10-03 11:22 | +10 stop | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 10-03 11:21 | +10 stop | SOL | UP | 0.62 | 0.46 | -1.91 |
| 10-03 11:21 | +10 stop | XRP | DOWN | 0.59 | 0.80 | 1.82 |
| 10-03 11:21 | +10 stop | ETH | UP | 0.62 | 0.46 | -1.95 |
| 10-03 11:21 | +20 | ETH | UP | 0.62 | 0.84 | 1.93 |
| 10-03 11:21 | +15 | ETH | UP | 0.62 | 0.84 | 1.93 |
| 10-03 11:21 | +10 | ETH | UP | 0.62 | 0.84 | 1.93 |
| 10-03 11:21 | +5 | ETH | UP | 0.62 | 0.68 | 0.27 |
| 10-03 11:20 | +10 stop | BTC | UP | 0.60 | 0.70 | 0.68 |
| 10-03 11:20 | +10 | BTC | UP | 0.60 | 0.70 | 0.68 |
| 10-03 11:20 | +5 | BTC | UP | 0.60 | 0.67 | 0.37 |
| 10-03 11:20 | +5 | ZEC | UP | 0.65 | 0.75 | 0.70 |
| 10-03 11:20 | +10 stop | HYPE | UP | 0.65 | 0.39 | -2.89 |
| 10-03 11:20 | +20 | HYPE | UP | 0.65 | 0.86 | 1.89 |
