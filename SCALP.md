# Range-Scalp Bot

*Updated Sun Oct 11 18:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12277 | 10588 | 1689 (25) | 0 | $-4104.09 | -5.3% |
| **+10¢** | 9328 | 7372 | 1956 (37) | 0 | $-3863.73 | -6.6% |
| **+15¢** | 7859 | 5783 | 2076 (54) | 0 | $-3294.68 | -6.7% |
| **+20¢** | 7006 | 4843 | 2163 (68) | 0 | $-2787.34 | -6.3% |
| **+10¢ (15¢ stop)** | 15133 | 15092 | 41 (25) | 0 | $-5971.53 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 18:13 | +10 stop | SOL | DOWN | 0.60 | 0.97 | 3.46 |
| 10-11 18:11 | +10 stop | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-11 18:11 | +10 stop | NEAR | UP | 0.49 | 0.31 | -2.11 |
| 10-11 18:11 | +10 stop | XRP | DOWN | 0.59 | 0.78 | 1.60 |
| 10-11 18:10 | +10 stop | BNB | DOWN | 0.58 | 0.68 | 0.66 |
| 10-11 18:10 | +10 stop | BTC | UP | 0.58 | 0.35 | -2.64 |
| 10-11 18:10 | +20 | BTC | UP | 0.59 | no | -6.07 |
| 10-11 18:10 | +15 | BTC | UP | 0.59 | no | -6.07 |
| 10-11 18:10 | +10 | BTC | UP | 0.59 | no | -6.07 |
| 10-11 18:10 | +5 | BTC | UP | 0.59 | no | -6.07 |
| 10-11 18:09 | +10 stop | XRP | UP | 0.70 | 0.50 | -2.33 |
| 10-11 18:09 | +10 stop | DOGE | DOWN | 0.57 | 0.80 | 2.00 |
| 10-11 18:08 | +10 stop | DOGE | UP | 0.43 | 0.58 | 1.14 |
| 10-11 18:08 | +10 stop | BNB | UP | 0.67 | 0.51 | -1.94 |
| 10-11 18:08 | +10 stop | ZEC | DOWN | 0.52 | 0.63 | 0.75 |
| 10-11 18:08 | +10 | ZEC | DOWN | 0.52 | 0.63 | 0.75 |
| 10-11 18:08 | +5 | ZEC | DOWN | 0.52 | 0.63 | 0.75 |
| 10-11 18:08 | +5 | BTC | UP | 0.68 | 0.73 | 0.20 |
| 10-11 18:07 | +10 stop | XRP | UP | 0.71 | 0.81 | 0.74 |
| 10-11 18:06 | +10 stop | XRP | UP | 0.53 | 0.65 | 0.85 |
| 10-11 18:06 | +10 stop | DOGE | DOWN | 0.67 | 0.49 | -2.14 |
| 10-11 18:06 | +5 | DOGE | DOWN | 0.67 | 0.80 | 1.02 |
| 10-11 18:06 | +10 stop | BNB | DOWN | 0.62 | 0.46 | -1.99 |
| 10-11 18:06 | +20 | BNB | DOWN | 0.62 | 0.88 | 2.31 |
| 10-11 18:06 | +15 | BNB | DOWN | 0.62 | 0.81 | 1.58 |
| 10-11 18:06 | +10 | BNB | DOWN | 0.62 | 0.76 | 1.06 |
| 10-11 18:06 | +5 | BNB | DOWN | 0.62 | 0.68 | 0.23 |
| 10-11 18:06 | +10 stop | BTC | UP | 0.59 | 0.69 | 0.68 |
| 10-11 18:06 | +20 | BTC | UP | 0.58 | 0.78 | 1.69 |
| 10-11 18:05 | +10 stop | SOL | UP | 0.61 | 0.72 | 0.78 |
| 10-11 18:05 | +10 stop | ETH | DOWN | 0.51 | 0.36 | -1.85 |
| 10-11 18:04 | +10 stop | BTC | DOWN | 0.66 | 0.50 | -1.94 |
| 10-11 18:04 | +10 stop | XRP | DOWN | 0.59 | 0.38 | -2.44 |
| 10-11 18:04 | +15 | XRP | DOWN | 0.59 | 0.78 | 1.60 |
| 10-11 18:04 | +10 | XRP | DOWN | 0.59 | 0.78 | 1.60 |
| 10-11 18:04 | +5 | XRP | DOWN | 0.58 | 0.65 | 0.36 |
| 10-11 18:03 | +10 stop | BTC | UP | 0.61 | 0.44 | -2.05 |
| 10-11 18:03 | +15 | BTC | UP | 0.61 | 0.78 | 1.40 |
| 10-11 18:03 | +10 | BTC | UP | 0.61 | 0.73 | 0.89 |
| 10-11 18:03 | +5 | BTC | UP | 0.61 | 0.67 | 0.27 |
