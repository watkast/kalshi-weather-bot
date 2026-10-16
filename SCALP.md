# Range-Scalp Bot

*Updated Fri Oct 16 12:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19194 | 16679 | 2515 (29) | 8 | $-5779.87 | -4.8% |
| **+10¢** | 14470 | 11561 | 2909 (41) | 8 | $-5221.43 | -5.7% |
| **+15¢** | 12114 | 8983 | 3131 (60) | 8 | $-4727.87 | -6.2% |
| **+20¢** | 10748 | 7465 | 3283 (79) | 8 | $-4214.56 | -6.2% |
| **+10¢ (15¢ stop)** | 23620 | 23570 | 50 (29) | 2 | $-9111.91 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 12:21 | +10 stop | BNB | UP | 0.71 | 0.81 | 0.74 |
| 10-16 12:21 | +10 stop | NEAR | UP | 0.69 | open |  |
| 10-16 12:20 | +10 stop | BTC | UP | 0.67 | 0.77 | 0.71 |
| 10-16 12:20 | +10 stop | XRP | UP | 0.71 | open |  |
| 10-16 12:19 | +10 stop | SOL | UP | 0.59 | 0.75 | 1.29 |
| 10-16 12:18 | +10 stop | BNB | DOWN | 0.54 | 0.32 | -2.54 |
| 10-16 12:18 | +10 stop | ZEC | UP | 0.60 | 0.71 | 0.75 |
| 10-16 12:18 | +10 stop | BTC | UP | 0.64 | 0.45 | -2.25 |
| 10-16 12:18 | +10 stop | HYPE | UP | 0.64 | 0.84 | 1.73 |
| 10-16 12:18 | +20 | HYPE | UP | 0.64 | 0.84 | 1.73 |
| 10-16 12:18 | +15 | HYPE | UP | 0.64 | 0.84 | 1.73 |
| 10-16 12:18 | +10 | HYPE | UP | 0.63 | 0.84 | 1.83 |
| 10-16 12:18 | +5 | HYPE | UP | 0.63 | 0.68 | 0.17 |
| 10-16 12:18 | +10 stop | NEAR | UP | 0.63 | 0.47 | -1.95 |
| 10-16 12:18 | +10 stop | XRP | UP | 0.55 | 0.40 | -1.86 |
| 10-16 12:18 | +10 stop | DOGE | UP | 0.65 | 0.78 | 1.01 |
| 10-16 12:17 | +10 stop | ETH | UP | 0.67 | 0.78 | 0.81 |
| 10-16 12:17 | +10 stop | BNB | DOWN | 0.68 | 0.52 | -1.94 |
| 10-16 12:17 | +20 | BNB | DOWN | 0.68 | open |  |
| 10-16 12:17 | +15 | BNB | DOWN | 0.68 | open |  |
| 10-16 12:17 | +10 | BNB | DOWN | 0.68 | open |  |
| 10-16 12:17 | +5 | BNB | DOWN | 0.68 | open |  |
| 10-16 12:17 | +10 stop | SOL | DOWN | 0.67 | 0.43 | -2.74 |
| 10-16 12:17 | +20 | SOL | DOWN | 0.67 | open |  |
| 10-16 12:17 | +15 | SOL | DOWN | 0.67 | open |  |
| 10-16 12:17 | +10 | SOL | DOWN | 0.67 | open |  |
| 10-16 12:17 | +5 | SOL | DOWN | 0.67 | open |  |
| 10-16 12:16 | +10 stop | XRP | DOWN | 0.66 | 0.45 | -2.44 |
| 10-16 12:16 | +20 | XRP | DOWN | 0.66 | open |  |
| 10-16 12:16 | +15 | XRP | DOWN | 0.66 | open |  |
| 10-16 12:16 | +10 | XRP | DOWN | 0.66 | open |  |
| 10-16 12:16 | +5 | XRP | DOWN | 0.66 | open |  |
| 10-16 12:16 | +10 stop | NEAR | DOWN | 0.56 | 0.39 | -2.05 |
| 10-16 12:16 | +20 | NEAR | DOWN | 0.56 | open |  |
| 10-16 12:16 | +15 | NEAR | DOWN | 0.56 | open |  |
| 10-16 12:16 | +10 | NEAR | DOWN | 0.56 | open |  |
| 10-16 12:16 | +5 | NEAR | DOWN | 0.56 | open |  |
| 10-16 12:16 | +10 stop | DOGE | DOWN | 0.62 | 0.46 | -1.95 |
| 10-16 12:16 | +20 | DOGE | DOWN | 0.62 | open |  |
| 10-16 12:16 | +15 | DOGE | DOWN | 0.62 | open |  |
