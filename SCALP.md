# Range-Scalp Bot

*Updated Tue Nov 17 16:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62996 | 54950 | 8046 (117) | 5 | $-17156.24 | -4.3% |
| **+10¢** | 47054 | 37640 | 9414 (159) | 3 | $-16025.74 | -5.4% |
| **+15¢** | 39441 | 29290 | 10151 (201) | 3 | $-14545.06 | -5.9% |
| **+20¢** | 35145 | 24500 | 10645 (256) | 3 | $-12723.35 | -5.8% |
| **+10¢ (15¢ stop)** | 76667 | 76511 | 156 (92) | 0 | $-28251.58 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 16:27 | +10 stop | HYPE | DOWN | 0.36 | 0.52 | 1.25 |
| 11-17 16:24 | +5 | ETH | DOWN | 0.71 | 0.88 | 1.47 |
| 11-17 16:24 | +10 stop | ETH | DOWN | 0.71 | 0.88 | 1.47 |
| 11-17 16:24 | +10 stop | ZEC | DOWN | 0.68 | 0.84 | 1.34 |
| 11-17 16:23 | +10 stop | DOGE | DOWN | 0.61 | 0.71 | 0.71 |
| 11-17 16:23 | +10 stop | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 11-17 16:22 | +15 | BTC | DOWN | 0.71 | 0.89 | 1.58 |
| 11-17 16:22 | +10 stop | ZEC | DOWN | 0.61 | 0.77 | 1.30 |
| 11-17 16:22 | +10 stop | BNB | UP | 0.60 | 0.45 | -1.85 |
| 11-17 16:22 | +10 stop | XRP | UP | 0.54 | 0.33 | -2.44 |
| 11-17 16:22 | +5 | XRP | UP | 0.55 | open |  |
| 11-17 16:22 | +10 stop | BTC | DOWN | 0.64 | 0.80 | 1.31 |
| 11-17 16:22 | +10 | BTC | DOWN | 0.64 | 0.80 | 1.31 |
| 11-17 16:22 | +5 | BTC | DOWN | 0.64 | 0.80 | 1.31 |
| 11-17 16:22 | +10 stop | DOGE | UP | 0.65 | 0.42 | -2.64 |
| 11-17 16:22 | +15 | DOGE | UP | 0.65 | open |  |
| 11-17 16:22 | +5 | DOGE | UP | 0.65 | open |  |
| 11-17 16:22 | +5 | HYPE | UP | 0.63 | 0.77 | 1.14 |
| 11-17 16:21 | +10 stop | HYPE | UP | 0.56 | 0.30 | -2.93 |
| 11-17 16:21 | +10 stop | NEAR | DOWN | 0.71 | 0.84 | 1.05 |
| 11-17 16:21 | +10 stop | ETH | UP | 0.66 | 0.31 | -3.81 |
| 11-17 16:21 | +10 stop | BNB | UP | 0.70 | 0.54 | -1.93 |
| 11-17 16:21 | +5 | BNB | UP | 0.71 | open |  |
| 11-17 16:21 | +10 stop | BTC | DOWN | 0.46 | 0.60 | 1.05 |
| 11-17 16:21 | +15 | BTC | DOWN | 0.46 | 0.66 | 1.66 |
| 11-17 16:21 | +10 | BTC | DOWN | 0.46 | 0.60 | 1.05 |
| 11-17 16:21 | +5 | BTC | DOWN | 0.46 | 0.60 | 1.05 |
| 11-17 16:21 | +10 stop | SOL | DOWN | 0.51 | 0.68 | 1.37 |
| 11-17 16:21 | +10 stop | DOGE | DOWN | 0.44 | 0.60 | 1.25 |
| 11-17 16:21 | +10 stop | XRP | DOWN | 0.61 | 0.36 | -2.84 |
| 11-17 16:21 | +10 stop | ETH | DOWN | 0.61 | 0.45 | -1.95 |
| 11-17 16:20 | +10 stop | BNB | DOWN | 0.65 | 0.44 | -2.44 |
| 11-17 16:20 | +5 | BNB | DOWN | 0.65 | 0.72 | 0.39 |
| 11-17 16:20 | +10 stop | BTC | DOWN | 0.71 | 0.84 | 1.05 |
| 11-17 16:20 | +20 | BTC | DOWN | 0.71 | 0.95 | 2.24 |
| 11-17 16:20 | +10 stop | BNB | UP | 0.45 | 0.56 | 0.74 |
| 11-17 16:20 | +5 | BNB | UP | 0.46 | 0.56 | 0.64 |
| 11-17 16:19 | +10 | DOGE | UP | 0.70 | open |  |
| 11-17 16:19 | +10 stop | XRP | UP | 0.64 | 0.48 | -1.95 |
| 11-17 16:19 | +10 stop | SOL | UP | 0.59 | 0.35 | -2.73 |
