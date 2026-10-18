# Range-Scalp Bot

*Updated Sun Oct 18 15:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22695 | 19756 | 2939 (29) | 0 | $-6625.98 | -4.6% |
| **+10¢** | 17077 | 13684 | 3393 (43) | 1 | $-5880.43 | -5.5% |
| **+15¢** | 14302 | 10641 | 3661 (64) | 0 | $-5357.60 | -6.0% |
| **+20¢** | 12662 | 8830 | 3832 (82) | 1 | $-4755.78 | -6.0% |
| **+10¢ (15¢ stop)** | 27909 | 27859 | 50 (29) | 0 | $-10663.82 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 15:12 | +10 stop | NEAR | DOWN | 0.55 | 0.37 | -2.15 |
| 10-18 15:12 | +10 | NEAR | DOWN | 0.59 | open |  |
| 10-18 15:11 | +10 stop | NEAR | UP | 0.65 | 0.44 | -2.44 |
| 10-18 15:11 | +5 | NEAR | UP | 0.65 | 0.74 | 0.60 |
| 10-18 15:09 | +10 stop | NEAR | UP | 0.56 | 0.40 | -1.95 |
| 10-18 15:09 | +20 | NEAR | UP | 0.56 | open |  |
| 10-18 15:09 | +15 | NEAR | UP | 0.56 | 0.74 | 1.48 |
| 10-18 15:09 | +10 | NEAR | UP | 0.57 | 0.67 | 0.66 |
| 10-18 15:09 | +5 | NEAR | UP | 0.57 | 0.62 | 0.15 |
| 10-18 15:08 | +10 stop | HYPE | DOWN | 0.63 | 0.78 | 1.20 |
| 10-18 15:06 | +10 stop | HYPE | UP | 0.67 | 0.48 | -2.24 |
| 10-18 15:05 | +15 | HYPE | DOWN | 0.55 | 0.72 | 1.33 |
| 10-18 15:04 | +20 | HYPE | DOWN | 0.66 | 0.91 | 2.23 |
| 10-18 15:04 | +10 stop | HYPE | DOWN | 0.69 | 0.41 | -3.12 |
| 10-18 15:04 | +10 | HYPE | DOWN | 0.69 | 0.82 | 1.04 |
| 10-18 15:04 | +5 | HYPE | DOWN | 0.69 | 0.78 | 0.62 |
| 10-18 15:03 | +15 | HYPE | DOWN | 0.57 | 0.72 | 1.17 |
| 10-18 15:03 | +10 stop | HYPE | DOWN | 0.53 | 0.65 | 0.85 |
| 10-18 15:03 | +10 | HYPE | DOWN | 0.53 | 0.65 | 0.85 |
| 10-18 15:03 | +5 | HYPE | DOWN | 0.53 | 0.65 | 0.85 |
| 10-18 15:03 | +5 | NEAR | UP | 0.70 | 0.76 | 0.32 |
| 10-18 15:01 | +10 stop | HYPE | DOWN | 0.46 | 0.56 | 0.64 |
| 10-18 15:01 | +20 | HYPE | DOWN | 0.46 | 0.67 | 1.76 |
| 10-18 15:01 | +15 | HYPE | DOWN | 0.46 | 0.62 | 1.25 |
| 10-18 15:01 | +10 | HYPE | DOWN | 0.46 | 0.56 | 0.64 |
| 10-18 15:01 | +5 | HYPE | DOWN | 0.46 | 0.56 | 0.64 |
| 10-18 15:01 | +10 stop | DOGE | UP | 0.71 | 0.82 | 0.84 |
| 10-18 15:01 | +20 | DOGE | UP | 0.71 | 0.93 | 2.04 |
| 10-18 15:01 | +15 | DOGE | UP | 0.71 | 0.90 | 1.69 |
| 10-18 15:01 | +10 | DOGE | UP | 0.71 | 0.82 | 0.84 |
| 10-18 15:01 | +5 | DOGE | UP | 0.71 | 0.76 | 0.22 |
| 10-18 15:01 | +10 stop | NEAR | UP | 0.66 | 0.76 | 0.71 |
| 10-18 15:01 | +20 | NEAR | UP | 0.66 | 0.86 | 1.75 |
| 10-18 15:01 | +15 | NEAR | UP | 0.66 | 0.86 | 1.75 |
| 10-18 15:01 | +10 | NEAR | UP | 0.66 | 0.76 | 0.71 |
| 10-18 15:01 | +5 | NEAR | UP | 0.66 | 0.71 | 0.19 |
| 10-18 14:59 | +10 stop | BTC | UP | 0.67 | 0.22 | -4.79 |
| 10-18 14:57 | +10 stop | SOL | UP | 0.63 | 0.79 | 1.31 |
| 10-18 14:56 | +10 stop | SOL | DOWN | 0.64 | 0.78 | 1.10 |
| 10-18 14:53 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
