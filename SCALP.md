# Range-Scalp Bot

*Updated Sun Oct 11 23:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12666 | 10937 | 1729 (25) | 5 | $-4156.91 | -5.2% |
| **+10¢** | 9608 | 7606 | 2002 (37) | 5 | $-3891.96 | -6.4% |
| **+15¢** | 8084 | 5954 | 2130 (55) | 6 | $-3352.46 | -6.6% |
| **+20¢** | 7203 | 4982 | 2221 (69) | 6 | $-2856.13 | -6.3% |
| **+10¢ (15¢ stop)** | 15597 | 15556 | 41 (25) | 2 | $-6082.27 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 23:27 | +10 stop | BTC | UP | 0.55 | open |  |
| 10-11 23:27 | +10 stop | ETH | UP | 0.54 | open |  |
| 10-11 23:27 | +10 | ETH | UP | 0.53 | open |  |
| 10-11 23:27 | +5 | ETH | UP | 0.53 | open |  |
| 10-11 23:26 | +10 stop | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 10-11 23:26 | +15 | ETH | DOWN | 0.58 | open |  |
| 10-11 23:26 | +10 | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 10-11 23:26 | +5 | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 10-11 23:26 | +10 stop | DOGE | DOWN | 0.48 | 0.62 | 1.05 |
| 10-11 23:26 | +20 | DOGE | DOWN | 0.49 | open |  |
| 10-11 23:26 | +10 | DOGE | DOWN | 0.49 | 0.62 | 0.95 |
| 10-11 23:26 | +5 | DOGE | DOWN | 0.49 | 0.62 | 0.95 |
| 10-11 23:24 | +5 | SOL | DOWN | 0.62 | open |  |
| 10-11 23:24 | +10 stop | SOL | DOWN | 0.61 | 0.40 | -2.44 |
| 10-11 23:24 | +10 | SOL | DOWN | 0.61 | open |  |
| 10-11 23:24 | +5 | SOL | DOWN | 0.60 | 0.69 | 0.58 |
| 10-11 23:23 | +10 stop | SOL | DOWN | 0.57 | 0.69 | 0.84 |
| 10-11 23:23 | +20 | SOL | DOWN | 0.57 | open |  |
| 10-11 23:23 | +15 | SOL | DOWN | 0.57 | open |  |
| 10-11 23:23 | +10 | SOL | DOWN | 0.55 | 0.69 | 1.07 |
| 10-11 23:23 | +5 | SOL | DOWN | 0.55 | 0.60 | 0.15 |
| 10-11 23:23 | +10 stop | BTC | DOWN | 0.67 | 0.48 | -2.24 |
| 10-11 23:23 | +10 stop | DOGE | DOWN | 0.65 | 0.79 | 1.12 |
| 10-11 23:23 | +15 | DOGE | DOWN | 0.65 | open |  |
| 10-11 23:23 | +10 | DOGE | DOWN | 0.65 | 0.79 | 1.12 |
| 10-11 23:23 | +5 | DOGE | DOWN | 0.65 | 0.72 | 0.39 |
| 10-11 23:23 | +10 stop | XRP | UP | 0.61 | 0.71 | 0.68 |
| 10-11 23:22 | +10 stop | NEAR | DOWN | 0.67 | 0.44 | -2.60 |
| 10-11 23:21 | +10 stop | ETH | DOWN | 0.57 | 0.76 | 1.59 |
| 10-11 23:21 | +10 stop | DOGE | DOWN | 0.58 | 0.71 | 0.97 |
| 10-11 23:21 | +15 | DOGE | DOWN | 0.58 | 0.74 | 1.28 |
| 10-11 23:21 | +10 | DOGE | DOWN | 0.58 | 0.71 | 0.97 |
| 10-11 23:21 | +5 | DOGE | DOWN | 0.58 | 0.71 | 0.97 |
| 10-11 23:21 | +10 stop | XRP | UP | 0.61 | 0.43 | -2.15 |
| 10-11 23:21 | +10 stop | ZEC | UP | 0.68 | 0.79 | 0.82 |
| 10-11 23:20 | +10 stop | DOGE | DOWN | 0.49 | 0.69 | 1.67 |
| 10-11 23:20 | +15 | DOGE | DOWN | 0.49 | 0.69 | 1.67 |
| 10-11 23:20 | +10 | DOGE | DOWN | 0.49 | 0.69 | 1.67 |
| 10-11 23:20 | +5 | DOGE | DOWN | 0.49 | 0.69 | 1.67 |
| 10-11 23:20 | +10 stop | SOL | DOWN | 0.53 | 0.75 | 1.88 |
