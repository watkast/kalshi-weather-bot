# Range-Scalp Bot

*Updated Sat Oct 03 17:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 1060 | 927 | 133 (2) | 4 | $-282.07 | -4.2% |
| **+10¢** | 806 | 663 | 143 (4) | 5 | $-130.10 | -2.6% |
| **+15¢** | 682 | 527 | 155 (5) | 5 | $-98.84 | -2.3% |
| **+20¢** | 600 | 436 | 164 (5) | 5 | $-85.25 | -2.3% |
| **+10¢ (15¢ stop)** | 1341 | 1340 | 1 (1) | 3 | $-616.10 | -7.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 17:39 | +10 stop | BTC | UP | 0.68 | open |  |
| 10-03 17:39 | +10 stop | BNB | UP | 0.61 | open |  |
| 10-03 17:39 | +15 | BNB | UP | 0.61 | open |  |
| 10-03 17:39 | +10 | BNB | UP | 0.61 | open |  |
| 10-03 17:39 | +5 | BNB | UP | 0.61 | open |  |
| 10-03 17:39 | +10 stop | BTC | DOWN | 0.49 | 0.59 | 0.65 |
| 10-03 17:38 | +10 stop | ETH | UP | 0.57 | open |  |
| 10-03 17:38 | +10 stop | ZEC | UP | 0.41 | 0.53 | 0.80 |
| 10-03 17:38 | +10 stop | BNB | DOWN | 0.65 | 0.79 | 1.08 |
| 10-03 17:38 | +20 | BNB | DOWN | 0.65 | open |  |
| 10-03 17:38 | +15 | BNB | DOWN | 0.65 | 0.81 | 1.29 |
| 10-03 17:38 | +10 | BNB | DOWN | 0.65 | 0.79 | 1.08 |
| 10-03 17:38 | +5 | BNB | DOWN | 0.66 | 0.74 | 0.50 |
| 10-03 17:37 | +10 stop | HYPE | UP | 0.68 | 0.51 | -2.04 |
| 10-03 17:36 | +10 stop | ZEC | DOWN | 0.62 | 0.41 | -2.44 |
| 10-03 17:36 | +20 | ZEC | DOWN | 0.62 | 0.82 | 1.72 |
| 10-03 17:36 | +15 | ZEC | DOWN | 0.62 | 0.77 | 1.20 |
| 10-03 17:36 | +10 | ZEC | DOWN | 0.62 | 0.77 | 1.20 |
| 10-03 17:36 | +5 | ZEC | DOWN | 0.62 | 0.69 | 0.38 |
| 10-03 17:36 | +10 stop | ETH | DOWN | 0.66 | 0.46 | -2.34 |
| 10-03 17:36 | +20 | ETH | DOWN | 0.66 | open |  |
| 10-03 17:36 | +15 | ETH | DOWN | 0.66 | open |  |
| 10-03 17:36 | +10 | ETH | DOWN | 0.66 | open |  |
| 10-03 17:36 | +5 | ETH | DOWN | 0.66 | open |  |
| 10-03 17:35 | +10 stop | HYPE | UP | 0.71 | 0.52 | -2.20 |
| 10-03 17:35 | +5 | HYPE | UP | 0.71 | 0.83 | 0.98 |
| 10-03 17:35 | +10 stop | BTC | DOWN | 0.68 | 0.38 | -3.33 |
| 10-03 17:35 | +20 | BTC | DOWN | 0.68 | open |  |
| 10-03 17:35 | +15 | BTC | DOWN | 0.68 | open |  |
| 10-03 17:35 | +10 | BTC | DOWN | 0.68 | open |  |
| 10-03 17:35 | +5 | BTC | DOWN | 0.68 | open |  |
| 10-03 17:35 | +10 stop | SOL | UP | 0.62 | 0.73 | 0.79 |
| 10-03 17:34 | +10 stop | SOL | DOWN | 0.44 | 0.56 | 0.84 |
| 10-03 17:34 | +5 | HYPE | DOWN | 0.58 | 0.63 | 0.15 |
| 10-03 17:33 | +10 stop | HYPE | DOWN | 0.68 | 0.52 | -1.94 |
| 10-03 17:33 | +20 | HYPE | DOWN | 0.68 | open |  |
| 10-03 17:33 | +15 | HYPE | DOWN | 0.68 | open |  |
| 10-03 17:33 | +10 | HYPE | DOWN | 0.68 | open |  |
| 10-03 17:33 | +5 | HYPE | DOWN | 0.68 | 0.74 | 0.30 |
| 10-03 17:33 | +10 stop | SOL | UP | 0.60 | 0.40 | -2.34 |
