# Range-Scalp Bot

*Updated Tue Oct 06 03:17 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4569 | 3942 | 627 (6) | 3 | $-1527.01 | -5.3% |
| **+10¢** | 3515 | 2787 | 728 (9) | 3 | $-1412.74 | -6.4% |
| **+15¢** | 2953 | 2184 | 769 (12) | 4 | $-1216.62 | -6.6% |
| **+20¢** | 2649 | 1849 | 800 (17) | 6 | $-1004.68 | -6.0% |
| **+10¢ (15¢ stop)** | 5616 | 5605 | 11 (6) | 3 | $-2049.56 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 03:16 | +10 stop | NEAR | UP | 0.69 | open |  |
| 10-06 03:16 | +20 | NEAR | UP | 0.70 | open |  |
| 10-06 03:16 | +15 | NEAR | UP | 0.70 | open |  |
| 10-06 03:16 | +10 | NEAR | UP | 0.70 | open |  |
| 10-06 03:16 | +5 | NEAR | UP | 0.70 | open |  |
| 10-06 03:16 | +10 stop | BTC | UP | 0.59 | open |  |
| 10-06 03:16 | +20 | BTC | UP | 0.59 | open |  |
| 10-06 03:16 | +15 | BTC | UP | 0.59 | open |  |
| 10-06 03:16 | +10 | BTC | UP | 0.59 | open |  |
| 10-06 03:16 | +5 | BTC | UP | 0.59 | open |  |
| 10-06 03:16 | +10 stop | BNB | UP | 0.64 | 0.76 | 0.90 |
| 10-06 03:16 | +20 | BNB | UP | 0.64 | open |  |
| 10-06 03:16 | +15 | BNB | UP | 0.64 | open |  |
| 10-06 03:16 | +10 | BNB | UP | 0.64 | 0.76 | 0.90 |
| 10-06 03:16 | +5 | BNB | UP | 0.64 | 0.76 | 0.90 |
| 10-06 03:16 | +10 stop | ETH | UP | 0.56 | open |  |
| 10-06 03:16 | +20 | ETH | UP | 0.56 | open |  |
| 10-06 03:16 | +15 | ETH | UP | 0.56 | open |  |
| 10-06 03:16 | +10 | ETH | UP | 0.56 | open |  |
| 10-06 03:16 | +5 | ETH | UP | 0.56 | open |  |
| 10-06 03:16 | +10 stop | SOL | UP | 0.60 | 0.73 | 0.99 |
| 10-06 03:16 | +20 | SOL | UP | 0.60 | open |  |
| 10-06 03:16 | +15 | SOL | UP | 0.60 | 0.77 | 1.40 |
| 10-06 03:16 | +10 | SOL | UP | 0.60 | 0.73 | 0.99 |
| 10-06 03:16 | +5 | SOL | UP | 0.60 | 0.65 | 0.17 |
| 10-06 03:16 | +10 stop | DOGE | UP | 0.58 | 0.76 | 1.49 |
| 10-06 03:16 | +20 | DOGE | UP | 0.58 | open |  |
| 10-06 03:16 | +15 | DOGE | UP | 0.58 | 0.76 | 1.49 |
| 10-06 03:16 | +10 | DOGE | UP | 0.58 | 0.76 | 1.49 |
| 10-06 03:16 | +5 | DOGE | UP | 0.58 | 0.76 | 1.49 |
| 10-06 03:14 | +10 stop | DOGE | DOWN | 0.50 | 1.00 | 4.78 |
| 10-06 03:13 | +10 stop | DOGE | UP | 0.39 | 0.62 | 1.96 |
| 10-06 03:12 | +10 stop | DOGE | DOWN | 0.62 | 0.33 | -3.23 |
| 10-06 03:11 | +10 stop | ZEC | UP | 0.47 | 0.24 | -2.61 |
| 10-06 03:11 | +5 | ZEC | UP | 0.47 | 0.56 | 0.54 |
| 10-06 03:10 | +5 | ZEC | UP | 0.41 | 0.53 | 0.85 |
| 10-06 03:10 | +10 stop | SOL | DOWN | 0.56 | 0.69 | 0.97 |
| 10-06 03:10 | +10 stop | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 10-06 03:10 | +15 | SOL | DOWN | 0.67 | 0.90 | 2.09 |
| 10-06 03:10 | +10 | SOL | DOWN | 0.67 | 0.79 | 0.92 |
