# Range-Scalp Bot

*Updated Sun Oct 25 16:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33365 | 29108 | 4257 (42) | 1 | $-9396.10 | -4.5% |
| **+10¢** | 24978 | 20053 | 4925 (60) | 1 | $-8342.84 | -5.3% |
| **+15¢** | 20897 | 15594 | 5303 (83) | 3 | $-7528.47 | -5.7% |
| **+20¢** | 18517 | 12965 | 5552 (105) | 4 | $-6630.21 | -5.7% |
| **+10¢ (15¢ stop)** | 40911 | 40851 | 60 (32) | 0 | $-15607.04 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 16:10 | +10 stop | BNB | UP | 0.42 | 0.55 | 0.94 |
| 10-25 16:09 | +5 | DOGE | DOWN | 0.54 | 0.74 | 1.68 |
| 10-25 16:08 | +10 stop | BTC | DOWN | 0.54 | 0.76 | 1.89 |
| 10-25 16:08 | +20 | BTC | DOWN | 0.54 | 0.76 | 1.89 |
| 10-25 16:08 | +15 | BTC | DOWN | 0.54 | 0.76 | 1.89 |
| 10-25 16:08 | +10 | BTC | DOWN | 0.54 | 0.76 | 1.89 |
| 10-25 16:08 | +5 | BTC | DOWN | 0.54 | 0.76 | 1.89 |
| 10-25 16:08 | +10 stop | ETH | UP | 0.67 | 0.79 | 0.92 |
| 10-25 16:08 | +15 | ETH | UP | 0.67 | open |  |
| 10-25 16:08 | +10 | ETH | UP | 0.67 | 0.79 | 0.92 |
| 10-25 16:08 | +5 | ETH | UP | 0.67 | 0.79 | 0.92 |
| 10-25 16:08 | +10 stop | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 10-25 16:08 | +10 | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 10-25 16:08 | +5 | DOGE | DOWN | 0.63 | 0.69 | 0.28 |
| 10-25 16:07 | +10 stop | XRP | DOWN | 0.53 | 0.65 | 0.86 |
| 10-25 16:07 | +20 | XRP | DOWN | 0.57 | open |  |
| 10-25 16:07 | +15 | XRP | DOWN | 0.57 | 0.72 | 1.17 |
| 10-25 16:07 | +10 | XRP | DOWN | 0.59 | 0.72 | 0.98 |
| 10-25 16:07 | +5 | XRP | DOWN | 0.60 | 0.72 | 0.83 |
| 10-25 16:07 | +10 stop | BNB | DOWN | 0.71 | 0.39 | -3.51 |
| 10-25 16:07 | +20 | BNB | DOWN | 0.70 | open |  |
| 10-25 16:07 | +15 | BNB | DOWN | 0.70 | open |  |
| 10-25 16:07 | +10 | BNB | DOWN | 0.70 | open |  |
| 10-25 16:07 | +5 | BNB | DOWN | 0.70 | open |  |
| 10-25 16:05 | +10 stop | HYPE | UP | 0.67 | 0.79 | 0.92 |
| 10-25 16:05 | +5 | HYPE | UP | 0.67 | 0.72 | 0.19 |
| 10-25 16:04 | +5 | ZEC | UP | 0.66 | 0.72 | 0.29 |
| 10-25 16:03 | +5 | HYPE | UP | 0.64 | 0.69 | 0.18 |
| 10-25 16:03 | +10 stop | NEAR | DOWN | 0.64 | 0.80 | 1.31 |
| 10-25 16:03 | +10 | NEAR | DOWN | 0.64 | 0.80 | 1.31 |
| 10-25 16:03 | +5 | NEAR | DOWN | 0.64 | 0.80 | 1.31 |
| 10-25 16:03 | +5 | XRP | DOWN | 0.70 | 0.79 | 0.63 |
| 10-25 16:02 | +5 | NEAR | DOWN | 0.61 | 0.67 | 0.27 |
| 10-25 16:02 | +10 stop | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 10-25 16:02 | +20 | XRP | DOWN | 0.56 | 0.79 | 2.00 |
| 10-25 16:02 | +15 | XRP | DOWN | 0.56 | 0.79 | 2.00 |
| 10-25 16:02 | +10 | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 10-25 16:02 | +5 | XRP | DOWN | 0.56 | 0.65 | 0.56 |
| 10-25 16:01 | +10 stop | ZEC | UP | 0.67 | 0.82 | 1.23 |
| 10-25 16:01 | +20 | ZEC | UP | 0.67 | 0.89 | 1.97 |
