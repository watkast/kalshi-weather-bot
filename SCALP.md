# Range-Scalp Bot

*Updated Wed Oct 14 03:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15387 | 13325 | 2062 (27) | 3 | $-4861.58 | -5.0% |
| **+10¢** | 11639 | 9245 | 2394 (39) | 3 | $-4535.09 | -6.2% |
| **+15¢** | 9776 | 7211 | 2565 (58) | 4 | $-4038.52 | -6.6% |
| **+20¢** | 8689 | 6005 | 2684 (75) | 5 | $-3550.39 | -6.5% |
| **+10¢ (15¢ stop)** | 18870 | 18820 | 50 (29) | 0 | $-7262.37 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 03:27 | +10 stop | SOL | UP | 0.61 | 0.87 | 2.35 |
| 10-14 03:27 | +10 stop | HYPE | DOWN | 0.55 | 0.40 | -1.85 |
| 10-14 03:27 | +20 | HYPE | DOWN | 0.55 | open |  |
| 10-14 03:27 | +15 | HYPE | DOWN | 0.55 | 0.70 | 1.17 |
| 10-14 03:27 | +10 | HYPE | DOWN | 0.56 | 0.70 | 1.07 |
| 10-14 03:27 | +5 | HYPE | DOWN | 0.56 | 0.70 | 1.07 |
| 10-14 03:27 | +10 stop | ETH | UP | 0.67 | 0.94 | 2.44 |
| 10-14 03:25 | +20 | ETH | UP | 0.69 | 0.94 | 2.28 |
| 10-14 03:25 | +10 | ETH | UP | 0.68 | 0.94 | 2.35 |
| 10-14 03:25 | +5 | ETH | UP | 0.68 | 0.74 | 0.31 |
| 10-14 03:25 | +10 stop | DOGE | UP | 0.70 | 0.48 | -2.55 |
| 10-14 03:25 | +10 | DOGE | UP | 0.70 | 0.86 | 1.36 |
| 10-14 03:25 | +5 | DOGE | UP | 0.70 | 0.86 | 1.36 |
| 10-14 03:24 | +10 stop | BNB | DOWN | 0.56 | 0.66 | 0.66 |
| 10-14 03:24 | +10 stop | SOL | UP | 0.68 | 0.42 | -2.96 |
| 10-14 03:24 | +10 stop | XRP | UP | 0.58 | 0.23 | -3.81 |
| 10-14 03:24 | +10 | XRP | UP | 0.58 | 0.95 | 3.48 |
| 10-14 03:24 | +5 | XRP | UP | 0.58 | 0.95 | 3.48 |
| 10-14 03:24 | +10 stop | XRP | DOWN | 0.41 | 0.56 | 1.15 |
| 10-14 03:24 | +10 | XRP | DOWN | 0.41 | 0.56 | 1.15 |
| 10-14 03:24 | +5 | XRP | DOWN | 0.41 | 0.56 | 1.15 |
| 10-14 03:23 | +10 stop | DOGE | UP | 0.60 | 0.71 | 0.78 |
| 10-14 03:23 | +10 stop | ETH | UP | 0.69 | 0.51 | -2.13 |
| 10-14 03:23 | +10 stop | BNB | DOWN | 0.58 | 0.40 | -2.15 |
| 10-14 03:23 | +10 stop | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 10-14 03:23 | +5 | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 10-14 03:23 | +10 stop | SOL | DOWN | 0.59 | 0.40 | -2.24 |
| 10-14 03:23 | +10 | SOL | DOWN | 0.59 | open |  |
| 10-14 03:23 | +5 | SOL | DOWN | 0.59 | open |  |
| 10-14 03:22 | +10 stop | DOGE | DOWN | 0.71 | 0.52 | -2.23 |
| 10-14 03:22 | +10 stop | BTC | UP | 0.67 | 0.78 | 0.81 |
| 10-14 03:22 | +5 | BTC | UP | 0.67 | 0.78 | 0.81 |
| 10-14 03:21 | +10 stop | HYPE | UP | 0.59 | 0.69 | 0.68 |
| 10-14 03:21 | +5 | HYPE | UP | 0.59 | 0.69 | 0.64 |
| 10-14 03:21 | +10 stop | ETH | DOWN | 0.61 | 0.40 | -2.44 |
| 10-14 03:21 | +5 | SOL | DOWN | 0.65 | 0.73 | 0.50 |
| 10-14 03:21 | +10 stop | BNB | DOWN | 0.50 | 0.69 | 1.57 |
| 10-14 03:21 | +10 stop | SOL | DOWN | 0.55 | 0.73 | 1.48 |
| 10-14 03:21 | +20 | SOL | DOWN | 0.55 | open |  |
| 10-14 03:21 | +10 | SOL | DOWN | 0.55 | 0.73 | 1.48 |
