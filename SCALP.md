# Range-Scalp Bot

*Updated Wed Nov 18 04:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63580 | 55453 | 8127 (118) | 0 | $-17370.85 | -4.3% |
| **+10¢** | 47497 | 37984 | 9513 (159) | 0 | $-16296.70 | -5.5% |
| **+15¢** | 39826 | 29569 | 10257 (203) | 1 | $-14776.46 | -5.9% |
| **+20¢** | 35471 | 24707 | 10764 (258) | 2 | $-13044.99 | -5.9% |
| **+10¢ (15¢ stop)** | 77358 | 77200 | 158 (93) | 0 | $-28437.00 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 04:11 | +10 stop | DOGE | DOWN | 0.53 | 0.22 | -3.43 |
| 11-18 04:10 | +10 stop | BNB | UP | 0.64 | 0.89 | 2.26 |
| 11-18 04:10 | +15 | BNB | UP | 0.64 | 0.89 | 2.26 |
| 11-18 04:10 | +10 | BNB | UP | 0.64 | 0.89 | 2.26 |
| 11-18 04:10 | +5 | BNB | UP | 0.64 | 0.89 | 2.26 |
| 11-18 04:10 | +10 stop | DOGE | UP | 0.57 | 0.42 | -1.86 |
| 11-18 04:10 | +5 | DOGE | UP | 0.57 | 0.77 | 1.69 |
| 11-18 04:10 | +10 stop | BNB | DOWN | 0.40 | 0.57 | 1.35 |
| 11-18 04:10 | +20 | BNB | DOWN | 0.40 | open |  |
| 11-18 04:10 | +15 | BNB | DOWN | 0.41 | 0.57 | 1.25 |
| 11-18 04:10 | +10 | BNB | DOWN | 0.41 | 0.57 | 1.25 |
| 11-18 04:10 | +5 | BNB | DOWN | 0.41 | 0.57 | 1.25 |
| 11-18 04:10 | +10 stop | DOGE | DOWN | 0.39 | 0.56 | 1.35 |
| 11-18 04:10 | +5 | DOGE | DOWN | 0.39 | 0.56 | 1.35 |
| 11-18 04:09 | +5 | BNB | DOWN | 0.65 | 0.78 | 1.01 |
| 11-18 04:09 | +10 stop | DOGE | UP | 0.51 | 0.24 | -3.01 |
| 11-18 04:09 | +10 | DOGE | UP | 0.51 | 0.77 | 2.29 |
| 11-18 04:09 | +5 | DOGE | UP | 0.51 | 0.56 | 0.14 |
| 11-18 04:08 | +10 stop | BNB | DOWN | 0.57 | 0.78 | 1.79 |
| 11-18 04:08 | +20 | BNB | DOWN | 0.57 | 0.78 | 1.79 |
| 11-18 04:08 | +15 | BNB | DOWN | 0.57 | 0.78 | 1.79 |
| 11-18 04:08 | +10 | BNB | DOWN | 0.57 | 0.78 | 1.79 |
| 11-18 04:08 | +5 | BNB | DOWN | 0.57 | 0.62 | 0.15 |
| 11-18 04:08 | +10 stop | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 11-18 04:08 | +15 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 11-18 04:08 | +10 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 11-18 04:08 | +5 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 11-18 04:07 | +10 stop | ZEC | DOWN | 0.57 | 0.28 | -3.23 |
| 11-18 04:06 | +10 stop | XRP | DOWN | 0.64 | 0.44 | -2.35 |
| 11-18 04:05 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 11-18 04:05 | +10 | SOL | DOWN | 0.58 | 0.72 | 1.07 |
| 11-18 04:04 | +10 stop | SOL | DOWN | 0.60 | 0.72 | 0.88 |
| 11-18 04:04 | +10 stop | NEAR | DOWN | 0.63 | 0.84 | 1.84 |
| 11-18 04:04 | +5 | NEAR | DOWN | 0.60 | 0.66 | 0.23 |
| 11-18 04:04 | +5 | BNB | DOWN | 0.45 | 0.59 | 1.03 |
| 11-18 04:03 | +5 | SOL | DOWN | 0.64 | 0.72 | 0.48 |
| 11-18 04:03 | +10 stop | DOGE | DOWN | 0.62 | 0.74 | 0.89 |
| 11-18 04:03 | +20 | DOGE | DOWN | 0.62 | open |  |
| 11-18 04:03 | +15 | DOGE | DOWN | 0.62 | open |  |
| 11-18 04:03 | +10 | DOGE | DOWN | 0.62 | 0.74 | 0.89 |
