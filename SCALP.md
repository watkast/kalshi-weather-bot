# Range-Scalp Bot

*Updated Tue Oct 27 01:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35795 | 31246 | 4549 (43) | 4 | $-9970.38 | -4.4% |
| **+10¢** | 26758 | 21495 | 5263 (65) | 3 | $-8809.98 | -5.2% |
| **+15¢** | 22394 | 16735 | 5659 (89) | 2 | $-7860.66 | -5.6% |
| **+20¢** | 19850 | 13920 | 5930 (112) | 1 | $-6917.11 | -5.5% |
| **+10¢ (15¢ stop)** | 43871 | 43808 | 63 (33) | 0 | $-16689.89 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 01:40 | +10 | BTC | UP | 0.70 | 0.87 | 1.47 |
| 10-27 01:40 | +5 | BTC | UP | 0.71 | 0.87 | 1.37 |
| 10-27 01:40 | +10 stop | BTC | UP | 0.71 | 0.50 | -2.43 |
| 10-27 01:40 | +10 stop | BNB | UP | 0.69 | 0.83 | 1.11 |
| 10-27 01:40 | +20 | BNB | UP | 0.69 | 0.91 | 1.97 |
| 10-27 01:40 | +15 | BNB | UP | 0.69 | 0.85 | 1.36 |
| 10-27 01:40 | +10 stop | XRP | UP | 0.67 | 0.77 | 0.71 |
| 10-27 01:38 | +10 stop | BTC | UP | 0.60 | 0.77 | 1.40 |
| 10-27 01:38 | +5 | BTC | UP | 0.60 | 0.67 | 0.37 |
| 10-27 01:38 | +10 stop | BNB | DOWN | 0.60 | 0.35 | -2.83 |
| 10-27 01:38 | +10 | BNB | DOWN | 0.60 | open |  |
| 10-27 01:38 | +5 | BNB | DOWN | 0.60 | open |  |
| 10-27 01:37 | +10 | ETH | UP | 0.57 | 0.77 | 1.69 |
| 10-27 01:37 | +10 stop | HYPE | UP | 0.64 | 0.84 | 1.73 |
| 10-27 01:37 | +10 | HYPE | UP | 0.64 | 0.84 | 1.73 |
| 10-27 01:37 | +5 | HYPE | UP | 0.64 | 0.84 | 1.73 |
| 10-27 01:37 | +10 stop | BNB | UP | 0.42 | 0.57 | 1.14 |
| 10-27 01:37 | +20 | BNB | UP | 0.42 | 0.64 | 1.85 |
| 10-27 01:37 | +15 | BNB | UP | 0.44 | 0.64 | 1.65 |
| 10-27 01:37 | +10 | BNB | UP | 0.44 | 0.57 | 0.94 |
| 10-27 01:37 | +5 | BNB | UP | 0.47 | 0.57 | 0.64 |
| 10-27 01:37 | +10 stop | XRP | UP | 0.50 | 0.68 | 1.46 |
| 10-27 01:37 | +5 | ETH | UP | 0.66 | 0.77 | 0.81 |
| 10-27 01:37 | +10 stop | ETH | UP | 0.69 | 0.48 | -2.43 |
| 10-27 01:36 | +10 stop | SOL | UP | 0.70 | 0.52 | -2.13 |
| 10-27 01:36 | +10 stop | SOL | UP | 0.48 | 0.58 | 0.64 |
| 10-27 01:36 | +10 stop | BTC | UP | 0.51 | 0.66 | 1.16 |
| 10-27 01:36 | +10 stop | ETH | UP | 0.44 | 0.56 | 0.84 |
| 10-27 01:36 | +10 stop | HYPE | UP | 0.60 | 0.74 | 1.09 |
| 10-27 01:36 | +10 stop | XRP | UP | 0.61 | 0.74 | 0.96 |
| 10-27 01:35 | +10 stop | BTC | DOWN | 0.56 | 0.66 | 0.66 |
| 10-27 01:34 | +10 stop | DOGE | DOWN | 0.57 | 0.25 | -3.52 |
| 10-27 01:34 | +10 stop | XRP | DOWN | 0.66 | 0.41 | -2.83 |
| 10-27 01:34 | +10 | XRP | DOWN | 0.66 | open |  |
| 10-27 01:34 | +10 stop | NEAR | UP | 0.63 | 0.73 | 0.69 |
| 10-27 01:34 | +10 | NEAR | UP | 0.63 | 0.73 | 0.69 |
| 10-27 01:34 | +5 | NEAR | UP | 0.63 | 0.72 | 0.58 |
| 10-27 01:33 | +10 stop | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-27 01:33 | +10 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-27 01:33 | +10 | DOGE | DOWN | 0.69 | open |  |
