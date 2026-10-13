# Range-Scalp Bot

*Updated Tue Oct 13 00:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14050 | 12156 | 1894 (26) | 5 | $-4494.11 | -5.1% |
| **+10¢** | 10634 | 8430 | 2204 (38) | 5 | $-4241.47 | -6.3% |
| **+15¢** | 8929 | 6572 | 2357 (56) | 6 | $-3777.45 | -6.7% |
| **+20¢** | 7946 | 5492 | 2454 (71) | 6 | $-3227.34 | -6.5% |
| **+10¢ (15¢ stop)** | 17239 | 17190 | 49 (29) | 0 | $-6700.08 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 00:11 | +10 stop | ZEC | DOWN | 0.67 | 0.38 | -3.23 |
| 10-13 00:11 | +20 | ZEC | DOWN | 0.65 | 0.87 | 1.91 |
| 10-13 00:11 | +15 | ZEC | DOWN | 0.63 | 0.78 | 1.23 |
| 10-13 00:11 | +10 | ZEC | DOWN | 0.62 | 0.73 | 0.82 |
| 10-13 00:11 | +5 | ZEC | DOWN | 0.62 | 0.73 | 0.75 |
| 10-13 00:09 | +10 stop | NEAR | UP | 0.64 | 0.80 | 1.31 |
| 10-13 00:09 | +20 | NEAR | UP | 0.64 | 0.91 | 2.50 |
| 10-13 00:09 | +15 | NEAR | UP | 0.64 | 0.80 | 1.31 |
| 10-13 00:09 | +10 | NEAR | UP | 0.64 | 0.80 | 1.31 |
| 10-13 00:09 | +5 | NEAR | UP | 0.64 | 0.71 | 0.38 |
| 10-13 00:06 | +5 | XRP | DOWN | 0.60 | 0.70 | 0.68 |
| 10-13 00:05 | +10 stop | XRP | DOWN | 0.70 | 0.95 | 2.29 |
| 10-13 00:05 | +10 | XRP | DOWN | 0.70 | 0.95 | 2.29 |
| 10-13 00:05 | +5 | XRP | DOWN | 0.70 | 0.79 | 0.63 |
| 10-13 00:05 | +10 stop | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-13 00:04 | +10 | NEAR | DOWN | 0.60 | 0.72 | 0.88 |
| 10-13 00:04 | +5 | NEAR | DOWN | 0.58 | 0.69 | 0.77 |
| 10-13 00:04 | +10 stop | NEAR | DOWN | 0.56 | 0.69 | 0.97 |
| 10-13 00:04 | +5 | NEAR | DOWN | 0.56 | 0.61 | 0.15 |
| 10-13 00:04 | +5 | SOL | UP | 0.69 | open |  |
| 10-13 00:03 | +10 stop | BNB | UP | 0.62 | 0.41 | -2.44 |
| 10-13 00:03 | +10 | BNB | UP | 0.62 | open |  |
| 10-13 00:03 | +5 | BNB | UP | 0.62 | open |  |
| 10-13 00:03 | +5 | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-13 00:03 | +5 | DOGE | UP | 0.67 | open |  |
| 10-13 00:02 | +5 | BTC | UP | 0.66 | open |  |
| 10-13 00:02 | +5 | BNB | UP | 0.57 | 0.65 | 0.46 |
| 10-13 00:02 | +10 stop | DOGE | UP | 0.60 | 0.39 | -2.44 |
| 10-13 00:02 | +20 | DOGE | UP | 0.60 | open |  |
| 10-13 00:02 | +15 | DOGE | UP | 0.60 | open |  |
| 10-13 00:02 | +10 | DOGE | UP | 0.60 | open |  |
| 10-13 00:02 | +5 | DOGE | UP | 0.60 | 0.66 | 0.27 |
| 10-13 00:02 | +10 stop | SOL | UP | 0.66 | 0.45 | -2.44 |
| 10-13 00:02 | +20 | SOL | UP | 0.66 | open |  |
| 10-13 00:02 | +15 | SOL | UP | 0.67 | open |  |
| 10-13 00:02 | +10 | SOL | UP | 0.67 | open |  |
| 10-13 00:02 | +5 | SOL | UP | 0.67 | 0.74 | 0.43 |
| 10-13 00:02 | +5 | ETH | UP | 0.68 | open |  |
| 10-13 00:01 | +10 stop | XRP | UP | 0.67 | 0.79 | 0.92 |
| 10-13 00:01 | +20 | XRP | UP | 0.67 | open |  |
