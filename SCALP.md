# Range-Scalp Bot

*Updated Mon Oct 05 15:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3904 | 3355 | 549 (4) | 4 | $-1393.79 | -5.7% |
| **+10¢** | 3017 | 2384 | 633 (5) | 5 | $-1288.36 | -6.8% |
| **+15¢** | 2537 | 1870 | 667 (8) | 5 | $-1125.20 | -7.1% |
| **+20¢** | 2266 | 1571 | 695 (13) | 5 | $-956.57 | -6.7% |
| **+10¢ (15¢ stop)** | 4829 | 4824 | 5 (2) | 0 | $-1833.42 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 15:26 | +10 stop | ZEC | DOWN | 0.59 | 0.71 | 0.83 |
| 10-05 15:26 | +10 stop | BTC | UP | 0.62 | 0.42 | -2.35 |
| 10-05 15:26 | +10 | BTC | UP | 0.62 | open |  |
| 10-05 15:26 | +10 stop | SOL | UP | 0.58 | 0.42 | -1.96 |
| 10-05 15:24 | +10 stop | BTC | UP | 0.55 | 0.72 | 1.37 |
| 10-05 15:24 | +10 stop | SOL | DOWN | 0.54 | 0.35 | -2.24 |
| 10-05 15:24 | +15 | SOL | DOWN | 0.54 | open |  |
| 10-05 15:24 | +10 | SOL | DOWN | 0.54 | open |  |
| 10-05 15:24 | +5 | SOL | DOWN | 0.54 | open |  |
| 10-05 15:24 | +10 stop | HYPE | DOWN | 0.60 | 0.32 | -3.13 |
| 10-05 15:24 | +5 | HYPE | DOWN | 0.60 | open |  |
| 10-05 15:23 | +10 stop | DOGE | UP | 0.60 | 0.72 | 0.88 |
| 10-05 15:23 | +5 | DOGE | UP | 0.60 | 0.65 | 0.17 |
| 10-05 15:23 | +10 stop | ETH | UP | 0.59 | 0.69 | 0.68 |
| 10-05 15:23 | +10 stop | ZEC | UP | 0.55 | 0.36 | -2.20 |
| 10-05 15:23 | +10 stop | ZEC | DOWN | 0.55 | 0.68 | 0.96 |
| 10-05 15:23 | +10 stop | DOGE | DOWN | 0.46 | 0.61 | 1.15 |
| 10-05 15:23 | +5 | DOGE | DOWN | 0.46 | 0.61 | 1.15 |
| 10-05 15:23 | +10 stop | ETH | DOWN | 0.48 | 0.59 | 0.75 |
| 10-05 15:22 | +10 stop | NEAR | UP | 0.60 | 0.72 | 0.88 |
| 10-05 15:22 | +10 | NEAR | UP | 0.60 | 0.72 | 0.88 |
| 10-05 15:22 | +5 | NEAR | UP | 0.60 | 0.67 | 0.37 |
| 10-05 15:22 | +5 | BTC | DOWN | 0.63 | open |  |
| 10-05 15:22 | +10 stop | BTC | DOWN | 0.63 | 0.43 | -2.35 |
| 10-05 15:22 | +10 stop | DOGE | UP | 0.45 | 0.57 | 0.84 |
| 10-05 15:22 | +5 | DOGE | UP | 0.46 | 0.57 | 0.74 |
| 10-05 15:21 | +10 stop | ETH | UP | 0.63 | 0.42 | -2.45 |
| 10-05 15:20 | +5 | BTC | DOWN | 0.54 | 0.63 | 0.55 |
| 10-05 15:19 | +10 stop | HYPE | DOWN | 0.60 | 0.71 | 0.78 |
| 10-05 15:19 | +5 | HYPE | DOWN | 0.60 | 0.71 | 0.78 |
| 10-05 15:19 | +5 | BTC | DOWN | 0.54 | 0.60 | 0.25 |
| 10-05 15:19 | +5 | DOGE | DOWN | 0.53 | 0.58 | 0.14 |
| 10-05 15:19 | +5 | ZEC | UP | 0.62 | open |  |
| 10-05 15:19 | +5 | DOGE | DOWN | 0.53 | 0.63 | 0.65 |
| 10-05 15:18 | +5 | ZEC | UP | 0.55 | 0.60 | 0.15 |
| 10-05 15:18 | +10 stop | BTC | DOWN | 0.53 | 0.38 | -1.85 |
| 10-05 15:18 | +5 | DOGE | DOWN | 0.58 | 0.63 | 0.15 |
| 10-05 15:18 | +10 stop | NEAR | UP | 0.70 | 0.82 | 0.94 |
| 10-05 15:18 | +20 | NEAR | UP | 0.70 | 0.93 | 2.06 |
| 10-05 15:18 | +15 | NEAR | UP | 0.70 | 0.88 | 1.57 |
