# Range-Scalp Bot

*Updated Mon Oct 12 18:50 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13792 | 11946 | 1846 (25) | 0 | $-4320.47 | -5.0% |
| **+10¢** | 10442 | 8293 | 2149 (37) | 0 | $-4052.57 | -6.2% |
| **+15¢** | 8778 | 6480 | 2298 (55) | 0 | $-3578.12 | -6.5% |
| **+20¢** | 7805 | 5410 | 2395 (70) | 2 | $-3042.81 | -6.2% |
| **+10¢ (15¢ stop)** | 16941 | 16894 | 47 (27) | 0 | $-6618.37 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 18:46 | +10 stop | BTC | DOWN | 0.71 | 0.89 | 1.58 |
| 10-12 18:46 | +20 | BTC | DOWN | 0.71 | 0.93 | 1.96 |
| 10-12 18:46 | +15 | BTC | DOWN | 0.71 | 0.89 | 1.58 |
| 10-12 18:46 | +10 | BTC | DOWN | 0.71 | 0.89 | 1.58 |
| 10-12 18:46 | +5 | BTC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-12 18:46 | +10 stop | BNB | DOWN | 0.70 | 0.83 | 1.01 |
| 10-12 18:46 | +20 | BNB | DOWN | 0.70 | 0.94 | 2.12 |
| 10-12 18:46 | +15 | BNB | DOWN | 0.70 | 0.86 | 1.32 |
| 10-12 18:46 | +10 | BNB | DOWN | 0.70 | 0.83 | 1.01 |
| 10-12 18:46 | +5 | BNB | DOWN | 0.70 | 0.83 | 1.01 |
| 10-12 18:46 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-12 18:46 | +20 | SOL | DOWN | 0.70 | open |  |
| 10-12 18:46 | +15 | SOL | DOWN | 0.70 | 0.89 | 1.65 |
| 10-12 18:46 | +10 | SOL | DOWN | 0.70 | 0.82 | 0.91 |
| 10-12 18:46 | +5 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-12 18:45 | +10 stop | HYPE | DOWN | 0.64 | 0.77 | 1.00 |
| 10-12 18:45 | +20 | HYPE | DOWN | 0.64 | 0.87 | 2.01 |
| 10-12 18:45 | +15 | HYPE | DOWN | 0.64 | 0.87 | 2.01 |
| 10-12 18:45 | +10 | HYPE | DOWN | 0.64 | 0.77 | 0.96 |
| 10-12 18:45 | +5 | HYPE | DOWN | 0.65 | 0.72 | 0.39 |
| 10-12 18:45 | +10 stop | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 10-12 18:45 | +20 | NEAR | DOWN | 0.64 | open |  |
| 10-12 18:45 | +15 | NEAR | DOWN | 0.64 | 0.79 | 1.21 |
| 10-12 18:45 | +10 | NEAR | DOWN | 0.64 | 0.79 | 1.21 |
| 10-12 18:45 | +5 | NEAR | DOWN | 0.65 | 0.70 | 0.19 |
| 10-12 18:45 | +10 stop | ZEC | DOWN | 0.62 | 0.73 | 0.79 |
| 10-12 18:45 | +20 | ZEC | DOWN | 0.62 | 0.87 | 2.25 |
| 10-12 18:45 | +15 | ZEC | DOWN | 0.62 | 0.78 | 1.30 |
| 10-12 18:45 | +10 | ZEC | DOWN | 0.62 | 0.73 | 0.79 |
| 10-12 18:45 | +5 | ZEC | DOWN | 0.62 | 0.67 | 0.17 |
| 10-12 18:41 | +10 stop | HYPE | UP | 0.65 | 0.49 | -1.94 |
| 10-12 18:41 | +5 | HYPE | UP | 0.65 | 0.79 | 1.12 |
| 10-12 18:41 | +10 stop | ETH | UP | 0.71 | 0.92 | 1.89 |
| 10-12 18:41 | +5 | ETH | UP | 0.70 | 0.77 | 0.42 |
| 10-12 18:40 | +10 stop | ETH | UP | 0.57 | 0.75 | 1.48 |
| 10-12 18:39 | +10 stop | HYPE | UP | 0.56 | 0.70 | 1.07 |
| 10-12 18:39 | +10 stop | SOL | UP | 0.62 | 0.74 | 0.89 |
| 10-12 18:39 | +15 | SOL | UP | 0.62 | 0.84 | 1.93 |
| 10-12 18:39 | +10 | SOL | UP | 0.62 | 0.74 | 0.89 |
| 10-12 18:39 | +5 | SOL | UP | 0.62 | 0.71 | 0.58 |
