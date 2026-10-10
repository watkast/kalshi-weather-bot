# Range-Scalp Bot

*Updated Sat Oct 10 05:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10008 | 8632 | 1376 (18) | 0 | $-3412.92 | -5.4% |
| **+10¢** | 7564 | 5960 | 1604 (30) | 0 | $-3288.47 | -6.9% |
| **+15¢** | 6387 | 4696 | 1691 (43) | 0 | $-2719.72 | -6.8% |
| **+20¢** | 5676 | 3920 | 1756 (55) | 0 | $-2279.32 | -6.4% |
| **+10¢ (15¢ stop)** | 12290 | 12255 | 35 (22) | 0 | $-4832.84 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 05:25 | +10 stop | HYPE | DOWN | 0.65 | 0.78 | 1.01 |
| 10-10 05:23 | +10 stop | ZEC | UP | 0.61 | 0.43 | -2.15 |
| 10-10 05:23 | +10 stop | HYPE | UP | 0.56 | 0.39 | -2.05 |
| 10-10 05:23 | +20 | HYPE | UP | 0.56 | 0.86 | 2.73 |
| 10-10 05:23 | +15 | HYPE | UP | 0.56 | 0.86 | 2.73 |
| 10-10 05:23 | +10 | HYPE | UP | 0.56 | 0.86 | 2.73 |
| 10-10 05:23 | +5 | HYPE | UP | 0.56 | 0.86 | 2.73 |
| 10-10 05:23 | +10 stop | XRP | DOWN | 0.66 | 0.84 | 1.54 |
| 10-10 05:23 | +20 | XRP | DOWN | 0.66 | 0.89 | 2.07 |
| 10-10 05:23 | +10 | XRP | DOWN | 0.66 | 0.84 | 1.54 |
| 10-10 05:23 | +5 | XRP | DOWN | 0.66 | 0.73 | 0.40 |
| 10-10 05:18 | +15 | XRP | DOWN | 0.71 | 0.89 | 1.58 |
| 10-10 05:18 | +10 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 10-10 05:18 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
| 10-10 05:18 | +5 | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 10-10 05:18 | +10 | DOGE | DOWN | 0.71 | 0.82 | 0.86 |
| 10-10 05:17 | +10 stop | HYPE | DOWN | 0.65 | 0.80 | 1.18 |
| 10-10 05:17 | +10 | HYPE | DOWN | 0.65 | 0.80 | 1.18 |
| 10-10 05:17 | +5 | HYPE | DOWN | 0.64 | 0.71 | 0.34 |
| 10-10 05:17 | +10 stop | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 10-10 05:17 | +20 | SOL | DOWN | 0.59 | 0.82 | 2.02 |
| 10-10 05:17 | +15 | SOL | DOWN | 0.59 | 0.74 | 1.19 |
| 10-10 05:17 | +10 | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 10-10 05:17 | +5 | SOL | DOWN | 0.59 | 0.66 | 0.37 |
| 10-10 05:17 | +5 | NEAR | UP | 0.59 | 0.79 | 1.68 |
| 10-10 05:16 | +10 stop | ZEC | UP | 0.58 | 0.37 | -2.49 |
| 10-10 05:16 | +20 | ZEC | UP | 0.58 | no | -6.02 |
| 10-10 05:16 | +15 | ZEC | UP | 0.58 | no | -6.02 |
| 10-10 05:16 | +10 | ZEC | UP | 0.59 | no | -6.07 |
| 10-10 05:16 | +5 | ZEC | UP | 0.59 | no | -6.07 |
| 10-10 05:16 | +10 stop | NEAR | DOWN | 0.46 | 0.19 | -3.01 |
| 10-10 05:16 | +20 | NEAR | DOWN | 0.46 | yes | -4.80 |
| 10-10 05:16 | +15 | NEAR | DOWN | 0.46 | yes | -4.80 |
| 10-10 05:16 | +10 | NEAR | DOWN | 0.46 | yes | -4.80 |
| 10-10 05:16 | +5 | NEAR | DOWN | 0.46 | 0.53 | 0.32 |
| 10-10 05:16 | +10 stop | ETH | DOWN | 0.67 | 0.81 | 1.17 |
| 10-10 05:16 | +20 | ETH | DOWN | 0.67 | 0.88 | 1.86 |
| 10-10 05:16 | +15 | ETH | DOWN | 0.67 | 0.84 | 1.44 |
| 10-10 05:16 | +10 | ETH | DOWN | 0.67 | 0.81 | 1.13 |
| 10-10 05:16 | +5 | ETH | DOWN | 0.67 | 0.76 | 0.63 |
