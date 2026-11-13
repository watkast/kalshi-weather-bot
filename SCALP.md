# Range-Scalp Bot

*Updated Fri Nov 13 21:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58680 | 51204 | 7476 (105) | 0 | $-15815.34 | -4.3% |
| **+10¢** | 43833 | 35089 | 8744 (139) | 1 | $-14788.40 | -5.4% |
| **+15¢** | 36736 | 27317 | 9419 (174) | 2 | $-13370.98 | -5.8% |
| **+20¢** | 32727 | 22839 | 9888 (225) | 3 | $-11753.87 | -5.7% |
| **+10¢ (15¢ stop)** | 71448 | 71314 | 134 (82) | 0 | $-26294.60 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 21:22 | +5 | HYPE | DOWN | 0.69 | 0.82 | 0.99 |
| 11-13 21:21 | +10 stop | HYPE | DOWN | 0.57 | 0.82 | 2.21 |
| 11-13 21:21 | +5 | HYPE | DOWN | 0.57 | 0.65 | 0.46 |
| 11-13 21:20 | +10 stop | NEAR | DOWN | 0.57 | 0.70 | 0.97 |
| 11-13 21:20 | +10 stop | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 11-13 21:20 | +20 | XRP | DOWN | 0.63 | 0.83 | 1.73 |
| 11-13 21:20 | +15 | XRP | DOWN | 0.63 | 0.81 | 1.52 |
| 11-13 21:20 | +10 | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 11-13 21:20 | +5 | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 11-13 21:20 | +10 stop | HYPE | DOWN | 0.54 | 0.64 | 0.65 |
| 11-13 21:20 | +5 | HYPE | DOWN | 0.54 | 0.64 | 0.70 |
| 11-13 21:19 | +5 | XRP | DOWN | 0.66 | 0.78 | 0.92 |
| 11-13 21:18 | +20 | ZEC | UP | 0.61 | open |  |
| 11-13 21:18 | +10 stop | NEAR | UP | 0.52 | 0.26 | -2.92 |
| 11-13 21:18 | +10 stop | ZEC | UP | 0.61 | 0.35 | -2.93 |
| 11-13 21:17 | +10 stop | SOL | DOWN | 0.58 | 0.70 | 0.87 |
| 11-13 21:17 | +20 | SOL | DOWN | 0.58 | 0.83 | 2.22 |
| 11-13 21:17 | +15 | SOL | DOWN | 0.58 | 0.74 | 1.28 |
| 11-13 21:17 | +10 | SOL | DOWN | 0.58 | 0.70 | 0.87 |
| 11-13 21:17 | +5 | SOL | DOWN | 0.58 | 0.70 | 0.87 |
| 11-13 21:17 | +5 | ETH | DOWN | 0.65 | 0.70 | 0.19 |
| 11-13 21:17 | +10 stop | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 11-13 21:17 | +5 | HYPE | DOWN | 0.60 | 0.69 | 0.58 |
| 11-13 21:17 | +10 stop | XRP | DOWN | 0.54 | 0.64 | 0.65 |
| 11-13 21:17 | +20 | XRP | DOWN | 0.54 | 0.78 | 2.09 |
| 11-13 21:17 | +15 | XRP | DOWN | 0.55 | 0.78 | 1.99 |
| 11-13 21:17 | +10 | XRP | DOWN | 0.54 | 0.64 | 0.65 |
| 11-13 21:17 | +5 | XRP | DOWN | 0.55 | 0.63 | 0.45 |
| 11-13 21:16 | +10 stop | ZEC | DOWN | 0.71 | 0.56 | -1.83 |
| 11-13 21:16 | +15 | ZEC | DOWN | 0.71 | 0.87 | 1.37 |
| 11-13 21:16 | +10 | ZEC | DOWN | 0.71 | 0.87 | 1.37 |
| 11-13 21:16 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.22 |
| 11-13 21:16 | +10 stop | NEAR | DOWN | 0.67 | 0.50 | -2.04 |
| 11-13 21:16 | +20 | NEAR | DOWN | 0.67 | open |  |
| 11-13 21:16 | +15 | NEAR | DOWN | 0.67 | open |  |
| 11-13 21:16 | +10 | NEAR | DOWN | 0.69 | 0.79 | 0.73 |
| 11-13 21:16 | +5 | NEAR | DOWN | 0.69 | 0.75 | 0.31 |
| 11-13 21:16 | +10 stop | DOGE | DOWN | 0.69 | 0.88 | 1.67 |
| 11-13 21:16 | +20 | DOGE | DOWN | 0.69 | 0.94 | 2.28 |
| 11-13 21:16 | +15 | DOGE | DOWN | 0.69 | 0.88 | 1.67 |
