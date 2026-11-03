# Range-Scalp Bot

*Updated Tue Nov 03 05:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45637 | 39735 | 5902 (69) | 2 | $-13180.53 | -4.6% |
| **+10¢** | 34069 | 27229 | 6840 (91) | 3 | $-12076.68 | -5.6% |
| **+15¢** | 28512 | 21153 | 7359 (119) | 3 | $-11075.07 | -6.2% |
| **+20¢** | 25323 | 17613 | 7710 (154) | 4 | $-9852.41 | -6.2% |
| **+10¢ (15¢ stop)** | 55689 | 55600 | 89 (53) | 1 | $-20967.65 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 05:42 | +10 stop | DOGE | UP | 0.71 | open |  |
| 11-03 05:42 | +20 | DOGE | UP | 0.71 | open |  |
| 11-03 05:42 | +15 | DOGE | UP | 0.71 | open |  |
| 11-03 05:42 | +10 | DOGE | UP | 0.71 | open |  |
| 11-03 05:42 | +5 | DOGE | UP | 0.71 | open |  |
| 11-03 05:42 | +10 stop | SOL | DOWN | 0.51 | 0.11 | -4.25 |
| 11-03 05:42 | +20 | SOL | DOWN | 0.52 | open |  |
| 11-03 05:42 | +15 | SOL | DOWN | 0.52 | open |  |
| 11-03 05:42 | +10 | SOL | DOWN | 0.53 | open |  |
| 11-03 05:42 | +5 | SOL | DOWN | 0.52 | 0.60 | 0.45 |
| 11-03 05:42 | +10 stop | HYPE | DOWN | 0.65 | 0.38 | -3.03 |
| 11-03 05:42 | +20 | HYPE | DOWN | 0.67 | open |  |
| 11-03 05:41 | +15 | HYPE | DOWN | 0.70 | open |  |
| 11-03 05:41 | +10 | HYPE | DOWN | 0.70 | open |  |
| 11-03 05:41 | +5 | HYPE | DOWN | 0.70 | open |  |
| 11-03 05:41 | +10 stop | XRP | UP | 0.70 | 0.96 | 2.38 |
| 11-03 05:41 | +15 | XRP | UP | 0.70 | 0.96 | 2.38 |
| 11-03 05:41 | +10 | XRP | UP | 0.67 | 0.79 | 0.92 |
| 11-03 05:41 | +5 | XRP | UP | 0.67 | 0.75 | 0.50 |
| 11-03 05:35 | +10 stop | NEAR | UP | 0.62 | 0.72 | 0.68 |
| 11-03 05:35 | +15 | NEAR | UP | 0.63 | 0.80 | 1.41 |
| 11-03 05:35 | +10 | NEAR | UP | 0.63 | 0.80 | 1.41 |
| 11-03 05:35 | +5 | NEAR | UP | 0.63 | 0.72 | 0.58 |
| 11-03 05:33 | +10 stop | NEAR | UP | 0.64 | 0.74 | 0.69 |
| 11-03 05:33 | +10 stop | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 11-03 05:33 | +20 | XRP | DOWN | 0.66 | open |  |
| 11-03 05:33 | +15 | XRP | DOWN | 0.66 | 0.83 | 1.44 |
| 11-03 05:33 | +10 | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 11-03 05:33 | +5 | XRP | DOWN | 0.66 | 0.72 | 0.29 |
| 11-03 05:32 | +10 stop | NEAR | DOWN | 0.65 | 0.46 | -2.24 |
| 11-03 05:32 | +10 stop | ZEC | DOWN | 0.67 | 0.93 | 2.41 |
| 11-03 05:32 | +20 | ZEC | DOWN | 0.68 | 0.93 | 2.31 |
| 11-03 05:32 | +15 | ZEC | DOWN | 0.68 | 0.93 | 2.31 |
| 11-03 05:32 | +10 | ZEC | DOWN | 0.68 | 0.93 | 2.31 |
| 11-03 05:32 | +5 | ZEC | DOWN | 0.67 | 0.93 | 2.41 |
| 11-03 05:31 | +10 stop | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-03 05:31 | +20 | DOGE | DOWN | 0.62 | 0.83 | 1.83 |
| 11-03 05:31 | +15 | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-03 05:31 | +10 | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-03 05:31 | +5 | DOGE | DOWN | 0.62 | 0.69 | 0.38 |
