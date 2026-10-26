# Range-Scalp Bot

*Updated Mon Oct 26 23:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35579 | 31045 | 4534 (43) | 2 | $-9996.22 | -4.5% |
| **+10¢** | 26607 | 21364 | 5243 (65) | 2 | $-8831.19 | -5.3% |
| **+15¢** | 22271 | 16632 | 5639 (89) | 2 | $-7903.49 | -5.7% |
| **+20¢** | 19745 | 13835 | 5910 (112) | 4 | $-6968.63 | -5.6% |
| **+10¢ (15¢ stop)** | 43628 | 43566 | 62 (33) | 1 | $-16622.78 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 23:22 | +10 stop | NEAR | UP | 0.61 | open |  |
| 10-26 23:21 | +10 stop | BNB | UP | 0.60 | 0.43 | -2.05 |
| 10-26 23:21 | +15 | BNB | UP | 0.60 | open |  |
| 10-26 23:21 | +10 | BNB | UP | 0.61 | open |  |
| 10-26 23:21 | +5 | BNB | UP | 0.62 | open |  |
| 10-26 23:21 | +10 stop | NEAR | UP | 0.69 | 0.51 | -2.13 |
| 10-26 23:21 | +15 | NEAR | UP | 0.69 | open |  |
| 10-26 23:21 | +10 | NEAR | UP | 0.69 | open |  |
| 10-26 23:21 | +5 | NEAR | UP | 0.69 | open |  |
| 10-26 23:21 | +10 stop | BNB | UP | 0.49 | 0.66 | 1.35 |
| 10-26 23:21 | +20 | BNB | UP | 0.49 | open |  |
| 10-26 23:21 | +15 | BNB | UP | 0.50 | 0.66 | 1.26 |
| 10-26 23:21 | +10 | BNB | UP | 0.47 | 0.66 | 1.56 |
| 10-26 23:21 | +5 | BNB | UP | 0.48 | 0.66 | 1.46 |
| 10-26 23:17 | +5 | BNB | UP | 0.62 | 0.75 | 0.99 |
| 10-26 23:17 | +10 stop | SOL | UP | 0.65 | 0.78 | 1.01 |
| 10-26 23:17 | +20 | SOL | UP | 0.65 | 0.90 | 2.29 |
| 10-26 23:17 | +15 | SOL | UP | 0.65 | 0.82 | 1.43 |
| 10-26 23:17 | +10 | SOL | UP | 0.66 | 0.78 | 0.91 |
| 10-26 23:17 | +5 | SOL | UP | 0.66 | 0.78 | 0.91 |
| 10-26 23:17 | +10 stop | NEAR | UP | 0.66 | 0.79 | 0.97 |
| 10-26 23:17 | +20 | NEAR | UP | 0.67 | open |  |
| 10-26 23:17 | +15 | NEAR | UP | 0.67 | 0.83 | 1.39 |
| 10-26 23:17 | +10 | NEAR | UP | 0.67 | 0.79 | 0.97 |
| 10-26 23:17 | +5 | NEAR | UP | 0.67 | 0.73 | 0.33 |
| 10-26 23:17 | +10 stop | BNB | UP | 0.56 | 0.75 | 1.58 |
| 10-26 23:17 | +20 | BNB | UP | 0.56 | 0.79 | 2.00 |
| 10-26 23:17 | +15 | BNB | UP | 0.56 | 0.75 | 1.58 |
| 10-26 23:17 | +10 | BNB | UP | 0.56 | 0.75 | 1.58 |
| 10-26 23:17 | +5 | BNB | UP | 0.55 | 0.63 | 0.45 |
| 10-26 23:17 | +5 | ZEC | UP | 0.61 | 0.66 | 0.17 |
| 10-26 23:16 | +10 stop | DOGE | UP | 0.71 | 0.84 | 1.05 |
| 10-26 23:16 | +20 | DOGE | UP | 0.71 | 0.91 | 1.79 |
| 10-26 23:16 | +15 | DOGE | UP | 0.71 | 0.86 | 1.26 |
| 10-26 23:16 | +10 | DOGE | UP | 0.71 | 0.84 | 1.05 |
| 10-26 23:16 | +5 | DOGE | UP | 0.71 | 0.84 | 1.05 |
| 10-26 23:16 | +10 stop | BTC | UP | 0.64 | 0.82 | 1.52 |
| 10-26 23:16 | +20 | BTC | UP | 0.64 | open |  |
| 10-26 23:16 | +15 | BTC | UP | 0.64 | 0.82 | 1.52 |
| 10-26 23:16 | +10 | BTC | UP | 0.64 | 0.82 | 1.52 |
