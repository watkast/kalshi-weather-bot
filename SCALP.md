# Range-Scalp Bot

*Updated Mon Oct 05 04:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3260 | 2792 | 468 (3) | 2 | $-1218.11 | -5.9% |
| **+10¢** | 2522 | 1993 | 529 (4) | 3 | $-1068.70 | -6.7% |
| **+15¢** | 2121 | 1563 | 558 (5) | 7 | $-951.01 | -7.1% |
| **+20¢** | 1894 | 1309 | 585 (10) | 5 | $-843.65 | -7.1% |
| **+10¢ (15¢ stop)** | 4056 | 4055 | 1 (1) | 0 | $-1597.81 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 04:12 | +10 stop | BNB | DOWN | 0.69 | 0.84 | 1.22 |
| 10-05 04:11 | +10 stop | SOL | DOWN | 0.59 | 0.44 | -1.85 |
| 10-05 04:11 | +5 | SOL | DOWN | 0.56 | 0.61 | 0.17 |
| 10-05 04:11 | +10 stop | HYPE | UP | 0.42 | 0.26 | -1.92 |
| 10-05 04:11 | +10 | HYPE | UP | 0.42 | 0.56 | 1.04 |
| 10-05 04:11 | +5 | HYPE | UP | 0.42 | 0.56 | 1.04 |
| 10-05 04:10 | +10 stop | XRP | DOWN | 0.65 | 0.49 | -1.94 |
| 10-05 04:10 | +5 | SOL | UP | 0.41 | 0.59 | 1.43 |
| 10-05 04:10 | +10 stop | BNB | UP | 0.52 | 0.36 | -1.95 |
| 10-05 04:09 | +10 stop | XRP | UP | 0.59 | 0.43 | -1.95 |
| 10-05 04:09 | +5 | XRP | UP | 0.59 | 0.67 | 0.47 |
| 10-05 04:09 | +10 stop | BTC | DOWN | 0.68 | 0.80 | 0.92 |
| 10-05 04:09 | +10 | BTC | DOWN | 0.68 | 0.80 | 0.92 |
| 10-05 04:09 | +5 | BTC | DOWN | 0.68 | 0.80 | 0.92 |
| 10-05 04:09 | +10 stop | SOL | UP | 0.65 | 0.45 | -2.34 |
| 10-05 04:09 | +10 | SOL | UP | 0.65 | 0.85 | 1.75 |
| 10-05 04:09 | +5 | SOL | UP | 0.65 | 0.71 | 0.29 |
| 10-05 04:09 | +10 stop | HYPE | UP | 0.69 | 0.81 | 0.94 |
| 10-05 04:09 | +15 | HYPE | UP | 0.71 | open |  |
| 10-05 04:09 | +10 | HYPE | UP | 0.71 | 0.81 | 0.74 |
| 10-05 04:09 | +5 | HYPE | UP | 0.71 | 0.81 | 0.74 |
| 10-05 04:09 | +10 stop | DOGE | DOWN | 0.69 | 0.83 | 1.15 |
| 10-05 04:09 | +10 stop | ZEC | UP | 0.66 | 0.77 | 0.82 |
| 10-05 04:09 | +10 | ZEC | UP | 0.66 | 0.77 | 0.82 |
| 10-05 04:09 | +5 | ZEC | UP | 0.66 | 0.77 | 0.81 |
| 10-05 04:09 | +10 stop | XRP | UP | 0.51 | 0.61 | 0.65 |
| 10-05 04:09 | +20 | XRP | UP | 0.51 | 0.79 | 2.50 |
| 10-05 04:09 | +5 | XRP | UP | 0.51 | 0.61 | 0.65 |
| 10-05 04:09 | +10 stop | SOL | UP | 0.57 | 0.67 | 0.66 |
| 10-05 04:09 | +20 | SOL | UP | 0.57 | 0.85 | 2.53 |
| 10-05 04:09 | +15 | SOL | UP | 0.57 | 0.85 | 2.53 |
| 10-05 04:09 | +10 | SOL | UP | 0.57 | 0.67 | 0.66 |
| 10-05 04:09 | +5 | SOL | UP | 0.57 | 0.67 | 0.66 |
| 10-05 04:08 | +10 stop | ZEC | UP | 0.35 | 0.58 | 1.96 |
| 10-05 04:08 | +10 | ZEC | UP | 0.35 | 0.58 | 1.96 |
| 10-05 04:08 | +5 | ZEC | UP | 0.35 | 0.58 | 1.96 |
| 10-05 04:07 | +10 stop | BNB | UP | 0.66 | 0.30 | -3.90 |
| 10-05 04:07 | +15 | BNB | UP | 0.66 | open |  |
| 10-05 04:07 | +5 | ZEC | UP | 0.69 | 0.75 | 0.31 |
| 10-05 04:07 | +10 stop | DOGE | UP | 0.67 | 0.36 | -3.43 |
