# Range-Scalp Bot

*Updated Sun Nov 01 21:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43974 | 38306 | 5668 (65) | 2 | $-12623.42 | -4.6% |
| **+10¢** | 32809 | 26261 | 6548 (86) | 2 | $-11361.32 | -5.5% |
| **+15¢** | 27457 | 20409 | 7048 (113) | 3 | $-10376.32 | -6.0% |
| **+20¢** | 24386 | 17004 | 7382 (147) | 4 | $-9159.22 | -6.0% |
| **+10¢ (15¢ stop)** | 53637 | 53551 | 86 (51) | 0 | $-20305.20 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 21:20 | +10 stop | ZEC | UP | 0.62 | 0.74 | 0.89 |
| 11-01 21:20 | +20 | ZEC | UP | 0.62 | open |  |
| 11-01 21:20 | +15 | ZEC | UP | 0.62 | 0.77 | 1.20 |
| 11-01 21:20 | +10 | ZEC | UP | 0.62 | 0.74 | 0.89 |
| 11-01 21:20 | +5 | ZEC | UP | 0.62 | 0.74 | 0.89 |
| 11-01 21:19 | +10 stop | BNB | DOWN | 0.66 | 0.79 | 1.02 |
| 11-01 21:18 | +10 stop | BTC | DOWN | 0.59 | 0.77 | 1.50 |
| 11-01 21:18 | +10 stop | XRP | DOWN | 0.65 | 0.83 | 1.54 |
| 11-01 21:18 | +15 | XRP | DOWN | 0.65 | 0.83 | 1.54 |
| 11-01 21:18 | +10 | XRP | DOWN | 0.65 | 0.83 | 1.54 |
| 11-01 21:18 | +5 | XRP | DOWN | 0.65 | 0.72 | 0.39 |
| 11-01 21:18 | +10 stop | ETH | DOWN | 0.63 | 0.85 | 1.94 |
| 11-01 21:18 | +10 stop | SOL | DOWN | 0.58 | 0.69 | 0.77 |
| 11-01 21:18 | +10 | SOL | DOWN | 0.58 | 0.69 | 0.77 |
| 11-01 21:18 | +5 | SOL | DOWN | 0.58 | 0.69 | 0.77 |
| 11-01 21:17 | +5 | ZEC | UP | 0.62 | 0.81 | 1.62 |
| 11-01 21:17 | +10 stop | HYPE | DOWN | 0.60 | 0.72 | 0.88 |
| 11-01 21:17 | +10 stop | BTC | DOWN | 0.70 | 0.54 | -1.93 |
| 11-01 21:17 | +15 | BTC | DOWN | 0.70 | open |  |
| 11-01 21:17 | +10 | BTC | DOWN | 0.70 | 0.84 | 1.15 |
| 11-01 21:17 | +5 | BTC | DOWN | 0.70 | 0.77 | 0.42 |
| 11-01 21:17 | +10 stop | BNB | DOWN | 0.52 | 0.62 | 0.65 |
| 11-01 21:17 | +10 stop | DOGE | DOWN | 0.70 | 0.92 | 2.03 |
| 11-01 21:17 | +10 | DOGE | DOWN | 0.70 | 0.92 | 2.03 |
| 11-01 21:17 | +5 | DOGE | DOWN | 0.70 | 0.76 | 0.32 |
| 11-01 21:17 | +10 stop | SOL | DOWN | 0.50 | 0.60 | 0.65 |
| 11-01 21:17 | +20 | SOL | DOWN | 0.50 | 0.88 | 3.54 |
| 11-01 21:17 | +15 | SOL | DOWN | 0.50 | 0.69 | 1.57 |
| 11-01 21:17 | +10 | SOL | DOWN | 0.50 | 0.60 | 0.65 |
| 11-01 21:17 | +5 | SOL | DOWN | 0.50 | 0.60 | 0.65 |
| 11-01 21:17 | +10 stop | ZEC | UP | 0.54 | 0.81 | 2.41 |
| 11-01 21:17 | +20 | ZEC | UP | 0.54 | 0.81 | 2.41 |
| 11-01 21:17 | +15 | ZEC | UP | 0.54 | 0.81 | 2.41 |
| 11-01 21:17 | +10 | ZEC | UP | 0.54 | 0.81 | 2.41 |
| 11-01 21:17 | +5 | ZEC | UP | 0.54 | 0.62 | 0.45 |
| 11-01 21:16 | +10 stop | HYPE | UP | 0.57 | 0.39 | -2.15 |
| 11-01 21:16 | +20 | HYPE | UP | 0.57 | 0.80 | 2.00 |
| 11-01 21:16 | +15 | HYPE | UP | 0.57 | 0.74 | 1.38 |
| 11-01 21:16 | +10 | HYPE | UP | 0.57 | 0.74 | 1.38 |
| 11-01 21:16 | +5 | HYPE | UP | 0.57 | 0.66 | 0.56 |
