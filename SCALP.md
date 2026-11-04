# Range-Scalp Bot

*Updated Wed Nov 04 18:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47376 | 41257 | 6119 (72) | 0 | $-13639.51 | -4.6% |
| **+10¢** | 35387 | 28287 | 7100 (97) | 0 | $-12478.33 | -5.6% |
| **+15¢** | 29633 | 21989 | 7644 (125) | 1 | $-11436.85 | -6.2% |
| **+20¢** | 26328 | 18323 | 8005 (165) | 1 | $-10083.02 | -6.1% |
| **+10¢ (15¢ stop)** | 57738 | 57645 | 93 (56) | 0 | $-21510.84 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 18:26 | +10 stop | XRP | DOWN | 0.58 | 0.36 | -2.55 |
| 11-04 18:26 | +5 | XRP | DOWN | 0.57 | 0.87 | 2.74 |
| 11-04 18:26 | +10 stop | ETH | UP | 0.60 | 0.77 | 1.40 |
| 11-04 18:26 | +10 stop | XRP | UP | 0.38 | 0.64 | 2.26 |
| 11-04 18:26 | +5 | XRP | UP | 0.38 | 0.64 | 2.26 |
| 11-04 18:26 | +10 stop | BTC | DOWN | 0.65 | 0.43 | -2.54 |
| 11-04 18:26 | +10 | BTC | DOWN | 0.65 | 0.80 | 1.22 |
| 11-04 18:26 | +5 | BTC | DOWN | 0.65 | 0.80 | 1.22 |
| 11-04 18:25 | +10 stop | XRP | UP | 0.50 | 0.62 | 0.85 |
| 11-04 18:25 | +5 | XRP | UP | 0.50 | 0.62 | 0.85 |
| 11-04 18:24 | +15 | DOGE | UP | 0.64 | 0.79 | 1.21 |
| 11-04 18:24 | +5 | DOGE | UP | 0.64 | 0.72 | 0.48 |
| 11-04 18:24 | +10 stop | BNB | DOWN | 0.65 | 0.75 | 0.74 |
| 11-04 18:24 | +10 stop | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 11-04 18:24 | +20 | BTC | DOWN | 0.62 | 0.84 | 1.93 |
| 11-04 18:24 | +15 | BTC | DOWN | 0.62 | 0.80 | 1.51 |
| 11-04 18:24 | +10 | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 11-04 18:24 | +5 | BTC | DOWN | 0.62 | 0.68 | 0.27 |
| 11-04 18:24 | +10 stop | DOGE | UP | 0.65 | 0.79 | 1.12 |
| 11-04 18:24 | +15 | BNB | DOWN | 0.57 | 0.73 | 1.28 |
| 11-04 18:23 | +10 stop | XRP | DOWN | 0.63 | 0.38 | -2.82 |
| 11-04 18:23 | +10 stop | ETH | DOWN | 0.56 | 0.40 | -1.95 |
| 11-04 18:22 | +10 stop | BNB | DOWN | 0.70 | 0.54 | -1.93 |
| 11-04 18:22 | +10 | BNB | DOWN | 0.70 | 0.81 | 0.84 |
| 11-04 18:22 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 11-04 18:22 | +10 stop | DOGE | DOWN | 0.66 | 0.44 | -2.54 |
| 11-04 18:21 | +10 stop | ETH | UP | 0.70 | 0.54 | -1.93 |
| 11-04 18:21 | +20 | ETH | UP | 0.70 | open |  |
| 11-04 18:21 | +15 | ETH | UP | 0.70 | open |  |
| 11-04 18:21 | +10 | ETH | UP | 0.70 | 0.82 | 0.94 |
| 11-04 18:21 | +5 | ETH | UP | 0.70 | 0.77 | 0.42 |
| 11-04 18:21 | +10 stop | DOGE | UP | 0.64 | 0.41 | -2.64 |
| 11-04 18:20 | +5 | ZEC | DOWN | 0.71 | 0.78 | 0.42 |
| 11-04 18:20 | +10 stop | BTC | DOWN | 0.64 | 0.47 | -2.05 |
| 11-04 18:20 | +10 | BTC | DOWN | 0.64 | 0.79 | 1.21 |
| 11-04 18:20 | +5 | BNB | DOWN | 0.60 | 0.65 | 0.17 |
| 11-04 18:20 | +5 | BTC | DOWN | 0.65 | 0.71 | 0.29 |
| 11-04 18:19 | +10 stop | SOL | DOWN | 0.62 | 0.75 | 0.99 |
| 11-04 18:19 | +10 | SOL | DOWN | 0.62 | 0.75 | 0.99 |
| 11-04 18:19 | +5 | SOL | DOWN | 0.62 | 0.68 | 0.27 |
