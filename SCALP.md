# Range-Scalp Bot

*Updated Sat Oct 03 16:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 982 | 860 | 122 (2) | 2 | $-250.21 | -4.0% |
| **+10¢** | 746 | 612 | 134 (4) | 2 | $-127.57 | -2.7% |
| **+15¢** | 631 | 487 | 144 (5) | 2 | $-92.31 | -2.3% |
| **+20¢** | 554 | 403 | 151 (5) | 2 | $-73.36 | -2.1% |
| **+10¢ (15¢ stop)** | 1240 | 1239 | 1 (1) | 0 | $-585.63 | -7.5% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 16:25 | +10 stop | HYPE | UP | 0.62 | 0.77 | 1.20 |
| 10-03 16:24 | +10 stop | SOL | DOWN | 0.67 | 0.49 | -2.14 |
| 10-03 16:22 | +5 | XRP | DOWN | 0.68 | 0.73 | 0.20 |
| 10-03 16:22 | +10 stop | HYPE | DOWN | 0.62 | 0.46 | -1.95 |
| 10-03 16:20 | +10 | SOL | UP | 0.68 | 0.83 | 1.24 |
| 10-03 16:20 | +10 stop | SOL | UP | 0.68 | 0.48 | -2.34 |
| 10-03 16:20 | +5 | SOL | UP | 0.68 | 0.83 | 1.24 |
| 10-03 16:20 | +10 stop | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-03 16:20 | +20 | XRP | DOWN | 0.63 | 0.84 | 1.83 |
| 10-03 16:20 | +15 | XRP | DOWN | 0.63 | 0.78 | 1.20 |
| 10-03 16:20 | +10 | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-03 16:20 | +5 | XRP | DOWN | 0.63 | 0.69 | 0.28 |
| 10-03 16:19 | +15 | HYPE | DOWN | 0.54 | open |  |
| 10-03 16:19 | +10 stop | ZEC | DOWN | 0.60 | 0.45 | -1.85 |
| 10-03 16:19 | +20 | ZEC | DOWN | 0.60 | 0.85 | 2.24 |
| 10-03 16:19 | +15 | ZEC | DOWN | 0.60 | 0.76 | 1.30 |
| 10-03 16:19 | +10 | ZEC | DOWN | 0.60 | 0.71 | 0.78 |
| 10-03 16:19 | +5 | ZEC | DOWN | 0.60 | 0.71 | 0.78 |
| 10-03 16:19 | +10 stop | SOL | DOWN | 0.56 | 0.35 | -2.44 |
| 10-03 16:18 | +10 stop | HYPE | DOWN | 0.70 | 0.53 | -2.03 |
| 10-03 16:18 | +10 | HYPE | DOWN | 0.70 | open |  |
| 10-03 16:18 | +5 | HYPE | DOWN | 0.70 | open |  |
| 10-03 16:16 | +10 stop | SOL | UP | 0.56 | 0.41 | -1.85 |
| 10-03 16:16 | +20 | SOL | UP | 0.56 | 0.83 | 2.42 |
| 10-03 16:16 | +15 | SOL | UP | 0.56 | 0.83 | 2.42 |
| 10-03 16:16 | +10 | SOL | UP | 0.56 | 0.68 | 0.86 |
| 10-03 16:16 | +5 | SOL | UP | 0.56 | 0.64 | 0.45 |
| 10-03 16:16 | +10 stop | NEAR | UP | 0.50 | 0.31 | -2.23 |
| 10-03 16:16 | +20 | NEAR | UP | 0.50 | open |  |
| 10-03 16:16 | +15 | NEAR | UP | 0.50 | open |  |
| 10-03 16:16 | +10 | NEAR | UP | 0.50 | open |  |
| 10-03 16:16 | +5 | NEAR | UP | 0.50 | open |  |
| 10-03 16:16 | +10 stop | DOGE | DOWN | 0.71 | 0.81 | 0.76 |
| 10-03 16:16 | +20 | DOGE | DOWN | 0.71 | 0.91 | 1.82 |
| 10-03 16:16 | +15 | DOGE | DOWN | 0.71 | 0.86 | 1.28 |
| 10-03 16:16 | +10 | DOGE | DOWN | 0.71 | 0.81 | 0.76 |
| 10-03 16:16 | +5 | DOGE | DOWN | 0.71 | 0.76 | 0.24 |
| 10-03 16:16 | +10 stop | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 10-03 16:16 | +20 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-03 16:16 | +15 | BTC | DOWN | 0.69 | 0.87 | 1.57 |
