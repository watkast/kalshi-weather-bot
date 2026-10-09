# Range-Scalp Bot

*Updated Fri Oct 09 02:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8343 | 7219 | 1124 (13) | 0 | $-2702.03 | -5.1% |
| **+10¢** | 6327 | 4999 | 1328 (25) | 0 | $-2648.23 | -6.6% |
| **+15¢** | 5337 | 3939 | 1398 (37) | 1 | $-2142.68 | -6.4% |
| **+20¢** | 4750 | 3300 | 1450 (45) | 1 | $-1750.27 | -5.9% |
| **+10¢ (15¢ stop)** | 10132 | 10102 | 30 (19) | 0 | $-3726.11 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 01:56 | +10 stop | BTC | DOWN | 0.60 | 0.74 | 1.09 |
| 10-09 01:56 | +5 | BTC | DOWN | 0.60 | 0.67 | 0.37 |
| 10-09 01:56 | +10 stop | NEAR | DOWN | 0.33 | 0.57 | 2.06 |
| 10-09 01:56 | +20 | NEAR | DOWN | 0.33 | 0.57 | 2.06 |
| 10-09 01:56 | +15 | NEAR | DOWN | 0.33 | 0.57 | 2.06 |
| 10-09 01:56 | +10 | NEAR | DOWN | 0.33 | 0.57 | 2.06 |
| 10-09 01:56 | +5 | NEAR | DOWN | 0.33 | 0.57 | 2.06 |
| 10-09 01:55 | +5 | BTC | DOWN | 0.60 | 0.76 | 1.30 |
| 10-09 01:55 | +10 stop | ZEC | UP | 0.65 | 0.79 | 1.12 |
| 10-09 01:55 | +10 | ZEC | UP | 0.65 | 0.79 | 1.12 |
| 10-09 01:55 | +5 | ZEC | UP | 0.65 | 0.79 | 1.12 |
| 10-09 01:55 | +10 stop | BTC | DOWN | 0.58 | 0.76 | 1.49 |
| 10-09 01:55 | +5 | BTC | DOWN | 0.58 | 0.65 | 0.36 |
| 10-09 01:53 | +10 stop | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 10-09 01:53 | +10 | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 10-09 01:53 | +5 | ETH | DOWN | 0.69 | 0.75 | 0.31 |
| 10-09 01:51 | +10 stop | ZEC | DOWN | 0.60 | 0.72 | 0.88 |
| 10-09 01:51 | +15 | ZEC | DOWN | 0.60 | open |  |
| 10-09 01:51 | +10 | ZEC | DOWN | 0.60 | 0.72 | 0.88 |
| 10-09 01:51 | +5 | ZEC | DOWN | 0.59 | 0.65 | 0.27 |
| 10-09 01:51 | +10 stop | BTC | DOWN | 0.60 | 0.75 | 1.19 |
| 10-09 01:51 | +10 stop | SOL | DOWN | 0.63 | 0.78 | 1.19 |
| 10-09 01:51 | +15 | SOL | DOWN | 0.63 | 0.82 | 1.61 |
| 10-09 01:51 | +10 | SOL | DOWN | 0.63 | 0.78 | 1.19 |
| 10-09 01:51 | +5 | SOL | DOWN | 0.64 | 0.78 | 1.10 |
| 10-09 01:51 | +10 stop | NEAR | DOWN | 0.59 | 0.70 | 0.78 |
| 10-09 01:51 | +15 | NEAR | DOWN | 0.60 | 0.76 | 1.30 |
| 10-09 01:51 | +10 | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
| 10-09 01:51 | +5 | NEAR | DOWN | 0.61 | 0.70 | 0.57 |
| 10-09 01:50 | +10 stop | ZEC | UP | 0.56 | 0.74 | 1.46 |
| 10-09 01:50 | +15 | ZEC | UP | 0.56 | 0.74 | 1.46 |
| 10-09 01:50 | +10 | ZEC | UP | 0.56 | 0.74 | 1.46 |
| 10-09 01:50 | +5 | ZEC | UP | 0.56 | 0.74 | 1.46 |
| 10-09 01:49 | +10 stop | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 10-09 01:49 | +15 | ETH | DOWN | 0.58 | 0.75 | 1.38 |
| 10-09 01:49 | +10 | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 10-09 01:49 | +5 | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 10-09 01:49 | +10 stop | BTC | DOWN | 0.70 | 0.55 | -1.83 |
| 10-09 01:49 | +15 | BTC | DOWN | 0.70 | 0.90 | 1.78 |
| 10-09 01:49 | +10 | BTC | DOWN | 0.70 | 0.90 | 1.78 |
