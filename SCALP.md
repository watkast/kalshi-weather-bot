# Range-Scalp Bot

*Updated Thu Oct 22 04:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28320 | 24682 | 3638 (39) | 2 | $-8105.40 | -4.5% |
| **+10¢** | 21260 | 17051 | 4209 (55) | 2 | $-7191.10 | -5.4% |
| **+15¢** | 17811 | 13281 | 4530 (78) | 1 | $-6424.91 | -5.7% |
| **+20¢** | 15757 | 11007 | 4750 (98) | 1 | $-5795.62 | -5.9% |
| **+10¢ (15¢ stop)** | 34751 | 34692 | 59 (32) | 1 | $-13020.55 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 04:55 | +10 stop | NEAR | UP | 0.68 | open |  |
| 10-22 04:55 | +15 | NEAR | UP | 0.68 | open |  |
| 10-22 04:55 | +10 | NEAR | UP | 0.67 | open |  |
| 10-22 04:55 | +5 | NEAR | UP | 0.66 | 0.71 | 0.19 |
| 10-22 04:55 | +10 stop | ZEC | UP | 0.67 | 0.87 | 1.76 |
| 10-22 04:55 | +15 | ZEC | UP | 0.67 | 0.87 | 1.76 |
| 10-22 04:55 | +10 | ZEC | UP | 0.67 | 0.87 | 1.76 |
| 10-22 04:52 | +10 stop | ZEC | DOWN | 0.60 | 0.25 | -3.79 |
| 10-22 04:52 | +5 | ZEC | DOWN | 0.60 | open |  |
| 10-22 04:52 | +10 stop | SOL | UP | 0.65 | 0.80 | 1.22 |
| 10-22 04:51 | +5 | DOGE | UP | 0.71 | 0.78 | 0.42 |
| 10-22 04:51 | +10 stop | SOL | DOWN | 0.42 | 0.60 | 1.45 |
| 10-22 04:51 | +10 stop | HYPE | DOWN | 0.63 | 0.31 | -3.52 |
| 10-22 04:51 | +10 stop | XRP | DOWN | 0.44 | 0.60 | 1.25 |
| 10-22 04:51 | +5 | ZEC | DOWN | 0.67 | 0.72 | 0.19 |
| 10-22 04:50 | +10 stop | SOL | UP | 0.57 | 0.42 | -1.86 |
| 10-22 04:50 | +10 stop | DOGE | UP | 0.62 | 0.78 | 1.30 |
| 10-22 04:49 | +5 | XRP | DOWN | 0.61 | open |  |
| 10-22 04:49 | +10 stop | SOL | DOWN | 0.40 | 0.56 | 1.25 |
| 10-22 04:49 | +5 | XRP | DOWN | 0.55 | 0.68 | 0.96 |
| 10-22 04:49 | +10 stop | ZEC | DOWN | 0.59 | 0.71 | 0.89 |
| 10-22 04:49 | +10 stop | NEAR | DOWN | 0.67 | 0.42 | -2.84 |
| 10-22 04:48 | +5 | ZEC | DOWN | 0.58 | 0.65 | 0.33 |
| 10-22 04:48 | +10 stop | BTC | UP | 0.69 | 0.79 | 0.73 |
| 10-22 04:48 | +20 | BTC | UP | 0.69 | 0.90 | 1.89 |
| 10-22 04:48 | +15 | BTC | UP | 0.69 | 0.86 | 1.46 |
| 10-22 04:48 | +10 | BTC | UP | 0.69 | 0.79 | 0.73 |
| 10-22 04:48 | +5 | BTC | UP | 0.69 | 0.79 | 0.73 |
| 10-22 04:48 | +10 stop | HYPE | UP | 0.60 | 0.39 | -2.44 |
| 10-22 04:48 | +20 | HYPE | UP | 0.60 | 0.81 | 1.82 |
| 10-22 04:48 | +15 | HYPE | UP | 0.60 | 0.79 | 1.61 |
| 10-22 04:48 | +10 | HYPE | UP | 0.60 | 0.79 | 1.61 |
| 10-22 04:48 | +5 | HYPE | UP | 0.60 | 0.68 | 0.47 |
| 10-22 04:48 | +10 stop | ZEC | UP | 0.56 | 0.39 | -2.05 |
| 10-22 04:48 | +20 | ZEC | UP | 0.56 | 0.87 | 2.84 |
| 10-22 04:48 | +15 | ZEC | UP | 0.56 | 0.74 | 1.48 |
| 10-22 04:48 | +10 | ZEC | UP | 0.56 | 0.74 | 1.48 |
| 10-22 04:48 | +5 | ZEC | UP | 0.56 | 0.64 | 0.45 |
| 10-22 04:48 | +10 stop | XRP | DOWN | 0.66 | 0.50 | -1.94 |
| 10-22 04:48 | +10 | XRP | DOWN | 0.66 | open |  |
