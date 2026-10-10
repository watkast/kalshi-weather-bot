# Range-Scalp Bot

*Updated Sat Oct 10 09:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10222 | 8809 | 1413 (22) | 0 | $-3508.72 | -5.4% |
| **+10¢** | 7729 | 6086 | 1643 (34) | 0 | $-3353.29 | -6.9% |
| **+15¢** | 6529 | 4790 | 1739 (49) | 0 | $-2814.54 | -6.9% |
| **+20¢** | 5800 | 3992 | 1808 (63) | 2 | $-2373.46 | -6.5% |
| **+10¢ (15¢ stop)** | 12557 | 12520 | 37 (24) | 0 | $-4940.56 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 09:31 | +10 stop | BNB | UP | 0.55 | 0.70 | 1.17 |
| 10-10 09:31 | +20 | BNB | UP | 0.55 | open |  |
| 10-10 09:31 | +15 | BNB | UP | 0.55 | 0.70 | 1.17 |
| 10-10 09:31 | +10 | BNB | UP | 0.55 | 0.70 | 1.17 |
| 10-10 09:31 | +5 | BNB | UP | 0.55 | 0.70 | 1.17 |
| 10-10 09:30 | +10 stop | DOGE | UP | 0.63 | 0.79 | 1.31 |
| 10-10 09:30 | +20 | DOGE | UP | 0.63 | open |  |
| 10-10 09:30 | +15 | DOGE | UP | 0.63 | 0.79 | 1.31 |
| 10-10 09:30 | +10 | DOGE | UP | 0.63 | 0.79 | 1.31 |
| 10-10 09:30 | +5 | DOGE | UP | 0.63 | 0.70 | 0.38 |
| 10-10 09:28 | +10 stop | BNB | DOWN | 0.65 | 0.40 | -2.87 |
| 10-10 09:26 | +10 stop | BNB | UP | 0.71 | 0.26 | -4.79 |
| 10-10 09:26 | +10 stop | BNB | UP | 0.68 | 0.48 | -2.38 |
| 10-10 09:26 | +20 | BNB | UP | 0.68 | 0.89 | 1.83 |
| 10-10 09:26 | +15 | BNB | UP | 0.68 | 0.89 | 1.83 |
| 10-10 09:26 | +10 | BNB | UP | 0.68 | 0.89 | 1.83 |
| 10-10 09:26 | +5 | BNB | UP | 0.68 | 0.89 | 1.83 |
| 10-10 09:22 | +10 stop | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-10 09:21 | +10 stop | NEAR | UP | 0.62 | 0.76 | 1.10 |
| 10-10 09:21 | +10 stop | ETH | DOWN | 0.58 | 0.71 | 0.94 |
| 10-10 09:20 | +5 | NEAR | DOWN | 0.55 | yes | -5.68 |
| 10-10 09:20 | +10 stop | ETH | DOWN | 0.70 | 0.55 | -1.87 |
| 10-10 09:20 | +20 | ETH | DOWN | 0.70 | 0.91 | 1.92 |
| 10-10 09:20 | +15 | ETH | DOWN | 0.69 | 0.88 | 1.67 |
| 10-10 09:20 | +10 | ETH | DOWN | 0.69 | 0.88 | 1.67 |
| 10-10 09:20 | +5 | ETH | DOWN | 0.69 | 0.75 | 0.31 |
| 10-10 09:19 | +10 stop | BNB | UP | 0.59 | 0.73 | 1.09 |
| 10-10 09:19 | +20 | BNB | UP | 0.59 | 0.84 | 2.23 |
| 10-10 09:19 | +15 | BNB | UP | 0.59 | 0.75 | 1.29 |
| 10-10 09:19 | +10 | BNB | UP | 0.59 | 0.73 | 1.09 |
| 10-10 09:19 | +5 | BNB | UP | 0.59 | 0.68 | 0.57 |
| 10-10 09:19 | +10 stop | BTC | DOWN | 0.69 | 0.45 | -2.73 |
| 10-10 09:19 | +20 | BTC | DOWN | 0.69 | 0.93 | 2.15 |
| 10-10 09:19 | +15 | BTC | DOWN | 0.69 | 0.87 | 1.57 |
| 10-10 09:19 | +10 | BTC | DOWN | 0.69 | 0.87 | 1.57 |
| 10-10 09:19 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-10 09:19 | +10 stop | SOL | DOWN | 0.59 | 0.70 | 0.78 |
| 10-10 09:19 | +20 | SOL | DOWN | 0.59 | 0.86 | 2.44 |
| 10-10 09:19 | +15 | SOL | DOWN | 0.59 | 0.76 | 1.40 |
| 10-10 09:19 | +10 | SOL | DOWN | 0.59 | 0.70 | 0.78 |
