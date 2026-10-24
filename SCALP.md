# Range-Scalp Bot

*Updated Sat Oct 24 03:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31387 | 27354 | 4033 (40) | 4 | $-9051.64 | -4.6% |
| **+10¢** | 23482 | 18824 | 4658 (58) | 4 | $-8038.87 | -5.4% |
| **+15¢** | 19656 | 14650 | 5006 (81) | 3 | $-7170.74 | -5.8% |
| **+20¢** | 17411 | 12168 | 5243 (103) | 3 | $-6394.60 | -5.8% |
| **+10¢ (15¢ stop)** | 38529 | 38470 | 59 (32) | 0 | $-14696.03 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 03:43 | +10 stop | SOL | UP | 0.69 | 0.95 | 2.42 |
| 10-24 03:42 | +10 stop | BTC | DOWN | 0.68 | 0.81 | 1.03 |
| 10-24 03:41 | +10 stop | SOL | UP | 0.59 | 0.39 | -2.34 |
| 10-24 03:41 | +10 stop | NEAR | DOWN | 0.65 | 0.76 | 0.83 |
| 10-24 03:41 | +20 | NEAR | DOWN | 0.65 | 0.94 | 2.75 |
| 10-24 03:41 | +15 | NEAR | DOWN | 0.65 | 0.81 | 1.35 |
| 10-24 03:41 | +10 | NEAR | DOWN | 0.65 | 0.76 | 0.83 |
| 10-24 03:41 | +5 | NEAR | DOWN | 0.65 | 0.73 | 0.52 |
| 10-24 03:40 | +10 stop | HYPE | DOWN | 0.55 | 0.29 | -2.93 |
| 10-24 03:40 | +10 stop | SOL | DOWN | 0.49 | 0.25 | -2.72 |
| 10-24 03:40 | +10 | SOL | DOWN | 0.50 | open |  |
| 10-24 03:40 | +5 | SOL | DOWN | 0.55 | open |  |
| 10-24 03:40 | +10 stop | DOGE | DOWN | 0.66 | 0.50 | -1.94 |
| 10-24 03:40 | +15 | DOGE | DOWN | 0.66 | 0.96 | 2.85 |
| 10-24 03:40 | +10 | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 10-24 03:38 | +5 | BNB | DOWN | 0.64 | 0.73 | 0.59 |
| 10-24 03:37 | +10 stop | BTC | UP | 0.61 | 0.27 | -3.71 |
| 10-24 03:37 | +10 stop | DOGE | UP | 0.52 | 0.32 | -2.34 |
| 10-24 03:37 | +10 stop | XRP | DOWN | 0.66 | 0.87 | 1.83 |
| 10-24 03:37 | +10 stop | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 10-24 03:37 | +15 | NEAR | DOWN | 0.68 | 0.83 | 1.24 |
| 10-24 03:37 | +10 | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 10-24 03:37 | +5 | NEAR | DOWN | 0.68 | 0.77 | 0.61 |
| 10-24 03:37 | +5 | DOGE | UP | 0.51 | open |  |
| 10-24 03:37 | +15 | XRP | DOWN | 0.67 | 0.87 | 1.76 |
| 10-24 03:37 | +10 | XRP | DOWN | 0.67 | 0.87 | 1.76 |
| 10-24 03:37 | +5 | XRP | DOWN | 0.67 | 0.72 | 0.19 |
| 10-24 03:36 | +5 | DOGE | DOWN | 0.45 | 0.56 | 0.77 |
| 10-24 03:36 | +5 | BNB | DOWN | 0.50 | 0.61 | 0.75 |
| 10-24 03:36 | +10 stop | ETH | DOWN | 0.47 | 0.60 | 0.95 |
| 10-24 03:36 | +10 stop | DOGE | DOWN | 0.62 | 0.43 | -2.25 |
| 10-24 03:36 | +10 stop | HYPE | DOWN | 0.61 | 0.46 | -1.89 |
| 10-24 03:35 | +10 stop | SOL | UP | 0.64 | 0.78 | 1.10 |
| 10-24 03:35 | +15 | SOL | UP | 0.64 | 0.95 | 2.90 |
| 10-24 03:35 | +10 | SOL | UP | 0.64 | 0.78 | 1.10 |
| 10-24 03:35 | +5 | SOL | UP | 0.64 | 0.78 | 1.10 |
| 10-24 03:35 | +10 stop | XRP | DOWN | 0.71 | 0.56 | -1.83 |
| 10-24 03:35 | +10 stop | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 10-24 03:35 | +5 | BTC | UP | 0.70 | open |  |
| 10-24 03:34 | +10 stop | BNB | DOWN | 0.55 | 0.73 | 1.48 |
