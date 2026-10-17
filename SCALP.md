# Range-Scalp Bot

*Updated Sat Oct 17 16:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21245 | 18499 | 2746 (29) | 1 | $-6147.55 | -4.6% |
| **+10¢** | 15988 | 12816 | 3172 (41) | 2 | $-5474.24 | -5.4% |
| **+15¢** | 13366 | 9949 | 3417 (61) | 2 | $-4961.22 | -5.9% |
| **+20¢** | 11845 | 8265 | 3580 (80) | 2 | $-4397.69 | -5.9% |
| **+10¢ (15¢ stop)** | 26090 | 26040 | 50 (29) | 0 | $-9921.02 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 16:42 | +10 stop | XRP | UP | 0.45 | 0.62 | 1.35 |
| 10-17 16:41 | +10 stop | HYPE | UP | 0.67 | 0.87 | 1.76 |
| 10-17 16:41 | +15 | DOGE | DOWN | 0.71 | 0.92 | 1.91 |
| 10-17 16:41 | +10 stop | DOGE | DOWN | 0.70 | 0.92 | 2.01 |
| 10-17 16:41 | +20 | DOGE | DOWN | 0.71 | 0.92 | 1.91 |
| 10-17 16:41 | +10 | DOGE | DOWN | 0.71 | 0.92 | 1.91 |
| 10-17 16:41 | +5 | DOGE | DOWN | 0.69 | 0.74 | 0.21 |
| 10-17 16:40 | +10 stop | XRP | DOWN | 0.58 | 0.39 | -2.29 |
| 10-17 16:39 | +10 stop | HYPE | DOWN | 0.56 | 0.41 | -1.85 |
| 10-17 16:39 | +10 stop | XRP | DOWN | 0.63 | 0.46 | -2.05 |
| 10-17 16:39 | +10 | XRP | DOWN | 0.64 | open |  |
| 10-17 16:39 | +5 | XRP | DOWN | 0.64 | open |  |
| 10-17 16:38 | +10 stop | BNB | DOWN | 0.53 | 0.70 | 1.34 |
| 10-17 16:38 | +10 stop | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-17 16:38 | +20 | DOGE | DOWN | 0.62 | 0.86 | 2.14 |
| 10-17 16:38 | +15 | DOGE | DOWN | 0.62 | 0.77 | 1.20 |
| 10-17 16:38 | +10 | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-17 16:38 | +5 | DOGE | DOWN | 0.62 | 0.67 | 0.17 |
| 10-17 16:38 | +10 stop | NEAR | DOWN | 0.60 | 0.76 | 1.29 |
| 10-17 16:38 | +15 | NEAR | DOWN | 0.60 | 0.76 | 1.30 |
| 10-17 16:38 | +10 | NEAR | DOWN | 0.60 | 0.76 | 1.27 |
| 10-17 16:38 | +5 | NEAR | DOWN | 0.60 | 0.69 | 0.55 |
| 10-17 16:38 | +10 stop | XRP | DOWN | 0.48 | 0.58 | 0.64 |
| 10-17 16:38 | +10 | XRP | DOWN | 0.48 | 0.58 | 0.64 |
| 10-17 16:38 | +5 | XRP | DOWN | 0.49 | 0.58 | 0.54 |
| 10-17 16:38 | +10 stop | HYPE | UP | 0.66 | 0.47 | -2.24 |
| 10-17 16:38 | +5 | HYPE | UP | 0.60 | 0.66 | 0.23 |
| 10-17 16:38 | +10 stop | BNB | DOWN | 0.71 | 0.51 | -2.33 |
| 10-17 16:38 | +10 | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 10-17 16:38 | +5 | BNB | DOWN | 0.71 | 0.76 | 0.22 |
| 10-17 16:36 | +10 stop | ETH | DOWN | 0.68 | 0.81 | 1.03 |
| 10-17 16:36 | +10 stop | HYPE | DOWN | 0.59 | 0.40 | -2.24 |
| 10-17 16:36 | +10 | HYPE | DOWN | 0.59 | open |  |
| 10-17 16:36 | +5 | HYPE | DOWN | 0.59 | 0.67 | 0.47 |
| 10-17 16:35 | +10 stop | DOGE | DOWN | 0.67 | 0.83 | 1.34 |
| 10-17 16:35 | +15 | DOGE | DOWN | 0.67 | 0.83 | 1.34 |
| 10-17 16:35 | +10 | DOGE | DOWN | 0.67 | 0.83 | 1.34 |
| 10-17 16:35 | +5 | DOGE | DOWN | 0.65 | 0.72 | 0.42 |
| 10-17 16:35 | +5 | BNB | DOWN | 0.66 | 0.75 | 0.60 |
| 10-17 16:35 | +10 stop | XRP | UP | 0.59 | 0.28 | -3.42 |
