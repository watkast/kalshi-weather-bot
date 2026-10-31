# Range-Scalp Bot

*Updated Sat Oct 31 12:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42236 | 36849 | 5387 (55) | 1 | $-11858.61 | -4.5% |
| **+10¢** | 31487 | 25249 | 6238 (79) | 2 | $-10632.70 | -5.4% |
| **+15¢** | 26333 | 19607 | 6726 (107) | 2 | $-9724.42 | -5.9% |
| **+20¢** | 23386 | 16340 | 7046 (138) | 2 | $-8578.66 | -5.8% |
| **+10¢ (15¢ stop)** | 51512 | 51437 | 75 (41) | 2 | $-19451.89 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 12:15 | +10 stop | XRP | DOWN | 0.46 | open |  |
| 10-31 12:15 | +20 | XRP | DOWN | 0.46 | open |  |
| 10-31 12:15 | +15 | XRP | DOWN | 0.46 | open |  |
| 10-31 12:15 | +10 | XRP | DOWN | 0.46 | open |  |
| 10-31 12:15 | +5 | XRP | DOWN | 0.46 | 0.53 | 0.34 |
| 10-31 12:15 | +10 stop | SOL | DOWN | 0.63 | open |  |
| 10-31 12:15 | +20 | SOL | DOWN | 0.63 | open |  |
| 10-31 12:15 | +15 | SOL | DOWN | 0.64 | open |  |
| 10-31 12:15 | +10 | SOL | DOWN | 0.64 | open |  |
| 10-31 12:15 | +5 | SOL | DOWN | 0.64 | open |  |
| 10-31 12:12 | +10 stop | DOGE | UP | 0.63 | 0.76 | 1.02 |
| 10-31 12:12 | +5 | DOGE | UP | 0.63 | 0.69 | 0.30 |
| 10-31 12:11 | +10 stop | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-31 12:11 | +20 | ZEC | DOWN | 0.71 | yes | -7.25 |
| 10-31 12:11 | +15 | ZEC | DOWN | 0.71 | 0.91 | 1.75 |
| 10-31 12:11 | +10 | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-31 12:11 | +5 | ZEC | DOWN | 0.71 | 0.80 | 0.63 |
| 10-31 12:11 | +10 stop | NEAR | DOWN | 0.67 | 0.79 | 0.92 |
| 10-31 12:11 | +15 | NEAR | DOWN | 0.67 | 0.85 | 1.55 |
| 10-31 12:11 | +10 | NEAR | DOWN | 0.67 | 0.79 | 0.89 |
| 10-31 12:10 | +10 stop | BTC | DOWN | 0.60 | 0.85 | 2.24 |
| 10-31 12:10 | +5 | SOL | UP | 0.64 | 0.89 | 2.26 |
| 10-31 12:10 | +15 | XRP | DOWN | 0.54 | 0.70 | 1.32 |
| 10-31 12:10 | +5 | XRP | DOWN | 0.53 | 0.70 | 1.37 |
| 10-31 12:09 | +10 stop | DOGE | UP | 0.65 | 0.79 | 1.12 |
| 10-31 12:09 | +5 | DOGE | UP | 0.65 | 0.73 | 0.50 |
| 10-31 12:09 | +5 | SOL | UP | 0.54 | 0.59 | 0.15 |
| 10-31 12:08 | +10 stop | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 10-31 12:08 | +10 | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 10-31 12:08 | +5 | XRP | DOWN | 0.66 | 0.72 | 0.29 |
| 10-31 12:08 | +5 | ZEC | DOWN | 0.55 | 0.71 | 1.27 |
| 10-31 12:07 | +10 stop | BTC | DOWN | 0.69 | 0.53 | -1.93 |
| 10-31 12:07 | +20 | BTC | DOWN | 0.69 | 0.90 | 1.88 |
| 10-31 12:07 | +15 | BTC | DOWN | 0.69 | 0.85 | 1.36 |
| 10-31 12:07 | +10 | BTC | DOWN | 0.69 | 0.85 | 1.36 |
| 10-31 12:07 | +5 | BTC | DOWN | 0.68 | 0.85 | 1.45 |
| 10-31 12:07 | +10 stop | NEAR | UP | 0.68 | 0.36 | -3.53 |
| 10-31 12:07 | +5 | NEAR | UP | 0.68 | 0.85 | 1.45 |
| 10-31 12:07 | +10 stop | DOGE | UP | 0.52 | 0.62 | 0.65 |
| 10-31 12:07 | +5 | DOGE | UP | 0.52 | 0.62 | 0.65 |
