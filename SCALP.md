# Range-Scalp Bot

*Updated Mon Oct 05 06:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3420 | 2934 | 486 (3) | 3 | $-1251.75 | -5.8% |
| **+10¢** | 2645 | 2091 | 554 (4) | 4 | $-1124.95 | -6.8% |
| **+15¢** | 2223 | 1635 | 588 (6) | 5 | $-1024.71 | -7.3% |
| **+20¢** | 1980 | 1366 | 614 (11) | 6 | $-902.61 | -7.3% |
| **+10¢ (15¢ stop)** | 4240 | 4239 | 1 (1) | 1 | $-1630.38 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 06:23 | +15 | SOL | UP | 0.66 | open |  |
| 10-05 06:23 | +5 | ZEC | UP | 0.63 | 0.75 | 0.89 |
| 10-05 06:23 | +10 stop | ETH | UP | 0.50 | 0.60 | 0.65 |
| 10-05 06:23 | +20 | ETH | UP | 0.53 | open |  |
| 10-05 06:23 | +15 | ETH | UP | 0.53 | open |  |
| 10-05 06:23 | +10 | ETH | UP | 0.53 | open |  |
| 10-05 06:23 | +5 | ETH | UP | 0.53 | 0.60 | 0.35 |
| 10-05 06:22 | +10 stop | SOL | UP | 0.69 | open |  |
| 10-05 06:22 | +10 | SOL | UP | 0.69 | open |  |
| 10-05 06:22 | +5 | SOL | UP | 0.70 | open |  |
| 10-05 06:22 | +5 | BTC | UP | 0.62 | 0.70 | 0.48 |
| 10-05 06:22 | +10 stop | ZEC | UP | 0.57 | 0.75 | 1.48 |
| 10-05 06:22 | +15 | ZEC | UP | 0.57 | 0.75 | 1.48 |
| 10-05 06:22 | +10 | ZEC | UP | 0.57 | 0.75 | 1.48 |
| 10-05 06:22 | +5 | ZEC | UP | 0.57 | 0.66 | 0.56 |
| 10-05 06:22 | +10 stop | DOGE | UP | 0.50 | 0.70 | 1.67 |
| 10-05 06:22 | +20 | DOGE | UP | 0.50 | 0.70 | 1.67 |
| 10-05 06:22 | +15 | DOGE | UP | 0.50 | 0.70 | 1.67 |
| 10-05 06:22 | +10 | DOGE | UP | 0.50 | 0.70 | 1.67 |
| 10-05 06:22 | +5 | DOGE | UP | 0.50 | 0.70 | 1.67 |
| 10-05 06:22 | +10 stop | BTC | UP | 0.54 | 0.70 | 1.27 |
| 10-05 06:22 | +20 | BTC | UP | 0.54 | open |  |
| 10-05 06:22 | +15 | BTC | UP | 0.54 | 0.70 | 1.27 |
| 10-05 06:22 | +10 | BTC | UP | 0.54 | 0.70 | 1.27 |
| 10-05 06:22 | +5 | BTC | UP | 0.54 | 0.60 | 0.25 |
| 10-05 06:22 | +10 stop | SOL | UP | 0.51 | 0.64 | 0.95 |
| 10-05 06:22 | +20 | SOL | UP | 0.51 | 0.73 | 1.88 |
| 10-05 06:22 | +15 | SOL | UP | 0.51 | 0.68 | 1.36 |
| 10-05 06:22 | +10 | SOL | UP | 0.51 | 0.64 | 0.95 |
| 10-05 06:22 | +5 | SOL | UP | 0.51 | 0.64 | 0.95 |
| 10-05 06:21 | +5 | XRP | DOWN | 0.71 | 0.79 | 0.53 |
| 10-05 06:21 | +10 stop | BNB | UP | 0.54 | 0.39 | -1.85 |
| 10-05 06:21 | +10 | BNB | UP | 0.54 | open |  |
| 10-05 06:21 | +5 | BNB | UP | 0.54 | 0.62 | 0.45 |
| 10-05 06:20 | +10 stop | XRP | DOWN | 0.60 | 0.70 | 0.68 |
| 10-05 06:20 | +10 | XRP | DOWN | 0.60 | 0.70 | 0.68 |
| 10-05 06:20 | +5 | XRP | DOWN | 0.60 | 0.67 | 0.37 |
| 10-05 06:20 | +10 stop | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-05 06:19 | +10 stop | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 10-05 06:19 | +15 | NEAR | DOWN | 0.71 | 0.87 | 1.37 |
