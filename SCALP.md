# Range-Scalp Bot

*Updated Sat Oct 10 13:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10487 | 9044 | 1443 (22) | 0 | $-3551.87 | -5.4% |
| **+10¢** | 7938 | 6257 | 1681 (36) | 2 | $-3382.79 | -6.8% |
| **+15¢** | 6699 | 4919 | 1780 (52) | 1 | $-2843.75 | -6.8% |
| **+20¢** | 5957 | 4103 | 1854 (66) | 1 | $-2404.68 | -6.4% |
| **+10¢ (15¢ stop)** | 12883 | 12845 | 38 (25) | 0 | $-5043.48 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 13:41 | +10 stop | XRP | DOWN | 0.62 | 0.34 | -3.13 |
| 10-10 13:41 | +20 | XRP | DOWN | 0.62 | 0.82 | 1.72 |
| 10-10 13:41 | +15 | XRP | DOWN | 0.62 | 0.82 | 1.72 |
| 10-10 13:41 | +10 | XRP | DOWN | 0.62 | 0.82 | 1.72 |
| 10-10 13:41 | +5 | XRP | DOWN | 0.62 | 0.68 | 0.27 |
| 10-10 13:41 | +10 stop | DOGE | UP | 0.59 | 0.73 | 1.09 |
| 10-10 13:39 | +10 stop | DOGE | DOWN | 0.65 | 0.49 | -1.94 |
| 10-10 13:39 | +10 | DOGE | DOWN | 0.65 | 0.89 | 2.18 |
| 10-10 13:39 | +5 | DOGE | DOWN | 0.65 | 0.89 | 2.17 |
| 10-10 13:38 | +5 | SOL | UP | 0.43 | 0.61 | 1.45 |
| 10-10 13:37 | +10 stop | ETH | DOWN | 0.62 | 0.73 | 0.79 |
| 10-10 13:37 | +15 | ETH | DOWN | 0.62 | 0.87 | 2.25 |
| 10-10 13:37 | +10 | ETH | DOWN | 0.62 | 0.73 | 0.79 |
| 10-10 13:37 | +5 | ETH | DOWN | 0.62 | 0.73 | 0.79 |
| 10-10 13:37 | +10 stop | SOL | UP | 0.66 | 0.46 | -2.34 |
| 10-10 13:37 | +10 stop | DOGE | UP | 0.60 | 0.45 | -1.85 |
| 10-10 13:37 | +5 | XRP | DOWN | 0.61 | 0.74 | 0.99 |
| 10-10 13:37 | +5 | XRP | DOWN | 0.55 | 0.65 | 0.66 |
| 10-10 13:36 | +10 stop | BNB | UP | 0.58 | 0.77 | 1.59 |
| 10-10 13:36 | +5 | DOGE | DOWN | 0.54 | 0.73 | 1.58 |
| 10-10 13:36 | +10 stop | SOL | DOWN | 0.56 | 0.38 | -2.15 |
| 10-10 13:35 | +10 stop | XRP | DOWN | 0.68 | 0.82 | 1.13 |
| 10-10 13:35 | +15 | XRP | DOWN | 0.68 | 0.83 | 1.24 |
| 10-10 13:35 | +10 | XRP | DOWN | 0.68 | 0.82 | 1.13 |
| 10-10 13:35 | +5 | XRP | DOWN | 0.68 | 0.74 | 0.30 |
| 10-10 13:35 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 10-10 13:35 | +10 | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 10-10 13:35 | +5 | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 10-10 13:35 | +10 stop | DOGE | DOWN | 0.60 | 0.41 | -2.24 |
| 10-10 13:35 | +15 | DOGE | DOWN | 0.60 | 0.89 | 2.66 |
| 10-10 13:35 | +10 | DOGE | DOWN | 0.60 | 0.73 | 0.99 |
| 10-10 13:35 | +5 | DOGE | DOWN | 0.60 | 0.67 | 0.37 |
| 10-10 13:35 | +5 | BNB | UP | 0.68 | 0.77 | 0.61 |
| 10-10 13:34 | +5 | BTC | DOWN | 0.61 | 0.66 | 0.17 |
| 10-10 13:34 | +10 stop | SOL | UP | 0.58 | 0.41 | -2.05 |
| 10-10 13:34 | +10 | SOL | UP | 0.58 | open |  |
| 10-10 13:34 | +5 | SOL | UP | 0.58 | 0.65 | 0.36 |
| 10-10 13:33 | +5 | XRP | DOWN | 0.61 | 0.72 | 0.78 |
| 10-10 13:33 | +5 | DOGE | DOWN | 0.55 | 0.71 | 1.27 |
| 10-10 13:32 | +5 | XRP | DOWN | 0.57 | 0.67 | 0.66 |
