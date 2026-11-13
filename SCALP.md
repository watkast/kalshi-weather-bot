# Range-Scalp Bot

*Updated Fri Nov 13 10:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58159 | 50751 | 7408 (102) | 1 | $-15670.46 | -4.3% |
| **+10¢** | 43451 | 34788 | 8663 (134) | 3 | $-14647.59 | -5.4% |
| **+15¢** | 36426 | 27098 | 9328 (168) | 3 | $-13214.99 | -5.8% |
| **+20¢** | 32454 | 22662 | 9792 (219) | 4 | $-11576.84 | -5.7% |
| **+10¢ (15¢ stop)** | 70855 | 70726 | 129 (79) | 0 | $-26029.08 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 10:43 | +10 stop | BNB | UP | 0.60 | 0.85 | 2.19 |
| 11-13 10:43 | +5 | BNB | UP | 0.61 | 0.85 | 2.14 |
| 11-13 10:42 | +10 stop | SOL | UP | 0.33 | 0.54 | 1.76 |
| 11-13 10:42 | +20 | SOL | UP | 0.34 | 0.54 | 1.66 |
| 11-13 10:42 | +15 | SOL | UP | 0.34 | 0.54 | 1.66 |
| 11-13 10:42 | +10 | SOL | UP | 0.36 | 0.54 | 1.45 |
| 11-13 10:42 | +5 | SOL | UP | 0.36 | 0.54 | 1.45 |
| 11-13 10:41 | +10 stop | BNB | DOWN | 0.70 | 0.36 | -3.72 |
| 11-13 10:40 | +10 stop | BNB | DOWN | 0.61 | 0.73 | 0.89 |
| 11-13 10:40 | +10 stop | BTC | UP | 0.54 | 0.64 | 0.65 |
| 11-13 10:38 | +10 stop | BNB | UP | 0.67 | 0.49 | -2.14 |
| 11-13 10:38 | +5 | BNB | UP | 0.67 | 0.84 | 1.44 |
| 11-13 10:38 | +10 | NEAR | DOWN | 0.63 | 0.73 | 0.69 |
| 11-13 10:38 | +5 | BNB | DOWN | 0.45 | 0.63 | 1.45 |
| 11-13 10:38 | +5 | NEAR | DOWN | 0.64 | 0.69 | 0.18 |
| 11-13 10:37 | +10 stop | NEAR | DOWN | 0.59 | 0.69 | 0.68 |
| 11-13 10:37 | +20 | NEAR | DOWN | 0.58 | 0.78 | 1.69 |
| 11-13 10:37 | +15 | NEAR | DOWN | 0.58 | 0.73 | 1.18 |
| 11-13 10:37 | +10 | NEAR | DOWN | 0.58 | 0.68 | 0.66 |
| 11-13 10:37 | +5 | NEAR | DOWN | 0.58 | 0.67 | 0.56 |
| 11-13 10:37 | +10 stop | BNB | DOWN | 0.68 | 0.43 | -2.83 |
| 11-13 10:37 | +20 | BNB | DOWN | 0.68 | open |  |
| 11-13 10:37 | +15 | BNB | DOWN | 0.68 | open |  |
| 11-13 10:37 | +10 | BNB | DOWN | 0.67 | open |  |
| 11-13 10:37 | +5 | BNB | DOWN | 0.67 | 0.74 | 0.40 |
| 11-13 10:37 | +10 stop | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-13 10:37 | +20 | ZEC | DOWN | 0.68 | open |  |
| 11-13 10:37 | +10 | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-13 10:37 | +5 | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-13 10:36 | +10 stop | BTC | UP | 0.65 | 0.77 | 0.91 |
| 11-13 10:36 | +5 | ETH | DOWN | 0.34 | 0.68 | 3.08 |
| 11-13 10:35 | +10 stop | BTC | DOWN | 0.62 | 0.44 | -2.15 |
| 11-13 10:34 | +15 | ZEC | DOWN | 0.66 | 0.82 | 1.33 |
| 11-13 10:33 | +10 stop | DOGE | DOWN | 0.61 | 0.72 | 0.78 |
| 11-13 10:33 | +15 | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 11-13 10:33 | +10 | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-13 10:33 | +5 | DOGE | DOWN | 0.65 | 0.70 | 0.19 |
| 11-13 10:33 | +5 | ETH | DOWN | 0.59 | 0.68 | 0.57 |
| 11-13 10:32 | +10 stop | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-13 10:32 | +10 | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
