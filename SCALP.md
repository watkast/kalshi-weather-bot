# Range-Scalp Bot

*Updated Mon Oct 05 17:18 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4030 | 3461 | 569 (4) | 2 | $-1468.73 | -5.8% |
| **+10¢** | 3116 | 2461 | 655 (5) | 3 | $-1349.70 | -6.9% |
| **+15¢** | 2620 | 1931 | 689 (8) | 4 | $-1157.45 | -7.0% |
| **+20¢** | 2340 | 1622 | 718 (13) | 4 | $-993.38 | -6.8% |
| **+10¢ (15¢ stop)** | 4961 | 4956 | 5 (2) | 3 | $-1808.84 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 17:17 | +5 | BNB | UP | 0.70 | open |  |
| 10-05 17:15 | +10 stop | ZEC | UP | 0.63 | 0.87 | 2.15 |
| 10-05 17:15 | +20 | ZEC | UP | 0.63 | 0.87 | 2.15 |
| 10-05 17:15 | +15 | ZEC | UP | 0.63 | 0.87 | 2.15 |
| 10-05 17:15 | +10 | ZEC | UP | 0.63 | 0.87 | 2.15 |
| 10-05 17:15 | +5 | ZEC | UP | 0.63 | 0.68 | 0.17 |
| 10-05 17:15 | +10 stop | NEAR | UP | 0.71 | open |  |
| 10-05 17:15 | +20 | NEAR | UP | 0.71 | open |  |
| 10-05 17:15 | +15 | NEAR | UP | 0.71 | open |  |
| 10-05 17:15 | +10 | NEAR | UP | 0.70 | open |  |
| 10-05 17:15 | +5 | NEAR | UP | 0.70 | open |  |
| 10-05 17:15 | +10 stop | HYPE | UP | 0.61 | open |  |
| 10-05 17:15 | +20 | HYPE | UP | 0.61 | open |  |
| 10-05 17:15 | +15 | HYPE | UP | 0.61 | open |  |
| 10-05 17:15 | +10 | HYPE | UP | 0.61 | open |  |
| 10-05 17:15 | +5 | HYPE | UP | 0.61 | 0.67 | 0.23 |
| 10-05 17:15 | +10 stop | BTC | UP | 0.70 | 0.80 | 0.73 |
| 10-05 17:15 | +20 | BTC | UP | 0.70 | open |  |
| 10-05 17:15 | +15 | BTC | UP | 0.70 | open |  |
| 10-05 17:15 | +10 | BTC | UP | 0.70 | 0.80 | 0.73 |
| 10-05 17:15 | +5 | BTC | UP | 0.70 | 0.75 | 0.21 |
| 10-05 17:15 | +10 stop | BNB | UP | 0.60 | open |  |
| 10-05 17:15 | +20 | BNB | UP | 0.60 | open |  |
| 10-05 17:15 | +15 | BNB | UP | 0.59 | open |  |
| 10-05 17:15 | +10 | BNB | UP | 0.59 | open |  |
| 10-05 17:15 | +5 | BNB | UP | 0.59 | 0.69 | 0.64 |
| 10-05 17:03 | +10 stop | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 10-05 17:03 | +10 | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 10-05 17:03 | +5 | ZEC | DOWN | 0.70 | 0.77 | 0.42 |
| 10-05 17:02 | +10 stop | XRP | DOWN | 0.70 | 0.84 | 1.15 |
| 10-05 17:02 | +20 | XRP | DOWN | 0.70 | 0.90 | 1.80 |
| 10-05 17:02 | +15 | XRP | DOWN | 0.70 | 0.85 | 1.26 |
| 10-05 17:02 | +10 | XRP | DOWN | 0.70 | 0.84 | 1.15 |
| 10-05 17:02 | +5 | XRP | DOWN | 0.70 | 0.76 | 0.32 |
| 10-05 17:01 | +10 stop | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 10-05 17:01 | +20 | NEAR | DOWN | 0.65 | 0.89 | 2.17 |
| 10-05 17:01 | +15 | NEAR | DOWN | 0.65 | 0.81 | 1.33 |
| 10-05 17:01 | +10 | NEAR | DOWN | 0.65 | 0.77 | 0.88 |
| 10-05 17:01 | +5 | NEAR | DOWN | 0.65 | 0.72 | 0.36 |
| 10-05 17:01 | +10 stop | DOGE | DOWN | 0.57 | 0.71 | 1.07 |
