# Range-Scalp Bot

*Updated Sun Oct 25 03:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32518 | 28354 | 4164 (42) | 2 | $-9264.27 | -4.5% |
| **+10¢** | 24339 | 19517 | 4822 (60) | 3 | $-8300.52 | -5.4% |
| **+15¢** | 20375 | 15187 | 5188 (83) | 3 | $-7455.39 | -5.8% |
| **+20¢** | 18048 | 12620 | 5428 (105) | 4 | $-6591.99 | -5.8% |
| **+10¢ (15¢ stop)** | 39956 | 39896 | 60 (32) | 0 | $-15279.93 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 03:42 | +5 | HYPE | DOWN | 0.54 | 0.64 | 0.65 |
| 10-25 03:41 | +10 stop | NEAR | UP | 0.71 | 0.83 | 0.95 |
| 10-25 03:41 | +10 stop | HYPE | DOWN | 0.68 | 0.47 | -2.44 |
| 10-25 03:41 | +10 | HYPE | DOWN | 0.68 | open |  |
| 10-25 03:41 | +10 stop | XRP | DOWN | 0.40 | 0.53 | 0.95 |
| 10-25 03:41 | +10 | XRP | DOWN | 0.40 | 0.53 | 0.95 |
| 10-25 03:41 | +5 | XRP | DOWN | 0.40 | 0.53 | 0.95 |
| 10-25 03:40 | +10 stop | DOGE | UP | 0.36 | 0.55 | 1.55 |
| 10-25 03:40 | +10 | DOGE | UP | 0.39 | 0.55 | 1.25 |
| 10-25 03:40 | +5 | DOGE | UP | 0.47 | 0.55 | 0.44 |
| 10-25 03:39 | +10 stop | NEAR | UP | 0.62 | 0.46 | -1.94 |
| 10-25 03:39 | +10 stop | DOGE | UP | 0.61 | 0.72 | 0.78 |
| 10-25 03:39 | +10 stop | HYPE | DOWN | 0.55 | 0.68 | 0.96 |
| 10-25 03:38 | +5 | NEAR | DOWN | 0.68 | open |  |
| 10-25 03:38 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-25 03:38 | +10 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-25 03:38 | +10 | HYPE | DOWN | 0.57 | 0.68 | 0.76 |
| 10-25 03:38 | +10 stop | XRP | DOWN | 0.39 | 0.55 | 1.25 |
| 10-25 03:37 | +10 stop | HYPE | DOWN | 0.69 | 0.53 | -1.93 |
| 10-25 03:37 | +10 stop | DOGE | DOWN | 0.70 | 0.54 | -1.93 |
| 10-25 03:36 | +10 stop | HYPE | UP | 0.46 | 0.31 | -1.83 |
| 10-25 03:36 | +10 stop | ZEC | DOWN | 0.68 | 0.80 | 0.92 |
| 10-25 03:36 | +20 | ZEC | DOWN | 0.68 | open |  |
| 10-25 03:36 | +15 | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 10-25 03:36 | +10 | ZEC | DOWN | 0.68 | 0.80 | 0.92 |
| 10-25 03:36 | +5 | ZEC | DOWN | 0.68 | 0.74 | 0.30 |
| 10-25 03:36 | +10 stop | NEAR | DOWN | 0.71 | 0.50 | -2.43 |
| 10-25 03:36 | +20 | NEAR | DOWN | 0.71 | open |  |
| 10-25 03:36 | +15 | NEAR | DOWN | 0.71 | open |  |
| 10-25 03:36 | +10 | NEAR | DOWN | 0.71 | open |  |
| 10-25 03:36 | +5 | NEAR | DOWN | 0.71 | 0.78 | 0.42 |
| 10-25 03:35 | +10 stop | XRP | DOWN | 0.71 | 0.52 | -2.23 |
| 10-25 03:35 | +5 | HYPE | DOWN | 0.68 | 0.73 | 0.20 |
| 10-25 03:35 | +10 stop | DOGE | DOWN | 0.70 | 0.54 | -1.93 |
| 10-25 03:34 | +5 | HYPE | DOWN | 0.61 | 0.66 | 0.17 |
| 10-25 03:33 | +5 | BTC | DOWN | 0.68 | 0.74 | 0.30 |
| 10-25 03:32 | +10 stop | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 10-25 03:32 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-25 03:32 | +10 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-25 03:32 | +5 | ZEC | DOWN | 0.70 | 0.76 | 0.32 |
