# Range-Scalp Bot

*Updated Fri Oct 23 06:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29882 | 26015 | 3867 (39) | 4 | $-8794.94 | -4.7% |
| **+10¢** | 22403 | 17926 | 4477 (55) | 6 | $-7907.32 | -5.6% |
| **+15¢** | 18757 | 13946 | 4811 (78) | 7 | $-7110.41 | -6.0% |
| **+20¢** | 16603 | 11562 | 5041 (101) | 6 | $-6422.11 | -6.2% |
| **+10¢ (15¢ stop)** | 36677 | 36618 | 59 (32) | 2 | $-13805.65 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 06:25 | +10 stop | ZEC | DOWN | 0.70 | open |  |
| 10-23 06:24 | +5 | ETH | DOWN | 0.58 | 0.74 | 1.28 |
| 10-23 06:24 | +5 | BTC | UP | 0.58 | open |  |
| 10-23 06:24 | +10 stop | NEAR | DOWN | 0.63 | open |  |
| 10-23 06:24 | +20 | NEAR | DOWN | 0.63 | open |  |
| 10-23 06:24 | +15 | NEAR | DOWN | 0.63 | open |  |
| 10-23 06:24 | +10 | NEAR | DOWN | 0.63 | open |  |
| 10-23 06:24 | +5 | NEAR | DOWN | 0.63 | 0.70 | 0.38 |
| 10-23 06:24 | +10 stop | ZEC | UP | 0.68 | 0.53 | -1.84 |
| 10-23 06:24 | +20 | ZEC | UP | 0.68 | open |  |
| 10-23 06:24 | +15 | ZEC | UP | 0.68 | open |  |
| 10-23 06:24 | +10 | ZEC | UP | 0.68 | open |  |
| 10-23 06:24 | +5 | ZEC | UP | 0.68 | open |  |
| 10-23 06:24 | +10 stop | DOGE | UP | 0.63 | 0.48 | -1.85 |
| 10-23 06:24 | +20 | DOGE | UP | 0.63 | open |  |
| 10-23 06:24 | +15 | DOGE | UP | 0.62 | open |  |
| 10-23 06:24 | +10 | DOGE | UP | 0.62 | open |  |
| 10-23 06:24 | +5 | DOGE | UP | 0.62 | 0.68 | 0.27 |
| 10-23 06:24 | +10 stop | ETH | DOWN | 0.52 | 0.74 | 1.88 |
| 10-23 06:24 | +20 | ETH | DOWN | 0.52 | 0.74 | 1.88 |
| 10-23 06:24 | +10 | ETH | DOWN | 0.52 | 0.74 | 1.88 |
| 10-23 06:24 | +5 | ETH | DOWN | 0.52 | 0.57 | 0.14 |
| 10-23 06:23 | +10 stop | BTC | UP | 0.56 | 0.29 | -3.03 |
| 10-23 06:23 | +20 | BTC | UP | 0.56 | open |  |
| 10-23 06:23 | +15 | BTC | UP | 0.56 | open |  |
| 10-23 06:23 | +10 | BTC | UP | 0.56 | open |  |
| 10-23 06:23 | +5 | BTC | UP | 0.56 | 0.63 | 0.35 |
| 10-23 06:22 | +10 stop | XRP | DOWN | 0.66 | 0.82 | 1.34 |
| 10-23 06:22 | +5 | SOL | UP | 0.71 | open |  |
| 10-23 06:20 | +15 | ETH | UP | 0.65 | open |  |
| 10-23 06:20 | +10 stop | ETH | UP | 0.64 | 0.76 | 0.90 |
| 10-23 06:20 | +10 | ETH | UP | 0.64 | 0.76 | 0.90 |
| 10-23 06:20 | +10 stop | SOL | UP | 0.66 | 0.35 | -3.42 |
| 10-23 06:20 | +10 | SOL | UP | 0.66 | open |  |
| 10-23 06:20 | +5 | SOL | UP | 0.66 | 0.71 | 0.19 |
| 10-23 06:20 | +5 | NEAR | UP | 0.64 | 0.70 | 0.28 |
| 10-23 06:20 | +5 | ETH | UP | 0.68 | 0.76 | 0.51 |
| 10-23 06:18 | +10 stop | XRP | DOWN | 0.66 | 0.51 | -1.84 |
| 10-23 06:18 | +10 stop | DOGE | UP | 0.60 | 0.70 | 0.68 |
| 10-23 06:18 | +10 | DOGE | UP | 0.62 | 0.74 | 0.89 |
