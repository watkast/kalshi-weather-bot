# Range-Scalp Bot

*Updated Sat Nov 07 17:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51249 | 44678 | 6571 (79) | 4 | $-14307.47 | -4.4% |
| **+10¢** | 38254 | 30596 | 7658 (105) | 5 | $-13289.21 | -5.5% |
| **+15¢** | 32026 | 23772 | 8254 (134) | 5 | $-12207.83 | -6.1% |
| **+20¢** | 28485 | 19834 | 8651 (177) | 5 | $-10768.47 | -6.0% |
| **+10¢ (15¢ stop)** | 62449 | 62346 | 103 (61) | 0 | $-23138.62 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 17:28 | +5 | XRP | DOWN | 0.57 | open |  |
| 11-07 17:27 | +10 stop | BNB | UP | 0.52 | 0.66 | 1.06 |
| 11-07 17:26 | +10 stop | SOL | DOWN | 0.69 | 0.49 | -2.33 |
| 11-07 17:26 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 11-07 17:26 | +10 stop | XRP | DOWN | 0.53 | 0.35 | -2.14 |
| 11-07 17:26 | +5 | XRP | DOWN | 0.54 | 0.59 | 0.15 |
| 11-07 17:24 | +10 stop | BNB | UP | 0.65 | 0.47 | -2.14 |
| 11-07 17:24 | +10 stop | SOL | UP | 0.70 | 0.54 | -1.93 |
| 11-07 17:24 | +10 stop | BNB | DOWN | 0.59 | 0.44 | -1.85 |
| 11-07 17:23 | +10 stop | BTC | DOWN | 0.60 | 0.78 | 1.50 |
| 11-07 17:23 | +10 stop | ZEC | DOWN | 0.68 | 0.49 | -2.24 |
| 11-07 17:23 | +20 | ZEC | DOWN | 0.68 | 0.88 | 1.76 |
| 11-07 17:23 | +15 | ZEC | DOWN | 0.68 | 0.87 | 1.66 |
| 11-07 17:23 | +10 | ZEC | DOWN | 0.68 | 0.87 | 1.66 |
| 11-07 17:23 | +5 | ZEC | DOWN | 0.67 | 0.87 | 1.71 |
| 11-07 17:22 | +10 stop | NEAR | UP | 0.65 | 0.76 | 0.81 |
| 11-07 17:22 | +10 stop | HYPE | UP | 0.67 | 0.81 | 1.13 |
| 11-07 17:21 | +10 stop | SOL | DOWN | 0.57 | 0.41 | -1.95 |
| 11-07 17:21 | +5 | SOL | DOWN | 0.57 | 0.66 | 0.56 |
| 11-07 17:21 | +5 | BTC | DOWN | 0.60 | 0.78 | 1.50 |
| 11-07 17:21 | +10 stop | SOL | DOWN | 0.55 | 0.68 | 0.92 |
| 11-07 17:21 | +5 | SOL | DOWN | 0.55 | 0.68 | 0.92 |
| 11-07 17:21 | +10 stop | BNB | UP | 0.61 | 0.75 | 1.04 |
| 11-07 17:21 | +10 stop | XRP | DOWN | 0.54 | 0.33 | -2.44 |
| 11-07 17:20 | +10 stop | HYPE | DOWN | 0.60 | 0.38 | -2.54 |
| 11-07 17:20 | +10 stop | DOGE | DOWN | 0.61 | 0.79 | 1.46 |
| 11-07 17:19 | +10 stop | SOL | DOWN | 0.60 | 0.72 | 0.88 |
| 11-07 17:19 | +10 stop | NEAR | DOWN | 0.53 | 0.37 | -1.95 |
| 11-07 17:18 | +10 stop | XRP | UP | 0.54 | 0.65 | 0.76 |
| 11-07 17:18 | +10 stop | DOGE | UP | 0.65 | 0.44 | -2.44 |
| 11-07 17:18 | +10 stop | HYPE | UP | 0.62 | 0.47 | -1.85 |
| 11-07 17:16 | +10 stop | DOGE | DOWN | 0.62 | 0.43 | -2.25 |
| 11-07 17:16 | +20 | DOGE | DOWN | 0.62 | 0.88 | 2.35 |
| 11-07 17:16 | +15 | DOGE | DOWN | 0.62 | 0.79 | 1.41 |
| 11-07 17:16 | +10 | DOGE | DOWN | 0.62 | 0.79 | 1.41 |
| 11-07 17:16 | +5 | DOGE | DOWN | 0.62 | 0.70 | 0.48 |
| 11-07 17:16 | +10 stop | SOL | DOWN | 0.68 | 0.53 | -1.84 |
| 11-07 17:16 | +20 | SOL | DOWN | 0.68 | open |  |
| 11-07 17:16 | +15 | SOL | DOWN | 0.68 | open |  |
| 11-07 17:16 | +10 | SOL | DOWN | 0.68 | open |  |
