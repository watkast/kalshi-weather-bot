# Range-Scalp Bot

*Updated Mon Oct 05 23:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4345 | 3743 | 602 (6) | 0 | $-1488.96 | -5.4% |
| **+10¢** | 3347 | 2651 | 696 (9) | 1 | $-1356.28 | -6.4% |
| **+15¢** | 2806 | 2072 | 734 (12) | 4 | $-1171.87 | -6.7% |
| **+20¢** | 2510 | 1745 | 765 (17) | 4 | $-994.63 | -6.3% |
| **+10¢ (15¢ stop)** | 5328 | 5317 | 11 (6) | 0 | $-1894.24 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 23:32 | +5 | NEAR | UP | 0.50 | 0.63 | 0.95 |
| 10-05 23:32 | +10 stop | HYPE | DOWN | 0.50 | 0.66 | 1.26 |
| 10-05 23:32 | +20 | HYPE | DOWN | 0.50 | 0.70 | 1.67 |
| 10-05 23:32 | +15 | HYPE | DOWN | 0.50 | 0.66 | 1.26 |
| 10-05 23:32 | +10 | HYPE | DOWN | 0.50 | 0.66 | 1.26 |
| 10-05 23:32 | +5 | HYPE | DOWN | 0.50 | 0.66 | 1.26 |
| 10-05 23:32 | +10 stop | DOGE | DOWN | 0.71 | 0.82 | 0.85 |
| 10-05 23:32 | +20 | DOGE | DOWN | 0.71 | open |  |
| 10-05 23:32 | +15 | DOGE | DOWN | 0.71 | open |  |
| 10-05 23:32 | +10 | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-05 23:32 | +5 | DOGE | DOWN | 0.71 | 0.78 | 0.42 |
| 10-05 23:32 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-05 23:32 | +20 | XRP | DOWN | 0.70 | 0.91 | 1.86 |
| 10-05 23:32 | +15 | XRP | DOWN | 0.70 | 0.86 | 1.36 |
| 10-05 23:32 | +10 | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-05 23:32 | +5 | XRP | DOWN | 0.70 | 0.75 | 0.21 |
| 10-05 23:31 | +5 | BNB | DOWN | 0.55 | 0.71 | 1.27 |
| 10-05 23:31 | +10 stop | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 10-05 23:31 | +20 | SOL | DOWN | 0.63 | open |  |
| 10-05 23:31 | +15 | SOL | DOWN | 0.63 | open |  |
| 10-05 23:31 | +10 | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 10-05 23:31 | +5 | SOL | DOWN | 0.63 | 0.68 | 0.17 |
| 10-05 23:31 | +10 stop | ZEC | DOWN | 0.66 | 0.79 | 1.03 |
| 10-05 23:31 | +20 | ZEC | DOWN | 0.66 | 0.88 | 1.97 |
| 10-05 23:31 | +15 | ZEC | DOWN | 0.67 | 0.84 | 1.45 |
| 10-05 23:31 | +10 | ZEC | DOWN | 0.67 | 0.79 | 0.95 |
| 10-05 23:31 | +5 | ZEC | DOWN | 0.66 | 0.72 | 0.30 |
| 10-05 23:31 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-05 23:31 | +20 | BTC | DOWN | 0.67 | open |  |
| 10-05 23:31 | +15 | BTC | DOWN | 0.67 | open |  |
| 10-05 23:31 | +10 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-05 23:31 | +5 | BTC | DOWN | 0.67 | 0.75 | 0.50 |
| 10-05 23:31 | +10 stop | ETH | DOWN | 0.61 | 0.72 | 0.78 |
| 10-05 23:31 | +20 | ETH | DOWN | 0.61 | 0.81 | 1.72 |
| 10-05 23:31 | +15 | ETH | DOWN | 0.61 | 0.77 | 1.30 |
| 10-05 23:31 | +10 | ETH | DOWN | 0.61 | 0.72 | 0.78 |
| 10-05 23:31 | +5 | ETH | DOWN | 0.61 | 0.72 | 0.78 |
| 10-05 23:31 | +10 stop | BNB | DOWN | 0.56 | 0.71 | 1.17 |
| 10-05 23:31 | +20 | BNB | DOWN | 0.56 | 0.76 | 1.69 |
| 10-05 23:31 | +15 | BNB | DOWN | 0.56 | 0.71 | 1.17 |
