# Range-Scalp Bot

*Updated Wed Oct 14 23:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16742 | 14516 | 2226 (28) | 1 | $-5229.84 | -5.0% |
| **+10¢** | 12660 | 10080 | 2580 (40) | 1 | $-4779.79 | -6.0% |
| **+15¢** | 10637 | 7865 | 2772 (59) | 1 | $-4298.72 | -6.4% |
| **+20¢** | 9450 | 6546 | 2904 (76) | 1 | $-3799.15 | -6.4% |
| **+10¢ (15¢ stop)** | 20616 | 20566 | 50 (29) | 0 | $-7924.38 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 23:57 | +10 stop | NEAR | DOWN | 0.63 | 0.40 | -2.64 |
| 10-14 23:57 | +10 stop | ETH | DOWN | 0.48 | 0.08 | -4.22 |
| 10-14 23:56 | +10 stop | ZEC | UP | 0.57 | 0.75 | 1.48 |
| 10-14 23:54 | +10 stop | ZEC | UP | 0.69 | 0.52 | -2.02 |
| 10-14 23:54 | +20 | ZEC | UP | 0.69 | 0.89 | 1.79 |
| 10-14 23:54 | +15 | ZEC | UP | 0.69 | 0.89 | 1.79 |
| 10-14 23:54 | +10 | ZEC | UP | 0.69 | 0.89 | 1.78 |
| 10-14 23:54 | +5 | ZEC | UP | 0.69 | 0.75 | 0.31 |
| 10-14 23:54 | +10 stop | BNB | DOWN | 0.68 | 0.83 | 1.24 |
| 10-14 23:54 | +10 stop | NEAR | DOWN | 0.59 | 0.70 | 0.78 |
| 10-14 23:53 | +10 stop | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-14 23:53 | +10 stop | BTC | UP | 0.70 | 0.55 | -1.83 |
| 10-14 23:53 | +20 | BTC | UP | 0.70 | 0.94 | 2.26 |
| 10-14 23:53 | +15 | BTC | UP | 0.70 | 0.87 | 1.47 |
| 10-14 23:53 | +10 | BTC | UP | 0.70 | 0.87 | 1.47 |
| 10-14 23:53 | +5 | BTC | UP | 0.70 | 0.87 | 1.47 |
| 10-14 23:52 | +10 stop | BNB | UP | 0.61 | 0.40 | -2.44 |
| 10-14 23:52 | +20 | BNB | UP | 0.61 | 0.89 | 2.56 |
| 10-14 23:52 | +15 | BNB | UP | 0.61 | 0.79 | 1.51 |
| 10-14 23:52 | +10 | BNB | UP | 0.61 | 0.79 | 1.51 |
| 10-14 23:52 | +5 | BNB | UP | 0.61 | 0.79 | 1.51 |
| 10-14 23:52 | +10 stop | XRP | DOWN | 0.70 | 0.83 | 1.05 |
| 10-14 23:52 | +10 stop | HYPE | DOWN | 0.69 | 0.79 | 0.74 |
| 10-14 23:51 | +10 stop | HYPE | DOWN | 0.55 | 0.66 | 0.76 |
| 10-14 23:51 | +10 stop | NEAR | UP | 0.68 | 0.53 | -1.84 |
| 10-14 23:51 | +15 | NEAR | UP | 0.68 | open |  |
| 10-14 23:51 | +10 | NEAR | UP | 0.68 | open |  |
| 10-14 23:51 | +5 | NEAR | UP | 0.68 | open |  |
| 10-14 23:51 | +10 stop | SOL | DOWN | 0.62 | 0.75 | 0.99 |
| 10-14 23:51 | +5 | ETH | UP | 0.71 | 0.91 | 1.80 |
| 10-14 23:51 | +10 stop | SOL | UP | 0.41 | 0.57 | 1.25 |
| 10-14 23:50 | +10 stop | HYPE | DOWN | 0.51 | 0.64 | 0.95 |
| 10-14 23:50 | +10 stop | XRP | UP | 0.54 | 0.38 | -1.95 |
| 10-14 23:49 | +5 | BNB | UP | 0.70 | 0.75 | 0.21 |
| 10-14 23:49 | +10 stop | SOL | DOWN | 0.64 | 0.44 | -2.35 |
| 10-14 23:49 | +10 | SOL | DOWN | 0.64 | 0.75 | 0.79 |
| 10-14 23:48 | +10 stop | XRP | DOWN | 0.59 | 0.44 | -1.87 |
| 10-14 23:48 | +10 | XRP | DOWN | 0.59 | 0.71 | 0.86 |
| 10-14 23:48 | +5 | XRP | DOWN | 0.61 | 0.68 | 0.37 |
| 10-14 23:48 | +10 stop | HYPE | DOWN | 0.68 | 0.53 | -1.84 |
