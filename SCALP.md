# Range-Scalp Bot

*Updated Sat Oct 03 09:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 505 | 431 | 74 (1) | 5 | $-208.29 | -6.5% |
| **+10¢** | 388 | 307 | 81 (2) | 7 | $-162.07 | -6.6% |
| **+15¢** | 330 | 243 | 87 (3) | 7 | $-157.54 | -7.6% |
| **+20¢** | 286 | 196 | 90 (3) | 6 | $-153.04 | -8.4% |
| **+10¢ (15¢ stop)** | 674 | 673 | 1 (1) | 5 | $-363.06 | -8.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 09:07 | +10 stop | ZEC | UP | 0.62 | open |  |
| 10-03 09:07 | +10 stop | SOL | UP | 0.63 | open |  |
| 10-03 09:06 | +10 stop | NEAR | DOWN | 0.62 | open |  |
| 10-03 09:06 | +10 stop | DOGE | UP | 0.70 | open |  |
| 10-03 09:06 | +10 stop | ZEC | DOWN | 0.58 | 0.36 | -2.55 |
| 10-03 09:06 | +5 | ZEC | DOWN | 0.56 | open |  |
| 10-03 09:06 | +10 stop | HYPE | UP | 0.66 | 0.76 | 0.71 |
| 10-03 09:06 | +10 stop | SOL | UP | 0.52 | 0.62 | 0.65 |
| 10-03 09:06 | +5 | ZEC | UP | 0.48 | 0.56 | 0.44 |
| 10-03 09:06 | +5 | HYPE | UP | 0.63 | 0.76 | 1.00 |
| 10-03 09:05 | +10 stop | NEAR | UP | 0.63 | 0.45 | -2.14 |
| 10-03 09:05 | +10 stop | ZEC | UP | 0.63 | 0.44 | -2.25 |
| 10-03 09:04 | +10 stop | BTC | UP | 0.70 | open |  |
| 10-03 09:04 | +15 | BTC | UP | 0.70 | open |  |
| 10-03 09:04 | +10 | BTC | UP | 0.70 | open |  |
| 10-03 09:04 | +5 | BTC | UP | 0.70 | 0.76 | 0.32 |
| 10-03 09:03 | +10 stop | NEAR | UP | 0.63 | 0.45 | -2.15 |
| 10-03 09:03 | +10 stop | SOL | UP | 0.59 | 0.70 | 0.78 |
| 10-03 09:03 | +5 | HYPE | UP | 0.55 | 0.60 | 0.15 |
| 10-03 09:03 | +10 stop | ZEC | DOWN | 0.70 | 0.40 | -3.32 |
| 10-03 09:02 | +5 | BTC | UP | 0.62 | 0.71 | 0.58 |
| 10-03 09:02 | +10 stop | HYPE | DOWN | 0.53 | 0.37 | -1.95 |
| 10-03 09:02 | +20 | HYPE | DOWN | 0.51 | open |  |
| 10-03 09:02 | +15 | HYPE | DOWN | 0.51 | open |  |
| 10-03 09:02 | +10 | HYPE | DOWN | 0.51 | open |  |
| 10-03 09:02 | +5 | HYPE | DOWN | 0.51 | 0.57 | 0.24 |
| 10-03 09:01 | +10 stop | BNB | UP | 0.71 | 0.83 | 0.95 |
| 10-03 09:01 | +20 | BNB | UP | 0.71 | 0.92 | 1.86 |
| 10-03 09:01 | +15 | BNB | UP | 0.71 | 0.87 | 1.37 |
| 10-03 09:01 | +10 | BNB | UP | 0.71 | 0.83 | 0.95 |
| 10-03 09:01 | +5 | BNB | UP | 0.71 | 0.80 | 0.63 |
| 10-03 09:01 | +10 stop | NEAR | DOWN | 0.57 | 0.37 | -2.31 |
| 10-03 09:01 | +20 | NEAR | DOWN | 0.57 | open |  |
| 10-03 09:01 | +15 | NEAR | DOWN | 0.57 | open |  |
| 10-03 09:01 | +10 | NEAR | DOWN | 0.57 | open |  |
| 10-03 09:01 | +5 | NEAR | DOWN | 0.57 | open |  |
| 10-03 09:01 | +10 stop | DOGE | DOWN | 0.57 | 0.25 | -3.52 |
| 10-03 09:01 | +20 | DOGE | DOWN | 0.57 | open |  |
| 10-03 09:01 | +15 | DOGE | DOWN | 0.57 | open |  |
| 10-03 09:01 | +10 | DOGE | DOWN | 0.57 | open |  |
