# Range-Scalp Bot

*Updated Sun Oct 11 22:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12571 | 10854 | 1717 (25) | 4 | $-4128.51 | -5.2% |
| **+10¢** | 9540 | 7550 | 1990 (37) | 6 | $-3880.69 | -6.5% |
| **+15¢** | 8030 | 5913 | 2117 (55) | 7 | $-3336.94 | -6.6% |
| **+20¢** | 7156 | 4949 | 2207 (69) | 8 | $-2837.11 | -6.3% |
| **+10¢ (15¢ stop)** | 15479 | 15438 | 41 (25) | 3 | $-6050.38 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 22:06 | +10 stop | BTC | UP | 0.62 | open |  |
| 10-11 22:06 | +15 | BTC | UP | 0.62 | open |  |
| 10-11 22:06 | +10 | BTC | UP | 0.62 | open |  |
| 10-11 22:06 | +5 | BTC | UP | 0.62 | 0.68 | 0.27 |
| 10-11 22:06 | +10 stop | BNB | UP | 0.64 | open |  |
| 10-11 22:06 | +10 | BNB | UP | 0.64 | open |  |
| 10-11 22:06 | +5 | BNB | UP | 0.64 | open |  |
| 10-11 22:06 | +10 stop | DOGE | UP | 0.57 | open |  |
| 10-11 22:06 | +10 | DOGE | UP | 0.57 | open |  |
| 10-11 22:06 | +5 | DOGE | UP | 0.57 | 0.66 | 0.56 |
| 10-11 22:05 | +10 stop | ZEC | UP | 0.42 | 0.56 | 1.04 |
| 10-11 22:05 | +5 | ZEC | UP | 0.55 | open |  |
| 10-11 22:05 | +10 stop | NEAR | UP | 0.71 | 0.55 | -1.93 |
| 10-11 22:05 | +20 | NEAR | UP | 0.71 | open |  |
| 10-11 22:05 | +15 | NEAR | UP | 0.70 | open |  |
| 10-11 22:05 | +10 | NEAR | UP | 0.70 | open |  |
| 10-11 22:05 | +5 | NEAR | UP | 0.70 | open |  |
| 10-11 22:04 | +5 | BTC | UP | 0.69 | 0.75 | 0.31 |
| 10-11 22:04 | +10 stop | DOGE | UP | 0.70 | 0.80 | 0.73 |
| 10-11 22:04 | +20 | DOGE | UP | 0.70 | open |  |
| 10-11 22:04 | +15 | DOGE | UP | 0.70 | open |  |
| 10-11 22:04 | +10 | DOGE | UP | 0.70 | 0.80 | 0.73 |
| 10-11 22:04 | +5 | DOGE | UP | 0.70 | 0.79 | 0.63 |
| 10-11 22:03 | +10 stop | SOL | UP | 0.65 | 0.79 | 1.12 |
| 10-11 22:03 | +20 | SOL | UP | 0.65 | open |  |
| 10-11 22:03 | +15 | SOL | UP | 0.65 | open |  |
| 10-11 22:03 | +10 | SOL | UP | 0.63 | 0.79 | 1.29 |
| 10-11 22:03 | +5 | SOL | UP | 0.63 | 0.69 | 0.26 |
| 10-11 22:03 | +10 stop | BTC | UP | 0.65 | 0.75 | 0.70 |
| 10-11 22:03 | +10 stop | BNB | UP | 0.67 | 0.79 | 0.92 |
| 10-11 22:03 | +10 | BNB | UP | 0.67 | 0.79 | 0.92 |
| 10-11 22:03 | +5 | BNB | UP | 0.67 | 0.75 | 0.50 |
| 10-11 22:03 | +10 stop | ZEC | DOWN | 0.55 | 0.39 | -1.95 |
| 10-11 22:03 | +15 | ZEC | DOWN | 0.55 | open |  |
| 10-11 22:03 | +10 | ZEC | DOWN | 0.56 | open |  |
| 10-11 22:03 | +5 | ZEC | DOWN | 0.55 | 0.62 | 0.35 |
| 10-11 22:03 | +10 stop | BNB | DOWN | 0.41 | 0.55 | 1.05 |
| 10-11 22:03 | +20 | BNB | DOWN | 0.41 | open |  |
| 10-11 22:03 | +15 | BNB | DOWN | 0.41 | open |  |
| 10-11 22:03 | +10 | BNB | DOWN | 0.41 | 0.55 | 1.05 |
