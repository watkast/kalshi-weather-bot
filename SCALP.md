# Range-Scalp Bot

*Updated Sat Oct 03 23:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 1465 | 1275 | 190 (2) | 3 | $-422.96 | -4.6% |
| **+10¢** | 1124 | 915 | 209 (4) | 4 | $-252.48 | -3.6% |
| **+15¢** | 947 | 722 | 225 (5) | 4 | $-214.41 | -3.6% |
| **+20¢** | 836 | 592 | 244 (7) | 4 | $-242.71 | -4.6% |
| **+10¢ (15¢ stop)** | 1835 | 1834 | 1 (1) | 0 | $-753.07 | -6.5% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 23:58 | +10 stop | XRP | DOWN | 0.64 | 0.86 | 1.94 |
| 10-03 23:58 | +15 | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 10-03 23:58 | +10 | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 10-03 23:58 | +5 | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 10-03 23:57 | +10 stop | ZEC | UP | 0.71 | 0.93 | 1.99 |
| 10-03 23:57 | +20 | ZEC | UP | 0.71 | 0.93 | 1.99 |
| 10-03 23:57 | +15 | ZEC | UP | 0.71 | 0.93 | 1.99 |
| 10-03 23:57 | +10 | ZEC | UP | 0.71 | 0.93 | 1.99 |
| 10-03 23:57 | +5 | ZEC | UP | 0.71 | 0.79 | 0.53 |
| 10-03 23:57 | +10 stop | ETH | DOWN | 0.42 | 0.58 | 1.24 |
| 10-03 23:57 | +20 | ETH | DOWN | 0.42 | 0.70 | 2.47 |
| 10-03 23:57 | +15 | ETH | DOWN | 0.41 | 0.58 | 1.35 |
| 10-03 23:57 | +10 | ETH | DOWN | 0.41 | 0.58 | 1.35 |
| 10-03 23:57 | +5 | ETH | DOWN | 0.41 | 0.58 | 1.35 |
| 10-03 23:57 | +10 stop | XRP | DOWN | 0.40 | 0.57 | 1.35 |
| 10-03 23:57 | +20 | XRP | DOWN | 0.40 | 0.86 | 4.34 |
| 10-03 23:57 | +15 | XRP | DOWN | 0.40 | 0.57 | 1.35 |
| 10-03 23:57 | +10 | XRP | DOWN | 0.40 | 0.57 | 1.35 |
| 10-03 23:57 | +5 | XRP | DOWN | 0.40 | 0.57 | 1.35 |
| 10-03 23:57 | +10 stop | BNB | UP | 0.61 | 0.41 | -2.34 |
| 10-03 23:57 | +15 | BNB | UP | 0.61 | open |  |
| 10-03 23:57 | +10 | BNB | UP | 0.61 | open |  |
| 10-03 23:57 | +5 | BNB | UP | 0.61 | 0.69 | 0.48 |
| 10-03 23:54 | +10 stop | ZEC | DOWN | 0.58 | 0.86 | 2.52 |
| 10-03 23:53 | +10 stop | BNB | DOWN | 0.53 | 0.71 | 1.47 |
| 10-03 23:53 | +10 stop | DOGE | DOWN | 0.59 | 0.75 | 1.29 |
| 10-03 23:52 | +10 stop | XRP | UP | 0.57 | 0.40 | -2.05 |
| 10-03 23:51 | +10 stop | DOGE | UP | 0.58 | 0.43 | -1.86 |
| 10-03 23:51 | +10 stop | ETH | DOWN | 0.59 | 0.81 | 1.92 |
| 10-03 23:51 | +20 | ETH | DOWN | 0.59 | 0.81 | 1.92 |
| 10-03 23:51 | +15 | ETH | DOWN | 0.59 | 0.81 | 1.92 |
| 10-03 23:51 | +10 | ETH | DOWN | 0.59 | 0.81 | 1.92 |
| 10-03 23:51 | +5 | ETH | DOWN | 0.59 | 0.64 | 0.16 |
| 10-03 23:51 | +15 | DOGE | UP | 0.57 | open |  |
| 10-03 23:51 | +10 stop | NEAR | UP | 0.68 | 0.85 | 1.45 |
| 10-03 23:51 | +10 stop | SOL | UP | 0.57 | 0.34 | -2.63 |
| 10-03 23:51 | +10 stop | BNB | DOWN | 0.61 | 0.42 | -2.27 |
| 10-03 23:51 | +5 | BNB | DOWN | 0.61 | 0.71 | 0.66 |
| 10-03 23:50 | +10 stop | ZEC | UP | 0.60 | 0.44 | -1.96 |
| 10-03 23:50 | +10 stop | XRP | UP | 0.63 | 0.74 | 0.79 |
