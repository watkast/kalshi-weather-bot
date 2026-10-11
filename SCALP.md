# Range-Scalp Bot

*Updated Sun Oct 11 09:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11697 | 10086 | 1611 (24) | 5 | $-3952.16 | -5.4% |
| **+10¢** | 8863 | 6993 | 1870 (37) | 5 | $-3748.38 | -6.7% |
| **+15¢** | 7461 | 5479 | 1982 (53) | 5 | $-3212.93 | -6.9% |
| **+20¢** | 6646 | 4585 | 2061 (67) | 5 | $-2688.97 | -6.4% |
| **+10¢ (15¢ stop)** | 14402 | 14361 | 41 (25) | 0 | $-5709.78 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 09:11 | +10 stop | NEAR | DOWN | 0.35 | 0.67 | 2.88 |
| 10-11 09:10 | +10 stop | BTC | DOWN | 0.71 | 0.44 | -3.03 |
| 10-11 09:10 | +5 | BTC | DOWN | 0.71 | open |  |
| 10-11 09:09 | +15 | BNB | UP | 0.67 | 0.85 | 1.55 |
| 10-11 09:09 | +10 stop | ZEC | DOWN | 0.67 | 0.44 | -2.64 |
| 10-11 09:09 | +15 | ZEC | DOWN | 0.67 | open |  |
| 10-11 09:09 | +10 | ZEC | DOWN | 0.67 | open |  |
| 10-11 09:09 | +5 | ZEC | DOWN | 0.67 | open |  |
| 10-11 09:08 | +10 stop | NEAR | UP | 0.65 | 0.47 | -2.14 |
| 10-11 09:08 | +20 | NEAR | UP | 0.65 | 0.86 | 1.85 |
| 10-11 09:08 | +15 | NEAR | UP | 0.66 | 0.86 | 1.75 |
| 10-11 09:08 | +10 | NEAR | UP | 0.69 | 0.86 | 1.46 |
| 10-11 09:08 | +5 | NEAR | UP | 0.69 | 0.86 | 1.46 |
| 10-11 09:08 | +10 stop | SOL | UP | 0.63 | 0.76 | 1.00 |
| 10-11 09:07 | +10 stop | BTC | DOWN | 0.53 | 0.69 | 1.27 |
| 10-11 09:07 | +10 stop | DOGE | UP | 0.63 | 0.85 | 1.94 |
| 10-11 09:06 | +10 stop | NEAR | DOWN | 0.42 | 0.62 | 1.67 |
| 10-11 09:06 | +20 | NEAR | DOWN | 0.42 | 0.62 | 1.67 |
| 10-11 09:06 | +15 | NEAR | DOWN | 0.42 | 0.62 | 1.65 |
| 10-11 09:06 | +10 | NEAR | DOWN | 0.44 | 0.62 | 1.45 |
| 10-11 09:06 | +5 | NEAR | DOWN | 0.45 | 0.62 | 1.37 |
| 10-11 09:06 | +10 stop | BNB | UP | 0.71 | 0.85 | 1.17 |
| 10-11 09:06 | +10 | BNB | UP | 0.71 | 0.85 | 1.17 |
| 10-11 09:06 | +5 | BNB | UP | 0.71 | 0.79 | 0.54 |
| 10-11 09:05 | +10 stop | ZEC | DOWN | 0.55 | 0.73 | 1.48 |
| 10-11 09:05 | +15 | ZEC | DOWN | 0.55 | 0.73 | 1.48 |
| 10-11 09:05 | +10 | ZEC | DOWN | 0.55 | 0.73 | 1.48 |
| 10-11 09:05 | +5 | ZEC | DOWN | 0.55 | 0.63 | 0.45 |
| 10-11 09:04 | +10 stop | DOGE | UP | 0.55 | 0.76 | 1.79 |
| 10-11 09:03 | +10 stop | DOGE | DOWN | 0.59 | 0.42 | -2.05 |
| 10-11 09:03 | +10 stop | BNB | UP | 0.56 | 0.68 | 0.82 |
| 10-11 09:03 | +20 | BNB | UP | 0.56 | 0.79 | 1.96 |
| 10-11 09:03 | +15 | BNB | UP | 0.56 | 0.73 | 1.34 |
| 10-11 09:03 | +10 | BNB | UP | 0.56 | 0.68 | 0.82 |
| 10-11 09:03 | +5 | BNB | UP | 0.56 | 0.68 | 0.82 |
| 10-11 09:03 | +10 | XRP | UP | 0.68 | 0.81 | 0.99 |
| 10-11 09:03 | +5 | XRP | UP | 0.68 | 0.74 | 0.26 |
| 10-11 09:02 | +10 stop | SOL | UP | 0.59 | 0.77 | 1.47 |
| 10-11 09:02 | +10 stop | ETH | UP | 0.69 | 0.79 | 0.73 |
| 10-11 09:02 | +10 stop | XRP | UP | 0.70 | 0.81 | 0.84 |
