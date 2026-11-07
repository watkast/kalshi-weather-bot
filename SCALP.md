# Range-Scalp Bot

*Updated Sat Nov 07 09:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50810 | 44297 | 6513 (76) | 0 | $-14223.99 | -4.4% |
| **+10¢** | 37934 | 30345 | 7589 (102) | 0 | $-13178.75 | -5.5% |
| **+15¢** | 31755 | 23579 | 8176 (131) | 1 | $-12084.71 | -6.1% |
| **+20¢** | 28235 | 19664 | 8571 (173) | 1 | $-10675.35 | -6.0% |
| **+10¢ (15¢ stop)** | 61874 | 61775 | 99 (58) | 0 | $-22856.31 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 09:41 | +10 stop | BTC | DOWN | 0.69 | 0.97 | 2.60 |
| 11-07 09:41 | +15 | BTC | DOWN | 0.69 | 0.97 | 2.60 |
| 11-07 09:41 | +10 | BTC | DOWN | 0.69 | 0.97 | 2.60 |
| 11-07 09:41 | +5 | BTC | DOWN | 0.69 | 0.75 | 0.31 |
| 11-07 09:31 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 11-07 09:31 | +10 | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 11-07 09:31 | +5 | XRP | DOWN | 0.70 | 0.78 | 0.52 |
| 11-07 09:31 | +10 stop | XRP | UP | 0.46 | 0.60 | 1.05 |
| 11-07 09:31 | +20 | XRP | UP | 0.46 | open |  |
| 11-07 09:31 | +15 | XRP | UP | 0.46 | open |  |
| 11-07 09:31 | +10 | XRP | UP | 0.46 | 0.60 | 1.05 |
| 11-07 09:31 | +5 | XRP | UP | 0.46 | 0.60 | 1.05 |
| 11-07 09:31 | +10 stop | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 11-07 09:31 | +20 | NEAR | DOWN | 0.71 | 0.93 | 1.98 |
| 11-07 09:31 | +15 | NEAR | DOWN | 0.71 | 0.86 | 1.26 |
| 11-07 09:31 | +10 | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 11-07 09:31 | +5 | NEAR | DOWN | 0.71 | 0.77 | 0.32 |
| 11-07 09:31 | +10 stop | BTC | DOWN | 0.69 | 0.82 | 1.04 |
| 11-07 09:31 | +20 | BTC | DOWN | 0.69 | 0.97 | 2.60 |
| 11-07 09:31 | +15 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 11-07 09:31 | +10 | BTC | DOWN | 0.69 | 0.82 | 1.04 |
| 11-07 09:31 | +5 | BTC | DOWN | 0.69 | 0.78 | 0.62 |
| 11-07 09:21 | +10 stop | ZEC | DOWN | 0.66 | 0.79 | 1.02 |
| 11-07 09:21 | +10 | ZEC | DOWN | 0.66 | 0.79 | 1.02 |
| 11-07 09:21 | +5 | ZEC | DOWN | 0.66 | 0.79 | 1.02 |
| 11-07 09:18 | +10 stop | ZEC | DOWN | 0.61 | 0.72 | 0.78 |
| 11-07 09:18 | +10 | ZEC | DOWN | 0.61 | 0.72 | 0.78 |
| 11-07 09:18 | +5 | ZEC | DOWN | 0.61 | 0.68 | 0.37 |
| 11-07 09:16 | +10 stop | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-07 09:16 | +20 | ZEC | DOWN | 0.69 | 0.91 | 2.00 |
| 11-07 09:16 | +15 | ZEC | DOWN | 0.69 | 0.85 | 1.36 |
| 11-07 09:16 | +10 | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-07 09:16 | +5 | ZEC | DOWN | 0.69 | 0.74 | 0.21 |
| 11-07 09:16 | +10 stop | NEAR | DOWN | 0.65 | 0.82 | 1.43 |
| 11-07 09:16 | +20 | NEAR | DOWN | 0.65 | 0.85 | 1.75 |
| 11-07 09:16 | +15 | NEAR | DOWN | 0.65 | 0.82 | 1.43 |
| 11-07 09:16 | +10 | NEAR | DOWN | 0.65 | 0.82 | 1.43 |
| 11-07 09:16 | +5 | NEAR | DOWN | 0.65 | 0.71 | 0.29 |
| 11-07 09:16 | +10 stop | DOGE | DOWN | 0.64 | 0.81 | 1.42 |
| 11-07 09:16 | +20 | DOGE | DOWN | 0.64 | 0.88 | 2.15 |
