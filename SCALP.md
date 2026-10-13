# Range-Scalp Bot

*Updated Tue Oct 13 23:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15127 | 13089 | 2038 (27) | 5 | $-4870.45 | -5.1% |
| **+10¢** | 11432 | 9064 | 2368 (39) | 6 | $-4573.87 | -6.4% |
| **+15¢** | 9608 | 7075 | 2533 (58) | 7 | $-4060.04 | -6.7% |
| **+20¢** | 8541 | 5896 | 2645 (74) | 8 | $-3551.65 | -6.6% |
| **+10¢ (15¢ stop)** | 18544 | 18494 | 50 (29) | 4 | $-7159.81 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 23:20 | +10 stop | NEAR | DOWN | 0.56 | open |  |
| 10-13 23:20 | +10 stop | SOL | DOWN | 0.52 | open |  |
| 10-13 23:20 | +10 stop | ZEC | DOWN | 0.64 | open |  |
| 10-13 23:20 | +5 | NEAR | DOWN | 0.59 | open |  |
| 10-13 23:20 | +10 stop | HYPE | DOWN | 0.67 | open |  |
| 10-13 23:20 | +5 | NEAR | UP | 0.44 | 0.53 | 0.54 |
| 10-13 23:19 | +10 stop | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 10-13 23:19 | +5 | BTC | UP | 0.44 | 0.60 | 1.25 |
| 10-13 23:19 | +5 | NEAR | UP | 0.56 | 0.62 | 0.26 |
| 10-13 23:19 | +5 | NEAR | UP | 0.58 | 0.65 | 0.36 |
| 10-13 23:18 | +10 stop | DOGE | DOWN | 0.60 | 0.77 | 1.36 |
| 10-13 23:18 | +10 | DOGE | DOWN | 0.60 | 0.77 | 1.36 |
| 10-13 23:18 | +5 | DOGE | DOWN | 0.57 | 0.66 | 0.56 |
| 10-13 23:18 | +10 stop | XRP | DOWN | 0.56 | 0.75 | 1.58 |
| 10-13 23:18 | +10 | XRP | DOWN | 0.56 | 0.75 | 1.58 |
| 10-13 23:18 | +5 | XRP | DOWN | 0.57 | 0.64 | 0.35 |
| 10-13 23:17 | +5 | SOL | UP | 0.69 | open |  |
| 10-13 23:17 | +5 | ZEC | UP | 0.65 | open |  |
| 10-13 23:17 | +10 stop | DOGE | DOWN | 0.51 | 0.61 | 0.65 |
| 10-13 23:17 | +15 | DOGE | DOWN | 0.51 | 0.66 | 1.16 |
| 10-13 23:17 | +10 | DOGE | DOWN | 0.51 | 0.61 | 0.65 |
| 10-13 23:17 | +5 | DOGE | DOWN | 0.51 | 0.59 | 0.45 |
| 10-13 23:16 | +10 stop | ZEC | UP | 0.60 | 0.40 | -2.39 |
| 10-13 23:16 | +20 | ZEC | UP | 0.60 | open |  |
| 10-13 23:16 | +15 | ZEC | UP | 0.60 | open |  |
| 10-13 23:16 | +10 | ZEC | UP | 0.60 | open |  |
| 10-13 23:16 | +5 | ZEC | UP | 0.60 | 0.66 | 0.22 |
| 10-13 23:16 | +5 | SOL | UP | 0.60 | 0.65 | 0.17 |
| 10-13 23:16 | +10 stop | NEAR | UP | 0.58 | 0.41 | -2.05 |
| 10-13 23:16 | +20 | NEAR | UP | 0.58 | open |  |
| 10-13 23:16 | +15 | NEAR | UP | 0.58 | open |  |
| 10-13 23:16 | +10 | NEAR | UP | 0.58 | open |  |
| 10-13 23:16 | +5 | NEAR | UP | 0.58 | 0.65 | 0.36 |
| 10-13 23:16 | +10 stop | DOGE | UP | 0.49 | 0.64 | 1.15 |
| 10-13 23:16 | +20 | DOGE | UP | 0.49 | open |  |
| 10-13 23:16 | +15 | DOGE | UP | 0.49 | 0.64 | 1.15 |
| 10-13 23:16 | +10 | DOGE | UP | 0.49 | 0.64 | 1.15 |
| 10-13 23:16 | +5 | DOGE | UP | 0.49 | 0.64 | 1.15 |
| 10-13 23:16 | +10 stop | SOL | UP | 0.60 | 0.42 | -2.15 |
| 10-13 23:16 | +20 | SOL | UP | 0.60 | open |  |
