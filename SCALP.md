# Range-Scalp Bot

*Updated Thu Oct 08 16:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7718 | 6688 | 1030 (13) | 0 | $-2405.22 | -4.9% |
| **+10¢** | 5853 | 4635 | 1218 (24) | 0 | $-2356.62 | -6.4% |
| **+15¢** | 4919 | 3639 | 1280 (32) | 0 | $-1921.83 | -6.2% |
| **+20¢** | 4399 | 3071 | 1328 (40) | 0 | $-1505.02 | -5.5% |
| **+10¢ (15¢ stop)** | 9378 | 9349 | 29 (18) | 0 | $-3449.47 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 16:43 | +10 stop | ETH | UP | 0.30 | 0.67 | 3.39 |
| 10-08 16:41 | +10 stop | DOGE | UP | 0.56 | 0.27 | -3.19 |
| 10-08 16:41 | +10 stop | HYPE | UP | 0.53 | 0.18 | -3.79 |
| 10-08 16:40 | +10 stop | HYPE | DOWN | 0.61 | 0.45 | -1.95 |
| 10-08 16:40 | +20 | HYPE | DOWN | 0.61 | 0.81 | 1.72 |
| 10-08 16:40 | +15 | HYPE | DOWN | 0.61 | 0.81 | 1.73 |
| 10-08 16:40 | +10 | HYPE | DOWN | 0.60 | 0.81 | 1.82 |
| 10-08 16:40 | +5 | HYPE | DOWN | 0.60 | 0.81 | 1.82 |
| 10-08 16:39 | +5 | SOL | DOWN | 0.51 | 0.70 | 1.57 |
| 10-08 16:39 | +10 stop | XRP | UP | 0.69 | 0.54 | -1.83 |
| 10-08 16:39 | +10 stop | BTC | DOWN | 0.58 | 0.38 | -2.35 |
| 10-08 16:39 | +10 stop | ETH | UP | 0.70 | 0.81 | 0.84 |
| 10-08 16:39 | +10 stop | SOL | DOWN | 0.57 | 0.35 | -2.58 |
| 10-08 16:39 | +10 | SOL | DOWN | 0.57 | 0.70 | 0.93 |
| 10-08 16:39 | +5 | SOL | DOWN | 0.57 | 0.62 | 0.15 |
| 10-08 16:37 | +10 stop | ETH | UP | 0.47 | 0.68 | 1.76 |
| 10-08 16:37 | +10 stop | SOL | DOWN | 0.60 | 0.78 | 1.50 |
| 10-08 16:37 | +10 | SOL | DOWN | 0.60 | 0.78 | 1.50 |
| 10-08 16:37 | +5 | SOL | DOWN | 0.58 | 0.78 | 1.69 |
| 10-08 16:37 | +10 stop | XRP | DOWN | 0.53 | 0.70 | 1.38 |
| 10-08 16:36 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-08 16:35 | +5 | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 10-08 16:35 | +10 stop | XRP | UP | 0.46 | 0.59 | 0.95 |
| 10-08 16:35 | +10 stop | BTC | DOWN | 0.68 | 0.53 | -1.84 |
| 10-08 16:35 | +20 | BTC | DOWN | 0.68 | 0.89 | 1.87 |
| 10-08 16:35 | +15 | BTC | DOWN | 0.68 | 0.89 | 1.87 |
| 10-08 16:35 | +10 | BTC | DOWN | 0.68 | 0.89 | 1.87 |
| 10-08 16:35 | +5 | BTC | DOWN | 0.68 | 0.89 | 1.87 |
| 10-08 16:35 | +10 stop | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-08 16:35 | +20 | SOL | DOWN | 0.64 | 0.97 | 3.14 |
| 10-08 16:35 | +15 | SOL | DOWN | 0.64 | 0.80 | 1.31 |
| 10-08 16:35 | +10 | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-08 16:35 | +5 | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-08 16:34 | +5 | ETH | DOWN | 0.58 | 0.63 | 0.15 |
| 10-08 16:34 | +10 stop | DOGE | DOWN | 0.66 | 0.49 | -2.04 |
| 10-08 16:34 | +5 | DOGE | DOWN | 0.66 | 0.72 | 0.29 |
| 10-08 16:33 | +10 stop | XRP | DOWN | 0.67 | 0.48 | -2.24 |
| 10-08 16:33 | +5 | XRP | DOWN | 0.67 | yes | -6.86 |
| 10-08 16:33 | +10 stop | ETH | DOWN | 0.68 | 0.46 | -2.54 |
| 10-08 16:33 | +10 stop | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
