# Range-Scalp Bot

*Updated Sun Oct 18 11:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22515 | 19605 | 2910 (29) | 3 | $-6532.76 | -4.6% |
| **+10¢** | 16939 | 13576 | 3363 (43) | 4 | $-5812.41 | -5.5% |
| **+15¢** | 14181 | 10550 | 3631 (63) | 4 | $-5324.08 | -6.0% |
| **+20¢** | 12552 | 8750 | 3802 (81) | 4 | $-4745.94 | -6.0% |
| **+10¢ (15¢ stop)** | 27674 | 27624 | 50 (29) | 3 | $-10561.90 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 11:32 | +5 | ZEC | DOWN | 0.69 | open |  |
| 10-18 11:31 | +10 stop | DOGE | DOWN | 0.69 | open |  |
| 10-18 11:31 | +20 | DOGE | DOWN | 0.69 | open |  |
| 10-18 11:31 | +15 | DOGE | DOWN | 0.69 | open |  |
| 10-18 11:31 | +10 | DOGE | DOWN | 0.69 | open |  |
| 10-18 11:31 | +5 | DOGE | DOWN | 0.69 | 0.77 | 0.52 |
| 10-18 11:31 | +10 stop | ZEC | UP | 0.47 | open |  |
| 10-18 11:31 | +20 | ZEC | UP | 0.47 | open |  |
| 10-18 11:31 | +15 | ZEC | UP | 0.47 | open |  |
| 10-18 11:31 | +10 | ZEC | UP | 0.47 | open |  |
| 10-18 11:31 | +5 | ZEC | UP | 0.47 | 0.55 | 0.44 |
| 10-18 11:31 | +10 stop | XRP | DOWN | 0.55 | 0.66 | 0.76 |
| 10-18 11:31 | +20 | XRP | DOWN | 0.55 | 0.79 | 2.10 |
| 10-18 11:31 | +15 | XRP | DOWN | 0.55 | 0.74 | 1.58 |
| 10-18 11:31 | +10 | XRP | DOWN | 0.55 | 0.66 | 0.76 |
| 10-18 11:31 | +5 | XRP | DOWN | 0.55 | 0.62 | 0.35 |
| 10-18 11:31 | +10 stop | NEAR | UP | 0.66 | 0.47 | -2.24 |
| 10-18 11:31 | +20 | NEAR | UP | 0.66 | open |  |
| 10-18 11:31 | +15 | NEAR | UP | 0.66 | open |  |
| 10-18 11:31 | +10 | NEAR | UP | 0.66 | open |  |
| 10-18 11:31 | +5 | NEAR | UP | 0.66 | open |  |
| 10-18 11:31 | +10 stop | SOL | UP | 0.63 | open |  |
| 10-18 11:31 | +20 | SOL | UP | 0.63 | open |  |
| 10-18 11:31 | +15 | SOL | UP | 0.63 | open |  |
| 10-18 11:31 | +10 | SOL | UP | 0.63 | open |  |
| 10-18 11:31 | +5 | SOL | UP | 0.63 | open |  |
| 10-18 11:28 | +10 stop | BTC | UP | 0.69 | 0.94 | 2.33 |
| 10-18 11:28 | +20 | BTC | UP | 0.69 | 0.94 | 2.33 |
| 10-18 11:28 | +15 | BTC | UP | 0.69 | 0.94 | 2.33 |
| 10-18 11:28 | +10 | BTC | UP | 0.69 | 0.94 | 2.33 |
| 10-18 11:28 | +5 | BTC | UP | 0.69 | 0.75 | 0.31 |
| 10-18 11:27 | +10 stop | BNB | UP | 0.67 | 0.82 | 1.23 |
| 10-18 11:25 | +10 stop | BTC | UP | 0.62 | 0.78 | 1.30 |
| 10-18 11:25 | +10 | BTC | UP | 0.62 | 0.78 | 1.30 |
| 10-18 11:25 | +5 | BTC | UP | 0.62 | 0.78 | 1.30 |
| 10-18 11:25 | +10 stop | BNB | DOWN | 0.53 | 0.30 | -2.63 |
| 10-18 11:25 | +20 | BNB | DOWN | 0.53 | yes | -5.48 |
| 10-18 11:25 | +15 | BNB | DOWN | 0.53 | yes | -5.48 |
| 10-18 11:25 | +10 | BNB | DOWN | 0.53 | yes | -5.48 |
| 10-18 11:25 | +5 | BNB | DOWN | 0.53 | yes | -5.48 |
