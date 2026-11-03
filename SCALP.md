# Range-Scalp Bot

*Updated Tue Nov 03 12:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45917 | 39977 | 5940 (69) | 3 | $-13272.28 | -4.6% |
| **+10¢** | 34286 | 27404 | 6882 (91) | 3 | $-12144.41 | -5.6% |
| **+15¢** | 28696 | 21294 | 7402 (119) | 2 | $-11115.28 | -6.2% |
| **+20¢** | 25484 | 17727 | 7757 (155) | 4 | $-9901.15 | -6.2% |
| **+10¢ (15¢ stop)** | 56015 | 55926 | 89 (53) | 2 | $-21007.98 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 12:20 | +5 | BTC | UP | 0.71 | open |  |
| 11-03 12:20 | +10 | ETH | UP | 0.71 | open |  |
| 11-03 12:17 | +5 | NEAR | UP | 0.71 | 0.84 | 1.05 |
| 11-03 12:17 | +5 | ETH | UP | 0.71 | open |  |
| 11-03 12:17 | +5 | ZEC | UP | 0.66 | open |  |
| 11-03 12:17 | +10 stop | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-03 12:17 | +20 | HYPE | DOWN | 0.68 | open |  |
| 11-03 12:17 | +15 | HYPE | DOWN | 0.68 | 0.84 | 1.34 |
| 11-03 12:17 | +10 | HYPE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-03 12:17 | +5 | HYPE | DOWN | 0.69 | 0.76 | 0.42 |
| 11-03 12:17 | +10 stop | BTC | UP | 0.71 | open |  |
| 11-03 12:17 | +20 | BTC | UP | 0.71 | open |  |
| 11-03 12:17 | +15 | BTC | UP | 0.71 | open |  |
| 11-03 12:17 | +10 | BTC | UP | 0.71 | open |  |
| 11-03 12:17 | +5 | BTC | UP | 0.71 | 0.76 | 0.22 |
| 11-03 12:16 | +10 stop | NEAR | UP | 0.59 | 0.69 | 0.68 |
| 11-03 12:16 | +20 | NEAR | UP | 0.59 | 0.84 | 2.23 |
| 11-03 12:16 | +15 | NEAR | UP | 0.59 | 0.84 | 2.23 |
| 11-03 12:16 | +10 | NEAR | UP | 0.59 | 0.69 | 0.68 |
| 11-03 12:16 | +5 | NEAR | UP | 0.59 | 0.67 | 0.47 |
| 11-03 12:16 | +10 stop | ZEC | UP | 0.63 | open |  |
| 11-03 12:16 | +20 | ZEC | UP | 0.63 | open |  |
| 11-03 12:16 | +15 | ZEC | UP | 0.63 | open |  |
| 11-03 12:16 | +10 | ZEC | UP | 0.62 | open |  |
| 11-03 12:16 | +5 | ZEC | UP | 0.63 | 0.68 | 0.17 |
| 11-03 12:16 | +10 stop | ETH | UP | 0.57 | 0.69 | 0.87 |
| 11-03 12:16 | +20 | ETH | UP | 0.58 | open |  |
| 11-03 12:16 | +15 | ETH | UP | 0.58 | 0.73 | 1.18 |
| 11-03 12:16 | +10 | ETH | UP | 0.58 | 0.69 | 0.77 |
| 11-03 12:16 | +5 | ETH | UP | 0.58 | 0.65 | 0.36 |
| 11-03 12:15 | +10 stop | HYPE | DOWN | 0.56 | 0.67 | 0.76 |
| 11-03 12:15 | +20 | HYPE | DOWN | 0.56 | 0.76 | 1.69 |
| 11-03 12:15 | +15 | HYPE | DOWN | 0.56 | 0.72 | 1.23 |
| 11-03 12:15 | +10 | HYPE | DOWN | 0.59 | 0.72 | 0.98 |
| 11-03 12:15 | +5 | HYPE | DOWN | 0.59 | 0.67 | 0.47 |
| 11-03 12:15 | +10 stop | BTC | DOWN | 0.36 | 0.55 | 1.55 |
| 11-03 12:15 | +20 | BTC | DOWN | 0.35 | 0.55 | 1.66 |
| 11-03 12:15 | +15 | BTC | DOWN | 0.35 | 0.55 | 1.66 |
| 11-03 12:15 | +10 | BTC | DOWN | 0.34 | 0.55 | 1.76 |
| 11-03 12:15 | +5 | BTC | DOWN | 0.33 | 0.55 | 1.86 |
