# Range-Scalp Bot

*Updated Sun Nov 01 19:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43839 | 38194 | 5645 (65) | 5 | $-12534.51 | -4.5% |
| **+10¢** | 32709 | 26186 | 6523 (86) | 5 | $-11280.72 | -5.5% |
| **+15¢** | 27371 | 20348 | 7023 (113) | 4 | $-10310.38 | -6.0% |
| **+20¢** | 24310 | 16954 | 7356 (147) | 4 | $-9096.85 | -6.0% |
| **+10¢ (15¢ stop)** | 53478 | 53392 | 86 (51) | 0 | $-20232.53 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 19:10 | +10 stop | NEAR | DOWN | 0.55 | 0.67 | 0.86 |
| 11-01 19:10 | +10 | NEAR | DOWN | 0.55 | 0.67 | 0.86 |
| 11-01 19:10 | +5 | NEAR | DOWN | 0.55 | 0.60 | 0.15 |
| 11-01 19:10 | +10 stop | ZEC | UP | 0.55 | 0.20 | -3.80 |
| 11-01 19:10 | +5 | ZEC | UP | 0.55 | open |  |
| 11-01 19:10 | +10 stop | DOGE | DOWN | 0.63 | 0.88 | 2.25 |
| 11-01 19:10 | +15 | DOGE | DOWN | 0.63 | 0.88 | 2.25 |
| 11-01 19:10 | +10 | DOGE | DOWN | 0.63 | 0.88 | 2.20 |
| 11-01 19:10 | +5 | DOGE | DOWN | 0.63 | 0.70 | 0.33 |
| 11-01 19:08 | +10 stop | HYPE | DOWN | 0.64 | 0.86 | 1.94 |
| 11-01 19:08 | +10 stop | ETH | UP | 0.53 | 0.38 | -1.85 |
| 11-01 19:08 | +10 stop | ZEC | UP | 0.68 | 0.36 | -3.53 |
| 11-01 19:08 | +10 | ZEC | UP | 0.68 | open |  |
| 11-01 19:08 | +5 | ZEC | UP | 0.67 | 0.74 | 0.40 |
| 11-01 19:07 | +10 stop | DOGE | UP | 0.59 | 0.30 | -3.22 |
| 11-01 19:07 | +10 stop | NEAR | UP | 0.69 | 0.43 | -2.92 |
| 11-01 19:07 | +10 | NEAR | UP | 0.65 | 0.76 | 0.81 |
| 11-01 19:07 | +5 | NEAR | UP | 0.65 | 0.71 | 0.29 |
| 11-01 19:07 | +10 stop | SOL | DOWN | 0.69 | 0.81 | 0.94 |
| 11-01 19:07 | +5 | XRP | UP | 0.63 | open |  |
| 11-01 19:07 | +10 stop | SOL | UP | 0.63 | 0.43 | -2.35 |
| 11-01 19:06 | +10 stop | ZEC | UP | 0.62 | 0.75 | 0.99 |
| 11-01 19:06 | +10 | ZEC | UP | 0.62 | 0.75 | 0.99 |
| 11-01 19:06 | +5 | ZEC | UP | 0.62 | 0.67 | 0.17 |
| 11-01 19:06 | +10 stop | BTC | UP | 0.63 | 0.44 | -2.25 |
| 11-01 19:06 | +10 stop | HYPE | UP | 0.48 | 0.32 | -1.98 |
| 11-01 19:05 | +10 stop | SOL | UP | 0.62 | 0.45 | -2.10 |
| 11-01 19:05 | +20 | SOL | UP | 0.62 | open |  |
| 11-01 19:05 | +15 | SOL | UP | 0.62 | open |  |
| 11-01 19:05 | +10 | SOL | UP | 0.62 | open |  |
| 11-01 19:05 | +5 | SOL | UP | 0.62 | open |  |
| 11-01 19:05 | +10 stop | XRP | UP | 0.59 | 0.44 | -1.85 |
| 11-01 19:05 | +10 | XRP | UP | 0.59 | open |  |
| 11-01 19:05 | +5 | XRP | UP | 0.59 | 0.66 | 0.37 |
| 11-01 19:05 | +10 stop | NEAR | UP | 0.71 | 0.81 | 0.74 |
| 11-01 19:05 | +10 | NEAR | UP | 0.71 | 0.81 | 0.74 |
| 11-01 19:04 | +10 stop | HYPE | DOWN | 0.60 | 0.41 | -2.28 |
| 11-01 19:04 | +5 | NEAR | UP | 0.66 | 0.73 | 0.40 |
| 11-01 19:04 | +10 stop | ZEC | UP | 0.57 | 0.70 | 0.97 |
| 11-01 19:04 | +10 | ZEC | UP | 0.57 | 0.70 | 0.97 |
