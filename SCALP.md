# Range-Scalp Bot

*Updated Wed Oct 07 14:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6570 | 5711 | 859 (9) | 1 | $-1939.50 | -4.7% |
| **+10¢** | 4989 | 3979 | 1010 (16) | 1 | $-1823.74 | -5.8% |
| **+15¢** | 4182 | 3116 | 1066 (20) | 1 | $-1528.77 | -5.8% |
| **+20¢** | 3738 | 2624 | 1114 (27) | 0 | $-1229.15 | -5.2% |
| **+10¢ (15¢ stop)** | 7975 | 7960 | 15 (9) | 0 | $-2815.69 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 14:27 | +10 stop | DOGE | UP | 0.34 | 0.63 | 2.57 |
| 10-07 14:26 | +10 stop | BTC | DOWN | 0.59 | 0.71 | 0.88 |
| 10-07 14:26 | +10 stop | XRP | DOWN | 0.62 | 0.75 | 0.99 |
| 10-07 14:26 | +20 | XRP | DOWN | 0.62 | 0.92 | 2.76 |
| 10-07 14:26 | +15 | XRP | DOWN | 0.62 | 0.77 | 1.20 |
| 10-07 14:26 | +10 | XRP | DOWN | 0.62 | 0.75 | 0.99 |
| 10-07 14:26 | +5 | XRP | DOWN | 0.62 | 0.75 | 0.99 |
| 10-07 14:25 | +10 stop | NEAR | UP | 0.71 | 0.54 | -2.03 |
| 10-07 14:24 | +10 stop | NEAR | UP | 0.70 | 0.54 | -1.92 |
| 10-07 14:24 | +10 | NEAR | UP | 0.70 | open |  |
| 10-07 14:23 | +10 stop | BTC | DOWN | 0.64 | 0.46 | -2.15 |
| 10-07 14:23 | +10 stop | DOGE | DOWN | 0.44 | 0.54 | 0.64 |
| 10-07 14:22 | +10 stop | BNB | UP | 0.60 | 0.76 | 1.30 |
| 10-07 14:22 | +10 stop | XRP | DOWN | 0.57 | 0.36 | -2.45 |
| 10-07 14:22 | +5 | NEAR | UP | 0.71 | open |  |
| 10-07 14:22 | +10 stop | SOL | UP | 0.59 | 0.72 | 0.99 |
| 10-07 14:21 | +5 | ETH | UP | 0.65 | 0.74 | 0.60 |
| 10-07 14:20 | +10 stop | BTC | DOWN | 0.67 | 0.47 | -2.34 |
| 10-07 14:20 | +10 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-07 14:20 | +5 | BTC | DOWN | 0.68 | 0.77 | 0.61 |
| 10-07 14:20 | +5 | SOL | DOWN | 0.60 | 0.66 | 0.27 |
| 10-07 14:20 | +10 stop | DOGE | DOWN | 0.68 | 0.51 | -2.04 |
| 10-07 14:20 | +10 | DOGE | DOWN | 0.68 | 0.82 | 1.13 |
| 10-07 14:20 | +5 | DOGE | DOWN | 0.69 | 0.82 | 1.08 |
| 10-07 14:20 | +10 stop | NEAR | UP | 0.57 | 0.72 | 1.17 |
| 10-07 14:20 | +15 | NEAR | UP | 0.59 | open |  |
| 10-07 14:20 | +10 | NEAR | UP | 0.59 | 0.72 | 0.99 |
| 10-07 14:20 | +5 | NEAR | UP | 0.59 | 0.65 | 0.28 |
| 10-07 14:20 | +10 stop | ETH | DOWN | 0.52 | 0.36 | -1.95 |
| 10-07 14:20 | +10 | ETH | DOWN | 0.52 | 0.68 | 1.26 |
| 10-07 14:20 | +5 | ETH | DOWN | 0.52 | 0.61 | 0.55 |
| 10-07 14:20 | +10 stop | BNB | DOWN | 0.64 | 0.38 | -2.94 |
| 10-07 14:20 | +10 | BNB | DOWN | 0.65 | 0.78 | 0.99 |
| 10-07 14:19 | +15 | ZEC | UP | 0.69 | 0.85 | 1.36 |
| 10-07 14:19 | +10 stop | NEAR | DOWN | 0.59 | 0.71 | 0.89 |
| 10-07 14:19 | +5 | BNB | DOWN | 0.63 | 0.78 | 1.20 |
| 10-07 14:18 | +10 stop | XRP | DOWN | 0.62 | 0.73 | 0.79 |
| 10-07 14:18 | +10 stop | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 10-07 14:18 | +10 | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 10-07 14:18 | +5 | ZEC | UP | 0.69 | 0.75 | 0.32 |
