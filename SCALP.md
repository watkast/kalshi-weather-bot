# Range-Scalp Bot

*Updated Sun Oct 18 16:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22757 | 19812 | 2945 (29) | 0 | $-6629.60 | -4.6% |
| **+10¢** | 17127 | 13727 | 3400 (43) | 0 | $-5879.94 | -5.5% |
| **+15¢** | 14345 | 10676 | 3669 (64) | 1 | $-5353.45 | -5.9% |
| **+20¢** | 12700 | 8860 | 3840 (82) | 1 | $-4744.15 | -6.0% |
| **+10¢ (15¢ stop)** | 27982 | 27932 | 50 (29) | 0 | $-10668.69 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 16:12 | +10 stop | DOGE | UP | 0.42 | 0.60 | 1.45 |
| 10-18 16:08 | +10 stop | NEAR | UP | 0.66 | 0.39 | -3.03 |
| 10-18 16:08 | +10 stop | DOGE | UP | 0.69 | 0.50 | -2.23 |
| 10-18 16:08 | +10 | DOGE | UP | 0.69 | 0.91 | 1.98 |
| 10-18 16:08 | +5 | DOGE | UP | 0.69 | 0.91 | 1.98 |
| 10-18 16:06 | +10 stop | DOGE | DOWN | 0.42 | 0.54 | 0.84 |
| 10-18 16:06 | +10 | DOGE | DOWN | 0.42 | 0.54 | 0.84 |
| 10-18 16:06 | +5 | DOGE | DOWN | 0.42 | 0.54 | 0.84 |
| 10-18 16:06 | +10 stop | NEAR | DOWN | 0.46 | 0.31 | -1.83 |
| 10-18 16:06 | +10 stop | DOGE | DOWN | 0.51 | 0.62 | 0.75 |
| 10-18 16:06 | +20 | DOGE | DOWN | 0.50 | open |  |
| 10-18 16:06 | +15 | DOGE | DOWN | 0.50 | open |  |
| 10-18 16:06 | +10 | DOGE | DOWN | 0.50 | 0.62 | 0.85 |
| 10-18 16:06 | +5 | DOGE | DOWN | 0.50 | 0.62 | 0.85 |
| 10-18 16:03 | +5 | NEAR | DOWN | 0.68 | 0.76 | 0.51 |
| 10-18 16:02 | +5 | BTC | DOWN | 0.70 | 0.77 | 0.42 |
| 10-18 16:01 | +10 stop | ZEC | DOWN | 0.66 | 0.79 | 1.02 |
| 10-18 16:01 | +20 | ZEC | DOWN | 0.66 | 0.95 | 2.71 |
| 10-18 16:01 | +15 | ZEC | DOWN | 0.67 | 0.84 | 1.44 |
| 10-18 16:01 | +10 | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-18 16:01 | +5 | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-18 16:00 | +10 stop | HYPE | DOWN | 0.67 | 0.89 | 1.93 |
| 10-18 16:00 | +20 | HYPE | DOWN | 0.67 | 0.89 | 1.93 |
| 10-18 16:00 | +15 | HYPE | DOWN | 0.67 | 0.89 | 1.93 |
| 10-18 16:00 | +10 | HYPE | DOWN | 0.67 | 0.89 | 1.93 |
| 10-18 16:00 | +5 | HYPE | DOWN | 0.67 | 0.73 | 0.26 |
| 10-18 16:00 | +10 stop | BNB | DOWN | 0.69 | 0.80 | 0.79 |
| 10-18 16:00 | +20 | BNB | DOWN | 0.69 | 0.91 | 1.91 |
| 10-18 16:00 | +15 | BNB | DOWN | 0.69 | 0.87 | 1.53 |
| 10-18 16:00 | +10 | BNB | DOWN | 0.69 | 0.80 | 0.79 |
| 10-18 16:00 | +5 | BNB | DOWN | 0.69 | 0.80 | 0.79 |
| 10-18 16:00 | +10 stop | NEAR | DOWN | 0.68 | 0.53 | -1.84 |
| 10-18 16:00 | +20 | NEAR | DOWN | 0.68 | 0.89 | 1.87 |
| 10-18 16:00 | +15 | NEAR | DOWN | 0.68 | 0.89 | 1.87 |
| 10-18 16:00 | +10 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 10-18 16:00 | +5 | NEAR | DOWN | 0.68 | 0.74 | 0.30 |
| 10-18 16:00 | +10 stop | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-18 16:00 | +20 | BTC | DOWN | 0.61 | 0.86 | 2.24 |
| 10-18 16:00 | +15 | BTC | DOWN | 0.61 | 0.77 | 1.30 |
| 10-18 16:00 | +10 | BTC | DOWN | 0.61 | 0.71 | 0.68 |
