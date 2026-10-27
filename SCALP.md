# Range-Scalp Bot

*Updated Tue Oct 27 00:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35694 | 31150 | 4544 (43) | 2 | $-9997.84 | -4.4% |
| **+10¢** | 26683 | 21428 | 5255 (65) | 4 | $-8836.79 | -5.3% |
| **+15¢** | 22340 | 16690 | 5650 (89) | 3 | $-7880.98 | -5.6% |
| **+20¢** | 19801 | 13881 | 5920 (112) | 4 | $-6936.48 | -5.6% |
| **+10¢ (15¢ stop)** | 43762 | 43700 | 62 (33) | 0 | $-16689.87 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 00:42 | +10 stop | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 10-27 00:42 | +20 | BNB | DOWN | 0.70 | 0.93 | 2.12 |
| 10-27 00:42 | +15 | BNB | DOWN | 0.70 | 0.93 | 2.12 |
| 10-27 00:42 | +10 | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 10-27 00:42 | +5 | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 10-27 00:42 | +5 | SOL | DOWN | 0.69 | 0.83 | 1.15 |
| 10-27 00:41 | +10 stop | SOL | DOWN | 0.59 | 0.36 | -2.64 |
| 10-27 00:41 | +5 | SOL | DOWN | 0.58 | 0.66 | 0.46 |
| 10-27 00:40 | +10 stop | DOGE | DOWN | 0.68 | 0.44 | -2.72 |
| 10-27 00:40 | +15 | DOGE | DOWN | 0.68 | 0.86 | 1.57 |
| 10-27 00:40 | +10 | DOGE | DOWN | 0.68 | 0.86 | 1.57 |
| 10-27 00:40 | +5 | DOGE | DOWN | 0.68 | 0.86 | 1.57 |
| 10-27 00:40 | +10 stop | BTC | UP | 0.62 | 0.25 | -4.01 |
| 10-27 00:40 | +20 | BTC | UP | 0.62 | open |  |
| 10-27 00:40 | +15 | BTC | UP | 0.62 | open |  |
| 10-27 00:40 | +10 | BTC | UP | 0.62 | open |  |
| 10-27 00:40 | +5 | BTC | UP | 0.62 | open |  |
| 10-27 00:40 | +5 | SOL | UP | 0.50 | 0.58 | 0.44 |
| 10-27 00:40 | +10 stop | DOGE | UP | 0.41 | 0.59 | 1.46 |
| 10-27 00:40 | +15 | DOGE | UP | 0.41 | 0.59 | 1.46 |
| 10-27 00:40 | +10 | DOGE | UP | 0.41 | 0.59 | 1.46 |
| 10-27 00:40 | +5 | DOGE | UP | 0.42 | 0.59 | 1.35 |
| 10-27 00:40 | +10 stop | SOL | UP | 0.48 | 0.58 | 0.64 |
| 10-27 00:39 | +10 stop | ZEC | UP | 0.64 | 0.47 | -2.05 |
| 10-27 00:39 | +10 stop | SOL | UP | 0.57 | 0.67 | 0.66 |
| 10-27 00:39 | +10 stop | NEAR | UP | 0.60 | 0.30 | -3.32 |
| 10-27 00:39 | +5 | NEAR | UP | 0.60 | open |  |
| 10-27 00:38 | +5 | XRP | DOWN | 0.63 | 0.72 | 0.58 |
| 10-27 00:38 | +10 stop | ZEC | UP | 0.61 | 0.76 | 1.17 |
| 10-27 00:38 | +10 stop | SOL | UP | 0.54 | 0.67 | 0.96 |
| 10-27 00:38 | +10 stop | XRP | DOWN | 0.61 | 0.72 | 0.78 |
| 10-27 00:38 | +20 | XRP | DOWN | 0.61 | 0.85 | 2.14 |
| 10-27 00:38 | +15 | XRP | DOWN | 0.61 | 0.85 | 2.14 |
| 10-27 00:38 | +10 | XRP | DOWN | 0.61 | 0.72 | 0.78 |
| 10-27 00:38 | +5 | XRP | DOWN | 0.61 | 0.66 | 0.17 |
| 10-27 00:38 | +10 stop | BNB | UP | 0.67 | 0.48 | -2.24 |
| 10-27 00:37 | +10 stop | BTC | UP | 0.70 | 0.82 | 0.94 |
| 10-27 00:37 | +10 | BTC | UP | 0.70 | 0.82 | 0.94 |
| 10-27 00:37 | +5 | BTC | UP | 0.69 | 0.77 | 0.52 |
| 10-27 00:37 | +10 stop | NEAR | DOWN | 0.59 | 0.38 | -2.44 |
