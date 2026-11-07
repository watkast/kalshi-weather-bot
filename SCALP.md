# Range-Scalp Bot

*Updated Sat Nov 07 10:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50862 | 44344 | 6518 (76) | 3 | $-14228.81 | -4.4% |
| **+10¢** | 37963 | 30366 | 7597 (102) | 7 | $-13205.44 | -5.5% |
| **+15¢** | 31780 | 23594 | 8186 (131) | 6 | $-12120.93 | -6.1% |
| **+20¢** | 28258 | 19677 | 8581 (173) | 7 | $-10707.36 | -6.0% |
| **+10¢ (15¢ stop)** | 61946 | 61847 | 99 (58) | 0 | $-22895.36 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 10:21 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 11-07 10:21 | +10 stop | BTC | UP | 0.52 | 0.33 | -2.24 |
| 11-07 10:20 | +10 stop | ZEC | DOWN | 0.62 | 0.73 | 0.79 |
| 11-07 10:20 | +10 stop | HYPE | UP | 0.69 | 0.81 | 0.95 |
| 11-07 10:20 | +10 stop | XRP | DOWN | 0.69 | 0.54 | -1.83 |
| 11-07 10:20 | +5 | DOGE | DOWN | 0.61 | 0.75 | 1.09 |
| 11-07 10:20 | +5 | XRP | DOWN | 0.70 | 0.79 | 0.63 |
| 11-07 10:19 | +10 stop | DOGE | DOWN | 0.49 | 0.60 | 0.75 |
| 11-07 10:19 | +5 | DOGE | DOWN | 0.50 | 0.57 | 0.34 |
| 11-07 10:19 | +10 stop | XRP | DOWN | 0.51 | 0.66 | 1.16 |
| 11-07 10:19 | +5 | XRP | DOWN | 0.51 | 0.59 | 0.45 |
| 11-07 10:19 | +10 stop | BTC | DOWN | 0.58 | 0.41 | -2.05 |
| 11-07 10:19 | +10 | BTC | DOWN | 0.58 | open |  |
| 11-07 10:19 | +10 stop | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 11-07 10:19 | +10 stop | HYPE | DOWN | 0.56 | 0.41 | -1.85 |
| 11-07 10:18 | +10 stop | HYPE | UP | 0.57 | 0.68 | 0.76 |
| 11-07 10:18 | +5 | HYPE | UP | 0.69 | 0.74 | 0.21 |
| 11-07 10:18 | +5 | BTC | UP | 0.59 | open |  |
| 11-07 10:17 | +10 stop | DOGE | UP | 0.68 | 0.49 | -2.24 |
| 11-07 10:17 | +5 | NEAR | DOWN | 0.61 | 0.67 | 0.27 |
| 11-07 10:17 | +10 stop | HYPE | DOWN | 0.54 | 0.33 | -2.44 |
| 11-07 10:17 | +20 | HYPE | DOWN | 0.54 | open |  |
| 11-07 10:17 | +15 | HYPE | DOWN | 0.54 | open |  |
| 11-07 10:17 | +10 | HYPE | DOWN | 0.54 | open |  |
| 11-07 10:17 | +5 | HYPE | DOWN | 0.54 | 0.62 | 0.45 |
| 11-07 10:17 | +10 stop | XRP | UP | 0.67 | 0.48 | -2.24 |
| 11-07 10:17 | +10 stop | BTC | DOWN | 0.49 | 0.60 | 0.75 |
| 11-07 10:17 | +20 | BTC | DOWN | 0.49 | open |  |
| 11-07 10:17 | +15 | BTC | DOWN | 0.49 | 0.66 | 1.36 |
| 11-07 10:17 | +10 | BTC | DOWN | 0.49 | 0.60 | 0.75 |
| 11-07 10:17 | +5 | BTC | DOWN | 0.49 | 0.54 | 0.14 |
| 11-07 10:16 | +10 stop | ETH | DOWN | 0.47 | 0.64 | 1.35 |
| 11-07 10:16 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-07 10:16 | +10 stop | NEAR | DOWN | 0.63 | 0.73 | 0.69 |
| 11-07 10:16 | +5 | NEAR | DOWN | 0.63 | 0.69 | 0.28 |
| 11-07 10:16 | +5 | BNB | DOWN | 0.40 | 0.55 | 1.15 |
| 11-07 10:16 | +10 stop | ZEC | DOWN | 0.62 | 0.45 | -2.05 |
| 11-07 10:16 | +20 | ZEC | DOWN | 0.62 | 0.83 | 1.83 |
| 11-07 10:16 | +15 | ZEC | DOWN | 0.62 | 0.77 | 1.20 |
| 11-07 10:16 | +10 | ZEC | DOWN | 0.62 | 0.73 | 0.79 |
