# Range-Scalp Bot

*Updated Sat Oct 31 00:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41455 | 36177 | 5278 (54) | 4 | $-11604.95 | -4.4% |
| **+10¢** | 30900 | 24793 | 6107 (78) | 4 | $-10341.35 | -5.3% |
| **+15¢** | 25830 | 19248 | 6582 (106) | 4 | $-9407.21 | -5.8% |
| **+20¢** | 22928 | 16035 | 6893 (137) | 5 | $-8277.98 | -5.8% |
| **+10¢ (15¢ stop)** | 50526 | 50451 | 75 (41) | 3 | $-19087.88 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 00:08 | +10 stop | NEAR | UP | 0.56 | 0.67 | 0.80 |
| 10-31 00:08 | +10 stop | DOGE | UP | 0.68 | open |  |
| 10-31 00:07 | +10 stop | BTC | DOWN | 0.69 | open |  |
| 10-31 00:06 | +10 stop | NEAR | UP | 0.52 | 0.62 | 0.65 |
| 10-31 00:05 | +10 stop | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-31 00:04 | +10 stop | NEAR | DOWN | 0.67 | 0.50 | -2.04 |
| 10-31 00:04 | +10 | NEAR | DOWN | 0.67 | open |  |
| 10-31 00:03 | +5 | NEAR | DOWN | 0.69 | open |  |
| 10-31 00:03 | +10 stop | DOGE | DOWN | 0.56 | 0.41 | -1.85 |
| 10-31 00:03 | +10 | DOGE | DOWN | 0.56 | open |  |
| 10-31 00:03 | +5 | XRP | UP | 0.65 | 0.71 | 0.29 |
| 10-31 00:03 | +5 | NEAR | DOWN | 0.57 | 0.62 | 0.15 |
| 10-31 00:03 | +10 stop | SOL | UP | 0.51 | open |  |
| 10-31 00:03 | +10 stop | ZEC | UP | 0.62 | 0.82 | 1.72 |
| 10-31 00:03 | +20 | ZEC | UP | 0.61 | 0.82 | 1.82 |
| 10-31 00:03 | +15 | ZEC | UP | 0.63 | 0.82 | 1.62 |
| 10-31 00:03 | +10 | ZEC | UP | 0.63 | 0.82 | 1.62 |
| 10-31 00:03 | +5 | ZEC | UP | 0.64 | 0.82 | 1.52 |
| 10-31 00:03 | +10 stop | BTC | UP | 0.49 | 0.31 | -2.13 |
| 10-31 00:02 | +10 stop | DOGE | DOWN | 0.56 | 0.68 | 0.86 |
| 10-31 00:02 | +20 | DOGE | DOWN | 0.56 | open |  |
| 10-31 00:02 | +15 | DOGE | DOWN | 0.56 | open |  |
| 10-31 00:02 | +10 | DOGE | DOWN | 0.56 | 0.68 | 0.86 |
| 10-31 00:02 | +10 stop | NEAR | DOWN | 0.53 | 0.66 | 0.96 |
| 10-31 00:02 | +20 | NEAR | DOWN | 0.53 | open |  |
| 10-31 00:02 | +15 | NEAR | DOWN | 0.53 | open |  |
| 10-31 00:02 | +10 | NEAR | DOWN | 0.53 | 0.66 | 0.96 |
| 10-31 00:02 | +5 | NEAR | DOWN | 0.53 | 0.59 | 0.25 |
| 10-31 00:02 | +5 | HYPE | DOWN | 0.66 | 0.71 | 0.19 |
| 10-31 00:01 | +5 | DOGE | DOWN | 0.69 | open |  |
| 10-31 00:01 | +10 stop | SOL | UP | 0.61 | 0.45 | -1.95 |
| 10-31 00:01 | +20 | SOL | UP | 0.61 | open |  |
| 10-31 00:01 | +15 | SOL | UP | 0.61 | open |  |
| 10-31 00:01 | +10 | SOL | UP | 0.61 | open |  |
| 10-31 00:01 | +5 | SOL | UP | 0.61 | open |  |
| 10-31 00:01 | +10 stop | BNB | UP | 0.66 | 0.76 | 0.71 |
| 10-31 00:01 | +20 | BNB | UP | 0.70 | 0.92 | 1.99 |
| 10-31 00:01 | +15 | BNB | UP | 0.70 | 0.85 | 1.26 |
| 10-31 00:01 | +10 | BNB | UP | 0.70 | 0.80 | 0.73 |
| 10-31 00:01 | +5 | BNB | UP | 0.70 | 0.76 | 0.32 |
