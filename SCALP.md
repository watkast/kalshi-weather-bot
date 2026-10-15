# Range-Scalp Bot

*Updated Thu Oct 15 19:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18035 | 15655 | 2380 (28) | 0 | $-5537.23 | -4.9% |
| **+10¢** | 13625 | 10869 | 2756 (40) | 0 | $-5020.35 | -5.9% |
| **+15¢** | 11426 | 8460 | 2966 (59) | 0 | $-4544.93 | -6.3% |
| **+20¢** | 10158 | 7056 | 3102 (77) | 0 | $-3948.16 | -6.2% |
| **+10¢ (15¢ stop)** | 22195 | 22145 | 50 (29) | 0 | $-8589.79 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 19:43 | +10 stop | SOL | DOWN | 0.55 | 0.81 | 2.31 |
| 10-15 19:43 | +20 | SOL | DOWN | 0.55 | 0.81 | 2.31 |
| 10-15 19:43 | +15 | SOL | DOWN | 0.55 | 0.81 | 2.31 |
| 10-15 19:43 | +10 | SOL | DOWN | 0.55 | 0.81 | 2.31 |
| 10-15 19:43 | +5 | SOL | DOWN | 0.55 | 0.81 | 2.31 |
| 10-15 19:43 | +10 stop | ETH | DOWN | 0.69 | 0.84 | 1.25 |
| 10-15 19:43 | +20 | ETH | DOWN | 0.70 | 1.00 | 2.82 |
| 10-15 19:43 | +15 | ETH | DOWN | 0.61 | 0.77 | 1.30 |
| 10-15 19:43 | +10 | ETH | DOWN | 0.61 | 0.71 | 0.68 |
| 10-15 19:43 | +5 | ETH | DOWN | 0.71 | 0.77 | 0.32 |
| 10-15 19:42 | +10 stop | BNB | DOWN | 0.46 | 0.23 | -2.62 |
| 10-15 19:42 | +20 | BNB | DOWN | 0.46 | 0.99 | 5.06 |
| 10-15 19:42 | +15 | BNB | DOWN | 0.45 | 0.99 | 5.13 |
| 10-15 19:42 | +10 | BNB | DOWN | 0.44 | 0.99 | 5.24 |
| 10-15 19:42 | +5 | BNB | DOWN | 0.44 | 0.53 | 0.51 |
| 10-15 19:40 | +10 stop | DOGE | DOWN | 0.67 | 0.34 | -3.62 |
| 10-15 19:40 | +20 | DOGE | DOWN | 0.67 | yes | -6.86 |
| 10-15 19:40 | +15 | DOGE | DOWN | 0.67 | yes | -6.86 |
| 10-15 19:40 | +10 | DOGE | DOWN | 0.67 | yes | -6.86 |
| 10-15 19:40 | +5 | DOGE | DOWN | 0.67 | yes | -6.86 |
| 10-15 19:40 | +10 stop | NEAR | UP | 0.66 | 0.79 | 1.02 |
| 10-15 19:40 | +5 | NEAR | UP | 0.66 | 0.79 | 1.02 |
| 10-15 19:39 | +10 stop | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-15 19:39 | +20 | ZEC | DOWN | 0.64 | yes | -6.57 |
| 10-15 19:39 | +15 | ZEC | DOWN | 0.64 | yes | -6.57 |
| 10-15 19:39 | +10 | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-15 19:39 | +5 | ZEC | DOWN | 0.65 | 0.72 | 0.39 |
| 10-15 19:38 | +10 stop | NEAR | DOWN | 0.53 | 0.34 | -2.24 |
| 10-15 19:36 | +10 stop | NEAR | UP | 0.58 | 0.40 | -2.15 |
| 10-15 19:36 | +10 | NEAR | UP | 0.57 | 0.69 | 0.87 |
| 10-15 19:36 | +5 | NEAR | UP | 0.57 | 0.63 | 0.25 |
| 10-15 19:36 | +10 stop | NEAR | DOWN | 0.56 | 0.68 | 0.86 |
| 10-15 19:36 | +10 | NEAR | DOWN | 0.56 | 0.68 | 0.86 |
| 10-15 19:36 | +5 | NEAR | DOWN | 0.56 | 0.68 | 0.86 |
| 10-15 19:33 | +10 stop | ZEC | DOWN | 0.66 | 0.79 | 1.01 |
| 10-15 19:33 | +10 | ZEC | DOWN | 0.66 | 0.76 | 0.71 |
| 10-15 19:33 | +5 | ZEC | DOWN | 0.66 | 0.75 | 0.60 |
| 10-15 19:32 | +10 | BNB | DOWN | 0.60 | 0.70 | 0.68 |
| 10-15 19:32 | +5 | BNB | DOWN | 0.60 | 0.70 | 0.68 |
| 10-15 19:32 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
