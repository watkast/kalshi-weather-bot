# Range-Scalp Bot

*Updated Wed Nov 04 02:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46653 | 40625 | 6028 (72) | 1 | $-13409.31 | -4.6% |
| **+10¢** | 34849 | 27861 | 6988 (96) | 1 | $-12239.45 | -5.6% |
| **+15¢** | 29183 | 21665 | 7518 (124) | 1 | $-11188.99 | -6.1% |
| **+20¢** | 25925 | 18052 | 7873 (164) | 1 | $-9838.43 | -6.0% |
| **+10¢ (15¢ stop)** | 56883 | 56790 | 93 (56) | 1 | $-21257.91 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 02:15 | +10 stop | DOGE | DOWN | 0.59 | open |  |
| 11-04 02:15 | +20 | DOGE | DOWN | 0.59 | open |  |
| 11-04 02:15 | +15 | DOGE | DOWN | 0.59 | open |  |
| 11-04 02:15 | +10 | DOGE | DOWN | 0.59 | open |  |
| 11-04 02:15 | +5 | DOGE | DOWN | 0.59 | open |  |
| 11-04 02:13 | +10 stop | HYPE | DOWN | 0.20 | 0.64 | 4.11 |
| 11-04 02:13 | +5 | HYPE | DOWN | 0.42 | 0.64 | 1.85 |
| 11-04 02:13 | +10 stop | XRP | DOWN | 0.47 | 0.68 | 1.79 |
| 11-04 02:13 | +20 | XRP | DOWN | 0.48 | 0.68 | 1.66 |
| 11-04 02:13 | +15 | XRP | DOWN | 0.61 | yes | -6.27 |
| 11-04 02:13 | +10 | XRP | DOWN | 0.63 | yes | -6.47 |
| 11-04 02:13 | +5 | XRP | DOWN | 0.63 | 0.68 | 0.17 |
| 11-04 02:13 | +10 stop | DOGE | DOWN | 0.46 | 0.63 | 1.35 |
| 11-04 02:13 | +10 | DOGE | DOWN | 0.46 | 0.63 | 1.35 |
| 11-04 02:13 | +5 | DOGE | DOWN | 0.46 | 0.63 | 1.35 |
| 11-04 02:13 | +10 stop | HYPE | DOWN | 0.71 | 0.53 | -2.13 |
| 11-04 02:13 | +10 | HYPE | DOWN | 0.71 | yes | -7.25 |
| 11-04 02:12 | +10 stop | BNB | DOWN | 0.52 | 0.26 | -2.92 |
| 11-04 02:12 | +10 stop | HYPE | DOWN | 0.55 | 0.67 | 0.86 |
| 11-04 02:12 | +10 | HYPE | DOWN | 0.55 | 0.67 | 0.86 |
| 11-04 02:12 | +5 | HYPE | DOWN | 0.55 | 0.67 | 0.86 |
| 11-04 02:12 | +5 | BNB | DOWN | 0.50 | 0.60 | 0.65 |
| 11-04 02:12 | +10 stop | NEAR | DOWN | 0.67 | 0.49 | -2.14 |
| 11-04 02:11 | +10 stop | BNB | UP | 0.60 | 0.45 | -1.88 |
| 11-04 02:11 | +20 | BNB | UP | 0.55 | 0.94 | 3.64 |
| 11-04 02:11 | +15 | BNB | UP | 0.55 | 0.71 | 1.27 |
| 11-04 02:11 | +10 | BNB | UP | 0.59 | 0.71 | 0.92 |
| 11-04 02:11 | +5 | BNB | UP | 0.53 | 0.60 | 0.35 |
| 11-04 02:11 | +10 stop | ZEC | UP | 0.49 | 0.65 | 1.26 |
| 11-04 02:11 | +20 | ZEC | UP | 0.52 | 0.77 | 2.19 |
| 11-04 02:11 | +15 | ZEC | UP | 0.52 | 0.77 | 2.19 |
| 11-04 02:11 | +10 | ZEC | UP | 0.54 | 0.65 | 0.76 |
| 11-04 02:11 | +5 | ZEC | UP | 0.54 | 0.65 | 0.76 |
| 11-04 02:11 | +10 stop | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 11-04 02:11 | +15 | HYPE | DOWN | 0.59 | yes | -6.07 |
| 11-04 02:11 | +10 | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 11-04 02:11 | +5 | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 11-04 02:11 | +10 stop | DOGE | UP | 0.45 | 0.58 | 0.94 |
| 11-04 02:11 | +20 | DOGE | UP | 0.45 | 0.85 | 3.73 |
| 11-04 02:11 | +15 | DOGE | UP | 0.45 | 0.85 | 3.73 |
