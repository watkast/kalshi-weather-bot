# Range-Scalp Bot

*Updated Mon Oct 05 01:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3080 | 2638 | 442 (3) | 0 | $-1152.25 | -5.9% |
| **+10¢** | 2392 | 1891 | 501 (4) | 0 | $-1011.69 | -6.7% |
| **+15¢** | 2017 | 1489 | 528 (5) | 0 | $-880.02 | -6.9% |
| **+20¢** | 1799 | 1250 | 549 (10) | 1 | $-739.36 | -6.5% |
| **+10¢ (15¢ stop)** | 3852 | 3851 | 1 (1) | 0 | $-1535.16 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 01:30 | +10 stop | NEAR | DOWN | 0.70 | 0.82 | 0.95 |
| 10-05 01:30 | +20 | NEAR | DOWN | 0.70 | open |  |
| 10-05 01:30 | +15 | NEAR | DOWN | 0.70 | 0.85 | 1.27 |
| 10-05 01:30 | +10 | NEAR | DOWN | 0.69 | 0.79 | 0.73 |
| 10-05 01:30 | +5 | NEAR | DOWN | 0.69 | 0.79 | 0.73 |
| 10-05 01:28 | +10 stop | ZEC | DOWN | 0.02 | 0.53 | 4.87 |
| 10-05 01:28 | +20 | ZEC | DOWN | 0.02 | 0.53 | 4.87 |
| 10-05 01:28 | +15 | ZEC | DOWN | 0.02 | 0.53 | 4.87 |
| 10-05 01:28 | +10 | ZEC | DOWN | 0.02 | 0.53 | 4.87 |
| 10-05 01:28 | +5 | ZEC | DOWN | 0.02 | 0.53 | 4.87 |
| 10-05 01:25 | +10 stop | ZEC | DOWN | 0.63 | 0.81 | 1.52 |
| 10-05 01:25 | +5 | ZEC | DOWN | 0.63 | 0.71 | 0.48 |
| 10-05 01:24 | +5 | ZEC | DOWN | 0.48 | 0.57 | 0.57 |
| 10-05 01:23 | +10 stop | ZEC | DOWN | 0.67 | 0.43 | -2.74 |
| 10-05 01:23 | +10 stop | SOL | UP | 0.61 | 0.71 | 0.68 |
| 10-05 01:23 | +20 | SOL | UP | 0.61 | 0.87 | 2.35 |
| 10-05 01:23 | +10 | SOL | UP | 0.61 | 0.71 | 0.68 |
| 10-05 01:23 | +5 | SOL | UP | 0.61 | 0.71 | 0.68 |
| 10-05 01:23 | +10 stop | DOGE | UP | 0.60 | 0.75 | 1.19 |
| 10-05 01:23 | +20 | DOGE | UP | 0.60 | 0.88 | 2.55 |
| 10-05 01:23 | +15 | DOGE | UP | 0.60 | 0.75 | 1.19 |
| 10-05 01:23 | +10 | DOGE | UP | 0.60 | 0.75 | 1.19 |
| 10-05 01:23 | +5 | DOGE | UP | 0.60 | 0.65 | 0.17 |
| 10-05 01:23 | +10 stop | HYPE | UP | 0.58 | 0.80 | 1.90 |
| 10-05 01:22 | +10 stop | ETH | UP | 0.63 | 0.47 | -1.95 |
| 10-05 01:22 | +10 stop | NEAR | DOWN | 0.51 | 0.64 | 0.95 |
| 10-05 01:22 | +5 | BTC | UP | 0.68 | 0.73 | 0.20 |
| 10-05 01:21 | +10 stop | HYPE | UP | 0.57 | 0.70 | 0.97 |
| 10-05 01:20 | +10 stop | BTC | UP | 0.67 | 0.84 | 1.44 |
| 10-05 01:20 | +15 | BTC | UP | 0.70 | 0.91 | 1.86 |
| 10-05 01:20 | +10 | BTC | UP | 0.70 | 0.84 | 1.15 |
| 10-05 01:20 | +5 | BTC | UP | 0.70 | 0.75 | 0.21 |
| 10-05 01:20 | +10 stop | ZEC | UP | 0.64 | 0.80 | 1.31 |
| 10-05 01:20 | +10 stop | NEAR | UP | 0.58 | 0.43 | -1.86 |
| 10-05 01:20 | +15 | NEAR | UP | 0.58 | no | -5.98 |
| 10-05 01:20 | +10 | NEAR | UP | 0.58 | no | -5.98 |
| 10-05 01:20 | +5 | NEAR | UP | 0.58 | no | -5.98 |
| 10-05 01:19 | +10 stop | SOL | UP | 0.71 | 0.83 | 0.95 |
| 10-05 01:19 | +15 | SOL | UP | 0.71 | 0.87 | 1.37 |
| 10-05 01:19 | +10 | SOL | UP | 0.71 | 0.83 | 0.95 |
