# Range-Scalp Bot

*Updated Thu Oct 22 23:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29443 | 25626 | 3817 (39) | 5 | $-8701.86 | -4.7% |
| **+10¢** | 22075 | 17654 | 4421 (55) | 5 | $-7862.77 | -5.7% |
| **+15¢** | 18483 | 13737 | 4746 (78) | 7 | $-7038.39 | -6.1% |
| **+20¢** | 16355 | 11380 | 4975 (100) | 7 | $-6386.94 | -6.2% |
| **+10¢ (15¢ stop)** | 36137 | 36078 | 59 (32) | 2 | $-13638.31 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 23:25 | +10 stop | ETH | DOWN | 0.71 | 0.56 | -1.83 |
| 10-22 23:25 | +5 | ETH | DOWN | 0.71 | open |  |
| 10-22 23:24 | +10 stop | DOGE | UP | 0.62 | 0.79 | 1.41 |
| 10-22 23:24 | +5 | HYPE | DOWN | 0.71 | open |  |
| 10-22 23:24 | +5 | NEAR | DOWN | 0.64 | 0.72 | 0.48 |
| 10-22 23:23 | +10 stop | BTC | DOWN | 0.64 | 0.78 | 1.10 |
| 10-22 23:23 | +20 | BTC | DOWN | 0.64 | open |  |
| 10-22 23:23 | +15 | BTC | DOWN | 0.64 | open |  |
| 10-22 23:23 | +10 | BTC | DOWN | 0.64 | 0.78 | 1.10 |
| 10-22 23:23 | +5 | BTC | DOWN | 0.64 | 0.70 | 0.28 |
| 10-22 23:23 | +10 stop | HYPE | DOWN | 0.61 | 0.74 | 0.99 |
| 10-22 23:23 | +15 | HYPE | DOWN | 0.61 | open |  |
| 10-22 23:23 | +10 | HYPE | DOWN | 0.61 | 0.74 | 0.99 |
| 10-22 23:23 | +5 | HYPE | DOWN | 0.61 | 0.66 | 0.17 |
| 10-22 23:23 | +5 | BNB | DOWN | 0.69 | open |  |
| 10-22 23:23 | +10 stop | NEAR | DOWN | 0.55 | 0.67 | 0.86 |
| 10-22 23:23 | +5 | NEAR | DOWN | 0.55 | 0.61 | 0.25 |
| 10-22 23:22 | +10 stop | DOGE | DOWN | 0.49 | 0.34 | -1.84 |
| 10-22 23:22 | +10 | DOGE | DOWN | 0.49 | open |  |
| 10-22 23:21 | +10 stop | ZEC | DOWN | 0.71 | open |  |
| 10-22 23:21 | +5 | DOGE | DOWN | 0.62 | open |  |
| 10-22 23:21 | +10 stop | ETH | DOWN | 0.66 | 0.47 | -2.24 |
| 10-22 23:21 | +15 | ETH | DOWN | 0.66 | open |  |
| 10-22 23:21 | +10 | ETH | DOWN | 0.66 | open |  |
| 10-22 23:21 | +5 | ETH | DOWN | 0.66 | 0.71 | 0.19 |
| 10-22 23:21 | +5 | BTC | DOWN | 0.61 | 0.70 | 0.58 |
| 10-22 23:20 | +10 stop | ZEC | UP | 0.58 | 0.40 | -2.15 |
| 10-22 23:20 | +20 | ZEC | UP | 0.58 | open |  |
| 10-22 23:20 | +15 | ZEC | UP | 0.59 | open |  |
| 10-22 23:20 | +10 | ZEC | UP | 0.59 | open |  |
| 10-22 23:20 | +5 | ZEC | UP | 0.59 | open |  |
| 10-22 23:20 | +10 stop | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 10-22 23:20 | +15 | SOL | DOWN | 0.67 | 0.84 | 1.44 |
| 10-22 23:20 | +10 | SOL | DOWN | 0.67 | 0.81 | 1.13 |
| 10-22 23:20 | +5 | SOL | DOWN | 0.67 | 0.81 | 1.13 |
| 10-22 23:20 | +10 stop | BNB | DOWN | 0.66 | open |  |
| 10-22 23:20 | +20 | BNB | DOWN | 0.66 | open |  |
| 10-22 23:20 | +15 | BNB | DOWN | 0.66 | open |  |
| 10-22 23:20 | +10 | BNB | DOWN | 0.66 | open |  |
| 10-22 23:20 | +5 | BNB | DOWN | 0.65 | 0.70 | 0.19 |
