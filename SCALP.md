# Range-Scalp Bot

*Updated Fri Oct 09 22:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9582 | 8276 | 1306 (18) | 2 | $-3200.00 | -5.3% |
| **+10¢** | 7233 | 5702 | 1531 (30) | 2 | $-3112.20 | -6.8% |
| **+15¢** | 6096 | 4483 | 1613 (43) | 4 | $-2568.70 | -6.7% |
| **+20¢** | 5429 | 3753 | 1676 (55) | 5 | $-2125.81 | -6.2% |
| **+10¢ (15¢ stop)** | 11720 | 11685 | 35 (22) | 0 | $-4483.52 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 22:58 | +10 stop | NEAR | DOWN | 0.55 | 0.65 | 0.66 |
| 10-09 22:57 | +10 stop | BTC | UP | 0.62 | 0.47 | -1.85 |
| 10-09 22:56 | +10 stop | DOGE | DOWN | 0.58 | 0.70 | 0.88 |
| 10-09 22:56 | +10 | DOGE | DOWN | 0.58 | 0.70 | 0.88 |
| 10-09 22:56 | +5 | DOGE | DOWN | 0.58 | 0.64 | 0.26 |
| 10-09 22:56 | +10 stop | ZEC | DOWN | 0.65 | 0.80 | 1.18 |
| 10-09 22:56 | +10 stop | ETH | UP | 0.60 | 0.34 | -2.93 |
| 10-09 22:55 | +10 stop | ETH | DOWN | 0.69 | 0.38 | -3.42 |
| 10-09 22:55 | +10 | ETH | DOWN | 0.69 | 0.87 | 1.57 |
| 10-09 22:55 | +5 | ETH | DOWN | 0.69 | 0.78 | 0.62 |
| 10-09 22:55 | +10 stop | NEAR | DOWN | 0.55 | 0.65 | 0.67 |
| 10-09 22:54 | +5 | BTC | UP | 0.61 | 0.91 | 2.73 |
| 10-09 22:54 | +10 stop | BTC | UP | 0.60 | 0.44 | -1.95 |
| 10-09 22:54 | +10 | BTC | UP | 0.60 | 0.91 | 2.83 |
| 10-09 22:54 | +5 | BTC | UP | 0.59 | 0.67 | 0.47 |
| 10-09 22:53 | +10 stop | DOGE | UP | 0.69 | 0.47 | -2.53 |
| 10-09 22:53 | +10 stop | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 10-09 22:53 | +10 stop | NEAR | UP | 0.53 | 0.38 | -1.85 |
| 10-09 22:52 | +10 stop | NEAR | UP | 0.71 | 0.53 | -2.11 |
| 10-09 22:52 | +20 | NEAR | UP | 0.70 | open |  |
| 10-09 22:52 | +15 | NEAR | UP | 0.70 | open |  |
| 10-09 22:52 | +10 | NEAR | UP | 0.70 | open |  |
| 10-09 22:52 | +5 | NEAR | UP | 0.70 | open |  |
| 10-09 22:52 | +10 stop | ZEC | DOWN | 0.71 | 0.84 | 1.05 |
| 10-09 22:51 | +10 stop | HYPE | DOWN | 0.62 | 0.40 | -2.54 |
| 10-09 22:50 | +10 stop | DOGE | DOWN | 0.71 | 0.49 | -2.53 |
| 10-09 22:49 | +10 stop | BNB | UP | 0.67 | 0.77 | 0.71 |
| 10-09 22:49 | +10 | BNB | UP | 0.67 | 0.77 | 0.71 |
| 10-09 22:49 | +5 | BNB | UP | 0.67 | 0.74 | 0.40 |
| 10-09 22:49 | +10 stop | BTC | UP | 0.55 | 0.67 | 0.86 |
| 10-09 22:49 | +20 | BTC | UP | 0.55 | 0.91 | 3.32 |
| 10-09 22:49 | +15 | BTC | UP | 0.55 | 0.91 | 3.32 |
| 10-09 22:49 | +10 | BTC | UP | 0.55 | 0.67 | 0.86 |
| 10-09 22:49 | +5 | BTC | UP | 0.55 | 0.61 | 0.25 |
| 10-09 22:48 | +5 | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 10-09 22:48 | +5 | DOGE | UP | 0.58 | 0.66 | 0.46 |
| 10-09 22:48 | +10 stop | XRP | UP | 0.57 | 0.70 | 0.95 |
| 10-09 22:47 | +10 stop | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-09 22:47 | +20 | SOL | DOWN | 0.63 | 0.83 | 1.73 |
| 10-09 22:47 | +15 | SOL | DOWN | 0.63 | 0.78 | 1.20 |
