# Range-Scalp Bot

*Updated Thu Oct 22 22:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29358 | 25549 | 3809 (39) | 1 | $-8697.82 | -4.7% |
| **+10¢** | 22014 | 17606 | 4408 (55) | 3 | $-7838.96 | -5.7% |
| **+15¢** | 18435 | 13701 | 4734 (78) | 3 | $-7024.44 | -6.1% |
| **+20¢** | 16318 | 11354 | 4964 (100) | 3 | $-6372.61 | -6.2% |
| **+10¢ (15¢ stop)** | 36025 | 35966 | 59 (32) | 0 | $-13585.48 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 22:19 | +5 | NEAR | DOWN | 0.64 | 0.73 | 0.59 |
| 10-22 22:19 | +10 stop | DOGE | DOWN | 0.63 | 0.84 | 1.83 |
| 10-22 22:19 | +10 stop | NEAR | DOWN | 0.60 | 0.73 | 0.99 |
| 10-22 22:19 | +10 stop | ZEC | DOWN | 0.56 | 0.66 | 0.70 |
| 10-22 22:19 | +5 | NEAR | DOWN | 0.58 | 0.65 | 0.36 |
| 10-22 22:19 | +5 | DOGE | DOWN | 0.61 | 0.70 | 0.59 |
| 10-22 22:18 | +10 stop | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-22 22:18 | +20 | SOL | DOWN | 0.63 | 0.87 | 2.15 |
| 10-22 22:18 | +15 | SOL | DOWN | 0.63 | 0.79 | 1.31 |
| 10-22 22:18 | +10 | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-22 22:18 | +5 | SOL | DOWN | 0.63 | 0.69 | 0.28 |
| 10-22 22:18 | +10 stop | XRP | DOWN | 0.53 | 0.64 | 0.75 |
| 10-22 22:18 | +20 | XRP | DOWN | 0.53 | 0.78 | 2.19 |
| 10-22 22:18 | +15 | XRP | DOWN | 0.53 | 0.70 | 1.37 |
| 10-22 22:18 | +10 | XRP | DOWN | 0.53 | 0.64 | 0.75 |
| 10-22 22:18 | +5 | XRP | DOWN | 0.53 | 0.64 | 0.75 |
| 10-22 22:18 | +10 stop | HYPE | DOWN | 0.60 | 0.71 | 0.74 |
| 10-22 22:18 | +20 | HYPE | DOWN | 0.60 | 0.85 | 2.20 |
| 10-22 22:18 | +15 | HYPE | DOWN | 0.60 | 0.85 | 2.20 |
| 10-22 22:18 | +10 | HYPE | DOWN | 0.60 | 0.71 | 0.74 |
| 10-22 22:18 | +5 | HYPE | DOWN | 0.60 | 0.70 | 0.64 |
| 10-22 22:18 | +5 | BNB | DOWN | 0.49 | 0.55 | 0.24 |
| 10-22 22:17 | +10 stop | BNB | DOWN | 0.52 | 0.68 | 1.26 |
| 10-22 22:17 | +20 | BNB | DOWN | 0.52 | 0.75 | 1.98 |
| 10-22 22:17 | +15 | BNB | DOWN | 0.52 | 0.68 | 1.26 |
| 10-22 22:17 | +10 | BNB | DOWN | 0.52 | 0.68 | 1.26 |
| 10-22 22:17 | +5 | BNB | DOWN | 0.52 | 0.58 | 0.24 |
| 10-22 22:17 | +10 stop | DOGE | UP | 0.54 | 0.36 | -2.15 |
| 10-22 22:17 | +20 | DOGE | UP | 0.54 | open |  |
| 10-22 22:17 | +15 | DOGE | UP | 0.54 | open |  |
| 10-22 22:17 | +10 | DOGE | UP | 0.54 | open |  |
| 10-22 22:17 | +5 | DOGE | UP | 0.54 | 0.63 | 0.55 |
| 10-22 22:16 | +10 stop | NEAR | UP | 0.53 | 0.37 | -1.95 |
| 10-22 22:16 | +20 | NEAR | UP | 0.53 | open |  |
| 10-22 22:16 | +15 | NEAR | UP | 0.53 | open |  |
| 10-22 22:16 | +10 | NEAR | UP | 0.53 | open |  |
| 10-22 22:16 | +5 | NEAR | UP | 0.53 | 0.60 | 0.35 |
| 10-22 22:16 | +10 stop | ETH | DOWN | 0.64 | 0.82 | 1.52 |
| 10-22 22:16 | +20 | ETH | DOWN | 0.63 | 0.84 | 1.83 |
| 10-22 22:16 | +15 | ETH | DOWN | 0.64 | 0.82 | 1.52 |
