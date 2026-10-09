# Range-Scalp Bot

*Updated Fri Oct 09 23:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9613 | 8304 | 1309 (18) | 3 | $-3199.20 | -5.3% |
| **+10¢** | 7255 | 5721 | 1534 (30) | 3 | $-3105.21 | -6.8% |
| **+15¢** | 6118 | 4500 | 1618 (43) | 3 | $-2569.52 | -6.7% |
| **+20¢** | 5450 | 3769 | 1681 (55) | 3 | $-2117.88 | -6.2% |
| **+10¢ (15¢ stop)** | 11756 | 11721 | 35 (22) | 0 | $-4492.11 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 23:28 | +10 stop | BTC | DOWN | 0.70 | 0.87 | 1.47 |
| 10-09 23:28 | +10 stop | HYPE | UP | 0.68 | 0.52 | -1.94 |
| 10-09 23:27 | +10 stop | ZEC | DOWN | 0.68 | 0.53 | -1.84 |
| 10-09 23:27 | +20 | ZEC | DOWN | 0.68 | open |  |
| 10-09 23:27 | +15 | ZEC | DOWN | 0.68 | open |  |
| 10-09 23:27 | +10 | ZEC | DOWN | 0.68 | open |  |
| 10-09 23:27 | +5 | ZEC | DOWN | 0.68 | open |  |
| 10-09 23:27 | +10 stop | HYPE | DOWN | 0.58 | 0.39 | -2.25 |
| 10-09 23:26 | +10 stop | HYPE | UP | 0.63 | 0.44 | -2.25 |
| 10-09 23:26 | +15 | HYPE | UP | 0.63 | 0.87 | 2.15 |
| 10-09 23:26 | +10 | HYPE | UP | 0.63 | 0.87 | 2.15 |
| 10-09 23:26 | +5 | HYPE | UP | 0.66 | 0.71 | 0.19 |
| 10-09 23:25 | +10 stop | BTC | UP | 0.67 | 0.41 | -2.93 |
| 10-09 23:25 | +20 | BTC | UP | 0.67 | open |  |
| 10-09 23:25 | +15 | BTC | UP | 0.67 | open |  |
| 10-09 23:25 | +10 | BTC | UP | 0.67 | open |  |
| 10-09 23:25 | +5 | BTC | UP | 0.67 | open |  |
| 10-09 23:24 | +10 stop | HYPE | UP | 0.54 | 0.66 | 0.86 |
| 10-09 23:21 | +10 stop | HYPE | UP | 0.57 | 0.36 | -2.45 |
| 10-09 23:21 | +20 | HYPE | UP | 0.57 | 0.87 | 2.74 |
| 10-09 23:21 | +15 | HYPE | UP | 0.57 | 0.74 | 1.38 |
| 10-09 23:21 | +10 | HYPE | UP | 0.57 | 0.69 | 0.87 |
| 10-09 23:21 | +5 | HYPE | UP | 0.57 | 0.66 | 0.56 |
| 10-09 23:20 | +10 stop | NEAR | DOWN | 0.61 | 0.78 | 1.35 |
| 10-09 23:19 | +10 stop | NEAR | DOWN | 0.67 | 0.51 | -1.94 |
| 10-09 23:17 | +10 stop | DOGE | DOWN | 0.23 | 0.57 | 3.09 |
| 10-09 23:17 | +20 | DOGE | DOWN | 0.23 | 0.57 | 3.09 |
| 10-09 23:17 | +15 | DOGE | DOWN | 0.23 | 0.57 | 3.09 |
| 10-09 23:17 | +10 | DOGE | DOWN | 0.23 | 0.57 | 3.09 |
| 10-09 23:17 | +5 | DOGE | DOWN | 0.23 | 0.57 | 3.09 |
| 10-09 23:16 | +10 stop | ZEC | UP | 0.70 | 0.55 | -1.83 |
| 10-09 23:16 | +20 | ZEC | UP | 0.70 | 0.91 | 1.90 |
| 10-09 23:16 | +15 | ZEC | UP | 0.70 | 0.89 | 1.68 |
| 10-09 23:16 | +10 | ZEC | UP | 0.70 | 0.80 | 0.73 |
| 10-09 23:16 | +5 | ZEC | UP | 0.70 | 0.78 | 0.52 |
| 10-09 23:16 | +10 stop | BNB | UP | 0.60 | 0.77 | 1.40 |
| 10-09 23:16 | +20 | BNB | UP | 0.60 | 0.80 | 1.71 |
| 10-09 23:16 | +15 | BNB | UP | 0.60 | 0.77 | 1.40 |
| 10-09 23:16 | +10 | BNB | UP | 0.60 | 0.77 | 1.40 |
| 10-09 23:16 | +5 | BNB | UP | 0.60 | 0.77 | 1.40 |
