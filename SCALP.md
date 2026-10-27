# Range-Scalp Bot

*Updated Tue Oct 27 06:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36135 | 31549 | 4586 (43) | 2 | $-10027.72 | -4.4% |
| **+10¢** | 27016 | 21710 | 5306 (65) | 2 | $-8864.26 | -5.2% |
| **+15¢** | 22608 | 16908 | 5700 (89) | 2 | $-7843.50 | -5.5% |
| **+20¢** | 20037 | 14065 | 5972 (112) | 2 | $-6882.49 | -5.5% |
| **+10¢ (15¢ stop)** | 44314 | 44251 | 63 (33) | 0 | $-16871.46 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 06:56 | +10 stop | ZEC | UP | 0.40 | 0.56 | 1.25 |
| 10-27 06:55 | +10 stop | BNB | DOWN | 0.69 | 0.85 | 1.36 |
| 10-27 06:55 | +15 | BNB | DOWN | 0.68 | 0.85 | 1.45 |
| 10-27 06:55 | +10 | BNB | DOWN | 0.68 | 0.85 | 1.45 |
| 10-27 06:55 | +5 | BNB | DOWN | 0.68 | 0.85 | 1.45 |
| 10-27 06:55 | +10 stop | NEAR | UP | 0.58 | 0.37 | -2.45 |
| 10-27 06:55 | +10 | NEAR | UP | 0.58 | open |  |
| 10-27 06:55 | +5 | NEAR | UP | 0.58 | open |  |
| 10-27 06:55 | +10 stop | ZEC | DOWN | 0.43 | 0.61 | 1.45 |
| 10-27 06:55 | +5 | NEAR | DOWN | 0.59 | 0.67 | 0.47 |
| 10-27 06:54 | +10 stop | BNB | DOWN | 0.63 | 0.78 | 1.20 |
| 10-27 06:54 | +20 | BNB | DOWN | 0.63 | 0.85 | 1.94 |
| 10-27 06:54 | +15 | BNB | DOWN | 0.63 | 0.78 | 1.20 |
| 10-27 06:54 | +10 | BNB | DOWN | 0.63 | 0.78 | 1.20 |
| 10-27 06:54 | +5 | BNB | DOWN | 0.63 | 0.78 | 1.20 |
| 10-27 06:54 | +10 stop | NEAR | DOWN | 0.55 | 0.67 | 0.86 |
| 10-27 06:54 | +10 | NEAR | DOWN | 0.55 | 0.67 | 0.86 |
| 10-27 06:54 | +5 | NEAR | DOWN | 0.55 | 0.60 | 0.15 |
| 10-27 06:54 | +10 stop | ZEC | UP | 0.56 | 0.32 | -2.74 |
| 10-27 06:53 | +10 stop | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 10-27 06:53 | +20 | NEAR | DOWN | 0.71 | open |  |
| 10-27 06:53 | +15 | NEAR | DOWN | 0.71 | open |  |
| 10-27 06:53 | +10 | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 10-27 06:53 | +5 | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 10-27 06:52 | +10 stop | ZEC | UP | 0.65 | 0.49 | -1.94 |
| 10-27 06:52 | +10 | ZEC | UP | 0.65 | open |  |
| 10-27 06:52 | +5 | ZEC | UP | 0.65 | open |  |
| 10-27 06:50 | +10 stop | ZEC | DOWN | 0.71 | 0.52 | -2.23 |
| 10-27 06:48 | +5 | BNB | DOWN | 0.60 | 0.67 | 0.37 |
| 10-27 06:48 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-27 06:48 | +15 | NEAR | DOWN | 0.70 | 0.90 | 1.80 |
| 10-27 06:48 | +10 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-27 06:48 | +5 | ZEC | DOWN | 0.65 | 0.73 | 0.50 |
| 10-27 06:47 | +5 | BTC | DOWN | 0.69 | 0.75 | 0.31 |
| 10-27 06:47 | +10 stop | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-27 06:47 | +20 | DOGE | DOWN | 0.66 | 0.87 | 1.86 |
| 10-27 06:47 | +15 | DOGE | DOWN | 0.66 | 0.87 | 1.86 |
| 10-27 06:47 | +10 | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-27 06:47 | +5 | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-27 06:47 | +10 stop | ETH | DOWN | 0.71 | 0.81 | 0.74 |
