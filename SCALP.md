# Range-Scalp Bot

*Updated Sun Oct 11 20:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12483 | 10772 | 1711 (25) | 0 | $-4143.74 | -5.3% |
| **+10¢** | 9477 | 7495 | 1982 (37) | 0 | $-3900.69 | -6.5% |
| **+15¢** | 7980 | 5873 | 2107 (55) | 0 | $-3343.53 | -6.7% |
| **+20¢** | 7113 | 4918 | 2195 (69) | 0 | $-2830.68 | -6.3% |
| **+10¢ (15¢ stop)** | 15382 | 15341 | 41 (25) | 0 | $-6042.42 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 20:43 | +10 stop | DOGE | UP | 0.57 | 0.68 | 0.77 |
| 10-11 20:43 | +5 | DOGE | UP | 0.68 | 0.83 | 1.24 |
| 10-11 20:42 | +10 stop | SOL | UP | 0.58 | 0.78 | 1.69 |
| 10-11 20:42 | +10 stop | DOGE | DOWN | 0.50 | 0.32 | -2.14 |
| 10-11 20:42 | +5 | DOGE | DOWN | 0.50 | 0.56 | 0.24 |
| 10-11 20:40 | +10 stop | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-11 20:40 | +10 stop | ZEC | DOWN | 0.53 | 0.68 | 1.16 |
| 10-11 20:40 | +5 | ZEC | DOWN | 0.53 | 0.68 | 1.16 |
| 10-11 20:38 | +10 stop | XRP | UP | 0.59 | 0.85 | 2.34 |
| 10-11 20:38 | +10 stop | ZEC | DOWN | 0.70 | 0.51 | -2.25 |
| 10-11 20:38 | +10 stop | DOGE | UP | 0.62 | 0.45 | -2.05 |
| 10-11 20:36 | +10 stop | ZEC | UP | 0.61 | 0.39 | -2.54 |
| 10-11 20:36 | +10 stop | NEAR | DOWN | 0.63 | 0.75 | 0.89 |
| 10-11 20:36 | +20 | NEAR | DOWN | 0.63 | 0.86 | 2.04 |
| 10-11 20:36 | +15 | NEAR | DOWN | 0.63 | 0.79 | 1.31 |
| 10-11 20:36 | +10 | NEAR | DOWN | 0.63 | 0.75 | 0.89 |
| 10-11 20:36 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 10-11 20:35 | +10 stop | ZEC | DOWN | 0.59 | 0.40 | -2.20 |
| 10-11 20:34 | +10 stop | DOGE | UP | 0.59 | 0.73 | 1.09 |
| 10-11 20:34 | +10 stop | BTC | UP | 0.70 | 0.83 | 1.05 |
| 10-11 20:34 | +10 stop | BNB | UP | 0.65 | 0.80 | 1.22 |
| 10-11 20:34 | +10 stop | XRP | UP | 0.62 | 0.78 | 1.32 |
| 10-11 20:34 | +10 stop | SOL | UP | 0.67 | 0.78 | 0.81 |
| 10-11 20:33 | +10 stop | SOL | DOWN | 0.45 | 0.56 | 0.74 |
| 10-11 20:31 | +10 stop | SOL | DOWN | 0.70 | 0.55 | -1.83 |
| 10-11 20:31 | +20 | SOL | DOWN | 0.70 | yes | -7.15 |
| 10-11 20:31 | +15 | SOL | DOWN | 0.70 | yes | -7.15 |
| 10-11 20:31 | +10 | SOL | DOWN | 0.70 | yes | -7.15 |
| 10-11 20:31 | +5 | SOL | DOWN | 0.70 | yes | -7.15 |
| 10-11 20:31 | +10 stop | ETH | DOWN | 0.62 | 0.43 | -2.25 |
| 10-11 20:31 | +20 | ETH | DOWN | 0.62 | yes | -6.37 |
| 10-11 20:31 | +15 | ETH | DOWN | 0.62 | yes | -6.37 |
| 10-11 20:31 | +10 | ETH | DOWN | 0.62 | yes | -6.37 |
| 10-11 20:31 | +5 | ETH | DOWN | 0.62 | yes | -6.37 |
| 10-11 20:31 | +10 stop | DOGE | DOWN | 0.66 | 0.49 | -2.04 |
| 10-11 20:31 | +20 | DOGE | DOWN | 0.66 | yes | -6.76 |
| 10-11 20:31 | +15 | DOGE | DOWN | 0.66 | yes | -6.76 |
| 10-11 20:31 | +10 | DOGE | DOWN | 0.66 | yes | -6.76 |
| 10-11 20:31 | +5 | DOGE | DOWN | 0.66 | 0.72 | 0.29 |
| 10-11 20:31 | +10 stop | BTC | DOWN | 0.64 | 0.40 | -2.74 |
