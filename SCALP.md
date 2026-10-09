# Range-Scalp Bot

*Updated Fri Oct 09 21:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9542 | 8239 | 1303 (18) | 2 | $-3198.22 | -5.3% |
| **+10¢** | 7201 | 5672 | 1529 (30) | 2 | $-3130.45 | -6.9% |
| **+15¢** | 6072 | 4462 | 1610 (43) | 2 | $-2583.98 | -6.8% |
| **+20¢** | 5406 | 3734 | 1672 (55) | 2 | $-2141.52 | -6.3% |
| **+10¢ (15¢ stop)** | 11675 | 11640 | 35 (22) | 0 | $-4481.25 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 21:57 | +10 stop | ETH | UP | 0.68 | 0.86 | 1.55 |
| 10-09 21:57 | +10 stop | XRP | DOWN | 0.70 | 0.34 | -3.93 |
| 10-09 21:57 | +20 | XRP | DOWN | 0.70 | open |  |
| 10-09 21:57 | +15 | XRP | DOWN | 0.70 | open |  |
| 10-09 21:57 | +10 | XRP | DOWN | 0.70 | open |  |
| 10-09 21:57 | +5 | XRP | DOWN | 0.70 | open |  |
| 10-09 21:57 | +10 stop | BNB | DOWN | 0.48 | 0.69 | 1.77 |
| 10-09 21:57 | +20 | BNB | DOWN | 0.50 | 0.79 | 2.60 |
| 10-09 21:57 | +15 | BNB | DOWN | 0.50 | 0.69 | 1.57 |
| 10-09 21:57 | +10 | BNB | DOWN | 0.51 | 0.69 | 1.47 |
| 10-09 21:57 | +5 | BNB | DOWN | 0.50 | 0.69 | 1.57 |
| 10-09 21:56 | +10 stop | NEAR | UP | 0.65 | 0.92 | 2.45 |
| 10-09 21:54 | +10 stop | DOGE | UP | 0.62 | 0.77 | 1.15 |
| 10-09 21:53 | +10 stop | ETH | DOWN | 0.61 | 0.33 | -3.11 |
| 10-09 21:52 | +10 stop | DOGE | UP | 0.67 | 0.39 | -3.13 |
| 10-09 21:52 | +15 | DOGE | UP | 0.66 | 0.81 | 1.28 |
| 10-09 21:52 | +10 | DOGE | UP | 0.66 | 0.77 | 0.81 |
| 10-09 21:52 | +5 | DOGE | UP | 0.66 | 0.77 | 0.86 |
| 10-09 21:52 | +10 stop | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 10-09 21:52 | +20 | XRP | DOWN | 0.66 | 0.86 | 1.75 |
| 10-09 21:52 | +15 | XRP | DOWN | 0.66 | 0.81 | 1.23 |
| 10-09 21:52 | +10 | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 10-09 21:52 | +5 | XRP | DOWN | 0.66 | 0.74 | 0.50 |
| 10-09 21:52 | +10 stop | NEAR | DOWN | 0.57 | 0.69 | 0.88 |
| 10-09 21:52 | +5 | ETH | DOWN | 0.70 | open |  |
| 10-09 21:50 | +10 stop | ETH | DOWN | 0.63 | 0.43 | -2.35 |
| 10-09 21:50 | +10 stop | BNB | DOWN | 0.67 | 0.78 | 0.82 |
| 10-09 21:50 | +10 | BNB | DOWN | 0.67 | 0.78 | 0.82 |
| 10-09 21:50 | +5 | BNB | DOWN | 0.67 | 0.74 | 0.41 |
| 10-09 21:50 | +10 stop | BTC | DOWN | 0.54 | 0.39 | -1.85 |
| 10-09 21:47 | +10 stop | XRP | UP | 0.61 | 0.33 | -3.11 |
| 10-09 21:47 | +10 stop | ETH | UP | 0.56 | 0.38 | -2.15 |
| 10-09 21:47 | +5 | DOGE | UP | 0.71 | 0.77 | 0.32 |
| 10-09 21:47 | +10 stop | BTC | UP | 0.60 | 0.45 | -1.85 |
| 10-09 21:47 | +20 | BTC | UP | 0.60 | 0.85 | 2.24 |
| 10-09 21:47 | +15 | BTC | UP | 0.60 | 0.76 | 1.30 |
| 10-09 21:47 | +10 | BTC | UP | 0.60 | 0.71 | 0.78 |
| 10-09 21:47 | +5 | BTC | UP | 0.60 | 0.71 | 0.78 |
| 10-09 21:47 | +10 stop | NEAR | UP | 0.69 | 0.52 | -2.07 |
| 10-09 21:47 | +20 | NEAR | UP | 0.69 | 0.92 | 2.00 |
