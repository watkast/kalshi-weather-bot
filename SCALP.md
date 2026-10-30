# Range-Scalp Bot

*Updated Fri Oct 30 07:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40411 | 35283 | 5128 (51) | 4 | $-11208.31 | -4.4% |
| **+10¢** | 30108 | 24176 | 5932 (74) | 5 | $-9964.37 | -5.3% |
| **+15¢** | 25177 | 18795 | 6382 (101) | 6 | $-8957.91 | -5.7% |
| **+20¢** | 22343 | 15653 | 6690 (130) | 6 | $-7880.35 | -5.6% |
| **+10¢ (15¢ stop)** | 49296 | 49226 | 70 (37) | 0 | $-18648.72 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 07:37 | +10 stop | ZEC | DOWN | 0.71 | 0.87 | 1.37 |
| 10-30 07:37 | +10 | ZEC | DOWN | 0.71 | 0.87 | 1.37 |
| 10-30 07:37 | +5 | ZEC | DOWN | 0.71 | 0.87 | 1.37 |
| 10-30 07:35 | +10 stop | XRP | UP | 0.50 | 0.29 | -2.43 |
| 10-30 07:35 | +15 | XRP | UP | 0.50 | open |  |
| 10-30 07:35 | +10 | XRP | UP | 0.50 | open |  |
| 10-30 07:35 | +5 | XRP | UP | 0.50 | 0.57 | 0.34 |
| 10-30 07:35 | +10 stop | DOGE | DOWN | 0.54 | 0.79 | 2.20 |
| 10-30 07:35 | +20 | DOGE | DOWN | 0.54 | 0.79 | 2.20 |
| 10-30 07:35 | +15 | DOGE | DOWN | 0.54 | 0.79 | 2.20 |
| 10-30 07:35 | +10 | DOGE | DOWN | 0.54 | 0.79 | 2.20 |
| 10-30 07:35 | +5 | DOGE | DOWN | 0.54 | 0.79 | 2.20 |
| 10-30 07:35 | +10 stop | ETH | DOWN | 0.63 | 0.77 | 1.10 |
| 10-30 07:35 | +20 | ETH | DOWN | 0.63 | 0.84 | 1.83 |
| 10-30 07:35 | +15 | ETH | DOWN | 0.63 | 0.84 | 1.83 |
| 10-30 07:35 | +10 | ETH | DOWN | 0.63 | 0.77 | 1.10 |
| 10-30 07:35 | +5 | ETH | DOWN | 0.63 | 0.77 | 1.08 |
| 10-30 07:34 | +10 stop | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 10-30 07:34 | +10 stop | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 10-30 07:34 | +20 | SOL | DOWN | 0.61 | 0.81 | 1.72 |
| 10-30 07:34 | +15 | SOL | DOWN | 0.62 | 0.81 | 1.62 |
| 10-30 07:34 | +10 | SOL | DOWN | 0.62 | 0.75 | 0.99 |
| 10-30 07:34 | +5 | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 10-30 07:34 | +10 stop | SOL | UP | 0.36 | 0.60 | 2.06 |
| 10-30 07:34 | +20 | SOL | UP | 0.36 | 0.60 | 2.06 |
| 10-30 07:34 | +15 | SOL | UP | 0.36 | 0.60 | 2.06 |
| 10-30 07:34 | +10 | SOL | UP | 0.36 | 0.60 | 2.06 |
| 10-30 07:34 | +5 | SOL | UP | 0.36 | 0.60 | 2.06 |
| 10-30 07:34 | +10 stop | XRP | UP | 0.46 | 0.65 | 1.56 |
| 10-30 07:34 | +20 | XRP | UP | 0.46 | open |  |
| 10-30 07:34 | +15 | XRP | UP | 0.46 | 0.65 | 1.56 |
| 10-30 07:34 | +10 | XRP | UP | 0.49 | 0.65 | 1.26 |
| 10-30 07:34 | +5 | XRP | UP | 0.50 | 0.65 | 1.16 |
| 10-30 07:34 | +10 stop | ZEC | UP | 0.44 | 0.56 | 0.84 |
| 10-30 07:34 | +20 | ZEC | UP | 0.44 | open |  |
| 10-30 07:34 | +15 | ZEC | UP | 0.44 | open |  |
| 10-30 07:34 | +10 | ZEC | UP | 0.44 | 0.56 | 0.84 |
| 10-30 07:34 | +5 | ZEC | UP | 0.44 | 0.56 | 0.84 |
| 10-30 07:34 | +10 stop | DOGE | UP | 0.32 | 0.56 | 2.06 |
| 10-30 07:34 | +20 | DOGE | UP | 0.33 | 0.56 | 1.97 |
