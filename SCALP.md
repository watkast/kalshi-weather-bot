# Range-Scalp Bot

*Updated Thu Oct 22 21:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29286 | 25492 | 3794 (39) | 0 | $-8626.82 | -4.7% |
| **+10¢** | 21969 | 17578 | 4391 (55) | 0 | $-7761.25 | -5.6% |
| **+15¢** | 18393 | 13676 | 4717 (78) | 0 | $-6953.87 | -6.0% |
| **+20¢** | 16282 | 11336 | 4946 (100) | 0 | $-6294.90 | -6.2% |
| **+10¢ (15¢ stop)** | 35943 | 35884 | 59 (32) | 0 | $-13551.51 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 21:06 | +10 stop | ZEC | UP | 0.52 | 0.65 | 0.96 |
| 10-22 21:06 | +10 stop | SOL | UP | 0.61 | 0.81 | 1.72 |
| 10-22 21:05 | +5 | BNB | DOWN | 0.70 | yes | -7.15 |
| 10-22 21:04 | +10 stop | DOGE | UP | 0.63 | 0.83 | 1.73 |
| 10-22 21:03 | +10 stop | NEAR | UP | 0.54 | 0.64 | 0.65 |
| 10-22 21:03 | +5 | HYPE | UP | 0.71 | 0.79 | 0.53 |
| 10-22 21:03 | +5 | SOL | DOWN | 0.57 | yes | -5.92 |
| 10-22 21:03 | +10 stop | ETH | DOWN | 0.58 | 0.43 | -1.86 |
| 10-22 21:03 | +10 | ETH | DOWN | 0.58 | yes | -5.98 |
| 10-22 21:03 | +5 | ETH | DOWN | 0.58 | yes | -5.98 |
| 10-22 21:02 | +5 | SOL | DOWN | 0.60 | 0.67 | 0.37 |
| 10-22 21:02 | +10 stop | BTC | DOWN | 0.55 | 0.31 | -2.73 |
| 10-22 21:01 | +10 stop | ZEC | DOWN | 0.64 | 0.39 | -2.84 |
| 10-22 21:01 | +20 | ZEC | DOWN | 0.64 | yes | -6.57 |
| 10-22 21:01 | +15 | ZEC | DOWN | 0.64 | yes | -6.57 |
| 10-22 21:01 | +10 | ZEC | DOWN | 0.64 | yes | -6.57 |
| 10-22 21:01 | +5 | ZEC | DOWN | 0.64 | yes | -6.57 |
| 10-22 21:01 | +10 stop | DOGE | UP | 0.65 | 0.50 | -1.84 |
| 10-22 21:01 | +20 | DOGE | UP | 0.65 | 0.85 | 1.75 |
| 10-22 21:01 | +15 | DOGE | UP | 0.65 | 0.83 | 1.54 |
| 10-22 21:01 | +10 | DOGE | UP | 0.65 | 0.83 | 1.54 |
| 10-22 21:01 | +5 | DOGE | UP | 0.65 | 0.70 | 0.19 |
| 10-22 21:01 | +10 stop | BNB | DOWN | 0.64 | 0.36 | -3.14 |
| 10-22 21:01 | +20 | BNB | DOWN | 0.66 | yes | -6.76 |
| 10-22 21:01 | +15 | BNB | DOWN | 0.66 | yes | -6.76 |
| 10-22 21:01 | +10 | BNB | DOWN | 0.66 | yes | -6.76 |
| 10-22 21:01 | +5 | BNB | DOWN | 0.66 | 0.72 | 0.29 |
| 10-22 21:01 | +10 stop | HYPE | UP | 0.57 | 0.71 | 1.07 |
| 10-22 21:01 | +20 | HYPE | UP | 0.56 | 0.79 | 2.00 |
| 10-22 21:01 | +15 | HYPE | UP | 0.57 | 0.73 | 1.28 |
| 10-22 21:01 | +10 | HYPE | UP | 0.58 | 0.71 | 0.97 |
| 10-22 21:01 | +5 | HYPE | UP | 0.58 | 0.66 | 0.46 |
| 10-22 21:01 | +10 stop | XRP | UP | 0.64 | 0.74 | 0.69 |
| 10-22 21:01 | +20 | XRP | UP | 0.66 | 0.92 | 2.38 |
| 10-22 21:01 | +15 | XRP | UP | 0.66 | 0.82 | 1.33 |
| 10-22 21:01 | +10 | XRP | UP | 0.66 | 0.78 | 0.91 |
| 10-22 21:01 | +5 | XRP | UP | 0.66 | 0.74 | 0.50 |
| 10-22 21:01 | +10 stop | BTC | UP | 0.57 | 0.40 | -2.05 |
| 10-22 21:01 | +20 | BTC | UP | 0.57 | 0.81 | 2.11 |
| 10-22 21:01 | +15 | BTC | UP | 0.57 | 0.81 | 2.11 |
