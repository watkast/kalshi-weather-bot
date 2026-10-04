# Range-Scalp Bot

*Updated Sun Oct 04 19:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2698 | 2323 | 375 (3) | 3 | $-910.76 | -5.3% |
| **+10¢** | 2105 | 1684 | 421 (4) | 3 | $-739.83 | -5.6% |
| **+15¢** | 1769 | 1328 | 441 (5) | 4 | $-596.34 | -5.4% |
| **+20¢** | 1574 | 1110 | 464 (9) | 6 | $-517.94 | -5.2% |
| **+10¢ (15¢ stop)** | 3357 | 3356 | 1 (1) | 3 | $-1259.11 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 19:32 | +10 stop | HYPE | UP | 0.67 | open |  |
| 10-04 19:32 | +20 | HYPE | UP | 0.66 | open |  |
| 10-04 19:32 | +15 | HYPE | UP | 0.66 | open |  |
| 10-04 19:32 | +10 | HYPE | UP | 0.66 | open |  |
| 10-04 19:32 | +5 | HYPE | UP | 0.67 | open |  |
| 10-04 19:32 | +10 stop | XRP | UP | 0.64 | 0.75 | 0.79 |
| 10-04 19:32 | +20 | XRP | UP | 0.69 | open |  |
| 10-04 19:32 | +15 | XRP | UP | 0.69 | open |  |
| 10-04 19:32 | +10 stop | DOGE | UP | 0.65 | open |  |
| 10-04 19:32 | +20 | DOGE | UP | 0.67 | open |  |
| 10-04 19:32 | +15 | DOGE | UP | 0.67 | open |  |
| 10-04 19:32 | +10 | DOGE | UP | 0.67 | open |  |
| 10-04 19:32 | +5 | DOGE | UP | 0.67 | open |  |
| 10-04 19:31 | +10 stop | NEAR | UP | 0.66 | open |  |
| 10-04 19:31 | +10 stop | SOL | UP | 0.56 | 0.67 | 0.76 |
| 10-04 19:31 | +20 | SOL | UP | 0.56 | open |  |
| 10-04 19:31 | +15 | SOL | UP | 0.56 | 0.72 | 1.27 |
| 10-04 19:31 | +10 | SOL | UP | 0.56 | 0.67 | 0.76 |
| 10-04 19:31 | +5 | SOL | UP | 0.56 | 0.67 | 0.76 |
| 10-04 19:31 | +10 stop | ZEC | UP | 0.71 | 0.86 | 1.26 |
| 10-04 19:31 | +20 | ZEC | UP | 0.71 | open |  |
| 10-04 19:31 | +15 | ZEC | UP | 0.71 | 0.86 | 1.26 |
| 10-04 19:31 | +10 | ZEC | UP | 0.71 | 0.86 | 1.26 |
| 10-04 19:31 | +5 | ZEC | UP | 0.71 | 0.77 | 0.32 |
| 10-04 19:31 | +10 stop | BNB | UP | 0.58 | 0.78 | 1.72 |
| 10-04 19:31 | +20 | BNB | UP | 0.58 | 0.78 | 1.72 |
| 10-04 19:31 | +15 | BNB | UP | 0.58 | 0.78 | 1.72 |
| 10-04 19:31 | +10 | BNB | UP | 0.58 | 0.78 | 1.73 |
| 10-04 19:31 | +5 | BNB | UP | 0.58 | 0.65 | 0.39 |
| 10-04 19:31 | +10 stop | NEAR | DOWN | 0.49 | 0.34 | -1.84 |
| 10-04 19:31 | +20 | NEAR | DOWN | 0.49 | open |  |
| 10-04 19:31 | +15 | NEAR | DOWN | 0.49 | open |  |
| 10-04 19:31 | +10 | NEAR | DOWN | 0.54 | open |  |
| 10-04 19:31 | +5 | NEAR | DOWN | 0.54 | open |  |
| 10-04 19:27 | +10 stop | ZEC | DOWN | 0.60 | 0.38 | -2.54 |
| 10-04 19:27 | +5 | ZEC | DOWN | 0.60 | yes | -6.17 |
| 10-04 19:26 | +5 | HYPE | UP | 0.70 | 0.76 | 0.32 |
| 10-04 19:26 | +10 stop | HYPE | UP | 0.70 | 0.50 | -2.33 |
| 10-04 19:26 | +10 stop | BNB | DOWN | 0.65 | 0.93 | 2.60 |
| 10-04 19:25 | +10 stop | BNB | UP | 0.58 | 0.42 | -1.96 |
