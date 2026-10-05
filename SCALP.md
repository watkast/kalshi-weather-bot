# Range-Scalp Bot

*Updated Mon Oct 05 06:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3399 | 2914 | 485 (3) | 0 | $-1256.19 | -5.9% |
| **+10¢** | 2628 | 2075 | 553 (4) | 0 | $-1134.57 | -6.9% |
| **+15¢** | 2210 | 1623 | 587 (6) | 0 | $-1035.53 | -7.5% |
| **+20¢** | 1970 | 1357 | 613 (11) | 1 | $-912.35 | -7.4% |
| **+10¢ (15¢ stop)** | 4219 | 4218 | 1 (1) | 0 | $-1634.55 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 06:01 | +10 stop | NEAR | UP | 0.64 | 0.74 | 0.69 |
| 10-05 06:01 | +20 | NEAR | UP | 0.64 | open |  |
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
| 10-05 05:50 | +15 | SOL | DOWN | 0.68 | 0.83 | 1.24 |
| 10-05 05:50 | +10 | SOL | DOWN | 0.68 | 0.83 | 1.24 |
| 10-05 05:50 | +5 | SOL | DOWN | 0.68 | 0.74 | 0.30 |
| 10-05 05:50 | +10 stop | BNB | DOWN | 0.59 | 0.70 | 0.78 |
| 10-05 05:50 | +10 | BNB | DOWN | 0.59 | 0.70 | 0.78 |
| 10-05 05:50 | +5 | BNB | DOWN | 0.59 | 0.70 | 0.78 |
| 10-05 05:49 | +10 stop | XRP | DOWN | 0.62 | 0.78 | 1.30 |
| 10-05 05:49 | +10 | XRP | DOWN | 0.62 | 0.78 | 1.30 |
| 10-05 05:49 | +10 stop | ETH | DOWN | 0.67 | 0.50 | -2.04 |
| 10-05 05:49 | +10 | ETH | DOWN | 0.67 | yes | -6.86 |
| 10-05 05:48 | +5 | ETH | DOWN | 0.71 | yes | -7.25 |
| 10-05 05:47 | +5 | BTC | DOWN | 0.66 | yes | -6.76 |
| 10-05 05:47 | +5 | XRP | DOWN | 0.66 | 0.78 | 0.91 |
