# Range-Scalp Bot

*Updated Wed Nov 04 17:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47302 | 41191 | 6111 (72) | 1 | $-13621.78 | -4.6% |
| **+10¢** | 35337 | 28247 | 7090 (97) | 2 | $-12454.50 | -5.6% |
| **+15¢** | 29591 | 21958 | 7633 (125) | 2 | $-11415.91 | -6.1% |
| **+20¢** | 26291 | 18297 | 7994 (165) | 2 | $-10069.25 | -6.1% |
| **+10¢ (15¢ stop)** | 57655 | 57562 | 93 (56) | 0 | $-21491.52 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 17:27 | +10 stop | SOL | UP | 0.44 | 0.56 | 0.84 |
| 11-04 17:25 | +10 stop | SOL | UP | 0.65 | 0.39 | -2.93 |
| 11-04 17:24 | +10 stop | SOL | UP | 0.63 | 0.43 | -2.35 |
| 11-04 17:23 | +10 stop | ZEC | UP | 0.67 | 0.83 | 1.34 |
| 11-04 17:22 | +5 | ZEC | UP | 0.61 | 0.68 | 0.37 |
| 11-04 17:22 | +10 stop | HYPE | UP | 0.70 | 0.85 | 1.26 |
| 11-04 17:22 | +20 | HYPE | UP | 0.70 | 0.93 | 2.11 |
| 11-04 17:22 | +15 | HYPE | UP | 0.71 | 0.87 | 1.37 |
| 11-04 17:22 | +10 | HYPE | UP | 0.71 | 0.85 | 1.16 |
| 11-04 17:22 | +5 | HYPE | UP | 0.70 | 0.77 | 0.42 |
| 11-04 17:22 | +10 stop | DOGE | DOWN | 0.55 | 0.34 | -2.44 |
| 11-04 17:22 | +5 | NEAR | UP | 0.60 | 0.66 | 0.27 |
| 11-04 17:22 | +10 stop | BTC | UP | 0.66 | 0.77 | 0.81 |
| 11-04 17:21 | +5 | NEAR | UP | 0.60 | 0.65 | 0.17 |
| 11-04 17:21 | +10 stop | DOGE | UP | 0.61 | 0.43 | -2.15 |
| 11-04 17:21 | +5 | DOGE | UP | 0.61 | 0.73 | 0.89 |
| 11-04 17:21 | +10 stop | NEAR | UP | 0.62 | 0.79 | 1.41 |
| 11-04 17:21 | +10 | NEAR | UP | 0.62 | 0.79 | 1.41 |
| 11-04 17:21 | +5 | NEAR | UP | 0.62 | 0.69 | 0.38 |
| 11-04 17:20 | +10 stop | BTC | UP | 0.66 | 0.78 | 0.91 |
| 11-04 17:19 | +15 | DOGE | UP | 0.59 | 0.77 | 1.50 |
| 11-04 17:19 | +5 | DOGE | UP | 0.59 | 0.70 | 0.78 |
| 11-04 17:19 | +10 stop | NEAR | UP | 0.55 | 0.69 | 1.07 |
| 11-04 17:19 | +20 | NEAR | UP | 0.55 | 0.79 | 2.10 |
| 11-04 17:19 | +15 | NEAR | UP | 0.55 | 0.71 | 1.27 |
| 11-04 17:19 | +10 | NEAR | UP | 0.55 | 0.69 | 1.07 |
| 11-04 17:19 | +5 | NEAR | UP | 0.55 | 0.69 | 1.07 |
| 11-04 17:19 | +10 stop | SOL | UP | 0.68 | 0.49 | -2.24 |
| 11-04 17:19 | +20 | SOL | UP | 0.68 | 0.91 | 2.08 |
| 11-04 17:19 | +15 | SOL | UP | 0.68 | 0.91 | 2.08 |
| 11-04 17:19 | +10 | SOL | UP | 0.68 | 0.82 | 1.13 |
| 11-04 17:19 | +5 | SOL | UP | 0.68 | 0.82 | 1.15 |
| 11-04 17:18 | +10 stop | ZEC | DOWN | 0.55 | 0.40 | -1.85 |
| 11-04 17:18 | +20 | ZEC | DOWN | 0.55 | open |  |
| 11-04 17:18 | +15 | ZEC | DOWN | 0.55 | open |  |
| 11-04 17:18 | +10 | ZEC | DOWN | 0.54 | open |  |
| 11-04 17:18 | +5 | ZEC | DOWN | 0.54 | 0.60 | 0.25 |
| 11-04 17:18 | +5 | HYPE | UP | 0.62 | 0.75 | 0.99 |
| 11-04 17:18 | +10 stop | HYPE | UP | 0.54 | 0.75 | 1.78 |
| 11-04 17:18 | +20 | HYPE | UP | 0.54 | 0.75 | 1.78 |
