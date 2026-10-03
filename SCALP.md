# Range-Scalp Bot

*Updated Sat Oct 03 14:48 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 898 | 784 | 114 (2) | 0 | $-241.52 | -4.2% |
| **+10¢** | 683 | 558 | 125 (4) | 0 | $-127.47 | -3.0% |
| **+15¢** | 578 | 442 | 136 (5) | 1 | $-113.52 | -3.1% |
| **+20¢** | 505 | 362 | 143 (5) | 2 | $-106.91 | -3.4% |
| **+10¢ (15¢ stop)** | 1137 | 1136 | 1 (1) | 0 | $-561.27 | -7.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 14:46 | +10 stop | BNB | UP | 0.60 | 0.73 | 0.94 |
| 10-03 14:46 | +20 | BNB | UP | 0.60 | open |  |
| 10-03 14:46 | +15 | BNB | UP | 0.60 | open |  |
| 10-03 14:46 | +10 | BNB | UP | 0.60 | 0.73 | 0.94 |
| 10-03 14:46 | +5 | BNB | UP | 0.60 | 0.69 | 0.53 |
| 10-03 14:45 | +10 stop | SOL | UP | 0.70 | 0.82 | 0.94 |
| 10-03 14:45 | +20 | SOL | UP | 0.70 | open |  |
| 10-03 14:45 | +15 | SOL | UP | 0.70 | 0.85 | 1.26 |
| 10-03 14:45 | +10 | SOL | UP | 0.70 | 0.82 | 0.94 |
| 10-03 14:45 | +5 | SOL | UP | 0.70 | 0.77 | 0.42 |
| 10-03 14:42 | +5 | DOGE | UP | 0.56 | 0.65 | 0.51 |
| 10-03 14:41 | +10 stop | DOGE | UP | 0.56 | 0.69 | 0.97 |
| 10-03 14:41 | +10 stop | XRP | UP | 0.62 | 0.73 | 0.79 |
| 10-03 14:41 | +15 | XRP | UP | 0.62 | 0.83 | 1.83 |
| 10-03 14:41 | +10 | XRP | UP | 0.63 | 0.73 | 0.70 |
| 10-03 14:41 | +5 | XRP | UP | 0.63 | 0.69 | 0.28 |
| 10-03 14:40 | +10 stop | BNB | UP | 0.31 | 0.63 | 2.90 |
| 10-03 14:40 | +5 | NEAR | UP | 0.68 | 0.77 | 0.62 |
| 10-03 14:39 | +10 stop | NEAR | UP | 0.60 | 0.77 | 1.40 |
| 10-03 14:39 | +10 stop | XRP | DOWN | 0.50 | 0.62 | 0.85 |
| 10-03 14:39 | +15 | XRP | DOWN | 0.50 | 0.71 | 1.77 |
| 10-03 14:39 | +10 | XRP | DOWN | 0.49 | 0.62 | 0.95 |
| 10-03 14:39 | +5 | XRP | DOWN | 0.49 | 0.62 | 0.94 |
| 10-03 14:39 | +10 stop | BNB | UP | 0.67 | 0.46 | -2.39 |
| 10-03 14:39 | +10 | BNB | UP | 0.67 | 0.94 | 2.57 |
| 10-03 14:39 | +5 | BNB | UP | 0.67 | 0.94 | 2.57 |
| 10-03 14:38 | +10 stop | ZEC | UP | 0.67 | 0.77 | 0.71 |
| 10-03 14:38 | +15 | ZEC | UP | 0.67 | 0.84 | 1.44 |
| 10-03 14:38 | +10 | ZEC | UP | 0.67 | 0.77 | 0.71 |
| 10-03 14:38 | +5 | ZEC | UP | 0.67 | 0.77 | 0.71 |
| 10-03 14:38 | +10 stop | NEAR | DOWN | 0.55 | 0.40 | -1.85 |
| 10-03 14:36 | +10 stop | NEAR | DOWN | 0.68 | 0.50 | -2.14 |
| 10-03 14:36 | +5 | NEAR | UP | 0.62 | 0.68 | 0.27 |
| 10-03 14:35 | +10 stop | XRP | DOWN | 0.67 | 0.77 | 0.71 |
| 10-03 14:35 | +10 stop | ETH | DOWN | 0.63 | 0.85 | 1.94 |
| 10-03 14:34 | +10 stop | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 10-03 14:34 | +5 | BNB | UP | 0.70 | 0.79 | 0.60 |
| 10-03 14:34 | +5 | DOGE | UP | 0.57 | 0.64 | 0.30 |
| 10-03 14:34 | +10 stop | ETH | UP | 0.46 | 0.57 | 0.74 |
| 10-03 14:33 | +10 stop | SOL | DOWN | 0.54 | 0.64 | 0.65 |
