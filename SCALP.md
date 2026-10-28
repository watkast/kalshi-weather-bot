# Range-Scalp Bot

*Updated Wed Oct 28 04:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37572 | 32781 | 4791 (45) | 0 | $-10599.62 | -4.5% |
| **+10¢** | 28060 | 22518 | 5542 (67) | 0 | $-9443.81 | -5.3% |
| **+15¢** | 23473 | 17523 | 5950 (91) | 0 | $-8406.36 | -5.7% |
| **+20¢** | 20810 | 14581 | 6229 (116) | 0 | $-7391.09 | -5.7% |
| **+10¢ (15¢ stop)** | 46026 | 45961 | 65 (34) | 0 | $-17510.40 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 04:40 | +10 stop | BNB | DOWN | 0.51 | 0.74 | 1.98 |
| 10-28 04:39 | +10 stop | XRP | UP | 0.62 | 0.83 | 1.83 |
| 10-28 04:38 | +10 stop | XRP | UP | 0.58 | 0.43 | -1.86 |
| 10-28 04:38 | +20 | XRP | UP | 0.57 | 0.83 | 2.32 |
| 10-28 04:38 | +15 | XRP | UP | 0.57 | 0.83 | 2.32 |
| 10-28 04:38 | +10 | XRP | UP | 0.57 | 0.67 | 0.66 |
| 10-28 04:38 | +5 | XRP | UP | 0.57 | 0.67 | 0.66 |
| 10-28 04:37 | +10 stop | HYPE | UP | 0.66 | 0.77 | 0.81 |
| 10-28 04:37 | +20 | HYPE | UP | 0.66 | 0.92 | 2.38 |
| 10-28 04:37 | +15 | HYPE | UP | 0.66 | 0.92 | 2.38 |
| 10-28 04:37 | +10 | HYPE | UP | 0.66 | 0.77 | 0.81 |
| 10-28 04:37 | +5 | HYPE | UP | 0.66 | 0.73 | 0.40 |
| 10-28 04:36 | +10 stop | BNB | DOWN | 0.52 | 0.66 | 1.06 |
| 10-28 04:35 | +10 stop | ZEC | UP | 0.67 | 0.44 | -2.64 |
| 10-28 04:35 | +20 | ZEC | UP | 0.68 | no | -6.96 |
| 10-28 04:35 | +15 | ZEC | UP | 0.67 | no | -6.86 |
| 10-28 04:35 | +10 | ZEC | UP | 0.68 | no | -6.96 |
| 10-28 04:35 | +5 | ZEC | UP | 0.68 | no | -6.96 |
| 10-28 04:35 | +10 stop | DOGE | UP | 0.66 | 0.79 | 1.02 |
| 10-28 04:35 | +10 | DOGE | UP | 0.66 | 0.79 | 1.02 |
| 10-28 04:35 | +5 | DOGE | UP | 0.66 | 0.73 | 0.40 |
| 10-28 04:33 | +10 stop | BNB | UP | 0.66 | 0.49 | -2.04 |
| 10-28 04:33 | +10 | BNB | UP | 0.66 | no | -6.76 |
| 10-28 04:33 | +5 | BNB | UP | 0.66 | no | -6.76 |
| 10-28 04:31 | +10 stop | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 10-28 04:31 | +20 | DOGE | UP | 0.68 | 0.89 | 1.87 |
| 10-28 04:31 | +15 | DOGE | UP | 0.68 | 0.87 | 1.66 |
| 10-28 04:31 | +10 | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 10-28 04:31 | +5 | DOGE | UP | 0.68 | 0.74 | 0.30 |
| 10-28 04:31 | +10 stop | BNB | UP | 0.69 | 0.80 | 0.83 |
| 10-28 04:31 | +20 | BNB | UP | 0.69 | no | -7.05 |
| 10-28 04:31 | +15 | BNB | UP | 0.69 | no | -7.05 |
| 10-28 04:31 | +10 | BNB | UP | 0.69 | 0.80 | 0.83 |
| 10-28 04:31 | +5 | BNB | UP | 0.69 | 0.75 | 0.31 |
| 10-28 04:26 | +10 stop | NEAR | UP | 0.60 | 0.26 | -3.71 |
| 10-28 04:23 | +5 | HYPE | DOWN | 0.57 | yes | -5.88 |
| 10-28 04:23 | +10 stop | HYPE | DOWN | 0.56 | 0.21 | -3.80 |
| 10-28 04:23 | +10 stop | BNB | DOWN | 0.55 | 0.21 | -3.70 |
| 10-28 04:23 | +5 | HYPE | DOWN | 0.57 | 0.64 | 0.35 |
| 10-28 04:22 | +10 stop | HYPE | UP | 0.53 | 0.34 | -2.24 |
