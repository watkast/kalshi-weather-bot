# Range-Scalp Bot

*Updated Thu Oct 15 11:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17389 | 15093 | 2296 (28) | 1 | $-5312.65 | -4.8% |
| **+10¢** | 13136 | 10477 | 2659 (40) | 1 | $-4832.08 | -5.8% |
| **+15¢** | 11035 | 8180 | 2855 (59) | 2 | $-4282.05 | -6.2% |
| **+20¢** | 9806 | 6820 | 2986 (77) | 2 | $-3713.01 | -6.0% |
| **+10¢ (15¢ stop)** | 21374 | 21324 | 50 (29) | 0 | $-8257.63 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 11:12 | +10 stop | ZEC | DOWN | 0.67 | 0.81 | 1.13 |
| 10-15 11:12 | +10 | ZEC | DOWN | 0.66 | 0.81 | 1.21 |
| 10-15 11:12 | +5 | ZEC | DOWN | 0.66 | 0.72 | 0.26 |
| 10-15 11:10 | +10 stop | ZEC | DOWN | 0.60 | 0.73 | 0.99 |
| 10-15 11:10 | +10 stop | NEAR | UP | 0.71 | 0.56 | -1.83 |
| 10-15 11:10 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.24 |
| 10-15 11:09 | +10 stop | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 10-15 11:09 | +20 | DOGE | DOWN | 0.70 | open |  |
| 10-15 11:09 | +15 | DOGE | DOWN | 0.70 | open |  |
| 10-15 11:09 | +10 | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 10-15 11:09 | +5 | DOGE | DOWN | 0.70 | 0.78 | 0.52 |
| 10-15 11:09 | +10 stop | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-15 11:09 | +20 | ZEC | DOWN | 0.61 | 0.81 | 1.72 |
| 10-15 11:09 | +15 | ZEC | DOWN | 0.61 | 0.81 | 1.72 |
| 10-15 11:09 | +10 | ZEC | DOWN | 0.61 | 0.73 | 0.89 |
| 10-15 11:09 | +5 | ZEC | DOWN | 0.61 | 0.67 | 0.27 |
| 10-15 11:08 | +5 | NEAR | DOWN | 0.49 | 0.64 | 1.15 |
| 10-15 11:08 | +10 stop | NEAR | DOWN | 0.58 | 0.31 | -3.03 |
| 10-15 11:08 | +20 | NEAR | DOWN | 0.58 | 0.82 | 2.11 |
| 10-15 11:08 | +15 | NEAR | DOWN | 0.58 | 0.82 | 2.11 |
| 10-15 11:08 | +10 | NEAR | DOWN | 0.57 | 0.82 | 2.21 |
| 10-15 11:08 | +5 | NEAR | DOWN | 0.57 | 0.65 | 0.46 |
| 10-15 11:07 | +10 stop | HYPE | DOWN | 0.51 | 0.19 | -3.49 |
| 10-15 11:07 | +20 | HYPE | DOWN | 0.51 | open |  |
| 10-15 11:07 | +15 | HYPE | DOWN | 0.51 | open |  |
| 10-15 11:07 | +10 | HYPE | DOWN | 0.51 | open |  |
| 10-15 11:07 | +5 | HYPE | DOWN | 0.51 | open |  |
| 10-15 11:01 | +5 | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-15 11:01 | +10 stop | XRP | DOWN | 0.64 | 0.77 | 0.98 |
| 10-15 11:01 | +20 | XRP | DOWN | 0.64 | 0.86 | 1.92 |
| 10-15 11:01 | +15 | XRP | DOWN | 0.64 | 0.82 | 1.50 |
| 10-15 11:01 | +10 | XRP | DOWN | 0.64 | 0.77 | 0.96 |
| 10-15 11:01 | +5 | XRP | DOWN | 0.64 | 0.72 | 0.48 |
| 10-15 11:00 | +10 stop | BTC | DOWN | 0.55 | 0.76 | 1.79 |
| 10-15 11:00 | +20 | BTC | DOWN | 0.55 | 0.76 | 1.79 |
| 10-15 11:00 | +15 | BTC | DOWN | 0.55 | 0.76 | 1.79 |
| 10-15 11:00 | +10 | BTC | DOWN | 0.54 | 0.64 | 0.65 |
| 10-15 11:00 | +5 | BTC | DOWN | 0.54 | 0.60 | 0.25 |
| 10-15 11:00 | +10 stop | BNB | DOWN | 0.60 | 0.76 | 1.30 |
| 10-15 11:00 | +20 | BNB | DOWN | 0.60 | 0.80 | 1.71 |
