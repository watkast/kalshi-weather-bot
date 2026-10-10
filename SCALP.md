# Range-Scalp Bot

*Updated Sat Oct 10 10:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10273 | 8857 | 1416 (22) | 1 | $-3501.42 | -5.4% |
| **+10¢** | 7768 | 6120 | 1648 (34) | 1 | $-3343.23 | -6.8% |
| **+15¢** | 6556 | 4812 | 1744 (49) | 3 | $-2808.60 | -6.8% |
| **+20¢** | 5825 | 4010 | 1815 (63) | 3 | $-2376.27 | -6.5% |
| **+10¢ (15¢ stop)** | 12614 | 12577 | 37 (24) | 0 | $-4945.67 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 10:10 | +10 stop | NEAR | DOWN | 0.69 | 0.52 | -2.08 |
| 10-10 10:10 | +10 | NEAR | DOWN | 0.70 | open |  |
| 10-10 10:10 | +5 | NEAR | DOWN | 0.70 | open |  |
| 10-10 10:09 | +10 stop | ZEC | DOWN | 0.65 | 0.85 | 1.75 |
| 10-10 10:09 | +20 | ZEC | DOWN | 0.64 | 0.85 | 1.85 |
| 10-10 10:09 | +15 | ZEC | DOWN | 0.62 | 0.85 | 2.04 |
| 10-10 10:09 | +10 | ZEC | DOWN | 0.62 | 0.85 | 2.04 |
| 10-10 10:09 | +5 | ZEC | DOWN | 0.62 | 0.71 | 0.58 |
| 10-10 10:07 | +10 stop | NEAR | DOWN | 0.65 | 0.75 | 0.73 |
| 10-10 10:07 | +20 | NEAR | DOWN | 0.65 | open |  |
| 10-10 10:07 | +15 | NEAR | DOWN | 0.65 | open |  |
| 10-10 10:07 | +10 | NEAR | DOWN | 0.65 | 0.75 | 0.73 |
| 10-10 10:07 | +5 | NEAR | DOWN | 0.65 | 0.73 | 0.53 |
| 10-10 10:07 | +10 stop | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-10 10:07 | +10 | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-10 10:07 | +5 | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-10 10:07 | +10 stop | BNB | DOWN | 0.65 | 0.87 | 1.96 |
| 10-10 10:05 | +10 stop | BTC | UP | 0.53 | 0.63 | 0.65 |
| 10-10 10:05 | +10 | BTC | UP | 0.53 | 0.63 | 0.65 |
| 10-10 10:05 | +5 | BTC | UP | 0.53 | 0.63 | 0.65 |
| 10-10 10:05 | +20 | BNB | UP | 0.68 | open |  |
| 10-10 10:05 | +15 | BNB | UP | 0.68 | open |  |
| 10-10 10:05 | +10 stop | BNB | UP | 0.68 | 0.50 | -2.14 |
| 10-10 10:04 | +5 | XRP | DOWN | 0.71 | 0.78 | 0.42 |
| 10-10 10:04 | +10 stop | BNB | DOWN | 0.64 | 0.47 | -2.04 |
| 10-10 10:04 | +10 | BNB | DOWN | 0.64 | 0.87 | 2.06 |
| 10-10 10:04 | +5 | BNB | DOWN | 0.64 | 0.73 | 0.60 |
| 10-10 10:03 | +10 stop | XRP | DOWN | 0.56 | 0.70 | 1.07 |
| 10-10 10:03 | +20 | XRP | DOWN | 0.56 | 0.78 | 1.89 |
| 10-10 10:03 | +15 | XRP | DOWN | 0.56 | 0.78 | 1.89 |
| 10-10 10:03 | +10 | XRP | DOWN | 0.56 | 0.70 | 1.07 |
| 10-10 10:03 | +5 | XRP | DOWN | 0.56 | 0.65 | 0.56 |
| 10-10 10:01 | +10 stop | BNB | UP | 0.41 | 0.53 | 0.85 |
| 10-10 10:01 | +20 | BNB | UP | 0.41 | 0.63 | 1.86 |
| 10-10 10:01 | +15 | BNB | UP | 0.41 | 0.63 | 1.86 |
| 10-10 10:01 | +10 | BNB | UP | 0.41 | 0.53 | 0.85 |
| 10-10 10:01 | +5 | BNB | UP | 0.41 | 0.53 | 0.85 |
| 10-10 10:01 | +10 stop | BTC | UP | 0.58 | 0.69 | 0.77 |
| 10-10 10:01 | +20 | BTC | UP | 0.58 | open |  |
| 10-10 10:01 | +15 | BTC | UP | 0.58 | open |  |
