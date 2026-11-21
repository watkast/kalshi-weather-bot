# Range-Scalp Bot

*Updated Sat Nov 21 22:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67839 | 59213 | 8626 (138) | 0 | $-18143.32 | -4.2% |
| **+10¢** | 50653 | 40574 | 10079 (181) | 0 | $-16818.65 | -5.3% |
| **+15¢** | 42462 | 31598 | 10864 (230) | 0 | $-15056.06 | -5.7% |
| **+20¢** | 37799 | 26381 | 11418 (288) | 0 | $-13377.50 | -5.6% |
| **+10¢ (15¢ stop)** | 82574 | 82396 | 178 (110) | 0 | $-30299.75 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 22:01 | +10 stop | XRP | DOWN | 0.58 | 0.71 | 0.97 |
| 11-21 22:01 | +20 | XRP | DOWN | 0.58 | 0.80 | 1.90 |
| 11-21 22:01 | +15 | XRP | DOWN | 0.58 | 0.80 | 1.90 |
| 11-21 22:01 | +10 | XRP | DOWN | 0.58 | 0.71 | 0.97 |
| 11-21 22:01 | +5 | XRP | DOWN | 0.58 | 0.67 | 0.56 |
| 11-21 22:01 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-21 22:01 | +20 | BTC | DOWN | 0.66 | 0.89 | 2.07 |
| 11-21 22:01 | +15 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-21 22:01 | +10 | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-21 22:01 | +5 | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-21 22:01 | +10 stop | ETH | DOWN | 0.65 | 0.81 | 1.33 |
| 11-21 22:01 | +20 | ETH | DOWN | 0.65 | 0.86 | 1.85 |
| 11-21 22:01 | +15 | ETH | DOWN | 0.65 | 0.81 | 1.33 |
| 11-21 22:01 | +10 | ETH | DOWN | 0.65 | 0.81 | 1.33 |
| 11-21 22:01 | +5 | ETH | DOWN | 0.65 | 0.72 | 0.39 |
| 11-21 22:01 | +10 stop | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-21 22:01 | +20 | DOGE | DOWN | 0.65 | 0.89 | 2.17 |
| 11-21 22:01 | +15 | DOGE | DOWN | 0.65 | 0.83 | 1.54 |
| 11-21 22:01 | +10 | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-21 22:01 | +5 | DOGE | DOWN | 0.66 | 0.72 | 0.29 |
| 11-21 22:01 | +10 stop | SOL | DOWN | 0.68 | 0.81 | 1.03 |
| 11-21 22:01 | +20 | SOL | DOWN | 0.68 | 0.88 | 1.76 |
| 11-21 22:01 | +15 | SOL | DOWN | 0.68 | 0.84 | 1.34 |
| 11-21 22:01 | +10 | SOL | DOWN | 0.68 | 0.81 | 0.99 |
| 11-21 22:01 | +5 | SOL | DOWN | 0.68 | 0.81 | 0.99 |
| 11-21 21:57 | +10 stop | BTC | UP | 0.60 | 0.70 | 0.68 |
| 11-21 21:55 | +10 stop | ETH | UP | 0.67 | 0.96 | 2.68 |
| 11-21 21:54 | +10 stop | BTC | UP | 0.57 | 0.37 | -2.35 |
| 11-21 21:54 | +15 | BTC | UP | 0.56 | 0.83 | 2.42 |
| 11-21 21:54 | +10 | BTC | UP | 0.56 | 0.67 | 0.76 |
| 11-21 21:54 | +10 stop | HYPE | UP | 0.57 | 0.76 | 1.59 |
| 11-21 21:54 | +20 | HYPE | UP | 0.57 | 0.77 | 1.69 |
| 11-21 21:54 | +15 | HYPE | UP | 0.57 | 0.76 | 1.59 |
| 11-21 21:54 | +10 | HYPE | UP | 0.57 | 0.76 | 1.59 |
| 11-21 21:54 | +5 | HYPE | UP | 0.57 | 0.66 | 0.56 |
| 11-21 21:53 | +10 stop | XRP | UP | 0.71 | 0.82 | 0.84 |
| 11-21 21:52 | +5 | BTC | UP | 0.71 | 0.83 | 0.95 |
| 11-21 21:52 | +10 stop | HYPE | DOWN | 0.57 | 0.41 | -1.95 |
| 11-21 21:51 | +10 stop | ZEC | UP | 0.56 | 0.81 | 2.21 |
| 11-21 21:51 | +10 stop | ETH | UP | 0.62 | 0.73 | 0.79 |
