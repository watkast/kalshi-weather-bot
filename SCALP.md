# Range-Scalp Bot

*Updated Tue Oct 27 05:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36079 | 31495 | 4584 (43) | 0 | $-10046.18 | -4.4% |
| **+10¢** | 26968 | 21665 | 5303 (65) | 0 | $-8887.29 | -5.2% |
| **+15¢** | 22568 | 16870 | 5698 (89) | 0 | $-7889.70 | -5.6% |
| **+20¢** | 20005 | 14035 | 5970 (112) | 0 | $-6930.36 | -5.5% |
| **+10¢ (15¢ stop)** | 44249 | 44186 | 63 (33) | 0 | $-16878.29 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 05:42 | +5 | HYPE | DOWN | 0.50 | 0.62 | 0.85 |
| 10-27 05:42 | +10 stop | BNB | DOWN | 0.66 | 0.76 | 0.71 |
| 10-27 05:42 | +10 stop | HYPE | DOWN | 0.59 | 0.72 | 0.98 |
| 10-27 05:42 | +5 | HYPE | DOWN | 0.59 | 0.65 | 0.27 |
| 10-27 05:41 | +10 stop | HYPE | UP | 0.40 | 0.59 | 1.56 |
| 10-27 05:41 | +5 | HYPE | UP | 0.45 | 0.59 | 1.05 |
| 10-27 05:41 | +10 stop | ZEC | DOWN | 0.60 | 0.77 | 1.40 |
| 10-27 05:41 | +15 | ZEC | DOWN | 0.60 | 0.77 | 1.40 |
| 10-27 05:41 | +10 | ZEC | DOWN | 0.60 | 0.77 | 1.40 |
| 10-27 05:41 | +5 | ZEC | DOWN | 0.60 | 0.77 | 1.40 |
| 10-27 05:40 | +5 | HYPE | UP | 0.57 | 0.63 | 0.25 |
| 10-27 05:40 | +10 stop | SOL | UP | 0.66 | 0.35 | -3.42 |
| 10-27 05:39 | +10 stop | HYPE | UP | 0.70 | 0.49 | -2.43 |
| 10-27 05:39 | +10 | HYPE | UP | 0.70 | 0.92 | 2.03 |
| 10-27 05:39 | +5 | HYPE | UP | 0.70 | 0.75 | 0.21 |
| 10-27 05:37 | +10 stop | ETH | UP | 0.64 | 0.45 | -2.25 |
| 10-27 05:37 | +5 | ETH | UP | 0.62 | 0.83 | 1.83 |
| 10-27 05:37 | +5 | HYPE | DOWN | 0.68 | 0.73 | 0.20 |
| 10-27 05:36 | +10 stop | HYPE | DOWN | 0.60 | 0.73 | 0.99 |
| 10-27 05:36 | +5 | HYPE | DOWN | 0.60 | 0.66 | 0.27 |
| 10-27 05:36 | +5 | DOGE | UP | 0.61 | 0.72 | 0.78 |
| 10-27 05:35 | +10 stop | HYPE | UP | 0.36 | 0.55 | 1.55 |
| 10-27 05:35 | +10 stop | SOL | DOWN | 0.70 | 0.54 | -1.93 |
| 10-27 05:35 | +20 | SOL | DOWN | 0.70 | yes | -7.15 |
| 10-27 05:35 | +15 | SOL | DOWN | 0.71 | 0.88 | 1.47 |
| 10-27 05:35 | +10 | SOL | DOWN | 0.71 | 0.84 | 1.05 |
| 10-27 05:35 | +5 | SOL | DOWN | 0.71 | 0.79 | 0.53 |
| 10-27 05:35 | +10 stop | ZEC | DOWN | 0.68 | 0.81 | 1.03 |
| 10-27 05:35 | +20 | ZEC | DOWN | 0.68 | 0.89 | 1.87 |
| 10-27 05:35 | +15 | ZEC | DOWN | 0.68 | 0.87 | 1.66 |
| 10-27 05:35 | +10 | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-27 05:35 | +5 | ZEC | DOWN | 0.68 | 0.77 | 0.61 |
| 10-27 05:35 | +10 stop | NEAR | UP | 0.62 | 0.72 | 0.68 |
| 10-27 05:35 | +10 stop | DOGE | UP | 0.60 | 0.72 | 0.88 |
| 10-27 05:35 | +5 | DOGE | UP | 0.60 | 0.68 | 0.47 |
| 10-27 05:34 | +10 stop | ETH | DOWN | 0.51 | 0.35 | -1.94 |
| 10-27 05:34 | +5 | ETH | DOWN | 0.51 | 0.58 | 0.34 |
| 10-27 05:34 | +10 stop | BTC | UP | 0.68 | 0.82 | 1.15 |
| 10-27 05:34 | +20 | BTC | UP | 0.67 | 0.88 | 1.86 |
| 10-27 05:34 | +15 | BTC | UP | 0.67 | 0.82 | 1.23 |
