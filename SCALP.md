# Range-Scalp Bot

*Updated Wed Nov 04 19:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47444 | 41312 | 6132 (72) | 3 | $-13681.58 | -4.6% |
| **+10¢** | 35441 | 28327 | 7114 (97) | 3 | $-12518.79 | -5.6% |
| **+15¢** | 29681 | 22021 | 7660 (125) | 3 | $-11480.38 | -6.2% |
| **+20¢** | 26372 | 18349 | 8023 (165) | 3 | $-10137.65 | -6.1% |
| **+10¢ (15¢ stop)** | 57832 | 57739 | 93 (56) | 0 | $-21558.10 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 19:28 | +10 stop | BTC | DOWN | 0.56 | 0.73 | 1.38 |
| 11-04 19:28 | +10 stop | XRP | DOWN | 0.61 | 0.72 | 0.78 |
| 11-04 19:26 | +10 stop | ZEC | UP | 0.59 | 0.71 | 0.88 |
| 11-04 19:26 | +10 stop | DOGE | UP | 0.67 | 0.82 | 1.23 |
| 11-04 19:26 | +10 stop | NEAR | DOWN | 0.62 | 0.46 | -1.95 |
| 11-04 19:25 | +10 stop | DOGE | DOWN | 0.57 | 0.36 | -2.45 |
| 11-04 19:21 | +10 stop | DOGE | UP | 0.55 | 0.34 | -2.44 |
| 11-04 19:21 | +10 stop | ZEC | UP | 0.55 | 0.65 | 0.66 |
| 11-04 19:21 | +10 stop | NEAR | DOWN | 0.64 | 0.75 | 0.79 |
| 11-04 19:21 | +10 stop | SOL | DOWN | 0.51 | 0.64 | 0.95 |
| 11-04 19:21 | +10 stop | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 11-04 19:20 | +10 stop | ETH | DOWN | 0.61 | 0.71 | 0.68 |
| 11-04 19:20 | +10 stop | BTC | DOWN | 0.61 | 0.73 | 0.89 |
| 11-04 19:20 | +10 stop | BNB | DOWN | 0.59 | 0.74 | 1.14 |
| 11-04 19:20 | +5 | DOGE | UP | 0.62 | 0.68 | 0.27 |
| 11-04 19:19 | +5 | SOL | UP | 0.58 | 0.66 | 0.46 |
| 11-04 19:18 | +5 | NEAR | UP | 0.69 | 0.87 | 1.57 |
| 11-04 19:18 | +10 stop | BTC | UP | 0.57 | 0.40 | -2.05 |
| 11-04 19:18 | +10 stop | DOGE | UP | 0.67 | 0.47 | -2.34 |
| 11-04 19:18 | +10 | DOGE | UP | 0.67 | 0.82 | 1.23 |
| 11-04 19:18 | +5 | DOGE | UP | 0.67 | 0.73 | 0.30 |
| 11-04 19:18 | +10 stop | SOL | UP | 0.65 | 0.48 | -2.04 |
| 11-04 19:18 | +20 | SOL | UP | 0.65 | 0.91 | 2.36 |
| 11-04 19:18 | +15 | SOL | UP | 0.63 | 0.91 | 2.55 |
| 11-04 19:18 | +10 | SOL | UP | 0.63 | 0.73 | 0.69 |
| 11-04 19:18 | +5 | SOL | UP | 0.63 | 0.69 | 0.28 |
| 11-04 19:17 | +10 stop | XRP | UP | 0.64 | 0.41 | -2.64 |
| 11-04 19:17 | +10 | XRP | UP | 0.64 | open |  |
| 11-04 19:17 | +5 | XRP | UP | 0.64 | open |  |
| 11-04 19:17 | +10 stop | NEAR | UP | 0.60 | 0.40 | -2.34 |
| 11-04 19:17 | +20 | NEAR | UP | 0.60 | 0.87 | 2.45 |
| 11-04 19:17 | +15 | NEAR | UP | 0.60 | 0.87 | 2.45 |
| 11-04 19:17 | +10 | NEAR | UP | 0.60 | 0.70 | 0.68 |
| 11-04 19:17 | +5 | NEAR | UP | 0.60 | 0.67 | 0.37 |
| 11-04 19:16 | +10 stop | BTC | UP | 0.67 | 0.52 | -1.84 |
| 11-04 19:16 | +20 | BTC | UP | 0.67 | open |  |
| 11-04 19:16 | +15 | BTC | UP | 0.67 | open |  |
| 11-04 19:16 | +10 | BTC | UP | 0.67 | open |  |
| 11-04 19:16 | +5 | BTC | UP | 0.67 | open |  |
| 11-04 19:16 | +10 stop | ETH | UP | 0.68 | 0.51 | -2.04 |
