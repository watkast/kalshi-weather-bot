# Range-Scalp Bot

*Updated Wed Nov 04 00:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46525 | 40516 | 6009 (72) | 3 | $-13351.18 | -4.6% |
| **+10¢** | 34743 | 27777 | 6966 (96) | 3 | $-12198.78 | -5.6% |
| **+15¢** | 29089 | 21596 | 7493 (124) | 3 | $-11145.27 | -6.1% |
| **+20¢** | 25843 | 17992 | 7851 (164) | 3 | $-9833.41 | -6.1% |
| **+10¢ (15¢ stop)** | 56741 | 56648 | 93 (56) | 0 | $-21247.23 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 00:13 | +10 stop | SOL | DOWN | 0.62 | 0.10 | -5.44 |
| 11-04 00:13 | +20 | SOL | DOWN | 0.62 | open |  |
| 11-04 00:13 | +15 | SOL | DOWN | 0.62 | open |  |
| 11-04 00:13 | +10 | SOL | DOWN | 0.62 | open |  |
| 11-04 00:13 | +5 | SOL | DOWN | 0.62 | 0.69 | 0.38 |
| 11-04 00:12 | +5 | XRP | UP | 0.56 | open |  |
| 11-04 00:12 | +10 stop | DOGE | UP | 0.66 | 0.39 | -3.03 |
| 11-04 00:12 | +10 stop | XRP | DOWN | 0.49 | 0.62 | 0.95 |
| 11-04 00:12 | +20 | XRP | DOWN | 0.48 | 0.73 | 2.18 |
| 11-04 00:12 | +15 | XRP | DOWN | 0.49 | 0.73 | 2.08 |
| 11-04 00:12 | +10 | XRP | DOWN | 0.50 | 0.62 | 0.85 |
| 11-04 00:12 | +5 | XRP | DOWN | 0.49 | 0.58 | 0.54 |
| 11-04 00:11 | +10 stop | BTC | UP | 0.47 | 0.68 | 1.76 |
| 11-04 00:11 | +20 | BTC | UP | 0.47 | 0.68 | 1.76 |
| 11-04 00:11 | +15 | BTC | UP | 0.47 | 0.68 | 1.76 |
| 11-04 00:11 | +10 | BTC | UP | 0.46 | 0.68 | 1.86 |
| 11-04 00:11 | +5 | BTC | UP | 0.46 | 0.68 | 1.86 |
| 11-04 00:11 | +10 stop | DOGE | UP | 0.70 | 0.42 | -3.13 |
| 11-04 00:11 | +20 | DOGE | UP | 0.67 | open |  |
| 11-04 00:11 | +15 | DOGE | UP | 0.67 | open |  |
| 11-04 00:11 | +10 | DOGE | UP | 0.67 | open |  |
| 11-04 00:11 | +5 | DOGE | UP | 0.67 | open |  |
| 11-04 00:07 | +10 stop | NEAR | UP | 0.66 | 0.87 | 1.86 |
| 11-04 00:07 | +10 stop | SOL | UP | 0.65 | 0.84 | 1.64 |
| 11-04 00:07 | +10 | SOL | UP | 0.65 | 0.84 | 1.64 |
| 11-04 00:07 | +5 | SOL | UP | 0.65 | 0.70 | 0.19 |
| 11-04 00:07 | +10 stop | DOGE | UP | 0.53 | 0.69 | 1.27 |
| 11-04 00:07 | +10 | DOGE | UP | 0.53 | 0.69 | 1.27 |
| 11-04 00:07 | +5 | DOGE | UP | 0.53 | 0.58 | 0.14 |
| 11-04 00:07 | +10 stop | XRP | UP | 0.58 | 0.71 | 0.93 |
| 11-04 00:07 | +15 | XRP | UP | 0.58 | 0.75 | 1.34 |
| 11-04 00:07 | +10 | XRP | UP | 0.58 | 0.71 | 0.93 |
| 11-04 00:07 | +5 | XRP | UP | 0.58 | 0.71 | 0.97 |
| 11-04 00:06 | +10 stop | BTC | UP | 0.67 | 0.79 | 0.92 |
| 11-04 00:06 | +10 | BTC | UP | 0.67 | 0.79 | 0.92 |
| 11-04 00:06 | +5 | BTC | UP | 0.67 | 0.79 | 0.92 |
| 11-04 00:05 | +10 stop | NEAR | UP | 0.66 | 0.51 | -1.84 |
| 11-04 00:04 | +10 stop | DOGE | UP | 0.70 | 0.82 | 0.94 |
| 11-04 00:04 | +20 | DOGE | UP | 0.70 | 0.90 | 1.80 |
| 11-04 00:04 | +15 | DOGE | UP | 0.70 | 0.86 | 1.36 |
