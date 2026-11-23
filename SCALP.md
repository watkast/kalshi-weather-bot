# Range-Scalp Bot

*Updated Mon Nov 23 03:17 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69510 | 60653 | 8857 (146) | 2 | $-18705.29 | -4.3% |
| **+10¢** | 51868 | 41521 | 10347 (189) | 3 | $-17395.74 | -5.3% |
| **+15¢** | 43462 | 32317 | 11145 (244) | 6 | $-15533.90 | -5.7% |
| **+20¢** | 38705 | 26988 | 11717 (306) | 6 | $-13833.60 | -5.7% |
| **+10¢ (15¢ stop)** | 84621 | 84431 | 190 (118) | 2 | $-31081.91 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 03:17 | +10 stop | NEAR | DOWN | 0.65 | open |  |
| 11-23 03:17 | +20 | NEAR | DOWN | 0.64 | open |  |
| 11-23 03:17 | +15 | NEAR | DOWN | 0.64 | open |  |
| 11-23 03:17 | +10 | NEAR | DOWN | 0.64 | open |  |
| 11-23 03:17 | +5 | NEAR | DOWN | 0.65 | open |  |
| 11-23 03:17 | +10 stop | ZEC | DOWN | 0.71 | open |  |
| 11-23 03:17 | +20 | ZEC | DOWN | 0.71 | open |  |
| 11-23 03:17 | +15 | ZEC | DOWN | 0.71 | open |  |
| 11-23 03:17 | +10 | ZEC | DOWN | 0.71 | open |  |
| 11-23 03:17 | +5 | ZEC | DOWN | 0.71 | open |  |
| 11-23 03:17 | +5 | XRP | DOWN | 0.67 | 0.72 | 0.19 |
| 11-23 03:16 | +10 stop | HYPE | DOWN | 0.51 | 0.61 | 0.65 |
| 11-23 03:16 | +20 | HYPE | DOWN | 0.51 | open |  |
| 11-23 03:16 | +15 | HYPE | DOWN | 0.51 | open |  |
| 11-23 03:16 | +10 | HYPE | DOWN | 0.51 | 0.61 | 0.65 |
| 11-23 03:16 | +5 | HYPE | DOWN | 0.51 | 0.61 | 0.65 |
| 11-23 03:16 | +10 stop | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 11-23 03:16 | +20 | XRP | DOWN | 0.62 | open |  |
| 11-23 03:16 | +15 | XRP | DOWN | 0.62 | open |  |
| 11-23 03:16 | +10 | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 11-23 03:16 | +5 | XRP | DOWN | 0.62 | 0.69 | 0.38 |
| 11-23 03:16 | +10 stop | DOGE | DOWN | 0.56 | 0.67 | 0.76 |
| 11-23 03:16 | +20 | DOGE | DOWN | 0.56 | open |  |
| 11-23 03:16 | +15 | DOGE | DOWN | 0.57 | open |  |
| 11-23 03:16 | +10 | DOGE | DOWN | 0.58 | open |  |
| 11-23 03:16 | +5 | DOGE | DOWN | 0.61 | 0.67 | 0.27 |
| 11-23 03:15 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-23 03:15 | +20 | BTC | DOWN | 0.67 | open |  |
| 11-23 03:15 | +15 | BTC | DOWN | 0.67 | open |  |
| 11-23 03:15 | +10 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-23 03:15 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 11-23 03:09 | +10 stop | ZEC | UP | 0.69 | 0.88 | 1.67 |
| 11-23 03:09 | +5 | ZEC | UP | 0.69 | 0.88 | 1.67 |
| 11-23 03:04 | +10 stop | ZEC | UP | 0.68 | 0.84 | 1.34 |
| 11-23 03:04 | +5 | ZEC | UP | 0.68 | 0.84 | 1.34 |
| 11-23 03:04 | +10 stop | NEAR | UP | 0.69 | 0.79 | 0.73 |
| 11-23 03:04 | +15 | NEAR | UP | 0.69 | 0.85 | 1.36 |
| 11-23 03:04 | +10 | NEAR | UP | 0.68 | 0.79 | 0.82 |
| 11-23 03:04 | +5 | NEAR | UP | 0.68 | 0.79 | 0.82 |
| 11-23 03:03 | +5 | HYPE | UP | 0.68 | 0.76 | 0.49 |
