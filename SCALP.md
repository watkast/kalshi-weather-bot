# Range-Scalp Bot

*Updated Sun Nov 01 19:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43870 | 38218 | 5652 (65) | 0 | $-12567.76 | -4.5% |
| **+10¢** | 32732 | 26201 | 6531 (86) | 0 | $-11314.89 | -5.5% |
| **+15¢** | 27391 | 20361 | 7030 (113) | 0 | $-10332.56 | -6.0% |
| **+20¢** | 24329 | 16966 | 7363 (147) | 0 | $-9115.77 | -6.0% |
| **+10¢ (15¢ stop)** | 53506 | 53420 | 86 (51) | 0 | $-20236.23 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 19:38 | +10 stop | NEAR | DOWN | 0.55 | 0.65 | 0.66 |
| 11-01 19:36 | +5 | NEAR | DOWN | 0.60 | 0.65 | 0.17 |
| 11-01 19:36 | +5 | NEAR | DOWN | 0.57 | 0.63 | 0.25 |
| 11-01 19:35 | +5 | NEAR | DOWN | 0.62 | 0.68 | 0.27 |
| 11-01 19:34 | +10 stop | XRP | DOWN | 0.62 | 0.78 | 1.30 |
| 11-01 19:34 | +10 | XRP | DOWN | 0.62 | 0.78 | 1.30 |
| 11-01 19:34 | +5 | XRP | DOWN | 0.62 | 0.71 | 0.58 |
| 11-01 19:33 | +10 stop | XRP | DOWN | 0.56 | 0.66 | 0.66 |
| 11-01 19:33 | +20 | XRP | DOWN | 0.56 | 0.78 | 1.89 |
| 11-01 19:33 | +15 | XRP | DOWN | 0.56 | 0.71 | 1.17 |
| 11-01 19:33 | +10 | XRP | DOWN | 0.56 | 0.66 | 0.66 |
| 11-01 19:33 | +5 | XRP | DOWN | 0.56 | 0.66 | 0.61 |
| 11-01 19:32 | +5 | BTC | DOWN | 0.67 | 0.74 | 0.40 |
| 11-01 19:32 | +5 | ETH | DOWN | 0.71 | 0.76 | 0.22 |
| 11-01 19:31 | +10 stop | NEAR | DOWN | 0.69 | 0.47 | -2.53 |
| 11-01 19:31 | +20 | NEAR | DOWN | 0.69 | 0.91 | 1.99 |
| 11-01 19:31 | +15 | NEAR | DOWN | 0.69 | 0.84 | 1.25 |
| 11-01 19:31 | +10 | NEAR | DOWN | 0.69 | 0.84 | 1.25 |
| 11-01 19:31 | +5 | NEAR | DOWN | 0.69 | 0.74 | 0.21 |
| 11-01 19:31 | +10 stop | ETH | DOWN | 0.62 | 0.76 | 1.07 |
| 11-01 19:31 | +20 | ETH | DOWN | 0.62 | 0.85 | 2.01 |
| 11-01 19:31 | +15 | ETH | DOWN | 0.62 | 0.80 | 1.48 |
| 11-01 19:31 | +10 | ETH | DOWN | 0.62 | 0.76 | 1.10 |
| 11-01 19:31 | +5 | ETH | DOWN | 0.62 | 0.69 | 0.38 |
| 11-01 19:31 | +10 stop | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-01 19:31 | +20 | DOGE | DOWN | 0.70 | 0.92 | 1.96 |
| 11-01 19:31 | +15 | DOGE | DOWN | 0.70 | 0.86 | 1.36 |
| 11-01 19:31 | +10 | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-01 19:31 | +5 | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-01 19:31 | +10 stop | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-01 19:31 | +20 | BTC | DOWN | 0.63 | 0.84 | 1.83 |
| 11-01 19:31 | +15 | BTC | DOWN | 0.63 | 0.84 | 1.83 |
| 11-01 19:31 | +10 | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-01 19:31 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-01 19:31 | +10 stop | BNB | DOWN | 0.59 | 0.73 | 1.09 |
| 11-01 19:31 | +20 | BNB | DOWN | 0.59 | 0.81 | 1.92 |
| 11-01 19:31 | +15 | BNB | DOWN | 0.59 | 0.81 | 1.92 |
| 11-01 19:31 | +10 | BNB | DOWN | 0.59 | 0.73 | 1.09 |
| 11-01 19:31 | +5 | BNB | DOWN | 0.59 | 0.67 | 0.47 |
| 11-01 19:22 | +10 stop | HYPE | UP | 0.71 | 0.88 | 1.47 |
