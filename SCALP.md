# Range-Scalp Bot

*Updated Sat Oct 24 15:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32164 | 28041 | 4123 (40) | 0 | $-9210.71 | -4.5% |
| **+10¢** | 24079 | 19307 | 4772 (58) | 0 | $-8234.61 | -5.4% |
| **+15¢** | 20162 | 15029 | 5133 (81) | 0 | $-7376.61 | -5.8% |
| **+20¢** | 17863 | 12490 | 5373 (103) | 0 | $-6544.41 | -5.8% |
| **+10¢ (15¢ stop)** | 39537 | 39478 | 59 (32) | 0 | $-15143.87 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 15:23 | +10 stop | HYPE | DOWN | 0.56 | 0.69 | 0.97 |
| 10-24 15:22 | +10 stop | NEAR | DOWN | 0.56 | 0.71 | 1.17 |
| 10-24 15:22 | +10 stop | ZEC | DOWN | 0.67 | 0.82 | 1.23 |
| 10-24 15:22 | +20 | ZEC | DOWN | 0.67 | 0.88 | 1.86 |
| 10-24 15:22 | +15 | ZEC | DOWN | 0.67 | 0.82 | 1.23 |
| 10-24 15:22 | +10 | ZEC | DOWN | 0.67 | 0.82 | 1.23 |
| 10-24 15:22 | +5 | ZEC | DOWN | 0.68 | 0.75 | 0.40 |
| 10-24 15:22 | +10 stop | HYPE | DOWN | 0.68 | 0.50 | -2.14 |
| 10-24 15:22 | +15 | HYPE | DOWN | 0.69 | 0.87 | 1.57 |
| 10-24 15:22 | +10 | HYPE | DOWN | 0.68 | 0.83 | 1.24 |
| 10-24 15:22 | +5 | HYPE | DOWN | 0.68 | 0.83 | 1.24 |
| 10-24 15:21 | +10 stop | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-24 15:21 | +20 | XRP | DOWN | 0.64 | 0.91 | 2.48 |
| 10-24 15:21 | +15 | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-24 15:21 | +10 | XRP | DOWN | 0.65 | 0.79 | 1.12 |
| 10-24 15:21 | +5 | XRP | DOWN | 0.65 | 0.72 | 0.39 |
| 10-24 15:21 | +20 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 10-24 15:21 | +15 | NEAR | DOWN | 0.67 | 0.85 | 1.55 |
| 10-24 15:21 | +5 | NEAR | DOWN | 0.67 | 0.74 | 0.40 |
| 10-24 15:19 | +10 | HYPE | DOWN | 0.56 | 0.77 | 1.79 |
| 10-24 15:18 | +15 | NEAR | DOWN | 0.61 | 0.76 | 1.20 |
| 10-24 15:18 | +10 | HYPE | DOWN | 0.54 | 0.66 | 0.86 |
| 10-24 15:18 | +10 stop | NEAR | DOWN | 0.67 | 0.51 | -1.94 |
| 10-24 15:18 | +10 | NEAR | DOWN | 0.67 | 0.80 | 1.02 |
| 10-24 15:18 | +5 | NEAR | DOWN | 0.67 | 0.75 | 0.50 |
| 10-24 15:17 | +5 | HYPE | DOWN | 0.70 | 0.77 | 0.42 |
| 10-24 15:17 | +10 stop | HYPE | DOWN | 0.62 | 0.77 | 1.20 |
| 10-24 15:17 | +20 | HYPE | DOWN | 0.62 | 0.83 | 1.79 |
| 10-24 15:17 | +15 | HYPE | DOWN | 0.63 | 0.79 | 1.31 |
| 10-24 15:17 | +10 | HYPE | DOWN | 0.60 | 0.71 | 0.76 |
| 10-24 15:17 | +5 | HYPE | DOWN | 0.60 | 0.66 | 0.25 |
| 10-24 15:17 | +10 stop | NEAR | DOWN | 0.50 | 0.62 | 0.85 |
| 10-24 15:17 | +20 | NEAR | DOWN | 0.50 | 0.75 | 2.18 |
| 10-24 15:17 | +15 | NEAR | DOWN | 0.50 | 0.66 | 1.26 |
| 10-24 15:17 | +10 | NEAR | DOWN | 0.51 | 0.62 | 0.75 |
| 10-24 15:17 | +5 | NEAR | DOWN | 0.51 | 0.62 | 0.75 |
| 10-24 15:16 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-24 15:16 | +20 | SOL | DOWN | 0.71 | 0.96 | 2.29 |
| 10-24 15:16 | +15 | SOL | DOWN | 0.71 | 0.89 | 1.58 |
| 10-24 15:16 | +10 | SOL | DOWN | 0.71 | 0.82 | 0.84 |
