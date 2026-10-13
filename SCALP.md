# Range-Scalp Bot

*Updated Tue Oct 13 12:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14588 | 12611 | 1977 (27) | 0 | $-4746.12 | -5.2% |
| **+10¢** | 11044 | 8750 | 2294 (39) | 0 | $-4445.25 | -6.4% |
| **+15¢** | 9284 | 6831 | 2453 (57) | 0 | $-3951.31 | -6.8% |
| **+20¢** | 8262 | 5707 | 2555 (72) | 0 | $-3407.07 | -6.6% |
| **+10¢ (15¢ stop)** | 17916 | 17867 | 49 (29) | 0 | $-6980.42 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 11:48 | +10 stop | NEAR | DOWN | 0.58 | 0.69 | 0.77 |
| 10-13 11:47 | +5 | SOL | DOWN | 0.71 | 0.77 | 0.32 |
| 10-13 11:47 | +5 | DOGE | DOWN | 0.65 | 0.70 | 0.19 |
| 10-13 11:46 | +10 stop | BNB | DOWN | 0.65 | 0.75 | 0.70 |
| 10-13 11:46 | +20 | BNB | DOWN | 0.67 | 0.89 | 2.00 |
| 10-13 11:46 | +15 | BNB | DOWN | 0.67 | 0.84 | 1.47 |
| 10-13 11:46 | +10 | BNB | DOWN | 0.67 | 0.78 | 0.84 |
| 10-13 11:46 | +5 | BNB | DOWN | 0.67 | 0.73 | 0.33 |
| 10-13 11:46 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-13 11:46 | +20 | ZEC | DOWN | 0.70 | 0.93 | 2.05 |
| 10-13 11:46 | +15 | ZEC | DOWN | 0.70 | 0.87 | 1.47 |
| 10-13 11:46 | +10 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-13 11:46 | +5 | ZEC | DOWN | 0.70 | 0.78 | 0.52 |
| 10-13 11:45 | +10 stop | XRP | DOWN | 0.62 | 0.74 | 0.89 |
| 10-13 11:45 | +20 | XRP | DOWN | 0.62 | 0.89 | 2.46 |
| 10-13 11:45 | +15 | XRP | DOWN | 0.62 | 0.77 | 1.20 |
| 10-13 11:45 | +10 | XRP | DOWN | 0.62 | 0.74 | 0.89 |
| 10-13 11:45 | +5 | XRP | DOWN | 0.62 | 0.67 | 0.17 |
| 10-13 11:45 | +10 stop | SOL | DOWN | 0.64 | 0.77 | 1.00 |
| 10-13 11:45 | +20 | SOL | DOWN | 0.64 | 0.87 | 2.05 |
| 10-13 11:45 | +15 | SOL | DOWN | 0.64 | 0.81 | 1.42 |
| 10-13 11:45 | +10 | SOL | DOWN | 0.64 | 0.77 | 1.00 |
| 10-13 11:45 | +5 | SOL | DOWN | 0.64 | 0.71 | 0.38 |
| 10-13 11:45 | +10 stop | NEAR | DOWN | 0.68 | 0.49 | -2.22 |
| 10-13 11:45 | +20 | NEAR | DOWN | 0.66 | 0.86 | 1.75 |
| 10-13 11:45 | +15 | NEAR | DOWN | 0.64 | 0.79 | 1.21 |
| 10-13 11:45 | +10 | NEAR | DOWN | 0.64 | 0.79 | 1.21 |
| 10-13 11:45 | +5 | NEAR | DOWN | 0.64 | 0.69 | 0.18 |
| 10-13 11:45 | +10 stop | DOGE | DOWN | 0.63 | 0.75 | 0.89 |
| 10-13 11:45 | +20 | DOGE | DOWN | 0.64 | 0.88 | 2.15 |
| 10-13 11:45 | +15 | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-13 11:45 | +10 | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 10-13 11:45 | +5 | DOGE | DOWN | 0.64 | 0.69 | 0.18 |
| 10-13 11:45 | +10 stop | HYPE | DOWN | 0.66 | 0.80 | 1.12 |
| 10-13 11:45 | +20 | HYPE | DOWN | 0.66 | 0.86 | 1.75 |
| 10-13 11:45 | +15 | HYPE | DOWN | 0.66 | 0.83 | 1.44 |
| 10-13 11:45 | +10 | HYPE | DOWN | 0.66 | 0.80 | 1.12 |
| 10-13 11:45 | +5 | HYPE | DOWN | 0.66 | 0.72 | 0.29 |
| 10-13 11:43 | +10 stop | BNB | UP | 0.57 | 0.89 | 2.95 |
| 10-13 11:43 | +10 stop | BTC | UP | 0.66 | 0.77 | 0.81 |
