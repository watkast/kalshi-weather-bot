# Range-Scalp Bot

*Updated Tue Nov 03 21:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46343 | 40355 | 5988 (72) | 6 | $-13318.33 | -4.6% |
| **+10¢** | 34591 | 27653 | 6938 (96) | 7 | $-12176.49 | -5.6% |
| **+15¢** | 28957 | 21494 | 7463 (124) | 6 | $-11130.80 | -6.1% |
| **+20¢** | 25724 | 17902 | 7822 (164) | 6 | $-9848.29 | -6.1% |
| **+10¢ (15¢ stop)** | 56530 | 56437 | 93 (56) | 0 | $-21201.10 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 21:10 | +10 stop | ZEC | UP | 0.67 | 0.78 | 0.81 |
| 11-03 21:10 | +5 | BNB | DOWN | 0.71 | 0.84 | 1.05 |
| 11-03 21:09 | +10 stop | NEAR | DOWN | 0.70 | 0.53 | -2.02 |
| 11-03 21:09 | +10 | NEAR | DOWN | 0.70 | open |  |
| 11-03 21:09 | +5 | BNB | DOWN | 0.48 | 0.56 | 0.44 |
| 11-03 21:09 | +10 stop | BNB | DOWN | 0.49 | 0.60 | 0.75 |
| 11-03 21:08 | +10 stop | NEAR | DOWN | 0.55 | 0.69 | 1.07 |
| 11-03 21:08 | +10 stop | BNB | DOWN | 0.65 | 0.47 | -2.10 |
| 11-03 21:07 | +10 stop | BTC | UP | 0.71 | 0.51 | -2.33 |
| 11-03 21:07 | +10 stop | NEAR | UP | 0.59 | 0.41 | -2.14 |
| 11-03 21:07 | +5 | NEAR | UP | 0.58 | 0.84 | 2.32 |
| 11-03 21:07 | +5 | BNB | DOWN | 0.56 | 0.67 | 0.76 |
| 11-03 21:06 | +10 stop | BTC | DOWN | 0.52 | 0.63 | 0.75 |
| 11-03 21:06 | +5 | BTC | DOWN | 0.66 | open |  |
| 11-03 21:06 | +10 stop | BNB | DOWN | 0.63 | 0.46 | -2.05 |
| 11-03 21:06 | +10 | BNB | DOWN | 0.63 | 0.75 | 0.89 |
| 11-03 21:06 | +5 | BNB | DOWN | 0.63 | 0.69 | 0.28 |
| 11-03 21:06 | +10 stop | ETH | DOWN | 0.51 | 0.61 | 0.65 |
| 11-03 21:06 | +10 stop | BTC | DOWN | 0.56 | 0.66 | 0.66 |
| 11-03 21:04 | +10 stop | BNB | DOWN | 0.55 | 0.69 | 1.07 |
| 11-03 21:04 | +20 | BNB | DOWN | 0.55 | 0.75 | 1.68 |
| 11-03 21:04 | +15 | BNB | DOWN | 0.55 | 0.75 | 1.68 |
| 11-03 21:04 | +10 | BNB | DOWN | 0.55 | 0.69 | 1.07 |
| 11-03 21:04 | +5 | BNB | DOWN | 0.54 | 0.69 | 1.17 |
| 11-03 21:04 | +10 stop | ZEC | UP | 0.62 | 0.73 | 0.79 |
| 11-03 21:03 | +10 stop | HYPE | UP | 0.59 | 0.79 | 1.71 |
| 11-03 21:03 | +10 stop | ETH | UP | 0.60 | 0.40 | -2.34 |
| 11-03 21:02 | +10 stop | ZEC | UP | 0.60 | 0.42 | -2.15 |
| 11-03 21:02 | +5 | NEAR | DOWN | 0.50 | 0.55 | 0.14 |
| 11-03 21:02 | +5 | BTC | DOWN | 0.60 | 0.66 | 0.27 |
| 11-03 21:02 | +10 stop | XRP | UP | 0.64 | 0.74 | 0.69 |
| 11-03 21:02 | +20 | XRP | UP | 0.64 | 0.86 | 1.94 |
| 11-03 21:02 | +15 | XRP | UP | 0.64 | 0.79 | 1.21 |
| 11-03 21:02 | +10 | XRP | UP | 0.64 | 0.74 | 0.70 |
| 11-03 21:02 | +5 | XRP | UP | 0.64 | 0.74 | 0.70 |
| 11-03 21:02 | +10 stop | NEAR | DOWN | 0.58 | 0.41 | -2.05 |
| 11-03 21:02 | +20 | NEAR | DOWN | 0.58 | 0.78 | 1.69 |
| 11-03 21:02 | +15 | NEAR | DOWN | 0.57 | 0.72 | 1.17 |
| 11-03 21:02 | +10 | NEAR | DOWN | 0.57 | 0.69 | 0.87 |
| 11-03 21:02 | +5 | NEAR | DOWN | 0.57 | 0.62 | 0.15 |
