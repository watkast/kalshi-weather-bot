# Range-Scalp Bot

*Updated Thu Oct 29 00:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38698 | 33766 | 4932 (49) | 1 | $-10889.31 | -4.5% |
| **+10¢** | 28859 | 23165 | 5694 (71) | 2 | $-9655.34 | -5.3% |
| **+15¢** | 24139 | 18020 | 6119 (97) | 1 | $-8626.21 | -5.7% |
| **+20¢** | 21418 | 15011 | 6407 (125) | 1 | $-7520.31 | -5.6% |
| **+10¢ (15¢ stop)** | 47340 | 47273 | 67 (35) | 0 | $-18002.07 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 00:12 | +5 | BTC | UP | 0.31 | 0.63 | 2.88 |
| 10-29 00:11 | +10 stop | ETH | UP | 0.56 | 0.21 | -3.80 |
| 10-29 00:11 | +10 stop | BTC | UP | 0.61 | 0.31 | -3.32 |
| 10-29 00:10 | +10 stop | DOGE | UP | 0.57 | 0.70 | 0.97 |
| 10-29 00:10 | +10 | DOGE | UP | 0.57 | 0.70 | 0.97 |
| 10-29 00:10 | +10 stop | BTC | DOWN | 0.67 | 0.45 | -2.54 |
| 10-29 00:09 | +10 stop | XRP | DOWN | 0.66 | 0.86 | 1.75 |
| 10-29 00:09 | +10 stop | NEAR | DOWN | 0.52 | 0.62 | 0.65 |
| 10-29 00:09 | +20 | NEAR | DOWN | 0.52 | 0.75 | 2.01 |
| 10-29 00:09 | +15 | NEAR | DOWN | 0.52 | 0.70 | 1.50 |
| 10-29 00:09 | +10 | NEAR | DOWN | 0.52 | 0.62 | 0.68 |
| 10-29 00:09 | +5 | NEAR | DOWN | 0.52 | 0.62 | 0.68 |
| 10-29 00:08 | +10 stop | DOGE | DOWN | 0.59 | 0.39 | -2.34 |
| 10-29 00:08 | +10 stop | ETH | DOWN | 0.66 | 0.49 | -2.04 |
| 10-29 00:08 | +10 stop | BTC | DOWN | 0.69 | 0.52 | -2.03 |
| 10-29 00:07 | +10 stop | DOGE | UP | 0.61 | 0.41 | -2.34 |
| 10-29 00:07 | +10 stop | SOL | UP | 0.59 | 0.69 | 0.68 |
| 10-29 00:07 | +10 stop | XRP | UP | 0.56 | 0.22 | -3.71 |
| 10-29 00:07 | +5 | XRP | UP | 0.56 | no | -5.78 |
| 10-29 00:07 | +10 stop | ETH | UP | 0.53 | 0.32 | -2.44 |
| 10-29 00:07 | +10 stop | ETH | DOWN | 0.41 | 0.61 | 1.66 |
| 10-29 00:07 | +10 stop | BTC | DOWN | 0.54 | 0.64 | 0.65 |
| 10-29 00:07 | +10 stop | SOL | DOWN | 0.49 | 0.65 | 1.26 |
| 10-29 00:06 | +10 stop | BNB | UP | 0.67 | 0.79 | 0.92 |
| 10-29 00:06 | +15 | BNB | UP | 0.67 | 0.85 | 1.55 |
| 10-29 00:06 | +10 | BNB | UP | 0.66 | 0.79 | 1.02 |
| 10-29 00:06 | +5 | BNB | UP | 0.66 | 0.79 | 1.02 |
| 10-29 00:05 | +5 | HYPE | UP | 0.59 | 0.68 | 0.57 |
| 10-29 00:04 | +5 | XRP | DOWN | 0.62 | 0.74 | 0.89 |
| 10-29 00:04 | +10 stop | ETH | DOWN | 0.63 | 0.76 | 1.00 |
| 10-29 00:04 | +10 stop | DOGE | UP | 0.54 | 0.39 | -1.85 |
| 10-29 00:04 | +10 | DOGE | UP | 0.54 | 0.70 | 1.27 |
| 10-29 00:04 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-29 00:04 | +10 stop | SOL | DOWN | 0.61 | 0.74 | 0.99 |
| 10-29 00:03 | +10 stop | ZEC | UP | 0.61 | 0.72 | 0.78 |
| 10-29 00:02 | +10 stop | ETH | DOWN | 0.62 | 0.34 | -3.13 |
| 10-29 00:02 | +10 stop | BTC | DOWN | 0.67 | 0.50 | -2.04 |
| 10-29 00:02 | +10 stop | SOL | DOWN | 0.70 | 0.44 | -2.93 |
| 10-29 00:02 | +10 stop | XRP | UP | 0.58 | 0.43 | -1.86 |
| 10-29 00:02 | +20 | XRP | UP | 0.58 | no | -5.98 |
