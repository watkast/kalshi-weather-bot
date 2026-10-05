# Range-Scalp Bot

*Updated Mon Oct 05 08:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3576 | 3067 | 509 (3) | 3 | $-1318.30 | -5.8% |
| **+10¢** | 2759 | 2175 | 584 (4) | 4 | $-1210.72 | -7.0% |
| **+15¢** | 2321 | 1705 | 616 (6) | 3 | $-1077.94 | -7.4% |
| **+20¢** | 2070 | 1428 | 642 (11) | 3 | $-943.12 | -7.3% |
| **+10¢ (15¢ stop)** | 4426 | 4425 | 1 (1) | 0 | $-1706.55 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 08:41 | +10 stop | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 10-05 08:41 | +20 | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 10-05 08:41 | +15 | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 10-05 08:39 | +10 stop | XRP | DOWN | 0.61 | 0.81 | 1.70 |
| 10-05 08:39 | +5 | XRP | DOWN | 0.61 | 0.81 | 1.70 |
| 10-05 08:37 | +10 stop | ZEC | DOWN | 0.59 | 0.72 | 0.98 |
| 10-05 08:36 | +10 stop | ZEC | UP | 0.57 | 0.35 | -2.54 |
| 10-05 08:36 | +10 | ZEC | UP | 0.57 | open |  |
| 10-05 08:36 | +5 | ZEC | UP | 0.56 | open |  |
| 10-05 08:36 | +10 stop | XRP | UP | 0.45 | 0.25 | -2.32 |
| 10-05 08:36 | +15 | XRP | UP | 0.45 | open |  |
| 10-05 08:36 | +10 | XRP | UP | 0.45 | open |  |
| 10-05 08:36 | +5 | XRP | UP | 0.45 | 0.54 | 0.54 |
| 10-05 08:36 | +5 | HYPE | DOWN | 0.64 | 0.81 | 1.43 |
| 10-05 08:35 | +10 stop | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 10-05 08:35 | +10 stop | SOL | DOWN | 0.62 | 0.80 | 1.51 |
| 10-05 08:35 | +10 stop | HYPE | DOWN | 0.61 | 0.81 | 1.72 |
| 10-05 08:35 | +20 | HYPE | DOWN | 0.61 | 0.81 | 1.72 |
| 10-05 08:35 | +15 | HYPE | DOWN | 0.61 | 0.81 | 1.72 |
| 10-05 08:35 | +10 | HYPE | DOWN | 0.61 | 0.81 | 1.72 |
| 10-05 08:35 | +5 | HYPE | DOWN | 0.61 | 0.68 | 0.37 |
| 10-05 08:35 | +10 stop | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 10-05 08:35 | +20 | ETH | DOWN | 0.66 | 0.93 | 2.45 |
| 10-05 08:35 | +15 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 10-05 08:35 | +10 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 10-05 08:35 | +5 | ETH | DOWN | 0.66 | 0.71 | 0.19 |
| 10-05 08:35 | +10 stop | ZEC | DOWN | 0.49 | 0.59 | 0.65 |
| 10-05 08:35 | +20 | ZEC | DOWN | 0.49 | 0.72 | 1.97 |
| 10-05 08:35 | +15 | ZEC | DOWN | 0.49 | 0.67 | 1.46 |
| 10-05 08:35 | +10 | ZEC | DOWN | 0.49 | 0.59 | 0.65 |
| 10-05 08:35 | +5 | ZEC | DOWN | 0.49 | 0.59 | 0.65 |
| 10-05 08:34 | +10 stop | XRP | DOWN | 0.43 | 0.64 | 1.75 |
| 10-05 08:34 | +15 | XRP | DOWN | 0.43 | 0.64 | 1.75 |
| 10-05 08:34 | +10 | XRP | DOWN | 0.43 | 0.64 | 1.75 |
| 10-05 08:34 | +5 | XRP | DOWN | 0.43 | 0.64 | 1.75 |
| 10-05 08:34 | +10 stop | BTC | DOWN | 0.60 | 0.78 | 1.45 |
| 10-05 08:32 | +5 | BNB | DOWN | 0.63 | 0.73 | 0.69 |
| 10-05 08:32 | +10 stop | ETH | DOWN | 0.59 | 0.81 | 1.92 |
| 10-05 08:32 | +20 | ETH | DOWN | 0.59 | 0.81 | 1.94 |
| 10-05 08:32 | +15 | ETH | DOWN | 0.59 | 0.81 | 1.94 |
