# Range-Scalp Bot

*Updated Sat Oct 17 04:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20356 | 17709 | 2647 (29) | 4 | $-6005.06 | -4.7% |
| **+10¢** | 15339 | 12285 | 3054 (41) | 3 | $-5343.19 | -5.5% |
| **+15¢** | 12825 | 9541 | 3284 (60) | 4 | $-4807.19 | -6.0% |
| **+20¢** | 11372 | 7932 | 3440 (79) | 4 | $-4243.40 | -5.9% |
| **+10¢ (15¢ stop)** | 25027 | 24977 | 50 (29) | 0 | $-9478.08 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 04:29 | +5 | ZEC | DOWN | 0.15 | open |  |
| 10-17 04:28 | +5 | ETH | DOWN | 0.70 | open |  |
| 10-17 04:28 | +10 stop | ZEC | DOWN | 0.48 | 0.18 | -3.29 |
| 10-17 04:28 | +15 | ZEC | DOWN | 0.47 | open |  |
| 10-17 04:28 | +10 | ZEC | DOWN | 0.47 | open |  |
| 10-17 04:28 | +5 | ZEC | DOWN | 0.44 | 0.51 | 0.34 |
| 10-17 04:28 | +10 stop | ETH | DOWN | 0.69 | 0.34 | -3.81 |
| 10-17 04:26 | +10 stop | ETH | UP | 0.62 | 0.39 | -2.64 |
| 10-17 04:26 | +5 | ZEC | DOWN | 0.68 | 0.74 | 0.30 |
| 10-17 04:26 | +10 stop | XRP | UP | 0.68 | 0.79 | 0.82 |
| 10-17 04:24 | +10 stop | DOGE | DOWN | 0.62 | 0.42 | -2.35 |
| 10-17 04:24 | +15 | DOGE | DOWN | 0.61 | open |  |
| 10-17 04:24 | +10 | DOGE | DOWN | 0.61 | open |  |
| 10-17 04:24 | +5 | DOGE | DOWN | 0.61 | open |  |
| 10-17 04:24 | +10 stop | XRP | DOWN | 0.59 | 0.43 | -1.95 |
| 10-17 04:24 | +5 | XRP | DOWN | 0.59 | open |  |
| 10-17 04:24 | +5 | ETH | DOWN | 0.57 | 0.63 | 0.25 |
| 10-17 04:24 | +10 stop | XRP | DOWN | 0.44 | 0.61 | 1.35 |
| 10-17 04:24 | +20 | XRP | DOWN | 0.55 | open |  |
| 10-17 04:24 | +15 | XRP | DOWN | 0.55 | open |  |
| 10-17 04:24 | +10 | XRP | DOWN | 0.55 | open |  |
| 10-17 04:24 | +5 | XRP | DOWN | 0.55 | 0.61 | 0.25 |
| 10-17 04:24 | +10 stop | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-17 04:24 | +15 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-17 04:24 | +10 | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-17 04:24 | +5 | ZEC | DOWN | 0.65 | 0.72 | 0.39 |
| 10-17 04:23 | +5 | ETH | DOWN | 0.53 | 0.64 | 0.75 |
| 10-17 04:23 | +10 stop | ETH | DOWN | 0.60 | 0.33 | -3.03 |
| 10-17 04:23 | +15 | ETH | DOWN | 0.60 | open |  |
| 10-17 04:23 | +10 | ETH | DOWN | 0.60 | 0.70 | 0.68 |
| 10-17 04:23 | +5 | ETH | DOWN | 0.60 | 0.65 | 0.17 |
| 10-17 04:18 | +5 | BTC | DOWN | 0.62 | 0.70 | 0.48 |
| 10-17 04:18 | +5 | ETH | DOWN | 0.66 | 0.72 | 0.29 |
| 10-17 04:16 | +10 stop | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 10-17 04:16 | +20 | BNB | DOWN | 0.63 | 0.85 | 1.94 |
| 10-17 04:16 | +15 | BNB | DOWN | 0.63 | 0.78 | 1.20 |
| 10-17 04:16 | +10 | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 10-17 04:16 | +5 | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 10-17 04:16 | +10 stop | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 10-17 04:16 | +20 | BTC | DOWN | 0.59 | 0.79 | 1.71 |
