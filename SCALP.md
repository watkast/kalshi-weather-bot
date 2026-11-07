# Range-Scalp Bot

*Updated Sat Nov 07 00:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50218 | 43778 | 6440 (76) | 4 | $-14097.40 | -4.5% |
| **+10¢** | 37471 | 29974 | 7497 (102) | 4 | $-13019.68 | -5.5% |
| **+15¢** | 31382 | 23303 | 8079 (131) | 4 | $-11929.54 | -6.1% |
| **+20¢** | 27897 | 19427 | 8470 (173) | 7 | $-10548.55 | -6.0% |
| **+10¢ (15¢ stop)** | 61145 | 61046 | 99 (58) | 3 | $-22664.30 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 00:39 | +10 stop | NEAR | DOWN | 0.46 | open |  |
| 11-07 00:38 | +10 stop | ETH | UP | 0.65 | open |  |
| 11-07 00:37 | +5 | NEAR | UP | 0.59 | open |  |
| 11-07 00:37 | +10 stop | ETH | UP | 0.47 | 0.59 | 0.85 |
| 11-07 00:37 | +10 stop | BNB | DOWN | 0.59 | open |  |
| 11-07 00:37 | +15 | BNB | DOWN | 0.59 | open |  |
| 11-07 00:37 | +10 | BNB | DOWN | 0.59 | open |  |
| 11-07 00:37 | +5 | BNB | DOWN | 0.59 | open |  |
| 11-07 00:36 | +10 stop | XRP | UP | 0.68 | 0.81 | 1.03 |
| 11-07 00:36 | +10 | XRP | UP | 0.68 | 0.81 | 1.03 |
| 11-07 00:36 | +5 | XRP | UP | 0.68 | 0.81 | 1.03 |
| 11-07 00:36 | +5 | BTC | UP | 0.62 | 0.71 | 0.58 |
| 11-07 00:36 | +10 stop | BTC | UP | 0.63 | 0.74 | 0.79 |
| 11-07 00:36 | +10 stop | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 11-07 00:35 | +10 stop | XRP | DOWN | 0.33 | 0.55 | 1.86 |
| 11-07 00:34 | +5 | XRP | UP | 0.54 | 0.62 | 0.45 |
| 11-07 00:34 | +10 stop | HYPE | DOWN | 0.60 | 0.38 | -2.54 |
| 11-07 00:34 | +10 stop | BTC | DOWN | 0.62 | 0.46 | -1.95 |
| 11-07 00:34 | +10 stop | XRP | UP | 0.59 | 0.44 | -1.85 |
| 11-07 00:34 | +10 | XRP | UP | 0.59 | 0.71 | 0.88 |
| 11-07 00:34 | +5 | XRP | UP | 0.59 | 0.66 | 0.37 |
| 11-07 00:34 | +10 stop | ETH | DOWN | 0.71 | 0.47 | -2.73 |
| 11-07 00:34 | +20 | ETH | DOWN | 0.71 | open |  |
| 11-07 00:34 | +15 | ETH | DOWN | 0.71 | open |  |
| 11-07 00:34 | +10 | ETH | DOWN | 0.71 | open |  |
| 11-07 00:34 | +5 | ETH | DOWN | 0.71 | open |  |
| 11-07 00:34 | +10 stop | ZEC | UP | 0.51 | 0.68 | 1.36 |
| 11-07 00:34 | +10 | ZEC | UP | 0.51 | 0.68 | 1.36 |
| 11-07 00:34 | +5 | ZEC | UP | 0.51 | 0.58 | 0.34 |
| 11-07 00:34 | +5 | NEAR | UP | 0.59 | 0.68 | 0.57 |
| 11-07 00:33 | +10 stop | ETH | UP | 0.31 | 0.54 | 1.97 |
| 11-07 00:33 | +20 | ETH | UP | 0.31 | 0.54 | 1.97 |
| 11-07 00:33 | +15 | ETH | UP | 0.31 | 0.54 | 1.97 |
| 11-07 00:33 | +10 | ETH | UP | 0.31 | 0.54 | 1.97 |
| 11-07 00:33 | +5 | ETH | UP | 0.31 | 0.54 | 1.97 |
| 11-07 00:32 | +10 stop | BTC | UP | 0.56 | 0.40 | -1.95 |
| 11-07 00:32 | +20 | BTC | UP | 0.56 | 0.76 | 1.69 |
| 11-07 00:32 | +15 | BTC | UP | 0.56 | 0.71 | 1.17 |
| 11-07 00:32 | +10 | BTC | UP | 0.56 | 0.66 | 0.66 |
| 11-07 00:32 | +5 | BTC | UP | 0.56 | 0.63 | 0.35 |
