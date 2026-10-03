# Range-Scalp Bot

*Updated Sat Oct 03 14:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 875 | 765 | 110 (1) | 1 | $-238.74 | -4.3% |
| **+10¢** | 665 | 545 | 120 (3) | 2 | $-121.45 | -2.9% |
| **+15¢** | 562 | 432 | 130 (4) | 3 | $-104.21 | -3.0% |
| **+20¢** | 493 | 357 | 136 (4) | 3 | $-85.65 | -2.8% |
| **+10¢ (15¢ stop)** | 1110 | 1109 | 1 (1) | 0 | $-555.87 | -8.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 14:27 | +10 stop | ZEC | DOWN | 0.56 | 0.27 | -3.22 |
| 10-03 14:27 | +20 | ZEC | DOWN | 0.57 | open |  |
| 10-03 14:27 | +15 | ZEC | DOWN | 0.57 | open |  |
| 10-03 14:23 | +10 stop | ZEC | DOWN | 0.65 | 0.79 | 1.15 |
| 10-03 14:22 | +10 stop | BNB | UP | 0.65 | 0.81 | 1.33 |
| 10-03 14:22 | +10 stop | ZEC | UP | 0.57 | 0.39 | -2.15 |
| 10-03 14:22 | +10 | ZEC | UP | 0.57 | 0.67 | 0.66 |
| 10-03 14:22 | +5 | ZEC | UP | 0.57 | 0.67 | 0.66 |
| 10-03 14:21 | +5 | NEAR | UP | 0.69 | 0.76 | 0.42 |
| 10-03 14:21 | +10 stop | BTC | UP | 0.67 | 0.77 | 0.71 |
| 10-03 14:21 | +10 | BTC | UP | 0.67 | 0.77 | 0.71 |
| 10-03 14:21 | +10 stop | BNB | DOWN | 0.55 | 0.65 | 0.66 |
| 10-03 14:20 | +5 | BTC | UP | 0.70 | 0.75 | 0.21 |
| 10-03 14:20 | +10 stop | BNB | UP | 0.62 | 0.46 | -1.94 |
| 10-03 14:20 | +15 | BNB | UP | 0.62 | 0.81 | 1.63 |
| 10-03 14:20 | +10 | BNB | UP | 0.62 | 0.81 | 1.63 |
| 10-03 14:20 | +5 | BNB | UP | 0.62 | 0.68 | 0.28 |
| 10-03 14:19 | +10 stop | ZEC | DOWN | 0.54 | 0.64 | 0.65 |
| 10-03 14:19 | +10 | ZEC | DOWN | 0.54 | 0.64 | 0.65 |
| 10-03 14:19 | +5 | NEAR | UP | 0.63 | 0.68 | 0.17 |
| 10-03 14:19 | +10 stop | BTC | UP | 0.58 | 0.69 | 0.77 |
| 10-03 14:19 | +10 | BTC | UP | 0.58 | 0.69 | 0.77 |
| 10-03 14:19 | +5 | BTC | UP | 0.58 | 0.63 | 0.15 |
| 10-03 14:18 | +10 stop | HYPE | UP | 0.67 | 0.78 | 0.77 |
| 10-03 14:18 | +10 stop | NEAR | UP | 0.63 | 0.76 | 1.00 |
| 10-03 14:18 | +10 stop | BNB | DOWN | 0.51 | 0.34 | -2.04 |
| 10-03 14:17 | +5 | XRP | UP | 0.68 | 0.79 | 0.81 |
| 10-03 14:17 | +10 stop | ETH | UP | 0.66 | 0.76 | 0.71 |
| 10-03 14:16 | +10 stop | ETH | UP | 0.55 | 0.65 | 0.69 |
| 10-03 14:16 | +20 | ETH | UP | 0.53 | 0.76 | 1.99 |
| 10-03 14:16 | +15 | ETH | UP | 0.56 | 0.72 | 1.32 |
| 10-03 14:16 | +10 | ETH | UP | 0.63 | 0.76 | 1.00 |
| 10-03 14:16 | +5 | ETH | UP | 0.63 | 0.69 | 0.28 |
| 10-03 14:16 | +5 | BTC | UP | 0.62 | 0.67 | 0.17 |
| 10-03 14:16 | +10 stop | HYPE | DOWN | 0.56 | 0.35 | -2.44 |
| 10-03 14:16 | +20 | HYPE | DOWN | 0.56 | open |  |
| 10-03 14:16 | +15 | HYPE | DOWN | 0.56 | open |  |
| 10-03 14:16 | +10 | HYPE | DOWN | 0.56 | open |  |
| 10-03 14:16 | +5 | HYPE | DOWN | 0.56 | open |  |
| 10-03 14:16 | +5 | BNB | UP | 0.66 | 0.75 | 0.60 |
