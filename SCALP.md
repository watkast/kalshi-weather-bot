# Range-Scalp Bot

*Updated Sat Oct 03 12:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 747 | 649 | 98 (1) | 4 | $-224.84 | -4.7% |
| **+10¢** | 566 | 458 | 108 (2) | 5 | $-163.98 | -4.6% |
| **+15¢** | 480 | 364 | 116 (3) | 5 | $-145.51 | -4.8% |
| **+20¢** | 417 | 295 | 122 (3) | 5 | $-148.33 | -5.6% |
| **+10¢ (15¢ stop)** | 956 | 955 | 1 (1) | 1 | $-513.95 | -8.5% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 12:26 | +15 | DOGE | DOWN | 0.71 | open |  |
| 10-03 12:26 | +5 | DOGE | DOWN | 0.71 | open |  |
| 10-03 12:26 | +10 stop | DOGE | DOWN | 0.65 | open |  |
| 10-03 12:24 | +10 stop | XRP | DOWN | 0.66 | 0.77 | 0.81 |
| 10-03 12:24 | +20 | XRP | DOWN | 0.66 | 0.93 | 2.49 |
| 10-03 12:24 | +15 | XRP | DOWN | 0.66 | 0.85 | 1.65 |
| 10-03 12:24 | +10 | XRP | DOWN | 0.66 | 0.77 | 0.81 |
| 10-03 12:24 | +5 | XRP | DOWN | 0.66 | 0.74 | 0.50 |
| 10-03 12:23 | +10 stop | ZEC | UP | 0.71 | 0.88 | 1.47 |
| 10-03 12:22 | +10 stop | BNB | UP | 0.64 | 0.82 | 1.52 |
| 10-03 12:22 | +20 | BNB | UP | 0.64 | 0.86 | 1.94 |
| 10-03 12:22 | +15 | BNB | UP | 0.64 | 0.82 | 1.52 |
| 10-03 12:22 | +10 | BNB | UP | 0.64 | 0.82 | 1.52 |
| 10-03 12:22 | +5 | BNB | UP | 0.64 | 0.69 | 0.18 |
| 10-03 12:22 | +10 stop | ZEC | UP | 0.65 | 0.47 | -2.14 |
| 10-03 12:22 | +5 | HYPE | UP | 0.63 | 0.75 | 0.89 |
| 10-03 12:22 | +10 stop | DOGE | UP | 0.63 | 0.77 | 1.10 |
| 10-03 12:21 | +10 stop | NEAR | DOWN | 0.43 | 0.57 | 1.04 |
| 10-03 12:21 | +15 | NEAR | DOWN | 0.48 | 0.66 | 1.46 |
| 10-03 12:21 | +10 | NEAR | DOWN | 0.48 | 0.66 | 1.46 |
| 10-03 12:21 | +5 | NEAR | DOWN | 0.48 | 0.57 | 0.54 |
| 10-03 12:21 | +10 stop | HYPE | UP | 0.69 | 0.48 | -2.43 |
| 10-03 12:21 | +5 | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 10-03 12:20 | +10 stop | DOGE | DOWN | 0.59 | 0.27 | -3.51 |
| 10-03 12:20 | +10 | DOGE | DOWN | 0.59 | open |  |
| 10-03 12:20 | +5 | DOGE | DOWN | 0.59 | 0.68 | 0.57 |
| 10-03 12:20 | +5 | HYPE | DOWN | 0.56 | 0.65 | 0.56 |
| 10-03 12:19 | +5 | ZEC | DOWN | 0.56 | open |  |
| 10-03 12:19 | +10 stop | XRP | UP | 0.57 | 0.73 | 1.28 |
| 10-03 12:19 | +10 | XRP | UP | 0.57 | 0.73 | 1.28 |
| 10-03 12:19 | +5 | XRP | UP | 0.57 | 0.73 | 1.28 |
| 10-03 12:19 | +10 stop | HYPE | DOWN | 0.62 | 0.44 | -2.15 |
| 10-03 12:19 | +15 | HYPE | DOWN | 0.61 | open |  |
| 10-03 12:19 | +10 | HYPE | DOWN | 0.61 | open |  |
| 10-03 12:19 | +5 | HYPE | DOWN | 0.61 | 0.68 | 0.37 |
| 10-03 12:19 | +10 stop | NEAR | DOWN | 0.54 | 0.68 | 1.06 |
| 10-03 12:19 | +20 | NEAR | DOWN | 0.54 | 0.77 | 1.99 |
| 10-03 12:19 | +15 | NEAR | DOWN | 0.54 | 0.72 | 1.47 |
| 10-03 12:19 | +10 | NEAR | DOWN | 0.54 | 0.68 | 1.06 |
| 10-03 12:19 | +5 | NEAR | DOWN | 0.54 | 0.68 | 1.06 |
