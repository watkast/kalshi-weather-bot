# Range-Scalp Bot

*Updated Sun Oct 18 08:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22284 | 19398 | 2886 (29) | 0 | $-6489.43 | -4.6% |
| **+10¢** | 16781 | 13447 | 3334 (42) | 0 | $-5772.41 | -5.5% |
| **+15¢** | 14053 | 10456 | 3597 (62) | 0 | $-5275.83 | -6.0% |
| **+20¢** | 12435 | 8667 | 3768 (80) | 0 | $-4726.20 | -6.1% |
| **+10¢ (15¢ stop)** | 27426 | 27376 | 50 (29) | 0 | $-10472.21 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 08:28 | +10 stop | XRP | UP | 0.24 | 0.50 | 2.29 |
| 10-18 08:26 | +10 stop | BTC | UP | 0.63 | 0.74 | 0.79 |
| 10-18 08:25 | +10 stop | XRP | UP | 0.69 | 0.52 | -2.03 |
| 10-18 08:25 | +10 stop | BTC | UP | 0.68 | 0.50 | -2.14 |
| 10-18 08:25 | +10 stop | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 10-18 08:25 | +10 stop | ZEC | DOWN | 0.62 | 0.75 | 0.99 |
| 10-18 08:24 | +10 stop | DOGE | DOWN | 0.59 | 0.70 | 0.80 |
| 10-18 08:23 | +10 stop | ZEC | UP | 0.65 | 0.77 | 0.91 |
| 10-18 08:23 | +10 stop | BNB | UP | 0.66 | 0.44 | -2.54 |
| 10-18 08:22 | +10 stop | DOGE | UP | 0.64 | 0.40 | -2.74 |
| 10-18 08:22 | +10 | DOGE | UP | 0.64 | no | -6.57 |
| 10-18 08:20 | +10 stop | SOL | UP | 0.68 | 0.78 | 0.71 |
| 10-18 08:20 | +10 stop | BNB | DOWN | 0.69 | 0.46 | -2.63 |
| 10-18 08:20 | +20 | BNB | DOWN | 0.69 | 0.92 | 2.14 |
| 10-18 08:20 | +15 | BNB | DOWN | 0.69 | 0.84 | 1.25 |
| 10-18 08:20 | +10 | BNB | DOWN | 0.69 | 0.84 | 1.25 |
| 10-18 08:20 | +5 | BNB | DOWN | 0.69 | 0.76 | 0.42 |
| 10-18 08:20 | +10 stop | BTC | UP | 0.67 | 0.79 | 0.92 |
| 10-18 08:20 | +10 stop | DOGE | UP | 0.58 | 0.68 | 0.66 |
| 10-18 08:20 | +10 | DOGE | UP | 0.58 | 0.68 | 0.66 |
| 10-18 08:19 | +10 stop | ETH | UP | 0.70 | 0.82 | 0.94 |
| 10-18 08:19 | +10 stop | DOGE | DOWN | 0.49 | 0.66 | 1.36 |
| 10-18 08:19 | +10 | DOGE | DOWN | 0.49 | 0.66 | 1.36 |
| 10-18 08:19 | +5 | ZEC | DOWN | 0.59 | 0.64 | 0.16 |
| 10-18 08:19 | +10 stop | ZEC | DOWN | 0.53 | 0.29 | -2.73 |
| 10-18 08:19 | +20 | ZEC | DOWN | 0.53 | 0.75 | 1.88 |
| 10-18 08:19 | +15 | ZEC | DOWN | 0.54 | 0.75 | 1.78 |
| 10-18 08:19 | +10 | ZEC | DOWN | 0.54 | 0.64 | 0.65 |
| 10-18 08:19 | +5 | ZEC | DOWN | 0.55 | 0.60 | 0.15 |
| 10-18 08:18 | +10 stop | HYPE | UP | 0.63 | 0.77 | 1.06 |
| 10-18 08:17 | +10 stop | XRP | UP | 0.60 | 0.80 | 1.71 |
| 10-18 08:17 | +5 | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-18 08:16 | +10 stop | XRP | DOWN | 0.56 | 0.38 | -2.15 |
| 10-18 08:16 | +20 | XRP | DOWN | 0.56 | 0.92 | 3.41 |
| 10-18 08:16 | +15 | XRP | DOWN | 0.56 | 0.73 | 1.38 |
| 10-18 08:16 | +10 | XRP | DOWN | 0.56 | 0.73 | 1.38 |
| 10-18 08:16 | +5 | XRP | DOWN | 0.57 | 0.73 | 1.28 |
| 10-18 08:16 | +10 stop | ETH | DOWN | 0.62 | 0.40 | -2.54 |
| 10-18 08:16 | +20 | ETH | DOWN | 0.62 | yes | -6.37 |
| 10-18 08:16 | +15 | ETH | DOWN | 0.62 | yes | -6.37 |
