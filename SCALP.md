# Range-Scalp Bot

*Updated Tue Oct 27 12:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36549 | 31916 | 4633 (43) | 3 | $-10108.57 | -4.4% |
| **+10¢** | 27306 | 21949 | 5357 (65) | 4 | $-8914.23 | -5.2% |
| **+15¢** | 22844 | 17095 | 5749 (89) | 4 | $-7840.41 | -5.5% |
| **+20¢** | 20243 | 14221 | 6022 (113) | 4 | $-6858.56 | -5.4% |
| **+10¢ (15¢ stop)** | 44806 | 44743 | 63 (33) | 0 | $-17089.98 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 12:38 | +10 stop | BNB | UP | 0.68 | 0.87 | 1.66 |
| 10-27 12:36 | +10 stop | DOGE | UP | 0.60 | 0.77 | 1.40 |
| 10-27 12:36 | +5 | DOGE | UP | 0.60 | 0.77 | 1.40 |
| 10-27 12:36 | +10 stop | HYPE | DOWN | 0.49 | 0.33 | -1.98 |
| 10-27 12:36 | +15 | HYPE | DOWN | 0.57 | open |  |
| 10-27 12:36 | +10 | HYPE | DOWN | 0.56 | open |  |
| 10-27 12:36 | +10 stop | BTC | UP | 0.64 | 0.76 | 0.90 |
| 10-27 12:36 | +10 stop | HYPE | DOWN | 0.55 | 0.68 | 0.96 |
| 10-27 12:36 | +10 stop | SOL | UP | 0.60 | 0.77 | 1.40 |
| 10-27 12:36 | +10 stop | DOGE | UP | 0.51 | 0.65 | 1.06 |
| 10-27 12:36 | +5 | DOGE | UP | 0.51 | 0.65 | 1.06 |
| 10-27 12:35 | +5 | HYPE | DOWN | 0.66 | open |  |
| 10-27 12:34 | +10 stop | HYPE | DOWN | 0.53 | 0.64 | 0.71 |
| 10-27 12:34 | +5 | HYPE | DOWN | 0.53 | 0.62 | 0.51 |
| 10-27 12:34 | +5 | BNB | UP | 0.69 | 0.87 | 1.52 |
| 10-27 12:33 | +10 stop | BTC | UP | 0.68 | 0.51 | -2.04 |
| 10-27 12:33 | +20 | BTC | UP | 0.68 | 0.92 | 2.13 |
| 10-27 12:33 | +15 | BTC | UP | 0.68 | 0.92 | 2.13 |
| 10-27 12:33 | +10 | BTC | UP | 0.68 | 0.79 | 0.82 |
| 10-27 12:33 | +5 | BTC | UP | 0.67 | 0.72 | 0.19 |
| 10-27 12:32 | +10 stop | ETH | UP | 0.60 | 0.70 | 0.68 |
| 10-27 12:32 | +10 stop | SOL | UP | 0.62 | 0.72 | 0.68 |
| 10-27 12:32 | +10 stop | DOGE | UP | 0.62 | 0.72 | 0.68 |
| 10-27 12:32 | +5 | DOGE | UP | 0.66 | 0.71 | 0.19 |
| 10-27 12:32 | +5 | BNB | UP | 0.69 | 0.75 | 0.31 |
| 10-27 12:32 | +10 stop | BNB | UP | 0.71 | 0.49 | -2.53 |
| 10-27 12:32 | +20 | BNB | UP | 0.71 | 0.92 | 1.86 |
| 10-27 12:32 | +15 | BNB | UP | 0.71 | 0.87 | 1.37 |
| 10-27 12:32 | +10 | BNB | UP | 0.71 | 0.87 | 1.37 |
| 10-27 12:32 | +10 stop | XRP | UP | 0.71 | 0.82 | 0.84 |
| 10-27 12:32 | +20 | XRP | UP | 0.71 | 0.95 | 2.25 |
| 10-27 12:32 | +15 | XRP | UP | 0.71 | 0.90 | 1.70 |
| 10-27 12:32 | +10 | XRP | UP | 0.70 | 0.80 | 0.73 |
| 10-27 12:32 | +5 | XRP | UP | 0.70 | 0.75 | 0.21 |
| 10-27 12:31 | +5 | DOGE | DOWN | 0.48 | 0.58 | 0.64 |
| 10-27 12:31 | +10 stop | ZEC | UP | 0.66 | 0.81 | 1.23 |
| 10-27 12:31 | +20 | ZEC | UP | 0.66 | 0.86 | 1.75 |
| 10-27 12:31 | +15 | ZEC | UP | 0.67 | 0.86 | 1.65 |
| 10-27 12:31 | +10 | ZEC | UP | 0.67 | 0.81 | 1.13 |
| 10-27 12:31 | +5 | ZEC | UP | 0.67 | 0.73 | 0.30 |
