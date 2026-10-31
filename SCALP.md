# Range-Scalp Bot

*Updated Sat Oct 31 17:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42500 | 37070 | 5430 (59) | 3 | $-11961.32 | -4.5% |
| **+10¢** | 31688 | 25404 | 6284 (81) | 3 | $-10737.49 | -5.4% |
| **+15¢** | 26505 | 19730 | 6775 (109) | 3 | $-9819.41 | -5.9% |
| **+20¢** | 23538 | 16435 | 7103 (141) | 3 | $-8705.87 | -5.9% |
| **+10¢ (15¢ stop)** | 51840 | 51761 | 79 (44) | 0 | $-19625.48 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 16:56 | +10 stop | XRP | UP | 0.54 | 0.25 | -3.22 |
| 10-31 16:56 | +10 stop | ZEC | UP | 0.59 | 0.41 | -2.14 |
| 10-31 16:56 | +15 | DOGE | DOWN | 0.64 | 0.86 | 1.94 |
| 10-31 16:55 | +10 stop | DOGE | DOWN | 0.64 | 0.86 | 1.94 |
| 10-31 16:55 | +10 | DOGE | DOWN | 0.64 | 0.86 | 1.94 |
| 10-31 16:55 | +5 | DOGE | DOWN | 0.64 | 0.86 | 1.94 |
| 10-31 16:55 | +10 stop | DOGE | UP | 0.36 | 0.61 | 2.16 |
| 10-31 16:55 | +10 | DOGE | UP | 0.36 | 0.61 | 2.16 |
| 10-31 16:55 | +5 | DOGE | UP | 0.36 | 0.61 | 2.16 |
| 10-31 16:55 | +10 stop | ETH | UP | 0.57 | 0.31 | -2.93 |
| 10-31 16:54 | +5 | ZEC | UP | 0.69 | open |  |
| 10-31 16:54 | +10 stop | ZEC | UP | 0.69 | 0.51 | -2.13 |
| 10-31 16:54 | +15 | ZEC | UP | 0.69 | open |  |
| 10-31 16:54 | +10 | ZEC | UP | 0.69 | open |  |
| 10-31 16:54 | +10 stop | DOGE | DOWN | 0.48 | 0.61 | 0.95 |
| 10-31 16:54 | +15 | DOGE | DOWN | 0.48 | 0.67 | 1.56 |
| 10-31 16:54 | +10 | DOGE | DOWN | 0.48 | 0.61 | 0.95 |
| 10-31 16:54 | +5 | DOGE | DOWN | 0.47 | 0.61 | 1.00 |
| 10-31 16:54 | +10 stop | BNB | UP | 0.69 | 0.85 | 1.34 |
| 10-31 16:54 | +10 stop | SOL | DOWN | 0.63 | 0.78 | 1.20 |
| 10-31 16:53 | +5 | DOGE | DOWN | 0.68 | 0.73 | 0.20 |
| 10-31 16:52 | +10 stop | SOL | DOWN | 0.59 | 0.73 | 1.09 |
| 10-31 16:52 | +10 stop | ETH | DOWN | 0.66 | 0.36 | -3.33 |
| 10-31 16:51 | +10 stop | XRP | UP | 0.70 | 0.41 | -3.26 |
| 10-31 16:50 | +10 stop | ZEC | DOWN | 0.61 | 0.74 | 0.99 |
| 10-31 16:50 | +10 | ZEC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-31 16:50 | +5 | ZEC | DOWN | 0.60 | 0.65 | 0.17 |
| 10-31 16:49 | +10 stop | SOL | DOWN | 0.65 | 0.50 | -1.84 |
| 10-31 16:49 | +10 stop | NEAR | UP | 0.57 | 0.82 | 2.21 |
| 10-31 16:48 | +10 stop | DOGE | DOWN | 0.58 | 0.72 | 1.07 |
| 10-31 16:48 | +20 | DOGE | DOWN | 0.58 | 0.86 | 2.53 |
| 10-31 16:48 | +15 | DOGE | DOWN | 0.58 | 0.73 | 1.18 |
| 10-31 16:48 | +10 | DOGE | DOWN | 0.58 | 0.72 | 1.07 |
| 10-31 16:48 | +5 | DOGE | DOWN | 0.58 | 0.65 | 0.36 |
| 10-31 16:47 | +10 stop | XRP | DOWN | 0.61 | 0.33 | -3.13 |
| 10-31 16:47 | +20 | XRP | DOWN | 0.61 | 0.88 | 2.45 |
| 10-31 16:47 | +15 | XRP | DOWN | 0.61 | 0.88 | 2.45 |
| 10-31 16:47 | +10 | XRP | DOWN | 0.61 | 0.73 | 0.89 |
| 10-31 16:47 | +5 | XRP | DOWN | 0.61 | 0.73 | 0.89 |
| 10-31 16:47 | +10 stop | NEAR | DOWN | 0.55 | 0.37 | -2.15 |
