# Range-Scalp Bot

*Updated Thu Oct 22 04:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28286 | 24652 | 3634 (39) | 3 | $-8098.75 | -4.5% |
| **+10¢** | 21234 | 17032 | 4202 (55) | 3 | $-7172.06 | -5.4% |
| **+15¢** | 17785 | 13262 | 4523 (78) | 3 | $-6413.21 | -5.7% |
| **+20¢** | 15733 | 10990 | 4743 (98) | 3 | $-5792.41 | -5.9% |
| **+10¢ (15¢ stop)** | 34712 | 34653 | 59 (32) | 2 | $-13004.23 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 04:25 | +10 stop | ZEC | UP | 0.45 | open |  |
| 10-22 04:25 | +5 | ZEC | DOWN | 0.62 | open |  |
| 10-22 04:25 | +10 stop | ETH | UP | 0.71 | 0.83 | 0.95 |
| 10-22 04:25 | +10 | ETH | UP | 0.71 | 0.83 | 0.95 |
| 10-22 04:25 | +5 | ETH | UP | 0.71 | 0.79 | 0.53 |
| 10-22 04:24 | +10 stop | BTC | UP | 0.60 | open |  |
| 10-22 04:24 | +5 | ZEC | DOWN | 0.61 | 0.67 | 0.27 |
| 10-22 04:24 | +10 stop | HYPE | UP | 0.64 | 0.74 | 0.69 |
| 10-22 04:24 | +15 | HYPE | UP | 0.64 | 0.79 | 1.21 |
| 10-22 04:24 | +10 | HYPE | UP | 0.64 | 0.74 | 0.69 |
| 10-22 04:24 | +5 | HYPE | UP | 0.64 | 0.73 | 0.59 |
| 10-22 04:23 | +5 | ZEC | DOWN | 0.58 | 0.65 | 0.33 |
| 10-22 04:23 | +10 stop | NEAR | UP | 0.68 | 0.81 | 1.03 |
| 10-22 04:23 | +5 | ZEC | DOWN | 0.58 | 0.67 | 0.56 |
| 10-22 04:23 | +10 stop | ZEC | DOWN | 0.69 | 0.43 | -2.93 |
| 10-22 04:21 | +5 | XRP | UP | 0.70 | 0.76 | 0.32 |
| 10-22 04:21 | +10 stop | XRP | UP | 0.70 | 0.81 | 0.84 |
| 10-22 04:20 | +10 stop | NEAR | UP | 0.64 | 0.48 | -1.95 |
| 10-22 04:20 | +10 stop | ZEC | DOWN | 0.61 | 0.44 | -2.05 |
| 10-22 04:20 | +20 | ZEC | DOWN | 0.61 | open |  |
| 10-22 04:20 | +15 | ZEC | DOWN | 0.61 | open |  |
| 10-22 04:20 | +10 | ZEC | DOWN | 0.61 | open |  |
| 10-22 04:20 | +5 | ZEC | DOWN | 0.61 | 0.68 | 0.37 |
| 10-22 04:20 | +10 stop | SOL | UP | 0.62 | 0.82 | 1.72 |
| 10-22 04:19 | +10 stop | XRP | DOWN | 0.57 | 0.41 | -1.95 |
| 10-22 04:19 | +10 stop | ETH | DOWN | 0.56 | 0.33 | -2.64 |
| 10-22 04:19 | +10 stop | BNB | DOWN | 0.70 | 0.83 | 1.05 |
| 10-22 04:19 | +10 stop | NEAR | DOWN | 0.64 | 0.49 | -1.85 |
| 10-22 04:19 | +10 stop | BTC | DOWN | 0.60 | 0.42 | -2.15 |
| 10-22 04:18 | +10 stop | SOL | UP | 0.60 | 0.44 | -1.95 |
| 10-22 04:18 | +10 | SOL | UP | 0.60 | 0.82 | 1.92 |
| 10-22 04:18 | +5 | XRP | UP | 0.62 | 0.67 | 0.17 |
| 10-22 04:18 | +5 | ZEC | UP | 0.47 | 0.54 | 0.34 |
| 10-22 04:17 | +5 | DOGE | UP | 0.67 | 0.79 | 0.92 |
| 10-22 04:17 | +5 | HYPE | UP | 0.67 | 0.74 | 0.40 |
| 10-22 04:17 | +5 | ETH | UP | 0.61 | 0.66 | 0.17 |
| 10-22 04:17 | +5 | SOL | UP | 0.69 | 0.82 | 1.04 |
| 10-22 04:17 | +10 stop | ZEC | DOWN | 0.48 | 0.60 | 0.85 |
| 10-22 04:17 | +20 | ZEC | DOWN | 0.48 | 0.68 | 1.66 |
| 10-22 04:17 | +15 | ZEC | DOWN | 0.48 | 0.68 | 1.66 |
