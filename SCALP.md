# Range-Scalp Bot

*Updated Sun Oct 04 01:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 1553 | 1344 | 209 (2) | 0 | $-501.41 | -5.1% |
| **+10¢** | 1191 | 958 | 233 (4) | 1 | $-356.62 | -4.7% |
| **+15¢** | 1007 | 758 | 249 (5) | 1 | $-310.61 | -4.9% |
| **+20¢** | 891 | 623 | 268 (7) | 1 | $-329.68 | -5.9% |
| **+10¢ (15¢ stop)** | 1947 | 1946 | 1 (1) | 1 | $-826.48 | -6.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 01:16 | +10 stop | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-04 01:16 | +20 | ZEC | DOWN | 0.66 | 0.91 | 2.27 |
| 10-04 01:16 | +15 | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-04 01:16 | +10 | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-04 01:16 | +5 | ZEC | DOWN | 0.66 | 0.72 | 0.29 |
| 10-04 01:16 | +10 stop | BTC | DOWN | 0.69 | open |  |
| 10-04 01:16 | +20 | BTC | DOWN | 0.69 | open |  |
| 10-04 01:16 | +15 | BTC | DOWN | 0.69 | open |  |
| 10-04 01:16 | +10 | BTC | DOWN | 0.69 | open |  |
| 10-04 01:16 | +5 | BTC | DOWN | 0.69 | 0.75 | 0.31 |
| 10-04 01:12 | +10 stop | BTC | UP | 0.62 | 0.74 | 0.89 |
| 10-04 01:12 | +20 | BTC | UP | 0.62 | no | -6.37 |
| 10-04 01:12 | +15 | BTC | UP | 0.62 | no | -6.37 |
| 10-04 01:12 | +10 | BTC | UP | 0.62 | 0.74 | 0.89 |
| 10-04 01:12 | +5 | BTC | UP | 0.62 | 0.74 | 0.89 |
| 10-04 01:11 | +10 stop | NEAR | DOWN | 0.57 | 0.74 | 1.38 |
| 10-04 01:11 | +10 stop | ZEC | UP | 0.57 | 0.24 | -3.63 |
| 10-04 01:10 | +10 stop | ZEC | DOWN | 0.62 | 0.42 | -2.35 |
| 10-04 01:10 | +20 | ZEC | DOWN | 0.62 | 0.89 | 2.46 |
| 10-04 01:10 | +15 | ZEC | DOWN | 0.62 | 0.89 | 2.46 |
| 10-04 01:10 | +10 | ZEC | DOWN | 0.62 | 0.75 | 0.99 |
| 10-04 01:10 | +5 | ZEC | DOWN | 0.62 | 0.75 | 0.99 |
| 10-04 01:08 | +10 stop | SOL | UP | 0.67 | 0.51 | -1.94 |
| 10-04 01:08 | +20 | SOL | UP | 0.67 | 0.89 | 1.97 |
| 10-04 01:08 | +15 | SOL | UP | 0.67 | 0.86 | 1.65 |
| 10-04 01:08 | +10 | SOL | UP | 0.67 | 0.86 | 1.65 |
| 10-04 01:08 | +5 | SOL | UP | 0.67 | 0.86 | 1.65 |
| 10-04 01:08 | +10 stop | ETH | UP | 0.62 | 0.84 | 1.93 |
| 10-04 01:07 | +10 stop | DOGE | DOWN | 0.66 | 0.17 | -5.16 |
| 10-04 01:07 | +10 stop | BTC | DOWN | 0.58 | 0.30 | -3.13 |
| 10-04 01:07 | +5 | BTC | DOWN | 0.58 | 0.64 | 0.25 |
| 10-04 01:07 | +10 | HYPE | UP | 0.64 | 0.76 | 0.90 |
| 10-04 01:07 | +5 | HYPE | UP | 0.63 | 0.71 | 0.48 |
| 10-04 01:07 | +10 stop | XRP | DOWN | 0.62 | 0.80 | 1.53 |
| 10-04 01:07 | +10 | XRP | DOWN | 0.62 | 0.80 | 1.52 |
| 10-04 01:07 | +5 | XRP | DOWN | 0.62 | 0.70 | 0.49 |
| 10-04 01:07 | +10 stop | DOGE | UP | 0.63 | 0.36 | -3.02 |
| 10-04 01:07 | +15 | DOGE | UP | 0.62 | 0.82 | 1.72 |
| 10-04 01:07 | +10 | DOGE | UP | 0.63 | 0.82 | 1.64 |
| 10-04 01:07 | +5 | DOGE | UP | 0.62 | 0.82 | 1.72 |
