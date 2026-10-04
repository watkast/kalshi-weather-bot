# Range-Scalp Bot

*Updated Sun Oct 04 17:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2572 | 2215 | 357 (3) | 4 | $-861.10 | -5.3% |
| **+10¢** | 2015 | 1614 | 401 (4) | 4 | $-688.77 | -5.4% |
| **+15¢** | 1691 | 1270 | 421 (5) | 3 | $-562.55 | -5.3% |
| **+20¢** | 1501 | 1059 | 442 (9) | 5 | $-486.46 | -5.1% |
| **+10¢ (15¢ stop)** | 3199 | 3198 | 1 (1) | 0 | $-1192.96 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 17:41 | +10 stop | XRP | UP | 0.65 | 0.82 | 1.43 |
| 10-04 17:40 | +10 stop | XRP | DOWN | 0.68 | 0.42 | -2.95 |
| 10-04 17:40 | +15 | XRP | DOWN | 0.68 | open |  |
| 10-04 17:40 | +10 | XRP | DOWN | 0.68 | open |  |
| 10-04 17:40 | +5 | XRP | DOWN | 0.68 | open |  |
| 10-04 17:40 | +10 stop | DOGE | UP | 0.61 | 0.35 | -2.93 |
| 10-04 17:40 | +10 stop | HYPE | DOWN | 0.65 | 0.49 | -1.94 |
| 10-04 17:38 | +10 stop | DOGE | DOWN | 0.61 | 0.43 | -2.15 |
| 10-04 17:38 | +10 stop | HYPE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-04 17:37 | +10 stop | NEAR | UP | 0.70 | 0.55 | -1.83 |
| 10-04 17:37 | +20 | NEAR | UP | 0.70 | 0.95 | 2.27 |
| 10-04 17:37 | +15 | NEAR | UP | 0.70 | 0.95 | 2.27 |
| 10-04 17:37 | +10 | NEAR | UP | 0.70 | 0.95 | 2.27 |
| 10-04 17:37 | +5 | NEAR | UP | 0.70 | 0.95 | 2.27 |
| 10-04 17:37 | +10 stop | BNB | DOWN | 0.70 | 0.92 | 1.95 |
| 10-04 17:36 | +10 stop | DOGE | UP | 0.58 | 0.38 | -2.35 |
| 10-04 17:36 | +10 stop | DOGE | UP | 0.49 | 0.67 | 1.46 |
| 10-04 17:36 | +10 stop | XRP | UP | 0.52 | 0.26 | -2.92 |
| 10-04 17:36 | +15 | DOGE | UP | 0.54 | 0.82 | 2.51 |
| 10-04 17:35 | +15 | DOGE | DOWN | 0.33 | 0.65 | 2.88 |
| 10-04 17:35 | +10 stop | BNB | DOWN | 0.58 | 0.73 | 1.18 |
| 10-04 17:34 | +10 stop | BTC | DOWN | 0.66 | 0.83 | 1.44 |
| 10-04 17:34 | +5 | ZEC | UP | 0.69 | 0.74 | 0.22 |
| 10-04 17:34 | +10 stop | DOGE | DOWN | 0.68 | 0.32 | -3.90 |
| 10-04 17:34 | +10 | DOGE | DOWN | 0.68 | open |  |
| 10-04 17:34 | +5 | DOGE | DOWN | 0.68 | open |  |
| 10-04 17:33 | +10 stop | BTC | UP | 0.65 | 0.47 | -2.14 |
| 10-04 17:33 | +10 | BTC | UP | 0.65 | open |  |
| 10-04 17:33 | +5 | BTC | UP | 0.65 | open |  |
| 10-04 17:33 | +10 | NEAR | UP | 0.65 | 0.79 | 1.08 |
| 10-04 17:33 | +5 | NEAR | UP | 0.65 | 0.72 | 0.35 |
| 10-04 17:33 | +10 stop | NEAR | UP | 0.65 | 0.47 | -2.18 |
| 10-04 17:32 | +5 | BTC | UP | 0.63 | 0.68 | 0.17 |
| 10-04 17:32 | +5 | SOL | DOWN | 0.66 | 0.75 | 0.58 |
| 10-04 17:31 | +10 stop | ETH | DOWN | 0.58 | 0.71 | 0.97 |
| 10-04 17:31 | +20 | ETH | DOWN | 0.58 | 0.80 | 1.90 |
| 10-04 17:31 | +15 | ETH | DOWN | 0.58 | 0.76 | 1.49 |
| 10-04 17:31 | +10 | ETH | DOWN | 0.58 | 0.71 | 0.97 |
| 10-04 17:31 | +5 | ETH | DOWN | 0.58 | 0.71 | 0.97 |
| 10-04 17:31 | +10 stop | DOGE | DOWN | 0.54 | 0.65 | 0.76 |
