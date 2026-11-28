# Range-Scalp Bot

*Updated Sat Nov 28 02:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 74245 | 64808 | 9437 (171) | 0 | $-19679.83 | -4.2% |
| **+10¢** | 55312 | 44286 | 11026 (217) | 2 | $-18303.55 | -5.3% |
| **+15¢** | 46316 | 34442 | 11874 (275) | 3 | $-16351.68 | -5.6% |
| **+20¢** | 41219 | 28713 | 12506 (342) | 3 | $-14758.70 | -5.7% |
| **+10¢ (15¢ stop)** | 90361 | 90142 | 219 (135) | 2 | $-33373.60 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-28 02:31 | +10 stop | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-28 02:31 | +20 | BTC | DOWN | 0.69 | open |  |
| 11-28 02:31 | +15 | BTC | DOWN | 0.69 | open |  |
| 11-28 02:31 | +10 | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-28 02:31 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 11-28 02:31 | +10 stop | XRP | DOWN | 0.70 | open |  |
| 11-28 02:31 | +20 | XRP | DOWN | 0.70 | open |  |
| 11-28 02:31 | +15 | XRP | DOWN | 0.70 | open |  |
| 11-28 02:31 | +10 | XRP | DOWN | 0.70 | open |  |
| 11-28 02:31 | +5 | XRP | DOWN | 0.70 | 0.76 | 0.32 |
| 11-28 02:31 | +10 stop | ETH | DOWN | 0.68 | open |  |
| 11-28 02:31 | +20 | ETH | DOWN | 0.68 | open |  |
| 11-28 02:31 | +15 | ETH | DOWN | 0.68 | open |  |
| 11-28 02:31 | +10 | ETH | DOWN | 0.68 | open |  |
| 11-28 02:31 | +5 | ETH | DOWN | 0.68 | 0.73 | 0.20 |
| 11-28 02:26 | +10 stop | NEAR | UP | 0.62 | 0.72 | 0.68 |
| 11-28 02:24 | +10 stop | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-28 02:24 | +10 stop | ETH | DOWN | 0.67 | 0.80 | 1.02 |
| 11-28 02:23 | +10 stop | NEAR | UP | 0.60 | 0.25 | -3.80 |
| 11-28 02:23 | +10 stop | BNB | DOWN | 0.71 | 0.55 | -1.93 |
| 11-28 02:21 | +10 | ZEC | UP | 0.51 | 0.65 | 1.06 |
| 11-28 02:21 | +5 | ZEC | UP | 0.51 | 0.57 | 0.24 |
| 11-28 02:21 | +10 stop | ZEC | UP | 0.57 | 0.69 | 0.87 |
| 11-28 02:21 | +20 | ZEC | UP | 0.57 | 0.83 | 2.34 |
| 11-28 02:21 | +15 | ZEC | UP | 0.55 | 0.83 | 2.53 |
| 11-28 02:21 | +10 | ZEC | UP | 0.53 | 0.65 | 0.86 |
| 11-28 02:21 | +5 | ZEC | UP | 0.53 | 0.65 | 0.91 |
| 11-28 02:20 | +10 stop | BNB | DOWN | 0.62 | 0.75 | 0.99 |
| 11-28 02:19 | +10 stop | NEAR | DOWN | 0.66 | 0.45 | -2.44 |
| 11-28 02:19 | +5 | DOGE | DOWN | 0.70 | 0.83 | 1.00 |
| 11-28 02:19 | +10 stop | BTC | UP | 0.58 | 0.41 | -2.05 |
| 11-28 02:19 | +10 stop | BNB | UP | 0.49 | 0.60 | 0.75 |
| 11-28 02:19 | +10 stop | DOGE | DOWN | 0.62 | 0.83 | 1.83 |
| 11-28 02:19 | +10 | DOGE | DOWN | 0.62 | 0.83 | 1.83 |
| 11-28 02:19 | +10 stop | HYPE | DOWN | 0.67 | 0.83 | 1.34 |
| 11-28 02:19 | +5 | HYPE | DOWN | 0.63 | 0.68 | 0.18 |
| 11-28 02:18 | +5 | ETH | UP | 0.67 | no | -6.86 |
| 11-28 02:18 | +5 | DOGE | DOWN | 0.57 | 0.62 | 0.15 |
| 11-28 02:17 | +10 stop | BTC | UP | 0.69 | 0.50 | -2.23 |
| 11-28 02:17 | +10 | BTC | UP | 0.69 | no | -7.05 |
