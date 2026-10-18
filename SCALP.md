# Range-Scalp Bot

*Updated Sun Oct 18 03:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21989 | 19153 | 2836 (29) | 0 | $-6322.33 | -4.6% |
| **+10¢** | 16547 | 13270 | 3277 (41) | 0 | $-5623.31 | -5.4% |
| **+15¢** | 13856 | 10322 | 3534 (61) | 0 | $-5095.67 | -5.9% |
| **+20¢** | 12261 | 8558 | 3703 (80) | 0 | $-4545.50 | -5.9% |
| **+10¢ (15¢ stop)** | 27052 | 27002 | 50 (29) | 0 | $-10337.77 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 03:16 | +10 stop | BNB | DOWN | 0.67 | 0.82 | 1.19 |
| 10-18 03:16 | +20 | BNB | DOWN | 0.67 | 0.91 | 2.10 |
| 10-18 03:16 | +15 | BNB | DOWN | 0.67 | 0.84 | 1.40 |
| 10-18 03:16 | +10 | BNB | DOWN | 0.67 | 0.82 | 1.19 |
| 10-18 03:16 | +5 | BNB | DOWN | 0.67 | 0.75 | 0.46 |
| 10-18 03:15 | +10 stop | XRP | DOWN | 0.69 | 0.80 | 0.83 |
| 10-18 03:15 | +20 | XRP | DOWN | 0.69 | 0.89 | 1.78 |
| 10-18 03:15 | +15 | XRP | DOWN | 0.69 | 0.88 | 1.67 |
| 10-18 03:15 | +10 | XRP | DOWN | 0.69 | 0.80 | 0.83 |
| 10-18 03:15 | +5 | XRP | DOWN | 0.69 | 0.78 | 0.62 |
| 10-18 03:15 | +10 stop | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 10-18 03:15 | +20 | DOGE | DOWN | 0.66 | 0.91 | 2.30 |
| 10-18 03:15 | +15 | DOGE | DOWN | 0.66 | 0.83 | 1.44 |
| 10-18 03:15 | +10 | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 10-18 03:15 | +5 | DOGE | DOWN | 0.66 | 0.74 | 0.50 |
| 10-18 03:15 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-18 03:15 | +20 | BTC | DOWN | 0.66 | 0.86 | 1.75 |
| 10-18 03:15 | +15 | BTC | DOWN | 0.66 | 0.83 | 1.44 |
| 10-18 03:15 | +10 | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-18 03:15 | +5 | BTC | DOWN | 0.66 | 0.74 | 0.50 |
| 10-18 03:15 | +10 stop | HYPE | DOWN | 0.62 | 0.73 | 0.75 |
| 10-18 03:15 | +20 | HYPE | DOWN | 0.62 | 0.84 | 1.89 |
| 10-18 03:15 | +15 | HYPE | DOWN | 0.62 | 0.79 | 1.37 |
| 10-18 03:15 | +10 | HYPE | DOWN | 0.62 | 0.73 | 0.75 |
| 10-18 03:15 | +5 | HYPE | DOWN | 0.62 | 0.69 | 0.34 |
| 10-18 03:08 | +10 stop | SOL | UP | 0.70 | 0.82 | 0.94 |
| 10-18 03:08 | +15 | SOL | UP | 0.70 | 0.88 | 1.57 |
| 10-18 03:08 | +10 | SOL | UP | 0.70 | 0.82 | 0.94 |
| 10-18 03:05 | +10 stop | BTC | UP | 0.70 | 0.82 | 0.94 |
| 10-18 03:05 | +10 stop | SOL | UP | 0.68 | 0.80 | 0.92 |
| 10-18 03:05 | +10 stop | ETH | UP | 0.70 | 0.80 | 0.73 |
| 10-18 03:05 | +10 stop | NEAR | UP | 0.68 | 0.81 | 1.03 |
| 10-18 03:04 | +10 stop | DOGE | UP | 0.60 | 0.79 | 1.61 |
| 10-18 03:04 | +10 stop | HYPE | UP | 0.54 | 0.72 | 1.47 |
| 10-18 03:03 | +5 | ZEC | DOWN | 0.57 | yes | -5.87 |
| 10-18 03:03 | +10 stop | ETH | DOWN | 0.63 | 0.45 | -2.15 |
| 10-18 03:03 | +10 stop | BTC | DOWN | 0.57 | 0.42 | -1.86 |
| 10-18 03:03 | +5 | ZEC | DOWN | 0.54 | 0.60 | 0.25 |
| 10-18 03:03 | +10 stop | NEAR | DOWN | 0.57 | 0.34 | -2.64 |
| 10-18 03:03 | +20 | NEAR | DOWN | 0.57 | yes | -5.88 |
