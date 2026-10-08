# Range-Scalp Bot

*Updated Thu Oct 08 15:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7620 | 6605 | 1015 (13) | 0 | $-2360.88 | -4.9% |
| **+10¢** | 5781 | 4582 | 1199 (24) | 0 | $-2298.01 | -6.3% |
| **+15¢** | 4860 | 3598 | 1262 (32) | 0 | $-1879.61 | -6.2% |
| **+20¢** | 4344 | 3035 | 1309 (40) | 0 | $-1465.14 | -5.4% |
| **+10¢ (15¢ stop)** | 9235 | 9206 | 29 (18) | 0 | $-3360.40 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 15:20 | +10 stop | ZEC | DOWN | 0.61 | 0.72 | 0.75 |
| 10-08 15:20 | +5 | ZEC | DOWN | 0.60 | 0.72 | 0.90 |
| 10-08 15:18 | +10 stop | ZEC | UP | 0.51 | 0.34 | -2.04 |
| 10-08 15:17 | +10 stop | SOL | DOWN | 0.69 | 0.83 | 1.16 |
| 10-08 15:17 | +20 | SOL | DOWN | 0.69 | 0.94 | 2.36 |
| 10-08 15:17 | +15 | SOL | DOWN | 0.69 | 0.84 | 1.26 |
| 10-08 15:17 | +10 | SOL | DOWN | 0.69 | 0.83 | 1.16 |
| 10-08 15:17 | +5 | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-08 15:17 | +20 | BTC | DOWN | 0.71 | 0.91 | 1.82 |
| 10-08 15:17 | +15 | BTC | DOWN | 0.71 | 0.88 | 1.47 |
| 10-08 15:17 | +10 | BTC | DOWN | 0.71 | 0.88 | 1.47 |
| 10-08 15:17 | +5 | BTC | DOWN | 0.71 | 0.77 | 0.32 |
| 10-08 15:17 | +10 stop | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 10-08 15:17 | +20 | ETH | DOWN | 0.63 | 0.89 | 2.36 |
| 10-08 15:17 | +15 | ETH | DOWN | 0.63 | 0.78 | 1.20 |
| 10-08 15:17 | +10 | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 10-08 15:17 | +5 | ETH | DOWN | 0.63 | 0.69 | 0.28 |
| 10-08 15:16 | +10 stop | SOL | UP | 0.28 | 0.57 | 2.57 |
| 10-08 15:16 | +20 | SOL | UP | 0.28 | 0.57 | 2.57 |
| 10-08 15:16 | +15 | SOL | UP | 0.28 | 0.57 | 2.57 |
| 10-08 15:16 | +10 | SOL | UP | 0.28 | 0.57 | 2.57 |
| 10-08 15:16 | +5 | SOL | UP | 0.30 | 0.57 | 2.37 |
| 10-08 15:16 | +10 stop | ZEC | DOWN | 0.55 | 0.39 | -1.95 |
| 10-08 15:16 | +20 | ZEC | DOWN | 0.55 | 0.83 | 2.52 |
| 10-08 15:16 | +15 | ZEC | DOWN | 0.55 | 0.72 | 1.37 |
| 10-08 15:16 | +10 | ZEC | DOWN | 0.55 | 0.72 | 1.37 |
| 10-08 15:16 | +5 | ZEC | DOWN | 0.55 | 0.63 | 0.45 |
| 10-08 15:16 | +10 stop | XRP | DOWN | 0.60 | 0.71 | 0.78 |
| 10-08 15:16 | +20 | XRP | DOWN | 0.60 | 0.83 | 2.03 |
| 10-08 15:16 | +15 | XRP | DOWN | 0.60 | 0.79 | 1.61 |
| 10-08 15:16 | +10 | XRP | DOWN | 0.60 | 0.71 | 0.78 |
| 10-08 15:16 | +5 | XRP | DOWN | 0.60 | 0.71 | 0.78 |
| 10-08 15:01 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 10-08 15:01 | +20 | XRP | DOWN | 0.71 | 0.91 | 1.81 |
| 10-08 15:01 | +15 | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 10-08 15:01 | +10 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 10-08 15:01 | +5 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 10-08 15:01 | +10 stop | DOGE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-08 15:01 | +20 | DOGE | DOWN | 0.68 | 0.89 | 1.87 |
| 10-08 15:01 | +15 | DOGE | DOWN | 0.68 | 0.84 | 1.34 |
