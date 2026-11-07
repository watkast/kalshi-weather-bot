# Range-Scalp Bot

*Updated Sat Nov 07 07:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50625 | 44129 | 6496 (76) | 1 | $-14223.88 | -4.5% |
| **+10¢** | 37788 | 30219 | 7569 (102) | 1 | $-13191.84 | -5.6% |
| **+15¢** | 31640 | 23488 | 8152 (131) | 1 | $-12082.62 | -6.1% |
| **+20¢** | 28133 | 19589 | 8544 (173) | 1 | $-10660.72 | -6.0% |
| **+10¢ (15¢ stop)** | 61653 | 61554 | 99 (58) | 1 | $-22806.46 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 07:00 | +10 stop | ETH | DOWN | 0.55 | open |  |
| 11-07 07:00 | +20 | ETH | DOWN | 0.55 | open |  |
| 11-07 07:00 | +15 | ETH | DOWN | 0.55 | open |  |
| 11-07 07:00 | +10 | ETH | DOWN | 0.55 | open |  |
| 11-07 07:00 | +5 | ETH | DOWN | 0.55 | open |  |
| 11-07 06:58 | +10 stop | SOL | UP | 0.62 | 0.44 | -2.15 |
| 11-07 06:57 | +10 stop | DOGE | DOWN | 0.70 | 0.83 | 1.05 |
| 11-07 06:57 | +20 | DOGE | DOWN | 0.70 | 0.93 | 2.14 |
| 11-07 06:57 | +15 | DOGE | DOWN | 0.70 | 0.89 | 1.68 |
| 11-07 06:57 | +10 | DOGE | DOWN | 0.70 | 0.83 | 1.05 |
| 11-07 06:57 | +5 | DOGE | DOWN | 0.70 | 0.75 | 0.21 |
| 11-07 06:56 | +10 stop | ETH | UP | 0.29 | 0.54 | 2.17 |
| 11-07 06:56 | +10 stop | SOL | UP | 0.71 | 0.47 | -2.73 |
| 11-07 06:54 | +10 stop | BTC | UP | 0.65 | 0.83 | 1.54 |
| 11-07 06:54 | +5 | BTC | UP | 0.63 | 0.83 | 1.73 |
| 11-07 06:54 | +5 | NEAR | DOWN | 0.67 | 0.73 | 0.30 |
| 11-07 06:54 | +10 stop | XRP | UP | 0.58 | 0.78 | 1.69 |
| 11-07 06:54 | +5 | XRP | UP | 0.58 | 0.78 | 1.69 |
| 11-07 06:52 | +10 stop | NEAR | DOWN | 0.56 | 0.73 | 1.38 |
| 11-07 06:52 | +20 | NEAR | DOWN | 0.56 | 0.96 | 3.79 |
| 11-07 06:52 | +15 | NEAR | DOWN | 0.56 | 0.73 | 1.38 |
| 11-07 06:52 | +10 | NEAR | DOWN | 0.56 | 0.73 | 1.38 |
| 11-07 06:52 | +5 | NEAR | DOWN | 0.56 | 0.62 | 0.25 |
| 11-07 06:52 | +10 stop | SOL | UP | 0.60 | 0.72 | 0.88 |
| 11-07 06:52 | +10 stop | ZEC | UP | 0.64 | 0.82 | 1.52 |
| 11-07 06:51 | +10 stop | SOL | DOWN | 0.61 | 0.43 | -2.15 |
| 11-07 06:51 | +10 | SOL | DOWN | 0.61 | 0.86 | 2.24 |
| 11-07 06:51 | +5 | SOL | DOWN | 0.61 | 0.86 | 2.24 |
| 11-07 06:51 | +5 | XRP | DOWN | 0.57 | 0.69 | 0.87 |
| 11-07 06:47 | +10 stop | ETH | DOWN | 0.67 | 0.48 | -2.24 |
| 11-07 06:47 | +20 | ETH | DOWN | 0.67 | 0.94 | 2.46 |
| 11-07 06:47 | +15 | ETH | DOWN | 0.67 | 0.82 | 1.23 |
| 11-07 06:47 | +10 | ETH | DOWN | 0.67 | 0.79 | 0.92 |
| 11-07 06:47 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 11-07 06:47 | +10 stop | ZEC | DOWN | 0.66 | 0.50 | -1.94 |
| 11-07 06:47 | +20 | ZEC | DOWN | 0.66 | yes | -6.76 |
| 11-07 06:47 | +15 | ZEC | DOWN | 0.66 | yes | -6.76 |
| 11-07 06:47 | +10 | ZEC | DOWN | 0.66 | yes | -6.76 |
| 11-07 06:47 | +5 | ZEC | DOWN | 0.66 | yes | -6.76 |
| 11-07 06:46 | +10 stop | BTC | DOWN | 0.68 | 0.38 | -3.33 |
