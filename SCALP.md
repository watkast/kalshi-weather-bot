# Range-Scalp Bot

*Updated Fri Oct 30 17:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41008 | 35799 | 5209 (53) | 6 | $-11402.38 | -4.4% |
| **+10¢** | 30553 | 24525 | 6028 (76) | 6 | $-10150.41 | -5.3% |
| **+15¢** | 25541 | 19047 | 6494 (103) | 7 | $-9201.03 | -5.7% |
| **+20¢** | 22670 | 15866 | 6804 (133) | 8 | $-8107.52 | -5.7% |
| **+10¢ (15¢ stop)** | 50005 | 49935 | 70 (37) | 3 | $-18926.36 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 17:10 | +10 stop | XRP | DOWN | 0.68 | open |  |
| 10-30 17:10 | +10 stop | DOGE | UP | 0.55 | open |  |
| 10-30 17:10 | +20 | DOGE | UP | 0.55 | open |  |
| 10-30 17:10 | +15 | DOGE | UP | 0.55 | open |  |
| 10-30 17:10 | +10 | DOGE | UP | 0.55 | open |  |
| 10-30 17:10 | +5 | DOGE | UP | 0.55 | open |  |
| 10-30 17:09 | +10 stop | BNB | DOWN | 0.70 | open |  |
| 10-30 17:09 | +10 stop | XRP | DOWN | 0.55 | 0.69 | 1.07 |
| 10-30 17:07 | +10 stop | SOL | DOWN | 0.57 | 0.74 | 1.38 |
| 10-30 17:07 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-30 17:07 | +10 stop | BNB | UP | 0.65 | 0.47 | -2.14 |
| 10-30 17:07 | +20 | BNB | UP | 0.66 | open |  |
| 10-30 17:07 | +10 | BNB | UP | 0.65 | open |  |
| 10-30 17:07 | +5 | BNB | UP | 0.65 | open |  |
| 10-30 17:06 | +10 stop | XRP | UP | 0.65 | 0.50 | -1.84 |
| 10-30 17:06 | +20 | XRP | UP | 0.65 | open |  |
| 10-30 17:06 | +15 | XRP | UP | 0.65 | open |  |
| 10-30 17:06 | +10 | XRP | UP | 0.65 | open |  |
| 10-30 17:06 | +5 | XRP | UP | 0.65 | open |  |
| 10-30 17:06 | +10 stop | NEAR | UP | 0.65 | 0.44 | -2.44 |
| 10-30 17:06 | +10 | NEAR | UP | 0.65 | open |  |
| 10-30 17:06 | +5 | NEAR | UP | 0.65 | open |  |
| 10-30 17:06 | +10 | SOL | UP | 0.61 | open |  |
| 10-30 17:05 | +10 stop | SOL | UP | 0.64 | 0.45 | -2.25 |
| 10-30 17:04 | +10 stop | XRP | UP | 0.67 | 0.81 | 1.13 |
| 10-30 17:04 | +10 | XRP | UP | 0.67 | 0.81 | 1.13 |
| 10-30 17:04 | +5 | XRP | UP | 0.67 | 0.81 | 1.13 |
| 10-30 17:04 | +15 | BNB | UP | 0.65 | open |  |
| 10-30 17:04 | +5 | BNB | UP | 0.65 | 0.73 | 0.50 |
| 10-30 17:04 | +10 stop | SOL | UP | 0.50 | 0.60 | 0.65 |
| 10-30 17:04 | +10 | SOL | UP | 0.52 | 0.64 | 0.85 |
| 10-30 17:04 | +5 | NEAR | UP | 0.54 | 0.59 | 0.15 |
| 10-30 17:03 | +5 | SOL | UP | 0.66 | open |  |
| 10-30 17:03 | +5 | BTC | UP | 0.65 | open |  |
| 10-30 17:03 | +5 | XRP | UP | 0.59 | 0.64 | 0.16 |
| 10-30 17:02 | +10 stop | ZEC | UP | 0.71 | 0.82 | 0.84 |
| 10-30 17:02 | +10 stop | BNB | UP | 0.62 | 0.73 | 0.79 |
| 10-30 17:02 | +10 | BNB | UP | 0.62 | 0.73 | 0.79 |
| 10-30 17:02 | +5 | BNB | UP | 0.62 | 0.71 | 0.58 |
| 10-30 17:02 | +10 stop | SOL | UP | 0.56 | 0.69 | 0.97 |
