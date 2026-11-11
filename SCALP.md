# Range-Scalp Bot

*Updated Wed Nov 11 23:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56346 | 49127 | 7219 (95) | 4 | $-15483.57 | -4.4% |
| **+10¢** | 42104 | 33681 | 8423 (125) | 4 | $-14450.25 | -5.5% |
| **+15¢** | 35307 | 26230 | 9077 (159) | 4 | $-13147.79 | -5.9% |
| **+20¢** | 31455 | 21932 | 9523 (209) | 4 | $-11506.51 | -5.8% |
| **+10¢ (15¢ stop)** | 68665 | 68544 | 121 (73) | 4 | $-25330.31 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 23:21 | +10 stop | XRP | UP | 0.70 | open |  |
| 11-11 23:21 | +10 stop | BNB | UP | 0.71 | open |  |
| 11-11 23:21 | +20 | BNB | UP | 0.70 | open |  |
| 11-11 23:21 | +15 | BNB | UP | 0.70 | open |  |
| 11-11 23:21 | +10 | BNB | UP | 0.69 | open |  |
| 11-11 23:21 | +5 | BNB | UP | 0.69 | open |  |
| 11-11 23:21 | +10 stop | ZEC | DOWN | 0.68 | open |  |
| 11-11 23:21 | +20 | ZEC | DOWN | 0.67 | open |  |
| 11-11 23:21 | +15 | ZEC | DOWN | 0.67 | open |  |
| 11-11 23:21 | +10 | ZEC | DOWN | 0.69 | open |  |
| 11-11 23:21 | +5 | ZEC | DOWN | 0.69 | open |  |
| 11-11 23:21 | +10 stop | NEAR | DOWN | 0.57 | open |  |
| 11-11 23:20 | +10 stop | NEAR | UP | 0.61 | 0.31 | -3.32 |
| 11-11 23:20 | +20 | NEAR | UP | 0.61 | open |  |
| 11-11 23:20 | +15 | NEAR | UP | 0.61 | open |  |
| 11-11 23:20 | +10 | NEAR | UP | 0.61 | open |  |
| 11-11 23:20 | +5 | NEAR | UP | 0.60 | open |  |
| 11-11 23:17 | +15 | XRP | UP | 0.69 | open |  |
| 11-11 23:17 | +10 | XRP | UP | 0.69 | open |  |
| 11-11 23:17 | +5 | XRP | UP | 0.70 | open |  |
| 11-11 23:17 | +10 stop | XRP | UP | 0.71 | 0.41 | -3.31 |
| 11-11 23:17 | +20 | XRP | UP | 0.71 | open |  |
| 11-11 23:16 | +10 stop | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 11-11 23:16 | +20 | ZEC | UP | 0.68 | 0.89 | 1.87 |
| 11-11 23:16 | +15 | ZEC | UP | 0.68 | 0.83 | 1.24 |
| 11-11 23:16 | +10 | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 11-11 23:16 | +5 | ZEC | UP | 0.69 | 0.77 | 0.52 |
| 11-11 23:07 | +5 | NEAR | UP | 0.43 | 0.54 | 0.74 |
| 11-11 23:07 | +10 stop | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 11-11 23:07 | +10 stop | DOGE | DOWN | 0.69 | 0.79 | 0.75 |
| 11-11 23:07 | +10 stop | ZEC | DOWN | 0.64 | 0.76 | 0.90 |
| 11-11 23:07 | +10 stop | BTC | DOWN | 0.65 | 0.78 | 1.01 |
| 11-11 23:06 | +10 stop | HYPE | DOWN | 0.65 | 0.84 | 1.64 |
| 11-11 23:06 | +10 | HYPE | DOWN | 0.65 | 0.84 | 1.64 |
| 11-11 23:06 | +5 | HYPE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-11 23:06 | +10 stop | NEAR | UP | 0.50 | 0.20 | -3.30 |
| 11-11 23:06 | +20 | NEAR | UP | 0.50 | no | -5.18 |
| 11-11 23:06 | +15 | NEAR | UP | 0.50 | no | -5.18 |
| 11-11 23:06 | +10 | NEAR | UP | 0.50 | no | -5.18 |
| 11-11 23:06 | +5 | NEAR | UP | 0.50 | 0.58 | 0.44 |
