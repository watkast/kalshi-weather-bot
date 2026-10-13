# Range-Scalp Bot

*Updated Tue Oct 13 20:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14916 | 12899 | 2017 (27) | 2 | $-4851.90 | -5.2% |
| **+10¢** | 11291 | 8953 | 2338 (39) | 2 | $-4515.51 | -6.4% |
| **+15¢** | 9488 | 6987 | 2501 (58) | 0 | $-4005.07 | -6.7% |
| **+20¢** | 8443 | 5835 | 2608 (74) | 0 | $-3460.60 | -6.5% |
| **+10¢ (15¢ stop)** | 18313 | 18263 | 50 (29) | 0 | $-7101.75 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 20:24 | +5 | NEAR | DOWN | 0.55 | open |  |
| 10-13 20:23 | +10 stop | NEAR | DOWN | 0.47 | 0.28 | -2.23 |
| 10-13 20:23 | +10 | NEAR | DOWN | 0.47 | open |  |
| 10-13 20:23 | +5 | NEAR | DOWN | 0.47 | 0.55 | 0.44 |
| 10-13 20:22 | +10 stop | NEAR | UP | 0.52 | 0.62 | 0.66 |
| 10-13 20:22 | +15 | NEAR | UP | 0.52 | 0.69 | 1.38 |
| 10-13 20:22 | +10 | NEAR | UP | 0.52 | 0.62 | 0.66 |
| 10-13 20:22 | +5 | NEAR | UP | 0.52 | 0.62 | 0.66 |
| 10-13 20:20 | +5 | BNB | DOWN | 0.63 | 0.71 | 0.48 |
| 10-13 20:20 | +10 stop | ZEC | DOWN | 0.58 | 0.74 | 1.25 |
| 10-13 20:19 | +10 stop | NEAR | UP | 0.59 | 0.75 | 1.29 |
| 10-13 20:19 | +20 | NEAR | UP | 0.59 | 0.80 | 1.81 |
| 10-13 20:19 | +15 | NEAR | UP | 0.59 | 0.75 | 1.29 |
| 10-13 20:19 | +10 | NEAR | UP | 0.59 | 0.75 | 1.29 |
| 10-13 20:19 | +5 | NEAR | UP | 0.59 | 0.65 | 0.27 |
| 10-13 20:19 | +10 stop | ZEC | UP | 0.52 | 0.37 | -1.85 |
| 10-13 20:19 | +10 | ZEC | UP | 0.52 | open |  |
| 10-13 20:19 | +5 | ZEC | UP | 0.52 | open |  |
| 10-13 20:18 | +10 stop | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-13 20:18 | +20 | BTC | DOWN | 0.66 | 0.86 | 1.75 |
| 10-13 20:18 | +15 | BTC | DOWN | 0.66 | 0.84 | 1.54 |
| 10-13 20:18 | +10 | BTC | DOWN | 0.66 | 0.78 | 0.91 |
| 10-13 20:18 | +5 | BTC | DOWN | 0.66 | 0.71 | 0.19 |
| 10-13 20:18 | +10 stop | XRP | DOWN | 0.67 | 0.80 | 1.02 |
| 10-13 20:18 | +15 | XRP | DOWN | 0.67 | 0.86 | 1.65 |
| 10-13 20:18 | +10 | XRP | DOWN | 0.67 | 0.80 | 1.02 |
| 10-13 20:18 | +5 | XRP | DOWN | 0.67 | 0.72 | 0.19 |
| 10-13 20:18 | +10 stop | SOL | DOWN | 0.65 | 0.77 | 0.91 |
| 10-13 20:18 | +10 | SOL | DOWN | 0.65 | 0.77 | 0.91 |
| 10-13 20:18 | +5 | SOL | DOWN | 0.65 | 0.77 | 0.91 |
| 10-13 20:16 | +10 stop | BNB | DOWN | 0.70 | 0.81 | 0.84 |
| 10-13 20:16 | +20 | BNB | DOWN | 0.69 | 0.93 | 2.17 |
| 10-13 20:16 | +15 | BNB | DOWN | 0.67 | 0.88 | 1.82 |
| 10-13 20:16 | +10 | BNB | DOWN | 0.66 | 0.76 | 0.71 |
| 10-13 20:16 | +5 | BNB | DOWN | 0.66 | 0.72 | 0.29 |
| 10-13 20:16 | +10 stop | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 10-13 20:16 | +20 | XRP | DOWN | 0.67 | 0.92 | 2.28 |
| 10-13 20:16 | +15 | XRP | DOWN | 0.67 | 0.83 | 1.34 |
| 10-13 20:16 | +10 | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 10-13 20:16 | +5 | XRP | DOWN | 0.67 | 0.72 | 0.19 |
