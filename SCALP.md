# Range-Scalp Bot

*Updated Mon Nov 23 00:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69311 | 60477 | 8834 (146) | 2 | $-18661.64 | -4.3% |
| **+10¢** | 51724 | 41408 | 10316 (189) | 3 | $-17315.79 | -5.3% |
| **+15¢** | 43349 | 32230 | 11119 (244) | 3 | $-15505.91 | -5.7% |
| **+20¢** | 38606 | 26918 | 11688 (305) | 3 | $-13797.72 | -5.7% |
| **+10¢ (15¢ stop)** | 84395 | 84205 | 190 (118) | 0 | $-31042.00 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 00:43 | +10 stop | SOL | DOWN | 0.27 | 0.61 | 3.10 |
| 11-23 00:43 | +20 | SOL | DOWN | 0.30 | 0.61 | 2.78 |
| 11-23 00:43 | +15 | SOL | DOWN | 0.31 | 0.61 | 2.68 |
| 11-23 00:43 | +10 | SOL | DOWN | 0.31 | 0.61 | 2.68 |
| 11-23 00:43 | +5 | SOL | DOWN | 0.30 | 0.61 | 2.78 |
| 11-23 00:43 | +10 stop | BTC | DOWN | 0.50 | 0.66 | 1.26 |
| 11-23 00:42 | +10 stop | BNB | DOWN | 0.55 | 0.69 | 1.07 |
| 11-23 00:42 | +10 | BNB | DOWN | 0.55 | 0.69 | 1.07 |
| 11-23 00:42 | +5 | BNB | DOWN | 0.55 | 0.69 | 1.07 |
| 11-23 00:42 | +10 stop | BTC | DOWN | 0.46 | 0.57 | 0.74 |
| 11-23 00:41 | +10 stop | NEAR | DOWN | 0.51 | 0.64 | 0.95 |
| 11-23 00:41 | +5 | NEAR | DOWN | 0.59 | 0.64 | 0.16 |
| 11-23 00:41 | +5 | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 11-23 00:40 | +5 | NEAR | UP | 0.39 | 0.59 | 1.66 |
| 11-23 00:40 | +10 stop | NEAR | UP | 0.60 | 0.36 | -2.74 |
| 11-23 00:38 | +10 stop | BNB | DOWN | 0.70 | 0.84 | 1.18 |
| 11-23 00:38 | +10 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-23 00:38 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 11-23 00:38 | +10 stop | ETH | DOWN | 0.68 | 0.82 | 1.13 |
| 11-23 00:38 | +10 stop | SOL | DOWN | 0.56 | 0.76 | 1.69 |
| 11-23 00:38 | +20 | SOL | DOWN | 0.56 | 0.76 | 1.69 |
| 11-23 00:38 | +15 | SOL | DOWN | 0.58 | 0.76 | 1.49 |
| 11-23 00:38 | +10 | SOL | DOWN | 0.59 | 0.76 | 1.40 |
| 11-23 00:38 | +5 | SOL | DOWN | 0.59 | 0.76 | 1.40 |
| 11-23 00:37 | +10 stop | NEAR | UP | 0.59 | 0.43 | -1.95 |
| 11-23 00:37 | +20 | NEAR | UP | 0.59 | open |  |
| 11-23 00:37 | +15 | NEAR | UP | 0.59 | open |  |
| 11-23 00:37 | +10 | NEAR | UP | 0.59 | open |  |
| 11-23 00:37 | +5 | NEAR | UP | 0.59 | 0.67 | 0.47 |
| 11-23 00:37 | +10 stop | BNB | UP | 0.40 | 0.54 | 1.05 |
| 11-23 00:37 | +20 | BNB | UP | 0.40 | 0.69 | 2.58 |
| 11-23 00:37 | +15 | BNB | UP | 0.40 | 0.69 | 2.58 |
| 11-23 00:37 | +10 | BNB | UP | 0.41 | 0.54 | 0.95 |
| 11-23 00:37 | +5 | BNB | UP | 0.41 | 0.54 | 0.95 |
| 11-23 00:37 | +10 stop | BTC | UP | 0.47 | 0.23 | -2.71 |
| 11-23 00:37 | +20 | BTC | UP | 0.47 | 0.78 | 2.79 |
| 11-23 00:37 | +15 | BTC | UP | 0.47 | 0.78 | 2.79 |
| 11-23 00:37 | +10 | BTC | UP | 0.47 | 0.78 | 2.79 |
| 11-23 00:37 | +5 | BTC | UP | 0.47 | 0.55 | 0.44 |
| 11-23 00:36 | +10 stop | XRP | UP | 0.65 | 0.26 | -4.20 |
