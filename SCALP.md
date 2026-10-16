# Range-Scalp Bot

*Updated Fri Oct 16 02:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18563 | 16126 | 2437 (28) | 4 | $-5613.15 | -4.8% |
| **+10¢** | 13998 | 11179 | 2819 (40) | 3 | $-5068.21 | -5.8% |
| **+15¢** | 11733 | 8698 | 3035 (59) | 5 | $-4592.45 | -6.2% |
| **+20¢** | 10418 | 7243 | 3175 (78) | 6 | $-4004.92 | -6.1% |
| **+10¢ (15¢ stop)** | 22870 | 22820 | 50 (29) | 1 | $-8842.64 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 02:27 | +10 stop | BTC | DOWN | 0.70 | open |  |
| 10-16 02:27 | +5 | BTC | DOWN | 0.70 | open |  |
| 10-16 02:27 | +10 stop | ETH | UP | 0.62 | 0.77 | 1.20 |
| 10-16 02:27 | +15 | ETH | UP | 0.61 | 0.77 | 1.30 |
| 10-16 02:27 | +10 | ETH | UP | 0.61 | 0.77 | 1.30 |
| 10-16 02:27 | +5 | ETH | UP | 0.61 | 0.77 | 1.30 |
| 10-16 02:27 | +10 stop | SOL | DOWN | 0.70 | 0.94 | 2.24 |
| 10-16 02:27 | +5 | SOL | DOWN | 0.70 | 0.94 | 2.24 |
| 10-16 02:27 | +10 stop | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-16 02:26 | +10 stop | HYPE | UP | 0.65 | 0.20 | -4.77 |
| 10-16 02:26 | +10 stop | ZEC | UP | 0.53 | 0.26 | -3.02 |
| 10-16 02:26 | +5 | ZEC | UP | 0.54 | open |  |
| 10-16 02:25 | +10 stop | DOGE | UP | 0.71 | 0.50 | -2.42 |
| 10-16 02:25 | +15 | DOGE | UP | 0.71 | open |  |
| 10-16 02:25 | +10 | DOGE | UP | 0.71 | open |  |
| 10-16 02:25 | +5 | DOGE | UP | 0.71 | open |  |
| 10-16 02:25 | +10 stop | XRP | DOWN | 0.58 | 0.81 | 2.01 |
| 10-16 02:25 | +10 stop | BTC | UP | 0.53 | 0.65 | 0.86 |
| 10-16 02:24 | +10 stop | NEAR | DOWN | 0.54 | 0.79 | 2.20 |
| 10-16 02:24 | +10 stop | XRP | DOWN | 0.63 | 0.47 | -1.95 |
| 10-16 02:24 | +10 stop | BTC | DOWN | 0.59 | 0.44 | -1.85 |
| 10-16 02:24 | +10 stop | SOL | UP | 0.61 | 0.78 | 1.40 |
| 10-16 02:24 | +10 stop | ETH | UP | 0.69 | 0.84 | 1.25 |
| 10-16 02:24 | +20 | ETH | UP | 0.69 | open |  |
| 10-16 02:24 | +15 | ETH | UP | 0.67 | 0.84 | 1.45 |
| 10-16 02:24 | +10 | ETH | UP | 0.67 | 0.84 | 1.44 |
| 10-16 02:24 | +5 | ETH | UP | 0.66 | 0.84 | 1.54 |
| 10-16 02:23 | +5 | XRP | UP | 0.54 | open |  |
| 10-16 02:23 | +5 | BTC | UP | 0.53 | 0.65 | 0.86 |
| 10-16 02:23 | +10 stop | ZEC | UP | 0.58 | 0.72 | 1.04 |
| 10-16 02:23 | +5 | ZEC | UP | 0.56 | 0.72 | 1.27 |
| 10-16 02:22 | +10 stop | XRP | UP | 0.59 | 0.40 | -2.24 |
| 10-16 02:22 | +5 | XRP | UP | 0.59 | 0.66 | 0.37 |
| 10-16 02:22 | +5 | BTC | UP | 0.59 | 0.65 | 0.27 |
| 10-16 02:22 | +10 stop | NEAR | UP | 0.66 | 0.48 | -2.14 |
| 10-16 02:21 | +5 | ZEC | DOWN | 0.49 | 0.60 | 0.74 |
| 10-16 02:21 | +5 | XRP | UP | 0.54 | 0.67 | 0.96 |
| 10-16 02:21 | +5 | BTC | UP | 0.51 | 0.64 | 0.95 |
| 10-16 02:21 | +10 stop | XRP | UP | 0.70 | 0.52 | -2.13 |
| 10-16 02:21 | +10 stop | ZEC | DOWN | 0.59 | 0.43 | -1.95 |
