# Range-Scalp Bot

*Updated Sun Oct 04 06:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 1883 | 1621 | 262 (3) | 0 | $-651.33 | -5.5% |
| **+10¢** | 1458 | 1168 | 290 (4) | 1 | $-474.95 | -5.2% |
| **+15¢** | 1229 | 922 | 307 (5) | 1 | $-405.13 | -5.2% |
| **+20¢** | 1086 | 760 | 326 (7) | 0 | $-394.91 | -5.8% |
| **+10¢ (15¢ stop)** | 2367 | 2366 | 1 (1) | 0 | $-970.42 | -6.5% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 06:28 | +10 stop | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-04 06:28 | +20 | DOGE | DOWN | 0.67 | 0.96 | 2.72 |
| 10-04 06:28 | +15 | DOGE | DOWN | 0.67 | 0.96 | 2.72 |
| 10-04 06:28 | +10 | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-04 06:28 | +5 | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-04 06:27 | +10 stop | NEAR | DOWN | 0.32 | 0.56 | 2.06 |
| 10-04 06:27 | +5 | NEAR | DOWN | 0.32 | 0.56 | 2.06 |
| 10-04 06:27 | +10 stop | BTC | DOWN | 0.69 | 0.95 | 2.38 |
| 10-04 06:27 | +20 | BTC | DOWN | 0.69 | 0.95 | 2.38 |
| 10-04 06:27 | +15 | BTC | DOWN | 0.69 | 0.95 | 2.38 |
| 10-04 06:27 | +10 | BTC | DOWN | 0.68 | 0.95 | 2.47 |
| 10-04 06:27 | +5 | BTC | DOWN | 0.68 | 0.95 | 2.47 |
| 10-04 06:26 | +10 stop | HYPE | UP | 0.61 | 0.74 | 0.94 |
| 10-04 06:26 | +20 | HYPE | UP | 0.61 | 0.88 | 2.40 |
| 10-04 06:26 | +15 | HYPE | UP | 0.61 | 0.79 | 1.46 |
| 10-04 06:26 | +10 | HYPE | UP | 0.61 | 0.74 | 0.94 |
| 10-04 06:26 | +5 | HYPE | UP | 0.61 | 0.74 | 0.94 |
| 10-04 06:24 | +10 stop | ZEC | DOWN | 0.55 | 0.73 | 1.53 |
| 10-04 06:24 | +5 | SOL | DOWN | 0.71 | 0.78 | 0.42 |
| 10-04 06:24 | +10 stop | ZEC | UP | 0.51 | 0.63 | 0.85 |
| 10-04 06:23 | +10 stop | SOL | DOWN | 0.58 | 0.69 | 0.77 |
| 10-04 06:23 | +20 | SOL | DOWN | 0.58 | 0.78 | 1.69 |
| 10-04 06:23 | +15 | SOL | DOWN | 0.58 | 0.78 | 1.69 |
| 10-04 06:23 | +10 | SOL | DOWN | 0.58 | 0.69 | 0.77 |
| 10-04 06:23 | +5 | SOL | DOWN | 0.58 | 0.66 | 0.46 |
| 10-04 06:23 | +10 stop | NEAR | UP | 0.60 | 0.76 | 1.26 |
| 10-04 06:23 | +10 stop | ZEC | DOWN | 0.55 | 0.35 | -2.34 |
| 10-04 06:23 | +20 | ZEC | DOWN | 0.55 | 0.83 | 2.52 |
| 10-04 06:23 | +5 | ZEC | DOWN | 0.55 | 0.62 | 0.35 |
| 10-04 06:22 | +10 stop | NEAR | UP | 0.70 | 0.52 | -2.10 |
| 10-04 06:21 | +15 | ZEC | UP | 0.66 | open |  |
| 10-04 06:21 | +10 | ZEC | UP | 0.66 | open |  |
| 10-04 06:21 | +5 | ZEC | UP | 0.63 | 0.73 | 0.69 |
| 10-04 06:21 | +10 stop | ZEC | UP | 0.62 | 0.73 | 0.74 |
| 10-04 06:19 | +10 stop | BNB | UP | 0.69 | 0.87 | 1.57 |
| 10-04 06:18 | +5 | BTC | UP | 0.68 | 0.74 | 0.30 |
| 10-04 06:18 | +10 stop | ZEC | DOWN | 0.64 | 0.48 | -1.99 |
| 10-04 06:18 | +10 stop | BNB | DOWN | 0.52 | 0.34 | -2.14 |
| 10-04 06:17 | +5 | HYPE | UP | 0.62 | 0.68 | 0.27 |
| 10-04 06:16 | +10 stop | DOGE | UP | 0.71 | 0.81 | 0.74 |
