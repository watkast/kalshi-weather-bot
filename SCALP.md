# Range-Scalp Bot

*Updated Sun Oct 11 00:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11162 | 9623 | 1539 (22) | 2 | $-3798.21 | -5.4% |
| **+10¢** | 8456 | 6664 | 1792 (36) | 4 | $-3625.18 | -6.8% |
| **+15¢** | 7126 | 5232 | 1894 (52) | 4 | $-3054.69 | -6.8% |
| **+20¢** | 6346 | 4375 | 1971 (66) | 4 | $-2569.48 | -6.5% |
| **+10¢ (15¢ stop)** | 13751 | 13710 | 41 (25) | 3 | $-5502.96 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 00:48 | +10 stop | NEAR | UP | 0.71 | 0.81 | 0.74 |
| 10-11 00:48 | +10 | NEAR | UP | 0.71 | 0.81 | 0.74 |
| 10-11 00:48 | +5 | NEAR | UP | 0.71 | 0.81 | 0.74 |
| 10-11 00:48 | +5 | XRP | UP | 0.65 | 0.71 | 0.29 |
| 10-11 00:48 | +10 stop | XRP | UP | 0.61 | 0.71 | 0.68 |
| 10-11 00:48 | +10 | XRP | UP | 0.61 | 0.71 | 0.68 |
| 10-11 00:48 | +5 | XRP | UP | 0.61 | 0.66 | 0.17 |
| 10-11 00:47 | +10 stop | HYPE | UP | 0.64 | open |  |
| 10-11 00:46 | +10 | SOL | UP | 0.71 | open |  |
| 10-11 00:46 | +5 | SOL | UP | 0.71 | 0.77 | 0.32 |
| 10-11 00:46 | +10 stop | SOL | UP | 0.71 | open |  |
| 10-11 00:46 | +20 | SOL | UP | 0.71 | open |  |
| 10-11 00:46 | +15 | SOL | UP | 0.71 | open |  |
| 10-11 00:46 | +10 stop | ETH | UP | 0.65 | open |  |
| 10-11 00:46 | +20 | ETH | UP | 0.65 | open |  |
| 10-11 00:46 | +15 | ETH | UP | 0.65 | open |  |
| 10-11 00:46 | +10 | ETH | UP | 0.65 | open |  |
| 10-11 00:46 | +5 | ETH | UP | 0.65 | 0.71 | 0.29 |
| 10-11 00:46 | +10 stop | XRP | UP | 0.60 | 0.72 | 0.88 |
| 10-11 00:46 | +20 | XRP | UP | 0.60 | 0.81 | 1.82 |
| 10-11 00:46 | +15 | XRP | UP | 0.60 | 0.78 | 1.50 |
| 10-11 00:46 | +10 | XRP | UP | 0.60 | 0.72 | 0.88 |
| 10-11 00:46 | +5 | XRP | UP | 0.60 | 0.67 | 0.37 |
| 10-11 00:46 | +10 stop | NEAR | UP | 0.61 | 0.72 | 0.78 |
| 10-11 00:46 | +20 | NEAR | UP | 0.61 | 0.81 | 1.73 |
| 10-11 00:46 | +15 | NEAR | UP | 0.61 | 0.81 | 1.73 |
| 10-11 00:46 | +10 | NEAR | UP | 0.62 | 0.72 | 0.72 |
| 10-11 00:46 | +5 | NEAR | UP | 0.62 | 0.68 | 0.31 |
| 10-11 00:46 | +10 stop | ZEC | UP | 0.71 | 0.83 | 0.96 |
| 10-11 00:46 | +20 | ZEC | UP | 0.71 | 0.93 | 2.03 |
| 10-11 00:46 | +15 | ZEC | UP | 0.71 | 0.89 | 1.59 |
| 10-11 00:46 | +10 | ZEC | UP | 0.71 | 0.83 | 0.96 |
| 10-11 00:46 | +5 | ZEC | UP | 0.71 | 0.78 | 0.43 |
| 10-11 00:46 | +10 stop | DOGE | UP | 0.61 | 0.77 | 1.30 |
| 10-11 00:46 | +20 | DOGE | UP | 0.61 | 0.82 | 1.82 |
| 10-11 00:46 | +15 | DOGE | UP | 0.60 | 0.77 | 1.40 |
| 10-11 00:46 | +10 | DOGE | UP | 0.60 | 0.77 | 1.40 |
| 10-11 00:46 | +5 | DOGE | UP | 0.60 | 0.69 | 0.58 |
| 10-11 00:46 | +10 stop | BNB | UP | 0.68 | 0.51 | -2.04 |
| 10-11 00:46 | +20 | BNB | UP | 0.68 | open |  |
