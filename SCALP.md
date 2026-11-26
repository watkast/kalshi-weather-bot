# Range-Scalp Bot

*Updated Thu Nov 26 20:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72835 | 63571 | 9264 (158) | 2 | $-19404.81 | -4.2% |
| **+10¢** | 54303 | 43488 | 10815 (203) | 3 | $-17989.62 | -5.3% |
| **+15¢** | 45473 | 33822 | 11651 (261) | 3 | $-16091.47 | -5.6% |
| **+20¢** | 40468 | 28200 | 12268 (327) | 4 | $-14491.00 | -5.7% |
| **+10¢ (15¢ stop)** | 88697 | 88488 | 209 (128) | 0 | $-32677.44 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 20:12 | +10 stop | ETH | DOWN | 0.70 | 0.85 | 1.26 |
| 11-26 20:12 | +20 | ETH | DOWN | 0.70 | open |  |
| 11-26 20:12 | +15 | ETH | DOWN | 0.70 | 0.85 | 1.26 |
| 11-26 20:12 | +10 | ETH | DOWN | 0.70 | 0.85 | 1.26 |
| 11-26 20:12 | +5 | ETH | DOWN | 0.70 | 0.85 | 1.26 |
| 11-26 20:12 | +10 stop | XRP | UP | 0.56 | 0.21 | -3.80 |
| 11-26 20:12 | +15 | XRP | UP | 0.56 | open |  |
| 11-26 20:12 | +10 | XRP | UP | 0.56 | open |  |
| 11-26 20:12 | +5 | XRP | UP | 0.56 | 0.65 | 0.56 |
| 11-26 20:11 | +10 stop | NEAR | UP | 0.70 | 0.81 | 0.88 |
| 11-26 20:10 | +10 stop | NEAR | DOWN | 0.37 | 0.54 | 1.35 |
| 11-26 20:10 | +15 | BTC | UP | 0.65 | 0.88 | 2.06 |
| 11-26 20:10 | +5 | BTC | UP | 0.65 | 0.70 | 0.19 |
| 11-26 20:09 | +10 stop | ETH | DOWN | 0.60 | 0.71 | 0.78 |
| 11-26 20:09 | +10 stop | DOGE | DOWN | 0.63 | 0.81 | 1.52 |
| 11-26 20:09 | +10 stop | XRP | DOWN | 0.60 | 0.76 | 1.30 |
| 11-26 20:09 | +15 | XRP | DOWN | 0.60 | 0.76 | 1.30 |
| 11-26 20:09 | +10 | XRP | DOWN | 0.60 | 0.76 | 1.30 |
| 11-26 20:09 | +5 | XRP | DOWN | 0.60 | 0.76 | 1.30 |
| 11-26 20:08 | +10 stop | BTC | UP | 0.59 | 0.70 | 0.78 |
| 11-26 20:08 | +10 | BTC | UP | 0.59 | 0.70 | 0.78 |
| 11-26 20:08 | +5 | BTC | UP | 0.62 | 0.68 | 0.27 |
| 11-26 20:07 | +10 stop | SOL | UP | 0.64 | 0.80 | 1.31 |
| 11-26 20:06 | +10 stop | DOGE | DOWN | 0.63 | 0.48 | -1.85 |
| 11-26 20:06 | +20 | DOGE | DOWN | 0.63 | 0.85 | 1.94 |
| 11-26 20:06 | +15 | DOGE | DOWN | 0.63 | 0.81 | 1.52 |
| 11-26 20:06 | +10 | DOGE | DOWN | 0.63 | 0.81 | 1.52 |
| 11-26 20:06 | +5 | DOGE | DOWN | 0.63 | 0.81 | 1.52 |
| 11-26 20:06 | +5 | NEAR | UP | 0.68 | 0.81 | 1.03 |
| 11-26 20:06 | +5 | BTC | DOWN | 0.49 | 0.60 | 0.75 |
| 11-26 20:06 | +10 stop | SOL | DOWN | 0.65 | 0.49 | -1.94 |
| 11-26 20:04 | +5 | DOGE | DOWN | 0.60 | 0.66 | 0.27 |
| 11-26 20:04 | +15 | ETH | DOWN | 0.64 | 0.81 | 1.42 |
| 11-26 20:04 | +5 | ETH | DOWN | 0.64 | 0.71 | 0.38 |
| 11-26 20:04 | +5 | ZEC | UP | 0.65 | 0.70 | 0.19 |
| 11-26 20:04 | +10 stop | BNB | UP | 0.53 | 0.66 | 0.96 |
| 11-26 20:03 | +10 stop | ETH | DOWN | 0.62 | 0.45 | -2.05 |
| 11-26 20:03 | +10 | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 11-26 20:03 | +5 | ETH | DOWN | 0.62 | 0.67 | 0.17 |
| 11-26 20:03 | +5 | ZEC | UP | 0.51 | 0.57 | 0.24 |
