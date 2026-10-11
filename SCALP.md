# Range-Scalp Bot

*Updated Sun Oct 11 12:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11904 | 10270 | 1634 (24) | 1 | $-3979.00 | -5.3% |
| **+10¢** | 9034 | 7133 | 1901 (37) | 1 | $-3789.95 | -6.7% |
| **+15¢** | 7613 | 5598 | 2015 (54) | 1 | $-3220.23 | -6.7% |
| **+20¢** | 6788 | 4693 | 2095 (67) | 1 | $-2681.33 | -6.3% |
| **+10¢ (15¢ stop)** | 14644 | 14603 | 41 (25) | 0 | $-5772.61 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 12:20 | +10 stop | NEAR | DOWN | 0.71 | 0.91 | 1.76 |
| 10-11 12:20 | +20 | NEAR | DOWN | 0.70 | 0.91 | 1.86 |
| 10-11 12:20 | +15 | NEAR | DOWN | 0.70 | 0.91 | 1.86 |
| 10-11 12:20 | +10 | NEAR | DOWN | 0.70 | 0.91 | 1.86 |
| 10-11 12:20 | +5 | NEAR | DOWN | 0.70 | 0.75 | 0.21 |
| 10-11 12:20 | +10 stop | XRP | DOWN | 0.60 | 0.71 | 0.78 |
| 10-11 12:19 | +10 stop | HYPE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-11 12:19 | +10 | HYPE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-11 12:19 | +5 | HYPE | DOWN | 0.66 | 0.73 | 0.40 |
| 10-11 12:17 | +5 | XRP | UP | 0.67 | open |  |
| 10-11 12:16 | +10 stop | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-11 12:16 | +20 | ZEC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-11 12:16 | +15 | ZEC | DOWN | 0.69 | 0.85 | 1.36 |
| 10-11 12:16 | +10 | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-11 12:16 | +5 | ZEC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-11 12:16 | +10 stop | BNB | DOWN | 0.63 | 0.73 | 0.69 |
| 10-11 12:16 | +20 | BNB | DOWN | 0.63 | 0.86 | 2.04 |
| 10-11 12:16 | +15 | BNB | DOWN | 0.63 | 0.81 | 1.52 |
| 10-11 12:16 | +10 | BNB | DOWN | 0.63 | 0.73 | 0.69 |
| 10-11 12:16 | +5 | BNB | DOWN | 0.63 | 0.69 | 0.28 |
| 10-11 12:16 | +10 stop | HYPE | DOWN | 0.64 | 0.77 | 1.00 |
| 10-11 12:16 | +20 | HYPE | DOWN | 0.64 | 0.88 | 2.15 |
| 10-11 12:16 | +15 | HYPE | DOWN | 0.64 | 0.80 | 1.31 |
| 10-11 12:16 | +10 | HYPE | DOWN | 0.64 | 0.77 | 1.00 |
| 10-11 12:16 | +5 | HYPE | DOWN | 0.64 | 0.69 | 0.18 |
| 10-11 12:16 | +5 | ETH | DOWN | 0.64 | 0.69 | 0.18 |
| 10-11 12:16 | +10 stop | XRP | UP | 0.58 | 0.43 | -1.86 |
| 10-11 12:16 | +20 | XRP | UP | 0.58 | open |  |
| 10-11 12:16 | +15 | XRP | UP | 0.58 | open |  |
| 10-11 12:16 | +10 | XRP | UP | 0.58 | open |  |
| 10-11 12:16 | +5 | XRP | UP | 0.58 | 0.64 | 0.25 |
| 10-11 12:15 | +10 stop | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 10-11 12:15 | +20 | SOL | DOWN | 0.67 | 0.87 | 1.76 |
| 10-11 12:15 | +15 | SOL | DOWN | 0.67 | 0.83 | 1.34 |
| 10-11 12:15 | +10 | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 10-11 12:15 | +5 | SOL | DOWN | 0.67 | 0.72 | 0.19 |
| 10-11 12:15 | +10 stop | ETH | DOWN | 0.61 | 0.71 | 0.68 |
| 10-11 12:15 | +20 | ETH | DOWN | 0.61 | 0.83 | 1.93 |
| 10-11 12:15 | +15 | ETH | DOWN | 0.61 | 0.78 | 1.40 |
| 10-11 12:15 | +10 | ETH | DOWN | 0.61 | 0.71 | 0.68 |
