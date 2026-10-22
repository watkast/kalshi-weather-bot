# Range-Scalp Bot

*Updated Thu Oct 22 03:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28196 | 24573 | 3623 (39) | 3 | $-8074.72 | -4.5% |
| **+10¢** | 21176 | 16987 | 4189 (55) | 4 | $-7140.46 | -5.4% |
| **+15¢** | 17733 | 13226 | 4507 (78) | 6 | $-6366.64 | -5.7% |
| **+20¢** | 15691 | 10966 | 4725 (98) | 6 | $-5728.20 | -5.8% |
| **+10¢ (15¢ stop)** | 34608 | 34549 | 59 (32) | 1 | $-12950.11 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 03:23 | +10 stop | XRP | DOWN | 0.67 | open |  |
| 10-22 03:23 | +10 | XRP | DOWN | 0.67 | open |  |
| 10-22 03:23 | +5 | XRP | DOWN | 0.67 | 0.73 | 0.30 |
| 10-22 03:23 | +10 stop | HYPE | DOWN | 0.63 | 0.75 | 0.89 |
| 10-22 03:22 | +15 | BTC | UP | 0.48 | open |  |
| 10-22 03:22 | +10 stop | SOL | UP | 0.49 | 0.29 | -2.33 |
| 10-22 03:22 | +15 | SOL | UP | 0.49 | open |  |
| 10-22 03:22 | +10 | SOL | UP | 0.50 | open |  |
| 10-22 03:22 | +5 | SOL | UP | 0.50 | 0.57 | 0.34 |
| 10-22 03:22 | +10 stop | ETH | UP | 0.52 | 0.28 | -2.73 |
| 10-22 03:22 | +10 stop | BTC | UP | 0.70 | 0.54 | -1.93 |
| 10-22 03:22 | +10 stop | ZEC | DOWN | 0.59 | 0.76 | 1.40 |
| 10-22 03:22 | +10 | ZEC | DOWN | 0.60 | 0.76 | 1.33 |
| 10-22 03:21 | +10 stop | BNB | UP | 0.65 | 0.50 | -1.84 |
| 10-22 03:21 | +10 stop | DOGE | UP | 0.63 | 0.46 | -2.05 |
| 10-22 03:21 | +10 stop | NEAR | DOWN | 0.69 | 0.79 | 0.73 |
| 10-22 03:21 | +10 | NEAR | DOWN | 0.69 | 0.79 | 0.73 |
| 10-22 03:21 | +5 | NEAR | DOWN | 0.69 | 0.76 | 0.42 |
| 10-22 03:21 | +10 stop | SOL | UP | 0.59 | 0.74 | 1.16 |
| 10-22 03:20 | +5 | HYPE | DOWN | 0.64 | 0.72 | 0.48 |
| 10-22 03:20 | +15 | BNB | DOWN | 0.63 | 0.79 | 1.31 |
| 10-22 03:20 | +15 | DOGE | DOWN | 0.68 | 0.85 | 1.45 |
| 10-22 03:20 | +10 | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-22 03:20 | +10 stop | XRP | DOWN | 0.52 | 0.32 | -2.34 |
| 10-22 03:19 | +10 stop | ETH | DOWN | 0.69 | 0.37 | -3.52 |
| 10-22 03:19 | +10 stop | BNB | DOWN | 0.68 | 0.49 | -2.28 |
| 10-22 03:19 | +10 | BNB | DOWN | 0.70 | open |  |
| 10-22 03:19 | +5 | BNB | DOWN | 0.70 | 0.79 | 0.63 |
| 10-22 03:19 | +10 stop | SOL | DOWN | 0.64 | 0.43 | -2.45 |
| 10-22 03:19 | +5 | DOGE | DOWN | 0.69 | 0.76 | 0.42 |
| 10-22 03:19 | +10 stop | BTC | DOWN | 0.66 | 0.49 | -2.04 |
| 10-22 03:19 | +10 | BTC | DOWN | 0.66 | 0.78 | 0.91 |
| 10-22 03:19 | +10 stop | DOGE | DOWN | 0.70 | 0.47 | -2.63 |
| 10-22 03:18 | +10 stop | NEAR | DOWN | 0.61 | 0.73 | 0.89 |
| 10-22 03:18 | +20 | NEAR | DOWN | 0.61 | 0.81 | 1.72 |
| 10-22 03:18 | +15 | NEAR | DOWN | 0.63 | 0.79 | 1.31 |
| 10-22 03:18 | +10 | NEAR | DOWN | 0.63 | 0.73 | 0.69 |
| 10-22 03:18 | +5 | NEAR | DOWN | 0.63 | 0.73 | 0.69 |
| 10-22 03:18 | +5 | SOL | UP | 0.60 | 0.67 | 0.37 |
| 10-22 03:18 | +10 stop | XRP | UP | 0.61 | 0.45 | -1.95 |
