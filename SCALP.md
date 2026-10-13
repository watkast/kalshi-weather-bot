# Range-Scalp Bot

*Updated Tue Oct 13 22:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15074 | 13042 | 2032 (27) | 2 | $-4859.93 | -5.1% |
| **+10¢** | 11396 | 9035 | 2361 (39) | 4 | $-4560.64 | -6.4% |
| **+15¢** | 9578 | 7052 | 2526 (58) | 4 | $-4048.70 | -6.7% |
| **+20¢** | 8513 | 5880 | 2633 (74) | 7 | $-3508.11 | -6.6% |
| **+10¢ (15¢ stop)** | 18483 | 18433 | 50 (29) | 0 | $-7150.90 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 22:25 | +5 | HYPE | DOWN | 0.67 | 0.72 | 0.24 |
| 10-13 22:25 | +10 stop | ETH | UP | 0.69 | 0.87 | 1.57 |
| 10-13 22:24 | +5 | ETH | UP | 0.71 | 0.87 | 1.37 |
| 10-13 22:24 | +10 stop | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 10-13 22:24 | +5 | HYPE | DOWN | 0.58 | 0.63 | 0.15 |
| 10-13 22:24 | +10 | SOL | DOWN | 0.63 | 0.80 | 1.41 |
| 10-13 22:23 | +10 stop | BTC | UP | 0.66 | 0.84 | 1.54 |
| 10-13 22:23 | +10 stop | SOL | DOWN | 0.59 | 0.80 | 1.81 |
| 10-13 22:23 | +5 | XRP | UP | 0.69 | 0.76 | 0.42 |
| 10-13 22:23 | +5 | DOGE | UP | 0.70 | 0.75 | 0.21 |
| 10-13 22:23 | +10 stop | HYPE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-13 22:23 | +20 | HYPE | DOWN | 0.60 | open |  |
| 10-13 22:23 | +15 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-13 22:23 | +10 | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-13 22:23 | +5 | HYPE | DOWN | 0.62 | 0.68 | 0.27 |
| 10-13 22:22 | +5 | BNB | UP | 0.70 | 0.84 | 1.15 |
| 10-13 22:22 | +10 stop | SOL | UP | 0.63 | 0.44 | -2.25 |
| 10-13 22:22 | +15 | SOL | UP | 0.63 | open |  |
| 10-13 22:22 | +5 | ETH | UP | 0.58 | 0.64 | 0.25 |
| 10-13 22:21 | +10 | NEAR | UP | 0.64 | 0.83 | 1.63 |
| 10-13 22:21 | +10 stop | NEAR | UP | 0.69 | 0.83 | 1.15 |
| 10-13 22:21 | +5 | NEAR | UP | 0.69 | 0.83 | 1.15 |
| 10-13 22:21 | +10 stop | XRP | UP | 0.71 | 0.82 | 0.84 |
| 10-13 22:21 | +10 | XRP | UP | 0.71 | 0.82 | 0.84 |
| 10-13 22:21 | +5 | XRP | UP | 0.70 | 0.77 | 0.42 |
| 10-13 22:21 | +10 stop | BNB | UP | 0.62 | 0.84 | 1.89 |
| 10-13 22:21 | +15 | BNB | UP | 0.62 | 0.84 | 1.89 |
| 10-13 22:21 | +5 | BNB | UP | 0.62 | 0.69 | 0.34 |
| 10-13 22:21 | +10 stop | DOGE | UP | 0.70 | 0.81 | 0.84 |
| 10-13 22:21 | +15 | DOGE | UP | 0.70 | 0.96 | 2.44 |
| 10-13 22:21 | +5 | DOGE | UP | 0.70 | 0.78 | 0.52 |
| 10-13 22:21 | +5 | SOL | UP | 0.60 | open |  |
| 10-13 22:21 | +10 stop | ETH | DOWN | 0.47 | 0.30 | -2.03 |
| 10-13 22:21 | +10 | ETH | DOWN | 0.47 | open |  |
| 10-13 22:21 | +5 | ETH | DOWN | 0.48 | 0.55 | 0.34 |
| 10-13 22:20 | +10 stop | NEAR | DOWN | 0.40 | 0.58 | 1.43 |
| 10-13 22:20 | +10 stop | SOL | DOWN | 0.53 | 0.37 | -1.95 |
| 10-13 22:20 | +10 | SOL | DOWN | 0.53 | 0.66 | 0.96 |
| 10-13 22:20 | +5 | SOL | DOWN | 0.53 | 0.60 | 0.35 |
| 10-13 22:19 | +10 stop | BTC | DOWN | 0.71 | 0.43 | -3.13 |
