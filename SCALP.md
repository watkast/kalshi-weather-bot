# Range-Scalp Bot

*Updated Fri Nov 13 18:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58449 | 51003 | 7446 (105) | 2 | $-15736.14 | -4.3% |
| **+10¢** | 43671 | 34964 | 8707 (139) | 2 | $-14691.99 | -5.4% |
| **+15¢** | 36605 | 27227 | 9378 (174) | 2 | $-13267.20 | -5.8% |
| **+20¢** | 32609 | 22761 | 9848 (225) | 2 | $-11667.96 | -5.7% |
| **+10¢ (15¢ stop)** | 71192 | 71058 | 134 (82) | 0 | $-26210.62 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 18:24 | +10 stop | NEAR | DOWN | 0.63 | 0.41 | -2.54 |
| 11-13 18:24 | +5 | DOGE | UP | 0.61 | 0.69 | 0.48 |
| 11-13 18:24 | +5 | ZEC | DOWN | 0.61 | open |  |
| 11-13 18:24 | +10 stop | HYPE | DOWN | 0.59 | 0.36 | -2.64 |
| 11-13 18:23 | +10 stop | NEAR | DOWN | 0.67 | 0.50 | -2.04 |
| 11-13 18:23 | +5 | DOGE | UP | 0.59 | 0.64 | 0.16 |
| 11-13 18:23 | +10 stop | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 11-13 18:23 | +10 stop | DOGE | UP | 0.61 | 0.84 | 2.03 |
| 11-13 18:23 | +20 | DOGE | UP | 0.61 | 0.84 | 2.03 |
| 11-13 18:23 | +15 | DOGE | UP | 0.61 | 0.84 | 2.03 |
| 11-13 18:23 | +10 | DOGE | UP | 0.61 | 0.84 | 2.03 |
| 11-13 18:23 | +5 | DOGE | UP | 0.61 | 0.66 | 0.17 |
| 11-13 18:23 | +5 | ETH | UP | 0.58 | 0.66 | 0.46 |
| 11-13 18:23 | +10 stop | ZEC | DOWN | 0.67 | 0.39 | -3.13 |
| 11-13 18:22 | +10 stop | HYPE | DOWN | 0.56 | 0.70 | 1.07 |
| 11-13 18:22 | +10 stop | ETH | UP | 0.55 | 0.66 | 0.76 |
| 11-13 18:22 | +20 | ETH | UP | 0.55 | 0.76 | 1.79 |
| 11-13 18:22 | +15 | ETH | UP | 0.56 | 0.71 | 1.17 |
| 11-13 18:22 | +10 | ETH | UP | 0.56 | 0.66 | 0.66 |
| 11-13 18:22 | +5 | ETH | UP | 0.56 | 0.62 | 0.25 |
| 11-13 18:22 | +10 stop | SOL | UP | 0.58 | 0.41 | -2.05 |
| 11-13 18:22 | +10 | SOL | UP | 0.58 | 0.78 | 1.69 |
| 11-13 18:22 | +5 | SOL | UP | 0.57 | 0.64 | 0.35 |
| 11-13 18:21 | +10 stop | ZEC | UP | 0.60 | 0.42 | -2.15 |
| 11-13 18:20 | +10 stop | ETH | UP | 0.71 | 0.82 | 0.84 |
| 11-13 18:20 | +10 | ETH | UP | 0.71 | 0.82 | 0.84 |
| 11-13 18:20 | +5 | ETH | UP | 0.71 | 0.82 | 0.84 |
| 11-13 18:20 | +10 stop | HYPE | UP | 0.67 | 0.50 | -2.04 |
| 11-13 18:20 | +10 | HYPE | UP | 0.67 | 0.87 | 1.76 |
| 11-13 18:20 | +5 | HYPE | UP | 0.67 | 0.87 | 1.76 |
| 11-13 18:19 | +10 stop | NEAR | UP | 0.69 | 0.54 | -1.83 |
| 11-13 18:19 | +10 stop | ZEC | UP | 0.65 | 0.50 | -1.84 |
| 11-13 18:18 | +10 stop | HYPE | DOWN | 0.56 | 0.38 | -2.15 |
| 11-13 18:18 | +10 stop | NEAR | DOWN | 0.67 | 0.49 | -2.14 |
| 11-13 18:18 | +10 | NEAR | DOWN | 0.67 | open |  |
| 11-13 18:18 | +5 | NEAR | DOWN | 0.67 | open |  |
| 11-13 18:18 | +10 stop | SOL | UP | 0.59 | 0.73 | 1.09 |
| 11-13 18:18 | +10 stop | BNB | UP | 0.55 | 0.70 | 1.17 |
| 11-13 18:18 | +20 | BNB | UP | 0.55 | 0.81 | 2.31 |
| 11-13 18:18 | +15 | BNB | UP | 0.55 | 0.70 | 1.17 |
