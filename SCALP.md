# Range-Scalp Bot

*Updated Tue Nov 03 23:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46478 | 40472 | 6006 (72) | 2 | $-13362.52 | -4.6% |
| **+10¢** | 34703 | 27740 | 6963 (96) | 2 | $-12227.32 | -5.6% |
| **+15¢** | 29053 | 21564 | 7489 (124) | 3 | $-11178.07 | -6.1% |
| **+20¢** | 25812 | 17965 | 7847 (164) | 3 | $-9870.07 | -6.1% |
| **+10¢ (15¢ stop)** | 56693 | 56600 | 93 (56) | 1 | $-21249.93 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 23:28 | +10 stop | ETH | UP | 0.56 | open |  |
| 11-03 23:27 | +10 stop | BNB | UP | 0.65 | 0.77 | 0.95 |
| 11-03 23:26 | +10 stop | XRP | DOWN | 0.62 | 0.16 | -4.87 |
| 11-03 23:26 | +10 | XRP | DOWN | 0.63 | open |  |
| 11-03 23:26 | +5 | XRP | DOWN | 0.62 | 0.69 | 0.38 |
| 11-03 23:24 | +5 | XRP | DOWN | 0.66 | 0.73 | 0.40 |
| 11-03 23:23 | +5 | XRP | DOWN | 0.59 | 0.66 | 0.37 |
| 11-03 23:23 | +10 stop | DOGE | UP | 0.67 | 0.80 | 1.02 |
| 11-03 23:23 | +10 stop | ETH | DOWN | 0.67 | 0.52 | -1.84 |
| 11-03 23:23 | +10 stop | BTC | UP | 0.68 | 0.80 | 0.92 |
| 11-03 23:23 | +20 | BTC | UP | 0.68 | 0.89 | 1.87 |
| 11-03 23:23 | +15 | BTC | UP | 0.68 | 0.84 | 1.34 |
| 11-03 23:23 | +10 | BTC | UP | 0.68 | 0.80 | 0.92 |
| 11-03 23:23 | +5 | BTC | UP | 0.68 | 0.76 | 0.51 |
| 11-03 23:23 | +10 stop | SOL | UP | 0.71 | 0.82 | 0.84 |
| 11-03 23:23 | +10 stop | BNB | DOWN | 0.58 | 0.42 | -1.96 |
| 11-03 23:23 | +10 stop | XRP | DOWN | 0.58 | 0.73 | 1.18 |
| 11-03 23:23 | +10 | XRP | DOWN | 0.58 | 0.73 | 1.18 |
| 11-03 23:23 | +5 | XRP | DOWN | 0.58 | 0.63 | 0.15 |
| 11-03 23:22 | +10 stop | HYPE | DOWN | 0.44 | 0.69 | 2.17 |
| 11-03 23:22 | +10 stop | DOGE | DOWN | 0.60 | 0.34 | -2.93 |
| 11-03 23:22 | +10 stop | SOL | DOWN | 0.48 | 0.58 | 0.64 |
| 11-03 23:21 | +5 | DOGE | DOWN | 0.69 | open |  |
| 11-03 23:21 | +10 stop | ZEC | UP | 0.61 | 0.75 | 1.09 |
| 11-03 23:21 | +15 | ZEC | UP | 0.60 | 0.75 | 1.19 |
| 11-03 23:21 | +10 | ZEC | UP | 0.60 | 0.70 | 0.68 |
| 11-03 23:21 | +5 | ZEC | UP | 0.60 | 0.70 | 0.68 |
| 11-03 23:21 | +10 stop | NEAR | UP | 0.52 | 0.63 | 0.75 |
| 11-03 23:21 | +15 | NEAR | UP | 0.54 | 0.69 | 1.17 |
| 11-03 23:21 | +10 | NEAR | UP | 0.54 | 0.69 | 1.17 |
| 11-03 23:21 | +5 | NEAR | UP | 0.54 | 0.63 | 0.55 |
| 11-03 23:20 | +10 stop | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-03 23:20 | +10 | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-03 23:20 | +5 | BTC | DOWN | 0.63 | 0.70 | 0.38 |
| 11-03 23:20 | +10 stop | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 11-03 23:19 | +5 | BTC | DOWN | 0.58 | 0.68 | 0.66 |
| 11-03 23:19 | +5 | DOGE | UP | 0.59 | 0.65 | 0.27 |
| 11-03 23:19 | +10 stop | ZEC | UP | 0.61 | 0.76 | 1.20 |
| 11-03 23:19 | +20 | ZEC | UP | 0.61 | 0.85 | 2.14 |
| 11-03 23:19 | +15 | ZEC | UP | 0.61 | 0.76 | 1.20 |
