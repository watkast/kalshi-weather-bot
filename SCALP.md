# Range-Scalp Bot

*Updated Wed Nov 04 02:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46674 | 40646 | 6028 (72) | 2 | $-13395.19 | -4.6% |
| **+10¢** | 34865 | 27877 | 6988 (96) | 2 | $-12222.07 | -5.6% |
| **+15¢** | 29198 | 21680 | 7518 (124) | 1 | $-11166.71 | -6.1% |
| **+20¢** | 25934 | 18061 | 7873 (164) | 2 | $-9820.75 | -6.0% |
| **+10¢ (15¢ stop)** | 56907 | 56814 | 93 (56) | 0 | $-21247.72 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 02:24 | +10 stop | XRP | DOWN | 0.66 | 0.80 | 1.17 |
| 11-04 02:24 | +20 | XRP | DOWN | 0.66 | open |  |
| 11-04 02:24 | +15 | XRP | DOWN | 0.66 | 0.84 | 1.59 |
| 11-04 02:24 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-04 02:24 | +10 | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 11-04 02:24 | +5 | ETH | DOWN | 0.70 | 0.78 | 0.52 |
| 11-04 02:22 | +10 stop | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 11-04 02:22 | +15 | XRP | DOWN | 0.60 | 0.82 | 1.92 |
| 11-04 02:21 | +10 stop | XRP | DOWN | 0.64 | 0.82 | 1.52 |
| 11-04 02:21 | +5 | ETH | DOWN | 0.64 | 0.70 | 0.28 |
| 11-04 02:21 | +10 stop | ZEC | DOWN | 0.71 | 0.53 | -2.13 |
| 11-04 02:20 | +5 | ETH | DOWN | 0.54 | 0.63 | 0.55 |
| 11-04 02:20 | +5 | DOGE | DOWN | 0.68 | 0.75 | 0.38 |
| 11-04 02:20 | +10 stop | XRP | UP | 0.58 | 0.40 | -2.11 |
| 11-04 02:20 | +10 | XRP | UP | 0.57 | open |  |
| 11-04 02:20 | +5 | XRP | UP | 0.57 | open |  |
| 11-04 02:20 | +10 stop | ZEC | UP | 0.56 | 0.35 | -2.44 |
| 11-04 02:20 | +10 stop | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 11-04 02:20 | +15 | SOL | DOWN | 0.67 | 0.87 | 1.76 |
| 11-04 02:20 | +10 | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 11-04 02:20 | +5 | SOL | DOWN | 0.67 | 0.75 | 0.50 |
| 11-04 02:20 | +10 stop | BNB | DOWN | 0.62 | 0.77 | 1.16 |
| 11-04 02:20 | +15 | BNB | DOWN | 0.62 | 0.84 | 1.89 |
| 11-04 02:20 | +10 | BNB | DOWN | 0.62 | 0.77 | 1.16 |
| 11-04 02:20 | +5 | BNB | DOWN | 0.62 | 0.77 | 1.20 |
| 11-04 02:20 | +5 | DOGE | DOWN | 0.54 | 0.63 | 0.55 |
| 11-04 02:19 | +10 stop | XRP | DOWN | 0.47 | 0.57 | 0.64 |
| 11-04 02:19 | +15 | XRP | DOWN | 0.47 | 0.62 | 1.15 |
| 11-04 02:19 | +10 | XRP | DOWN | 0.47 | 0.57 | 0.64 |
| 11-04 02:19 | +5 | XRP | DOWN | 0.47 | 0.57 | 0.64 |
| 11-04 02:19 | +10 stop | ETH | DOWN | 0.54 | 0.70 | 1.27 |
| 11-04 02:19 | +10 | ETH | DOWN | 0.54 | 0.70 | 1.27 |
| 11-04 02:19 | +5 | ETH | DOWN | 0.54 | 0.60 | 0.25 |
| 11-04 02:19 | +10 stop | DOGE | DOWN | 0.61 | 0.72 | 0.78 |
| 11-04 02:19 | +20 | DOGE | DOWN | 0.61 | 0.81 | 1.72 |
| 11-04 02:19 | +15 | DOGE | DOWN | 0.61 | 0.81 | 1.72 |
| 11-04 02:19 | +10 | DOGE | DOWN | 0.61 | 0.72 | 0.78 |
| 11-04 02:19 | +5 | DOGE | DOWN | 0.61 | 0.69 | 0.48 |
| 11-04 02:19 | +10 stop | NEAR | DOWN | 0.65 | 0.79 | 1.12 |
| 11-04 02:19 | +10 | NEAR | DOWN | 0.65 | 0.79 | 1.12 |
