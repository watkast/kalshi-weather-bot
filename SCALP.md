# Range-Scalp Bot

*Updated Mon Oct 05 03:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3191 | 2731 | 460 (3) | 0 | $-1206.85 | -6.0% |
| **+10¢** | 2477 | 1955 | 522 (4) | 0 | $-1070.68 | -6.9% |
| **+15¢** | 2091 | 1541 | 550 (5) | 0 | $-938.99 | -7.2% |
| **+20¢** | 1865 | 1288 | 577 (10) | 0 | $-839.65 | -7.2% |
| **+10¢ (15¢ stop)** | 3976 | 3975 | 1 (1) | 0 | $-1546.74 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 03:17 | +10 stop | XRP | DOWN | 0.70 | 0.83 | 1.05 |
| 10-05 03:17 | +20 | XRP | DOWN | 0.70 | 0.90 | 1.82 |
| 10-05 03:17 | +15 | XRP | DOWN | 0.70 | 0.86 | 1.36 |
| 10-05 03:17 | +10 | XRP | DOWN | 0.70 | 0.83 | 1.05 |
| 10-05 03:17 | +5 | XRP | DOWN | 0.70 | 0.78 | 0.52 |
| 10-05 03:17 | +5 | DOGE | DOWN | 0.71 | 0.77 | 0.32 |
| 10-05 03:17 | +10 stop | DOGE | DOWN | 0.57 | 0.68 | 0.76 |
| 10-05 03:17 | +20 | DOGE | DOWN | 0.57 | 0.77 | 1.69 |
| 10-05 03:17 | +15 | DOGE | DOWN | 0.57 | 0.73 | 1.28 |
| 10-05 03:17 | +10 | DOGE | DOWN | 0.57 | 0.68 | 0.76 |
| 10-05 03:17 | +5 | DOGE | DOWN | 0.57 | 0.63 | 0.25 |
| 10-05 03:17 | +5 | HYPE | DOWN | 0.62 | 0.71 | 0.54 |
| 10-05 03:16 | +10 stop | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 10-05 03:16 | +20 | BTC | DOWN | 0.59 | 0.80 | 1.81 |
| 10-05 03:16 | +15 | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 10-05 03:16 | +10 | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 10-05 03:16 | +5 | BTC | DOWN | 0.59 | 0.66 | 0.37 |
| 10-05 03:16 | +10 stop | HYPE | DOWN | 0.65 | 0.75 | 0.70 |
| 10-05 03:16 | +20 | HYPE | DOWN | 0.65 | 0.87 | 1.96 |
| 10-05 03:16 | +15 | HYPE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-05 03:16 | +10 | HYPE | DOWN | 0.65 | 0.75 | 0.70 |
| 10-05 03:16 | +5 | HYPE | DOWN | 0.65 | 0.74 | 0.60 |
| 10-05 03:15 | +10 stop | SOL | UP | 0.31 | 0.63 | 2.88 |
| 10-05 03:15 | +20 | SOL | UP | 0.31 | 0.63 | 2.88 |
| 10-05 03:15 | +15 | SOL | UP | 0.31 | 0.63 | 2.83 |
| 10-05 03:15 | +10 | SOL | UP | 0.31 | 0.63 | 2.83 |
| 10-05 03:15 | +5 | SOL | UP | 0.31 | 0.63 | 2.83 |
| 10-05 03:15 | +10 stop | NEAR | DOWN | 0.70 | 0.54 | -1.93 |
| 10-05 03:15 | +20 | NEAR | DOWN | 0.70 | 0.91 | 1.89 |
| 10-05 03:15 | +15 | NEAR | DOWN | 0.70 | 0.86 | 1.36 |
| 10-05 03:15 | +10 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-05 03:15 | +5 | NEAR | DOWN | 0.70 | 0.78 | 0.52 |
| 10-05 03:15 | +10 stop | DOGE | UP | 0.30 | 0.54 | 2.07 |
| 10-05 03:15 | +20 | DOGE | UP | 0.30 | 0.54 | 2.07 |
| 10-05 03:15 | +15 | DOGE | UP | 0.30 | 0.54 | 2.07 |
| 10-05 03:15 | +10 | DOGE | UP | 0.30 | 0.54 | 2.07 |
| 10-05 03:15 | +5 | DOGE | UP | 0.30 | 0.54 | 2.07 |
| 10-05 03:13 | +10 stop | DOGE | DOWN | 0.70 | 0.91 | 1.83 |
| 10-05 03:11 | +10 stop | ZEC | UP | 0.67 | 0.83 | 1.34 |
| 10-05 03:11 | +20 | ZEC | UP | 0.67 | no | -6.91 |
