# Range-Scalp Bot

*Updated Fri Oct 23 00:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29497 | 25676 | 3821 (39) | 3 | $-8695.65 | -4.7% |
| **+10¢** | 22117 | 17692 | 4425 (55) | 2 | $-7839.48 | -5.6% |
| **+15¢** | 18520 | 13770 | 4750 (78) | 2 | $-7006.66 | -6.0% |
| **+20¢** | 16388 | 11409 | 4979 (100) | 3 | $-6349.72 | -6.2% |
| **+10¢ (15¢ stop)** | 36208 | 36149 | 59 (32) | 0 | $-13659.87 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 00:09 | +10 stop | ZEC | DOWN | 0.60 | 0.45 | -1.85 |
| 10-23 00:08 | +10 stop | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 10-23 00:08 | +10 stop | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 10-23 00:08 | +10 | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 10-23 00:08 | +10 stop | HYPE | DOWN | 0.62 | 0.73 | 0.79 |
| 10-23 00:07 | +10 stop | XRP | DOWN | 0.69 | 0.83 | 1.15 |
| 10-23 00:07 | +20 | XRP | DOWN | 0.68 | 0.88 | 1.76 |
| 10-23 00:07 | +15 | XRP | DOWN | 0.70 | 0.85 | 1.26 |
| 10-23 00:07 | +10 | XRP | DOWN | 0.70 | 0.83 | 1.05 |
| 10-23 00:07 | +5 | XRP | DOWN | 0.70 | 0.75 | 0.21 |
| 10-23 00:07 | +10 stop | NEAR | UP | 0.56 | 0.33 | -2.64 |
| 10-23 00:07 | +10 stop | ZEC | UP | 0.71 | 0.56 | -1.83 |
| 10-23 00:07 | +5 | ZEC | UP | 0.71 | open |  |
| 10-23 00:07 | +10 stop | DOGE | UP | 0.69 | 0.36 | -3.62 |
| 10-23 00:07 | +5 | DOGE | UP | 0.69 | open |  |
| 10-23 00:06 | +10 stop | HYPE | UP | 0.66 | 0.43 | -2.68 |
| 10-23 00:06 | +10 | HYPE | UP | 0.66 | open |  |
| 10-23 00:06 | +5 | HYPE | UP | 0.66 | open |  |
| 10-23 00:06 | +10 stop | NEAR | UP | 0.57 | 0.69 | 0.87 |
| 10-23 00:05 | +10 stop | NEAR | DOWN | 0.49 | 0.64 | 1.15 |
| 10-23 00:05 | +10 stop | DOGE | DOWN | 0.37 | 0.59 | 1.86 |
| 10-23 00:05 | +5 | HYPE | UP | 0.58 | 0.73 | 1.14 |
| 10-23 00:04 | +10 stop | BNB | DOWN | 0.60 | 0.71 | 0.78 |
| 10-23 00:04 | +10 stop | ZEC | UP | 0.69 | 0.38 | -3.42 |
| 10-23 00:04 | +15 | ZEC | UP | 0.69 | open |  |
| 10-23 00:04 | +10 | ZEC | UP | 0.69 | open |  |
| 10-23 00:04 | +5 | ZEC | UP | 0.69 | 0.74 | 0.21 |
| 10-23 00:04 | +10 stop | HYPE | UP | 0.63 | 0.78 | 1.16 |
| 10-23 00:04 | +10 | HYPE | UP | 0.64 | 0.78 | 1.10 |
| 10-23 00:04 | +5 | HYPE | UP | 0.64 | 0.72 | 0.44 |
| 10-23 00:03 | +10 stop | XRP | DOWN | 0.68 | 0.82 | 1.13 |
| 10-23 00:03 | +10 stop | DOGE | UP | 0.61 | 0.43 | -2.15 |
| 10-23 00:03 | +10 stop | NEAR | UP | 0.60 | 0.34 | -2.93 |
| 10-23 00:03 | +5 | XRP | DOWN | 0.69 | 0.75 | 0.31 |
| 10-23 00:03 | +5 | ETH | DOWN | 0.65 | 0.74 | 0.60 |
| 10-23 00:03 | +10 stop | XRP | DOWN | 0.49 | 0.62 | 0.95 |
| 10-23 00:03 | +5 | XRP | DOWN | 0.49 | 0.54 | 0.14 |
| 10-23 00:02 | +10 stop | BNB | DOWN | 0.51 | 0.64 | 0.95 |
| 10-23 00:02 | +10 stop | HYPE | UP | 0.71 | 0.56 | -1.83 |
| 10-23 00:02 | +5 | XRP | DOWN | 0.55 | 0.60 | 0.15 |
