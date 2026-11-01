# Range-Scalp Bot

*Updated Sun Nov 01 08:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43375 | 37796 | 5579 (63) | 2 | $-12405.02 | -4.5% |
| **+10¢** | 32353 | 25912 | 6441 (85) | 2 | $-11094.42 | -5.5% |
| **+15¢** | 27074 | 20137 | 6937 (112) | 2 | $-10139.13 | -6.0% |
| **+20¢** | 24044 | 16778 | 7266 (146) | 4 | $-8942.67 | -5.9% |
| **+10¢ (15¢ stop)** | 52899 | 52814 | 85 (50) | 0 | $-19990.03 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 08:23 | +10 stop | ZEC | DOWN | 0.27 | 0.57 | 2.68 |
| 11-01 08:23 | +5 | ZEC | DOWN | 0.27 | 0.57 | 2.68 |
| 11-01 08:23 | +10 stop | DOGE | DOWN | 0.47 | 0.14 | -3.57 |
| 11-01 08:22 | +10 stop | DOGE | UP | 0.58 | 0.38 | -2.35 |
| 11-01 08:22 | +10 stop | ZEC | DOWN | 0.56 | 0.74 | 1.49 |
| 11-01 08:22 | +5 | ZEC | DOWN | 0.56 | 0.65 | 0.59 |
| 11-01 08:22 | +10 stop | NEAR | UP | 0.66 | 0.79 | 1.02 |
| 11-01 08:21 | +10 stop | ETH | UP | 0.55 | 0.77 | 1.89 |
| 11-01 08:20 | +10 stop | ZEC | UP | 0.65 | 0.47 | -2.14 |
| 11-01 08:20 | +15 | ZEC | UP | 0.65 | 0.80 | 1.22 |
| 11-01 08:20 | +10 | ZEC | UP | 0.65 | 0.77 | 0.91 |
| 11-01 08:20 | +5 | ZEC | UP | 0.65 | 0.70 | 0.19 |
| 11-01 08:20 | +10 stop | BTC | UP | 0.62 | 0.82 | 1.72 |
| 11-01 08:19 | +10 stop | SOL | DOWN | 0.68 | 0.50 | -2.14 |
| 11-01 08:19 | +10 | SOL | DOWN | 0.68 | open |  |
| 11-01 08:19 | +5 | SOL | DOWN | 0.68 | open |  |
| 11-01 08:19 | +10 stop | BTC | DOWN | 0.62 | 0.38 | -2.74 |
| 11-01 08:19 | +10 stop | XRP | UP | 0.71 | 0.86 | 1.26 |
| 11-01 08:19 | +10 stop | ETH | DOWN | 0.65 | 0.49 | -1.94 |
| 11-01 08:19 | +10 stop | NEAR | DOWN | 0.50 | 0.35 | -1.84 |
| 11-01 08:19 | +10 stop | DOGE | DOWN | 0.56 | 0.39 | -2.04 |
| 11-01 08:18 | +10 stop | ETH | DOWN | 0.53 | 0.66 | 0.96 |
| 11-01 08:18 | +10 stop | SOL | DOWN | 0.56 | 0.66 | 0.66 |
| 11-01 08:18 | +20 | SOL | DOWN | 0.56 | open |  |
| 11-01 08:18 | +15 | SOL | DOWN | 0.56 | open |  |
| 11-01 08:18 | +10 | SOL | DOWN | 0.56 | 0.66 | 0.66 |
| 11-01 08:18 | +5 | SOL | DOWN | 0.56 | 0.66 | 0.66 |
| 11-01 08:18 | +10 stop | XRP | UP | 0.71 | 0.54 | -2.03 |
| 11-01 08:18 | +20 | XRP | UP | 0.70 | open |  |
| 11-01 08:18 | +15 | XRP | UP | 0.71 | 0.86 | 1.30 |
| 11-01 08:18 | +10 | XRP | UP | 0.71 | 0.86 | 1.29 |
| 11-01 08:18 | +5 | XRP | UP | 0.71 | 0.79 | 0.56 |
| 11-01 08:18 | +10 stop | HYPE | DOWN | 0.66 | 0.79 | 1.02 |
| 11-01 08:18 | +10 stop | ZEC | UP | 0.58 | 0.68 | 0.66 |
| 11-01 08:18 | +20 | ZEC | UP | 0.58 | 0.80 | 1.90 |
| 11-01 08:18 | +15 | ZEC | UP | 0.58 | 0.75 | 1.38 |
| 11-01 08:18 | +10 | ZEC | UP | 0.58 | 0.68 | 0.66 |
| 11-01 08:18 | +5 | ZEC | UP | 0.58 | 0.64 | 0.25 |
| 11-01 08:17 | +10 stop | NEAR | UP | 0.68 | 0.50 | -2.14 |
| 11-01 08:17 | +20 | NEAR | UP | 0.67 | 0.88 | 1.86 |
