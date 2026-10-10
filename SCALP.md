# Range-Scalp Bot

*Updated Sat Oct 10 12:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10416 | 8982 | 1434 (22) | 1 | $-3538.96 | -5.4% |
| **+10¢** | 7886 | 6215 | 1671 (36) | 1 | $-3371.86 | -6.8% |
| **+15¢** | 6652 | 4880 | 1772 (52) | 0 | $-2854.09 | -6.8% |
| **+20¢** | 5915 | 4069 | 1846 (66) | 1 | $-2423.61 | -6.5% |
| **+10¢ (15¢ stop)** | 12806 | 12768 | 38 (25) | 0 | $-5023.11 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 12:42 | +10 stop | ZEC | DOWN | 0.30 | 0.58 | 2.49 |
| 10-10 12:41 | +10 stop | BTC | UP | 0.62 | 0.74 | 0.89 |
| 10-10 12:40 | +10 stop | ZEC | DOWN | 0.68 | 0.50 | -2.14 |
| 10-10 12:39 | +10 stop | ETH | UP | 0.62 | 0.76 | 1.10 |
| 10-10 12:37 | +10 stop | ZEC | DOWN | 0.70 | 0.55 | -1.83 |
| 10-10 12:37 | +10 stop | BTC | DOWN | 0.60 | 0.45 | -1.85 |
| 10-10 12:37 | +10 stop | HYPE | DOWN | 0.58 | 0.70 | 0.88 |
| 10-10 12:37 | +10 stop | XRP | DOWN | 0.67 | 0.51 | -1.94 |
| 10-10 12:37 | +10 stop | BNB | DOWN | 0.69 | 0.43 | -2.93 |
| 10-10 12:37 | +5 | DOGE | UP | 0.68 | 0.77 | 0.61 |
| 10-10 12:37 | +10 stop | ETH | DOWN | 0.57 | 0.36 | -2.43 |
| 10-10 12:37 | +10 | ETH | DOWN | 0.57 | open |  |
| 10-10 12:37 | +5 | ETH | DOWN | 0.57 | open |  |
| 10-10 12:35 | +10 stop | ZEC | UP | 0.60 | 0.70 | 0.70 |
| 10-10 12:35 | +10 stop | DOGE | UP | 0.70 | 0.85 | 1.30 |
| 10-10 12:35 | +20 | DOGE | UP | 0.70 | 0.94 | 2.29 |
| 10-10 12:35 | +15 | DOGE | UP | 0.70 | 0.85 | 1.30 |
| 10-10 12:35 | +10 | DOGE | UP | 0.70 | 0.85 | 1.30 |
| 10-10 12:35 | +5 | DOGE | UP | 0.70 | 0.77 | 0.46 |
| 10-10 12:34 | +10 stop | XRP | DOWN | 0.56 | 0.68 | 0.91 |
| 10-10 12:34 | +10 stop | ZEC | UP | 0.50 | 0.60 | 0.67 |
| 10-10 12:34 | +10 stop | HYPE | UP | 0.68 | 0.47 | -2.48 |
| 10-10 12:34 | +10 | HYPE | UP | 0.68 | 0.84 | 1.30 |
| 10-10 12:34 | +5 | HYPE | UP | 0.68 | 0.84 | 1.30 |
| 10-10 12:33 | +5 | BNB | UP | 0.60 | 0.81 | 1.82 |
| 10-10 12:32 | +10 stop | ZEC | UP | 0.66 | 0.48 | -2.14 |
| 10-10 12:32 | +20 | ZEC | UP | 0.66 | 0.91 | 2.32 |
| 10-10 12:32 | +15 | ZEC | UP | 0.66 | 0.81 | 1.23 |
| 10-10 12:32 | +10 | ZEC | UP | 0.66 | 0.80 | 1.12 |
| 10-10 12:32 | +5 | ZEC | UP | 0.66 | 0.80 | 1.12 |
| 10-10 12:32 | +5 | XRP | UP | 0.68 | 0.75 | 0.40 |
| 10-10 12:31 | +10 stop | DOGE | UP | 0.61 | 0.76 | 1.20 |
| 10-10 12:31 | +20 | DOGE | UP | 0.61 | 0.82 | 1.82 |
| 10-10 12:31 | +15 | DOGE | UP | 0.61 | 0.76 | 1.20 |
| 10-10 12:31 | +10 | DOGE | UP | 0.61 | 0.76 | 1.20 |
| 10-10 12:31 | +5 | DOGE | UP | 0.61 | 0.66 | 0.17 |
| 10-10 12:31 | +10 stop | NEAR | DOWN | 0.59 | 0.69 | 0.71 |
| 10-10 12:31 | +20 | NEAR | DOWN | 0.59 | 0.79 | 1.74 |
| 10-10 12:31 | +15 | NEAR | DOWN | 0.59 | 0.78 | 1.63 |
| 10-10 12:31 | +10 | NEAR | DOWN | 0.59 | 0.69 | 0.71 |
