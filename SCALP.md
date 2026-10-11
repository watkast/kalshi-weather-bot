# Range-Scalp Bot

*Updated Sun Oct 11 17:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12240 | 10557 | 1683 (24) | 3 | $-4098.01 | -5.3% |
| **+10¢** | 9299 | 7347 | 1952 (37) | 1 | $-3865.94 | -6.6% |
| **+15¢** | 7837 | 5765 | 2072 (54) | 0 | $-3301.09 | -6.7% |
| **+20¢** | 6985 | 4826 | 2159 (68) | 0 | $-2798.82 | -6.4% |
| **+10¢ (15¢ stop)** | 15076 | 15035 | 41 (25) | 0 | $-5946.91 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 17:43 | +10 stop | HYPE | DOWN | 0.54 | 0.66 | 0.86 |
| 10-11 17:43 | +10 stop | ETH | UP | 0.53 | 0.21 | -3.46 |
| 10-11 17:43 | +5 | ETH | UP | 0.53 | open |  |
| 10-11 17:43 | +10 stop | HYPE | UP | 0.64 | 0.43 | -2.45 |
| 10-11 17:43 | +5 | HYPE | UP | 0.65 | open |  |
| 10-11 17:42 | +10 stop | DOGE | UP | 0.61 | 0.36 | -2.84 |
| 10-11 17:42 | +10 | DOGE | UP | 0.61 | open |  |
| 10-11 17:42 | +5 | DOGE | UP | 0.61 | open |  |
| 10-11 17:40 | +10 stop | XRP | UP | 0.53 | 0.29 | -2.73 |
| 10-11 17:39 | +10 stop | BNB | UP | 0.68 | 0.46 | -2.54 |
| 10-11 17:37 | +10 stop | XRP | UP | 0.67 | 0.52 | -1.84 |
| 10-11 17:36 | +5 | NEAR | UP | 0.64 | 0.69 | 0.18 |
| 10-11 17:35 | +10 stop | ETH | UP | 0.63 | 0.78 | 1.20 |
| 10-11 17:35 | +5 | ETH | UP | 0.63 | 0.68 | 0.17 |
| 10-11 17:34 | +10 stop | DOGE | UP | 0.70 | 0.88 | 1.57 |
| 10-11 17:34 | +10 | DOGE | UP | 0.70 | 0.88 | 1.57 |
| 10-11 17:34 | +5 | DOGE | UP | 0.70 | 0.88 | 1.57 |
| 10-11 17:34 | +10 stop | BTC | UP | 0.71 | 0.90 | 1.69 |
| 10-11 17:34 | +5 | ETH | DOWN | 0.53 | 0.64 | 0.75 |
| 10-11 17:34 | +10 stop | DOGE | UP | 0.58 | 0.68 | 0.66 |
| 10-11 17:34 | +10 | DOGE | UP | 0.58 | 0.68 | 0.66 |
| 10-11 17:34 | +5 | DOGE | UP | 0.58 | 0.68 | 0.66 |
| 10-11 17:33 | +10 stop | HYPE | UP | 0.64 | 0.83 | 1.63 |
| 10-11 17:33 | +5 | HYPE | UP | 0.62 | 0.71 | 0.58 |
| 10-11 17:32 | +5 | HYPE | DOWN | 0.50 | 0.55 | 0.14 |
| 10-11 17:32 | +5 | XRP | DOWN | 0.61 | 0.67 | 0.27 |
| 10-11 17:32 | +10 stop | DOGE | UP | 0.54 | 0.67 | 0.96 |
| 10-11 17:32 | +10 | DOGE | UP | 0.54 | 0.67 | 0.96 |
| 10-11 17:32 | +5 | DOGE | UP | 0.54 | 0.62 | 0.45 |
| 10-11 17:32 | +10 stop | NEAR | UP | 0.56 | 0.67 | 0.76 |
| 10-11 17:32 | +20 | NEAR | UP | 0.56 | 0.78 | 1.89 |
| 10-11 17:32 | +15 | NEAR | UP | 0.56 | 0.74 | 1.48 |
| 10-11 17:32 | +10 | NEAR | UP | 0.56 | 0.67 | 0.76 |
| 10-11 17:32 | +5 | NEAR | UP | 0.56 | 0.62 | 0.25 |
| 10-11 17:31 | +10 stop | XRP | DOWN | 0.56 | 0.23 | -3.61 |
| 10-11 17:31 | +20 | XRP | DOWN | 0.56 | 0.87 | 2.84 |
| 10-11 17:31 | +15 | XRP | DOWN | 0.56 | 0.75 | 1.58 |
| 10-11 17:31 | +10 | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 10-11 17:31 | +5 | XRP | DOWN | 0.56 | 0.63 | 0.35 |
| 10-11 17:31 | +10 stop | SOL | UP | 0.63 | 0.74 | 0.82 |
