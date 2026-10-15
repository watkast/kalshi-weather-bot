# Range-Scalp Bot

*Updated Thu Oct 15 13:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17601 | 15292 | 2309 (28) | 4 | $-5281.21 | -4.8% |
| **+10¢** | 13297 | 10624 | 2673 (40) | 6 | $-4762.65 | -5.7% |
| **+15¢** | 11154 | 8280 | 2874 (59) | 6 | $-4243.45 | -6.1% |
| **+20¢** | 9911 | 6902 | 3009 (77) | 6 | $-3682.89 | -5.9% |
| **+10¢ (15¢ stop)** | 21655 | 21605 | 50 (29) | 0 | $-8349.23 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 13:39 | +10 stop | DOGE | UP | 0.70 | 0.87 | 1.47 |
| 10-15 13:39 | +10 stop | XRP | UP | 0.71 | 0.84 | 1.05 |
| 10-15 13:39 | +20 | XRP | UP | 0.70 | 0.91 | 1.87 |
| 10-15 13:39 | +15 | XRP | UP | 0.69 | 0.84 | 1.25 |
| 10-15 13:39 | +10 | XRP | UP | 0.69 | 0.84 | 1.25 |
| 10-15 13:39 | +5 | XRP | UP | 0.69 | 0.76 | 0.42 |
| 10-15 13:38 | +5 | SOL | UP | 0.48 | 0.56 | 0.44 |
| 10-15 13:38 | +10 stop | DOGE | DOWN | 0.69 | 0.54 | -1.83 |
| 10-15 13:38 | +5 | DOGE | DOWN | 0.69 | open |  |
| 10-15 13:38 | +5 | SOL | UP | 0.58 | 0.63 | 0.15 |
| 10-15 13:38 | +10 stop | SOL | UP | 0.59 | 0.69 | 0.68 |
| 10-15 13:37 | +20 | SOL | UP | 0.64 | 0.86 | 1.94 |
| 10-15 13:37 | +15 | SOL | UP | 0.64 | 0.86 | 1.94 |
| 10-15 13:37 | +10 | SOL | UP | 0.64 | 0.86 | 1.94 |
| 10-15 13:37 | +10 stop | ETH | UP | 0.68 | 0.49 | -2.24 |
| 10-15 13:37 | +5 | ETH | UP | 0.68 | 0.73 | 0.20 |
| 10-15 13:37 | +5 | SOL | UP | 0.55 | 0.69 | 1.07 |
| 10-15 13:37 | +10 stop | BNB | DOWN | 0.54 | 0.31 | -2.63 |
| 10-15 13:37 | +10 | BNB | DOWN | 0.54 | open |  |
| 10-15 13:37 | +10 stop | SOL | UP | 0.58 | 0.69 | 0.77 |
| 10-15 13:37 | +10 stop | SOL | DOWN | 0.51 | 0.69 | 1.47 |
| 10-15 13:36 | +10 stop | BTC | DOWN | 0.60 | 0.42 | -2.15 |
| 10-15 13:36 | +10 stop | NEAR | DOWN | 0.60 | 0.42 | -2.15 |
| 10-15 13:36 | +10 stop | DOGE | DOWN | 0.61 | 0.39 | -2.54 |
| 10-15 13:36 | +10 stop | HYPE | DOWN | 0.55 | 0.70 | 1.17 |
| 10-15 13:35 | +5 | SOL | UP | 0.44 | 0.56 | 0.84 |
| 10-15 13:35 | +10 stop | ZEC | UP | 0.57 | 0.69 | 0.87 |
| 10-15 13:34 | +10 stop | XRP | UP | 0.48 | 0.32 | -1.94 |
| 10-15 13:34 | +10 stop | BNB | UP | 0.56 | 0.37 | -2.25 |
| 10-15 13:34 | +5 | BNB | UP | 0.56 | 0.68 | 0.86 |
| 10-15 13:34 | +10 stop | SOL | UP | 0.47 | 0.31 | -1.93 |
| 10-15 13:34 | +20 | SOL | UP | 0.47 | 0.69 | 1.87 |
| 10-15 13:34 | +15 | SOL | UP | 0.47 | 0.69 | 1.87 |
| 10-15 13:34 | +10 | SOL | UP | 0.47 | 0.69 | 1.87 |
| 10-15 13:34 | +5 | SOL | UP | 0.47 | 0.56 | 0.54 |
| 10-15 13:34 | +10 stop | DOGE | UP | 0.69 | 0.50 | -2.23 |
| 10-15 13:34 | +10 stop | XRP | DOWN | 0.44 | 0.57 | 0.94 |
| 10-15 13:34 | +10 stop | NEAR | UP | 0.69 | 0.51 | -2.13 |
| 10-15 13:34 | +15 | NEAR | UP | 0.69 | 0.92 | 2.09 |
| 10-15 13:34 | +10 | NEAR | UP | 0.69 | 0.79 | 0.73 |
