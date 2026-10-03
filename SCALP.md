# Range-Scalp Bot

*Updated Sat Oct 03 15:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 932 | 817 | 115 (2) | 2 | $-230.06 | -3.9% |
| **+10¢** | 704 | 578 | 126 (4) | 2 | $-110.80 | -2.5% |
| **+15¢** | 594 | 458 | 136 (5) | 1 | $-86.65 | -2.3% |
| **+20¢** | 519 | 376 | 143 (5) | 1 | $-75.87 | -2.3% |
| **+10¢ (15¢ stop)** | 1167 | 1166 | 1 (1) | 0 | $-562.21 | -7.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 15:26 | +10 stop | SOL | UP | 0.62 | 0.87 | 2.26 |
| 10-03 15:25 | +10 stop | SOL | DOWN | 0.71 | 0.45 | -2.93 |
| 10-03 15:24 | +15 | BTC | UP | 0.64 | 0.86 | 1.94 |
| 10-03 15:24 | +5 | BTC | UP | 0.64 | 0.70 | 0.28 |
| 10-03 15:23 | +5 | SOL | UP | 0.61 | 0.67 | 0.27 |
| 10-03 15:23 | +5 | NEAR | UP | 0.60 | open |  |
| 10-03 15:22 | +10 stop | ETH | UP | 0.68 | 0.53 | -1.84 |
| 10-03 15:22 | +15 | ETH | UP | 0.68 | 0.83 | 1.24 |
| 10-03 15:22 | +10 | ETH | UP | 0.68 | 0.82 | 1.13 |
| 10-03 15:22 | +5 | ETH | UP | 0.68 | 0.74 | 0.30 |
| 10-03 15:22 | +10 stop | SOL | UP | 0.55 | 0.39 | -1.94 |
| 10-03 15:22 | +15 | SOL | UP | 0.55 | 0.87 | 2.95 |
| 10-03 15:22 | +10 | SOL | UP | 0.55 | 0.65 | 0.67 |
| 10-03 15:22 | +5 | SOL | UP | 0.55 | 0.63 | 0.46 |
| 10-03 15:22 | +10 stop | NEAR | UP | 0.58 | 0.35 | -2.63 |
| 10-03 15:22 | +10 | NEAR | UP | 0.58 | open |  |
| 10-03 15:22 | +5 | NEAR | UP | 0.58 | 0.65 | 0.37 |
| 10-03 15:22 | +10 stop | ZEC | UP | 0.61 | 0.46 | -1.90 |
| 10-03 15:22 | +10 stop | BTC | UP | 0.68 | 0.86 | 1.55 |
| 10-03 15:22 | +10 | BTC | UP | 0.68 | 0.86 | 1.55 |
| 10-03 15:22 | +5 | BTC | UP | 0.68 | 0.73 | 0.20 |
| 10-03 15:22 | +10 stop | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 10-03 15:22 | +10 | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 10-03 15:22 | +5 | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 10-03 15:21 | +10 stop | NEAR | DOWN | 0.25 | 0.59 | 3.09 |
| 10-03 15:21 | +10 | NEAR | DOWN | 0.28 | 0.59 | 2.83 |
| 10-03 15:21 | +5 | NEAR | DOWN | 0.28 | 0.59 | 2.83 |
| 10-03 15:21 | +5 | ZEC | DOWN | 0.65 | 0.81 | 1.33 |
| 10-03 15:21 | +5 | BTC | UP | 0.58 | 0.68 | 0.66 |
| 10-03 15:20 | +5 | BTC | UP | 0.53 | 0.63 | 0.65 |
| 10-03 15:20 | +5 | ETH | UP | 0.71 | 0.79 | 0.54 |
| 10-03 15:19 | +5 | BTC | UP | 0.53 | 0.60 | 0.35 |
| 10-03 15:19 | +10 stop | BTC | UP | 0.54 | 0.68 | 1.06 |
| 10-03 15:19 | +5 | ZEC | DOWN | 0.63 | 0.68 | 0.17 |
| 10-03 15:19 | +5 | SOL | UP | 0.67 | 0.76 | 0.61 |
| 10-03 15:19 | +10 stop | BTC | DOWN | 0.44 | 0.57 | 0.94 |
| 10-03 15:18 | +10 stop | SOL | UP | 0.60 | 0.76 | 1.30 |
| 10-03 15:18 | +10 | SOL | UP | 0.60 | 0.76 | 1.30 |
| 10-03 15:18 | +5 | SOL | UP | 0.60 | 0.65 | 0.17 |
| 10-03 15:18 | +10 stop | DOGE | UP | 0.69 | 0.90 | 1.92 |
