# Range-Scalp Bot

*Updated Mon Nov 16 11:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61967 | 54066 | 7901 (115) | 3 | $-16739.70 | -4.3% |
| **+10¢** | 46286 | 37037 | 9249 (157) | 3 | $-15623.91 | -5.4% |
| **+15¢** | 38788 | 28816 | 9972 (196) | 3 | $-14198.39 | -5.8% |
| **+20¢** | 34578 | 24123 | 10455 (249) | 5 | $-12371.25 | -5.7% |
| **+10¢ (15¢ stop)** | 75421 | 75267 | 154 (90) | 0 | $-27803.24 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 11:25 | +10 stop | DOGE | DOWN | 0.43 | 0.55 | 0.84 |
| 11-16 11:24 | +10 stop | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 11-16 11:23 | +10 stop | DOGE | DOWN | 0.68 | 0.52 | -1.94 |
| 11-16 11:22 | +10 stop | NEAR | DOWN | 0.52 | 0.27 | -2.82 |
| 11-16 11:22 | +10 stop | XRP | DOWN | 0.67 | 0.45 | -2.54 |
| 11-16 11:22 | +5 | ZEC | UP | 0.65 | 0.71 | 0.29 |
| 11-16 11:21 | +10 stop | DOGE | DOWN | 0.65 | 0.76 | 0.84 |
| 11-16 11:21 | +10 stop | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 11-16 11:20 | +10 stop | ETH | UP | 0.70 | 0.84 | 1.15 |
| 11-16 11:20 | +20 | ETH | UP | 0.69 | open |  |
| 11-16 11:20 | +15 | ETH | UP | 0.70 | 0.87 | 1.47 |
| 11-16 11:20 | +10 | ETH | UP | 0.70 | 0.84 | 1.15 |
| 11-16 11:20 | +5 | ETH | UP | 0.70 | 0.76 | 0.32 |
| 11-16 11:20 | +5 | ZEC | UP | 0.63 | 0.71 | 0.49 |
| 11-16 11:19 | +5 | HYPE | DOWN | 0.67 | 0.72 | 0.21 |
| 11-16 11:19 | +5 | XRP | UP | 0.63 | open |  |
| 11-16 11:18 | +10 stop | HYPE | DOWN | 0.57 | 0.68 | 0.76 |
| 11-16 11:18 | +20 | HYPE | DOWN | 0.57 | 0.86 | 2.63 |
| 11-16 11:18 | +15 | HYPE | DOWN | 0.57 | 0.72 | 1.17 |
| 11-16 11:18 | +10 | HYPE | DOWN | 0.57 | 0.68 | 0.76 |
| 11-16 11:18 | +5 | HYPE | DOWN | 0.57 | 0.65 | 0.46 |
| 11-16 11:18 | +10 stop | XRP | UP | 0.68 | 0.40 | -3.13 |
| 11-16 11:18 | +15 | XRP | UP | 0.68 | open |  |
| 11-16 11:18 | +10 | XRP | UP | 0.68 | open |  |
| 11-16 11:18 | +5 | XRP | UP | 0.68 | 0.73 | 0.20 |
| 11-16 11:18 | +10 stop | SOL | UP | 0.64 | 0.48 | -1.95 |
| 11-16 11:18 | +10 | SOL | UP | 0.66 | open |  |
| 11-16 11:18 | +5 | SOL | UP | 0.66 | open |  |
| 11-16 11:18 | +5 | NEAR | UP | 0.70 | 0.77 | 0.43 |
| 11-16 11:18 | +20 | DOGE | UP | 0.70 | open |  |
| 11-16 11:18 | +15 | DOGE | UP | 0.70 | open |  |
| 11-16 11:18 | +5 | DOGE | UP | 0.69 | open |  |
| 11-16 11:18 | +10 stop | ZEC | UP | 0.65 | 0.79 | 1.12 |
| 11-16 11:18 | +10 | ZEC | UP | 0.65 | 0.79 | 1.12 |
| 11-16 11:18 | +5 | ZEC | UP | 0.63 | 0.68 | 0.17 |
| 11-16 11:17 | +10 stop | DOGE | UP | 0.71 | 0.50 | -2.43 |
| 11-16 11:17 | +10 | DOGE | UP | 0.70 | open |  |
| 11-16 11:17 | +5 | ZEC | UP | 0.65 | 0.76 | 0.81 |
| 11-16 11:16 | +5 | DOGE | UP | 0.64 | 0.69 | 0.22 |
| 11-16 11:16 | +5 | XRP | UP | 0.67 | 0.74 | 0.40 |
