# Range-Scalp Bot

*Updated Tue Oct 06 02:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4544 | 3919 | 625 (6) | 0 | $-1524.68 | -5.3% |
| **+10¢** | 3497 | 2773 | 724 (9) | 0 | $-1401.53 | -6.4% |
| **+15¢** | 2935 | 2170 | 765 (12) | 1 | $-1211.09 | -6.6% |
| **+20¢** | 2634 | 1838 | 796 (17) | 1 | $-998.48 | -6.0% |
| **+10¢ (15¢ stop)** | 5584 | 5573 | 11 (6) | 0 | $-2044.86 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 02:56 | +10 stop | HYPE | DOWN | 0.66 | 0.76 | 0.74 |
| 10-06 02:54 | +10 stop | HYPE | UP | 0.53 | 0.34 | -2.24 |
| 10-06 02:54 | +10 stop | ZEC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-06 02:52 | +10 stop | ZEC | UP | 0.63 | 0.37 | -2.94 |
| 10-06 02:52 | +10 stop | HYPE | DOWN | 0.65 | 0.46 | -2.28 |
| 10-06 02:50 | +10 stop | ZEC | UP | 0.51 | 0.63 | 0.86 |
| 10-06 02:50 | +5 | BTC | DOWN | 0.71 | 0.78 | 0.42 |
| 10-06 02:50 | +10 stop | XRP | DOWN | 0.67 | 0.77 | 0.71 |
| 10-06 02:50 | +20 | XRP | DOWN | 0.67 | 0.87 | 1.76 |
| 10-06 02:50 | +15 | XRP | DOWN | 0.67 | 0.83 | 1.34 |
| 10-06 02:50 | +10 | XRP | DOWN | 0.67 | 0.77 | 0.71 |
| 10-06 02:50 | +5 | XRP | DOWN | 0.67 | 0.75 | 0.50 |
| 10-06 02:49 | +5 | HYPE | DOWN | 0.69 | 0.76 | 0.42 |
| 10-06 02:49 | +10 stop | ZEC | DOWN | 0.67 | 0.49 | -2.13 |
| 10-06 02:49 | +20 | ZEC | DOWN | 0.67 | 0.92 | 2.24 |
| 10-06 02:49 | +15 | ZEC | DOWN | 0.66 | 0.82 | 1.33 |
| 10-06 02:49 | +10 | ZEC | DOWN | 0.64 | 0.76 | 0.90 |
| 10-06 02:49 | +5 | ZEC | DOWN | 0.64 | 0.76 | 0.90 |
| 10-06 02:46 | +10 stop | HYPE | DOWN | 0.69 | 0.51 | -2.17 |
| 10-06 02:46 | +20 | HYPE | DOWN | 0.69 | open |  |
| 10-06 02:46 | +15 | HYPE | DOWN | 0.68 | open |  |
| 10-06 02:46 | +10 | HYPE | DOWN | 0.68 | 0.81 | 0.99 |
| 10-06 02:46 | +5 | HYPE | DOWN | 0.68 | 0.74 | 0.26 |
| 10-06 02:43 | +10 stop | XRP | DOWN | 0.62 | 0.38 | -2.74 |
| 10-06 02:42 | +5 | BTC | UP | 0.46 | 0.60 | 1.05 |
| 10-06 02:41 | +10 stop | XRP | UP | 0.60 | 0.31 | -3.22 |
| 10-06 02:41 | +10 stop | BTC | UP | 0.55 | 0.35 | -2.34 |
| 10-06 02:41 | +5 | BTC | UP | 0.55 | 0.64 | 0.55 |
| 10-06 02:40 | +10 stop | NEAR | UP | 0.70 | 0.87 | 1.42 |
| 10-06 02:40 | +10 stop | DOGE | DOWN | 0.56 | 0.81 | 2.21 |
| 10-06 02:40 | +10 stop | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 10-06 02:39 | +10 | NEAR | UP | 0.55 | 0.80 | 2.20 |
| 10-06 02:39 | +10 stop | BTC | UP | 0.62 | 0.73 | 0.79 |
| 10-06 02:39 | +5 | BTC | UP | 0.62 | 0.73 | 0.79 |
| 10-06 02:39 | +10 stop | NEAR | UP | 0.69 | 0.51 | -2.13 |
| 10-06 02:39 | +5 | DOGE | DOWN | 0.64 | 0.81 | 1.42 |
| 10-06 02:38 | +10 stop | DOGE | DOWN | 0.65 | 0.48 | -2.04 |
| 10-06 02:38 | +20 | DOGE | DOWN | 0.65 | 0.87 | 1.96 |
| 10-06 02:38 | +15 | DOGE | DOWN | 0.65 | 0.81 | 1.33 |
| 10-06 02:38 | +10 | DOGE | DOWN | 0.65 | 0.81 | 1.33 |
