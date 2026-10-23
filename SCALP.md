# Range-Scalp Bot

*Updated Fri Oct 23 20:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30928 | 26955 | 3973 (39) | 4 | $-8927.44 | -4.6% |
| **+10¢** | 23130 | 18537 | 4593 (57) | 5 | $-7947.95 | -5.5% |
| **+15¢** | 19351 | 14408 | 4943 (80) | 5 | $-7173.55 | -5.9% |
| **+20¢** | 17139 | 11963 | 5176 (103) | 5 | $-6410.22 | -6.0% |
| **+10¢ (15¢ stop)** | 37958 | 37899 | 59 (32) | 1 | $-14505.37 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 20:42 | +10 stop | DOGE | DOWN | 0.67 | open |  |
| 10-23 20:42 | +5 | DOGE | DOWN | 0.67 | 0.72 | 0.19 |
| 10-23 20:42 | +5 | SOL | DOWN | 0.70 | open |  |
| 10-23 20:41 | +10 stop | HYPE | UP | 0.52 | 0.32 | -2.34 |
| 10-23 20:41 | +10 | HYPE | UP | 0.52 | open |  |
| 10-23 20:41 | +5 | HYPE | UP | 0.52 | open |  |
| 10-23 20:41 | +10 stop | BTC | DOWN | 0.71 | 0.56 | -1.83 |
| 10-23 20:41 | +10 stop | SOL | UP | 0.53 | 0.31 | -2.53 |
| 10-23 20:41 | +5 | SOL | UP | 0.53 | 0.61 | 0.45 |
| 10-23 20:40 | +10 stop | XRP | UP | 0.61 | 0.41 | -2.34 |
| 10-23 20:40 | +10 stop | HYPE | UP | 0.65 | 0.77 | 0.87 |
| 10-23 20:40 | +15 | HYPE | UP | 0.65 | open |  |
| 10-23 20:40 | +10 | HYPE | UP | 0.65 | 0.77 | 0.87 |
| 10-23 20:40 | +5 | HYPE | UP | 0.65 | 0.77 | 0.87 |
| 10-23 20:40 | +10 stop | DOGE | UP | 0.66 | 0.49 | -2.04 |
| 10-23 20:40 | +15 | DOGE | UP | 0.66 | open |  |
| 10-23 20:40 | +10 | DOGE | UP | 0.66 | open |  |
| 10-23 20:40 | +5 | DOGE | UP | 0.66 | 0.71 | 0.19 |
| 10-23 20:40 | +5 | SOL | UP | 0.54 | 0.62 | 0.45 |
| 10-23 20:40 | +10 stop | SOL | UP | 0.51 | 0.62 | 0.75 |
| 10-23 20:39 | +10 stop | XRP | UP | 0.69 | 0.53 | -1.93 |
| 10-23 20:39 | +10 stop | BTC | DOWN | 0.52 | 0.33 | -2.24 |
| 10-23 20:37 | +5 | ETH | UP | 0.63 | 0.74 | 0.79 |
| 10-23 20:37 | +10 stop | ETH | UP | 0.70 | 0.84 | 1.15 |
| 10-23 20:37 | +10 stop | ZEC | UP | 0.71 | 0.85 | 1.16 |
| 10-23 20:36 | +5 | ZEC | UP | 0.70 | 0.76 | 0.32 |
| 10-23 20:36 | +10 stop | BNB | UP | 0.59 | 0.74 | 1.19 |
| 10-23 20:36 | +10 stop | DOGE | DOWN | 0.63 | 0.45 | -2.15 |
| 10-23 20:36 | +10 stop | SOL | DOWN | 0.68 | 0.52 | -1.94 |
| 10-23 20:35 | +10 stop | NEAR | DOWN | 0.67 | 0.50 | -2.04 |
| 10-23 20:35 | +10 stop | ZEC | UP | 0.54 | 0.67 | 0.96 |
| 10-23 20:35 | +5 | ZEC | UP | 0.54 | 0.61 | 0.35 |
| 10-23 20:35 | +10 stop | ETH | DOWN | 0.53 | 0.37 | -1.95 |
| 10-23 20:35 | +10 stop | HYPE | DOWN | 0.71 | 0.52 | -2.23 |
| 10-23 20:34 | +10 stop | BTC | DOWN | 0.57 | 0.75 | 1.48 |
| 10-23 20:34 | +10 stop | BNB | UP | 0.68 | 0.53 | -1.84 |
| 10-23 20:34 | +20 | BNB | UP | 0.68 | 0.88 | 1.76 |
| 10-23 20:34 | +15 | BNB | UP | 0.68 | 0.85 | 1.45 |
| 10-23 20:34 | +10 | BNB | UP | 0.68 | 0.82 | 1.13 |
| 10-23 20:34 | +5 | BNB | UP | 0.68 | 0.74 | 0.30 |
