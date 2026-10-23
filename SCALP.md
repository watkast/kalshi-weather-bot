# Range-Scalp Bot

*Updated Fri Oct 23 03:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29717 | 25863 | 3854 (39) | 0 | $-8803.12 | -4.7% |
| **+10¢** | 22278 | 17817 | 4461 (55) | 0 | $-7931.13 | -5.7% |
| **+15¢** | 18659 | 13870 | 4789 (78) | 0 | $-7101.60 | -6.1% |
| **+20¢** | 16513 | 11495 | 5018 (100) | 0 | $-6426.72 | -6.2% |
| **+10¢ (15¢ stop)** | 36461 | 36402 | 59 (32) | 0 | $-13736.72 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 03:43 | +10 stop | ZEC | DOWN | 0.07 | 0.58 | 4.88 |
| 10-23 03:41 | +10 stop | NEAR | DOWN | 0.42 | 0.59 | 1.31 |
| 10-23 03:41 | +10 stop | ZEC | UP | 0.59 | 0.25 | -3.71 |
| 10-23 03:41 | +10 | ZEC | UP | 0.59 | 0.95 | 3.35 |
| 10-23 03:41 | +5 | ZEC | UP | 0.61 | 0.95 | 3.16 |
| 10-23 03:41 | +10 stop | ETH | DOWN | 0.59 | 0.72 | 0.98 |
| 10-23 03:40 | +5 | ETH | DOWN | 0.64 | 0.72 | 0.48 |
| 10-23 03:40 | +10 stop | HYPE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-23 03:39 | +10 stop | DOGE | DOWN | 0.68 | 0.44 | -2.74 |
| 10-23 03:39 | +5 | DOGE | DOWN | 0.68 | yes | -6.96 |
| 10-23 03:39 | +5 | ETH | DOWN | 0.54 | 0.60 | 0.25 |
| 10-23 03:38 | +5 | ZEC | UP | 0.60 | 0.66 | 0.27 |
| 10-23 03:38 | +10 stop | NEAR | UP | 0.62 | 0.47 | -1.85 |
| 10-23 03:38 | +10 stop | ZEC | UP | 0.57 | 0.73 | 1.28 |
| 10-23 03:38 | +10 stop | XRP | UP | 0.69 | 0.83 | 1.15 |
| 10-23 03:38 | +10 stop | ETH | DOWN | 0.52 | 0.62 | 0.65 |
| 10-23 03:38 | +20 | ETH | DOWN | 0.52 | 0.72 | 1.67 |
| 10-23 03:38 | +5 | ETH | DOWN | 0.52 | 0.60 | 0.45 |
| 10-23 03:38 | +10 stop | NEAR | DOWN | 0.55 | 0.32 | -2.64 |
| 10-23 03:38 | +15 | NEAR | DOWN | 0.56 | 0.77 | 1.79 |
| 10-23 03:38 | +10 | NEAR | DOWN | 0.57 | 0.69 | 0.87 |
| 10-23 03:38 | +5 | NEAR | DOWN | 0.57 | 0.69 | 0.87 |
| 10-23 03:37 | +10 stop | NEAR | UP | 0.42 | 0.59 | 1.35 |
| 10-23 03:37 | +15 | NEAR | UP | 0.42 | 0.59 | 1.35 |
| 10-23 03:37 | +10 | NEAR | UP | 0.42 | 0.59 | 1.35 |
| 10-23 03:37 | +5 | NEAR | UP | 0.42 | 0.59 | 1.35 |
| 10-23 03:37 | +5 | DOGE | DOWN | 0.68 | 0.76 | 0.51 |
| 10-23 03:37 | +20 | XRP | UP | 0.66 | 0.91 | 2.27 |
| 10-23 03:37 | +15 | XRP | UP | 0.66 | 0.83 | 1.44 |
| 10-23 03:37 | +5 | XRP | UP | 0.66 | 0.72 | 0.29 |
| 10-23 03:37 | +10 stop | ZEC | UP | 0.60 | 0.42 | -2.15 |
| 10-23 03:37 | +20 | ZEC | UP | 0.60 | 0.95 | 3.25 |
| 10-23 03:37 | +15 | ZEC | UP | 0.60 | 0.95 | 3.25 |
| 10-23 03:37 | +10 | ZEC | UP | 0.60 | 0.73 | 0.99 |
| 10-23 03:37 | +5 | ZEC | UP | 0.60 | 0.65 | 0.17 |
| 10-23 03:36 | +10 stop | DOGE | DOWN | 0.55 | 0.67 | 0.86 |
| 10-23 03:36 | +5 | DOGE | DOWN | 0.55 | 0.62 | 0.35 |
| 10-23 03:36 | +10 stop | HYPE | UP | 0.60 | 0.38 | -2.54 |
| 10-23 03:36 | +15 | HYPE | UP | 0.60 | no | -6.17 |
| 10-23 03:36 | +10 | HYPE | UP | 0.60 | no | -6.17 |
