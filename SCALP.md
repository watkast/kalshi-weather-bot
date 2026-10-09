# Range-Scalp Bot

*Updated Fri Oct 09 03:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8421 | 7283 | 1138 (13) | 0 | $-2755.36 | -5.2% |
| **+10¢** | 6382 | 5037 | 1345 (25) | 0 | $-2714.41 | -6.8% |
| **+15¢** | 5386 | 3970 | 1416 (37) | 0 | $-2204.93 | -6.5% |
| **+20¢** | 4792 | 3323 | 1469 (45) | 0 | $-1825.01 | -6.1% |
| **+10¢ (15¢ stop)** | 10234 | 10204 | 30 (19) | 0 | $-3756.88 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 02:51 | +10 stop | NEAR | UP | 0.68 | 0.84 | 1.34 |
| 10-09 02:50 | +10 stop | NEAR | DOWN | 0.58 | 0.37 | -2.43 |
| 10-09 02:49 | +5 | NEAR | UP | 0.62 | 0.74 | 0.89 |
| 10-09 02:49 | +10 stop | XRP | UP | 0.69 | 0.89 | 1.78 |
| 10-09 02:48 | +10 stop | HYPE | UP | 0.62 | 0.72 | 0.68 |
| 10-09 02:48 | +10 stop | ETH | UP | 0.67 | 0.80 | 1.02 |
| 10-09 02:47 | +10 stop | HYPE | UP | 0.48 | 0.60 | 0.81 |
| 10-09 02:47 | +10 stop | NEAR | UP | 0.57 | 0.42 | -1.86 |
| 10-09 02:47 | +20 | NEAR | UP | 0.57 | 0.84 | 2.42 |
| 10-09 02:47 | +15 | NEAR | UP | 0.57 | 0.74 | 1.38 |
| 10-09 02:47 | +10 | NEAR | UP | 0.57 | 0.74 | 1.38 |
| 10-09 02:47 | +5 | NEAR | UP | 0.57 | 0.63 | 0.25 |
| 10-09 02:47 | +5 | BTC | UP | 0.66 | 0.77 | 0.81 |
| 10-09 02:47 | +10 stop | XRP | UP | 0.55 | 0.67 | 0.86 |
| 10-09 02:47 | +10 stop | ETH | DOWN | 0.52 | 0.31 | -2.43 |
| 10-09 02:47 | +20 | ETH | DOWN | 0.52 | yes | -5.38 |
| 10-09 02:47 | +15 | ETH | DOWN | 0.52 | yes | -5.38 |
| 10-09 02:47 | +10 | ETH | DOWN | 0.52 | yes | -5.38 |
| 10-09 02:47 | +5 | ETH | DOWN | 0.52 | yes | -5.38 |
| 10-09 02:47 | +10 stop | DOGE | DOWN | 0.56 | 0.40 | -1.95 |
| 10-09 02:47 | +20 | DOGE | DOWN | 0.56 | yes | -5.78 |
| 10-09 02:47 | +15 | DOGE | DOWN | 0.56 | yes | -5.78 |
| 10-09 02:47 | +10 | DOGE | DOWN | 0.56 | yes | -5.78 |
| 10-09 02:47 | +5 | DOGE | DOWN | 0.56 | yes | -5.78 |
| 10-09 02:47 | +10 stop | HYPE | DOWN | 0.57 | 0.42 | -1.86 |
| 10-09 02:47 | +20 | HYPE | DOWN | 0.57 | yes | -5.88 |
| 10-09 02:47 | +15 | HYPE | DOWN | 0.57 | yes | -5.88 |
| 10-09 02:47 | +10 | HYPE | DOWN | 0.57 | yes | -5.88 |
| 10-09 02:47 | +5 | HYPE | DOWN | 0.57 | yes | -5.88 |
| 10-09 02:47 | +10 stop | BTC | DOWN | 0.57 | 0.35 | -2.54 |
| 10-09 02:47 | +20 | BTC | DOWN | 0.57 | yes | -5.88 |
| 10-09 02:47 | +15 | BTC | DOWN | 0.57 | yes | -5.88 |
| 10-09 02:47 | +10 | BTC | DOWN | 0.57 | yes | -5.88 |
| 10-09 02:47 | +5 | BTC | DOWN | 0.57 | 0.62 | 0.15 |
| 10-09 02:46 | +10 stop | ZEC | UP | 0.70 | 0.83 | 1.05 |
| 10-09 02:46 | +20 | ZEC | UP | 0.70 | 0.92 | 1.96 |
| 10-09 02:46 | +15 | ZEC | UP | 0.70 | 0.85 | 1.26 |
| 10-09 02:46 | +10 | ZEC | UP | 0.70 | 0.83 | 1.05 |
| 10-09 02:46 | +5 | ZEC | UP | 0.70 | 0.83 | 1.05 |
| 10-09 02:46 | +10 stop | BNB | UP | 0.53 | 0.64 | 0.75 |
