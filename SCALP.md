# Range-Scalp Bot

*Updated Tue Oct 20 17:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25931 | 22586 | 3345 (32) | 2 | $-7548.53 | -4.6% |
| **+10¢** | 19519 | 15656 | 3863 (47) | 5 | $-6655.14 | -5.4% |
| **+15¢** | 16340 | 12182 | 4158 (71) | 4 | $-5935.82 | -5.8% |
| **+20¢** | 14454 | 10097 | 4357 (89) | 4 | $-5322.72 | -5.9% |
| **+10¢ (15¢ stop)** | 31794 | 31741 | 53 (30) | 0 | $-11682.73 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 17:14 | +10 stop | BTC | UP | 0.71 | 0.23 | -5.08 |
| 10-20 17:12 | +10 stop | BNB | DOWN | 0.67 | 0.82 | 1.23 |
| 10-20 17:12 | +10 stop | HYPE | UP | 0.55 | 0.34 | -2.48 |
| 10-20 17:12 | +10 stop | XRP | DOWN | 0.45 | 0.20 | -2.80 |
| 10-20 17:12 | +5 | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 10-20 17:11 | +10 stop | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 10-20 17:11 | +5 | SOL | DOWN | 0.65 | 0.70 | 0.19 |
| 10-20 17:11 | +10 stop | HYPE | UP | 0.70 | 0.55 | -1.83 |
| 10-20 17:11 | +5 | HYPE | UP | 0.70 | 0.91 | 1.90 |
| 10-20 17:11 | +10 stop | BTC | UP | 0.69 | 0.49 | -2.33 |
| 10-20 17:11 | +10 stop | ETH | DOWN | 0.63 | 0.78 | 1.20 |
| 10-20 17:11 | +10 | ETH | DOWN | 0.63 | 0.78 | 1.20 |
| 10-20 17:11 | +5 | ETH | DOWN | 0.65 | 0.70 | 0.19 |
| 10-20 17:11 | +10 stop | DOGE | DOWN | 0.66 | 0.83 | 1.44 |
| 10-20 17:11 | +10 | DOGE | DOWN | 0.66 | 0.83 | 1.44 |
| 10-20 17:11 | +5 | DOGE | DOWN | 0.65 | 0.83 | 1.54 |
| 10-20 17:11 | +15 | DOGE | DOWN | 0.64 | 0.83 | 1.63 |
| 10-20 17:10 | +10 stop | XRP | DOWN | 0.55 | 0.38 | -2.05 |
| 10-20 17:10 | +10 stop | BNB | UP | 0.69 | 0.52 | -2.03 |
| 10-20 17:10 | +10 stop | DOGE | DOWN | 0.56 | 0.67 | 0.76 |
| 10-20 17:10 | +10 | DOGE | DOWN | 0.56 | 0.67 | 0.76 |
| 10-20 17:10 | +5 | DOGE | DOWN | 0.56 | 0.67 | 0.76 |
| 10-20 17:10 | +10 stop | HYPE | UP | 0.40 | 0.59 | 1.56 |
| 10-20 17:10 | +5 | HYPE | UP | 0.40 | 0.59 | 1.56 |
| 10-20 17:09 | +10 stop | ETH | UP | 0.55 | 0.70 | 1.17 |
| 10-20 17:09 | +5 | ETH | UP | 0.55 | 0.70 | 1.17 |
| 10-20 17:08 | +5 | SOL | UP | 0.60 | 0.66 | 0.27 |
| 10-20 17:08 | +10 stop | NEAR | UP | 0.47 | 0.58 | 0.71 |
| 10-20 17:08 | +10 stop | DOGE | UP | 0.56 | 0.70 | 1.07 |
| 10-20 17:08 | +10 | DOGE | UP | 0.56 | 0.70 | 1.07 |
| 10-20 17:08 | +5 | DOGE | UP | 0.55 | 0.64 | 0.55 |
| 10-20 17:07 | +10 stop | BTC | UP | 0.71 | 0.82 | 0.84 |
| 10-20 17:07 | +10 stop | SOL | UP | 0.63 | 0.45 | -2.15 |
| 10-20 17:07 | +10 | SOL | UP | 0.63 | open |  |
| 10-20 17:07 | +5 | SOL | UP | 0.60 | 0.65 | 0.17 |
| 10-20 17:07 | +5 | ETH | UP | 0.66 | 0.71 | 0.19 |
| 10-20 17:06 | +10 stop | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 10-20 17:06 | +5 | HYPE | UP | 0.67 | 0.72 | 0.19 |
| 10-20 17:06 | +10 stop | ETH | DOWN | 0.54 | 0.32 | -2.54 |
| 10-20 17:06 | +10 | ETH | DOWN | 0.54 | 0.70 | 1.27 |
