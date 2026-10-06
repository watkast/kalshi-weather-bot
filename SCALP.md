# Range-Scalp Bot

*Updated Tue Oct 06 21:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5509 | 4776 | 733 (9) | 0 | $-1678.34 | -4.8% |
| **+10¢** | 4207 | 3346 | 861 (14) | 1 | $-1595.65 | -6.0% |
| **+15¢** | 3528 | 2615 | 913 (18) | 1 | $-1388.80 | -6.3% |
| **+20¢** | 3152 | 2204 | 948 (25) | 2 | $-1107.35 | -5.6% |
| **+10¢ (15¢ stop)** | 6709 | 6694 | 15 (9) | 0 | $-2397.93 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 21:43 | +10 stop | ETH | DOWN | 0.71 | 0.42 | -3.23 |
| 10-06 21:43 | +5 | ETH | DOWN | 0.71 | 0.99 | 2.62 |
| 10-06 21:41 | +10 stop | ETH | UP | 0.67 | 0.31 | -3.91 |
| 10-06 21:39 | +10 stop | DOGE | DOWN | 0.70 | 0.84 | 1.15 |
| 10-06 21:39 | +20 | DOGE | DOWN | 0.70 | 0.92 | 2.03 |
| 10-06 21:39 | +15 | DOGE | DOWN | 0.70 | 0.85 | 1.26 |
| 10-06 21:39 | +10 | DOGE | DOWN | 0.70 | 0.84 | 1.15 |
| 10-06 21:39 | +5 | DOGE | DOWN | 0.70 | 0.78 | 0.52 |
| 10-06 21:39 | +10 stop | BNB | DOWN | 0.51 | 0.64 | 0.95 |
| 10-06 21:39 | +20 | BNB | DOWN | 0.51 | 0.78 | 2.39 |
| 10-06 21:39 | +15 | BNB | DOWN | 0.51 | 0.78 | 2.39 |
| 10-06 21:39 | +10 | BNB | DOWN | 0.51 | 0.64 | 0.95 |
| 10-06 21:39 | +5 | BNB | DOWN | 0.51 | 0.64 | 0.95 |
| 10-06 21:39 | +10 stop | HYPE | DOWN | 0.59 | 0.79 | 1.71 |
| 10-06 21:39 | +15 | HYPE | DOWN | 0.59 | 0.79 | 1.71 |
| 10-06 21:39 | +10 | HYPE | DOWN | 0.59 | 0.79 | 1.71 |
| 10-06 21:39 | +5 | HYPE | DOWN | 0.59 | 0.79 | 1.71 |
| 10-06 21:38 | +10 stop | ETH | DOWN | 0.62 | 0.40 | -2.54 |
| 10-06 21:38 | +20 | ETH | DOWN | 0.62 | 0.99 | 3.50 |
| 10-06 21:38 | +15 | ETH | DOWN | 0.62 | 0.99 | 3.50 |
| 10-06 21:38 | +10 | ETH | DOWN | 0.62 | 0.72 | 0.68 |
| 10-06 21:38 | +5 | ETH | DOWN | 0.62 | 0.68 | 0.27 |
| 10-06 21:38 | +10 stop | BTC | UP | 0.68 | 0.82 | 1.13 |
| 10-06 21:38 | +15 | BTC | UP | 0.68 | 0.90 | 1.97 |
| 10-06 21:38 | +10 | BTC | UP | 0.68 | 0.82 | 1.13 |
| 10-06 21:38 | +5 | BTC | UP | 0.68 | 0.73 | 0.20 |
| 10-06 21:38 | +10 stop | HYPE | UP | 0.44 | 0.62 | 1.45 |
| 10-06 21:38 | +20 | HYPE | UP | 0.44 | open |  |
| 10-06 21:38 | +15 | HYPE | UP | 0.44 | 0.62 | 1.45 |
| 10-06 21:38 | +10 | HYPE | UP | 0.44 | 0.62 | 1.45 |
| 10-06 21:38 | +5 | HYPE | UP | 0.44 | 0.62 | 1.45 |
| 10-06 21:37 | +10 stop | XRP | DOWN | 0.60 | 0.89 | 2.66 |
| 10-06 21:37 | +5 | XRP | DOWN | 0.60 | 0.89 | 2.66 |
| 10-06 21:36 | +5 | XRP | UP | 0.47 | 0.62 | 1.15 |
| 10-06 21:34 | +10 stop | XRP | UP | 0.66 | 0.47 | -2.24 |
| 10-06 21:34 | +15 | XRP | UP | 0.66 | open |  |
| 10-06 21:34 | +10 | XRP | UP | 0.66 | open |  |
| 10-06 21:34 | +5 | XRP | UP | 0.66 | 0.71 | 0.19 |
| 10-06 21:32 | +5 | BTC | UP | 0.67 | 0.72 | 0.19 |
| 10-06 21:31 | +10 stop | BNB | UP | 0.66 | 0.77 | 0.81 |
