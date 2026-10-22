# Range-Scalp Bot

*Updated Thu Oct 22 16:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29004 | 25259 | 3745 (39) | 1 | $-8454.70 | -4.6% |
| **+10¢** | 21760 | 17428 | 4332 (55) | 1 | $-7558.12 | -5.5% |
| **+15¢** | 18212 | 13556 | 4656 (78) | 3 | $-6765.18 | -5.9% |
| **+20¢** | 16117 | 11236 | 4881 (100) | 4 | $-6106.85 | -6.0% |
| **+10¢ (15¢ stop)** | 35593 | 35534 | 59 (32) | 0 | $-13391.58 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 16:40 | +10 stop | XRP | DOWN | 0.67 | 0.88 | 1.90 |
| 10-22 16:40 | +10 stop | DOGE | DOWN | 0.67 | 0.80 | 1.02 |
| 10-22 16:40 | +5 | HYPE | DOWN | 0.69 | 0.82 | 1.04 |
| 10-22 16:38 | +10 stop | DOGE | UP | 0.59 | 0.43 | -1.93 |
| 10-22 16:38 | +10 stop | XRP | UP | 0.61 | 0.43 | -2.15 |
| 10-22 16:38 | +10 stop | ZEC | DOWN | 0.69 | 0.79 | 0.74 |
| 10-22 16:38 | +20 | ZEC | DOWN | 0.69 | 0.91 | 2.03 |
| 10-22 16:38 | +15 | ZEC | DOWN | 0.68 | 0.83 | 1.29 |
| 10-22 16:38 | +10 | ZEC | DOWN | 0.68 | 0.79 | 0.87 |
| 10-22 16:38 | +5 | ZEC | DOWN | 0.68 | 0.79 | 0.87 |
| 10-22 16:38 | +10 stop | SOL | UP | 0.68 | 0.50 | -2.10 |
| 10-22 16:37 | +10 stop | DOGE | DOWN | 0.48 | 0.32 | -1.94 |
| 10-22 16:37 | +10 stop | XRP | UP | 0.53 | 0.63 | 0.65 |
| 10-22 16:37 | +10 stop | DOGE | UP | 0.65 | 0.45 | -2.34 |
| 10-22 16:37 | +10 stop | SOL | UP | 0.66 | 0.47 | -2.24 |
| 10-22 16:35 | +10 stop | HYPE | DOWN | 0.63 | 0.82 | 1.62 |
| 10-22 16:35 | +10 | HYPE | DOWN | 0.63 | 0.82 | 1.62 |
| 10-22 16:35 | +5 | HYPE | DOWN | 0.62 | 0.69 | 0.38 |
| 10-22 16:35 | +5 | SOL | DOWN | 0.60 | 0.78 | 1.50 |
| 10-22 16:35 | +10 stop | XRP | DOWN | 0.62 | 0.39 | -2.64 |
| 10-22 16:35 | +10 | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-22 16:35 | +5 | XRP | DOWN | 0.63 | 0.69 | 0.28 |
| 10-22 16:35 | +10 stop | NEAR | DOWN | 0.48 | 0.29 | -2.23 |
| 10-22 16:34 | +10 stop | SOL | DOWN | 0.66 | 0.49 | -2.04 |
| 10-22 16:34 | +15 | SOL | DOWN | 0.65 | open |  |
| 10-22 16:34 | +10 | SOL | DOWN | 0.65 | 0.78 | 1.01 |
| 10-22 16:34 | +5 | SOL | DOWN | 0.65 | 0.71 | 0.29 |
| 10-22 16:33 | +5 | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 10-22 16:33 | +5 | DOGE | DOWN | 0.60 | 0.67 | 0.37 |
| 10-22 16:33 | +10 stop | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 10-22 16:33 | +10 | SOL | DOWN | 0.69 | 0.80 | 0.83 |
| 10-22 16:33 | +5 | SOL | DOWN | 0.69 | 0.75 | 0.31 |
| 10-22 16:32 | +5 | NEAR | DOWN | 0.70 | open |  |
| 10-22 16:31 | +10 stop | DOGE | DOWN | 0.70 | 0.55 | -1.83 |
| 10-22 16:31 | +20 | DOGE | DOWN | 0.70 | open |  |
| 10-22 16:31 | +15 | DOGE | DOWN | 0.70 | open |  |
| 10-22 16:31 | +10 | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 10-22 16:31 | +5 | DOGE | DOWN | 0.70 | 0.77 | 0.42 |
| 10-22 16:31 | +10 stop | HYPE | DOWN | 0.68 | 0.80 | 0.88 |
| 10-22 16:31 | +20 | HYPE | DOWN | 0.68 | 0.94 | 2.36 |
