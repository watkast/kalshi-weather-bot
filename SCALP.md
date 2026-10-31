# Range-Scalp Bot

*Updated Sat Oct 31 15:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42404 | 36989 | 5415 (59) | 3 | $-11911.24 | -4.5% |
| **+10¢** | 31614 | 25346 | 6268 (81) | 4 | $-10699.89 | -5.4% |
| **+15¢** | 26441 | 19682 | 6759 (109) | 4 | $-9797.89 | -5.9% |
| **+20¢** | 23482 | 16398 | 7084 (141) | 4 | $-8665.57 | -5.9% |
| **+10¢ (15¢ stop)** | 51715 | 51636 | 79 (44) | 0 | $-19541.32 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 15:25 | +10 stop | ETH | DOWN | 0.69 | 0.54 | -1.83 |
| 10-31 15:25 | +20 | ETH | DOWN | 0.69 | open |  |
| 10-31 15:25 | +15 | ETH | DOWN | 0.69 | open |  |
| 10-31 15:25 | +10 | ETH | DOWN | 0.70 | open |  |
| 10-31 15:25 | +5 | ETH | DOWN | 0.70 | 0.75 | 0.21 |
| 10-31 15:25 | +10 stop | BTC | UP | 0.66 | 0.82 | 1.33 |
| 10-31 15:24 | +10 stop | BTC | DOWN | 0.58 | 0.40 | -2.15 |
| 10-31 15:23 | +10 stop | ZEC | DOWN | 0.65 | 0.46 | -2.24 |
| 10-31 15:23 | +5 | NEAR | DOWN | 0.64 | open |  |
| 10-31 15:22 | +10 stop | NEAR | DOWN | 0.67 | 0.49 | -2.14 |
| 10-31 15:22 | +5 | ETH | DOWN | 0.59 | 0.73 | 1.09 |
| 10-31 15:22 | +10 stop | DOGE | DOWN | 0.60 | 0.81 | 1.82 |
| 10-31 15:22 | +10 stop | ETH | DOWN | 0.59 | 0.73 | 1.09 |
| 10-31 15:21 | +5 | BTC | UP | 0.62 | 0.69 | 0.38 |
| 10-31 15:20 | +10 stop | ZEC | UP | 0.63 | 0.46 | -2.05 |
| 10-31 15:20 | +20 | ZEC | UP | 0.63 | 0.85 | 1.94 |
| 10-31 15:20 | +15 | ZEC | UP | 0.63 | 0.78 | 1.20 |
| 10-31 15:20 | +10 | ZEC | UP | 0.63 | 0.78 | 1.20 |
| 10-31 15:20 | +5 | ZEC | UP | 0.63 | 0.70 | 0.38 |
| 10-31 15:20 | +5 | DOGE | UP | 0.68 | open |  |
| 10-31 15:19 | +10 stop | NEAR | UP | 0.59 | 0.44 | -1.85 |
| 10-31 15:19 | +10 stop | SOL | UP | 0.71 | 0.82 | 0.84 |
| 10-31 15:19 | +20 | SOL | UP | 0.71 | 0.91 | 1.80 |
| 10-31 15:19 | +15 | SOL | UP | 0.71 | 0.86 | 1.26 |
| 10-31 15:19 | +10 | SOL | UP | 0.71 | 0.82 | 0.84 |
| 10-31 15:19 | +5 | SOL | UP | 0.71 | 0.82 | 0.84 |
| 10-31 15:19 | +10 stop | ETH | UP | 0.62 | 0.45 | -2.05 |
| 10-31 15:19 | +10 stop | BTC | UP | 0.58 | 0.40 | -2.15 |
| 10-31 15:19 | +15 | BTC | UP | 0.58 | 0.82 | 2.11 |
| 10-31 15:19 | +10 | BTC | UP | 0.58 | 0.69 | 0.77 |
| 10-31 15:19 | +5 | BTC | UP | 0.57 | 0.63 | 0.25 |
| 10-31 15:19 | +5 | DOGE | UP | 0.59 | 0.66 | 0.37 |
| 10-31 15:19 | +10 stop | BNB | UP | 0.62 | 0.83 | 1.83 |
| 10-31 15:18 | +10 stop | DOGE | UP | 0.71 | 0.39 | -3.52 |
| 10-31 15:18 | +20 | DOGE | UP | 0.71 | open |  |
| 10-31 15:18 | +15 | DOGE | UP | 0.71 | open |  |
| 10-31 15:18 | +10 | DOGE | UP | 0.71 | open |  |
| 10-31 15:18 | +5 | DOGE | UP | 0.71 | 0.80 | 0.63 |
| 10-31 15:18 | +10 stop | NEAR | UP | 0.60 | 0.71 | 0.78 |
| 10-31 15:18 | +5 | SOL | UP | 0.70 | 0.75 | 0.21 |
