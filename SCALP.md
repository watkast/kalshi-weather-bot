# Range-Scalp Bot

*Updated Mon Oct 12 20:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13853 | 11995 | 1858 (25) | 5 | $-4367.74 | -5.0% |
| **+10¢** | 10480 | 8316 | 2164 (37) | 6 | $-4124.03 | -6.3% |
| **+15¢** | 8812 | 6499 | 2313 (55) | 7 | $-3642.84 | -6.6% |
| **+20¢** | 7839 | 5429 | 2410 (70) | 7 | $-3099.17 | -6.3% |
| **+10¢ (15¢ stop)** | 17015 | 16968 | 47 (27) | 0 | $-6640.92 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 19:55 | +10 stop | BTC | UP | 0.71 | 0.82 | 0.84 |
| 10-12 19:53 | +10 stop | NEAR | UP | 0.67 | 0.48 | -2.24 |
| 10-12 19:53 | +20 | NEAR | UP | 0.67 | open |  |
| 10-12 19:53 | +15 | NEAR | UP | 0.67 | open |  |
| 10-12 19:53 | +10 | NEAR | UP | 0.68 | open |  |
| 10-12 19:53 | +5 | NEAR | UP | 0.68 | open |  |
| 10-12 19:53 | +10 stop | HYPE | DOWN | 0.69 | 0.80 | 0.83 |
| 10-12 19:53 | +10 | HYPE | DOWN | 0.69 | 0.80 | 0.83 |
| 10-12 19:53 | +5 | HYPE | DOWN | 0.70 | 0.80 | 0.77 |
| 10-12 19:52 | +10 stop | ETH | UP | 0.69 | 0.80 | 0.83 |
| 10-12 19:51 | +10 stop | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-12 19:51 | +20 | HYPE | DOWN | 0.71 | 0.99 | 2.61 |
| 10-12 19:51 | +15 | HYPE | DOWN | 0.71 | 0.87 | 1.37 |
| 10-12 19:51 | +10 | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-12 19:51 | +5 | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-12 19:50 | +10 stop | BNB | UP | 0.71 | 0.81 | 0.74 |
| 10-12 19:50 | +10 stop | ETH | UP | 0.58 | 0.71 | 0.97 |
| 10-12 19:50 | +10 stop | BTC | UP | 0.60 | 0.74 | 1.09 |
| 10-12 19:49 | +10 stop | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 10-12 19:48 | +10 stop | BNB | DOWN | 0.55 | 0.35 | -2.34 |
| 10-12 19:47 | +10 stop | SOL | UP | 0.56 | 0.73 | 1.36 |
| 10-12 19:47 | +10 | SOL | UP | 0.56 | 0.73 | 1.36 |
| 10-12 19:47 | +5 | SOL | UP | 0.56 | 0.62 | 0.23 |
| 10-12 19:47 | +10 stop | ZEC | UP | 0.67 | 0.52 | -1.84 |
| 10-12 19:47 | +10 stop | DOGE | UP | 0.57 | 0.74 | 1.38 |
| 10-12 19:47 | +20 | DOGE | UP | 0.57 | 0.78 | 1.79 |
| 10-12 19:47 | +15 | DOGE | UP | 0.57 | 0.74 | 1.38 |
| 10-12 19:47 | +10 | DOGE | UP | 0.57 | 0.74 | 1.38 |
| 10-12 19:47 | +5 | DOGE | UP | 0.57 | 0.63 | 0.25 |
| 10-12 19:47 | +10 stop | SOL | DOWN | 0.47 | 0.58 | 0.74 |
| 10-12 19:47 | +20 | SOL | DOWN | 0.47 | open |  |
| 10-12 19:47 | +15 | SOL | DOWN | 0.48 | open |  |
| 10-12 19:47 | +10 | SOL | DOWN | 0.48 | 0.58 | 0.64 |
| 10-12 19:47 | +5 | SOL | DOWN | 0.48 | 0.58 | 0.64 |
| 10-12 19:47 | +10 stop | XRP | DOWN | 0.49 | 0.29 | -2.33 |
| 10-12 19:47 | +20 | XRP | DOWN | 0.49 | open |  |
| 10-12 19:47 | +15 | XRP | DOWN | 0.49 | open |  |
| 10-12 19:47 | +10 | XRP | DOWN | 0.49 | open |  |
| 10-12 19:47 | +5 | XRP | DOWN | 0.49 | 0.56 | 0.34 |
| 10-12 19:45 | +10 stop | BTC | DOWN | 0.62 | 0.42 | -2.35 |
