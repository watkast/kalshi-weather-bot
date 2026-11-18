# Range-Scalp Bot

*Updated Wed Nov 18 02:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63500 | 55379 | 8121 (118) | 1 | $-17376.07 | -4.3% |
| **+10¢** | 47436 | 37931 | 9505 (159) | 1 | $-16302.40 | -5.5% |
| **+15¢** | 39774 | 29525 | 10249 (203) | 1 | $-14790.60 | -5.9% |
| **+20¢** | 35431 | 24675 | 10756 (258) | 1 | $-13058.22 | -5.9% |
| **+10¢ (15¢ stop)** | 77278 | 77120 | 158 (93) | 0 | $-28438.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 02:55 | +10 stop | XRP | DOWN | 0.71 | 0.31 | -4.30 |
| 11-18 02:55 | +20 | XRP | DOWN | 0.71 | open |  |
| 11-18 02:55 | +15 | XRP | DOWN | 0.71 | open |  |
| 11-18 02:55 | +10 | XRP | DOWN | 0.71 | open |  |
| 11-18 02:55 | +5 | XRP | DOWN | 0.71 | open |  |
| 11-18 02:53 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 11-18 02:51 | +10 stop | XRP | DOWN | 0.69 | 0.54 | -1.83 |
| 11-18 02:51 | +15 | XRP | DOWN | 0.69 | 0.87 | 1.53 |
| 11-18 02:51 | +10 | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 11-18 02:51 | +5 | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 11-18 02:49 | +10 stop | XRP | DOWN | 0.62 | 0.77 | 1.20 |
| 11-18 02:49 | +20 | XRP | DOWN | 0.61 | 0.81 | 1.72 |
| 11-18 02:49 | +15 | XRP | DOWN | 0.61 | 0.77 | 1.30 |
| 11-18 02:49 | +10 | XRP | DOWN | 0.61 | 0.77 | 1.30 |
| 11-18 02:49 | +5 | XRP | DOWN | 0.60 | 0.68 | 0.47 |
| 11-18 02:46 | +10 stop | NEAR | DOWN | 0.66 | 0.76 | 0.71 |
| 11-18 02:46 | +20 | NEAR | DOWN | 0.66 | 0.87 | 1.86 |
| 11-18 02:46 | +15 | NEAR | DOWN | 0.66 | 0.81 | 1.23 |
| 11-18 02:46 | +10 | NEAR | DOWN | 0.66 | 0.76 | 0.71 |
| 11-18 02:46 | +5 | NEAR | DOWN | 0.66 | 0.76 | 0.71 |
| 11-18 02:46 | +10 stop | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-18 02:46 | +20 | HYPE | DOWN | 0.69 | 0.89 | 1.78 |
| 11-18 02:46 | +15 | HYPE | DOWN | 0.69 | 0.85 | 1.36 |
| 11-18 02:46 | +10 | HYPE | DOWN | 0.71 | 0.81 | 0.76 |
| 11-18 02:46 | +5 | HYPE | DOWN | 0.69 | 0.75 | 0.31 |
| 11-18 02:46 | +10 stop | ZEC | DOWN | 0.65 | 0.79 | 1.12 |
| 11-18 02:46 | +20 | ZEC | DOWN | 0.65 | 0.85 | 1.75 |
| 11-18 02:46 | +15 | ZEC | DOWN | 0.64 | 0.79 | 1.21 |
| 11-18 02:46 | +10 | ZEC | DOWN | 0.64 | 0.79 | 1.21 |
| 11-18 02:46 | +5 | ZEC | DOWN | 0.64 | 0.71 | 0.38 |
| 11-18 02:46 | +10 stop | BNB | DOWN | 0.69 | 0.80 | 0.83 |
| 11-18 02:46 | +20 | BNB | DOWN | 0.68 | 0.89 | 1.87 |
| 11-18 02:46 | +15 | BNB | DOWN | 0.68 | 0.87 | 1.66 |
| 11-18 02:46 | +10 | BNB | DOWN | 0.68 | 0.80 | 0.92 |
| 11-18 02:46 | +5 | BNB | DOWN | 0.68 | 0.80 | 0.92 |
| 11-18 02:46 | +10 stop | BTC | DOWN | 0.69 | 0.83 | 1.15 |
| 11-18 02:46 | +20 | BTC | DOWN | 0.69 | 0.90 | 1.89 |
| 11-18 02:46 | +15 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 11-18 02:46 | +10 | BTC | DOWN | 0.69 | 0.83 | 1.15 |
| 11-18 02:46 | +5 | BTC | DOWN | 0.69 | 0.75 | 0.31 |
