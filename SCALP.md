# Range-Scalp Bot

*Updated Wed Oct 14 21:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16571 | 14366 | 2205 (28) | 2 | $-5175.37 | -5.0% |
| **+10¢** | 12534 | 9979 | 2555 (40) | 2 | $-4729.81 | -6.0% |
| **+15¢** | 10531 | 7788 | 2743 (59) | 2 | $-4230.67 | -6.4% |
| **+20¢** | 9356 | 6481 | 2875 (76) | 2 | $-3743.44 | -6.4% |
| **+10¢ (15¢ stop)** | 20398 | 20348 | 50 (29) | 0 | $-7866.83 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 21:26 | +10 stop | HYPE | DOWN | 0.58 | 0.41 | -2.05 |
| 10-14 21:26 | +10 stop | BNB | DOWN | 0.70 | 0.51 | -2.23 |
| 10-14 21:24 | +10 stop | HYPE | DOWN | 0.53 | 0.64 | 0.72 |
| 10-14 21:23 | +10 stop | NEAR | UP | 0.58 | 0.71 | 0.97 |
| 10-14 21:23 | +10 stop | HYPE | DOWN | 0.70 | 0.54 | -1.93 |
| 10-14 21:22 | +10 stop | BNB | DOWN | 0.66 | 0.47 | -2.23 |
| 10-14 21:22 | +10 | BNB | DOWN | 0.66 | open |  |
| 10-14 21:22 | +5 | BNB | DOWN | 0.66 | open |  |
| 10-14 21:21 | +10 stop | XRP | DOWN | 0.47 | 0.32 | -1.84 |
| 10-14 21:21 | +10 stop | DOGE | DOWN | 0.61 | 0.34 | -3.03 |
| 10-14 21:21 | +5 | ZEC | UP | 0.65 | 0.70 | 0.19 |
| 10-14 21:20 | +10 stop | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-14 21:20 | +10 stop | NEAR | DOWN | 0.58 | 0.35 | -2.63 |
| 10-14 21:20 | +5 | BTC | UP | 0.64 | 0.77 | 1.00 |
| 10-14 21:18 | +5 | BTC | UP | 0.58 | 0.64 | 0.25 |
| 10-14 21:18 | +5 | NEAR | UP | 0.66 | 0.71 | 0.19 |
| 10-14 21:18 | +15 | BTC | UP | 0.58 | 0.77 | 1.59 |
| 10-14 21:18 | +5 | BTC | UP | 0.58 | 0.66 | 0.46 |
| 10-14 21:18 | +10 stop | HYPE | DOWN | 0.68 | 0.82 | 1.09 |
| 10-14 21:17 | +5 | NEAR | UP | 0.55 | 0.61 | 0.25 |
| 10-14 21:17 | +10 stop | ETH | UP | 0.67 | 0.79 | 0.92 |
| 10-14 21:17 | +10 | ETH | UP | 0.67 | 0.79 | 0.92 |
| 10-14 21:17 | +10 stop | BTC | UP | 0.62 | 0.77 | 1.20 |
| 10-14 21:17 | +10 | BTC | UP | 0.62 | 0.77 | 1.20 |
| 10-14 21:17 | +5 | ETH | UP | 0.67 | 0.72 | 0.19 |
| 10-14 21:17 | +5 | BTC | UP | 0.63 | 0.69 | 0.28 |
| 10-14 21:16 | +10 stop | ZEC | UP | 0.71 | 0.81 | 0.74 |
| 10-14 21:16 | +20 | ZEC | UP | 0.71 | 0.91 | 1.80 |
| 10-14 21:16 | +15 | ZEC | UP | 0.71 | 0.86 | 1.26 |
| 10-14 21:16 | +10 | ZEC | UP | 0.71 | 0.81 | 0.74 |
| 10-14 21:16 | +5 | ZEC | UP | 0.71 | 0.76 | 0.22 |
| 10-14 21:16 | +10 stop | ETH | UP | 0.55 | 0.65 | 0.66 |
| 10-14 21:16 | +20 | ETH | UP | 0.55 | 0.79 | 2.10 |
| 10-14 21:16 | +15 | ETH | UP | 0.55 | 0.72 | 1.37 |
| 10-14 21:16 | +10 | ETH | UP | 0.55 | 0.65 | 0.66 |
| 10-14 21:16 | +5 | ETH | UP | 0.55 | 0.63 | 0.45 |
| 10-14 21:16 | +10 stop | XRP | UP | 0.58 | 0.42 | -1.99 |
| 10-14 21:16 | +20 | XRP | UP | 0.59 | 0.82 | 2.02 |
| 10-14 21:16 | +15 | XRP | UP | 0.59 | 0.82 | 2.02 |
| 10-14 21:16 | +10 | XRP | UP | 0.58 | 0.82 | 2.07 |
