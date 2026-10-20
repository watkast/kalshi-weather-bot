# Range-Scalp Bot

*Updated Tue Oct 20 10:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25506 | 22211 | 3295 (31) | 0 | $-7447.37 | -4.6% |
| **+10¢** | 19200 | 15390 | 3810 (46) | 0 | $-6617.00 | -5.5% |
| **+15¢** | 16064 | 11962 | 4102 (70) | 0 | $-5945.49 | -5.9% |
| **+20¢** | 14204 | 9910 | 4294 (88) | 0 | $-5326.56 | -6.0% |
| **+10¢ (15¢ stop)** | 31316 | 31263 | 53 (30) | 0 | $-11578.60 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 10:25 | +10 stop | BNB | DOWN | 0.68 | 0.84 | 1.34 |
| 10-20 10:25 | +20 | BNB | DOWN | 0.68 | yes | -6.96 |
| 10-20 10:25 | +15 | BNB | DOWN | 0.68 | 0.84 | 1.34 |
| 10-20 10:25 | +10 | BNB | DOWN | 0.69 | 0.84 | 1.25 |
| 10-20 10:25 | +5 | BNB | DOWN | 0.68 | 0.73 | 0.20 |
| 10-20 10:23 | +10 stop | ZEC | DOWN | 0.71 | 0.84 | 1.05 |
| 10-20 10:23 | +10 stop | NEAR | DOWN | 0.63 | 0.74 | 0.79 |
| 10-20 10:23 | +10 stop | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-20 10:23 | +10 stop | ETH | DOWN | 0.60 | 0.86 | 2.34 |
| 10-20 10:22 | +10 stop | BTC | UP | 0.49 | 0.23 | -2.91 |
| 10-20 10:22 | +10 stop | ZEC | DOWN | 0.57 | 0.67 | 0.66 |
| 10-20 10:22 | +10 stop | HYPE | DOWN | 0.67 | 0.83 | 1.34 |
| 10-20 10:22 | +10 stop | XRP | DOWN | 0.62 | 0.81 | 1.62 |
| 10-20 10:21 | +20 | ZEC | UP | 0.64 | 0.86 | 1.94 |
| 10-20 10:20 | +10 stop | ZEC | UP | 0.66 | 0.50 | -1.94 |
| 10-20 10:20 | +15 | ZEC | UP | 0.66 | 0.86 | 1.75 |
| 10-20 10:20 | +10 | ZEC | UP | 0.66 | 0.86 | 1.75 |
| 10-20 10:20 | +10 stop | ETH | UP | 0.62 | 0.45 | -2.05 |
| 10-20 10:20 | +10 stop | BTC | UP | 0.69 | 0.53 | -1.93 |
| 10-20 10:20 | +10 stop | HYPE | UP | 0.68 | 0.48 | -2.34 |
| 10-20 10:20 | +10 | HYPE | UP | 0.68 | no | -6.99 |
| 10-20 10:20 | +5 | HYPE | UP | 0.67 | no | -6.90 |
| 10-20 10:19 | +10 stop | NEAR | UP | 0.63 | 0.79 | 1.31 |
| 10-20 10:19 | +10 stop | XRP | DOWN | 0.54 | 0.35 | -2.24 |
| 10-20 10:19 | +10 stop | BNB | UP | 0.68 | 0.88 | 1.76 |
| 10-20 10:19 | +15 | BNB | UP | 0.68 | 0.88 | 1.76 |
| 10-20 10:19 | +10 | BNB | UP | 0.68 | 0.88 | 1.76 |
| 10-20 10:19 | +5 | BNB | UP | 0.68 | 0.88 | 1.76 |
| 10-20 10:19 | +10 stop | DOGE | DOWN | 0.59 | 0.38 | -2.44 |
| 10-20 10:19 | +10 | DOGE | DOWN | 0.59 | 0.71 | 0.88 |
| 10-20 10:19 | +5 | DOGE | DOWN | 0.59 | 0.71 | 0.88 |
| 10-20 10:19 | +5 | SOL | DOWN | 0.62 | 0.70 | 0.48 |
| 10-20 10:18 | +5 | ZEC | DOWN | 0.63 | 0.70 | 0.38 |
| 10-20 10:18 | +5 | ETH | DOWN | 0.70 | 0.86 | 1.36 |
| 10-20 10:18 | +10 stop | ZEC | UP | 0.49 | 0.66 | 1.36 |
| 10-20 10:18 | +20 | ZEC | UP | 0.49 | 0.69 | 1.67 |
| 10-20 10:18 | +15 | ZEC | UP | 0.49 | 0.66 | 1.36 |
| 10-20 10:18 | +10 | ZEC | UP | 0.49 | 0.66 | 1.36 |
| 10-20 10:18 | +5 | ZEC | UP | 0.48 | 0.56 | 0.44 |
| 10-20 10:17 | +10 stop | XRP | DOWN | 0.71 | 0.56 | -1.83 |
