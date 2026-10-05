# Range-Scalp Bot

*Updated Mon Oct 05 05:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3359 | 2884 | 475 (3) | 1 | $-1205.99 | -5.7% |
| **+10¢** | 2599 | 2059 | 540 (4) | 2 | $-1065.60 | -6.5% |
| **+15¢** | 2185 | 1613 | 572 (5) | 4 | $-963.32 | -7.0% |
| **+20¢** | 1947 | 1350 | 597 (10) | 5 | $-834.69 | -6.8% |
| **+10¢ (15¢ stop)** | 4173 | 4172 | 1 (1) | 1 | $-1606.35 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 05:21 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 10-05 05:21 | +10 stop | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 10-05 05:21 | +10 | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 10-05 05:21 | +5 | ETH | DOWN | 0.66 | 0.71 | 0.19 |
| 10-05 05:21 | +10 stop | BNB | UP | 0.54 | open |  |
| 10-05 05:20 | +5 | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 10-05 05:20 | +10 stop | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-05 05:20 | +15 | DOGE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-05 05:20 | +10 | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-05 05:20 | +5 | DOGE | DOWN | 0.71 | 0.78 | 0.42 |
| 10-05 05:19 | +20 | XRP | DOWN | 0.62 | open |  |
| 10-05 05:19 | +15 | XRP | DOWN | 0.62 | 0.81 | 1.62 |
| 10-05 05:19 | +5 | XRP | DOWN | 0.62 | 0.70 | 0.48 |
| 10-05 05:19 | +5 | BTC | DOWN | 0.53 | 0.63 | 0.65 |
| 10-05 05:19 | +10 stop | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 10-05 05:19 | +15 | ETH | DOWN | 0.59 | 0.77 | 1.50 |
| 10-05 05:19 | +10 | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 10-05 05:19 | +5 | ETH | DOWN | 0.59 | 0.68 | 0.57 |
| 10-05 05:19 | +5 | ZEC | UP | 0.65 | 0.75 | 0.70 |
| 10-05 05:19 | +5 | BTC | DOWN | 0.59 | 0.64 | 0.16 |
| 10-05 05:18 | +10 stop | BNB | DOWN | 0.65 | 0.50 | -1.86 |
| 10-05 05:18 | +10 stop | ZEC | UP | 0.47 | 0.61 | 1.05 |
| 10-05 05:18 | +10 | ZEC | UP | 0.47 | 0.61 | 1.05 |
| 10-05 05:18 | +5 | ZEC | UP | 0.47 | 0.55 | 0.44 |
| 10-05 05:18 | +10 stop | XRP | DOWN | 0.68 | 0.81 | 1.03 |
| 10-05 05:18 | +10 | XRP | DOWN | 0.68 | 0.81 | 1.03 |
| 10-05 05:18 | +5 | XRP | DOWN | 0.68 | 0.77 | 0.61 |
| 10-05 05:17 | +10 stop | HYPE | UP | 0.56 | 0.39 | -2.05 |
| 10-05 05:17 | +10 stop | NEAR | UP | 0.13 | 0.59 | 4.35 |
| 10-05 05:17 | +10 stop | ZEC | UP | 0.55 | 0.66 | 0.76 |
| 10-05 05:17 | +10 | ZEC | UP | 0.54 | 0.66 | 0.86 |
| 10-05 05:17 | +5 | ZEC | UP | 0.54 | 0.66 | 0.86 |
| 10-05 05:17 | +10 stop | BNB | UP | 0.57 | 0.37 | -2.35 |
| 10-05 05:17 | +20 | BNB | UP | 0.57 | open |  |
| 10-05 05:17 | +15 | BNB | UP | 0.57 | open |  |
| 10-05 05:17 | +10 | BNB | UP | 0.57 | open |  |
| 10-05 05:17 | +5 | BNB | UP | 0.57 | open |  |
| 10-05 05:16 | +10 stop | ZEC | DOWN | 0.44 | 0.56 | 0.84 |
| 10-05 05:16 | +20 | ZEC | DOWN | 0.44 | open |  |
| 10-05 05:16 | +15 | ZEC | DOWN | 0.44 | open |  |
