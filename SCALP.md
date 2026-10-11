# Range-Scalp Bot

*Updated Sun Oct 11 02:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11277 | 9726 | 1551 (23) | 2 | $-3808.00 | -5.4% |
| **+10¢** | 8544 | 6740 | 1804 (36) | 3 | $-3619.64 | -6.7% |
| **+15¢** | 7198 | 5290 | 1908 (52) | 5 | $-3055.95 | -6.8% |
| **+20¢** | 6408 | 4422 | 1986 (66) | 5 | $-2568.48 | -6.4% |
| **+10¢ (15¢ stop)** | 13892 | 13851 | 41 (25) | 3 | $-5582.93 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 02:31 | +10 stop | ZEC | UP | 0.52 | 0.63 | 0.75 |
| 10-11 02:31 | +20 | ZEC | UP | 0.52 | open |  |
| 10-11 02:31 | +15 | ZEC | UP | 0.52 | open |  |
| 10-11 02:31 | +10 | ZEC | UP | 0.52 | 0.63 | 0.75 |
| 10-11 02:31 | +5 | ZEC | UP | 0.52 | 0.63 | 0.75 |
| 10-11 02:31 | +10 stop | NEAR | UP | 0.55 | 0.67 | 0.86 |
| 10-11 02:31 | +20 | NEAR | UP | 0.55 | open |  |
| 10-11 02:31 | +15 | NEAR | UP | 0.55 | open |  |
| 10-11 02:31 | +10 | NEAR | UP | 0.55 | 0.67 | 0.86 |
| 10-11 02:31 | +5 | NEAR | UP | 0.55 | 0.62 | 0.35 |
| 10-11 02:31 | +10 stop | DOGE | UP | 0.68 | open |  |
| 10-11 02:31 | +20 | DOGE | UP | 0.68 | open |  |
| 10-11 02:31 | +15 | DOGE | UP | 0.68 | open |  |
| 10-11 02:31 | +10 | DOGE | UP | 0.68 | open |  |
| 10-11 02:31 | +5 | DOGE | UP | 0.68 | open |  |
| 10-11 02:31 | +10 stop | BNB | UP | 0.61 | open |  |
| 10-11 02:31 | +20 | BNB | UP | 0.61 | open |  |
| 10-11 02:31 | +15 | BNB | UP | 0.61 | open |  |
| 10-11 02:31 | +10 | BNB | UP | 0.61 | open |  |
| 10-11 02:31 | +5 | BNB | UP | 0.61 | 0.67 | 0.27 |
| 10-11 02:31 | +10 stop | BTC | UP | 0.67 | open |  |
| 10-11 02:31 | +20 | BTC | UP | 0.67 | open |  |
| 10-11 02:31 | +15 | BTC | UP | 0.67 | open |  |
| 10-11 02:31 | +10 | BTC | UP | 0.67 | open |  |
| 10-11 02:31 | +5 | BTC | UP | 0.67 | open |  |
| 10-11 02:29 | +10 stop | SOL | UP | 0.63 | 0.41 | -2.54 |
| 10-11 02:29 | +20 | SOL | UP | 0.63 | 1.00 | 3.48 |
| 10-11 02:29 | +15 | SOL | UP | 0.63 | 1.00 | 3.48 |
| 10-11 02:29 | +10 | SOL | UP | 0.63 | 0.77 | 1.10 |
| 10-11 02:29 | +5 | SOL | UP | 0.63 | 0.77 | 1.10 |
| 10-11 02:28 | +10 stop | XRP | UP | 0.63 | 0.35 | -3.13 |
| 10-11 02:28 | +20 | XRP | UP | 0.63 | no | -6.47 |
| 10-11 02:28 | +15 | XRP | UP | 0.64 | no | -6.57 |
| 10-11 02:28 | +10 | XRP | UP | 0.64 | no | -6.57 |
| 10-11 02:28 | +5 | XRP | UP | 0.64 | no | -6.57 |
| 10-11 02:26 | +10 stop | BTC | UP | 0.63 | 0.48 | -1.85 |
| 10-11 02:26 | +5 | BTC | UP | 0.69 | yes | 2.95 |
| 10-11 02:24 | +5 | BTC | UP | 0.60 | 0.65 | 0.17 |
| 10-11 02:24 | +10 stop | BTC | UP | 0.57 | 0.67 | 0.66 |
| 10-11 02:24 | +5 | BTC | UP | 0.57 | 0.65 | 0.46 |
