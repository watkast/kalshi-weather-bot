# Range-Scalp Bot

*Updated Mon Oct 05 06:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3401 | 2916 | 485 (3) | 1 | $-1255.85 | -5.8% |
| **+10¢** | 2630 | 2077 | 553 (4) | 1 | $-1132.58 | -6.8% |
| **+15¢** | 2211 | 1624 | 587 (6) | 1 | $-1033.98 | -7.5% |
| **+20¢** | 1972 | 1359 | 613 (11) | 1 | $-908.54 | -7.3% |
| **+10¢ (15¢ stop)** | 4221 | 4220 | 1 (1) | 1 | $-1635.69 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 06:13 | +10 stop | NEAR | UP | 0.64 | open |  |
| 10-05 06:13 | +20 | NEAR | UP | 0.64 | open |  |
| 10-05 06:13 | +15 | NEAR | UP | 0.64 | open |  |
| 10-05 06:13 | +10 | NEAR | UP | 0.64 | open |  |
| 10-05 06:13 | +5 | NEAR | UP | 0.64 | open |  |
| 10-05 06:09 | +10 stop | BNB | UP | 0.54 | 0.39 | -1.85 |
| 10-05 06:09 | +10 | BNB | UP | 0.57 | 0.73 | 1.28 |
| 10-05 06:09 | +5 | BNB | UP | 0.57 | 0.62 | 0.15 |
| 10-05 06:06 | +10 stop | BNB | UP | 0.67 | 0.77 | 0.71 |
| 10-05 06:06 | +20 | BNB | UP | 0.67 | 0.89 | 1.97 |
| 10-05 06:06 | +15 | BNB | UP | 0.67 | 0.85 | 1.55 |
| 10-05 06:06 | +10 | BNB | UP | 0.67 | 0.77 | 0.71 |
| 10-05 06:06 | +5 | BNB | UP | 0.67 | 0.72 | 0.19 |
| 10-05 06:01 | +10 stop | NEAR | UP | 0.64 | 0.74 | 0.69 |
| 10-05 06:01 | +20 | NEAR | UP | 0.64 | 0.85 | 1.84 |
| 10-05 06:01 | +15 | NEAR | UP | 0.64 | 0.79 | 1.21 |
| 10-05 06:01 | +10 | NEAR | UP | 0.64 | 0.74 | 0.69 |
| 10-05 06:01 | +5 | NEAR | UP | 0.64 | 0.74 | 0.69 |
| 10-05 06:01 | +10 stop | BTC | UP | 0.68 | 0.78 | 0.71 |
| 10-05 06:01 | +20 | BTC | UP | 0.68 | 0.88 | 1.76 |
| 10-05 06:01 | +15 | BTC | UP | 0.68 | 0.84 | 1.34 |
| 10-05 06:01 | +10 | BTC | UP | 0.70 | 0.84 | 1.15 |
| 10-05 06:01 | +5 | BTC | UP | 0.70 | 0.76 | 0.32 |
| 10-05 05:59 | +10 stop | BTC | UP | 0.70 | 0.94 | 2.19 |
| 10-05 05:59 | +10 stop | DOGE | DOWN | 0.53 | 0.68 | 1.16 |
| 10-05 05:58 | +10 stop | BTC | DOWN | 0.30 | 0.55 | 2.17 |
| 10-05 05:57 | +10 stop | DOGE | DOWN | 0.66 | 0.44 | -2.54 |
| 10-05 05:57 | +15 | DOGE | DOWN | 0.70 | no | 2.85 |
| 10-05 05:57 | +10 | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 10-05 05:57 | +5 | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 10-05 05:57 | +10 stop | BTC | UP | 0.70 | 0.37 | -3.62 |
| 10-05 05:56 | +5 | BNB | DOWN | 0.43 | 0.59 | 1.25 |
| 10-05 05:56 | +5 | BNB | DOWN | 0.51 | 0.63 | 0.85 |
| 10-05 05:54 | +10 stop | BNB | DOWN | 0.62 | 0.46 | -1.95 |
| 10-05 05:54 | +10 | BNB | DOWN | 0.62 | yes | -6.37 |
| 10-05 05:54 | +5 | BNB | DOWN | 0.62 | 0.67 | 0.17 |
| 10-05 05:53 | +10 stop | BTC | DOWN | 0.63 | 0.46 | -2.05 |
| 10-05 05:52 | +10 stop | BTC | UP | 0.53 | 0.38 | -1.85 |
| 10-05 05:51 | +10 stop | DOGE | UP | 0.52 | 0.37 | -1.85 |
| 10-05 05:50 | +10 stop | SOL | DOWN | 0.71 | 0.83 | 0.95 |
