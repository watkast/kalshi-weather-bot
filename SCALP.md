# Range-Scalp Bot

*Updated Thu Oct 29 16:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39426 | 34418 | 5008 (50) | 1 | $-10963.34 | -4.4% |
| **+10¢** | 29393 | 23606 | 5787 (73) | 1 | $-9704.90 | -5.2% |
| **+15¢** | 24576 | 18357 | 6219 (100) | 1 | $-8668.40 | -5.6% |
| **+20¢** | 21806 | 15291 | 6515 (129) | 1 | $-7555.61 | -5.5% |
| **+10¢ (15¢ stop)** | 48168 | 48098 | 70 (37) | 0 | $-18261.24 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 16:19 | +10 stop | BNB | DOWN | 0.65 | 0.75 | 0.70 |
| 10-29 16:17 | +10 stop | BNB | DOWN | 0.67 | 0.49 | -2.14 |
| 10-29 16:17 | +20 | BNB | DOWN | 0.67 | 0.87 | 1.76 |
| 10-29 16:17 | +15 | BNB | DOWN | 0.67 | 0.84 | 1.44 |
| 10-29 16:17 | +10 | BNB | DOWN | 0.67 | 0.77 | 0.71 |
| 10-29 16:17 | +5 | BNB | DOWN | 0.67 | 0.75 | 0.50 |
| 10-29 16:16 | +10 stop | NEAR | DOWN | 0.66 | 0.78 | 0.91 |
| 10-29 16:16 | +10 stop | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 10-29 16:16 | +20 | SOL | DOWN | 0.70 | 0.90 | 1.79 |
| 10-29 16:16 | +15 | SOL | DOWN | 0.70 | 0.86 | 1.36 |
| 10-29 16:16 | +10 | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 10-29 16:16 | +5 | SOL | DOWN | 0.70 | 0.78 | 0.52 |
| 10-29 16:16 | +10 stop | XRP | DOWN | 0.61 | 0.74 | 0.99 |
| 10-29 16:16 | +20 | XRP | DOWN | 0.61 | 0.81 | 1.72 |
| 10-29 16:16 | +15 | XRP | DOWN | 0.61 | 0.79 | 1.51 |
| 10-29 16:16 | +10 | XRP | DOWN | 0.61 | 0.74 | 0.99 |
| 10-29 16:16 | +5 | XRP | DOWN | 0.61 | 0.67 | 0.27 |
| 10-29 16:16 | +10 stop | BTC | DOWN | 0.59 | 0.71 | 0.88 |
| 10-29 16:16 | +20 | BTC | DOWN | 0.59 | 0.84 | 2.23 |
| 10-29 16:16 | +15 | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 10-29 16:16 | +10 | BTC | DOWN | 0.59 | 0.71 | 0.88 |
| 10-29 16:16 | +5 | BTC | DOWN | 0.58 | 0.68 | 0.66 |
| 10-29 16:15 | +10 stop | NEAR | UP | 0.55 | 0.38 | -2.05 |
| 10-29 16:15 | +20 | NEAR | UP | 0.55 | open |  |
| 10-29 16:15 | +15 | NEAR | UP | 0.55 | open |  |
| 10-29 16:15 | +10 | NEAR | UP | 0.53 | open |  |
| 10-29 16:15 | +5 | NEAR | UP | 0.53 | open |  |
| 10-29 16:13 | +10 stop | SOL | DOWN | 0.70 | 0.91 | 1.86 |
| 10-29 16:13 | +15 | SOL | DOWN | 0.71 | 0.91 | 1.76 |
| 10-29 16:13 | +10 | SOL | DOWN | 0.70 | 0.91 | 1.86 |
| 10-29 16:13 | +5 | SOL | DOWN | 0.70 | 0.91 | 1.86 |
| 10-29 16:12 | +10 stop | ETH | UP | 0.52 | 0.15 | -3.97 |
| 10-29 16:12 | +10 stop | SOL | UP | 0.49 | 0.68 | 1.56 |
| 10-29 16:12 | +5 | SOL | UP | 0.47 | 0.68 | 1.76 |
| 10-29 16:12 | +10 stop | BTC | UP | 0.34 | 0.65 | 2.78 |
| 10-29 16:12 | +20 | BTC | UP | 0.34 | 0.65 | 2.78 |
| 10-29 16:12 | +15 | BTC | UP | 0.35 | 0.65 | 2.68 |
| 10-29 16:12 | +10 | BTC | UP | 0.35 | 0.65 | 2.68 |
| 10-29 16:12 | +5 | BTC | UP | 0.35 | 0.65 | 2.68 |
| 10-29 16:07 | +5 | BTC | UP | 0.68 | 0.80 | 0.92 |
