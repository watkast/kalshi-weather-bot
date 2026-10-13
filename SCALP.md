# Range-Scalp Bot

*Updated Tue Oct 13 23:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15148 | 13105 | 2043 (27) | 1 | $-4893.87 | -5.1% |
| **+10¢** | 11451 | 9078 | 2373 (39) | 1 | $-4591.01 | -6.4% |
| **+15¢** | 9625 | 7086 | 2539 (58) | 1 | $-4080.09 | -6.8% |
| **+20¢** | 8557 | 5905 | 2652 (74) | 1 | $-3576.38 | -6.7% |
| **+10¢ (15¢ stop)** | 18569 | 18519 | 50 (29) | 0 | $-7171.11 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 23:40 | +20 | NEAR | DOWN | 0.66 | open |  |
| 10-13 23:40 | +15 | NEAR | DOWN | 0.67 | open |  |
| 10-13 23:39 | +10 stop | NEAR | DOWN | 0.71 | 0.50 | -2.43 |
| 10-13 23:39 | +10 | NEAR | DOWN | 0.71 | open |  |
| 10-13 23:39 | +10 stop | NEAR | UP | 0.47 | 0.57 | 0.64 |
| 10-13 23:39 | +10 | NEAR | UP | 0.47 | 0.57 | 0.64 |
| 10-13 23:38 | +10 stop | NEAR | DOWN | 0.51 | 0.62 | 0.75 |
| 10-13 23:38 | +15 | NEAR | DOWN | 0.51 | 0.69 | 1.47 |
| 10-13 23:38 | +10 | NEAR | DOWN | 0.51 | 0.62 | 0.75 |
| 10-13 23:36 | +10 stop | NEAR | UP | 0.54 | 0.34 | -2.34 |
| 10-13 23:36 | +5 | NEAR | UP | 0.54 | open |  |
| 10-13 23:36 | +5 | ETH | UP | 0.71 | 0.83 | 0.95 |
| 10-13 23:35 | +5 | BTC | UP | 0.55 | 0.69 | 1.07 |
| 10-13 23:35 | +5 | BTC | UP | 0.58 | 0.64 | 0.25 |
| 10-13 23:33 | +5 | BTC | UP | 0.58 | 0.63 | 0.15 |
| 10-13 23:31 | +15 | XRP | UP | 0.70 | 0.86 | 1.36 |
| 10-13 23:31 | +10 | XRP | UP | 0.70 | 0.81 | 0.84 |
| 10-13 23:31 | +5 | XRP | UP | 0.70 | 0.75 | 0.21 |
| 10-13 23:31 | +10 stop | XRP | UP | 0.71 | 0.81 | 0.74 |
| 10-13 23:31 | +20 | XRP | UP | 0.71 | 0.92 | 1.84 |
| 10-13 23:31 | +5 | NEAR | UP | 0.65 | 0.73 | 0.50 |
| 10-13 23:30 | +10 stop | NEAR | DOWN | 0.47 | 0.25 | -2.52 |
| 10-13 23:30 | +20 | NEAR | DOWN | 0.47 | 0.69 | 1.87 |
| 10-13 23:30 | +15 | NEAR | DOWN | 0.47 | 0.64 | 1.35 |
| 10-13 23:30 | +10 | NEAR | DOWN | 0.47 | 0.64 | 1.35 |
| 10-13 23:30 | +5 | NEAR | DOWN | 0.47 | 0.56 | 0.59 |
| 10-13 23:30 | +10 stop | SOL | UP | 0.64 | 0.74 | 0.69 |
| 10-13 23:30 | +20 | SOL | UP | 0.64 | 0.86 | 1.94 |
| 10-13 23:30 | +15 | SOL | UP | 0.64 | 0.79 | 1.21 |
| 10-13 23:30 | +10 | SOL | UP | 0.64 | 0.74 | 0.69 |
| 10-13 23:30 | +5 | SOL | UP | 0.64 | 0.73 | 0.59 |
| 10-13 23:30 | +10 stop | BTC | UP | 0.62 | 0.75 | 0.99 |
| 10-13 23:30 | +20 | BTC | UP | 0.62 | 0.84 | 1.93 |
| 10-13 23:30 | +15 | BTC | UP | 0.62 | 0.84 | 1.93 |
| 10-13 23:30 | +10 | BTC | UP | 0.62 | 0.75 | 0.99 |
| 10-13 23:30 | +5 | BTC | UP | 0.62 | 0.71 | 0.58 |
| 10-13 23:30 | +10 stop | ETH | UP | 0.66 | 0.83 | 1.44 |
| 10-13 23:30 | +20 | ETH | UP | 0.66 | 0.87 | 1.86 |
| 10-13 23:30 | +15 | ETH | UP | 0.66 | 0.83 | 1.44 |
| 10-13 23:30 | +10 | ETH | UP | 0.66 | 0.83 | 1.44 |
