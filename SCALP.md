# Range-Scalp Bot

*Updated Tue Oct 20 11:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25566 | 22260 | 3306 (31) | 0 | $-7495.42 | -4.7% |
| **+10¢** | 19243 | 15425 | 3818 (46) | 0 | $-6632.89 | -5.5% |
| **+15¢** | 16102 | 11992 | 4110 (70) | 1 | $-5947.19 | -5.9% |
| **+20¢** | 14239 | 9938 | 4301 (88) | 2 | $-5313.17 | -5.9% |
| **+10¢ (15¢ stop)** | 31377 | 31324 | 53 (30) | 0 | $-11584.82 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 11:18 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
| 10-20 11:17 | +10 stop | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 10-20 11:17 | +20 | SOL | DOWN | 0.71 | 0.91 | 1.82 |
| 10-20 11:17 | +15 | SOL | DOWN | 0.71 | 0.87 | 1.37 |
| 10-20 11:17 | +10 | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 10-20 11:17 | +5 | SOL | DOWN | 0.71 | 0.76 | 0.22 |
| 10-20 11:17 | +10 stop | XRP | DOWN | 0.61 | 0.81 | 1.72 |
| 10-20 11:17 | +20 | XRP | DOWN | 0.61 | 0.81 | 1.72 |
| 10-20 11:17 | +15 | XRP | DOWN | 0.61 | 0.81 | 1.72 |
| 10-20 11:17 | +10 | XRP | DOWN | 0.61 | 0.81 | 1.72 |
| 10-20 11:17 | +5 | XRP | DOWN | 0.61 | 0.67 | 0.27 |
| 10-20 11:16 | +10 stop | BNB | DOWN | 0.69 | 0.82 | 1.04 |
| 10-20 11:16 | +20 | BNB | DOWN | 0.69 | open |  |
| 10-20 11:16 | +15 | BNB | DOWN | 0.69 | 0.85 | 1.36 |
| 10-20 11:16 | +10 | BNB | DOWN | 0.69 | 0.82 | 1.04 |
| 10-20 11:16 | +5 | BNB | DOWN | 0.69 | 0.76 | 0.42 |
| 10-20 11:16 | +10 stop | ZEC | DOWN | 0.63 | 0.75 | 0.89 |
| 10-20 11:16 | +20 | ZEC | DOWN | 0.63 | 0.84 | 1.83 |
| 10-20 11:16 | +15 | ZEC | DOWN | 0.63 | 0.79 | 1.31 |
| 10-20 11:16 | +10 | ZEC | DOWN | 0.62 | 0.75 | 0.99 |
| 10-20 11:16 | +5 | ZEC | DOWN | 0.62 | 0.69 | 0.38 |
| 10-20 11:16 | +10 stop | DOGE | DOWN | 0.59 | 0.70 | 0.80 |
| 10-20 11:16 | +10 | DOGE | DOWN | 0.59 | 0.70 | 0.80 |
| 10-20 11:16 | +5 | DOGE | DOWN | 0.59 | 0.67 | 0.49 |
| 10-20 11:16 | +10 stop | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-20 11:16 | +20 | BTC | DOWN | 0.63 | 0.86 | 2.04 |
| 10-20 11:16 | +15 | BTC | DOWN | 0.63 | 0.82 | 1.62 |
| 10-20 11:16 | +10 | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 10-20 11:16 | +5 | BTC | DOWN | 0.62 | 0.70 | 0.48 |
| 10-20 11:15 | +10 stop | DOGE | UP | 0.47 | 0.57 | 0.64 |
| 10-20 11:15 | +20 | DOGE | UP | 0.47 | open |  |
| 10-20 11:15 | +15 | DOGE | UP | 0.47 | open |  |
| 10-20 11:15 | +10 | DOGE | UP | 0.47 | 0.57 | 0.64 |
| 10-20 11:15 | +5 | DOGE | UP | 0.48 | 0.57 | 0.54 |
| 10-20 11:11 | +5 | BNB | DOWN | 0.64 | 0.76 | 0.90 |
| 10-20 11:11 | +10 stop | BNB | DOWN | 0.59 | 0.76 | 1.40 |
| 10-20 11:11 | +20 | BNB | DOWN | 0.60 | 0.85 | 2.24 |
| 10-20 11:11 | +15 | BNB | DOWN | 0.60 | 0.76 | 1.30 |
| 10-20 11:11 | +10 | BNB | DOWN | 0.60 | 0.76 | 1.30 |
| 10-20 11:11 | +5 | BNB | DOWN | 0.60 | 0.68 | 0.47 |
