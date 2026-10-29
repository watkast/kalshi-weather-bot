# Range-Scalp Bot

*Updated Thu Oct 29 03:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38881 | 33930 | 4951 (49) | 9 | $-10910.06 | -4.5% |
| **+10¢** | 29006 | 23290 | 5716 (71) | 8 | $-9653.35 | -5.3% |
| **+15¢** | 24261 | 18120 | 6141 (97) | 9 | $-8606.54 | -5.6% |
| **+20¢** | 21527 | 15095 | 6432 (125) | 9 | $-7503.52 | -5.5% |
| **+10¢ (15¢ stop)** | 47565 | 47498 | 67 (35) | 0 | $-18067.90 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 03:25 | +10 | ZEC | UP | 0.39 | 0.64 | 2.16 |
| 10-29 03:24 | +5 | ZEC | UP | 0.71 | open |  |
| 10-29 03:24 | +10 stop | ZEC | UP | 0.71 | 0.36 | -3.82 |
| 10-29 03:24 | +10 stop | BTC | DOWN | 0.59 | 0.85 | 2.34 |
| 10-29 03:24 | +10 stop | XRP | DOWN | 0.63 | 0.48 | -1.85 |
| 10-29 03:24 | +10 stop | ETH | DOWN | 0.59 | 0.78 | 1.60 |
| 10-29 03:23 | +10 stop | BNB | DOWN | 0.70 | 0.87 | 1.47 |
| 10-29 03:23 | +5 | BNB | UP | 0.63 | open |  |
| 10-29 03:22 | +10 stop | DOGE | DOWN | 0.69 | 0.85 | 1.36 |
| 10-29 03:22 | +10 stop | ZEC | DOWN | 0.63 | 0.47 | -1.95 |
| 10-29 03:22 | +10 stop | SOL | DOWN | 0.58 | 0.73 | 1.18 |
| 10-29 03:22 | +10 stop | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 10-29 03:21 | +10 | ZEC | UP | 0.53 | 0.63 | 0.65 |
| 10-29 03:21 | +5 | ZEC | UP | 0.53 | 0.58 | 0.14 |
| 10-29 03:21 | +10 stop | XRP | UP | 0.54 | 0.24 | -3.31 |
| 10-29 03:21 | +20 | XRP | UP | 0.54 | open |  |
| 10-29 03:21 | +10 | XRP | UP | 0.55 | open |  |
| 10-29 03:21 | +5 | XRP | UP | 0.55 | open |  |
| 10-29 03:21 | +10 stop | BTC | DOWN | 0.66 | 0.80 | 1.12 |
| 10-29 03:21 | +10 stop | NEAR | UP | 0.52 | 0.33 | -2.24 |
| 10-29 03:21 | +10 | SOL | UP | 0.59 | open |  |
| 10-29 03:21 | +5 | SOL | UP | 0.60 | open |  |
| 10-29 03:21 | +10 | NEAR | UP | 0.57 | open |  |
| 10-29 03:21 | +5 | NEAR | UP | 0.57 | open |  |
| 10-29 03:20 | +15 | BTC | UP | 0.52 | open |  |
| 10-29 03:20 | +5 | ETH | UP | 0.65 | open |  |
| 10-29 03:20 | +5 | DOGE | UP | 0.69 | open |  |
| 10-29 03:20 | +10 stop | NEAR | UP | 0.70 | 0.52 | -2.13 |
| 10-29 03:19 | +15 | XRP | UP | 0.69 | open |  |
| 10-29 03:19 | +10 | XRP | UP | 0.69 | 0.79 | 0.73 |
| 10-29 03:19 | +5 | XRP | UP | 0.69 | 0.74 | 0.21 |
| 10-29 03:19 | +10 stop | BTC | UP | 0.64 | 0.48 | -1.95 |
| 10-29 03:19 | +10 | BTC | UP | 0.64 | open |  |
| 10-29 03:19 | +10 | ZEC | UP | 0.61 | 0.76 | 1.20 |
| 10-29 03:19 | +5 | ZEC | UP | 0.61 | 0.67 | 0.27 |
| 10-29 03:19 | +10 stop | NEAR | DOWN | 0.59 | 0.43 | -1.95 |
| 10-29 03:18 | +5 | DOGE | UP | 0.55 | 0.60 | 0.15 |
| 10-29 03:18 | +10 stop | SOL | UP | 0.62 | 0.43 | -2.25 |
| 10-29 03:18 | +10 stop | DOGE | UP | 0.56 | 0.36 | -2.35 |
| 10-29 03:18 | +5 | BTC | UP | 0.69 | open |  |
