# Range-Scalp Bot

*Updated Thu Oct 08 12:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7533 | 6526 | 1007 (13) | 2 | $-2356.94 | -5.0% |
| **+10¢** | 5713 | 4525 | 1188 (22) | 4 | $-2318.51 | -6.4% |
| **+15¢** | 4797 | 3544 | 1253 (30) | 4 | $-1932.67 | -6.4% |
| **+20¢** | 4285 | 2986 | 1299 (37) | 5 | $-1535.11 | -5.7% |
| **+10¢ (15¢ stop)** | 9128 | 9101 | 27 (17) | 2 | $-3316.29 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 12:09 | +10 stop | ETH | UP | 0.61 | open |  |
| 10-08 12:09 | +5 | ETH | UP | 0.58 | 0.67 | 0.56 |
| 10-08 12:09 | +10 stop | XRP | DOWN | 0.71 | 0.86 | 1.27 |
| 10-08 12:09 | +20 | XRP | DOWN | 0.71 | open |  |
| 10-08 12:09 | +15 | XRP | DOWN | 0.71 | 0.86 | 1.27 |
| 10-08 12:09 | +10 | XRP | DOWN | 0.71 | 0.86 | 1.27 |
| 10-08 12:09 | +5 | XRP | DOWN | 0.70 | 0.75 | 0.21 |
| 10-08 12:08 | +10 stop | ETH | DOWN | 0.71 | 0.42 | -3.23 |
| 10-08 12:08 | +20 | ETH | DOWN | 0.71 | open |  |
| 10-08 12:08 | +15 | ETH | DOWN | 0.70 | open |  |
| 10-08 12:08 | +10 | ETH | DOWN | 0.70 | open |  |
| 10-08 12:08 | +5 | ETH | DOWN | 0.70 | 0.76 | 0.32 |
| 10-08 12:07 | +10 stop | NEAR | UP | 0.57 | 0.38 | -2.25 |
| 10-08 12:06 | +10 stop | HYPE | DOWN | 0.70 | open |  |
| 10-08 12:06 | +20 | HYPE | DOWN | 0.70 | open |  |
| 10-08 12:06 | +15 | HYPE | DOWN | 0.70 | open |  |
| 10-08 12:06 | +10 | HYPE | DOWN | 0.70 | open |  |
| 10-08 12:06 | +5 | HYPE | DOWN | 0.70 | 0.77 | 0.42 |
| 10-08 12:06 | +20 | NEAR | DOWN | 0.71 | open |  |
| 10-08 12:03 | +15 | NEAR | DOWN | 0.68 | open |  |
| 10-08 12:03 | +10 stop | NEAR | DOWN | 0.69 | 0.53 | -1.93 |
| 10-08 12:03 | +10 | NEAR | DOWN | 0.69 | open |  |
| 10-08 12:03 | +5 | NEAR | DOWN | 0.69 | open |  |
| 10-08 12:03 | +10 stop | NEAR | DOWN | 0.47 | 0.60 | 0.95 |
| 10-08 12:03 | +20 | NEAR | DOWN | 0.47 | 0.71 | 2.07 |
| 10-08 12:03 | +15 | NEAR | DOWN | 0.47 | 0.63 | 1.25 |
| 10-08 12:03 | +10 | NEAR | DOWN | 0.47 | 0.60 | 0.95 |
| 10-08 12:03 | +5 | NEAR | DOWN | 0.47 | 0.60 | 0.95 |
| 10-08 12:02 | +5 | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-08 12:02 | +15 | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 10-08 12:02 | +10 stop | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 10-08 12:02 | +20 | XRP | DOWN | 0.62 | 0.82 | 1.72 |
| 10-08 12:02 | +15 | XRP | DOWN | 0.62 | 0.80 | 1.51 |
| 10-08 12:02 | +10 | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 10-08 12:02 | +5 | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 10-08 12:01 | +10 stop | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-08 12:01 | +10 | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-08 12:01 | +5 | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-08 12:01 | +10 stop | SOL | UP | 0.53 | 0.36 | -2.05 |
| 10-08 12:01 | +20 | SOL | UP | 0.55 | open |  |
