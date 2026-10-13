# Range-Scalp Bot

*Updated Tue Oct 13 21:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15037 | 13006 | 2031 (27) | 1 | $-4877.03 | -5.1% |
| **+10¢** | 11369 | 9013 | 2356 (39) | 5 | $-4559.59 | -6.4% |
| **+15¢** | 9556 | 7035 | 2521 (58) | 5 | $-4048.66 | -6.7% |
| **+20¢** | 8496 | 5868 | 2628 (74) | 6 | $-3507.83 | -6.6% |
| **+10¢ (15¢ stop)** | 18440 | 18390 | 50 (29) | 3 | $-7145.87 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 21:57 | +10 stop | XRP | UP | 0.60 | open |  |
| 10-13 21:57 | +15 | XRP | UP | 0.60 | open |  |
| 10-13 21:57 | +10 | XRP | UP | 0.60 | open |  |
| 10-13 21:57 | +5 | XRP | UP | 0.60 | open |  |
| 10-13 21:57 | +10 stop | NEAR | UP | 0.63 | open |  |
| 10-13 21:57 | +10 | NEAR | UP | 0.63 | open |  |
| 10-13 21:57 | +5 | NEAR | UP | 0.63 | 0.71 | 0.48 |
| 10-13 21:56 | +10 stop | ETH | UP | 0.71 | 0.81 | 0.74 |
| 10-13 21:56 | +20 | ETH | UP | 0.71 | open |  |
| 10-13 21:56 | +15 | ETH | UP | 0.71 | 0.89 | 1.58 |
| 10-13 21:56 | +10 | ETH | UP | 0.71 | 0.81 | 0.74 |
| 10-13 21:56 | +5 | ETH | UP | 0.71 | 0.79 | 0.53 |
| 10-13 21:56 | +10 stop | NEAR | DOWN | 0.52 | 0.25 | -3.02 |
| 10-13 21:55 | +5 | DOGE | UP | 0.65 | 0.83 | 1.54 |
| 10-13 21:55 | +10 stop | BNB | UP | 0.68 | open |  |
| 10-13 21:55 | +20 | BNB | UP | 0.68 | open |  |
| 10-13 21:55 | +15 | BNB | UP | 0.68 | open |  |
| 10-13 21:55 | +10 | BNB | UP | 0.68 | open |  |
| 10-13 21:55 | +5 | BNB | UP | 0.68 | 0.73 | 0.20 |
| 10-13 21:55 | +10 stop | ZEC | DOWN | 0.63 | 0.83 | 1.71 |
| 10-13 21:55 | +5 | XRP | UP | 0.70 | 0.76 | 0.32 |
| 10-13 21:54 | +10 stop | HYPE | UP | 0.64 | 0.74 | 0.69 |
| 10-13 21:54 | +15 | HYPE | UP | 0.64 | 0.87 | 2.05 |
| 10-13 21:54 | +10 | HYPE | UP | 0.64 | 0.74 | 0.69 |
| 10-13 21:54 | +5 | HYPE | UP | 0.64 | 0.69 | 0.18 |
| 10-13 21:54 | +10 stop | DOGE | UP | 0.65 | 0.83 | 1.50 |
| 10-13 21:54 | +15 | DOGE | UP | 0.65 | 0.83 | 1.50 |
| 10-13 21:54 | +10 | DOGE | UP | 0.65 | 0.83 | 1.50 |
| 10-13 21:54 | +5 | DOGE | UP | 0.65 | 0.75 | 0.66 |
| 10-13 21:54 | +10 stop | XRP | UP | 0.57 | 0.69 | 0.90 |
| 10-13 21:54 | +20 | XRP | UP | 0.57 | open |  |
| 10-13 21:54 | +15 | XRP | UP | 0.57 | 0.74 | 1.41 |
| 10-13 21:54 | +10 | XRP | UP | 0.56 | 0.69 | 0.97 |
| 10-13 21:54 | +5 | XRP | UP | 0.56 | 0.64 | 0.45 |
| 10-13 21:54 | +10 stop | ZEC | UP | 0.54 | 0.38 | -1.95 |
| 10-13 21:53 | +10 stop | ETH | UP | 0.69 | 0.82 | 1.04 |
| 10-13 21:53 | +5 | ETH | UP | 0.67 | 0.82 | 1.23 |
| 10-13 21:52 | +10 stop | DOGE | UP | 0.69 | 0.85 | 1.36 |
| 10-13 21:52 | +20 | DOGE | UP | 0.69 | 0.90 | 1.90 |
| 10-13 21:52 | +15 | DOGE | UP | 0.69 | 0.85 | 1.39 |
