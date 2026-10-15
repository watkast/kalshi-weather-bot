# Range-Scalp Bot

*Updated Thu Oct 15 21:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18210 | 15809 | 2401 (28) | 4 | $-5585.02 | -4.9% |
| **+10¢** | 13751 | 10971 | 2780 (40) | 3 | $-5046.91 | -5.8% |
| **+15¢** | 11531 | 8539 | 2992 (59) | 4 | $-4577.40 | -6.3% |
| **+20¢** | 10244 | 7118 | 3126 (77) | 4 | $-3970.47 | -6.2% |
| **+10¢ (15¢ stop)** | 22413 | 22363 | 50 (29) | 1 | $-8669.81 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 21:56 | +10 stop | NEAR | UP | 0.63 | open |  |
| 10-15 21:55 | +10 stop | NEAR | DOWN | 0.59 | 0.44 | -1.85 |
| 10-15 21:54 | +10 stop | ZEC | UP | 0.61 | 0.44 | -2.05 |
| 10-15 21:54 | +10 stop | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-15 21:54 | +5 | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-15 21:53 | +10 stop | XRP | UP | 0.57 | 0.39 | -2.14 |
| 10-15 21:53 | +10 stop | SOL | UP | 0.69 | 0.84 | 1.25 |
| 10-15 21:53 | +10 stop | HYPE | DOWN | 0.62 | 0.78 | 1.31 |
| 10-15 21:53 | +15 | HYPE | DOWN | 0.63 | 0.78 | 1.22 |
| 10-15 21:53 | +10 | HYPE | DOWN | 0.63 | 0.78 | 1.22 |
| 10-15 21:53 | +5 | HYPE | DOWN | 0.61 | 0.66 | 0.17 |
| 10-15 21:53 | +5 | ZEC | UP | 0.69 | open |  |
| 10-15 21:52 | +10 stop | SOL | UP | 0.64 | 0.45 | -2.25 |
| 10-15 21:52 | +10 stop | XRP | DOWN | 0.61 | 0.42 | -2.25 |
| 10-15 21:52 | +5 | ZEC | UP | 0.53 | 0.58 | 0.14 |
| 10-15 21:52 | +10 stop | ZEC | UP | 0.59 | 0.69 | 0.68 |
| 10-15 21:52 | +5 | ZEC | UP | 0.59 | 0.66 | 0.37 |
| 10-15 21:52 | +10 stop | NEAR | UP | 0.62 | 0.29 | -3.62 |
| 10-15 21:51 | +10 stop | DOGE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-15 21:51 | +10 stop | ETH | DOWN | 0.66 | 0.80 | 1.12 |
| 10-15 21:51 | +20 | ETH | DOWN | 0.66 | 0.86 | 1.75 |
| 10-15 21:51 | +15 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 10-15 21:51 | +10 | ETH | DOWN | 0.66 | 0.80 | 1.12 |
| 10-15 21:51 | +5 | ETH | DOWN | 0.66 | 0.80 | 1.12 |
| 10-15 21:50 | +10 stop | XRP | UP | 0.67 | 0.51 | -1.94 |
| 10-15 21:50 | +10 stop | HYPE | DOWN | 0.55 | 0.80 | 2.20 |
| 10-15 21:50 | +15 | HYPE | DOWN | 0.55 | 0.80 | 2.20 |
| 10-15 21:50 | +10 | HYPE | DOWN | 0.55 | 0.80 | 2.20 |
| 10-15 21:50 | +5 | HYPE | DOWN | 0.55 | 0.63 | 0.45 |
| 10-15 21:49 | +10 stop | SOL | UP | 0.71 | 0.56 | -1.83 |
| 10-15 21:49 | +10 stop | BNB | DOWN | 0.66 | 0.76 | 0.71 |
| 10-15 21:49 | +5 | BNB | DOWN | 0.66 | 0.73 | 0.40 |
| 10-15 21:49 | +10 stop | NEAR | UP | 0.62 | 0.72 | 0.68 |
| 10-15 21:49 | +5 | DOGE | DOWN | 0.63 | 0.69 | 0.28 |
| 10-15 21:47 | +5 | XRP | DOWN | 0.68 | 0.75 | 0.42 |
| 10-15 21:46 | +10 stop | ZEC | DOWN | 0.56 | 0.28 | -3.13 |
| 10-15 21:46 | +20 | ZEC | DOWN | 0.56 | 0.82 | 2.31 |
| 10-15 21:46 | +15 | ZEC | DOWN | 0.56 | 0.82 | 2.31 |
| 10-15 21:46 | +10 | ZEC | DOWN | 0.56 | 0.82 | 2.31 |
| 10-15 21:46 | +5 | ZEC | DOWN | 0.56 | 0.61 | 0.15 |
