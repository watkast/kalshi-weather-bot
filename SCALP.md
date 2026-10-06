# Range-Scalp Bot

*Updated Tue Oct 06 03:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4555 | 3930 | 625 (6) | 3 | $-1520.49 | -5.3% |
| **+10¢** | 3504 | 2780 | 724 (9) | 3 | $-1393.33 | -6.3% |
| **+15¢** | 2943 | 2178 | 765 (12) | 3 | $-1198.40 | -6.5% |
| **+20¢** | 2642 | 1846 | 796 (17) | 3 | $-983.27 | -5.9% |
| **+10¢ (15¢ stop)** | 5598 | 5587 | 11 (6) | 2 | $-2050.06 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 03:07 | +10 stop | ETH | UP | 0.48 | 0.58 | 0.64 |
| 10-06 03:07 | +10 stop | SOL | UP | 0.70 | open |  |
| 10-06 03:06 | +10 stop | NEAR | DOWN | 0.62 | open |  |
| 10-06 03:06 | +5 | NEAR | DOWN | 0.62 | open |  |
| 10-06 03:05 | +10 stop | ETH | DOWN | 0.55 | 0.28 | -3.03 |
| 10-06 03:05 | +10 stop | SOL | DOWN | 0.58 | 0.36 | -2.55 |
| 10-06 03:05 | +10 stop | DOGE | UP | 0.63 | 0.76 | 1.00 |
| 10-06 03:05 | +20 | DOGE | UP | 0.63 | 0.83 | 1.73 |
| 10-06 03:05 | +15 | DOGE | UP | 0.63 | 0.80 | 1.41 |
| 10-06 03:05 | +10 | DOGE | UP | 0.63 | 0.76 | 1.00 |
| 10-06 03:05 | +5 | DOGE | UP | 0.63 | 0.69 | 0.28 |
| 10-06 03:05 | +10 stop | XRP | UP | 0.59 | 0.82 | 2.02 |
| 10-06 03:05 | +20 | XRP | UP | 0.59 | 0.82 | 2.02 |
| 10-06 03:05 | +15 | XRP | UP | 0.59 | 0.82 | 2.02 |
| 10-06 03:05 | +10 | XRP | UP | 0.59 | 0.82 | 2.02 |
| 10-06 03:05 | +5 | XRP | UP | 0.59 | 0.66 | 0.37 |
| 10-06 03:04 | +5 | NEAR | UP | 0.51 | 0.57 | 0.24 |
| 10-06 03:04 | +5 | NEAR | UP | 0.59 | 0.64 | 0.16 |
| 10-06 03:03 | +10 stop | ETH | UP | 0.69 | 0.53 | -1.93 |
| 10-06 03:03 | +20 | ETH | UP | 0.69 | open |  |
| 10-06 03:03 | +15 | ETH | UP | 0.69 | open |  |
| 10-06 03:03 | +10 | ETH | UP | 0.69 | open |  |
| 10-06 03:03 | +5 | ETH | UP | 0.69 | open |  |
| 10-06 03:03 | +10 stop | SOL | UP | 0.70 | 0.52 | -2.13 |
| 10-06 03:02 | +5 | DOGE | UP | 0.60 | 0.70 | 0.68 |
| 10-06 03:02 | +10 stop | ETH | UP | 0.55 | 0.65 | 0.66 |
| 10-06 03:02 | +20 | ETH | UP | 0.55 | 0.78 | 1.99 |
| 10-06 03:02 | +15 | ETH | UP | 0.55 | 0.78 | 1.99 |
| 10-06 03:02 | +10 | ETH | UP | 0.55 | 0.65 | 0.66 |
| 10-06 03:02 | +5 | ETH | UP | 0.55 | 0.65 | 0.66 |
| 10-06 03:01 | +10 stop | DOGE | UP | 0.59 | 0.70 | 0.78 |
| 10-06 03:01 | +20 | DOGE | UP | 0.59 | 0.80 | 1.81 |
| 10-06 03:01 | +15 | DOGE | UP | 0.59 | 0.78 | 1.60 |
| 10-06 03:01 | +10 | DOGE | UP | 0.59 | 0.70 | 0.78 |
| 10-06 03:01 | +5 | DOGE | UP | 0.56 | 0.61 | 0.15 |
| 10-06 03:01 | +10 stop | NEAR | UP | 0.64 | 0.48 | -1.95 |
| 10-06 03:01 | +20 | NEAR | UP | 0.64 | open |  |
| 10-06 03:01 | +15 | NEAR | UP | 0.64 | open |  |
| 10-06 03:01 | +10 | NEAR | UP | 0.64 | open |  |
| 10-06 03:01 | +5 | NEAR | UP | 0.64 | 0.71 | 0.38 |
