# Range-Scalp Bot

*Updated Thu Oct 22 03:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28223 | 24595 | 3628 (39) | 0 | $-8093.31 | -4.6% |
| **+10¢** | 21196 | 17001 | 4195 (55) | 0 | $-7162.22 | -5.4% |
| **+15¢** | 17753 | 13237 | 4516 (78) | 0 | $-6406.44 | -5.7% |
| **+20¢** | 15706 | 10970 | 4736 (98) | 0 | $-5789.97 | -5.9% |
| **+10¢ (15¢ stop)** | 34636 | 34577 | 59 (32) | 0 | $-12946.72 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 03:42 | +5 | SOL | UP | 0.66 | 0.75 | 0.60 |
| 10-22 03:42 | +10 stop | DOGE | UP | 0.67 | 0.83 | 1.34 |
| 10-22 03:42 | +5 | DOGE | UP | 0.67 | 0.74 | 0.40 |
| 10-22 03:41 | +5 | SOL | DOWN | 0.51 | 0.62 | 0.75 |
| 10-22 03:40 | +10 stop | DOGE | DOWN | 0.47 | 0.63 | 1.25 |
| 10-22 03:40 | +5 | DOGE | DOWN | 0.47 | 0.63 | 1.25 |
| 10-22 03:40 | +5 | SOL | DOWN | 0.53 | 0.62 | 0.55 |
| 10-22 03:40 | +10 stop | SOL | DOWN | 0.55 | 0.35 | -2.34 |
| 10-22 03:39 | +10 stop | SOL | UP | 0.40 | 0.56 | 1.25 |
| 10-22 03:39 | +10 stop | BTC | UP | 0.64 | 0.75 | 0.79 |
| 10-22 03:38 | +5 | XRP | DOWN | 0.69 | 0.86 | 1.46 |
| 10-22 03:38 | +10 stop | XRP | DOWN | 0.68 | 0.86 | 1.55 |
| 10-22 03:38 | +20 | XRP | DOWN | 0.68 | yes | -6.96 |
| 10-22 03:38 | +15 | XRP | DOWN | 0.68 | 0.86 | 1.55 |
| 10-22 03:38 | +10 | XRP | DOWN | 0.70 | 0.86 | 1.36 |
| 10-22 03:38 | +10 stop | NEAR | DOWN | 0.63 | 0.37 | -2.94 |
| 10-22 03:38 | +10 stop | DOGE | DOWN | 0.56 | 0.75 | 1.58 |
| 10-22 03:38 | +5 | DOGE | DOWN | 0.56 | 0.75 | 1.58 |
| 10-22 03:38 | +10 stop | BNB | UP | 0.69 | 0.83 | 1.15 |
| 10-22 03:38 | +5 | BNB | UP | 0.69 | 0.76 | 0.42 |
| 10-22 03:37 | +10 stop | ETH | UP | 0.59 | 0.70 | 0.78 |
| 10-22 03:37 | +10 | ETH | UP | 0.59 | 0.70 | 0.78 |
| 10-22 03:37 | +5 | ETH | UP | 0.59 | 0.65 | 0.27 |
| 10-22 03:37 | +10 stop | BTC | UP | 0.55 | 0.70 | 1.17 |
| 10-22 03:37 | +10 stop | DOGE | UP | 0.49 | 0.28 | -2.43 |
| 10-22 03:37 | +15 | DOGE | UP | 0.49 | 0.66 | 1.36 |
| 10-22 03:37 | +10 | DOGE | UP | 0.49 | 0.66 | 1.36 |
| 10-22 03:37 | +5 | DOGE | UP | 0.49 | 0.57 | 0.44 |
| 10-22 03:37 | +10 stop | NEAR | DOWN | 0.46 | 0.66 | 1.66 |
| 10-22 03:36 | +10 stop | SOL | DOWN | 0.55 | 0.40 | -1.85 |
| 10-22 03:36 | +15 | SOL | DOWN | 0.55 | yes | -5.68 |
| 10-22 03:36 | +10 | SOL | DOWN | 0.55 | yes | -5.68 |
| 10-22 03:36 | +5 | SOL | DOWN | 0.55 | 0.62 | 0.35 |
| 10-22 03:35 | +10 stop | BNB | DOWN | 0.68 | 0.53 | -1.84 |
| 10-22 03:35 | +15 | BNB | DOWN | 0.68 | yes | -6.96 |
| 10-22 03:35 | +10 | BNB | DOWN | 0.68 | yes | -6.96 |
| 10-22 03:35 | +5 | BNB | DOWN | 0.66 | 0.72 | 0.29 |
| 10-22 03:35 | +10 stop | BTC | DOWN | 0.67 | 0.43 | -2.74 |
| 10-22 03:35 | +15 | BTC | DOWN | 0.67 | yes | -6.86 |
| 10-22 03:35 | +10 | BTC | DOWN | 0.67 | yes | -6.86 |
