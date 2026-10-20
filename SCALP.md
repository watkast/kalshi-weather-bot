# Range-Scalp Bot

*Updated Tue Oct 20 23:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26371 | 22967 | 3404 (32) | 1 | $-7703.80 | -4.6% |
| **+10¢** | 19842 | 15913 | 3929 (47) | 2 | $-6785.69 | -5.4% |
| **+15¢** | 16606 | 12379 | 4227 (71) | 3 | $-6044.37 | -5.8% |
| **+20¢** | 14693 | 10259 | 4434 (90) | 3 | $-5454.70 | -5.9% |
| **+10¢ (15¢ stop)** | 32300 | 32247 | 53 (30) | 0 | $-11799.44 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 23:26 | +10 stop | XRP | UP | 0.68 | 0.79 | 0.82 |
| 10-20 23:26 | +10 | XRP | UP | 0.68 | 0.79 | 0.82 |
| 10-20 23:26 | +5 | XRP | UP | 0.68 | 0.73 | 0.20 |
| 10-20 23:25 | +10 stop | XRP | DOWN | 0.54 | 0.66 | 0.86 |
| 10-20 23:25 | +10 | XRP | DOWN | 0.54 | 0.66 | 0.86 |
| 10-20 23:25 | +5 | XRP | DOWN | 0.54 | 0.66 | 0.86 |
| 10-20 23:21 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-20 23:21 | +5 | XRP | DOWN | 0.64 | 0.70 | 0.28 |
| 10-20 23:19 | +10 stop | SOL | DOWN | 0.57 | 0.67 | 0.66 |
| 10-20 23:19 | +10 stop | XRP | DOWN | 0.58 | 0.68 | 0.66 |
| 10-20 23:19 | +10 stop | NEAR | DOWN | 0.56 | 0.66 | 0.66 |
| 10-20 23:18 | +10 stop | DOGE | DOWN | 0.62 | 0.74 | 0.89 |
| 10-20 23:18 | +5 | DOGE | DOWN | 0.62 | 0.74 | 0.89 |
| 10-20 23:17 | +10 stop | BTC | DOWN | 0.68 | 0.79 | 0.82 |
| 10-20 23:17 | +10 | BTC | DOWN | 0.68 | 0.79 | 0.82 |
| 10-20 23:17 | +5 | BTC | DOWN | 0.68 | 0.77 | 0.61 |
| 10-20 23:17 | +10 stop | NEAR | UP | 0.60 | 0.43 | -2.05 |
| 10-20 23:17 | +5 | DOGE | DOWN | 0.55 | 0.70 | 1.17 |
| 10-20 23:17 | +10 stop | HYPE | DOWN | 0.66 | 0.82 | 1.33 |
| 10-20 23:17 | +20 | HYPE | DOWN | 0.66 | 0.88 | 1.96 |
| 10-20 23:17 | +15 | HYPE | DOWN | 0.66 | 0.82 | 1.33 |
| 10-20 23:17 | +10 | HYPE | DOWN | 0.66 | 0.82 | 1.33 |
| 10-20 23:17 | +5 | HYPE | DOWN | 0.66 | 0.72 | 0.29 |
| 10-20 23:17 | +10 stop | SOL | DOWN | 0.67 | 0.51 | -1.94 |
| 10-20 23:17 | +20 | SOL | DOWN | 0.67 | 0.87 | 1.76 |
| 10-20 23:17 | +15 | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 10-20 23:17 | +10 | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 10-20 23:17 | +5 | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 10-20 23:17 | +10 stop | XRP | DOWN | 0.65 | 0.50 | -1.84 |
| 10-20 23:17 | +20 | XRP | DOWN | 0.65 | open |  |
| 10-20 23:17 | +15 | XRP | DOWN | 0.65 | open |  |
| 10-20 23:17 | +10 | XRP | DOWN | 0.65 | 0.78 | 1.01 |
| 10-20 23:17 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
| 10-20 23:16 | +10 stop | DOGE | UP | 0.53 | 0.29 | -2.73 |
| 10-20 23:16 | +20 | DOGE | UP | 0.53 | open |  |
| 10-20 23:16 | +15 | DOGE | UP | 0.53 | open |  |
| 10-20 23:16 | +10 | DOGE | UP | 0.53 | open |  |
| 10-20 23:16 | +5 | DOGE | UP | 0.53 | 0.58 | 0.14 |
| 10-20 23:16 | +10 stop | NEAR | UP | 0.66 | 0.51 | -1.84 |
| 10-20 23:16 | +20 | NEAR | UP | 0.66 | open |  |
