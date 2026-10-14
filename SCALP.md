# Range-Scalp Bot

*Updated Wed Oct 14 23:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16667 | 14445 | 2222 (28) | 5 | $-5240.21 | -5.0% |
| **+10¢** | 12608 | 10033 | 2575 (40) | 6 | $-4795.75 | -6.0% |
| **+15¢** | 10591 | 7825 | 2766 (59) | 7 | $-4319.02 | -6.5% |
| **+20¢** | 9411 | 6513 | 2898 (76) | 8 | $-3825.15 | -6.5% |
| **+10¢ (15¢ stop)** | 20526 | 20476 | 50 (29) | 5 | $-7902.69 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 23:08 | +10 stop | ZEC | DOWN | 0.66 | open |  |
| 10-14 23:08 | +5 | BNB | DOWN | 0.65 | 0.74 | 0.60 |
| 10-14 23:07 | +10 | XRP | DOWN | 0.68 | open |  |
| 10-14 23:07 | +10 stop | BNB | DOWN | 0.69 | open |  |
| 10-14 23:07 | +10 stop | DOGE | DOWN | 0.65 | open |  |
| 10-14 23:07 | +10 stop | ETH | DOWN | 0.71 | open |  |
| 10-14 23:07 | +5 | XRP | DOWN | 0.71 | open |  |
| 10-14 23:07 | +10 stop | XRP | DOWN | 0.64 | open |  |
| 10-14 23:06 | +10 stop | NEAR | DOWN | 0.61 | 0.76 | 1.20 |
| 10-14 23:06 | +10 | NEAR | DOWN | 0.61 | 0.76 | 1.20 |
| 10-14 23:06 | +5 | NEAR | DOWN | 0.61 | 0.68 | 0.37 |
| 10-14 23:06 | +10 stop | ZEC | UP | 0.70 | 0.47 | -2.63 |
| 10-14 23:06 | +20 | ZEC | UP | 0.70 | open |  |
| 10-14 23:06 | +15 | ZEC | UP | 0.70 | open |  |
| 10-14 23:06 | +10 | ZEC | UP | 0.70 | open |  |
| 10-14 23:06 | +5 | ZEC | UP | 0.70 | open |  |
| 10-14 23:06 | +10 stop | ETH | UP | 0.66 | 0.42 | -2.74 |
| 10-14 23:06 | +20 | ETH | UP | 0.66 | open |  |
| 10-14 23:06 | +15 | ETH | UP | 0.66 | open |  |
| 10-14 23:06 | +10 | ETH | UP | 0.66 | open |  |
| 10-14 23:06 | +5 | ETH | UP | 0.64 | open |  |
| 10-14 23:06 | +10 stop | SOL | DOWN | 0.65 | 0.79 | 1.12 |
| 10-14 23:05 | +10 stop | BTC | UP | 0.64 | 0.44 | -2.35 |
| 10-14 23:05 | +10 | BTC | UP | 0.64 | open |  |
| 10-14 23:05 | +10 stop | DOGE | UP | 0.64 | 0.49 | -1.85 |
| 10-14 23:05 | +10 stop | BNB | UP | 0.56 | 0.34 | -2.54 |
| 10-14 23:04 | +5 | ETH | UP | 0.68 | 0.75 | 0.40 |
| 10-14 23:04 | +10 stop | DOGE | DOWN | 0.53 | 0.38 | -1.85 |
| 10-14 23:04 | +10 stop | NEAR | DOWN | 0.59 | 0.73 | 1.09 |
| 10-14 23:03 | +5 | ZEC | UP | 0.66 | 0.74 | 0.49 |
| 10-14 23:03 | +10 stop | ETH | UP | 0.53 | 0.64 | 0.75 |
| 10-14 23:02 | +10 stop | BNB | DOWN | 0.63 | 0.44 | -2.20 |
| 10-14 23:02 | +10 | BNB | DOWN | 0.63 | 0.74 | 0.84 |
| 10-14 23:02 | +5 | BNB | DOWN | 0.63 | 0.68 | 0.22 |
| 10-14 23:02 | +10 stop | SOL | DOWN | 0.55 | 0.40 | -1.85 |
| 10-14 23:02 | +5 | ZEC | UP | 0.53 | 0.59 | 0.22 |
| 10-14 23:02 | +10 stop | ETH | DOWN | 0.58 | 0.43 | -1.86 |
| 10-14 23:02 | +5 | BTC | DOWN | 0.60 | 0.68 | 0.47 |
| 10-14 23:02 | +10 stop | XRP | DOWN | 0.56 | 0.38 | -2.15 |
| 10-14 23:02 | +20 | XRP | DOWN | 0.56 | open |  |
