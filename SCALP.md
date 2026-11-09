# Range-Scalp Bot

*Updated Mon Nov 09 00:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53058 | 46269 | 6789 (85) | 2 | $-14613.43 | -4.4% |
| **+10¢** | 39609 | 31691 | 7918 (110) | 3 | $-13611.12 | -5.5% |
| **+15¢** | 33190 | 24661 | 8529 (141) | 3 | $-12398.29 | -6.0% |
| **+20¢** | 29518 | 20575 | 8943 (186) | 4 | $-10923.45 | -5.9% |
| **+10¢ (15¢ stop)** | 64608 | 64502 | 106 (63) | 0 | $-23920.20 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 00:43 | +15 | SOL | DOWN | 0.71 | 0.89 | 1.58 |
| 11-09 00:43 | +10 | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 11-09 00:43 | +5 | SOL | DOWN | 0.71 | 0.80 | 0.63 |
| 11-09 00:43 | +10 stop | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 11-09 00:43 | +20 | BTC | DOWN | 0.67 | 0.89 | 1.97 |
| 11-09 00:43 | +15 | BTC | DOWN | 0.67 | 0.86 | 1.65 |
| 11-09 00:43 | +10 | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-09 00:43 | +5 | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-09 00:43 | +10 stop | SOL | DOWN | 0.69 | 0.80 | 0.83 |
| 11-09 00:42 | +10 stop | NEAR | DOWN | 0.28 | 0.57 | 2.54 |
| 11-09 00:42 | +15 | NEAR | DOWN | 0.28 | 0.57 | 2.54 |
| 11-09 00:42 | +10 | NEAR | DOWN | 0.28 | 0.57 | 2.54 |
| 11-09 00:42 | +5 | NEAR | DOWN | 0.28 | 0.57 | 2.54 |
| 11-09 00:42 | +10 stop | ZEC | UP | 0.71 | 0.83 | 0.96 |
| 11-09 00:41 | +10 stop | HYPE | UP | 0.38 | 0.65 | 2.37 |
| 11-09 00:40 | +10 stop | XRP | DOWN | 0.63 | 0.19 | -4.68 |
| 11-09 00:40 | +20 | XRP | DOWN | 0.63 | open |  |
| 11-09 00:40 | +15 | XRP | DOWN | 0.65 | open |  |
| 11-09 00:40 | +10 | XRP | DOWN | 0.58 | open |  |
| 11-09 00:40 | +5 | XRP | DOWN | 0.58 | 0.66 | 0.46 |
| 11-09 00:39 | +10 stop | ZEC | DOWN | 0.61 | 0.75 | 1.09 |
| 11-09 00:39 | +10 stop | HYPE | DOWN | 0.71 | 0.52 | -2.19 |
| 11-09 00:38 | +10 stop | XRP | UP | 0.40 | 0.67 | 2.37 |
| 11-09 00:38 | +20 | XRP | UP | 0.40 | 0.67 | 2.37 |
| 11-09 00:38 | +15 | XRP | UP | 0.40 | 0.67 | 2.37 |
| 11-09 00:38 | +10 | XRP | UP | 0.40 | 0.67 | 2.37 |
| 11-09 00:38 | +5 | XRP | UP | 0.40 | 0.67 | 2.37 |
| 11-09 00:38 | +10 stop | ETH | DOWN | 0.66 | 0.88 | 1.96 |
| 11-09 00:38 | +10 stop | BTC | DOWN | 0.64 | 0.86 | 1.94 |
| 11-09 00:37 | +10 | BNB | DOWN | 0.68 | 0.83 | 1.24 |
| 11-09 00:37 | +5 | BNB | DOWN | 0.68 | 0.83 | 1.24 |
| 11-09 00:37 | +10 stop | ZEC | UP | 0.58 | 0.36 | -2.59 |
| 11-09 00:37 | +15 | ZEC | UP | 0.59 | 0.83 | 2.13 |
| 11-09 00:37 | +10 | ZEC | UP | 0.60 | 0.83 | 2.03 |
| 11-09 00:37 | +10 stop | SOL | DOWN | 0.65 | 0.85 | 1.75 |
| 11-09 00:36 | +10 stop | HYPE | UP | 0.56 | 0.26 | -3.32 |
| 11-09 00:36 | +20 | HYPE | UP | 0.56 | 0.79 | 2.00 |
| 11-09 00:36 | +15 | HYPE | UP | 0.57 | 0.72 | 1.17 |
| 11-09 00:36 | +10 | HYPE | UP | 0.57 | 0.72 | 1.17 |
| 11-09 00:36 | +5 | HYPE | UP | 0.57 | 0.65 | 0.46 |
