# Range-Scalp Bot

*Updated Sun Nov 01 20:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43899 | 38243 | 5656 (65) | 6 | $-12579.56 | -4.6% |
| **+10¢** | 32755 | 26220 | 6535 (86) | 6 | $-11323.40 | -5.5% |
| **+15¢** | 27407 | 20373 | 7034 (113) | 7 | $-10339.97 | -6.0% |
| **+20¢** | 24341 | 16974 | 7367 (147) | 8 | $-9125.73 | -6.0% |
| **+10¢ (15¢ stop)** | 53564 | 53478 | 86 (51) | 0 | $-20292.64 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 20:12 | +10 stop | HYPE | DOWN | 0.60 | 0.40 | -2.34 |
| 11-01 20:12 | +20 | HYPE | DOWN | 0.60 | open |  |
| 11-01 20:12 | +15 | HYPE | DOWN | 0.60 | open |  |
| 11-01 20:12 | +10 | HYPE | DOWN | 0.60 | open |  |
| 11-01 20:12 | +5 | HYPE | DOWN | 0.60 | open |  |
| 11-01 20:11 | +10 stop | XRP | DOWN | 0.59 | 0.75 | 1.29 |
| 11-01 20:11 | +20 | XRP | DOWN | 0.59 | 0.80 | 1.81 |
| 11-01 20:11 | +15 | XRP | DOWN | 0.59 | 0.75 | 1.29 |
| 11-01 20:11 | +10 | XRP | DOWN | 0.60 | 0.75 | 1.19 |
| 11-01 20:11 | +5 | XRP | DOWN | 0.60 | 0.75 | 1.19 |
| 11-01 20:10 | +10 stop | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 11-01 20:10 | +10 stop | BTC | UP | 0.70 | 0.40 | -3.32 |
| 11-01 20:10 | +15 | BTC | UP | 0.70 | open |  |
| 11-01 20:10 | +10 | BTC | UP | 0.70 | open |  |
| 11-01 20:10 | +5 | BTC | UP | 0.70 | open |  |
| 11-01 20:09 | +10 stop | ETH | UP | 0.70 | 0.39 | -3.42 |
| 11-01 20:09 | +10 | ETH | UP | 0.70 | open |  |
| 11-01 20:09 | +5 | ETH | UP | 0.71 | open |  |
| 11-01 20:09 | +10 stop | DOGE | UP | 0.59 | 0.39 | -2.34 |
| 11-01 20:08 | +5 | ETH | UP | 0.63 | 0.73 | 0.69 |
| 11-01 20:07 | +10 stop | ZEC | UP | 0.59 | 0.38 | -2.44 |
| 11-01 20:07 | +10 stop | BNB | UP | 0.68 | 0.48 | -2.29 |
| 11-01 20:07 | +10 stop | ETH | UP | 0.63 | 0.73 | 0.69 |
| 11-01 20:07 | +20 | ETH | UP | 0.63 | open |  |
| 11-01 20:07 | +15 | ETH | UP | 0.63 | open |  |
| 11-01 20:07 | +10 | ETH | UP | 0.63 | 0.73 | 0.69 |
| 11-01 20:07 | +5 | ETH | UP | 0.63 | 0.68 | 0.17 |
| 11-01 20:07 | +10 stop | SOL | UP | 0.67 | 0.35 | -3.52 |
| 11-01 20:07 | +15 | SOL | UP | 0.67 | open |  |
| 11-01 20:07 | +10 stop | DOGE | DOWN | 0.63 | 0.43 | -2.35 |
| 11-01 20:06 | +10 stop | NEAR | DOWN | 0.55 | 0.77 | 1.89 |
| 11-01 20:06 | +10 stop | ZEC | UP | 0.50 | 0.63 | 0.99 |
| 11-01 20:05 | +10 stop | BTC | UP | 0.61 | 0.72 | 0.78 |
| 11-01 20:05 | +10 stop | ETH | UP | 0.60 | 0.71 | 0.76 |
| 11-01 20:05 | +10 stop | ZEC | DOWN | 0.56 | 0.41 | -1.85 |
| 11-01 20:05 | +10 stop | SOL | UP | 0.68 | 0.82 | 1.13 |
| 11-01 20:05 | +5 | BNB | DOWN | 0.65 | 0.84 | 1.64 |
| 11-01 20:04 | +10 stop | ETH | DOWN | 0.69 | 0.52 | -2.03 |
| 11-01 20:04 | +10 stop | SOL | DOWN | 0.68 | 0.49 | -2.24 |
| 11-01 20:04 | +10 | SOL | DOWN | 0.68 | 0.88 | 1.76 |
