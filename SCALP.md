# Range-Scalp Bot

*Updated Wed Nov 25 04:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71391 | 62316 | 9075 (156) | 2 | $-19001.98 | -4.2% |
| **+10¢** | 53245 | 42643 | 10602 (202) | 2 | $-17622.22 | -5.3% |
| **+15¢** | 44592 | 33179 | 11413 (259) | 2 | $-15656.67 | -5.6% |
| **+20¢** | 39702 | 27683 | 12019 (325) | 2 | $-14062.59 | -5.6% |
| **+10¢ (15¢ stop)** | 86913 | 86710 | 203 (123) | 0 | $-31956.27 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 04:10 | +10 stop | DOGE | DOWN | 0.58 | 0.33 | -2.84 |
| 11-25 04:10 | +5 | DOGE | DOWN | 0.57 | open |  |
| 11-25 04:10 | +10 stop | DOGE | DOWN | 0.52 | 0.62 | 0.65 |
| 11-25 04:10 | +5 | DOGE | DOWN | 0.52 | 0.62 | 0.65 |
| 11-25 04:10 | +10 stop | ZEC | UP | 0.71 | 0.47 | -2.73 |
| 11-25 04:09 | +10 stop | DOGE | DOWN | 0.64 | 0.77 | 1.00 |
| 11-25 04:07 | +10 stop | DOGE | DOWN | 0.68 | 0.49 | -2.24 |
| 11-25 04:07 | +20 | DOGE | DOWN | 0.68 | open |  |
| 11-25 04:07 | +15 | DOGE | DOWN | 0.68 | open |  |
| 11-25 04:07 | +10 | DOGE | DOWN | 0.68 | open |  |
| 11-25 04:07 | +5 | DOGE | DOWN | 0.68 | 0.77 | 0.61 |
| 11-25 04:05 | +10 stop | ZEC | DOWN | 0.61 | 0.43 | -2.14 |
| 11-25 04:02 | +5 | ZEC | DOWN | 0.67 | open |  |
| 11-25 04:01 | +10 stop | ZEC | DOWN | 0.65 | 0.47 | -2.14 |
| 11-25 04:01 | +20 | ZEC | DOWN | 0.65 | open |  |
| 11-25 04:01 | +15 | ZEC | DOWN | 0.66 | open |  |
| 11-25 04:01 | +10 | ZEC | DOWN | 0.66 | open |  |
| 11-25 04:01 | +5 | ZEC | DOWN | 0.66 | 0.71 | 0.19 |
| 11-25 03:58 | +10 stop | BNB | DOWN | 0.40 | 0.56 | 1.23 |
| 11-25 03:57 | +10 stop | XRP | UP | 0.50 | 0.70 | 1.67 |
| 11-25 03:56 | +10 stop | ZEC | DOWN | 0.53 | 0.65 | 0.86 |
| 11-25 03:56 | +20 | ZEC | DOWN | 0.53 | 0.79 | 2.30 |
| 11-25 03:56 | +15 | ZEC | DOWN | 0.53 | 0.79 | 2.30 |
| 11-25 03:56 | +10 | ZEC | DOWN | 0.53 | 0.65 | 0.86 |
| 11-25 03:56 | +5 | ZEC | DOWN | 0.49 | 0.59 | 0.65 |
| 11-25 03:53 | +10 stop | NEAR | UP | 0.67 | 0.77 | 0.71 |
| 11-25 03:53 | +10 | NEAR | UP | 0.67 | 0.77 | 0.71 |
| 11-25 03:53 | +5 | NEAR | UP | 0.67 | 0.77 | 0.71 |
| 11-25 03:50 | +10 stop | XRP | DOWN | 0.63 | 0.41 | -2.58 |
| 11-25 03:50 | +10 stop | SOL | DOWN | 0.61 | 0.75 | 1.09 |
| 11-25 03:49 | +5 | NEAR | UP | 0.65 | 0.70 | 0.19 |
| 11-25 03:49 | +10 stop | NEAR | UP | 0.64 | 0.76 | 0.90 |
| 11-25 03:48 | +10 stop | BNB | DOWN | 0.70 | 0.80 | 0.73 |
| 11-25 03:48 | +5 | XRP | UP | 0.61 | 0.70 | 0.58 |
| 11-25 03:48 | +5 | BTC | DOWN | 0.67 | 0.74 | 0.40 |
| 11-25 03:47 | +10 stop | BTC | DOWN | 0.53 | 0.64 | 0.75 |
| 11-25 03:47 | +20 | BTC | DOWN | 0.53 | 0.74 | 1.78 |
| 11-25 03:47 | +15 | BTC | DOWN | 0.54 | 0.74 | 1.68 |
| 11-25 03:47 | +10 | BTC | DOWN | 0.54 | 0.64 | 0.65 |
| 11-25 03:47 | +5 | BTC | DOWN | 0.54 | 0.59 | 0.15 |
