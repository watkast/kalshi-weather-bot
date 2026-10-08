# Range-Scalp Bot

*Updated Thu Oct 08 16:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7683 | 6660 | 1023 (13) | 3 | $-2381.92 | -4.9% |
| **+10¢** | 5826 | 4616 | 1210 (24) | 4 | $-2330.85 | -6.4% |
| **+15¢** | 4895 | 3623 | 1272 (32) | 3 | $-1900.73 | -6.2% |
| **+20¢** | 4375 | 3055 | 1320 (40) | 3 | $-1490.43 | -5.4% |
| **+10¢ (15¢ stop)** | 9339 | 9310 | 29 (18) | 0 | $-3433.57 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 16:11 | +10 | BNB | UP | 0.56 | open |  |
| 10-08 16:11 | +10 | BNB | UP | 0.49 | 0.61 | 0.85 |
| 10-08 16:11 | +10 stop | BNB | UP | 0.56 | 0.20 | -3.90 |
| 10-08 16:11 | +10 stop | ETH | UP | 0.63 | 0.48 | -1.85 |
| 10-08 16:09 | +10 stop | BNB | DOWN | 0.68 | 0.47 | -2.42 |
| 10-08 16:09 | +5 | BNB | DOWN | 0.68 | 0.79 | 0.84 |
| 10-08 16:09 | +10 stop | SOL | UP | 0.66 | 0.80 | 1.12 |
| 10-08 16:08 | +10 stop | BTC | UP | 0.60 | 0.71 | 0.78 |
| 10-08 16:08 | +10 stop | NEAR | UP | 0.57 | 0.72 | 1.17 |
| 10-08 16:08 | +10 stop | DOGE | UP | 0.59 | 0.69 | 0.68 |
| 10-08 16:08 | +5 | DOGE | UP | 0.59 | 0.67 | 0.47 |
| 10-08 16:08 | +10 stop | BTC | DOWN | 0.46 | 0.56 | 0.64 |
| 10-08 16:08 | +10 stop | ETH | DOWN | 0.63 | 0.45 | -2.15 |
| 10-08 16:07 | +10 stop | XRP | UP | 0.61 | 0.82 | 1.82 |
| 10-08 16:07 | +10 stop | SOL | DOWN | 0.58 | 0.37 | -2.45 |
| 10-08 16:06 | +10 stop | BTC | DOWN | 0.63 | 0.46 | -2.05 |
| 10-08 16:06 | +5 | BTC | DOWN | 0.63 | open |  |
| 10-08 16:06 | +10 stop | NEAR | DOWN | 0.62 | 0.76 | 1.10 |
| 10-08 16:06 | +10 stop | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-08 16:05 | +10 stop | BTC | UP | 0.53 | 0.35 | -2.14 |
| 10-08 16:05 | +10 stop | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-08 16:05 | +5 | XRP | UP | 0.68 | 0.82 | 1.13 |
| 10-08 16:05 | +5 | XRP | UP | 0.60 | 0.65 | 0.17 |
| 10-08 16:05 | +10 stop | BNB | DOWN | 0.66 | 0.82 | 1.33 |
| 10-08 16:05 | +5 | BNB | DOWN | 0.66 | 0.75 | 0.60 |
| 10-08 16:04 | +10 stop | ETH | DOWN | 0.62 | 0.72 | 0.68 |
| 10-08 16:04 | +10 stop | XRP | UP | 0.63 | 0.42 | -2.44 |
| 10-08 16:04 | +10 | XRP | UP | 0.63 | 0.82 | 1.64 |
| 10-08 16:04 | +5 | XRP | UP | 0.63 | 0.69 | 0.30 |
| 10-08 16:03 | +10 stop | SOL | UP | 0.54 | 0.36 | -2.15 |
| 10-08 16:03 | +15 | SOL | UP | 0.53 | 0.74 | 1.78 |
| 10-08 16:03 | +10 stop | DOGE | UP | 0.71 | 0.53 | -2.13 |
| 10-08 16:03 | +10 | SOL | UP | 0.70 | 0.80 | 0.76 |
| 10-08 16:03 | +5 | SOL | UP | 0.71 | 0.80 | 0.66 |
| 10-08 16:03 | +10 stop | BTC | UP | 0.70 | 0.51 | -2.23 |
| 10-08 16:02 | +10 stop | ZEC | UP | 0.65 | 0.79 | 1.12 |
| 10-08 16:02 | +10 stop | DOGE | DOWN | 0.57 | 0.41 | -1.95 |
| 10-08 16:02 | +10 stop | BTC | DOWN | 0.59 | 0.39 | -2.34 |
| 10-08 16:02 | +20 | BTC | DOWN | 0.59 | open |  |
| 10-08 16:02 | +15 | BTC | DOWN | 0.59 | open |  |
