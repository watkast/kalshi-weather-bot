# Range-Scalp Bot

*Updated Tue Oct 13 07:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14380 | 12437 | 1943 (27) | 4 | $-4631.28 | -5.1% |
| **+10¢** | 10874 | 8617 | 2257 (39) | 4 | $-4361.65 | -6.4% |
| **+15¢** | 9131 | 6719 | 2412 (57) | 6 | $-3870.96 | -6.8% |
| **+20¢** | 8126 | 5613 | 2513 (72) | 6 | $-3329.18 | -6.5% |
| **+10¢ (15¢ stop)** | 17623 | 17574 | 49 (29) | 0 | $-6818.06 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 07:25 | +10 stop | DOGE | DOWN | 0.63 | 0.75 | 0.89 |
| 10-13 07:24 | +10 stop | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 10-13 07:24 | +20 | BNB | DOWN | 0.71 | 0.94 | 2.05 |
| 10-13 07:24 | +15 | BNB | DOWN | 0.71 | 0.88 | 1.47 |
| 10-13 07:24 | +10 | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 10-13 07:24 | +5 | BNB | DOWN | 0.71 | 0.80 | 0.63 |
| 10-13 07:24 | +10 stop | DOGE | UP | 0.52 | 0.30 | -2.53 |
| 10-13 07:24 | +15 | DOGE | UP | 0.53 | open |  |
| 10-13 07:24 | +10 | DOGE | UP | 0.53 | open |  |
| 10-13 07:24 | +5 | DOGE | UP | 0.52 | open |  |
| 10-13 07:23 | +10 stop | ETH | UP | 0.59 | 0.17 | -4.47 |
| 10-13 07:23 | +15 | ETH | UP | 0.60 | open |  |
| 10-13 07:23 | +10 | ETH | UP | 0.60 | open |  |
| 10-13 07:23 | +5 | ETH | UP | 0.60 | open |  |
| 10-13 07:22 | +10 stop | DOGE | UP | 0.54 | 0.83 | 2.62 |
| 10-13 07:22 | +10 | DOGE | UP | 0.54 | 0.83 | 2.62 |
| 10-13 07:22 | +5 | DOGE | UP | 0.54 | 0.83 | 2.62 |
| 10-13 07:22 | +10 stop | ZEC | UP | 0.60 | 0.39 | -2.44 |
| 10-13 07:22 | +10 | ZEC | UP | 0.60 | open |  |
| 10-13 07:22 | +5 | ZEC | UP | 0.60 | open |  |
| 10-13 07:22 | +10 stop | HYPE | DOWN | 0.69 | 0.86 | 1.46 |
| 10-13 07:22 | +10 | HYPE | DOWN | 0.69 | 0.86 | 1.46 |
| 10-13 07:22 | +5 | HYPE | DOWN | 0.69 | 0.74 | 0.21 |
| 10-13 07:21 | +10 stop | SOL | UP | 0.47 | 0.57 | 0.64 |
| 10-13 07:21 | +10 | SOL | UP | 0.47 | 0.57 | 0.64 |
| 10-13 07:21 | +10 stop | XRP | UP | 0.51 | 0.36 | -1.85 |
| 10-13 07:21 | +10 stop | NEAR | DOWN | 0.63 | 0.73 | 0.69 |
| 10-13 07:21 | +20 | NEAR | DOWN | 0.63 | 0.84 | 1.83 |
| 10-13 07:21 | +15 | NEAR | DOWN | 0.63 | 0.84 | 1.83 |
| 10-13 07:21 | +10 | NEAR | DOWN | 0.63 | 0.73 | 0.69 |
| 10-13 07:21 | +5 | NEAR | DOWN | 0.63 | 0.72 | 0.58 |
| 10-13 07:20 | +10 stop | SOL | DOWN | 0.59 | 0.37 | -2.54 |
| 10-13 07:20 | +10 stop | ZEC | DOWN | 0.52 | 0.35 | -2.02 |
| 10-13 07:20 | +10 stop | DOGE | DOWN | 0.48 | 0.67 | 1.57 |
| 10-13 07:20 | +10 stop | XRP | DOWN | 0.68 | 0.51 | -2.04 |
| 10-13 07:20 | +10 stop | HYPE | DOWN | 0.66 | 0.45 | -2.44 |
| 10-13 07:19 | +5 | SOL | DOWN | 0.61 | 0.68 | 0.37 |
| 10-13 07:19 | +10 stop | BNB | UP | 0.63 | 0.77 | 1.10 |
| 10-13 07:19 | +20 | BNB | UP | 0.63 | 0.85 | 1.94 |
| 10-13 07:19 | +15 | BNB | UP | 0.63 | 0.85 | 1.94 |
