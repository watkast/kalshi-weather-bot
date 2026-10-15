# Range-Scalp Bot

*Updated Thu Oct 15 17:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17899 | 15537 | 2362 (28) | 4 | $-5493.42 | -4.9% |
| **+10¢** | 13523 | 10786 | 2737 (40) | 3 | $-4994.58 | -5.9% |
| **+15¢** | 11340 | 8398 | 2942 (59) | 4 | $-4492.20 | -6.3% |
| **+20¢** | 10081 | 7003 | 3078 (77) | 4 | $-3909.93 | -6.2% |
| **+10¢ (15¢ stop)** | 22054 | 22004 | 50 (29) | 0 | $-8538.21 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 17:41 | +10 stop | SOL | DOWN | 0.69 | 0.19 | -5.26 |
| 10-15 17:41 | +20 | SOL | DOWN | 0.69 | open |  |
| 10-15 17:41 | +15 | SOL | DOWN | 0.69 | open |  |
| 10-15 17:41 | +10 | SOL | DOWN | 0.69 | open |  |
| 10-15 17:41 | +5 | SOL | DOWN | 0.69 | open |  |
| 10-15 17:41 | +10 stop | BNB | UP | 0.57 | 0.67 | 0.66 |
| 10-15 17:40 | +10 stop | XRP | DOWN | 0.51 | 0.31 | -2.34 |
| 10-15 17:40 | +10 stop | BTC | UP | 0.63 | 0.73 | 0.69 |
| 10-15 17:40 | +10 | SOL | DOWN | 0.61 | 0.77 | 1.30 |
| 10-15 17:40 | +5 | SOL | DOWN | 0.61 | 0.67 | 0.27 |
| 10-15 17:39 | +5 | BNB | DOWN | 0.63 | open |  |
| 10-15 17:38 | +10 stop | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 10-15 17:38 | +20 | DOGE | UP | 0.69 | 0.96 | 2.53 |
| 10-15 17:38 | +15 | DOGE | UP | 0.69 | 0.86 | 1.46 |
| 10-15 17:38 | +10 | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 10-15 17:38 | +10 stop | SOL | DOWN | 0.62 | 0.77 | 1.20 |
| 10-15 17:38 | +10 stop | BTC | UP | 0.50 | 0.63 | 0.95 |
| 10-15 17:38 | +10 stop | ETH | UP | 0.65 | 0.80 | 1.22 |
| 10-15 17:38 | +20 | ETH | UP | 0.65 | 0.85 | 1.75 |
| 10-15 17:38 | +15 | ETH | UP | 0.64 | 0.80 | 1.31 |
| 10-15 17:38 | +10 | ETH | UP | 0.64 | 0.80 | 1.31 |
| 10-15 17:38 | +5 | ETH | UP | 0.64 | 0.80 | 1.31 |
| 10-15 17:37 | +10 stop | BNB | DOWN | 0.61 | 0.45 | -1.95 |
| 10-15 17:37 | +10 stop | XRP | DOWN | 0.58 | 0.42 | -1.96 |
| 10-15 17:36 | +10 stop | SOL | UP | 0.59 | 0.39 | -2.34 |
| 10-15 17:36 | +10 stop | BTC | UP | 0.70 | 0.55 | -1.83 |
| 10-15 17:36 | +10 stop | XRP | UP | 0.69 | 0.54 | -1.83 |
| 10-15 17:36 | +10 | XRP | UP | 0.67 | 0.98 | 2.97 |
| 10-15 17:36 | +5 | XRP | UP | 0.65 | 0.72 | 0.40 |
| 10-15 17:35 | +5 | NEAR | UP | 0.71 | 0.77 | 0.32 |
| 10-15 17:34 | +10 | XRP | DOWN | 0.57 | 0.69 | 0.87 |
| 10-15 17:34 | +10 stop | NEAR | UP | 0.64 | 0.77 | 1.00 |
| 10-15 17:34 | +15 | NEAR | UP | 0.64 | 0.81 | 1.42 |
| 10-15 17:34 | +10 | NEAR | UP | 0.64 | 0.77 | 1.00 |
| 10-15 17:34 | +5 | NEAR | UP | 0.64 | 0.73 | 0.59 |
| 10-15 17:34 | +10 stop | SOL | DOWN | 0.59 | 0.31 | -3.12 |
| 10-15 17:34 | +10 stop | ETH | UP | 0.68 | 0.87 | 1.66 |
| 10-15 17:34 | +20 | ETH | UP | 0.67 | 0.87 | 1.76 |
| 10-15 17:34 | +15 | ETH | UP | 0.67 | 0.87 | 1.76 |
| 10-15 17:34 | +10 | ETH | UP | 0.67 | 0.77 | 0.71 |
