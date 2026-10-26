# Range-Scalp Bot

*Updated Mon Oct 26 22:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35494 | 30972 | 4522 (43) | 4 | $-9962.65 | -4.5% |
| **+10¢** | 26547 | 21316 | 5231 (65) | 5 | $-8807.82 | -5.3% |
| **+15¢** | 22221 | 16594 | 5627 (89) | 2 | $-7882.04 | -5.6% |
| **+20¢** | 19701 | 13804 | 5897 (112) | 3 | $-6945.81 | -5.6% |
| **+10¢ (15¢ stop)** | 43532 | 43470 | 62 (33) | 0 | $-16594.30 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 22:11 | +10 stop | NEAR | UP | 0.31 | 0.55 | 2.07 |
| 10-26 22:09 | +5 | DOGE | UP | 0.64 | open |  |
| 10-26 22:09 | +10 stop | ZEC | UP | 0.66 | 0.36 | -3.33 |
| 10-26 22:09 | +10 stop | SOL | UP | 0.54 | 0.32 | -2.54 |
| 10-26 22:08 | +10 stop | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-26 22:08 | +20 | BNB | DOWN | 0.69 | 0.90 | 1.92 |
| 10-26 22:08 | +15 | BNB | DOWN | 0.69 | 0.87 | 1.57 |
| 10-26 22:08 | +10 stop | ETH | UP | 0.58 | 0.39 | -2.25 |
| 10-26 22:08 | +10 stop | DOGE | UP | 0.61 | 0.28 | -3.62 |
| 10-26 22:08 | +10 | DOGE | UP | 0.61 | open |  |
| 10-26 22:08 | +5 | DOGE | UP | 0.61 | 0.67 | 0.27 |
| 10-26 22:07 | +10 stop | ZEC | UP | 0.54 | 0.64 | 0.65 |
| 10-26 22:07 | +10 stop | ETH | DOWN | 0.62 | 0.43 | -2.25 |
| 10-26 22:07 | +15 | ETH | DOWN | 0.62 | 0.84 | 1.93 |
| 10-26 22:07 | +10 stop | XRP | UP | 0.59 | 0.28 | -3.42 |
| 10-26 22:07 | +10 stop | SOL | DOWN | 0.64 | 0.46 | -2.15 |
| 10-26 22:07 | +10 stop | DOGE | DOWN | 0.66 | 0.50 | -1.94 |
| 10-26 22:06 | +10 stop | NEAR | UP | 0.57 | 0.72 | 1.17 |
| 10-26 22:05 | +10 stop | ETH | UP | 0.61 | 0.36 | -2.84 |
| 10-26 22:05 | +10 stop | BNB | DOWN | 0.59 | 0.79 | 1.71 |
| 10-26 22:05 | +15 | BNB | DOWN | 0.59 | 0.79 | 1.71 |
| 10-26 22:05 | +10 stop | SOL | UP | 0.71 | 0.43 | -3.13 |
| 10-26 22:05 | +10 stop | XRP | UP | 0.69 | 0.80 | 0.83 |
| 10-26 22:05 | +10 stop | DOGE | UP | 0.66 | 0.42 | -2.74 |
| 10-26 22:04 | +5 | BNB | UP | 0.56 | open |  |
| 10-26 22:03 | +10 stop | BNB | UP | 0.61 | 0.46 | -1.85 |
| 10-26 22:03 | +10 | BNB | UP | 0.61 | open |  |
| 10-26 22:03 | +5 | BNB | UP | 0.61 | 0.70 | 0.58 |
| 10-26 22:02 | +10 stop | ETH | UP | 0.69 | 0.54 | -1.83 |
| 10-26 22:02 | +10 | ETH | UP | 0.69 | open |  |
| 10-26 22:02 | +5 | ETH | UP | 0.68 | open |  |
| 10-26 22:02 | +10 stop | BTC | DOWN | 0.53 | 0.69 | 1.27 |
| 10-26 22:02 | +20 | BTC | DOWN | 0.53 | 0.80 | 2.40 |
| 10-26 22:02 | +15 | BTC | DOWN | 0.53 | 0.69 | 1.27 |
| 10-26 22:02 | +10 | BTC | DOWN | 0.53 | 0.69 | 1.27 |
| 10-26 22:02 | +5 | BTC | DOWN | 0.53 | 0.69 | 1.27 |
| 10-26 22:02 | +10 stop | BNB | DOWN | 0.51 | 0.64 | 0.95 |
| 10-26 22:02 | +20 | BNB | DOWN | 0.51 | 0.79 | 2.50 |
| 10-26 22:02 | +15 | BNB | DOWN | 0.51 | 0.70 | 1.57 |
| 10-26 22:02 | +10 | BNB | DOWN | 0.51 | 0.64 | 0.95 |
