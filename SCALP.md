# Range-Scalp Bot

*Updated Sun Oct 04 04:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 1718 | 1478 | 240 (3) | 0 | $-594.42 | -5.5% |
| **+10¢** | 1332 | 1067 | 265 (4) | 0 | $-428.77 | -5.1% |
| **+15¢** | 1124 | 845 | 279 (5) | 0 | $-353.89 | -5.0% |
| **+20¢** | 989 | 691 | 298 (7) | 0 | $-366.87 | -5.9% |
| **+10¢ (15¢ stop)** | 2174 | 2173 | 1 (1) | 0 | $-920.39 | -6.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 03:56 | +10 stop | BNB | UP | 0.61 | 0.76 | 1.20 |
| 10-04 03:56 | +20 | BNB | UP | 0.61 | 0.89 | 2.56 |
| 10-04 03:56 | +15 | BNB | UP | 0.61 | 0.76 | 1.20 |
| 10-04 03:56 | +10 | BNB | UP | 0.61 | 0.76 | 1.20 |
| 10-04 03:56 | +5 | BNB | UP | 0.61 | 0.70 | 0.58 |
| 10-04 03:53 | +5 | XRP | DOWN | 0.71 | 0.84 | 1.05 |
| 10-04 03:53 | +10 stop | XRP | DOWN | 0.71 | 0.84 | 1.05 |
| 10-04 03:51 | +10 stop | XRP | UP | 0.56 | 0.39 | -2.05 |
| 10-04 03:51 | +10 stop | HYPE | DOWN | 0.56 | 0.74 | 1.43 |
| 10-04 03:51 | +5 | HYPE | DOWN | 0.58 | 0.74 | 1.28 |
| 10-04 03:50 | +10 stop | XRP | DOWN | 0.64 | 0.41 | -2.64 |
| 10-04 03:50 | +10 | XRP | DOWN | 0.64 | 0.84 | 1.73 |
| 10-04 03:49 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-04 03:49 | +10 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-04 03:49 | +5 | ETH | DOWN | 0.66 | 0.71 | 0.19 |
| 10-04 03:49 | +5 | XRP | DOWN | 0.65 | 0.71 | 0.29 |
| 10-04 03:48 | +10 stop | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 10-04 03:48 | +10 stop | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 10-04 03:48 | +10 | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 10-04 03:48 | +5 | XRP | DOWN | 0.57 | 0.64 | 0.35 |
| 10-04 03:48 | +10 stop | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-04 03:48 | +20 | DOGE | DOWN | 0.66 | 0.87 | 1.86 |
| 10-04 03:48 | +15 | DOGE | DOWN | 0.66 | 0.82 | 1.33 |
| 10-04 03:48 | +10 | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-04 03:48 | +5 | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 10-04 03:48 | +10 stop | HYPE | DOWN | 0.57 | 0.67 | 0.66 |
| 10-04 03:47 | +10 stop | XRP | DOWN | 0.52 | 0.63 | 0.75 |
| 10-04 03:47 | +10 | XRP | DOWN | 0.52 | 0.63 | 0.75 |
| 10-04 03:47 | +5 | XRP | DOWN | 0.52 | 0.63 | 0.75 |
| 10-04 03:47 | +5 | ETH | DOWN | 0.57 | 0.65 | 0.46 |
| 10-04 03:46 | +10 stop | BTC | DOWN | 0.67 | 0.84 | 1.44 |
| 10-04 03:46 | +20 | BTC | DOWN | 0.66 | 0.87 | 1.86 |
| 10-04 03:46 | +15 | BTC | DOWN | 0.66 | 0.84 | 1.54 |
| 10-04 03:46 | +10 | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 10-04 03:46 | +5 | BTC | DOWN | 0.66 | 0.75 | 0.60 |
| 10-04 03:46 | +20 | ZEC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-04 03:46 | +10 stop | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-04 03:46 | +15 | ZEC | DOWN | 0.69 | 0.88 | 1.67 |
| 10-04 03:46 | +10 | ZEC | DOWN | 0.69 | 0.80 | 0.81 |
| 10-04 03:46 | +5 | ZEC | DOWN | 0.69 | 0.77 | 0.50 |
