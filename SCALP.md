# Range-Scalp Bot

*Updated Wed Oct 07 07:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6144 | 5328 | 816 (9) | 2 | $-1880.89 | -4.9% |
| **+10¢** | 4684 | 3726 | 958 (16) | 2 | $-1755.73 | -6.0% |
| **+15¢** | 3936 | 2922 | 1014 (20) | 2 | $-1496.70 | -6.1% |
| **+20¢** | 3518 | 2459 | 1059 (27) | 3 | $-1228.82 | -5.6% |
| **+10¢ (15¢ stop)** | 7447 | 7432 | 15 (9) | 1 | $-2564.52 | -5.5% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 07:34 | +10 stop | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 10-07 07:34 | +10 | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 10-07 07:34 | +5 | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 10-07 07:34 | +5 | ZEC | DOWN | 0.68 | open |  |
| 10-07 07:34 | +10 stop | BTC | UP | 0.70 | 0.83 | 1.05 |
| 10-07 07:34 | +20 | BTC | UP | 0.70 | open |  |
| 10-07 07:34 | +15 | BTC | UP | 0.70 | 0.86 | 1.36 |
| 10-07 07:34 | +10 | BTC | UP | 0.70 | 0.83 | 1.05 |
| 10-07 07:34 | +5 | BTC | UP | 0.70 | 0.77 | 0.42 |
| 10-07 07:34 | +5 | SOL | UP | 0.67 | 0.81 | 1.13 |
| 10-07 07:34 | +10 stop | XRP | UP | 0.68 | 0.88 | 1.76 |
| 10-07 07:34 | +20 | XRP | UP | 0.68 | 0.88 | 1.76 |
| 10-07 07:34 | +15 | XRP | UP | 0.68 | 0.88 | 1.76 |
| 10-07 07:34 | +10 | XRP | UP | 0.68 | 0.88 | 1.76 |
| 10-07 07:34 | +5 | XRP | UP | 0.68 | 0.74 | 0.30 |
| 10-07 07:32 | +5 | ZEC | DOWN | 0.59 | 0.64 | 0.16 |
| 10-07 07:32 | +10 stop | NEAR | UP | 0.68 | open |  |
| 10-07 07:32 | +20 | NEAR | UP | 0.68 | open |  |
| 10-07 07:32 | +15 | NEAR | UP | 0.68 | open |  |
| 10-07 07:32 | +10 | NEAR | UP | 0.68 | open |  |
| 10-07 07:32 | +5 | NEAR | UP | 0.68 | open |  |
| 10-07 07:31 | +10 stop | DOGE | UP | 0.66 | 0.79 | 1.02 |
| 10-07 07:31 | +20 | DOGE | UP | 0.66 | 0.89 | 2.07 |
| 10-07 07:31 | +15 | DOGE | UP | 0.66 | 0.89 | 2.07 |
| 10-07 07:31 | +10 | DOGE | UP | 0.66 | 0.79 | 1.02 |
| 10-07 07:31 | +5 | DOGE | UP | 0.66 | 0.71 | 0.19 |
| 10-07 07:31 | +10 stop | ZEC | DOWN | 0.63 | 0.46 | -2.05 |
| 10-07 07:31 | +20 | ZEC | DOWN | 0.63 | open |  |
| 10-07 07:31 | +15 | ZEC | DOWN | 0.63 | open |  |
| 10-07 07:31 | +10 | ZEC | DOWN | 0.63 | open |  |
| 10-07 07:31 | +5 | ZEC | DOWN | 0.63 | 0.70 | 0.38 |
| 10-07 07:31 | +10 stop | SOL | UP | 0.71 | 0.81 | 0.74 |
| 10-07 07:31 | +20 | SOL | UP | 0.71 | 0.92 | 1.87 |
| 10-07 07:31 | +15 | SOL | UP | 0.71 | 0.89 | 1.58 |
| 10-07 07:31 | +10 | SOL | UP | 0.71 | 0.81 | 0.74 |
| 10-07 07:31 | +5 | SOL | UP | 0.71 | 0.76 | 0.22 |
| 10-07 07:23 | +10 stop | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 10-07 07:23 | +10 stop | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 10-07 07:23 | +20 | BTC | DOWN | 0.63 | 0.88 | 2.25 |
| 10-07 07:23 | +15 | BTC | DOWN | 0.63 | 0.88 | 2.25 |
