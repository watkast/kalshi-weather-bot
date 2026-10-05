# Range-Scalp Bot

*Updated Mon Oct 05 20:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4266 | 3675 | 591 (4) | 1 | $-1479.83 | -5.5% |
| **+10¢** | 3290 | 2607 | 683 (5) | 1 | $-1362.13 | -6.6% |
| **+15¢** | 2758 | 2037 | 721 (8) | 1 | $-1184.44 | -6.8% |
| **+20¢** | 2465 | 1713 | 752 (13) | 1 | $-1020.10 | -6.6% |
| **+10¢ (15¢ stop)** | 5253 | 5248 | 5 (2) | 0 | $-1905.56 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 20:25 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-05 20:24 | +10 stop | NEAR | DOWN | 0.64 | 0.77 | 1.00 |
| 10-05 20:24 | +5 | NEAR | DOWN | 0.63 | 0.77 | 1.07 |
| 10-05 20:21 | +5 | NEAR | DOWN | 0.64 | 0.69 | 0.18 |
| 10-05 20:21 | +10 stop | NEAR | DOWN | 0.69 | 0.51 | -2.13 |
| 10-05 20:21 | +10 stop | ZEC | UP | 0.51 | 0.32 | -2.24 |
| 10-05 20:20 | +10 stop | NEAR | UP | 0.54 | 0.33 | -2.44 |
| 10-05 20:19 | +10 stop | ZEC | DOWN | 0.59 | 0.42 | -2.05 |
| 10-05 20:18 | +5 | ZEC | UP | 0.65 | open |  |
| 10-05 20:16 | +10 stop | ZEC | UP | 0.61 | 0.42 | -2.25 |
| 10-05 20:16 | +20 | ZEC | UP | 0.61 | open |  |
| 10-05 20:16 | +15 | ZEC | UP | 0.61 | open |  |
| 10-05 20:16 | +10 | ZEC | UP | 0.61 | open |  |
| 10-05 20:16 | +5 | ZEC | UP | 0.61 | 0.69 | 0.48 |
| 10-05 20:16 | +10 stop | HYPE | UP | 0.63 | 0.80 | 1.41 |
| 10-05 20:16 | +20 | HYPE | UP | 0.63 | 0.86 | 2.04 |
| 10-05 20:16 | +15 | HYPE | UP | 0.63 | 0.80 | 1.41 |
| 10-05 20:16 | +10 | HYPE | UP | 0.63 | 0.80 | 1.41 |
| 10-05 20:16 | +5 | HYPE | UP | 0.63 | 0.80 | 1.41 |
| 10-05 20:16 | +10 stop | XRP | UP | 0.66 | 0.80 | 1.12 |
| 10-05 20:16 | +20 | XRP | UP | 0.66 | 0.87 | 1.86 |
| 10-05 20:16 | +15 | XRP | UP | 0.66 | 0.81 | 1.23 |
| 10-05 20:16 | +10 | XRP | UP | 0.66 | 0.80 | 1.12 |
| 10-05 20:16 | +5 | XRP | UP | 0.66 | 0.73 | 0.40 |
| 10-05 20:16 | +10 stop | NEAR | DOWN | 0.63 | 0.30 | -3.62 |
| 10-05 20:16 | +20 | NEAR | DOWN | 0.63 | 0.88 | 2.25 |
| 10-05 20:16 | +15 | NEAR | DOWN | 0.63 | 0.88 | 2.25 |
| 10-05 20:16 | +10 | NEAR | DOWN | 0.63 | 0.77 | 1.10 |
| 10-05 20:16 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 10-05 20:16 | +10 stop | BTC | UP | 0.62 | 0.72 | 0.68 |
| 10-05 20:16 | +20 | BTC | UP | 0.62 | 0.82 | 1.72 |
| 10-05 20:16 | +15 | BTC | UP | 0.62 | 0.78 | 1.30 |
| 10-05 20:16 | +10 | BTC | UP | 0.62 | 0.72 | 0.68 |
| 10-05 20:16 | +5 | BTC | UP | 0.62 | 0.72 | 0.68 |
| 10-05 20:16 | +10 stop | DOGE | UP | 0.65 | 0.77 | 0.91 |
| 10-05 20:16 | +20 | DOGE | UP | 0.65 | 0.87 | 1.96 |
| 10-05 20:16 | +15 | DOGE | UP | 0.65 | 0.80 | 1.22 |
| 10-05 20:16 | +10 | DOGE | UP | 0.65 | 0.77 | 0.91 |
| 10-05 20:16 | +5 | DOGE | UP | 0.65 | 0.77 | 0.91 |
| 10-05 20:16 | +10 stop | SOL | UP | 0.56 | 0.68 | 0.86 |
