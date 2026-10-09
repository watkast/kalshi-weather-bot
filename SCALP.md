# Range-Scalp Bot

*Updated Fri Oct 09 00:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8214 | 7106 | 1108 (13) | 2 | $-2678.43 | -5.2% |
| **+10¢** | 6219 | 4908 | 1311 (25) | 2 | $-2648.33 | -6.8% |
| **+15¢** | 5240 | 3861 | 1379 (37) | 3 | $-2154.94 | -6.6% |
| **+20¢** | 4670 | 3238 | 1432 (45) | 4 | $-1767.03 | -6.0% |
| **+10¢ (15¢ stop)** | 9977 | 9947 | 30 (19) | 0 | $-3695.09 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 00:09 | +10 stop | BNB | UP | 0.66 | 0.81 | 1.23 |
| 10-09 00:08 | +10 stop | ZEC | UP | 0.68 | 0.82 | 1.10 |
| 10-09 00:08 | +5 | ZEC | UP | 0.69 | 0.76 | 0.43 |
| 10-09 00:08 | +10 stop | HYPE | UP | 0.57 | 0.74 | 1.38 |
| 10-09 00:07 | +10 stop | BTC | UP | 0.68 | 0.83 | 1.24 |
| 10-09 00:07 | +15 | BTC | UP | 0.68 | 0.83 | 1.24 |
| 10-09 00:07 | +10 | BTC | UP | 0.68 | 0.83 | 1.24 |
| 10-09 00:07 | +5 | BTC | UP | 0.66 | 0.73 | 0.40 |
| 10-09 00:07 | +10 stop | BNB | DOWN | 0.64 | 0.42 | -2.55 |
| 10-09 00:07 | +20 | BNB | DOWN | 0.64 | open |  |
| 10-09 00:07 | +15 | BNB | DOWN | 0.64 | open |  |
| 10-09 00:07 | +10 | BNB | DOWN | 0.64 | open |  |
| 10-09 00:07 | +5 | BNB | DOWN | 0.64 | open |  |
| 10-09 00:06 | +5 | ZEC | UP | 0.57 | 0.64 | 0.37 |
| 10-09 00:06 | +10 stop | SOL | DOWN | 0.60 | 0.70 | 0.68 |
| 10-09 00:06 | +15 | SOL | DOWN | 0.60 | 0.75 | 1.19 |
| 10-09 00:06 | +10 | SOL | DOWN | 0.60 | 0.70 | 0.68 |
| 10-09 00:06 | +5 | SOL | DOWN | 0.60 | 0.69 | 0.58 |
| 10-09 00:05 | +10 stop | HYPE | UP | 0.62 | 0.33 | -3.23 |
| 10-09 00:05 | +10 stop | ZEC | UP | 0.71 | 0.48 | -2.63 |
| 10-09 00:05 | +10 | ZEC | UP | 0.71 | 0.82 | 0.84 |
| 10-09 00:05 | +5 | ZEC | UP | 0.71 | 0.76 | 0.22 |
| 10-09 00:04 | +10 stop | HYPE | DOWN | 0.64 | 0.43 | -2.45 |
| 10-09 00:04 | +20 | HYPE | DOWN | 0.64 | open |  |
| 10-09 00:04 | +15 | HYPE | DOWN | 0.64 | open |  |
| 10-09 00:04 | +10 | HYPE | DOWN | 0.64 | open |  |
| 10-09 00:04 | +5 | HYPE | DOWN | 0.64 | open |  |
| 10-09 00:04 | +10 stop | BTC | UP | 0.67 | 0.77 | 0.71 |
| 10-09 00:04 | +10 stop | NEAR | DOWN | 0.61 | 0.35 | -2.93 |
| 10-09 00:03 | +10 stop | DOGE | UP | 0.69 | 0.81 | 0.94 |
| 10-09 00:03 | +20 | DOGE | UP | 0.69 | 0.89 | 1.78 |
| 10-09 00:03 | +15 | DOGE | UP | 0.69 | 0.89 | 1.78 |
| 10-09 00:03 | +10 | DOGE | UP | 0.69 | 0.81 | 0.94 |
| 10-09 00:03 | +5 | DOGE | UP | 0.69 | 0.77 | 0.52 |
| 10-09 00:03 | +10 stop | ETH | UP | 0.57 | 0.72 | 1.17 |
| 10-09 00:03 | +20 | ETH | UP | 0.57 | 0.79 | 1.90 |
| 10-09 00:03 | +15 | ETH | UP | 0.57 | 0.72 | 1.17 |
| 10-09 00:03 | +10 | ETH | UP | 0.57 | 0.72 | 1.17 |
| 10-09 00:03 | +5 | ETH | UP | 0.57 | 0.72 | 1.17 |
| 10-09 00:02 | +10 stop | HYPE | DOWN | 0.53 | 0.67 | 1.06 |
