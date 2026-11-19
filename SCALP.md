# Range-Scalp Bot

*Updated Thu Nov 19 18:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65334 | 57041 | 8293 (124) | 1 | $-17422.73 | -4.2% |
| **+10¢** | 48791 | 39084 | 9707 (165) | 1 | $-16245.61 | -5.3% |
| **+15¢** | 40912 | 30442 | 10470 (211) | 1 | $-14621.56 | -5.7% |
| **+20¢** | 36432 | 25431 | 11001 (266) | 1 | $-12944.77 | -5.7% |
| **+10¢ (15¢ stop)** | 79531 | 79367 | 164 (98) | 0 | $-29263.93 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 18:20 | +10 stop | NEAR | UP | 0.69 | 0.81 | 0.89 |
| 11-19 18:20 | +10 stop | ZEC | UP | 0.56 | 0.74 | 1.49 |
| 11-19 18:19 | +10 stop | BNB | UP | 0.68 | 0.79 | 0.82 |
| 11-19 18:18 | +10 stop | ETH | UP | 0.63 | 0.74 | 0.79 |
| 11-19 18:18 | +10 stop | NEAR | DOWN | 0.51 | 0.61 | 0.65 |
| 11-19 18:18 | +10 stop | XRP | DOWN | 0.46 | 0.31 | -1.83 |
| 11-19 18:17 | +10 stop | DOGE | DOWN | 0.60 | 0.44 | -1.95 |
| 11-19 18:17 | +10 stop | BNB | UP | 0.53 | 0.68 | 1.16 |
| 11-19 18:17 | +10 stop | ZEC | DOWN | 0.66 | 0.48 | -2.14 |
| 11-19 18:17 | +20 | ZEC | DOWN | 0.66 | open |  |
| 11-19 18:17 | +15 | ZEC | DOWN | 0.66 | open |  |
| 11-19 18:17 | +10 | ZEC | DOWN | 0.66 | open |  |
| 11-19 18:17 | +5 | ZEC | DOWN | 0.66 | open |  |
| 11-19 18:17 | +10 stop | HYPE | UP | 0.58 | 0.71 | 0.97 |
| 11-19 18:17 | +20 | HYPE | UP | 0.59 | 0.79 | 1.71 |
| 11-19 18:17 | +15 | HYPE | UP | 0.58 | 0.73 | 1.18 |
| 11-19 18:17 | +10 | HYPE | UP | 0.58 | 0.71 | 0.97 |
| 11-19 18:17 | +5 | HYPE | UP | 0.59 | 0.71 | 0.88 |
| 11-19 18:16 | +10 stop | NEAR | UP | 0.52 | 0.36 | -1.99 |
| 11-19 18:16 | +20 | NEAR | UP | 0.52 | 0.81 | 2.57 |
| 11-19 18:16 | +15 | NEAR | UP | 0.52 | 0.69 | 1.33 |
| 11-19 18:16 | +10 | NEAR | UP | 0.52 | 0.69 | 1.33 |
| 11-19 18:16 | +5 | NEAR | UP | 0.52 | 0.62 | 0.61 |
| 11-19 18:16 | +5 | XRP | UP | 0.62 | 0.68 | 0.27 |
| 11-19 18:16 | +10 stop | DOGE | UP | 0.59 | 0.44 | -1.85 |
| 11-19 18:16 | +20 | DOGE | UP | 0.59 | 0.84 | 2.23 |
| 11-19 18:16 | +15 | DOGE | UP | 0.59 | 0.78 | 1.60 |
| 11-19 18:16 | +10 | DOGE | UP | 0.60 | 0.78 | 1.50 |
| 11-19 18:16 | +5 | DOGE | UP | 0.62 | 0.78 | 1.34 |
| 11-19 18:16 | +5 | ETH | UP | 0.63 | 0.68 | 0.17 |
| 11-19 18:16 | +15 | BNB | UP | 0.65 | 0.88 | 2.06 |
| 11-19 18:15 | +10 stop | BTC | UP | 0.68 | 0.80 | 0.92 |
| 11-19 18:15 | +20 | BTC | UP | 0.68 | 0.89 | 1.87 |
| 11-19 18:15 | +15 | BTC | UP | 0.68 | 0.89 | 1.87 |
| 11-19 18:15 | +10 | BTC | UP | 0.70 | 0.80 | 0.73 |
| 11-19 18:15 | +5 | BTC | UP | 0.70 | 0.80 | 0.73 |
| 11-19 18:15 | +10 stop | ETH | UP | 0.66 | 0.51 | -1.84 |
| 11-19 18:15 | +20 | ETH | UP | 0.68 | 0.91 | 2.04 |
| 11-19 18:15 | +15 | ETH | UP | 0.69 | 0.91 | 1.95 |
| 11-19 18:15 | +10 | ETH | UP | 0.71 | 0.82 | 0.84 |
