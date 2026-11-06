# Range-Scalp Bot

*Updated Fri Nov 06 04:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49165 | 42842 | 6323 (75) | 0 | $-13933.28 | -4.5% |
| **+10¢** | 36710 | 29360 | 7350 (101) | 1 | $-12785.14 | -5.5% |
| **+15¢** | 30747 | 22834 | 7913 (130) | 1 | $-11653.24 | -6.0% |
| **+20¢** | 27330 | 19036 | 8294 (170) | 1 | $-10305.56 | -6.0% |
| **+10¢ (15¢ stop)** | 59957 | 59862 | 95 (57) | 0 | $-22200.48 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 04:13 | +10 stop | ETH | DOWN | 0.57 | 0.40 | -2.05 |
| 11-06 04:13 | +20 | ETH | DOWN | 0.57 | open |  |
| 11-06 04:13 | +15 | ETH | DOWN | 0.57 | open |  |
| 11-06 04:13 | +10 | ETH | DOWN | 0.57 | open |  |
| 11-06 04:13 | +5 | ETH | DOWN | 0.57 | 0.65 | 0.46 |
| 11-06 04:12 | +10 stop | XRP | UP | 0.65 | 0.50 | -1.84 |
| 11-06 04:12 | +20 | XRP | UP | 0.66 | 0.90 | 2.17 |
| 11-06 04:12 | +15 | XRP | UP | 0.66 | 0.90 | 2.17 |
| 11-06 04:12 | +10 | XRP | UP | 0.66 | 0.90 | 2.17 |
| 11-06 04:12 | +5 | XRP | UP | 0.66 | 0.90 | 2.17 |
| 11-06 04:09 | +10 stop | ZEC | DOWN | 0.63 | 0.48 | -1.85 |
| 11-06 04:07 | +10 stop | XRP | DOWN | 0.70 | 0.86 | 1.36 |
| 11-06 04:07 | +10 | XRP | DOWN | 0.70 | 0.86 | 1.36 |
| 11-06 04:07 | +10 stop | ZEC | UP | 0.66 | 0.51 | -1.84 |
| 11-06 04:07 | +20 | ZEC | UP | 0.66 | 0.89 | 2.07 |
| 11-06 04:07 | +15 | ZEC | UP | 0.66 | 0.81 | 1.23 |
| 11-06 04:07 | +10 | ZEC | UP | 0.66 | 0.81 | 1.23 |
| 11-06 04:07 | +5 | ZEC | UP | 0.66 | 0.71 | 0.19 |
| 11-06 04:06 | +10 stop | SOL | DOWN | 0.68 | 0.79 | 0.82 |
| 11-06 04:06 | +20 | SOL | DOWN | 0.68 | 0.88 | 1.76 |
| 11-06 04:06 | +15 | SOL | DOWN | 0.68 | 0.84 | 1.34 |
| 11-06 04:06 | +10 | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 11-06 04:06 | +5 | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 11-06 04:06 | +10 stop | BNB | DOWN | 0.57 | 0.71 | 1.07 |
| 11-06 04:06 | +20 | BNB | DOWN | 0.57 | 0.80 | 2.00 |
| 11-06 04:06 | +15 | BNB | DOWN | 0.57 | 0.80 | 2.00 |
| 11-06 04:06 | +10 | BNB | DOWN | 0.57 | 0.71 | 1.07 |
| 11-06 04:06 | +5 | BNB | DOWN | 0.58 | 0.71 | 0.97 |
| 11-06 04:05 | +5 | XRP | DOWN | 0.70 | 0.86 | 1.36 |
| 11-06 04:03 | +10 stop | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-06 04:03 | +15 | BTC | DOWN | 0.71 | 0.87 | 1.37 |
| 11-06 04:03 | +10 | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-06 04:03 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 11-06 04:03 | +10 stop | SOL | DOWN | 0.64 | 0.77 | 1.00 |
| 11-06 04:03 | +20 | SOL | DOWN | 0.64 | 0.87 | 2.05 |
| 11-06 04:03 | +15 | SOL | DOWN | 0.64 | 0.80 | 1.31 |
| 11-06 04:03 | +10 | SOL | DOWN | 0.64 | 0.77 | 1.00 |
| 11-06 04:03 | +5 | SOL | DOWN | 0.64 | 0.73 | 0.59 |
| 11-06 04:02 | +10 stop | ZEC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-06 04:02 | +10 | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
