# Range-Scalp Bot

*Updated Tue Nov 03 04:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45579 | 39687 | 5892 (69) | 1 | $-13148.43 | -4.6% |
| **+10¢** | 34021 | 27192 | 6829 (91) | 1 | $-12051.35 | -5.6% |
| **+15¢** | 28469 | 21122 | 7347 (119) | 1 | $-11050.42 | -6.2% |
| **+20¢** | 25286 | 17588 | 7698 (154) | 1 | $-9829.30 | -6.2% |
| **+10¢ (15¢ stop)** | 55613 | 55524 | 89 (53) | 0 | $-20957.04 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 04:40 | +10 stop | HYPE | DOWN | 0.62 | 0.73 | 0.75 |
| 11-03 04:40 | +5 | HYPE | DOWN | 0.62 | 0.73 | 0.75 |
| 11-03 04:37 | +10 stop | SOL | DOWN | 0.66 | 0.84 | 1.54 |
| 11-03 04:37 | +10 stop | HYPE | DOWN | 0.51 | 0.65 | 1.06 |
| 11-03 04:32 | +10 stop | SOL | DOWN | 0.70 | 0.53 | -2.07 |
| 11-03 04:31 | +10 stop | ETH | DOWN | 0.63 | 0.75 | 0.89 |
| 11-03 04:31 | +20 | ETH | DOWN | 0.63 | 0.91 | 2.48 |
| 11-03 04:31 | +15 | ETH | DOWN | 0.63 | 0.80 | 1.38 |
| 11-03 04:31 | +10 | ETH | DOWN | 0.63 | 0.75 | 0.86 |
| 11-03 04:31 | +5 | ETH | DOWN | 0.63 | 0.72 | 0.55 |
| 11-03 04:31 | +10 stop | XRP | DOWN | 0.68 | 0.80 | 0.92 |
| 11-03 04:31 | +20 | XRP | DOWN | 0.68 | 0.89 | 1.87 |
| 11-03 04:31 | +15 | XRP | DOWN | 0.68 | 0.83 | 1.24 |
| 11-03 04:31 | +10 | XRP | DOWN | 0.68 | 0.80 | 0.92 |
| 11-03 04:31 | +5 | XRP | DOWN | 0.67 | 0.75 | 0.50 |
| 11-03 04:31 | +10 stop | DOGE | DOWN | 0.68 | 0.81 | 1.03 |
| 11-03 04:31 | +20 | DOGE | DOWN | 0.68 | 0.92 | 2.13 |
| 11-03 04:31 | +15 | DOGE | DOWN | 0.68 | 0.92 | 2.13 |
| 11-03 04:31 | +10 | DOGE | DOWN | 0.68 | 0.81 | 1.03 |
| 11-03 04:31 | +5 | DOGE | DOWN | 0.68 | 0.77 | 0.61 |
| 11-03 04:31 | +10 stop | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-03 04:31 | +20 | ZEC | DOWN | 0.71 | 0.91 | 1.79 |
| 11-03 04:31 | +15 | ZEC | DOWN | 0.71 | 0.91 | 1.79 |
| 11-03 04:31 | +10 | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-03 04:31 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.22 |
| 11-03 04:31 | +10 stop | SOL | UP | 0.51 | 0.35 | -1.94 |
| 11-03 04:31 | +20 | SOL | UP | 0.51 | open |  |
| 11-03 04:31 | +15 | SOL | UP | 0.51 | open |  |
| 11-03 04:31 | +10 | SOL | UP | 0.51 | open |  |
| 11-03 04:31 | +5 | SOL | UP | 0.51 | open |  |
| 11-03 04:31 | +10 stop | HYPE | DOWN | 0.70 | 0.51 | -2.23 |
| 11-03 04:31 | +20 | HYPE | DOWN | 0.70 | 0.93 | 2.09 |
| 11-03 04:31 | +15 | HYPE | DOWN | 0.70 | 0.86 | 1.36 |
| 11-03 04:31 | +10 | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-03 04:31 | +5 | HYPE | DOWN | 0.70 | 0.75 | 0.21 |
| 11-03 04:31 | +10 stop | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 11-03 04:31 | +20 | BNB | DOWN | 0.68 | 0.89 | 1.87 |
| 11-03 04:31 | +15 | BNB | DOWN | 0.68 | 0.84 | 1.34 |
| 11-03 04:31 | +10 | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 11-03 04:31 | +5 | BNB | DOWN | 0.68 | 0.75 | 0.40 |
