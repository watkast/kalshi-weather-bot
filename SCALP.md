# Range-Scalp Bot

*Updated Fri Nov 13 08:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58004 | 50604 | 7400 (102) | 0 | $-15706.01 | -4.3% |
| **+10¢** | 43335 | 34686 | 8649 (134) | 0 | $-14675.08 | -5.4% |
| **+15¢** | 36331 | 27020 | 9311 (168) | 0 | $-13227.61 | -5.8% |
| **+20¢** | 32367 | 22593 | 9774 (219) | 1 | $-11603.48 | -5.7% |
| **+10¢ (15¢ stop)** | 70679 | 70550 | 129 (79) | 0 | $-25989.91 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 08:17 | +10 stop | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-13 08:17 | +20 | DOGE | DOWN | 0.68 | open |  |
| 11-13 08:17 | +15 | DOGE | DOWN | 0.68 | 0.83 | 1.24 |
| 11-13 08:17 | +10 | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-13 08:17 | +5 | DOGE | DOWN | 0.68 | 0.75 | 0.40 |
| 11-13 08:17 | +10 stop | SOL | DOWN | 0.61 | 0.77 | 1.30 |
| 11-13 08:17 | +20 | SOL | DOWN | 0.61 | 0.84 | 2.03 |
| 11-13 08:17 | +15 | SOL | DOWN | 0.61 | 0.77 | 1.30 |
| 11-13 08:17 | +10 | SOL | DOWN | 0.61 | 0.77 | 1.30 |
| 11-13 08:17 | +5 | SOL | DOWN | 0.60 | 0.69 | 0.58 |
| 11-13 08:17 | +10 | BNB | DOWN | 0.71 | 0.83 | 0.95 |
| 11-13 08:17 | +5 | BNB | DOWN | 0.71 | 0.78 | 0.42 |
| 11-13 08:16 | +10 stop | HYPE | DOWN | 0.66 | 0.77 | 0.81 |
| 11-13 08:16 | +20 | HYPE | DOWN | 0.66 | 0.91 | 2.23 |
| 11-13 08:16 | +15 | HYPE | DOWN | 0.66 | 0.81 | 1.23 |
| 11-13 08:16 | +10 | HYPE | DOWN | 0.66 | 0.77 | 0.85 |
| 11-13 08:16 | +5 | HYPE | DOWN | 0.64 | 0.72 | 0.48 |
| 11-13 08:16 | +10 stop | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 11-13 08:16 | +20 | XRP | DOWN | 0.68 | 0.88 | 1.76 |
| 11-13 08:16 | +15 | XRP | DOWN | 0.68 | 0.83 | 1.24 |
| 11-13 08:16 | +10 | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 11-13 08:16 | +5 | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 11-13 08:16 | +10 stop | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-13 08:16 | +20 | ZEC | DOWN | 0.69 | 0.89 | 1.78 |
| 11-13 08:16 | +15 | ZEC | DOWN | 0.68 | 0.86 | 1.55 |
| 11-13 08:16 | +10 | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-13 08:16 | +5 | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-13 08:13 | +10 stop | ETH | UP | 0.61 | 0.72 | 0.78 |
| 11-13 08:13 | +10 stop | DOGE | UP | 0.54 | 0.33 | -2.44 |
| 11-13 08:13 | +20 | DOGE | UP | 0.54 | 0.88 | 3.14 |
| 11-13 08:13 | +15 | DOGE | UP | 0.55 | 0.88 | 3.04 |
| 11-13 08:09 | +10 stop | BNB | DOWN | 0.63 | 0.47 | -1.95 |
| 11-13 08:08 | +10 stop | BNB | UP | 0.58 | 0.29 | -3.25 |
| 11-13 08:07 | +10 stop | BNB | DOWN | 0.41 | 0.57 | 1.25 |
| 11-13 08:05 | +10 stop | NEAR | UP | 0.44 | 0.57 | 0.90 |
| 11-13 08:05 | +10 stop | DOGE | UP | 0.49 | 0.63 | 1.05 |
| 11-13 08:04 | +10 stop | ZEC | UP | 0.66 | 0.76 | 0.71 |
| 11-13 08:04 | +10 stop | ETH | UP | 0.62 | 0.74 | 0.89 |
| 11-13 08:03 | +5 | DOGE | DOWN | 0.60 | 0.77 | 1.40 |
| 11-13 08:03 | +10 stop | BNB | DOWN | 0.65 | 0.46 | -2.24 |
