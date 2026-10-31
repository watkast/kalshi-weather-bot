# Range-Scalp Bot

*Updated Sat Oct 31 13:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42294 | 36893 | 5401 (58) | 7 | $-11894.83 | -4.5% |
| **+10¢** | 31531 | 25278 | 6253 (81) | 8 | $-10681.84 | -5.4% |
| **+15¢** | 26368 | 19626 | 6742 (109) | 8 | $-9777.96 | -5.9% |
| **+20¢** | 23418 | 16355 | 7063 (141) | 8 | $-8626.89 | -5.9% |
| **+10¢ (15¢ stop)** | 51587 | 51508 | 79 (44) | 0 | $-19490.69 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 13:55 | +10 stop | ZEC | DOWN | 0.56 | 0.71 | 1.17 |
| 10-31 13:55 | +5 | BTC | DOWN | 0.65 | 0.78 | 1.01 |
| 10-31 13:54 | +10 stop | BTC | UP | 0.46 | 0.30 | -1.93 |
| 10-31 13:54 | +20 | BTC | UP | 0.46 | open |  |
| 10-31 13:54 | +15 | BTC | UP | 0.46 | open |  |
| 10-31 13:54 | +10 | BTC | UP | 0.46 | open |  |
| 10-31 13:54 | +5 | BTC | UP | 0.46 | 0.54 | 0.44 |
| 10-31 13:54 | +10 stop | NEAR | DOWN | 0.56 | 0.67 | 0.76 |
| 10-31 13:54 | +10 stop | ZEC | UP | 0.71 | 0.53 | -2.13 |
| 10-31 13:54 | +10 | ZEC | UP | 0.69 | open |  |
| 10-31 13:54 | +5 | ZEC | UP | 0.70 | open |  |
| 10-31 13:52 | +10 stop | DOGE | DOWN | 0.57 | 0.87 | 2.74 |
| 10-31 13:52 | +10 stop | NEAR | UP | 0.64 | 0.37 | -3.04 |
| 10-31 13:52 | +20 | NEAR | UP | 0.64 | open |  |
| 10-31 13:52 | +15 | NEAR | UP | 0.64 | open |  |
| 10-31 13:52 | +10 | NEAR | UP | 0.64 | open |  |
| 10-31 13:52 | +5 | NEAR | UP | 0.66 | open |  |
| 10-31 13:52 | +10 stop | XRP | DOWN | 0.57 | 0.78 | 1.79 |
| 10-31 13:52 | +10 stop | SOL | UP | 0.61 | 0.07 | -5.63 |
| 10-31 13:52 | +5 | SOL | UP | 0.61 | open |  |
| 10-31 13:52 | +10 stop | SOL | UP | 0.57 | 0.67 | 0.66 |
| 10-31 13:52 | +20 | SOL | UP | 0.57 | open |  |
| 10-31 13:52 | +15 | SOL | UP | 0.57 | open |  |
| 10-31 13:52 | +10 | SOL | UP | 0.58 | open |  |
| 10-31 13:52 | +5 | SOL | UP | 0.58 | 0.67 | 0.56 |
| 10-31 13:51 | +10 stop | HYPE | UP | 0.55 | 0.35 | -2.38 |
| 10-31 13:51 | +10 | HYPE | UP | 0.55 | open |  |
| 10-31 13:51 | +5 | HYPE | UP | 0.55 | open |  |
| 10-31 13:50 | +10 stop | XRP | UP | 0.69 | 0.52 | -1.99 |
| 10-31 13:50 | +20 | XRP | UP | 0.68 | open |  |
| 10-31 13:50 | +15 | XRP | UP | 0.68 | open |  |
| 10-31 13:50 | +10 | XRP | UP | 0.68 | open |  |
| 10-31 13:50 | +5 | XRP | UP | 0.68 | open |  |
| 10-31 13:49 | +10 stop | DOGE | UP | 0.68 | 0.52 | -1.94 |
| 10-31 13:49 | +10 stop | BNB | UP | 0.55 | 0.21 | -3.70 |
| 10-31 13:49 | +10 | BNB | UP | 0.56 | open |  |
| 10-31 13:49 | +5 | BNB | UP | 0.59 | open |  |
| 10-31 13:48 | +15 | DOGE | UP | 0.71 | open |  |
| 10-31 13:48 | +10 | DOGE | UP | 0.71 | open |  |
| 10-31 13:48 | +5 | DOGE | UP | 0.71 | open |  |
