# Range-Scalp Bot

*Updated Tue Oct 27 23:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37224 | 32497 | 4727 (45) | 3 | $-10346.01 | -4.4% |
| **+10¢** | 27796 | 22318 | 5478 (67) | 5 | $-9259.13 | -5.3% |
| **+15¢** | 23257 | 17375 | 5882 (91) | 5 | $-8213.48 | -5.6% |
| **+20¢** | 20607 | 14452 | 6155 (116) | 6 | $-7190.96 | -5.6% |
| **+10¢ (15¢ stop)** | 45604 | 45539 | 65 (34) | 0 | $-17391.48 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 23:22 | +10 stop | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 10-27 23:22 | +5 | BTC | DOWN | 0.71 | 0.80 | 0.63 |
| 10-27 23:17 | +10 stop | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 10-27 23:17 | +20 | SOL | DOWN | 0.71 | open |  |
| 10-27 23:17 | +10 stop | BNB | DOWN | 0.64 | 0.81 | 1.38 |
| 10-27 23:17 | +15 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 10-27 23:17 | +10 | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 10-27 23:17 | +5 | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 10-27 23:17 | +10 stop | SOL | DOWN | 0.69 | 0.81 | 0.94 |
| 10-27 23:16 | +5 | ETH | DOWN | 0.68 | 0.77 | 0.61 |
| 10-27 23:16 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 10-27 23:16 | +10 stop | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 10-27 23:16 | +20 | ZEC | DOWN | 0.70 | 0.90 | 1.79 |
| 10-27 23:16 | +15 | ZEC | DOWN | 0.70 | 0.87 | 1.47 |
| 10-27 23:16 | +10 | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 10-27 23:16 | +5 | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 10-27 23:16 | +10 stop | ETH | UP | 0.48 | 0.32 | -1.94 |
| 10-27 23:16 | +20 | ETH | UP | 0.48 | open |  |
| 10-27 23:16 | +15 | ETH | UP | 0.48 | open |  |
| 10-27 23:16 | +10 | ETH | UP | 0.48 | open |  |
| 10-27 23:16 | +5 | ETH | UP | 0.48 | 0.57 | 0.54 |
| 10-27 23:16 | +10 stop | XRP | UP | 0.50 | 0.32 | -2.14 |
| 10-27 23:16 | +20 | XRP | UP | 0.50 | open |  |
| 10-27 23:16 | +15 | XRP | UP | 0.50 | open |  |
| 10-27 23:16 | +10 | XRP | UP | 0.49 | 0.59 | 0.65 |
| 10-27 23:16 | +5 | XRP | UP | 0.49 | 0.59 | 0.65 |
| 10-27 23:16 | +10 stop | NEAR | UP | 0.49 | 0.30 | -2.23 |
| 10-27 23:16 | +20 | NEAR | UP | 0.50 | open |  |
| 10-27 23:16 | +15 | NEAR | UP | 0.50 | open |  |
| 10-27 23:16 | +10 | NEAR | UP | 0.49 | open |  |
| 10-27 23:16 | +5 | NEAR | UP | 0.49 | open |  |
| 10-27 23:16 | +10 stop | BNB | UP | 0.51 | 0.36 | -1.85 |
| 10-27 23:16 | +20 | BNB | UP | 0.51 | open |  |
| 10-27 23:16 | +15 | BNB | UP | 0.51 | open |  |
| 10-27 23:16 | +10 | BNB | UP | 0.51 | open |  |
| 10-27 23:16 | +5 | BNB | UP | 0.51 | open |  |
| 10-27 23:16 | +10 stop | BTC | UP | 0.48 | 0.33 | -1.84 |
| 10-27 23:16 | +20 | BTC | UP | 0.48 | open |  |
| 10-27 23:16 | +15 | BTC | UP | 0.48 | open |  |
| 10-27 23:16 | +10 | BTC | UP | 0.48 | open |  |
