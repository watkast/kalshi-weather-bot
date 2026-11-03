# Range-Scalp Bot

*Updated Tue Nov 03 10:18 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45781 | 39862 | 5919 (69) | 1 | $-13211.37 | -4.6% |
| **+10¢** | 34187 | 27328 | 6859 (91) | 1 | $-12092.72 | -5.6% |
| **+15¢** | 28603 | 21224 | 7379 (119) | 3 | $-11087.62 | -6.2% |
| **+20¢** | 25406 | 17672 | 7734 (155) | 3 | $-9874.96 | -6.2% |
| **+10¢ (15¢ stop)** | 55855 | 55766 | 89 (53) | 0 | $-20967.01 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 10:17 | +10 stop | HYPE | DOWN | 0.61 | 0.41 | -2.34 |
| 11-03 10:17 | +20 | HYPE | DOWN | 0.61 | open |  |
| 11-03 10:17 | +15 | HYPE | DOWN | 0.61 | open |  |
| 11-03 10:17 | +10 | HYPE | DOWN | 0.61 | open |  |
| 11-03 10:17 | +5 | HYPE | DOWN | 0.61 | open |  |
| 11-03 10:17 | +10 stop | BNB | UP | 0.68 | 0.78 | 0.71 |
| 11-03 10:17 | +20 | BNB | UP | 0.68 | open |  |
| 11-03 10:17 | +15 | BNB | UP | 0.68 | open |  |
| 11-03 10:17 | +10 | BNB | UP | 0.68 | 0.78 | 0.71 |
| 11-03 10:17 | +5 | BNB | UP | 0.68 | 0.78 | 0.71 |
| 11-03 10:16 | +10 stop | NEAR | UP | 0.62 | 0.76 | 1.10 |
| 11-03 10:16 | +10 stop | BTC | UP | 0.61 | 0.73 | 0.89 |
| 11-03 10:16 | +20 | BTC | UP | 0.61 | open |  |
| 11-03 10:16 | +15 | BTC | UP | 0.61 | open |  |
| 11-03 10:16 | +10 | BTC | UP | 0.61 | 0.73 | 0.89 |
| 11-03 10:16 | +5 | BTC | UP | 0.61 | 0.73 | 0.89 |
| 11-03 10:16 | +5 | NEAR | UP | 0.64 | 0.76 | 0.90 |
| 11-03 10:15 | +10 stop | XRP | UP | 0.65 | 0.78 | 1.05 |
| 11-03 10:15 | +20 | XRP | UP | 0.63 | 0.85 | 1.94 |
| 11-03 10:15 | +15 | XRP | UP | 0.63 | 0.78 | 1.20 |
| 11-03 10:15 | +10 | XRP | UP | 0.63 | 0.78 | 1.20 |
| 11-03 10:15 | +5 | XRP | UP | 0.63 | 0.72 | 0.58 |
| 11-03 10:15 | +10 stop | NEAR | UP | 0.54 | 0.64 | 0.65 |
| 11-03 10:15 | +20 | NEAR | UP | 0.54 | 0.76 | 1.89 |
| 11-03 10:15 | +15 | NEAR | UP | 0.56 | 0.76 | 1.69 |
| 11-03 10:15 | +10 | NEAR | UP | 0.56 | 0.76 | 1.69 |
| 11-03 10:15 | +5 | NEAR | UP | 0.56 | 0.63 | 0.35 |
| 11-03 10:15 | +10 stop | ZEC | UP | 0.68 | 0.80 | 0.92 |
| 11-03 10:15 | +20 | ZEC | UP | 0.68 | 0.89 | 1.87 |
| 11-03 10:15 | +15 | ZEC | UP | 0.69 | 0.84 | 1.25 |
| 11-03 10:15 | +10 | ZEC | UP | 0.69 | 0.80 | 0.83 |
| 11-03 10:15 | +5 | ZEC | UP | 0.69 | 0.74 | 0.21 |
| 11-03 10:12 | +10 stop | ZEC | DOWN | 0.55 | 0.66 | 0.76 |
| 11-03 10:12 | +15 | ZEC | DOWN | 0.55 | 0.82 | 2.41 |
| 11-03 10:12 | +10 | ZEC | DOWN | 0.55 | 0.66 | 0.76 |
| 11-03 10:12 | +5 | ZEC | DOWN | 0.64 | 0.82 | 1.52 |
| 11-03 10:09 | +10 stop | BTC | DOWN | 0.70 | 0.88 | 1.57 |
| 11-03 10:09 | +10 stop | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-03 10:09 | +20 | DOGE | DOWN | 0.62 | 0.82 | 1.72 |
| 11-03 10:09 | +15 | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
