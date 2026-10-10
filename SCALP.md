# Range-Scalp Bot

*Updated Sat Oct 10 04:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9946 | 8586 | 1360 (18) | 0 | $-3335.92 | -5.3% |
| **+10¢** | 7517 | 5931 | 1586 (30) | 0 | $-3202.46 | -6.8% |
| **+15¢** | 6347 | 4674 | 1673 (43) | 0 | $-2639.41 | -6.6% |
| **+20¢** | 5640 | 3902 | 1738 (55) | 0 | $-2201.06 | -6.2% |
| **+10¢ (15¢ stop)** | 12211 | 12176 | 35 (22) | 0 | $-4773.98 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 04:28 | +10 stop | XRP | UP | 0.60 | 0.40 | -2.34 |
| 10-10 04:28 | +20 | XRP | UP | 0.60 | 0.95 | 3.29 |
| 10-10 04:28 | +15 | XRP | UP | 0.59 | 0.95 | 3.37 |
| 10-10 04:28 | +10 | XRP | UP | 0.59 | 0.95 | 3.37 |
| 10-10 04:28 | +5 | XRP | UP | 0.59 | 0.95 | 3.39 |
| 10-10 04:24 | +10 stop | NEAR | DOWN | 0.69 | 0.82 | 1.04 |
| 10-10 04:24 | +20 | NEAR | DOWN | 0.69 | 0.93 | 2.17 |
| 10-10 04:24 | +15 | NEAR | DOWN | 0.69 | 0.88 | 1.67 |
| 10-10 04:24 | +10 | NEAR | DOWN | 0.69 | 0.82 | 1.04 |
| 10-10 04:24 | +5 | NEAR | DOWN | 0.69 | 0.77 | 0.52 |
| 10-10 04:21 | +10 stop | ZEC | DOWN | 0.69 | 0.85 | 1.36 |
| 10-10 04:20 | +10 stop | ZEC | UP | 0.62 | 0.38 | -2.76 |
| 10-10 04:18 | +5 | BNB | DOWN | 0.63 | 0.69 | 0.28 |
| 10-10 04:18 | +10 stop | ETH | DOWN | 0.56 | 0.68 | 0.86 |
| 10-10 04:17 | +10 stop | ZEC | DOWN | 0.66 | 0.48 | -2.17 |
| 10-10 04:17 | +20 | ZEC | DOWN | 0.66 | 0.91 | 2.28 |
| 10-10 04:17 | +15 | ZEC | DOWN | 0.66 | 0.85 | 1.64 |
| 10-10 04:17 | +10 | ZEC | DOWN | 0.66 | 0.85 | 1.64 |
| 10-10 04:17 | +5 | ZEC | DOWN | 0.66 | 0.75 | 0.59 |
| 10-10 04:17 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-10 04:17 | +20 | BTC | DOWN | 0.66 | 0.87 | 1.86 |
| 10-10 04:17 | +15 | BTC | DOWN | 0.66 | 0.82 | 1.33 |
| 10-10 04:17 | +10 | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-10 04:17 | +5 | BTC | DOWN | 0.66 | 0.73 | 0.40 |
| 10-10 04:17 | +10 stop | BNB | DOWN | 0.57 | 0.69 | 0.87 |
| 10-10 04:17 | +20 | BNB | DOWN | 0.57 | 0.83 | 2.32 |
| 10-10 04:17 | +15 | BNB | DOWN | 0.57 | 0.83 | 2.32 |
| 10-10 04:17 | +10 | BNB | DOWN | 0.57 | 0.69 | 0.87 |
| 10-10 04:17 | +5 | BNB | DOWN | 0.57 | 0.62 | 0.15 |
| 10-10 04:16 | +5 | ETH | DOWN | 0.70 | 0.79 | 0.63 |
| 10-10 04:16 | +10 stop | ETH | DOWN | 0.71 | 0.56 | -1.83 |
| 10-10 04:16 | +20 | ETH | DOWN | 0.71 | 0.93 | 2.04 |
| 10-10 04:16 | +15 | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 10-10 04:16 | +10 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-10 04:12 | +10 stop | HYPE | UP | 0.66 | 0.87 | 1.86 |
| 10-10 04:12 | +20 | HYPE | UP | 0.66 | 0.87 | 1.86 |
| 10-10 04:12 | +15 | HYPE | UP | 0.66 | 0.87 | 1.86 |
| 10-10 04:12 | +10 | HYPE | UP | 0.66 | 0.87 | 1.86 |
| 10-10 04:12 | +5 | HYPE | UP | 0.66 | 0.87 | 1.86 |
| 10-10 04:01 | +5 | BTC | UP | 0.69 | 0.79 | 0.73 |
