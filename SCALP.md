# Range-Scalp Bot

*Updated Sat Oct 17 18:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21390 | 18635 | 2755 (29) | 2 | $-6132.33 | -4.6% |
| **+10¢** | 16084 | 12899 | 3185 (41) | 0 | $-5469.63 | -5.4% |
| **+15¢** | 13448 | 10015 | 3433 (61) | 1 | $-4960.74 | -5.9% |
| **+20¢** | 11914 | 8316 | 3598 (80) | 2 | $-4411.31 | -5.9% |
| **+10¢ (15¢ stop)** | 26249 | 26199 | 50 (29) | 0 | $-9993.23 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 18:25 | +10 | NEAR | UP | 0.52 | 0.69 | 1.37 |
| 10-17 18:24 | +10 stop | NEAR | UP | 0.66 | 0.50 | -1.94 |
| 10-17 18:23 | +5 | NEAR | UP | 0.65 | open |  |
| 10-17 18:23 | +10 stop | BNB | DOWN | 0.57 | 0.32 | -2.84 |
| 10-17 18:23 | +10 stop | NEAR | UP | 0.64 | 0.48 | -1.95 |
| 10-17 18:22 | +5 | ETH | UP | 0.70 | 0.79 | 0.63 |
| 10-17 18:22 | +10 stop | NEAR | DOWN | 0.63 | 0.47 | -1.95 |
| 10-17 18:22 | +5 | BTC | UP | 0.70 | 0.81 | 0.84 |
| 10-17 18:22 | +10 stop | XRP | UP | 0.71 | 0.85 | 1.16 |
| 10-17 18:22 | +10 stop | BNB | DOWN | 0.69 | 0.50 | -2.23 |
| 10-17 18:22 | +5 | BNB | DOWN | 0.69 | open |  |
| 10-17 18:22 | +10 stop | NEAR | DOWN | 0.69 | 0.52 | -2.03 |
| 10-17 18:22 | +10 stop | BTC | UP | 0.58 | 0.72 | 1.07 |
| 10-17 18:22 | +15 | BTC | UP | 0.58 | 0.81 | 2.01 |
| 10-17 18:22 | +10 | BTC | UP | 0.58 | 0.72 | 1.07 |
| 10-17 18:22 | +5 | BTC | UP | 0.56 | 0.61 | 0.15 |
| 10-17 18:21 | +10 stop | DOGE | UP | 0.67 | 0.79 | 0.92 |
| 10-17 18:21 | +5 | DOGE | UP | 0.67 | 0.74 | 0.40 |
| 10-17 18:21 | +10 stop | SOL | UP | 0.65 | 0.75 | 0.70 |
| 10-17 18:21 | +15 | SOL | UP | 0.65 | 0.83 | 1.54 |
| 10-17 18:21 | +10 | SOL | UP | 0.64 | 0.75 | 0.79 |
| 10-17 18:21 | +5 | SOL | UP | 0.65 | 0.75 | 0.70 |
| 10-17 18:21 | +5 | ETH | UP | 0.54 | 0.64 | 0.65 |
| 10-17 18:21 | +10 stop | ETH | UP | 0.64 | 0.79 | 1.21 |
| 10-17 18:21 | +10 | ETH | UP | 0.64 | 0.79 | 1.21 |
| 10-17 18:21 | +5 | ETH | UP | 0.64 | 0.69 | 0.18 |
| 10-17 18:20 | +10 stop | NEAR | UP | 0.57 | 0.42 | -1.86 |
| 10-17 18:20 | +10 stop | HYPE | UP | 0.67 | 0.82 | 1.23 |
| 10-17 18:20 | +10 | HYPE | UP | 0.67 | 0.82 | 1.23 |
| 10-17 18:20 | +5 | HYPE | UP | 0.67 | 0.72 | 0.19 |
| 10-17 18:20 | +5 | BNB | DOWN | 0.61 | 0.67 | 0.27 |
| 10-17 18:19 | +10 stop | NEAR | DOWN | 0.42 | 0.53 | 0.74 |
| 10-17 18:19 | +10 stop | BNB | DOWN | 0.57 | 0.67 | 0.66 |
| 10-17 18:19 | +5 | BNB | DOWN | 0.57 | 0.62 | 0.15 |
| 10-17 18:19 | +10 stop | XRP | UP | 0.62 | 0.44 | -2.15 |
| 10-17 18:19 | +10 | XRP | UP | 0.62 | 0.73 | 0.79 |
| 10-17 18:19 | +10 stop | DOGE | UP | 0.62 | 0.73 | 0.79 |
| 10-17 18:19 | +5 | DOGE | UP | 0.62 | 0.70 | 0.48 |
| 10-17 18:19 | +10 stop | SOL | UP | 0.55 | 0.69 | 1.07 |
| 10-17 18:19 | +10 | SOL | UP | 0.55 | 0.69 | 1.07 |
