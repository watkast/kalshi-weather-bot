# Range-Scalp Bot

*Updated Fri Nov 06 04:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49176 | 42853 | 6323 (75) | 1 | $-13929.80 | -4.5% |
| **+10¢** | 36720 | 29370 | 7350 (101) | 1 | $-12775.77 | -5.5% |
| **+15¢** | 30755 | 22842 | 7913 (130) | 1 | $-11640.79 | -6.0% |
| **+20¢** | 27338 | 19044 | 8294 (170) | 1 | $-10288.94 | -6.0% |
| **+10¢ (15¢ stop)** | 59968 | 59873 | 95 (57) | 0 | $-22197.24 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 04:21 | +10 stop | BNB | DOWN | 0.66 | 0.47 | -2.19 |
| 11-06 04:18 | +10 stop | BNB | DOWN | 0.67 | 0.48 | -2.24 |
| 11-06 04:18 | +10 | BNB | DOWN | 0.67 | open |  |
| 11-06 04:18 | +5 | BNB | DOWN | 0.67 | open |  |
| 11-06 04:17 | +5 | BNB | DOWN | 0.62 | 0.67 | 0.17 |
| 11-06 04:17 | +10 stop | SOL | DOWN | 0.66 | 0.79 | 1.02 |
| 11-06 04:17 | +10 | SOL | DOWN | 0.66 | 0.79 | 1.02 |
| 11-06 04:17 | +5 | SOL | DOWN | 0.66 | 0.72 | 0.29 |
| 11-06 04:17 | +5 | HYPE | DOWN | 0.60 | 0.67 | 0.37 |
| 11-06 04:17 | +10 stop | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-06 04:17 | +20 | NEAR | DOWN | 0.68 | 0.93 | 2.28 |
| 11-06 04:17 | +15 | NEAR | DOWN | 0.68 | 0.84 | 1.34 |
| 11-06 04:17 | +10 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-06 04:17 | +5 | NEAR | DOWN | 0.68 | 0.73 | 0.20 |
| 11-06 04:16 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-06 04:16 | +20 | BTC | DOWN | 0.67 | 0.88 | 1.86 |
| 11-06 04:16 | +15 | BTC | DOWN | 0.67 | 0.88 | 1.86 |
| 11-06 04:16 | +10 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-06 04:16 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 11-06 04:16 | +10 stop | SOL | DOWN | 0.53 | 0.64 | 0.75 |
| 11-06 04:16 | +20 | SOL | DOWN | 0.53 | 0.79 | 2.30 |
| 11-06 04:16 | +15 | SOL | DOWN | 0.53 | 0.72 | 1.57 |
| 11-06 04:16 | +10 | SOL | DOWN | 0.53 | 0.64 | 0.75 |
| 11-06 04:16 | +5 | SOL | DOWN | 0.53 | 0.64 | 0.75 |
| 11-06 04:16 | +10 stop | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 11-06 04:16 | +20 | ETH | DOWN | 0.62 | 0.83 | 1.83 |
| 11-06 04:16 | +15 | ETH | DOWN | 0.62 | 0.78 | 1.30 |
| 11-06 04:16 | +10 | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 11-06 04:16 | +5 | ETH | DOWN | 0.62 | 0.67 | 0.17 |
| 11-06 04:16 | +10 stop | XRP | DOWN | 0.60 | 0.70 | 0.68 |
| 11-06 04:16 | +20 | XRP | DOWN | 0.60 | 0.80 | 1.71 |
| 11-06 04:16 | +15 | XRP | DOWN | 0.60 | 0.80 | 1.71 |
| 11-06 04:16 | +10 | XRP | DOWN | 0.60 | 0.70 | 0.68 |
| 11-06 04:16 | +5 | XRP | DOWN | 0.60 | 0.67 | 0.37 |
| 11-06 04:16 | +10 stop | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-06 04:16 | +20 | ZEC | DOWN | 0.61 | 0.87 | 2.35 |
| 11-06 04:16 | +15 | ZEC | DOWN | 0.61 | 0.79 | 1.51 |
| 11-06 04:16 | +10 | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-06 04:16 | +5 | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-06 04:16 | +10 stop | HYPE | DOWN | 0.50 | 0.67 | 1.36 |
