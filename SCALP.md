# Range-Scalp Bot

*Updated Sat Oct 03 16:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 969 | 847 | 122 (2) | 0 | $-257.88 | -4.2% |
| **+10¢** | 734 | 601 | 133 (4) | 1 | $-131.68 | -2.8% |
| **+15¢** | 620 | 477 | 143 (5) | 1 | $-102.81 | -2.6% |
| **+20¢** | 543 | 393 | 150 (5) | 2 | $-87.95 | -2.6% |
| **+10¢ (15¢ stop)** | 1222 | 1221 | 1 (1) | 0 | $-577.22 | -7.5% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 16:04 | +10 stop | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-03 16:04 | +5 | DOGE | DOWN | 0.66 | 0.71 | 0.19 |
| 10-03 16:04 | +10 stop | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-03 16:04 | +15 | HYPE | DOWN | 0.67 | 0.82 | 1.23 |
| 10-03 16:04 | +10 | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-03 16:04 | +5 | HYPE | DOWN | 0.67 | 0.72 | 0.19 |
| 10-03 16:04 | +10 stop | NEAR | DOWN | 0.57 | 0.71 | 1.07 |
| 10-03 16:04 | +10 | NEAR | DOWN | 0.57 | 0.71 | 1.07 |
| 10-03 16:04 | +5 | NEAR | DOWN | 0.57 | 0.62 | 0.15 |
| 10-03 16:04 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-03 16:04 | +20 | SOL | DOWN | 0.70 | open |  |
| 10-03 16:04 | +15 | SOL | DOWN | 0.70 | 0.86 | 1.36 |
| 10-03 16:04 | +10 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-03 16:04 | +5 | SOL | DOWN | 0.71 | 0.77 | 0.32 |
| 10-03 16:03 | +5 | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-03 16:02 | +10 stop | ZEC | DOWN | 0.57 | 0.70 | 0.93 |
| 10-03 16:02 | +20 | ZEC | DOWN | 0.57 | 0.79 | 1.90 |
| 10-03 16:02 | +15 | ZEC | DOWN | 0.57 | 0.75 | 1.48 |
| 10-03 16:02 | +10 | ZEC | DOWN | 0.58 | 0.70 | 0.87 |
| 10-03 16:02 | +5 | ZEC | DOWN | 0.58 | 0.70 | 0.87 |
| 10-03 16:02 | +10 stop | BTC | DOWN | 0.68 | 0.80 | 0.92 |
| 10-03 16:02 | +20 | BTC | DOWN | 0.68 | 0.89 | 1.87 |
| 10-03 16:02 | +15 | BTC | DOWN | 0.67 | 0.85 | 1.55 |
| 10-03 16:02 | +10 | BTC | DOWN | 0.67 | 0.80 | 1.02 |
| 10-03 16:02 | +5 | BTC | DOWN | 0.67 | 0.76 | 0.61 |
| 10-03 16:02 | +10 stop | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-03 16:02 | +20 | HYPE | DOWN | 0.63 | 0.83 | 1.73 |
| 10-03 16:02 | +15 | HYPE | DOWN | 0.63 | 0.78 | 1.20 |
| 10-03 16:02 | +10 | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-03 16:02 | +5 | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-03 16:02 | +10 stop | NEAR | DOWN | 0.60 | 0.73 | 0.99 |
| 10-03 16:02 | +20 | NEAR | DOWN | 0.60 | 0.84 | 2.13 |
| 10-03 16:02 | +15 | NEAR | DOWN | 0.60 | 0.77 | 1.40 |
| 10-03 16:02 | +10 | NEAR | DOWN | 0.60 | 0.73 | 0.99 |
| 10-03 16:02 | +5 | NEAR | DOWN | 0.60 | 0.65 | 0.17 |
| 10-03 16:01 | +5 | DOGE | DOWN | 0.68 | 0.73 | 0.20 |
| 10-03 16:01 | +10 stop | BNB | DOWN | 0.60 | 0.75 | 1.19 |
| 10-03 16:01 | +20 | BNB | DOWN | 0.61 | 0.82 | 1.82 |
| 10-03 16:01 | +15 | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-03 16:01 | +10 | BNB | DOWN | 0.62 | 0.75 | 0.99 |
