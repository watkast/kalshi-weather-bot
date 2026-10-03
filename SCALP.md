# Range-Scalp Bot

*Updated Sat Oct 03 20:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 1233 | 1075 | 158 (2) | 0 | $-360.05 | -4.6% |
| **+10¢** | 938 | 767 | 171 (4) | 0 | $-191.18 | -3.2% |
| **+15¢** | 792 | 607 | 185 (5) | 0 | $-157.09 | -3.2% |
| **+20¢** | 696 | 495 | 201 (6) | 1 | $-191.27 | -4.4% |
| **+10¢ (15¢ stop)** | 1545 | 1544 | 1 (1) | 0 | $-674.27 | -7.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 20:03 | +5 | BNB | UP | 0.71 | 0.79 | 0.53 |
| 10-03 20:02 | +10 stop | BNB | UP | 0.67 | 0.51 | -1.89 |
| 10-03 20:02 | +20 | BNB | UP | 0.67 | open |  |
| 10-03 20:02 | +15 | BNB | UP | 0.67 | 0.82 | 1.28 |
| 10-03 20:02 | +10 | BNB | UP | 0.67 | 0.79 | 0.97 |
| 10-03 20:02 | +5 | BNB | UP | 0.67 | 0.72 | 0.24 |
| 10-03 20:01 | +10 stop | HYPE | UP | 0.66 | 0.89 | 2.07 |
| 10-03 20:01 | +20 | HYPE | UP | 0.66 | 0.89 | 2.07 |
| 10-03 20:01 | +15 | HYPE | UP | 0.66 | 0.89 | 2.07 |
| 10-03 20:01 | +10 | HYPE | UP | 0.66 | 0.89 | 2.07 |
| 10-03 20:01 | +5 | HYPE | UP | 0.66 | 0.72 | 0.29 |
| 10-03 20:01 | +10 stop | BTC | UP | 0.68 | 0.78 | 0.71 |
| 10-03 20:01 | +20 | BTC | UP | 0.68 | 0.89 | 1.87 |
| 10-03 20:01 | +15 | BTC | UP | 0.68 | 0.84 | 1.34 |
| 10-03 20:01 | +10 | BTC | UP | 0.68 | 0.78 | 0.71 |
| 10-03 20:01 | +5 | BTC | UP | 0.68 | 0.78 | 0.71 |
| 10-03 20:01 | +10 stop | ETH | UP | 0.58 | 0.73 | 1.18 |
| 10-03 20:01 | +20 | ETH | UP | 0.58 | 0.80 | 1.90 |
| 10-03 20:01 | +15 | ETH | UP | 0.58 | 0.73 | 1.18 |
| 10-03 20:01 | +10 | ETH | UP | 0.58 | 0.73 | 1.18 |
| 10-03 20:01 | +5 | ETH | UP | 0.58 | 0.65 | 0.36 |
| 10-03 19:56 | +10 stop | XRP | DOWN | 0.61 | 0.40 | -2.44 |
| 10-03 19:56 | +10 stop | XRP | UP | 0.63 | 0.44 | -2.25 |
| 10-03 19:55 | +5 | NEAR | DOWN | 0.71 | 0.76 | 0.22 |
| 10-03 19:54 | +10 stop | BTC | DOWN | 0.50 | 0.08 | -4.42 |
| 10-03 19:53 | +10 stop | ETH | UP | 0.71 | 0.92 | 1.90 |
| 10-03 19:53 | +5 | DOGE | DOWN | 0.68 | 0.76 | 0.51 |
| 10-03 19:52 | +10 stop | BTC | DOWN | 0.66 | 0.51 | -1.84 |
| 10-03 19:52 | +15 | BTC | DOWN | 0.66 | yes | -6.76 |
| 10-03 19:52 | +10 | BTC | DOWN | 0.66 | yes | -6.76 |
| 10-03 19:52 | +5 | BTC | DOWN | 0.66 | yes | -6.76 |
| 10-03 19:52 | +10 stop | XRP | DOWN | 0.70 | 0.34 | -3.91 |
| 10-03 19:52 | +10 | XRP | DOWN | 0.69 | 0.84 | 1.25 |
| 10-03 19:52 | +5 | XRP | DOWN | 0.69 | 0.84 | 1.25 |
| 10-03 19:51 | +10 stop | DOGE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-03 19:51 | +10 stop | BNB | UP | 0.62 | 0.74 | 0.89 |
| 10-03 19:51 | +10 stop | HYPE | UP | 0.61 | 0.72 | 0.78 |
| 10-03 19:51 | +10 stop | SOL | UP | 0.58 | 0.25 | -3.62 |
| 10-03 19:50 | +5 | DOGE | DOWN | 0.59 | 0.66 | 0.37 |
| 10-03 19:50 | +10 stop | ETH | DOWN | 0.56 | 0.41 | -1.85 |
