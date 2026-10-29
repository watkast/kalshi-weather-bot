# Range-Scalp Bot

*Updated Thu Oct 29 23:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39875 | 34829 | 5046 (51) | 4 | $-10938.73 | -4.4% |
| **+10¢** | 29720 | 23884 | 5836 (74) | 4 | $-9670.96 | -5.2% |
| **+15¢** | 24853 | 18574 | 6279 (101) | 3 | $-8668.77 | -5.6% |
| **+20¢** | 22051 | 15467 | 6584 (130) | 4 | $-7593.00 | -5.5% |
| **+10¢ (15¢ stop)** | 48683 | 48613 | 70 (37) | 0 | $-18399.42 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 23:26 | +10 stop | NEAR | UP | 0.69 | 0.50 | -2.23 |
| 10-29 23:24 | +10 stop | BTC | DOWN | 0.61 | 0.72 | 0.78 |
| 10-29 23:24 | +10 stop | ETH | DOWN | 0.50 | 0.31 | -2.23 |
| 10-29 23:24 | +10 stop | SOL | DOWN | 0.47 | 0.67 | 1.66 |
| 10-29 23:23 | +10 stop | DOGE | DOWN | 0.62 | 0.26 | -3.91 |
| 10-29 23:23 | +10 stop | ZEC | UP | 0.60 | 0.74 | 1.09 |
| 10-29 23:23 | +20 | ZEC | UP | 0.60 | 0.81 | 1.82 |
| 10-29 23:23 | +15 | ZEC | UP | 0.60 | 0.81 | 1.85 |
| 10-29 23:23 | +10 | ZEC | UP | 0.59 | 0.74 | 1.19 |
| 10-29 23:23 | +5 | ZEC | UP | 0.58 | 0.74 | 1.28 |
| 10-29 23:23 | +10 stop | NEAR | UP | 0.57 | 0.41 | -1.95 |
| 10-29 23:23 | +10 stop | SOL | UP | 0.57 | 0.30 | -3.03 |
| 10-29 23:22 | +10 stop | HYPE | UP | 0.61 | 0.43 | -2.19 |
| 10-29 23:22 | +10 stop | DOGE | UP | 0.63 | 0.43 | -2.35 |
| 10-29 23:22 | +10 | DOGE | UP | 0.63 | 0.74 | 0.79 |
| 10-29 23:21 | +10 stop | NEAR | UP | 0.62 | 0.72 | 0.68 |
| 10-29 23:21 | +5 | DOGE | UP | 0.70 | 0.84 | 1.15 |
| 10-29 23:20 | +10 stop | ETH | UP | 0.54 | 0.25 | -3.22 |
| 10-29 23:20 | +10 stop | SOL | UP | 0.65 | 0.49 | -1.94 |
| 10-29 23:20 | +15 | SOL | UP | 0.65 | 0.83 | 1.54 |
| 10-29 23:20 | +10 | SOL | UP | 0.65 | 0.83 | 1.54 |
| 10-29 23:20 | +5 | SOL | UP | 0.65 | 0.73 | 0.50 |
| 10-29 23:19 | +10 stop | NEAR | UP | 0.54 | 0.66 | 0.86 |
| 10-29 23:19 | +10 stop | DOGE | UP | 0.58 | 0.70 | 0.87 |
| 10-29 23:19 | +15 | DOGE | UP | 0.58 | 0.74 | 1.28 |
| 10-29 23:19 | +10 | DOGE | UP | 0.58 | 0.70 | 0.87 |
| 10-29 23:19 | +5 | DOGE | UP | 0.59 | 0.64 | 0.16 |
| 10-29 23:18 | +5 | SOL | UP | 0.55 | 0.62 | 0.35 |
| 10-29 23:18 | +10 stop | HYPE | UP | 0.53 | 0.68 | 1.16 |
| 10-29 23:18 | +10 stop | DOGE | UP | 0.55 | 0.69 | 1.07 |
| 10-29 23:18 | +10 | DOGE | UP | 0.55 | 0.69 | 1.07 |
| 10-29 23:17 | +5 | DOGE | UP | 0.63 | 0.69 | 0.28 |
| 10-29 23:17 | +10 stop | ETH | UP | 0.68 | 0.49 | -2.24 |
| 10-29 23:17 | +10 | ETH | UP | 0.68 | open |  |
| 10-29 23:17 | +5 | ETH | UP | 0.69 | open |  |
| 10-29 23:17 | +5 | DOGE | UP | 0.53 | 0.59 | 0.25 |
| 10-29 23:17 | +5 | NEAR | DOWN | 0.57 | open |  |
| 10-29 23:17 | +10 stop | ETH | UP | 0.54 | 0.64 | 0.65 |
| 10-29 23:17 | +20 | ETH | UP | 0.54 | open |  |
| 10-29 23:17 | +15 | ETH | UP | 0.54 | 0.70 | 1.27 |
