# Range-Scalp Bot

*Updated Sun Oct 04 22:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2869 | 2463 | 406 (3) | 2 | $-1021.02 | -5.6% |
| **+10¢** | 2244 | 1789 | 455 (4) | 2 | $-835.77 | -5.9% |
| **+15¢** | 1889 | 1407 | 482 (5) | 2 | $-722.50 | -6.1% |
| **+20¢** | 1683 | 1178 | 505 (9) | 2 | $-627.28 | -5.9% |
| **+10¢ (15¢ stop)** | 3572 | 3571 | 1 (1) | 2 | $-1398.55 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 22:21 | +5 | XRP | UP | 0.65 | open |  |
| 10-04 22:20 | +5 | DOGE | UP | 0.68 | 0.75 | 0.40 |
| 10-04 22:20 | +10 stop | HYPE | UP | 0.59 | open |  |
| 10-04 22:19 | +5 | DOGE | UP | 0.57 | 0.64 | 0.30 |
| 10-04 22:19 | +5 | ETH | UP | 0.66 | 0.73 | 0.40 |
| 10-04 22:18 | +5 | NEAR | DOWN | 0.68 | 0.73 | 0.25 |
| 10-04 22:18 | +10 stop | HYPE | UP | 0.64 | 0.47 | -2.05 |
| 10-04 22:18 | +20 | HYPE | UP | 0.64 | open |  |
| 10-04 22:18 | +15 | HYPE | UP | 0.65 | open |  |
| 10-04 22:18 | +10 | HYPE | UP | 0.65 | open |  |
| 10-04 22:18 | +5 | HYPE | UP | 0.66 | open |  |
| 10-04 22:17 | +10 stop | SOL | UP | 0.60 | 0.71 | 0.78 |
| 10-04 22:17 | +10 | SOL | UP | 0.60 | 0.71 | 0.78 |
| 10-04 22:17 | +5 | SOL | UP | 0.60 | 0.71 | 0.78 |
| 10-04 22:17 | +10 stop | DOGE | UP | 0.57 | 0.70 | 0.97 |
| 10-04 22:17 | +20 | DOGE | UP | 0.57 | 0.80 | 2.00 |
| 10-04 22:17 | +15 | DOGE | UP | 0.57 | 0.75 | 1.48 |
| 10-04 22:17 | +10 | DOGE | UP | 0.57 | 0.70 | 0.97 |
| 10-04 22:17 | +5 | DOGE | UP | 0.57 | 0.63 | 0.25 |
| 10-04 22:17 | +10 stop | XRP | UP | 0.61 | open |  |
| 10-04 22:17 | +20 | XRP | UP | 0.61 | open |  |
| 10-04 22:17 | +15 | XRP | UP | 0.61 | open |  |
| 10-04 22:17 | +10 | XRP | UP | 0.61 | open |  |
| 10-04 22:17 | +5 | XRP | UP | 0.61 | 0.66 | 0.17 |
| 10-04 22:17 | +10 stop | NEAR | DOWN | 0.57 | 0.73 | 1.28 |
| 10-04 22:17 | +20 | NEAR | DOWN | 0.57 | 0.77 | 1.69 |
| 10-04 22:17 | +15 | NEAR | DOWN | 0.57 | 0.73 | 1.28 |
| 10-04 22:17 | +10 | NEAR | DOWN | 0.57 | 0.73 | 1.28 |
| 10-04 22:17 | +5 | NEAR | DOWN | 0.57 | 0.63 | 0.25 |
| 10-04 22:16 | +10 stop | ETH | UP | 0.60 | 0.73 | 0.99 |
| 10-04 22:16 | +20 | ETH | UP | 0.60 | 0.80 | 1.71 |
| 10-04 22:16 | +15 | ETH | UP | 0.60 | 0.76 | 1.30 |
| 10-04 22:16 | +10 | ETH | UP | 0.60 | 0.73 | 0.99 |
| 10-04 22:16 | +5 | ETH | UP | 0.60 | 0.69 | 0.58 |
| 10-04 22:16 | +10 stop | SOL | UP | 0.50 | 0.64 | 1.05 |
| 10-04 22:16 | +20 | SOL | UP | 0.50 | 0.71 | 1.77 |
| 10-04 22:16 | +15 | SOL | UP | 0.50 | 0.71 | 1.77 |
| 10-04 22:16 | +10 | SOL | UP | 0.50 | 0.64 | 1.05 |
| 10-04 22:16 | +5 | SOL | UP | 0.50 | 0.64 | 1.09 |
| 10-04 21:56 | +10 stop | XRP | DOWN | 0.71 | 0.93 | 1.98 |
