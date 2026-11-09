# Range-Scalp Bot

*Updated Mon Nov 09 05:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53385 | 46547 | 6838 (85) | 1 | $-14752.00 | -4.4% |
| **+10¢** | 39877 | 31901 | 7976 (110) | 2 | $-13752.52 | -5.5% |
| **+15¢** | 33411 | 24817 | 8594 (141) | 4 | $-12555.57 | -6.0% |
| **+20¢** | 29730 | 20720 | 9010 (186) | 4 | $-11038.99 | -5.9% |
| **+10¢ (15¢ stop)** | 65051 | 64945 | 106 (63) | 0 | $-24125.89 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 05:55 | +10 stop | SOL | DOWN | 0.63 | 0.79 | 1.31 |
| 11-09 05:55 | +10 stop | ZEC | DOWN | 0.69 | 0.88 | 1.67 |
| 11-09 05:55 | +10 | ZEC | DOWN | 0.69 | 0.88 | 1.67 |
| 11-09 05:55 | +5 | ZEC | DOWN | 0.69 | 0.88 | 1.67 |
| 11-09 05:54 | +10 stop | ZEC | DOWN | 0.53 | 0.67 | 1.02 |
| 11-09 05:54 | +10 | ZEC | DOWN | 0.53 | 0.67 | 1.02 |
| 11-09 05:54 | +5 | ZEC | DOWN | 0.53 | 0.67 | 1.08 |
| 11-09 05:53 | +10 stop | ETH | UP | 0.71 | 0.81 | 0.74 |
| 11-09 05:53 | +20 | ETH | UP | 0.71 | 0.94 | 2.13 |
| 11-09 05:53 | +15 | ETH | UP | 0.71 | 0.87 | 1.37 |
| 11-09 05:53 | +10 | ETH | UP | 0.71 | 0.81 | 0.74 |
| 11-09 05:53 | +5 | ETH | UP | 0.71 | 0.77 | 0.32 |
| 11-09 05:53 | +10 stop | XRP | DOWN | 0.60 | 0.24 | -3.87 |
| 11-09 05:53 | +15 | XRP | DOWN | 0.60 | open |  |
| 11-09 05:53 | +10 | XRP | DOWN | 0.60 | 0.70 | 0.69 |
| 11-09 05:53 | +5 | XRP | DOWN | 0.60 | 0.70 | 0.69 |
| 11-09 05:53 | +10 stop | SOL | DOWN | 0.67 | 0.52 | -1.84 |
| 11-09 05:53 | +20 | SOL | DOWN | 0.65 | 0.86 | 1.85 |
| 11-09 05:53 | +15 | SOL | DOWN | 0.65 | 0.86 | 1.85 |
| 11-09 05:53 | +10 | SOL | DOWN | 0.65 | 0.79 | 1.12 |
| 11-09 05:53 | +5 | SOL | DOWN | 0.65 | 0.79 | 1.12 |
| 11-09 05:53 | +10 stop | DOGE | UP | 0.61 | 0.71 | 0.68 |
| 11-09 05:53 | +20 | DOGE | UP | 0.61 | 0.81 | 1.72 |
| 11-09 05:53 | +15 | DOGE | UP | 0.61 | 0.81 | 1.72 |
| 11-09 05:53 | +10 | DOGE | UP | 0.61 | 0.71 | 0.68 |
| 11-09 05:53 | +5 | DOGE | UP | 0.61 | 0.71 | 0.69 |
| 11-09 05:52 | +10 stop | HYPE | UP | 0.41 | 0.60 | 1.56 |
| 11-09 05:51 | +10 stop | NEAR | UP | 0.66 | 0.38 | -3.13 |
| 11-09 05:51 | +15 | NEAR | UP | 0.66 | open |  |
| 11-09 05:51 | +10 | NEAR | UP | 0.66 | open |  |
| 11-09 05:51 | +5 | NEAR | UP | 0.66 | 0.72 | 0.29 |
| 11-09 05:50 | +10 stop | ZEC | UP | 0.55 | 0.74 | 1.58 |
| 11-09 05:50 | +10 | ZEC | UP | 0.55 | 0.74 | 1.58 |
| 11-09 05:50 | +5 | ZEC | UP | 0.55 | 0.74 | 1.58 |
| 11-09 05:50 | +10 stop | HYPE | UP | 0.56 | 0.69 | 0.95 |
| 11-09 05:47 | +5 | SOL | UP | 0.62 | 0.70 | 0.48 |
| 11-09 05:47 | +5 | BNB | UP | 0.67 | 0.75 | 0.50 |
| 11-09 05:47 | +10 stop | ETH | UP | 0.70 | 0.84 | 1.15 |
| 11-09 05:47 | +10 | ETH | UP | 0.70 | 0.84 | 1.15 |
| 11-09 05:47 | +5 | ETH | UP | 0.66 | 0.77 | 0.81 |
