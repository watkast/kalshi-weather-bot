# Range-Scalp Bot

*Updated Thu Oct 22 13:49 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28801 | 25096 | 3705 (39) | 0 | $-8290.74 | -4.6% |
| **+10¢** | 21620 | 17334 | 4286 (55) | 1 | $-7371.27 | -5.4% |
| **+15¢** | 18093 | 13484 | 4609 (78) | 2 | $-6592.35 | -5.8% |
| **+20¢** | 16008 | 11175 | 4833 (100) | 3 | $-5937.48 | -5.9% |
| **+10¢ (15¢ stop)** | 35333 | 35274 | 59 (32) | 1 | $-13239.06 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 13:48 | +10 stop | ZEC | DOWN | 0.71 | open |  |
| 10-22 13:48 | +10 | ZEC | DOWN | 0.71 | open |  |
| 10-22 13:46 | +10 stop | XRP | DOWN | 0.67 | 0.77 | 0.71 |
| 10-22 13:46 | +20 | XRP | DOWN | 0.67 | open |  |
| 10-22 13:46 | +15 | XRP | DOWN | 0.67 | 0.82 | 1.23 |
| 10-22 13:46 | +10 | XRP | DOWN | 0.67 | 0.77 | 0.71 |
| 10-22 13:46 | +5 | XRP | DOWN | 0.67 | 0.75 | 0.50 |
| 10-22 13:46 | +10 stop | DOGE | DOWN | 0.69 | 0.79 | 0.74 |
| 10-22 13:46 | +20 | DOGE | DOWN | 0.69 | open |  |
| 10-22 13:46 | +15 | DOGE | DOWN | 0.69 | open |  |
| 10-22 13:46 | +10 | DOGE | DOWN | 0.69 | 0.79 | 0.74 |
| 10-22 13:46 | +5 | DOGE | DOWN | 0.69 | 0.77 | 0.53 |
| 10-22 13:45 | +10 stop | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-22 13:45 | +20 | ZEC | DOWN | 0.70 | open |  |
| 10-22 13:45 | +15 | ZEC | DOWN | 0.70 | open |  |
| 10-22 13:45 | +10 | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-22 13:45 | +5 | ZEC | DOWN | 0.70 | 0.78 | 0.52 |
| 10-22 13:42 | +10 stop | NEAR | DOWN | 0.50 | 0.62 | 0.85 |
| 10-22 13:42 | +15 | NEAR | DOWN | 0.52 | yes | -5.38 |
| 10-22 13:42 | +10 | NEAR | DOWN | 0.52 | 0.62 | 0.65 |
| 10-22 13:42 | +5 | NEAR | DOWN | 0.51 | 0.62 | 0.75 |
| 10-22 13:41 | +10 stop | NEAR | DOWN | 0.36 | 0.53 | 1.35 |
| 10-22 13:41 | +10 stop | DOGE | UP | 0.71 | 0.41 | -3.32 |
| 10-22 13:41 | +10 stop | XRP | DOWN | 0.43 | 0.54 | 0.74 |
| 10-22 13:40 | +10 stop | HYPE | UP | 0.64 | 0.88 | 2.15 |
| 10-22 13:40 | +10 stop | XRP | UP | 0.52 | 0.63 | 0.75 |
| 10-22 13:40 | +10 stop | DOGE | UP | 0.57 | 0.38 | -2.25 |
| 10-22 13:39 | +10 stop | BNB | DOWN | 0.63 | 0.79 | 1.28 |
| 10-22 13:39 | +10 | BNB | DOWN | 0.63 | 0.79 | 1.31 |
| 10-22 13:39 | +5 | BNB | DOWN | 0.63 | 0.68 | 0.17 |
| 10-22 13:39 | +10 stop | DOGE | DOWN | 0.48 | 0.59 | 0.75 |
| 10-22 13:39 | +10 stop | ETH | DOWN | 0.62 | 0.36 | -2.94 |
| 10-22 13:39 | +10 stop | SOL | UP | 0.69 | 0.80 | 0.83 |
| 10-22 13:38 | +10 stop | BNB | DOWN | 0.58 | 0.68 | 0.66 |
| 10-22 13:38 | +10 stop | ZEC | UP | 0.66 | 0.82 | 1.33 |
| 10-22 13:38 | +20 | ZEC | UP | 0.69 | 0.92 | 2.05 |
| 10-22 13:38 | +15 | ZEC | UP | 0.69 | 0.85 | 1.36 |
| 10-22 13:38 | +10 | ZEC | UP | 0.69 | 0.82 | 1.04 |
| 10-22 13:38 | +5 | ZEC | UP | 0.69 | 0.82 | 1.04 |
| 10-22 13:38 | +10 stop | DOGE | UP | 0.66 | 0.45 | -2.44 |
