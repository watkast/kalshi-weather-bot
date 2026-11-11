# Range-Scalp Bot

*Updated Wed Nov 11 02:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55264 | 48202 | 7062 (94) | 2 | $-15054.34 | -4.3% |
| **+10¢** | 41286 | 33049 | 8237 (124) | 4 | $-13975.86 | -5.4% |
| **+15¢** | 34612 | 25735 | 8877 (158) | 5 | $-12703.76 | -5.9% |
| **+20¢** | 30816 | 21503 | 9313 (207) | 5 | $-11105.70 | -5.7% |
| **+10¢ (15¢ stop)** | 67314 | 67196 | 118 (73) | 0 | $-24811.28 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 02:26 | +20 | DOGE | UP | 0.70 | 0.90 | 1.78 |
| 11-11 02:26 | +15 | DOGE | UP | 0.70 | 0.85 | 1.26 |
| 11-11 02:26 | +10 | DOGE | UP | 0.70 | 0.82 | 0.94 |
| 11-11 02:26 | +5 | DOGE | UP | 0.70 | 0.82 | 0.94 |
| 11-11 02:26 | +10 stop | BTC | UP | 0.60 | 0.75 | 1.19 |
| 11-11 02:26 | +20 | BTC | UP | 0.62 | 0.88 | 2.35 |
| 11-11 02:26 | +15 | BTC | UP | 0.64 | 0.88 | 2.15 |
| 11-11 02:26 | +10 | BTC | UP | 0.63 | 0.75 | 0.89 |
| 11-11 02:26 | +5 | BTC | UP | 0.63 | 0.75 | 0.89 |
| 11-11 02:24 | +10 | HYPE | UP | 0.67 | 0.81 | 1.13 |
| 11-11 02:24 | +5 | HYPE | UP | 0.63 | 0.81 | 1.52 |
| 11-11 02:24 | +10 stop | NEAR | UP | 0.70 | 0.85 | 1.26 |
| 11-11 02:24 | +10 stop | HYPE | UP | 0.70 | 0.81 | 0.84 |
| 11-11 02:24 | +10 stop | XRP | DOWN | 0.64 | 0.43 | -2.45 |
| 11-11 02:24 | +20 | XRP | DOWN | 0.65 | open |  |
| 11-11 02:24 | +15 | XRP | DOWN | 0.65 | open |  |
| 11-11 02:24 | +10 | XRP | DOWN | 0.65 | open |  |
| 11-11 02:24 | +5 | XRP | DOWN | 0.65 | open |  |
| 11-11 02:24 | +10 stop | ETH | DOWN | 0.53 | 0.17 | -3.88 |
| 11-11 02:24 | +20 | ETH | DOWN | 0.51 | open |  |
| 11-11 02:24 | +15 | ETH | DOWN | 0.54 | open |  |
| 11-11 02:24 | +10 | ETH | DOWN | 0.52 | open |  |
| 11-11 02:24 | +5 | ETH | DOWN | 0.53 | 0.61 | 0.45 |
| 11-11 02:23 | +10 stop | HYPE | DOWN | 0.45 | 0.56 | 0.74 |
| 11-11 02:23 | +10 stop | ZEC | UP | 0.59 | 0.71 | 0.88 |
| 11-11 02:23 | +5 | ZEC | UP | 0.59 | 0.71 | 0.88 |
| 11-11 02:23 | +20 | HYPE | DOWN | 0.52 | open |  |
| 11-11 02:22 | +10 stop | HYPE | DOWN | 0.69 | 0.51 | -2.10 |
| 11-11 02:22 | +15 | HYPE | DOWN | 0.69 | open |  |
| 11-11 02:21 | +10 stop | NEAR | UP | 0.64 | 0.43 | -2.45 |
| 11-11 02:20 | +10 stop | ZEC | UP | 0.62 | 0.47 | -1.85 |
| 11-11 02:20 | +5 | HYPE | UP | 0.57 | 0.66 | 0.56 |
| 11-11 02:20 | +10 stop | HYPE | UP | 0.55 | 0.36 | -2.29 |
| 11-11 02:20 | +10 | HYPE | UP | 0.55 | 0.66 | 0.72 |
| 11-11 02:20 | +5 | HYPE | UP | 0.59 | 0.67 | 0.47 |
| 11-11 02:19 | +10 stop | BTC | DOWN | 0.57 | 0.71 | 1.07 |
| 11-11 02:19 | +10 stop | DOGE | DOWN | 0.62 | 0.75 | 0.99 |
| 11-11 02:19 | +10 | DOGE | DOWN | 0.63 | 0.75 | 0.89 |
| 11-11 02:18 | +5 | DOGE | DOWN | 0.61 | 0.75 | 1.09 |
| 11-11 02:18 | +10 stop | HYPE | UP | 0.56 | 0.67 | 0.73 |
