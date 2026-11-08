# Range-Scalp Bot

*Updated Sun Nov 08 23:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52992 | 46206 | 6786 (85) | 0 | $-14643.33 | -4.4% |
| **+10¢** | 39559 | 31648 | 7911 (110) | 0 | $-13620.42 | -5.5% |
| **+15¢** | 33145 | 24621 | 8524 (141) | 0 | $-12438.79 | -6.0% |
| **+20¢** | 29485 | 20550 | 8935 (186) | 0 | $-10927.54 | -5.9% |
| **+10¢ (15¢ stop)** | 64528 | 64422 | 106 (63) | 0 | $-23897.09 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 23:51 | +5 | HYPE | DOWN | 0.61 | 0.74 | 0.99 |
| 11-08 23:50 | +10 stop | ZEC | UP | 0.59 | 0.32 | -3.03 |
| 11-08 23:50 | +10 stop | NEAR | DOWN | 0.69 | 0.80 | 0.83 |
| 11-08 23:50 | +10 | NEAR | DOWN | 0.67 | 0.80 | 1.02 |
| 11-08 23:50 | +5 | NEAR | DOWN | 0.68 | 0.73 | 0.20 |
| 11-08 23:50 | +5 | HYPE | DOWN | 0.60 | 0.66 | 0.27 |
| 11-08 23:49 | +5 | HYPE | DOWN | 0.57 | 0.66 | 0.57 |
| 11-08 23:49 | +10 stop | XRP | DOWN | 0.63 | 0.74 | 0.79 |
| 11-08 23:49 | +5 | XRP | DOWN | 0.63 | 0.68 | 0.17 |
| 11-08 23:47 | +10 stop | XRP | DOWN | 0.59 | 0.73 | 1.09 |
| 11-08 23:47 | +10 stop | DOGE | DOWN | 0.66 | 0.77 | 0.80 |
| 11-08 23:47 | +10 | DOGE | DOWN | 0.66 | 0.77 | 0.80 |
| 11-08 23:47 | +5 | DOGE | DOWN | 0.66 | 0.72 | 0.29 |
| 11-08 23:47 | +10 stop | HYPE | DOWN | 0.67 | 0.80 | 1.02 |
| 11-08 23:47 | +20 | HYPE | DOWN | 0.67 | 0.87 | 1.76 |
| 11-08 23:47 | +15 | HYPE | DOWN | 0.67 | 0.83 | 1.34 |
| 11-08 23:47 | +10 | HYPE | DOWN | 0.67 | 0.80 | 1.02 |
| 11-08 23:47 | +5 | HYPE | DOWN | 0.67 | 0.72 | 0.19 |
| 11-08 23:47 | +10 stop | XRP | DOWN | 0.70 | 0.55 | -1.83 |
| 11-08 23:47 | +20 | XRP | DOWN | 0.70 | 0.91 | 1.92 |
| 11-08 23:47 | +15 | XRP | DOWN | 0.70 | 0.89 | 1.68 |
| 11-08 23:47 | +10 | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 11-08 23:47 | +5 | XRP | DOWN | 0.70 | 0.75 | 0.21 |
| 11-08 23:46 | +20 | SOL | DOWN | 0.68 | 0.90 | 1.99 |
| 11-08 23:46 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-08 23:46 | +15 | SOL | DOWN | 0.71 | 0.90 | 1.70 |
| 11-08 23:46 | +10 | SOL | DOWN | 0.71 | 0.83 | 0.95 |
| 11-08 23:46 | +5 | SOL | DOWN | 0.71 | 0.78 | 0.42 |
| 11-08 23:46 | +10 stop | ZEC | DOWN | 0.69 | 0.36 | -3.62 |
| 11-08 23:46 | +20 | ZEC | DOWN | 0.70 | 0.95 | 2.28 |
| 11-08 23:46 | +15 | ZEC | DOWN | 0.70 | 0.95 | 2.28 |
| 11-08 23:46 | +10 | ZEC | DOWN | 0.70 | 0.95 | 2.28 |
| 11-08 23:46 | +5 | ZEC | DOWN | 0.71 | 0.95 | 2.18 |
| 11-08 23:46 | +10 stop | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 11-08 23:46 | +20 | ETH | DOWN | 0.70 | 0.93 | 2.13 |
| 11-08 23:46 | +15 | ETH | DOWN | 0.70 | 0.87 | 1.47 |
| 11-08 23:46 | +10 | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 11-08 23:46 | +5 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 11-08 23:46 | +10 stop | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 11-08 23:46 | +20 | NEAR | DOWN | 0.65 | 0.90 | 2.27 |
