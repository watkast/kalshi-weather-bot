# Range-Scalp Bot

*Updated Thu Oct 15 12:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17464 | 15160 | 2304 (28) | 1 | $-5325.56 | -4.8% |
| **+10¢** | 13197 | 10529 | 2668 (40) | 1 | $-4832.49 | -5.8% |
| **+15¢** | 11083 | 8214 | 2869 (59) | 1 | $-4315.37 | -6.2% |
| **+20¢** | 9848 | 6846 | 3002 (77) | 3 | $-3755.54 | -6.1% |
| **+10¢ (15¢ stop)** | 21488 | 21438 | 50 (29) | 0 | $-8291.27 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 12:13 | +10 stop | NEAR | DOWN | 0.66 | 0.51 | -1.85 |
| 10-15 12:13 | +20 | NEAR | DOWN | 0.66 | open |  |
| 10-15 12:13 | +15 | NEAR | DOWN | 0.66 | open |  |
| 10-15 12:13 | +10 | NEAR | DOWN | 0.66 | open |  |
| 10-15 12:13 | +5 | NEAR | DOWN | 0.66 | open |  |
| 10-15 12:10 | +10 stop | ETH | DOWN | 0.69 | 0.84 | 1.25 |
| 10-15 12:10 | +5 | ETH | DOWN | 0.69 | 0.74 | 0.21 |
| 10-15 12:10 | +5 | NEAR | DOWN | 0.71 | 0.79 | 0.53 |
| 10-15 12:09 | +10 stop | DOGE | DOWN | 0.59 | 0.73 | 1.09 |
| 10-15 12:09 | +10 stop | DOGE | UP | 0.42 | 0.54 | 0.84 |
| 10-15 12:08 | +10 | BTC | DOWN | 0.66 | 0.82 | 1.33 |
| 10-15 12:08 | +5 | BTC | DOWN | 0.66 | 0.74 | 0.50 |
| 10-15 12:08 | +10 stop | DOGE | UP | 0.52 | 0.62 | 0.65 |
| 10-15 12:07 | +10 stop | DOGE | DOWN | 0.43 | 0.54 | 0.74 |
| 10-15 12:07 | +10 stop | ETH | DOWN | 0.60 | 0.45 | -1.85 |
| 10-15 12:07 | +10 stop | BNB | DOWN | 0.68 | 0.52 | -1.94 |
| 10-15 12:07 | +10 | BNB | DOWN | 0.68 | 0.85 | 1.45 |
| 10-15 12:07 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 10-15 12:06 | +10 stop | DOGE | UP | 0.57 | 0.42 | -1.86 |
| 10-15 12:06 | +5 | NEAR | DOWN | 0.66 | 0.75 | 0.60 |
| 10-15 12:06 | +5 | BTC | DOWN | 0.67 | 0.73 | 0.30 |
| 10-15 12:06 | +10 stop | NEAR | DOWN | 0.67 | 0.79 | 0.92 |
| 10-15 12:06 | +20 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 10-15 12:06 | +15 | NEAR | DOWN | 0.67 | 0.84 | 1.44 |
| 10-15 12:06 | +10 | NEAR | DOWN | 0.67 | 0.79 | 0.92 |
| 10-15 12:06 | +5 | NEAR | DOWN | 0.65 | 0.72 | 0.39 |
| 10-15 12:06 | +10 stop | XRP | DOWN | 0.63 | 0.82 | 1.62 |
| 10-15 12:06 | +10 | XRP | DOWN | 0.64 | 0.82 | 1.52 |
| 10-15 12:06 | +5 | XRP | DOWN | 0.63 | 0.70 | 0.38 |
| 10-15 12:06 | +10 stop | BTC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-15 12:04 | +5 | XRP | DOWN | 0.66 | 0.74 | 0.50 |
| 10-15 12:04 | +10 stop | SOL | DOWN | 0.65 | 0.85 | 1.75 |
| 10-15 12:03 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-15 12:03 | +20 | XRP | DOWN | 0.65 | 0.86 | 1.85 |
| 10-15 12:03 | +15 | XRP | DOWN | 0.65 | 0.82 | 1.43 |
| 10-15 12:03 | +10 | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-15 12:03 | +5 | XRP | DOWN | 0.65 | 0.71 | 0.29 |
| 10-15 12:03 | +5 | BTC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-15 12:03 | +10 stop | DOGE | DOWN | 0.57 | 0.42 | -1.86 |
| 10-15 12:03 | +10 stop | ZEC | DOWN | 0.62 | 0.75 | 0.99 |
