# Range-Scalp Bot

*Updated Sat Oct 10 14:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10519 | 9075 | 1444 (22) | 0 | $-3537.29 | -5.3% |
| **+10¢** | 7968 | 6284 | 1684 (36) | 0 | $-3369.47 | -6.7% |
| **+15¢** | 6721 | 4939 | 1782 (52) | 1 | $-2823.02 | -6.7% |
| **+20¢** | 5976 | 4120 | 1856 (66) | 2 | $-2377.90 | -6.3% |
| **+10¢ (15¢ stop)** | 12925 | 12887 | 38 (25) | 0 | $-5055.84 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 14:12 | +10 stop | DOGE | UP | 0.65 | 0.83 | 1.54 |
| 10-10 14:12 | +20 | DOGE | UP | 0.66 | open |  |
| 10-10 14:12 | +15 | DOGE | UP | 0.66 | 0.83 | 1.44 |
| 10-10 14:12 | +10 | DOGE | UP | 0.66 | 0.83 | 1.44 |
| 10-10 14:12 | +5 | DOGE | UP | 0.66 | 0.83 | 1.44 |
| 10-10 14:08 | +10 stop | BNB | UP | 0.69 | 0.93 | 2.15 |
| 10-10 14:08 | +10 | BNB | UP | 0.69 | 0.93 | 2.15 |
| 10-10 14:08 | +5 | BNB | UP | 0.69 | 0.93 | 2.15 |
| 10-10 14:07 | +10 stop | NEAR | UP | 0.69 | 0.84 | 1.20 |
| 10-10 14:07 | +10 | NEAR | UP | 0.69 | 0.84 | 1.20 |
| 10-10 14:07 | +5 | NEAR | UP | 0.69 | 0.76 | 0.37 |
| 10-10 14:07 | +10 stop | BNB | UP | 0.55 | 0.66 | 0.76 |
| 10-10 14:07 | +10 stop | BNB | DOWN | 0.42 | 0.55 | 0.94 |
| 10-10 14:06 | +10 stop | HYPE | UP | 0.70 | 0.84 | 1.15 |
| 10-10 14:06 | +5 | HYPE | UP | 0.70 | 0.77 | 0.42 |
| 10-10 14:06 | +10 stop | NEAR | DOWN | 0.57 | 0.76 | 1.59 |
| 10-10 14:06 | +10 | NEAR | DOWN | 0.58 | 0.76 | 1.49 |
| 10-10 14:06 | +5 | NEAR | DOWN | 0.58 | 0.66 | 0.46 |
| 10-10 14:06 | +5 | BNB | UP | 0.56 | 0.66 | 0.66 |
| 10-10 14:02 | +15 | BTC | DOWN | 0.71 | 0.89 | 1.58 |
| 10-10 14:02 | +10 stop | ZEC | DOWN | 0.68 | 0.78 | 0.73 |
| 10-10 14:02 | +10 stop | BTC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-10 14:02 | +10 | BTC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-10 14:02 | +5 | BTC | DOWN | 0.65 | 0.71 | 0.29 |
| 10-10 14:01 | +10 stop | BNB | UP | 0.55 | 0.39 | -1.95 |
| 10-10 14:01 | +20 | BNB | UP | 0.55 | 0.93 | 3.52 |
| 10-10 14:01 | +15 | BNB | UP | 0.55 | 0.71 | 1.27 |
| 10-10 14:01 | +10 | BNB | UP | 0.55 | 0.66 | 0.76 |
| 10-10 14:01 | +5 | BNB | UP | 0.55 | 0.62 | 0.35 |
| 10-10 14:01 | +5 | DOGE | DOWN | 0.69 | 0.74 | 0.21 |
| 10-10 14:01 | +20 | NEAR | DOWN | 0.71 | open |  |
| 10-10 14:01 | +15 | NEAR | DOWN | 0.71 | open |  |
| 10-10 14:01 | +10 stop | NEAR | DOWN | 0.71 | 0.84 | 1.09 |
| 10-10 14:01 | +10 | NEAR | DOWN | 0.71 | 0.84 | 1.09 |
| 10-10 14:01 | +5 | NEAR | DOWN | 0.71 | 0.77 | 0.36 |
| 10-10 14:01 | +10 stop | HYPE | UP | 0.62 | 0.45 | -2.09 |
| 10-10 14:01 | +20 | HYPE | UP | 0.62 | 0.84 | 1.89 |
| 10-10 14:01 | +15 | HYPE | UP | 0.62 | 0.84 | 1.89 |
| 10-10 14:01 | +10 | HYPE | UP | 0.62 | 0.77 | 1.16 |
| 10-10 14:01 | +5 | HYPE | UP | 0.62 | 0.71 | 0.54 |
