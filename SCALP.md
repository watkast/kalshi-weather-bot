# Range-Scalp Bot

*Updated Mon Oct 05 01:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3070 | 2631 | 439 (3) | 4 | $-1141.33 | -5.9% |
| **+10¢** | 2383 | 1886 | 497 (4) | 5 | $-997.08 | -6.6% |
| **+15¢** | 2007 | 1483 | 524 (5) | 7 | $-868.40 | -6.9% |
| **+20¢** | 1792 | 1246 | 546 (10) | 4 | $-733.55 | -6.5% |
| **+10¢ (15¢ stop)** | 3845 | 3844 | 1 (1) | 0 | $-1543.53 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 01:22 | +10 stop | ETH | UP | 0.63 | 0.47 | -1.95 |
| 10-05 01:22 | +10 stop | NEAR | DOWN | 0.51 | 0.64 | 0.95 |
| 10-05 01:22 | +5 | BTC | UP | 0.68 | 0.73 | 0.20 |
| 10-05 01:21 | +10 stop | HYPE | UP | 0.57 | 0.70 | 0.97 |
| 10-05 01:20 | +10 stop | BTC | UP | 0.67 | 0.84 | 1.44 |
| 10-05 01:20 | +15 | BTC | UP | 0.70 | open |  |
| 10-05 01:20 | +10 | BTC | UP | 0.70 | 0.84 | 1.15 |
| 10-05 01:20 | +5 | BTC | UP | 0.70 | 0.75 | 0.21 |
| 10-05 01:20 | +10 stop | ZEC | UP | 0.64 | 0.80 | 1.31 |
| 10-05 01:20 | +10 stop | NEAR | UP | 0.58 | 0.43 | -1.86 |
| 10-05 01:20 | +15 | NEAR | UP | 0.58 | open |  |
| 10-05 01:20 | +10 | NEAR | UP | 0.58 | open |  |
| 10-05 01:20 | +5 | NEAR | UP | 0.58 | open |  |
| 10-05 01:19 | +10 stop | SOL | UP | 0.71 | 0.83 | 0.95 |
| 10-05 01:19 | +15 | SOL | UP | 0.71 | open |  |
| 10-05 01:19 | +10 | SOL | UP | 0.71 | 0.83 | 0.95 |
| 10-05 01:19 | +5 | SOL | UP | 0.71 | 0.78 | 0.42 |
| 10-05 01:19 | +10 | HYPE | DOWN | 0.55 | open |  |
| 10-05 01:18 | +10 stop | ZEC | UP | 0.58 | 0.70 | 0.87 |
| 10-05 01:18 | +10 stop | ETH | UP | 0.70 | 0.47 | -2.63 |
| 10-05 01:18 | +10 stop | NEAR | DOWN | 0.54 | 0.72 | 1.47 |
| 10-05 01:18 | +20 | NEAR | DOWN | 0.54 | 0.75 | 1.78 |
| 10-05 01:18 | +15 | NEAR | DOWN | 0.54 | 0.72 | 1.47 |
| 10-05 01:18 | +10 | NEAR | DOWN | 0.54 | 0.72 | 1.47 |
| 10-05 01:18 | +5 | NEAR | DOWN | 0.54 | 0.72 | 1.47 |
| 10-05 01:17 | +10 stop | HYPE | DOWN | 0.50 | 0.34 | -1.98 |
| 10-05 01:17 | +10 | HYPE | DOWN | 0.50 | 0.60 | 0.65 |
| 10-05 01:17 | +5 | HYPE | DOWN | 0.64 | open |  |
| 10-05 01:17 | +5 | BNB | UP | 0.69 | 0.78 | 0.62 |
| 10-05 01:17 | +10 stop | DOGE | UP | 0.67 | 0.79 | 0.92 |
| 10-05 01:17 | +20 | DOGE | UP | 0.67 | 0.89 | 1.97 |
| 10-05 01:17 | +15 | DOGE | UP | 0.67 | 0.82 | 1.23 |
| 10-05 01:17 | +10 | DOGE | UP | 0.67 | 0.79 | 0.92 |
| 10-05 01:17 | +5 | DOGE | UP | 0.67 | 0.79 | 0.92 |
| 10-05 01:16 | +10 stop | XRP | UP | 0.66 | 0.77 | 0.79 |
| 10-05 01:16 | +20 | XRP | UP | 0.66 | 0.89 | 2.05 |
| 10-05 01:16 | +15 | XRP | UP | 0.66 | 0.84 | 1.52 |
| 10-05 01:16 | +10 | XRP | UP | 0.66 | 0.77 | 0.79 |
| 10-05 01:16 | +5 | XRP | UP | 0.66 | 0.72 | 0.27 |
| 10-05 01:16 | +10 stop | ZEC | DOWN | 0.66 | 0.51 | -1.84 |
