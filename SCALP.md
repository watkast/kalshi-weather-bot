# Range-Scalp Bot

*Updated Wed Oct 14 01:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15242 | 13185 | 2057 (27) | 2 | $-4934.96 | -5.1% |
| **+10¢** | 11533 | 9146 | 2387 (39) | 2 | $-4609.85 | -6.3% |
| **+15¢** | 9690 | 7134 | 2556 (58) | 2 | $-4108.94 | -6.8% |
| **+20¢** | 8616 | 5944 | 2672 (74) | 2 | $-3618.36 | -6.7% |
| **+10¢ (15¢ stop)** | 18682 | 18632 | 50 (29) | 2 | $-7200.65 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 01:30 | +10 stop | BTC | DOWN | 0.53 | open |  |
| 10-14 01:30 | +20 | BTC | DOWN | 0.53 | open |  |
| 10-14 01:30 | +15 | BTC | DOWN | 0.53 | open |  |
| 10-14 01:30 | +10 | BTC | DOWN | 0.53 | open |  |
| 10-14 01:30 | +5 | BTC | DOWN | 0.53 | open |  |
| 10-14 01:30 | +10 stop | DOGE | DOWN | 0.57 | open |  |
| 10-14 01:30 | +20 | DOGE | DOWN | 0.57 | open |  |
| 10-14 01:30 | +15 | DOGE | DOWN | 0.57 | open |  |
| 10-14 01:30 | +10 | DOGE | DOWN | 0.57 | open |  |
| 10-14 01:30 | +5 | DOGE | DOWN | 0.57 | open |  |
| 10-14 01:28 | +10 stop | NEAR | UP | 0.25 | 0.59 | 3.11 |
| 10-14 01:28 | +20 | NEAR | UP | 0.25 | 0.59 | 3.09 |
| 10-14 01:28 | +15 | NEAR | UP | 0.27 | 0.59 | 2.89 |
| 10-14 01:28 | +10 | NEAR | UP | 0.27 | 0.59 | 2.89 |
| 10-14 01:28 | +5 | NEAR | UP | 0.27 | 0.59 | 2.89 |
| 10-14 01:24 | +10 stop | ETH | UP | 0.54 | 0.71 | 1.37 |
| 10-14 01:24 | +10 stop | ZEC | UP | 0.50 | 0.64 | 1.05 |
| 10-14 01:24 | +15 | HYPE | UP | 0.71 | 0.89 | 1.58 |
| 10-14 01:24 | +10 | HYPE | UP | 0.70 | 0.81 | 0.84 |
| 10-14 01:24 | +5 | HYPE | UP | 0.69 | 0.77 | 0.56 |
| 10-14 01:23 | +10 stop | ETH | UP | 0.50 | 0.66 | 1.26 |
| 10-14 01:23 | +10 stop | SOL | UP | 0.69 | 0.87 | 1.57 |
| 10-14 01:23 | +10 stop | XRP | DOWN | 0.58 | 0.27 | -3.42 |
| 10-14 01:22 | +10 stop | BTC | UP | 0.64 | 0.80 | 1.31 |
| 10-14 01:22 | +10 stop | ZEC | DOWN | 0.64 | 0.41 | -2.64 |
| 10-14 01:22 | +10 | ZEC | DOWN | 0.64 | yes | -6.57 |
| 10-14 01:22 | +5 | ZEC | DOWN | 0.64 | yes | -6.57 |
| 10-14 01:22 | +10 stop | NEAR | DOWN | 0.56 | 0.34 | -2.54 |
| 10-14 01:22 | +10 stop | DOGE | DOWN | 0.53 | 0.36 | -2.05 |
| 10-14 01:22 | +10 stop | ETH | DOWN | 0.66 | 0.50 | -1.94 |
| 10-14 01:22 | +10 stop | XRP | DOWN | 0.68 | 0.53 | -1.84 |
| 10-14 01:22 | +10 | XRP | DOWN | 0.68 | 0.84 | 1.34 |
| 10-14 01:22 | +5 | XRP | DOWN | 0.68 | 0.84 | 1.34 |
| 10-14 01:20 | +10 stop | SOL | DOWN | 0.68 | 0.46 | -2.54 |
| 10-14 01:20 | +10 | SOL | DOWN | 0.68 | yes | -6.96 |
| 10-14 01:20 | +5 | SOL | DOWN | 0.69 | yes | -7.05 |
| 10-14 01:20 | +10 stop | ETH | DOWN | 0.71 | 0.55 | -1.93 |
| 10-14 01:20 | +20 | ETH | DOWN | 0.71 | 0.92 | 1.86 |
| 10-14 01:20 | +15 | ETH | DOWN | 0.71 | 0.92 | 1.86 |
| 10-14 01:20 | +10 | ETH | DOWN | 0.71 | 0.92 | 1.86 |
