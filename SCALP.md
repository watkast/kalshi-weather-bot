# Range-Scalp Bot

*Updated Sun Oct 25 11:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33064 | 28852 | 4212 (42) | 1 | $-9249.90 | -4.4% |
| **+10¢** | 24744 | 19868 | 4876 (60) | 1 | $-8228.60 | -5.3% |
| **+15¢** | 20710 | 15461 | 5249 (83) | 1 | $-7395.19 | -5.7% |
| **+20¢** | 18347 | 12851 | 5496 (105) | 1 | $-6515.76 | -5.7% |
| **+10¢ (15¢ stop)** | 40567 | 40507 | 60 (32) | 0 | $-15452.56 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 11:24 | +10 stop | NEAR | DOWN | 0.54 | 0.70 | 1.27 |
| 10-25 11:20 | +10 stop | NEAR | UP | 0.67 | 0.49 | -2.14 |
| 10-25 11:20 | +15 | NEAR | UP | 0.67 | open |  |
| 10-25 11:20 | +10 | NEAR | UP | 0.67 | open |  |
| 10-25 11:20 | +5 | NEAR | UP | 0.67 | open |  |
| 10-25 11:17 | +10 stop | SOL | UP | 0.66 | 0.78 | 0.91 |
| 10-25 11:17 | +20 | SOL | UP | 0.66 | 0.86 | 1.75 |
| 10-25 11:17 | +15 | SOL | UP | 0.66 | 0.81 | 1.23 |
| 10-25 11:17 | +10 | SOL | UP | 0.66 | 0.78 | 0.91 |
| 10-25 11:17 | +5 | SOL | UP | 0.66 | 0.73 | 0.40 |
| 10-25 11:17 | +10 stop | DOGE | UP | 0.68 | 0.81 | 1.03 |
| 10-25 11:17 | +20 | DOGE | UP | 0.68 | 0.91 | 2.12 |
| 10-25 11:17 | +15 | DOGE | UP | 0.68 | 0.87 | 1.66 |
| 10-25 11:17 | +10 | DOGE | UP | 0.68 | 0.81 | 1.03 |
| 10-25 11:17 | +5 | DOGE | UP | 0.68 | 0.77 | 0.61 |
| 10-25 11:17 | +10 stop | ZEC | UP | 0.69 | 0.83 | 1.15 |
| 10-25 11:17 | +20 | ZEC | UP | 0.69 | 0.89 | 1.78 |
| 10-25 11:17 | +15 | ZEC | UP | 0.69 | 0.87 | 1.57 |
| 10-25 11:17 | +10 | ZEC | UP | 0.68 | 0.83 | 1.24 |
| 10-25 11:17 | +5 | ZEC | UP | 0.68 | 0.83 | 1.24 |
| 10-25 11:17 | +10 stop | NEAR | UP | 0.63 | 0.75 | 0.89 |
| 10-25 11:17 | +20 | NEAR | UP | 0.63 | open |  |
| 10-25 11:17 | +15 | NEAR | UP | 0.63 | 0.82 | 1.62 |
| 10-25 11:17 | +10 | NEAR | UP | 0.63 | 0.75 | 0.89 |
| 10-25 11:17 | +5 | NEAR | UP | 0.63 | 0.69 | 0.28 |
| 10-25 11:15 | +10 stop | HYPE | UP | 0.67 | 0.82 | 1.20 |
| 10-25 11:15 | +20 | HYPE | UP | 0.67 | 0.91 | 2.16 |
| 10-25 11:15 | +15 | HYPE | UP | 0.67 | 0.85 | 1.52 |
| 10-25 11:15 | +10 | HYPE | UP | 0.68 | 0.82 | 1.09 |
| 10-25 11:15 | +5 | HYPE | UP | 0.68 | 0.77 | 0.57 |
| 10-25 11:10 | +10 stop | HYPE | DOWN | 0.50 | 0.19 | -3.39 |
| 10-25 11:10 | +20 | HYPE | DOWN | 0.49 | yes | -5.08 |
| 10-25 11:10 | +15 | HYPE | DOWN | 0.49 | yes | -5.08 |
| 10-25 11:10 | +10 | HYPE | DOWN | 0.49 | yes | -5.08 |
| 10-25 11:10 | +5 | HYPE | DOWN | 0.49 | 0.55 | 0.24 |
| 10-25 11:09 | +10 stop | DOGE | DOWN | 0.40 | 0.53 | 0.95 |
| 10-25 11:09 | +10 stop | SOL | DOWN | 0.65 | 0.34 | -3.42 |
| 10-25 11:09 | +10 stop | ETH | UP | 0.70 | 0.80 | 0.73 |
| 10-25 11:09 | +20 | ETH | UP | 0.70 | 0.92 | 1.96 |
| 10-25 11:09 | +15 | ETH | UP | 0.70 | 0.85 | 1.26 |
