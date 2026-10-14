# Range-Scalp Bot

*Updated Wed Oct 14 23:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16699 | 14475 | 2224 (28) | 1 | $-5239.42 | -5.0% |
| **+10¢** | 12631 | 10053 | 2578 (40) | 1 | $-4793.68 | -6.0% |
| **+15¢** | 10613 | 7843 | 2770 (59) | 1 | $-4317.62 | -6.5% |
| **+20¢** | 9430 | 6528 | 2902 (76) | 1 | $-3821.62 | -6.5% |
| **+10¢ (15¢ stop)** | 20560 | 20510 | 50 (29) | 0 | $-7908.12 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 23:27 | +10 stop | BNB | DOWN | 0.69 | 0.50 | -2.23 |
| 10-14 23:27 | +20 | BNB | DOWN | 0.69 | open |  |
| 10-14 23:27 | +15 | BNB | DOWN | 0.69 | open |  |
| 10-14 23:27 | +10 | BNB | DOWN | 0.69 | open |  |
| 10-14 23:27 | +5 | BNB | DOWN | 0.69 | open |  |
| 10-14 23:25 | +10 stop | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 10-14 23:25 | +5 | NEAR | DOWN | 0.68 | 0.75 | 0.40 |
| 10-14 23:24 | +5 | NEAR | DOWN | 0.55 | 0.67 | 0.86 |
| 10-14 23:23 | +10 stop | NEAR | DOWN | 0.59 | 0.40 | -2.24 |
| 10-14 23:23 | +20 | NEAR | DOWN | 0.59 | 0.79 | 1.71 |
| 10-14 23:23 | +15 | NEAR | DOWN | 0.59 | 0.75 | 1.29 |
| 10-14 23:23 | +10 | NEAR | DOWN | 0.59 | 0.70 | 0.78 |
| 10-14 23:23 | +5 | NEAR | DOWN | 0.59 | 0.64 | 0.16 |
| 10-14 23:21 | +5 | BNB | DOWN | 0.67 | 0.73 | 0.30 |
| 10-14 23:20 | +10 stop | BNB | DOWN | 0.66 | 0.82 | 1.33 |
| 10-14 23:19 | +5 | DOGE | DOWN | 0.66 | 0.75 | 0.60 |
| 10-14 23:19 | +10 stop | BNB | UP | 0.55 | 0.39 | -1.95 |
| 10-14 23:18 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-14 23:18 | +15 | BTC | DOWN | 0.60 | 0.79 | 1.61 |
| 10-14 23:18 | +10 | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-14 23:18 | +5 | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-14 23:18 | +10 stop | XRP | DOWN | 0.62 | 0.76 | 1.10 |
| 10-14 23:18 | +15 | XRP | DOWN | 0.62 | 0.80 | 1.51 |
| 10-14 23:18 | +10 | XRP | DOWN | 0.62 | 0.76 | 1.10 |
| 10-14 23:18 | +5 | XRP | DOWN | 0.62 | 0.71 | 0.58 |
| 10-14 23:18 | +10 stop | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-14 23:18 | +15 | DOGE | DOWN | 0.58 | 0.75 | 1.38 |
| 10-14 23:18 | +10 | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-14 23:18 | +5 | DOGE | DOWN | 0.58 | 0.67 | 0.56 |
| 10-14 23:18 | +10 stop | NEAR | DOWN | 0.60 | 0.74 | 1.09 |
| 10-14 23:18 | +10 | NEAR | DOWN | 0.60 | 0.74 | 1.09 |
| 10-14 23:18 | +5 | NEAR | DOWN | 0.60 | 0.65 | 0.17 |
| 10-14 23:18 | +10 stop | ETH | DOWN | 0.58 | 0.77 | 1.61 |
| 10-14 23:18 | +10 | ETH | DOWN | 0.58 | 0.77 | 1.61 |
| 10-14 23:18 | +5 | ETH | DOWN | 0.58 | 0.64 | 0.27 |
| 10-14 23:18 | +5 | SOL | DOWN | 0.65 | 0.71 | 0.30 |
| 10-14 23:17 | +10 stop | BNB | DOWN | 0.64 | 0.43 | -2.45 |
| 10-14 23:17 | +20 | BNB | DOWN | 0.64 | 0.84 | 1.73 |
| 10-14 23:17 | +15 | BNB | DOWN | 0.64 | 0.82 | 1.52 |
| 10-14 23:17 | +10 | BNB | DOWN | 0.64 | 0.75 | 0.79 |
