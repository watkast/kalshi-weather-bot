# Range-Scalp Bot

*Updated Wed Nov 11 06:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55527 | 48423 | 7104 (94) | 0 | $-15188.47 | -4.3% |
| **+10¢** | 41485 | 33196 | 8289 (124) | 0 | $-14139.13 | -5.4% |
| **+15¢** | 34788 | 25850 | 8938 (158) | 0 | $-12897.63 | -5.9% |
| **+20¢** | 30980 | 21606 | 9374 (207) | 0 | $-11272.71 | -5.8% |
| **+10¢ (15¢ stop)** | 67630 | 67512 | 118 (73) | 0 | $-24909.82 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 06:27 | +10 stop | HYPE | DOWN | 0.67 | 0.52 | -1.84 |
| 11-11 06:27 | +15 | HYPE | DOWN | 0.67 | 0.95 | 2.59 |
| 11-11 06:27 | +10 | HYPE | DOWN | 0.67 | 0.81 | 1.13 |
| 11-11 06:27 | +5 | HYPE | DOWN | 0.67 | 0.81 | 1.13 |
| 11-11 06:27 | +10 stop | NEAR | UP | 0.49 | 0.59 | 0.65 |
| 11-11 06:27 | +20 | NEAR | UP | 0.54 | no | -5.54 |
| 11-11 06:27 | +15 | NEAR | UP | 0.49 | no | -5.08 |
| 11-11 06:27 | +10 | NEAR | UP | 0.49 | 0.59 | 0.65 |
| 11-11 06:27 | +5 | NEAR | UP | 0.49 | 0.59 | 0.65 |
| 11-11 06:26 | +10 stop | BTC | DOWN | 0.52 | 0.62 | 0.65 |
| 11-11 06:26 | +10 | BTC | DOWN | 0.52 | 0.62 | 0.65 |
| 11-11 06:26 | +5 | BTC | DOWN | 0.49 | 0.62 | 0.95 |
| 11-11 06:26 | +10 stop | ZEC | DOWN | 0.63 | 0.76 | 1.00 |
| 11-11 06:26 | +5 | ZEC | DOWN | 0.63 | 0.69 | 0.28 |
| 11-11 06:24 | +10 stop | HYPE | DOWN | 0.66 | 0.81 | 1.23 |
| 11-11 06:24 | +10 stop | SOL | DOWN | 0.71 | 0.81 | 0.78 |
| 11-11 06:23 | +10 stop | ETH | DOWN | 0.58 | 0.74 | 1.28 |
| 11-11 06:23 | +10 stop | DOGE | DOWN | 0.64 | 0.83 | 1.61 |
| 11-11 06:23 | +20 | DOGE | DOWN | 0.64 | 0.87 | 2.03 |
| 11-11 06:23 | +15 | DOGE | DOWN | 0.64 | 0.83 | 1.61 |
| 11-11 06:23 | +10 | DOGE | DOWN | 0.64 | 0.83 | 1.63 |
| 11-11 06:22 | +10 stop | BTC | UP | 0.61 | 0.74 | 0.99 |
| 11-11 06:22 | +10 stop | XRP | DOWN | 0.63 | 0.48 | -1.85 |
| 11-11 06:22 | +20 | XRP | DOWN | 0.63 | 0.84 | 1.83 |
| 11-11 06:22 | +15 | XRP | DOWN | 0.63 | 0.82 | 1.62 |
| 11-11 06:22 | +10 | XRP | DOWN | 0.64 | 0.82 | 1.54 |
| 11-11 06:22 | +5 | XRP | DOWN | 0.64 | 0.82 | 1.54 |
| 11-11 06:22 | +10 stop | SOL | UP | 0.64 | 0.76 | 0.90 |
| 11-11 06:22 | +10 stop | ZEC | DOWN | 0.65 | 0.78 | 1.01 |
| 11-11 06:22 | +5 | ZEC | DOWN | 0.66 | 0.73 | 0.40 |
| 11-11 06:22 | +5 | NEAR | DOWN | 0.59 | 0.68 | 0.57 |
| 11-11 06:20 | +10 stop | NEAR | DOWN | 0.66 | 0.50 | -1.94 |
| 11-11 06:20 | +5 | ETH | DOWN | 0.70 | 0.79 | 0.63 |
| 11-11 06:20 | +15 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 11-11 06:20 | +10 stop | HYPE | DOWN | 0.62 | 0.39 | -2.64 |
| 11-11 06:20 | +10 stop | BTC | DOWN | 0.58 | 0.40 | -2.15 |
| 11-11 06:20 | +10 stop | SOL | DOWN | 0.70 | 0.52 | -2.13 |
| 11-11 06:20 | +10 | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 11-11 06:20 | +5 | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 11-11 06:20 | +5 | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
