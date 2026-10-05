# Range-Scalp Bot

*Updated Mon Oct 05 10:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3677 | 3159 | 518 (3) | 1 | $-1315.22 | -5.7% |
| **+10¢** | 2841 | 2245 | 596 (4) | 2 | $-1203.75 | -6.7% |
| **+15¢** | 2383 | 1757 | 626 (7) | 3 | $-1045.66 | -7.0% |
| **+20¢** | 2126 | 1474 | 652 (12) | 4 | $-898.09 | -6.7% |
| **+10¢ (15¢ stop)** | 4564 | 4563 | 1 (1) | 0 | $-1752.60 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 10:13 | +10 stop | ETH | DOWN | 0.70 | 0.89 | 1.68 |
| 10-05 10:13 | +15 | ETH | DOWN | 0.69 | 0.89 | 1.78 |
| 10-05 10:13 | +10 | ETH | DOWN | 0.69 | 0.89 | 1.78 |
| 10-05 10:13 | +10 stop | SOL | UP | 0.50 | 0.02 | -5.00 |
| 10-05 10:13 | +10 | SOL | UP | 0.49 | open |  |
| 10-05 10:13 | +5 | SOL | UP | 0.49 | 0.54 | 0.14 |
| 10-05 10:13 | +5 | ETH | DOWN | 0.70 | 0.89 | 1.68 |
| 10-05 10:12 | +10 stop | ETH | DOWN | 0.51 | 0.69 | 1.47 |
| 10-05 10:12 | +20 | ETH | DOWN | 0.50 | 0.89 | 3.62 |
| 10-05 10:12 | +15 | ETH | DOWN | 0.50 | 0.69 | 1.57 |
| 10-05 10:12 | +10 | ETH | DOWN | 0.50 | 0.69 | 1.57 |
| 10-05 10:12 | +5 | ETH | DOWN | 0.49 | 0.57 | 0.44 |
| 10-05 10:12 | +10 stop | HYPE | DOWN | 0.70 | 0.52 | -2.13 |
| 10-05 10:12 | +10 stop | SOL | UP | 0.47 | 0.58 | 0.74 |
| 10-05 10:12 | +20 | SOL | UP | 0.47 | open |  |
| 10-05 10:12 | +15 | SOL | UP | 0.47 | open |  |
| 10-05 10:12 | +10 | SOL | UP | 0.47 | 0.58 | 0.74 |
| 10-05 10:12 | +5 | SOL | UP | 0.47 | 0.58 | 0.74 |
| 10-05 10:12 | +5 | HYPE | DOWN | 0.68 | 0.99 | 2.96 |
| 10-05 10:12 | +10 stop | NEAR | UP | 0.59 | 0.71 | 0.88 |
| 10-05 10:12 | +20 | NEAR | UP | 0.59 | open |  |
| 10-05 10:12 | +15 | NEAR | UP | 0.61 | 0.76 | 1.20 |
| 10-05 10:12 | +10 | NEAR | UP | 0.63 | 0.76 | 1.00 |
| 10-05 10:12 | +5 | NEAR | UP | 0.63 | 0.71 | 0.50 |
| 10-05 10:11 | +5 | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 10-05 10:10 | +10 stop | HYPE | DOWN | 0.66 | 0.51 | -1.84 |
| 10-05 10:10 | +20 | HYPE | DOWN | 0.66 | 0.99 | 3.16 |
| 10-05 10:10 | +15 | HYPE | DOWN | 0.66 | 0.99 | 3.16 |
| 10-05 10:10 | +10 | HYPE | DOWN | 0.66 | 0.99 | 3.16 |
| 10-05 10:10 | +5 | HYPE | DOWN | 0.66 | 0.73 | 0.40 |
| 10-05 10:09 | +10 stop | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-05 10:09 | +10 | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-05 10:09 | +5 | ZEC | DOWN | 0.61 | 0.66 | 0.17 |
| 10-05 10:08 | +10 | NEAR | UP | 0.70 | 0.88 | 1.57 |
| 10-05 10:07 | +10 stop | ZEC | DOWN | 0.60 | 0.78 | 1.52 |
| 10-05 10:07 | +10 | ZEC | DOWN | 0.59 | 0.78 | 1.60 |
| 10-05 10:07 | +5 | ZEC | DOWN | 0.59 | 0.64 | 0.16 |
| 10-05 10:07 | +10 stop | NEAR | UP | 0.68 | 0.88 | 1.76 |
| 10-05 10:05 | +5 | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-05 10:04 | +10 stop | NEAR | UP | 0.58 | 0.34 | -2.74 |
