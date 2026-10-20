# Range-Scalp Bot

*Updated Tue Oct 20 14:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25744 | 22425 | 3319 (31) | 0 | $-7488.36 | -4.6% |
| **+10¢** | 19379 | 15546 | 3833 (46) | 0 | $-6598.38 | -5.4% |
| **+15¢** | 16222 | 12093 | 4129 (70) | 0 | $-5909.96 | -5.8% |
| **+20¢** | 14351 | 10027 | 4324 (88) | 0 | $-5274.93 | -5.9% |
| **+10¢ (15¢ stop)** | 31580 | 31527 | 53 (30) | 0 | $-11647.66 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 14:27 | +10 stop | XRP | DOWN | 0.43 | 0.59 | 1.25 |
| 10-20 14:27 | +10 | XRP | DOWN | 0.45 | 0.59 | 1.05 |
| 10-20 14:27 | +5 | XRP | DOWN | 0.45 | 0.59 | 1.05 |
| 10-20 14:27 | +10 stop | ETH | DOWN | 0.36 | 0.63 | 2.36 |
| 10-20 14:27 | +10 stop | DOGE | DOWN | 0.39 | 0.57 | 1.45 |
| 10-20 14:25 | +10 stop | SOL | DOWN | 0.68 | 0.44 | -2.74 |
| 10-20 14:25 | +10 | NEAR | UP | 0.63 | 0.82 | 1.62 |
| 10-20 14:24 | +10 stop | ETH | DOWN | 0.59 | 0.73 | 1.09 |
| 10-20 14:24 | +10 stop | DOGE | UP | 0.52 | 0.30 | -2.54 |
| 10-20 14:24 | +10 | DOGE | UP | 0.52 | 0.78 | 2.27 |
| 10-20 14:24 | +10 stop | SOL | DOWN | 0.49 | 0.59 | 0.65 |
| 10-20 14:24 | +10 stop | NEAR | UP | 0.58 | 0.82 | 2.11 |
| 10-20 14:23 | +5 | NEAR | DOWN | 0.58 | yes | -5.98 |
| 10-20 14:22 | +10 stop | SOL | DOWN | 0.69 | 0.48 | -2.43 |
| 10-20 14:21 | +10 stop | NEAR | DOWN | 0.62 | 0.40 | -2.54 |
| 10-20 14:21 | +10 stop | DOGE | DOWN | 0.66 | 0.35 | -3.42 |
| 10-20 14:21 | +5 | NEAR | DOWN | 0.61 | 0.66 | 0.17 |
| 10-20 14:20 | +10 stop | ETH | DOWN | 0.60 | 0.71 | 0.78 |
| 10-20 14:20 | +10 stop | NEAR | UP | 0.56 | 0.41 | -1.85 |
| 10-20 14:20 | +20 | NEAR | UP | 0.56 | 0.82 | 2.31 |
| 10-20 14:20 | +15 | NEAR | UP | 0.56 | 0.82 | 2.31 |
| 10-20 14:20 | +10 | NEAR | UP | 0.56 | 0.67 | 0.76 |
| 10-20 14:20 | +5 | NEAR | UP | 0.57 | 0.63 | 0.25 |
| 10-20 14:20 | +10 stop | DOGE | UP | 0.53 | 0.35 | -2.14 |
| 10-20 14:20 | +10 | DOGE | UP | 0.53 | 0.64 | 0.75 |
| 10-20 14:19 | +5 | DOGE | UP | 0.64 | 0.78 | 1.10 |
| 10-20 14:19 | +10 stop | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-20 14:19 | +10 stop | BNB | DOWN | 0.65 | 0.82 | 1.43 |
| 10-20 14:19 | +10 | BNB | DOWN | 0.65 | 0.82 | 1.43 |
| 10-20 14:19 | +10 stop | SOL | UP | 0.68 | 0.43 | -2.84 |
| 10-20 14:19 | +20 | SOL | UP | 0.68 | 0.96 | 2.58 |
| 10-20 14:19 | +15 | SOL | UP | 0.69 | 0.96 | 2.49 |
| 10-20 14:19 | +10 | SOL | UP | 0.69 | 0.83 | 1.15 |
| 10-20 14:19 | +5 | SOL | UP | 0.69 | 0.77 | 0.52 |
| 10-20 14:19 | +5 | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 10-20 14:19 | +10 stop | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 10-20 14:19 | +10 stop | DOGE | UP | 0.55 | 0.66 | 0.76 |
| 10-20 14:19 | +20 | DOGE | UP | 0.55 | 0.78 | 1.99 |
| 10-20 14:19 | +15 | DOGE | UP | 0.55 | 0.78 | 1.99 |
| 10-20 14:19 | +10 | DOGE | UP | 0.56 | 0.66 | 0.66 |
