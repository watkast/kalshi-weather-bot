# Range-Scalp Bot

*Updated Fri Oct 16 17:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19555 | 16991 | 2564 (29) | 0 | $-5907.06 | -4.8% |
| **+10¢** | 14745 | 11783 | 2962 (41) | 0 | $-5312.16 | -5.7% |
| **+15¢** | 12341 | 9156 | 3185 (60) | 0 | $-4794.88 | -6.2% |
| **+20¢** | 10952 | 7615 | 3337 (79) | 0 | $-4249.27 | -6.2% |
| **+10¢ (15¢ stop)** | 24047 | 23997 | 50 (29) | 0 | $-9199.40 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 17:32 | +10 stop | BTC | UP | 0.66 | 0.82 | 1.33 |
| 10-16 17:32 | +20 | BTC | UP | 0.66 | 0.87 | 1.86 |
| 10-16 17:32 | +15 | BTC | UP | 0.66 | 0.82 | 1.33 |
| 10-16 17:32 | +10 | BTC | UP | 0.66 | 0.82 | 1.33 |
| 10-16 17:32 | +5 | BTC | UP | 0.66 | 0.71 | 0.19 |
| 10-16 17:32 | +10 stop | DOGE | UP | 0.62 | 0.82 | 1.70 |
| 10-16 17:32 | +20 | DOGE | UP | 0.62 | 0.82 | 1.72 |
| 10-16 17:32 | +15 | DOGE | UP | 0.62 | 0.82 | 1.72 |
| 10-16 17:32 | +10 | DOGE | UP | 0.62 | 0.82 | 1.72 |
| 10-16 17:32 | +5 | DOGE | UP | 0.62 | 0.69 | 0.38 |
| 10-16 17:30 | +10 stop | NEAR | UP | 0.66 | 0.76 | 0.71 |
| 10-16 17:30 | +20 | NEAR | UP | 0.66 | 0.88 | 1.96 |
| 10-16 17:30 | +15 | NEAR | UP | 0.66 | 0.82 | 1.33 |
| 10-16 17:30 | +10 | NEAR | UP | 0.66 | 0.76 | 0.71 |
| 10-16 17:30 | +5 | NEAR | UP | 0.66 | 0.76 | 0.71 |
| 10-16 17:30 | +10 stop | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 10-16 17:30 | +20 | HYPE | UP | 0.67 | 0.87 | 1.76 |
| 10-16 17:30 | +15 | HYPE | UP | 0.67 | 0.83 | 1.34 |
| 10-16 17:30 | +10 | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 10-16 17:30 | +5 | HYPE | UP | 0.67 | 0.75 | 0.50 |
| 10-16 17:17 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-16 17:17 | +20 | SOL | DOWN | 0.70 | 0.91 | 1.85 |
| 10-16 17:17 | +15 | SOL | DOWN | 0.70 | 0.88 | 1.57 |
| 10-16 17:17 | +10 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-16 17:11 | +10 stop | HYPE | DOWN | 0.65 | 0.82 | 1.39 |
| 10-16 17:11 | +15 | HYPE | DOWN | 0.65 | 0.82 | 1.43 |
| 10-16 17:11 | +10 | HYPE | DOWN | 0.65 | 0.82 | 1.43 |
| 10-16 17:11 | +5 | HYPE | DOWN | 0.65 | 0.82 | 1.43 |
| 10-16 17:10 | +10 stop | ZEC | DOWN | 0.60 | 0.71 | 0.78 |
| 10-16 17:10 | +20 | ZEC | DOWN | 0.59 | 0.79 | 1.71 |
| 10-16 17:10 | +15 | ZEC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-16 17:10 | +10 | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-16 17:10 | +5 | ZEC | DOWN | 0.61 | 0.66 | 0.17 |
| 10-16 17:04 | +10 stop | ZEC | DOWN | 0.60 | 0.81 | 1.82 |
| 10-16 17:04 | +10 stop | DOGE | DOWN | 0.63 | 0.76 | 1.00 |
| 10-16 17:04 | +10 stop | NEAR | DOWN | 0.67 | 0.84 | 1.44 |
| 10-16 17:03 | +5 | BNB | DOWN | 0.68 | 0.78 | 0.71 |
| 10-16 17:03 | +10 stop | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-16 17:03 | +10 | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-16 17:03 | +5 | BTC | DOWN | 0.71 | 0.77 | 0.32 |
