# Range-Scalp Bot

*Updated Sun Oct 04 11:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2194 | 1895 | 299 (3) | 0 | $-720.29 | -5.2% |
| **+10¢** | 1711 | 1378 | 333 (4) | 0 | $-532.16 | -4.9% |
| **+15¢** | 1436 | 1082 | 354 (5) | 0 | $-459.25 | -5.1% |
| **+20¢** | 1269 | 896 | 373 (8) | 0 | $-406.40 | -5.1% |
| **+10¢ (15¢ stop)** | 2720 | 2719 | 1 (1) | 0 | $-1037.00 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 11:25 | +5 | DOGE | UP | 0.62 | 0.76 | 1.10 |
| 10-04 11:22 | +10 stop | DOGE | UP | 0.64 | 0.76 | 0.90 |
| 10-04 11:22 | +20 | DOGE | UP | 0.64 | 0.90 | 2.39 |
| 10-04 11:22 | +15 | DOGE | UP | 0.65 | 0.82 | 1.47 |
| 10-04 11:22 | +10 | DOGE | UP | 0.65 | 0.76 | 0.85 |
| 10-04 11:22 | +5 | DOGE | UP | 0.65 | 0.70 | 0.23 |
| 10-04 11:22 | +10 | ZEC | UP | 0.69 | 0.82 | 1.04 |
| 10-04 11:22 | +5 | ZEC | UP | 0.69 | 0.76 | 0.42 |
| 10-04 11:21 | +10 stop | XRP | UP | 0.66 | 0.84 | 1.52 |
| 10-04 11:21 | +10 stop | ZEC | UP | 0.68 | 0.82 | 1.13 |
| 10-04 11:20 | +5 | NEAR | DOWN | 0.54 | 0.63 | 0.56 |
| 10-04 11:19 | +10 stop | ZEC | DOWN | 0.62 | 0.43 | -2.29 |
| 10-04 11:19 | +10 stop | HYPE | UP | 0.68 | 0.78 | 0.71 |
| 10-04 11:19 | +20 | HYPE | UP | 0.68 | no | -6.96 |
| 10-04 11:19 | +15 | HYPE | UP | 0.68 | no | -6.96 |
| 10-04 11:19 | +10 | HYPE | UP | 0.68 | 0.78 | 0.71 |
| 10-04 11:19 | +5 | HYPE | UP | 0.68 | 0.74 | 0.30 |
| 10-04 11:18 | +5 | NEAR | DOWN | 0.67 | 0.74 | 0.40 |
| 10-04 11:18 | +10 stop | SOL | UP | 0.62 | 0.76 | 1.10 |
| 10-04 11:18 | +20 | SOL | UP | 0.62 | 0.87 | 2.25 |
| 10-04 11:18 | +15 | SOL | UP | 0.62 | 0.78 | 1.30 |
| 10-04 11:18 | +10 | SOL | UP | 0.62 | 0.76 | 1.10 |
| 10-04 11:18 | +5 | SOL | UP | 0.62 | 0.67 | 0.17 |
| 10-04 11:18 | +10 stop | XRP | DOWN | 0.65 | 0.47 | -2.14 |
| 10-04 11:18 | +10 | XRP | DOWN | 0.65 | yes | -6.66 |
| 10-04 11:18 | +5 | XRP | DOWN | 0.65 | yes | -6.66 |
| 10-04 11:17 | +10 stop | DOGE | DOWN | 0.58 | 0.43 | -1.86 |
| 10-04 11:17 | +10 stop | NEAR | DOWN | 0.69 | 0.48 | -2.43 |
| 10-04 11:17 | +20 | NEAR | DOWN | 0.69 | 0.90 | 1.88 |
| 10-04 11:17 | +15 | NEAR | DOWN | 0.69 | 0.86 | 1.46 |
| 10-04 11:17 | +10 | NEAR | DOWN | 0.69 | 0.82 | 1.04 |
| 10-04 11:17 | +5 | NEAR | DOWN | 0.69 | 0.74 | 0.21 |
| 10-04 11:17 | +10 stop | ETH | UP | 0.68 | 0.84 | 1.34 |
| 10-04 11:17 | +20 | ETH | UP | 0.68 | 0.91 | 2.10 |
| 10-04 11:17 | +15 | ETH | UP | 0.68 | 0.84 | 1.34 |
| 10-04 11:17 | +10 | ETH | UP | 0.68 | 0.84 | 1.34 |
| 10-04 11:17 | +5 | ETH | UP | 0.68 | 0.74 | 0.30 |
| 10-04 11:17 | +10 stop | BTC | UP | 0.64 | 0.75 | 0.79 |
| 10-04 11:17 | +20 | BTC | UP | 0.64 | 0.86 | 1.94 |
| 10-04 11:17 | +15 | BTC | UP | 0.64 | 0.81 | 1.42 |
