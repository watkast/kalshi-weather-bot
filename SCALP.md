# Range-Scalp Bot

*Updated Sat Nov 07 05:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50551 | 44063 | 6488 (76) | 4 | $-14228.30 | -4.5% |
| **+10¢** | 37725 | 30169 | 7556 (102) | 4 | $-13173.83 | -5.6% |
| **+15¢** | 31585 | 23445 | 8140 (131) | 5 | $-12077.78 | -6.1% |
| **+20¢** | 28084 | 19551 | 8533 (173) | 6 | $-10671.98 | -6.1% |
| **+10¢ (15¢ stop)** | 61558 | 61459 | 99 (58) | 2 | $-22780.86 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 05:52 | +10 stop | XRP | UP | 0.49 | open |  |
| 11-07 05:52 | +5 | ZEC | UP | 0.69 | open |  |
| 11-07 05:51 | +10 stop | ZEC | UP | 0.60 | open |  |
| 11-07 05:50 | +10 stop | ZEC | UP | 0.53 | 0.63 | 0.65 |
| 11-07 05:49 | +10 stop | XRP | UP | 0.66 | 0.50 | -1.94 |
| 11-07 05:49 | +5 | ZEC | UP | 0.61 | 0.66 | 0.17 |
| 11-07 05:48 | +10 stop | NEAR | UP | 0.64 | 0.75 | 0.79 |
| 11-07 05:48 | +5 | ETH | UP | 0.71 | 0.78 | 0.42 |
| 11-07 05:47 | +10 stop | ZEC | UP | 0.63 | 0.47 | -1.95 |
| 11-07 05:47 | +20 | ZEC | UP | 0.63 | open |  |
| 11-07 05:47 | +15 | ZEC | UP | 0.63 | open |  |
| 11-07 05:47 | +10 | ZEC | UP | 0.63 | open |  |
| 11-07 05:47 | +5 | ZEC | UP | 0.63 | 0.71 | 0.48 |
| 11-07 05:47 | +10 stop | BNB | DOWN | 0.56 | 0.39 | -2.05 |
| 11-07 05:47 | +20 | BNB | DOWN | 0.56 | open |  |
| 11-07 05:47 | +15 | BNB | DOWN | 0.56 | open |  |
| 11-07 05:47 | +10 | BNB | DOWN | 0.56 | open |  |
| 11-07 05:47 | +5 | BNB | DOWN | 0.56 | open |  |
| 11-07 05:47 | +5 | DOGE | UP | 0.65 | 0.73 | 0.50 |
| 11-07 05:47 | +5 | ETH | UP | 0.61 | 0.72 | 0.78 |
| 11-07 05:47 | +10 stop | NEAR | DOWN | 0.58 | 0.43 | -1.86 |
| 11-07 05:47 | +20 | NEAR | DOWN | 0.58 | open |  |
| 11-07 05:47 | +15 | NEAR | DOWN | 0.58 | open |  |
| 11-07 05:47 | +10 | NEAR | DOWN | 0.58 | open |  |
| 11-07 05:47 | +5 | NEAR | DOWN | 0.58 | open |  |
| 11-07 05:46 | +10 stop | DOGE | UP | 0.56 | 0.73 | 1.38 |
| 11-07 05:46 | +20 | DOGE | UP | 0.56 | 0.81 | 2.21 |
| 11-07 05:46 | +15 | DOGE | UP | 0.56 | 0.73 | 1.38 |
| 11-07 05:46 | +10 | DOGE | UP | 0.56 | 0.73 | 1.38 |
| 11-07 05:46 | +5 | DOGE | UP | 0.56 | 0.62 | 0.25 |
| 11-07 05:46 | +10 stop | XRP | DOWN | 0.51 | 0.35 | -1.94 |
| 11-07 05:46 | +20 | XRP | DOWN | 0.51 | open |  |
| 11-07 05:46 | +15 | XRP | DOWN | 0.51 | open |  |
| 11-07 05:46 | +10 | XRP | DOWN | 0.51 | open |  |
| 11-07 05:46 | +5 | XRP | DOWN | 0.51 | open |  |
| 11-07 05:46 | +10 stop | SOL | UP | 0.67 | 0.78 | 0.81 |
| 11-07 05:46 | +20 | SOL | UP | 0.67 | 0.87 | 1.76 |
| 11-07 05:46 | +15 | SOL | UP | 0.67 | 0.83 | 1.34 |
| 11-07 05:46 | +10 | SOL | UP | 0.67 | 0.78 | 0.81 |
| 11-07 05:46 | +5 | SOL | UP | 0.67 | 0.72 | 0.19 |
