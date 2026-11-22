# Range-Scalp Bot

*Updated Sun Nov 22 23:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69238 | 60409 | 8829 (145) | 1 | $-18680.97 | -4.3% |
| **+10¢** | 51674 | 41366 | 10308 (188) | 1 | $-17329.38 | -5.3% |
| **+15¢** | 43307 | 32197 | 11110 (241) | 3 | $-15535.07 | -5.7% |
| **+20¢** | 38567 | 26891 | 11676 (300) | 5 | $-13825.88 | -5.7% |
| **+10¢ (15¢ stop)** | 84324 | 84135 | 189 (117) | 1 | $-31030.27 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 23:34 | +10 stop | NEAR | UP | 0.63 | 0.74 | 0.79 |
| 11-22 23:34 | +20 | NEAR | UP | 0.63 | open |  |
| 11-22 23:34 | +15 | NEAR | UP | 0.63 | open |  |
| 11-22 23:34 | +10 | NEAR | UP | 0.63 | 0.74 | 0.79 |
| 11-22 23:34 | +5 | NEAR | UP | 0.63 | 0.74 | 0.79 |
| 11-22 23:33 | +5 | DOGE | UP | 0.69 | 0.75 | 0.31 |
| 11-22 23:33 | +10 stop | DOGE | UP | 0.69 | 0.83 | 1.15 |
| 11-22 23:33 | +20 | DOGE | UP | 0.70 | open |  |
| 11-22 23:33 | +15 | DOGE | UP | 0.71 | open |  |
| 11-22 23:33 | +10 | DOGE | UP | 0.71 | 0.83 | 0.95 |
| 11-22 23:33 | +5 | ETH | UP | 0.64 | 0.69 | 0.18 |
| 11-22 23:32 | +5 | SOL | UP | 0.69 | 0.74 | 0.21 |
| 11-22 23:32 | +10 stop | ETH | UP | 0.62 | 0.74 | 0.89 |
| 11-22 23:32 | +20 | ETH | UP | 0.62 | 0.86 | 2.14 |
| 11-22 23:32 | +15 | ETH | UP | 0.62 | 0.86 | 2.14 |
| 11-22 23:32 | +10 | ETH | UP | 0.62 | 0.74 | 0.89 |
| 11-22 23:32 | +5 | ETH | UP | 0.62 | 0.68 | 0.27 |
| 11-22 23:32 | +10 stop | XRP | UP | 0.68 | open |  |
| 11-22 23:32 | +20 | XRP | UP | 0.68 | open |  |
| 11-22 23:32 | +15 | XRP | UP | 0.69 | open |  |
| 11-22 23:32 | +10 | XRP | UP | 0.69 | open |  |
| 11-22 23:32 | +5 | XRP | UP | 0.70 | open |  |
| 11-22 23:31 | +10 stop | SOL | UP | 0.61 | 0.74 | 0.99 |
| 11-22 23:31 | +20 | SOL | UP | 0.61 | open |  |
| 11-22 23:31 | +15 | SOL | UP | 0.62 | 0.79 | 1.41 |
| 11-22 23:31 | +10 | SOL | UP | 0.62 | 0.74 | 0.89 |
| 11-22 23:31 | +5 | SOL | UP | 0.62 | 0.67 | 0.17 |
| 11-22 23:31 | +5 | HYPE | UP | 0.70 | 0.79 | 0.59 |
| 11-22 23:31 | +10 | HYPE | UP | 0.71 | 0.83 | 0.95 |
| 11-22 23:30 | +10 stop | HYPE | UP | 0.71 | 0.83 | 0.95 |
| 11-22 23:30 | +20 | HYPE | UP | 0.71 | open |  |
| 11-22 23:30 | +15 | HYPE | UP | 0.71 | 0.87 | 1.37 |
| 11-22 23:25 | +10 stop | HYPE | UP | 0.68 | 0.87 | 1.66 |
| 11-22 23:19 | +10 stop | NEAR | UP | 0.69 | 0.82 | 1.04 |
| 11-22 23:19 | +15 | NEAR | UP | 0.69 | 0.86 | 1.46 |
| 11-22 23:19 | +10 | NEAR | UP | 0.69 | 0.82 | 1.04 |
| 11-22 23:19 | +5 | NEAR | UP | 0.69 | 0.74 | 0.21 |
| 11-22 23:17 | +10 stop | HYPE | UP | 0.71 | 0.82 | 0.84 |
| 11-22 23:16 | +10 stop | ZEC | UP | 0.64 | 0.74 | 0.69 |
| 11-22 23:16 | +20 | ZEC | UP | 0.65 | 0.85 | 1.75 |
