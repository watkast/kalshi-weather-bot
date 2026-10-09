# Range-Scalp Bot

*Updated Fri Oct 09 22:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9565 | 8259 | 1306 (18) | 0 | $-3209.36 | -5.3% |
| **+10¢** | 7221 | 5690 | 1531 (30) | 0 | $-3124.95 | -6.9% |
| **+15¢** | 6090 | 4478 | 1612 (43) | 1 | $-2572.56 | -6.7% |
| **+20¢** | 5423 | 3749 | 1674 (55) | 2 | $-2125.47 | -6.2% |
| **+10¢ (15¢ stop)** | 11694 | 11659 | 35 (22) | 0 | $-4464.08 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 22:32 | +10 stop | NEAR | UP | 0.63 | 0.74 | 0.84 |
| 10-09 22:32 | +20 | NEAR | UP | 0.63 | 0.86 | 2.08 |
| 10-09 22:32 | +15 | NEAR | UP | 0.63 | 0.82 | 1.66 |
| 10-09 22:32 | +10 | NEAR | UP | 0.63 | 0.74 | 0.84 |
| 10-09 22:32 | +5 | NEAR | UP | 0.63 | 0.68 | 0.22 |
| 10-09 22:31 | +10 stop | XRP | UP | 0.65 | 0.82 | 1.43 |
| 10-09 22:31 | +20 | XRP | UP | 0.65 | 0.89 | 2.17 |
| 10-09 22:31 | +15 | XRP | UP | 0.65 | 0.82 | 1.43 |
| 10-09 22:31 | +10 | XRP | UP | 0.66 | 0.82 | 1.33 |
| 10-09 22:31 | +5 | XRP | UP | 0.66 | 0.71 | 0.19 |
| 10-09 22:31 | +10 stop | HYPE | UP | 0.59 | 0.69 | 0.68 |
| 10-09 22:31 | +10 | HYPE | UP | 0.59 | 0.69 | 0.68 |
| 10-09 22:31 | +5 | HYPE | UP | 0.59 | 0.69 | 0.68 |
| 10-09 22:31 | +10 stop | ZEC | UP | 0.59 | 0.71 | 0.85 |
| 10-09 22:31 | +20 | ZEC | UP | 0.59 | 0.80 | 1.78 |
| 10-09 22:31 | +15 | ZEC | UP | 0.59 | 0.80 | 1.78 |
| 10-09 22:31 | +10 | ZEC | UP | 0.59 | 0.71 | 0.85 |
| 10-09 22:31 | +5 | ZEC | UP | 0.59 | 0.65 | 0.24 |
| 10-09 22:31 | +10 stop | HYPE | DOWN | 0.43 | 0.56 | 0.94 |
| 10-09 22:31 | +20 | HYPE | DOWN | 0.43 | open |  |
| 10-09 22:31 | +15 | HYPE | DOWN | 0.43 | open |  |
| 10-09 22:31 | +10 | HYPE | DOWN | 0.43 | 0.56 | 0.94 |
| 10-09 22:31 | +5 | HYPE | DOWN | 0.43 | 0.56 | 0.94 |
| 10-09 22:31 | +10 stop | DOGE | DOWN | 0.45 | 0.63 | 1.47 |
| 10-09 22:31 | +20 | DOGE | DOWN | 0.45 | open |  |
| 10-09 22:31 | +15 | DOGE | DOWN | 0.45 | 0.63 | 1.47 |
| 10-09 22:31 | +10 | DOGE | DOWN | 0.45 | 0.63 | 1.47 |
| 10-09 22:31 | +5 | DOGE | DOWN | 0.45 | 0.63 | 1.47 |
| 10-09 22:25 | +10 stop | NEAR | DOWN | 0.49 | 0.62 | 0.95 |
| 10-09 22:24 | +5 | NEAR | DOWN | 0.69 | yes | -7.07 |
| 10-09 22:24 | +10 stop | NEAR | UP | 0.53 | 0.38 | -1.85 |
| 10-09 22:24 | +20 | NEAR | UP | 0.53 | 0.75 | 1.88 |
| 10-09 22:24 | +15 | NEAR | UP | 0.52 | 0.75 | 1.98 |
| 10-09 22:24 | +10 | NEAR | UP | 0.52 | 0.63 | 0.75 |
| 10-09 22:24 | +5 | NEAR | UP | 0.53 | 0.58 | 0.14 |
| 10-09 22:17 | +5 | HYPE | UP | 0.69 | 0.87 | 1.57 |
| 10-09 22:16 | +5 | DOGE | UP | 0.65 | 0.72 | 0.39 |
| 10-09 22:16 | +10 stop | SOL | UP | 0.69 | 0.85 | 1.36 |
| 10-09 22:16 | +20 | SOL | UP | 0.69 | 0.91 | 1.97 |
| 10-09 22:16 | +15 | SOL | UP | 0.69 | 0.85 | 1.36 |
