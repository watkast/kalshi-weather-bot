# Range-Scalp Bot

*Updated Tue Oct 20 00:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24801 | 21589 | 3212 (31) | 1 | $-7274.95 | -4.7% |
| **+10¢** | 18650 | 14938 | 3712 (46) | 1 | $-6481.77 | -5.5% |
| **+15¢** | 15609 | 11610 | 3999 (70) | 1 | $-5862.61 | -6.0% |
| **+20¢** | 13800 | 9612 | 4188 (88) | 2 | $-5288.69 | -6.1% |
| **+10¢ (15¢ stop)** | 30444 | 30392 | 52 (30) | 0 | $-11404.41 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 00:05 | +10 stop | SOL | DOWN | 0.71 | 0.85 | 1.16 |
| 10-20 00:05 | +10 | SOL | DOWN | 0.71 | 0.85 | 1.16 |
| 10-20 00:05 | +5 | SOL | DOWN | 0.71 | 0.78 | 0.42 |
| 10-20 00:05 | +10 stop | ZEC | DOWN | 0.63 | 0.77 | 1.10 |
| 10-20 00:05 | +15 | ZEC | DOWN | 0.63 | 0.80 | 1.41 |
| 10-20 00:05 | +10 | ZEC | DOWN | 0.63 | 0.77 | 1.10 |
| 10-20 00:04 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 10-20 00:04 | +10 stop | XRP | DOWN | 0.66 | 0.79 | 1.02 |
| 10-20 00:04 | +10 stop | NEAR | DOWN | 0.61 | 0.76 | 1.20 |
| 10-20 00:04 | +10 stop | NEAR | UP | 0.41 | 0.54 | 0.95 |
| 10-20 00:04 | +5 | DOGE | DOWN | 0.69 | 0.74 | 0.21 |
| 10-20 00:04 | +10 stop | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 10-20 00:04 | +10 | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 10-20 00:04 | +5 | BNB | DOWN | 0.71 | 0.77 | 0.32 |
| 10-20 00:04 | +10 stop | XRP | UP | 0.55 | 0.39 | -1.95 |
| 10-20 00:03 | +5 | ZEC | UP | 0.69 | open |  |
| 10-20 00:03 | +5 | BNB | DOWN | 0.63 | 0.71 | 0.48 |
| 10-20 00:02 | +10 stop | NEAR | UP | 0.52 | 0.65 | 0.96 |
| 10-20 00:02 | +10 stop | DOGE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-20 00:02 | +20 | DOGE | DOWN | 0.68 | 0.88 | 1.76 |
| 10-20 00:02 | +15 | DOGE | DOWN | 0.69 | 0.87 | 1.57 |
| 10-20 00:02 | +10 | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-20 00:02 | +5 | DOGE | DOWN | 0.69 | 0.74 | 0.21 |
| 10-20 00:02 | +10 stop | ZEC | UP | 0.56 | 0.72 | 1.27 |
| 10-20 00:02 | +20 | ZEC | UP | 0.56 | open |  |
| 10-20 00:02 | +15 | ZEC | UP | 0.56 | 0.72 | 1.27 |
| 10-20 00:02 | +10 | ZEC | UP | 0.56 | 0.72 | 1.27 |
| 10-20 00:02 | +5 | ZEC | UP | 0.56 | 0.65 | 0.56 |
| 10-20 00:02 | +10 stop | BNB | DOWN | 0.61 | 0.71 | 0.68 |
| 10-20 00:02 | +10 | BNB | DOWN | 0.61 | 0.71 | 0.68 |
| 10-20 00:02 | +5 | BNB | DOWN | 0.61 | 0.67 | 0.27 |
| 10-20 00:02 | +5 | NEAR | DOWN | 0.48 | 0.55 | 0.34 |
| 10-20 00:02 | +5 | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 10-20 00:02 | +10 stop | BTC | DOWN | 0.59 | 0.71 | 0.88 |
| 10-20 00:02 | +10 | BTC | DOWN | 0.60 | 0.71 | 0.78 |
| 10-20 00:02 | +5 | BTC | DOWN | 0.60 | 0.65 | 0.17 |
| 10-20 00:02 | +5 | SOL | DOWN | 0.62 | 0.69 | 0.38 |
| 10-20 00:01 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 10-20 00:01 | +10 stop | NEAR | DOWN | 0.57 | 0.42 | -1.86 |
| 10-20 00:01 | +20 | NEAR | DOWN | 0.57 | 0.79 | 1.90 |
