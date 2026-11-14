# Range-Scalp Bot

*Updated Sat Nov 14 11:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59396 | 51831 | 7565 (107) | 4 | $-16001.41 | -4.3% |
| **+10¢** | 44363 | 35508 | 8855 (142) | 4 | $-15010.01 | -5.4% |
| **+15¢** | 37178 | 27629 | 9549 (178) | 4 | $-13638.73 | -5.8% |
| **+20¢** | 33119 | 23096 | 10023 (230) | 4 | $-12015.71 | -5.8% |
| **+10¢ (15¢ stop)** | 72267 | 72125 | 142 (82) | 0 | $-26582.23 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 11:39 | +5 | NEAR | DOWN | 0.59 | open |  |
| 11-14 11:38 | +10 stop | XRP | DOWN | 0.61 | 0.43 | -2.15 |
| 11-14 11:37 | +10 stop | NEAR | DOWN | 0.66 | 0.43 | -2.64 |
| 11-14 11:36 | +10 stop | XRP | DOWN | 0.45 | 0.57 | 0.84 |
| 11-14 11:36 | +5 | NEAR | DOWN | 0.65 | 0.71 | 0.29 |
| 11-14 11:36 | +5 | DOGE | DOWN | 0.71 | open |  |
| 11-14 11:35 | +10 stop | SOL | DOWN | 0.67 | 0.50 | -2.03 |
| 11-14 11:35 | +20 | SOL | DOWN | 0.67 | open |  |
| 11-14 11:35 | +15 | SOL | DOWN | 0.67 | open |  |
| 11-14 11:35 | +10 | SOL | DOWN | 0.67 | open |  |
| 11-14 11:35 | +5 | SOL | DOWN | 0.67 | open |  |
| 11-14 11:35 | +10 stop | DOGE | DOWN | 0.71 | 0.51 | -2.33 |
| 11-14 11:35 | +15 | DOGE | DOWN | 0.71 | open |  |
| 11-14 11:35 | +10 | DOGE | DOWN | 0.71 | open |  |
| 11-14 11:35 | +5 | DOGE | DOWN | 0.71 | 0.77 | 0.32 |
| 11-14 11:35 | +10 stop | NEAR | DOWN | 0.71 | 0.55 | -1.93 |
| 11-14 11:35 | +20 | NEAR | DOWN | 0.71 | open |  |
| 11-14 11:35 | +15 | NEAR | DOWN | 0.71 | open |  |
| 11-14 11:35 | +10 | NEAR | DOWN | 0.71 | open |  |
| 11-14 11:35 | +5 | NEAR | DOWN | 0.71 | 0.78 | 0.42 |
| 11-14 11:33 | +10 stop | XRP | DOWN | 0.69 | 0.54 | -1.83 |
| 11-14 11:33 | +20 | XRP | DOWN | 0.69 | open |  |
| 11-14 11:33 | +15 | XRP | DOWN | 0.69 | open |  |
| 11-14 11:33 | +10 | XRP | DOWN | 0.69 | open |  |
| 11-14 11:33 | +5 | XRP | DOWN | 0.69 | open |  |
| 11-14 11:31 | +10 stop | NEAR | DOWN | 0.66 | 0.79 | 1.02 |
| 11-14 11:31 | +20 | NEAR | DOWN | 0.66 | 0.88 | 1.96 |
| 11-14 11:31 | +15 | NEAR | DOWN | 0.66 | 0.88 | 1.96 |
| 11-14 11:31 | +10 | NEAR | DOWN | 0.66 | 0.79 | 1.02 |
| 11-14 11:31 | +5 | NEAR | DOWN | 0.66 | 0.74 | 0.50 |
| 11-14 11:31 | +10 stop | DOGE | DOWN | 0.69 | 0.85 | 1.36 |
| 11-14 11:31 | +20 | DOGE | DOWN | 0.69 | open |  |
| 11-14 11:31 | +15 | DOGE | DOWN | 0.69 | 0.85 | 1.36 |
| 11-14 11:31 | +10 | DOGE | DOWN | 0.69 | 0.85 | 1.36 |
| 11-14 11:31 | +5 | DOGE | DOWN | 0.69 | 0.74 | 0.21 |
| 11-14 11:28 | +10 stop | BTC | UP | 0.22 | 0.54 | 2.89 |
| 11-14 11:27 | +10 stop | BTC | UP | 0.58 | 0.42 | -1.96 |
| 11-14 11:27 | +10 | BTC | UP | 0.58 | no | -5.98 |
| 11-14 11:27 | +5 | BTC | UP | 0.58 | no | -5.98 |
| 11-14 11:25 | +10 stop | BTC | DOWN | 0.58 | 0.70 | 0.87 |
