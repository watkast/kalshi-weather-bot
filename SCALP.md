# Range-Scalp Bot

*Updated Sun Oct 11 17:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12209 | 10528 | 1681 (24) | 1 | $-4100.38 | -5.3% |
| **+10¢** | 9276 | 7326 | 1950 (37) | 1 | $-3874.01 | -6.6% |
| **+15¢** | 7818 | 5747 | 2071 (54) | 1 | $-3324.75 | -6.8% |
| **+20¢** | 6966 | 4808 | 2158 (68) | 1 | $-2829.95 | -6.5% |
| **+10¢ (15¢ stop)** | 15039 | 14998 | 41 (25) | 1 | $-5934.39 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 17:03 | +10 stop | NEAR | DOWN | 0.65 | open |  |
| 10-11 17:02 | +10 stop | NEAR | DOWN | 0.71 | 0.54 | -2.03 |
| 10-11 17:02 | +20 | NEAR | DOWN | 0.71 | open |  |
| 10-11 17:02 | +15 | NEAR | DOWN | 0.71 | open |  |
| 10-11 17:02 | +10 | NEAR | DOWN | 0.71 | open |  |
| 10-11 17:02 | +5 | NEAR | DOWN | 0.71 | open |  |
| 10-11 16:56 | +10 stop | BNB | DOWN | 0.59 | 0.75 | 1.29 |
| 10-11 16:56 | +20 | BNB | DOWN | 0.59 | 0.80 | 1.81 |
| 10-11 16:56 | +15 | BNB | DOWN | 0.59 | 0.75 | 1.29 |
| 10-11 16:56 | +10 | BNB | DOWN | 0.59 | 0.75 | 1.29 |
| 10-11 16:56 | +5 | BNB | DOWN | 0.59 | 0.75 | 1.29 |
| 10-11 16:53 | +5 | XRP | DOWN | 0.63 | 0.68 | 0.17 |
| 10-11 16:53 | +10 stop | BTC | UP | 0.65 | 0.80 | 1.22 |
| 10-11 16:53 | +10 stop | SOL | UP | 0.60 | 0.72 | 0.88 |
| 10-11 16:53 | +5 | XRP | DOWN | 0.61 | 0.66 | 0.17 |
| 10-11 16:51 | +10 | XRP | DOWN | 0.60 | yes | -6.17 |
| 10-11 16:51 | +5 | XRP | DOWN | 0.60 | 0.65 | 0.17 |
| 10-11 16:51 | +10 stop | DOGE | DOWN | 0.53 | 0.26 | -3.02 |
| 10-11 16:51 | +5 | SOL | DOWN | 0.58 | yes | -5.98 |
| 10-11 16:50 | +10 stop | SOL | DOWN | 0.58 | 0.43 | -1.86 |
| 10-11 16:50 | +10 stop | ZEC | UP | 0.59 | 0.33 | -2.93 |
| 10-11 16:50 | +10 | ZEC | UP | 0.59 | no | -6.07 |
| 10-11 16:50 | +5 | ZEC | UP | 0.59 | no | -6.07 |
| 10-11 16:50 | +10 stop | XRP | DOWN | 0.71 | 0.45 | -2.93 |
| 10-11 16:50 | +5 | NEAR | UP | 0.58 | 0.67 | 0.56 |
| 10-11 16:49 | +10 stop | BNB | DOWN | 0.68 | 0.81 | 1.05 |
| 10-11 16:49 | +15 | BNB | DOWN | 0.68 | 0.83 | 1.26 |
| 10-11 16:49 | +10 | BNB | DOWN | 0.68 | 0.81 | 1.04 |
| 10-11 16:49 | +5 | BNB | DOWN | 0.68 | 0.76 | 0.52 |
| 10-11 16:49 | +10 stop | SOL | UP | 0.53 | 0.66 | 0.96 |
| 10-11 16:49 | +10 stop | DOGE | UP | 0.64 | 0.48 | -1.95 |
| 10-11 16:49 | +10 stop | BTC | UP | 0.51 | 0.68 | 1.36 |
| 10-11 16:48 | +10 stop | ZEC | DOWN | 0.38 | 0.53 | 1.15 |
| 10-11 16:48 | +5 | NEAR | UP | 0.55 | 0.62 | 0.35 |
| 10-11 16:48 | +10 stop | ETH | UP | 0.57 | 0.73 | 1.28 |
| 10-11 16:48 | +20 | ETH | UP | 0.57 | 0.77 | 1.69 |
| 10-11 16:48 | +15 | ETH | UP | 0.57 | 0.73 | 1.28 |
| 10-11 16:48 | +10 | ETH | UP | 0.57 | 0.73 | 1.28 |
| 10-11 16:48 | +5 | ETH | UP | 0.57 | 0.62 | 0.15 |
| 10-11 16:47 | +10 stop | XRP | DOWN | 0.63 | 0.46 | -2.05 |
