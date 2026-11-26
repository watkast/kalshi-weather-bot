# Range-Scalp Bot

*Updated Thu Nov 26 06:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72480 | 63275 | 9205 (158) | 1 | $-19210.27 | -4.2% |
| **+10¢** | 54058 | 43309 | 10749 (203) | 1 | $-17781.90 | -5.2% |
| **+15¢** | 45267 | 33688 | 11579 (261) | 1 | $-15860.01 | -5.6% |
| **+20¢** | 40292 | 28097 | 12195 (327) | 1 | $-14259.01 | -5.6% |
| **+10¢ (15¢ stop)** | 88249 | 88040 | 209 (128) | 1 | $-32374.70 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 06:10 | +5 | NEAR | DOWN | 0.58 | open |  |
| 11-26 06:08 | +10 stop | NEAR | DOWN | 0.69 | open |  |
| 11-26 06:08 | +20 | NEAR | DOWN | 0.68 | open |  |
| 11-26 06:08 | +15 | NEAR | DOWN | 0.68 | open |  |
| 11-26 06:08 | +10 | NEAR | DOWN | 0.67 | open |  |
| 11-26 06:08 | +5 | NEAR | DOWN | 0.67 | 0.75 | 0.50 |
| 11-26 06:08 | +5 | SOL | DOWN | 0.58 | 0.63 | 0.15 |
| 11-26 06:08 | +10 stop | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 11-26 06:08 | +20 | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 11-26 06:08 | +15 | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 11-26 06:08 | +10 | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 11-26 06:08 | +5 | SOL | DOWN | 0.59 | 0.66 | 0.37 |
| 11-26 05:57 | +10 stop | XRP | DOWN | 0.64 | 0.78 | 1.08 |
| 11-26 05:57 | +20 | XRP | DOWN | 0.64 | 0.99 | 3.30 |
| 11-26 05:57 | +15 | XRP | DOWN | 0.63 | 0.78 | 1.22 |
| 11-26 05:57 | +10 | XRP | DOWN | 0.61 | 0.78 | 1.40 |
| 11-26 05:57 | +5 | XRP | DOWN | 0.61 | 0.66 | 0.18 |
| 11-26 05:53 | +5 | HYPE | DOWN | 0.70 | 0.82 | 0.92 |
| 11-26 05:52 | +10 stop | ZEC | UP | 0.51 | 0.36 | -1.85 |
| 11-26 05:52 | +10 stop | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-26 05:52 | +20 | DOGE | DOWN | 0.67 | 0.87 | 1.76 |
| 11-26 05:52 | +15 | DOGE | DOWN | 0.67 | 0.84 | 1.44 |
| 11-26 05:52 | +10 | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-26 05:52 | +5 | DOGE | DOWN | 0.63 | 0.70 | 0.38 |
| 11-26 05:52 | +5 | ZEC | UP | 0.56 | 0.62 | 0.20 |
| 11-26 05:52 | +10 | XRP | DOWN | 0.59 | 0.69 | 0.68 |
| 11-26 05:52 | +5 | XRP | DOWN | 0.66 | 0.76 | 0.66 |
| 11-26 05:52 | +10 stop | HYPE | DOWN | 0.55 | 0.68 | 0.94 |
| 11-26 05:52 | +10 | HYPE | DOWN | 0.55 | 0.68 | 1.01 |
| 11-26 05:52 | +5 | HYPE | DOWN | 0.54 | 0.60 | 0.22 |
| 11-26 05:51 | +10 | XRP | DOWN | 0.57 | 0.69 | 0.87 |
| 11-26 05:51 | +5 | XRP | DOWN | 0.57 | 0.64 | 0.35 |
| 11-26 05:51 | +10 stop | ZEC | DOWN | 0.53 | 0.36 | -2.05 |
| 11-26 05:51 | +5 | ZEC | DOWN | 0.52 | 0.58 | 0.24 |
| 11-26 05:51 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 11-26 05:50 | +10 stop | XRP | UP | 0.47 | 0.59 | 0.85 |
| 11-26 05:48 | +10 stop | ZEC | DOWN | 0.61 | 0.74 | 0.99 |
| 11-26 05:47 | +10 stop | XRP | UP | 0.60 | 0.71 | 0.78 |
| 11-26 05:47 | +10 stop | ZEC | DOWN | 0.69 | 0.54 | -1.83 |
| 11-26 05:47 | +20 | ZEC | DOWN | 0.69 | 0.94 | 2.36 |
