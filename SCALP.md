# Range-Scalp Bot

*Updated Tue Oct 27 22:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37120 | 32406 | 4714 (45) | 0 | $-10328.88 | -4.4% |
| **+10¢** | 27728 | 22267 | 5461 (67) | 2 | $-9213.94 | -5.3% |
| **+15¢** | 23197 | 17331 | 5866 (91) | 2 | $-8192.17 | -5.6% |
| **+20¢** | 20552 | 14415 | 6137 (116) | 2 | $-7156.63 | -5.5% |
| **+10¢ (15¢ stop)** | 45467 | 45402 | 65 (34) | 2 | $-17302.27 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 22:01 | +5 | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 10-27 22:01 | +10 stop | BTC | DOWN | 0.55 | open |  |
| 10-27 22:01 | +20 | BTC | DOWN | 0.55 | open |  |
| 10-27 22:01 | +15 | BTC | DOWN | 0.55 | open |  |
| 10-27 22:01 | +10 | BTC | DOWN | 0.55 | open |  |
| 10-27 22:01 | +5 | BTC | DOWN | 0.55 | 0.63 | 0.45 |
| 10-27 22:01 | +10 stop | ETH | DOWN | 0.59 | open |  |
| 10-27 22:01 | +20 | ETH | DOWN | 0.59 | open |  |
| 10-27 22:01 | +15 | ETH | DOWN | 0.59 | open |  |
| 10-27 22:01 | +10 | ETH | DOWN | 0.59 | open |  |
| 10-27 22:01 | +5 | ETH | DOWN | 0.59 | 0.64 | 0.16 |
| 10-27 21:59 | +10 stop | NEAR | UP | 0.34 | 0.54 | 1.66 |
| 10-27 21:59 | +10 | NEAR | UP | 0.35 | 0.54 | 1.56 |
| 10-27 21:59 | +5 | NEAR | UP | 0.36 | 0.54 | 1.45 |
| 10-27 21:57 | +10 stop | NEAR | UP | 0.68 | 0.78 | 0.71 |
| 10-27 21:57 | +15 | NEAR | UP | 0.68 | no | -6.96 |
| 10-27 21:57 | +10 | NEAR | UP | 0.68 | 0.78 | 0.71 |
| 10-27 21:57 | +5 | NEAR | UP | 0.66 | 0.78 | 0.91 |
| 10-27 21:55 | +10 stop | DOGE | UP | 0.53 | 0.22 | -3.41 |
| 10-27 21:54 | +10 stop | ETH | UP | 0.69 | 0.79 | 0.73 |
| 10-27 21:54 | +15 | ETH | UP | 0.69 | no | -7.05 |
| 10-27 21:54 | +10 | ETH | UP | 0.69 | 0.79 | 0.73 |
| 10-27 21:54 | +5 | ETH | UP | 0.69 | 0.76 | 0.42 |
| 10-27 21:53 | +10 stop | BTC | DOWN | 0.55 | 0.69 | 1.07 |
| 10-27 21:53 | +10 stop | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 10-27 21:53 | +10 stop | SOL | DOWN | 0.60 | 0.86 | 2.34 |
| 10-27 21:53 | +10 stop | XRP | UP | 0.70 | 0.80 | 0.73 |
| 10-27 21:53 | +20 | XRP | UP | 0.70 | 0.91 | 1.88 |
| 10-27 21:53 | +15 | XRP | UP | 0.70 | 0.91 | 1.88 |
| 10-27 21:53 | +10 | XRP | UP | 0.70 | 0.80 | 0.73 |
| 10-27 21:53 | +5 | XRP | UP | 0.70 | 0.76 | 0.32 |
| 10-27 21:53 | +10 stop | NEAR | UP | 0.71 | 0.86 | 1.26 |
| 10-27 21:53 | +20 | NEAR | UP | 0.71 | no | -7.25 |
| 10-27 21:53 | +15 | NEAR | UP | 0.71 | 0.86 | 1.26 |
| 10-27 21:53 | +10 | NEAR | UP | 0.71 | 0.86 | 1.26 |
| 10-27 21:53 | +5 | NEAR | UP | 0.71 | 0.86 | 1.26 |
| 10-27 21:52 | +10 stop | BTC | UP | 0.61 | 0.45 | -1.95 |
| 10-27 21:52 | +10 | BTC | UP | 0.61 | no | -6.27 |
| 10-27 21:52 | +5 | BTC | UP | 0.61 | no | -6.27 |
| 10-27 21:52 | +10 stop | DOGE | UP | 0.64 | 0.36 | -3.09 |
