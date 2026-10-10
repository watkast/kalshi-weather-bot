# Range-Scalp Bot

*Updated Sat Oct 10 14:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10531 | 9087 | 1444 (22) | 2 | $-3531.67 | -5.3% |
| **+10¢** | 7977 | 6293 | 1684 (36) | 3 | $-3360.39 | -6.7% |
| **+15¢** | 6731 | 4948 | 1783 (52) | 3 | $-2817.28 | -6.7% |
| **+20¢** | 5984 | 4126 | 1858 (66) | 3 | $-2380.04 | -6.3% |
| **+10¢ (15¢ stop)** | 12940 | 12902 | 38 (25) | 2 | $-5069.21 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 14:23 | +10 stop | ZEC | UP | 0.65 | open |  |
| 10-10 14:23 | +5 | ZEC | UP | 0.65 | open |  |
| 10-10 14:21 | +10 stop | BTC | UP | 0.56 | 0.70 | 1.07 |
| 10-10 14:21 | +20 | BTC | UP | 0.56 | 0.78 | 1.89 |
| 10-10 14:21 | +15 | BTC | UP | 0.56 | 0.73 | 1.38 |
| 10-10 14:21 | +10 | BTC | UP | 0.56 | 0.70 | 1.07 |
| 10-10 14:21 | +5 | BTC | UP | 0.56 | 0.64 | 0.45 |
| 10-10 14:20 | +10 stop | XRP | UP | 0.69 | 0.52 | -2.07 |
| 10-10 14:20 | +15 | XRP | UP | 0.69 | 0.93 | 2.13 |
| 10-10 14:20 | +10 | XRP | UP | 0.69 | 0.83 | 1.11 |
| 10-10 14:20 | +5 | XRP | UP | 0.69 | 0.76 | 0.38 |
| 10-10 14:20 | +10 stop | ZEC | UP | 0.67 | 0.51 | -1.94 |
| 10-10 14:19 | +10 stop | BNB | UP | 0.64 | 0.75 | 0.75 |
| 10-10 14:19 | +10 stop | NEAR | DOWN | 0.67 | open |  |
| 10-10 14:19 | +15 | NEAR | DOWN | 0.67 | open |  |
| 10-10 14:19 | +10 | NEAR | DOWN | 0.69 | open |  |
| 10-10 14:19 | +5 | NEAR | DOWN | 0.69 | 0.76 | 0.42 |
| 10-10 14:18 | +10 stop | ZEC | DOWN | 0.62 | 0.40 | -2.54 |
| 10-10 14:18 | +10 stop | BNB | DOWN | 0.58 | 0.43 | -1.86 |
| 10-10 14:18 | +20 | BNB | DOWN | 0.58 | open |  |
| 10-10 14:18 | +15 | BNB | DOWN | 0.58 | open |  |
| 10-10 14:18 | +10 | BNB | DOWN | 0.58 | open |  |
| 10-10 14:18 | +5 | BNB | DOWN | 0.58 | open |  |
| 10-10 14:17 | +10 stop | XRP | DOWN | 0.68 | 0.30 | -4.11 |
| 10-10 14:17 | +10 stop | SOL | UP | 0.70 | 0.80 | 0.73 |
| 10-10 14:17 | +20 | SOL | UP | 0.71 | 0.91 | 1.86 |
| 10-10 14:17 | +15 | SOL | UP | 0.71 | 0.88 | 1.51 |
| 10-10 14:17 | +10 | SOL | UP | 0.71 | 0.83 | 0.99 |
| 10-10 14:17 | +5 | SOL | UP | 0.71 | 0.80 | 0.67 |
| 10-10 14:17 | +10 stop | DOGE | UP | 0.60 | 0.78 | 1.45 |
| 10-10 14:17 | +20 | DOGE | UP | 0.60 | 0.82 | 1.87 |
| 10-10 14:17 | +15 | DOGE | UP | 0.60 | 0.78 | 1.45 |
| 10-10 14:17 | +10 | DOGE | UP | 0.60 | 0.78 | 1.45 |
| 10-10 14:17 | +5 | DOGE | UP | 0.62 | 0.68 | 0.27 |
| 10-10 14:17 | +10 stop | ETH | UP | 0.60 | 0.79 | 1.63 |
| 10-10 14:17 | +15 | ETH | UP | 0.59 | 0.79 | 1.71 |
| 10-10 14:17 | +10 | ETH | UP | 0.59 | 0.69 | 0.68 |
| 10-10 14:17 | +5 | ETH | UP | 0.59 | 0.69 | 0.68 |
| 10-10 14:17 | +5 | BTC | UP | 0.61 | 0.67 | 0.27 |
| 10-10 14:16 | +10 stop | ZEC | UP | 0.55 | 0.35 | -2.34 |
