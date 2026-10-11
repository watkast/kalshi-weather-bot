# Range-Scalp Bot

*Updated Sun Oct 11 16:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12163 | 10488 | 1675 (24) | 2 | $-4083.47 | -5.3% |
| **+10¢** | 9243 | 7300 | 1943 (37) | 3 | $-3864.14 | -6.6% |
| **+15¢** | 7790 | 5728 | 2062 (54) | 3 | $-3298.92 | -6.7% |
| **+20¢** | 6939 | 4791 | 2148 (68) | 5 | $-2800.94 | -6.4% |
| **+10¢ (15¢ stop)** | 14992 | 14951 | 41 (25) | 0 | $-5932.64 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 16:23 | +10 stop | ETH | UP | 0.60 | 0.76 | 1.31 |
| 10-11 16:23 | +10 stop | HYPE | DOWN | 0.71 | 0.82 | 0.86 |
| 10-11 16:23 | +20 | HYPE | DOWN | 0.71 | open |  |
| 10-11 16:23 | +15 | HYPE | DOWN | 0.71 | 0.88 | 1.49 |
| 10-11 16:23 | +10 | HYPE | DOWN | 0.71 | 0.82 | 0.86 |
| 10-11 16:23 | +5 | HYPE | DOWN | 0.71 | 0.76 | 0.24 |
| 10-11 16:22 | +10 stop | ZEC | DOWN | 0.63 | 0.81 | 1.52 |
| 10-11 16:22 | +5 | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-11 16:21 | +10 stop | BTC | DOWN | 0.63 | 0.76 | 1.00 |
| 10-11 16:21 | +10 stop | ZEC | UP | 0.53 | 0.34 | -2.24 |
| 10-11 16:21 | +10 | ZEC | UP | 0.53 | open |  |
| 10-11 16:21 | +5 | ZEC | UP | 0.53 | 0.61 | 0.46 |
| 10-11 16:20 | +10 stop | NEAR | UP | 0.68 | 0.81 | 1.03 |
| 10-11 16:20 | +10 stop | ZEC | DOWN | 0.51 | 0.66 | 1.16 |
| 10-11 16:20 | +20 | ZEC | DOWN | 0.51 | 0.81 | 2.71 |
| 10-11 16:20 | +15 | ZEC | DOWN | 0.52 | 0.67 | 1.16 |
| 10-11 16:20 | +10 | ZEC | DOWN | 0.53 | 0.66 | 0.96 |
| 10-11 16:20 | +5 | ZEC | DOWN | 0.52 | 0.66 | 1.06 |
| 10-11 16:20 | +10 stop | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 10-11 16:20 | +10 | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 10-11 16:20 | +5 | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 10-11 16:20 | +10 stop | ETH | DOWN | 0.56 | 0.41 | -1.85 |
| 10-11 16:18 | +10 stop | BNB | DOWN | 0.59 | 0.72 | 0.98 |
| 10-11 16:18 | +20 | BNB | DOWN | 0.59 | open |  |
| 10-11 16:18 | +15 | BNB | DOWN | 0.60 | 0.77 | 1.40 |
| 10-11 16:18 | +10 | BNB | DOWN | 0.60 | 0.72 | 0.88 |
| 10-11 16:18 | +5 | BNB | DOWN | 0.61 | 0.72 | 0.78 |
| 10-11 16:18 | +10 stop | ETH | DOWN | 0.57 | 0.69 | 0.87 |
| 10-11 16:18 | +10 stop | ZEC | DOWN | 0.66 | 0.79 | 1.02 |
| 10-11 16:18 | +10 | ZEC | DOWN | 0.66 | 0.79 | 1.02 |
| 10-11 16:18 | +5 | ZEC | DOWN | 0.66 | 0.74 | 0.50 |
| 10-11 16:17 | +10 stop | BTC | DOWN | 0.70 | 0.54 | -1.93 |
| 10-11 16:17 | +5 | HYPE | DOWN | 0.68 | 0.89 | 1.83 |
| 10-11 16:17 | +10 stop | XRP | DOWN | 0.65 | 0.78 | 1.04 |
| 10-11 16:17 | +20 | XRP | DOWN | 0.65 | 0.86 | 1.88 |
| 10-11 16:17 | +15 | XRP | DOWN | 0.65 | 0.82 | 1.46 |
| 10-11 16:17 | +10 | XRP | DOWN | 0.64 | 0.78 | 1.12 |
| 10-11 16:17 | +5 | XRP | DOWN | 0.64 | 0.69 | 0.23 |
| 10-11 16:17 | +10 stop | ZEC | DOWN | 0.59 | 0.72 | 0.98 |
| 10-11 16:17 | +20 | ZEC | DOWN | 0.59 | 0.79 | 1.71 |
