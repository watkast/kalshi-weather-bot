# Range-Scalp Bot

*Updated Sun Oct 04 16:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2490 | 2154 | 336 (3) | 2 | $-771.58 | -4.9% |
| **+10¢** | 1948 | 1571 | 377 (4) | 2 | $-589.86 | -4.8% |
| **+15¢** | 1630 | 1232 | 398 (5) | 2 | $-478.81 | -4.7% |
| **+20¢** | 1448 | 1030 | 418 (9) | 3 | $-394.39 | -4.3% |
| **+10¢ (15¢ stop)** | 3085 | 3084 | 1 (1) | 1 | $-1130.62 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 16:10 | +10 stop | ZEC | UP | 0.62 | open |  |
| 10-04 16:10 | +20 | ZEC | UP | 0.63 | open |  |
| 10-04 16:10 | +15 | ZEC | UP | 0.63 | open |  |
| 10-04 16:10 | +10 | ZEC | UP | 0.62 | open |  |
| 10-04 16:10 | +5 | ZEC | UP | 0.63 | open |  |
| 10-04 16:10 | +10 stop | BNB | DOWN | 0.26 | 0.53 | 2.38 |
| 10-04 16:10 | +10 | BNB | DOWN | 0.32 | 0.53 | 1.76 |
| 10-04 16:10 | +5 | BNB | DOWN | 0.32 | 0.53 | 1.76 |
| 10-04 16:07 | +10 stop | NEAR | UP | 0.70 | 0.84 | 1.15 |
| 10-04 16:07 | +10 stop | DOGE | UP | 0.62 | 0.72 | 0.68 |
| 10-04 16:06 | +10 stop | NEAR | DOWN | 0.60 | 0.39 | -2.44 |
| 10-04 16:06 | +10 stop | DOGE | DOWN | 0.58 | 0.36 | -2.59 |
| 10-04 16:05 | +5 | DOGE | UP | 0.70 | 0.75 | 0.21 |
| 10-04 16:04 | +10 stop | DOGE | UP | 0.66 | 0.40 | -2.93 |
| 10-04 16:04 | +10 | DOGE | UP | 0.66 | 0.78 | 0.91 |
| 10-04 16:04 | +5 | DOGE | UP | 0.66 | 0.71 | 0.19 |
| 10-04 16:03 | +10 stop | NEAR | DOWN | 0.65 | 0.47 | -2.14 |
| 10-04 16:03 | +10 stop | SOL | DOWN | 0.66 | 0.79 | 1.02 |
| 10-04 16:02 | +10 stop | DOGE | DOWN | 0.66 | 0.80 | 1.11 |
| 10-04 16:01 | +10 stop | BNB | DOWN | 0.64 | 0.81 | 1.38 |
| 10-04 16:01 | +10 | BNB | DOWN | 0.64 | 0.81 | 1.38 |
| 10-04 16:01 | +5 | BNB | DOWN | 0.64 | 0.72 | 0.44 |
| 10-04 16:01 | +10 stop | HYPE | UP | 0.64 | 0.36 | -3.14 |
| 10-04 16:01 | +20 | HYPE | UP | 0.64 | open |  |
| 10-04 16:01 | +15 | HYPE | UP | 0.64 | open |  |
| 10-04 16:01 | +10 | HYPE | UP | 0.64 | open |  |
| 10-04 16:01 | +5 | HYPE | UP | 0.64 | open |  |
| 10-04 16:01 | +10 stop | NEAR | UP | 0.70 | 0.51 | -2.23 |
| 10-04 16:01 | +20 | NEAR | UP | 0.70 | 0.92 | 2.00 |
| 10-04 16:01 | +15 | NEAR | UP | 0.70 | 0.87 | 1.47 |
| 10-04 16:01 | +10 | NEAR | UP | 0.70 | 0.84 | 1.15 |
| 10-04 16:01 | +5 | NEAR | UP | 0.70 | 0.77 | 0.42 |
| 10-04 16:01 | +10 stop | BNB | UP | 0.53 | 0.63 | 0.65 |
| 10-04 16:01 | +20 | BNB | UP | 0.53 | 0.78 | 2.19 |
| 10-04 16:01 | +15 | BNB | UP | 0.53 | 0.78 | 2.19 |
| 10-04 16:01 | +10 | BNB | UP | 0.53 | 0.63 | 0.65 |
| 10-04 16:01 | +5 | BNB | UP | 0.53 | 0.63 | 0.65 |
| 10-04 16:01 | +10 stop | BTC | DOWN | 0.56 | 0.70 | 1.07 |
| 10-04 16:01 | +20 | BTC | DOWN | 0.56 | 0.76 | 1.69 |
| 10-04 16:01 | +15 | BTC | DOWN | 0.56 | 0.71 | 1.17 |
