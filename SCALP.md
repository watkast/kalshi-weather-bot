# Range-Scalp Bot

*Updated Thu Oct 08 16:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7694 | 6668 | 1026 (13) | 3 | $-2392.29 | -4.9% |
| **+10¢** | 5836 | 4622 | 1214 (24) | 3 | $-2345.85 | -6.4% |
| **+15¢** | 4903 | 3628 | 1275 (32) | 4 | $-1909.99 | -6.2% |
| **+20¢** | 4383 | 3060 | 1323 (40) | 4 | $-1497.77 | -5.4% |
| **+10¢ (15¢ stop)** | 9350 | 9321 | 29 (18) | 0 | $-3436.15 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 16:17 | +10 stop | SOL | UP | 0.71 | 0.82 | 0.84 |
| 10-08 16:17 | +5 | ZEC | UP | 0.68 | 0.74 | 0.30 |
| 10-08 16:17 | +10 stop | ZEC | UP | 0.69 | 0.83 | 1.15 |
| 10-08 16:17 | +10 stop | XRP | DOWN | 0.27 | 0.56 | 2.58 |
| 10-08 16:17 | +20 | XRP | DOWN | 0.28 | 0.56 | 2.47 |
| 10-08 16:17 | +15 | XRP | DOWN | 0.30 | 0.56 | 2.27 |
| 10-08 16:17 | +10 | XRP | DOWN | 0.27 | 0.56 | 2.58 |
| 10-08 16:17 | +5 | XRP | DOWN | 0.29 | 0.56 | 2.37 |
| 10-08 16:17 | +10 stop | DOGE | DOWN | 0.28 | 0.55 | 2.37 |
| 10-08 16:17 | +20 | DOGE | DOWN | 0.26 | 0.55 | 2.58 |
| 10-08 16:17 | +15 | DOGE | DOWN | 0.28 | 0.55 | 2.37 |
| 10-08 16:17 | +10 | DOGE | DOWN | 0.28 | 0.55 | 2.37 |
| 10-08 16:17 | +5 | DOGE | DOWN | 0.27 | 0.55 | 2.48 |
| 10-08 16:17 | +5 | HYPE | DOWN | 0.70 | open |  |
| 10-08 16:17 | +10 stop | BTC | DOWN | 0.65 | 0.30 | -3.81 |
| 10-08 16:17 | +20 | BTC | DOWN | 0.65 | open |  |
| 10-08 16:17 | +15 | BTC | DOWN | 0.65 | open |  |
| 10-08 16:17 | +10 | BTC | DOWN | 0.65 | open |  |
| 10-08 16:17 | +5 | BTC | DOWN | 0.65 | open |  |
| 10-08 16:16 | +10 stop | BNB | UP | 0.56 | 0.69 | 0.97 |
| 10-08 16:16 | +20 | BNB | UP | 0.56 | 0.78 | 1.89 |
| 10-08 16:16 | +15 | BNB | UP | 0.56 | 0.78 | 1.85 |
| 10-08 16:16 | +10 | BNB | UP | 0.56 | 0.69 | 0.93 |
| 10-08 16:16 | +5 | BNB | UP | 0.56 | 0.69 | 0.93 |
| 10-08 16:16 | +10 stop | ETH | DOWN | 0.55 | 0.65 | 0.66 |
| 10-08 16:16 | +20 | ETH | DOWN | 0.55 | open |  |
| 10-08 16:16 | +15 | ETH | DOWN | 0.55 | open |  |
| 10-08 16:16 | +10 | ETH | DOWN | 0.55 | 0.65 | 0.66 |
| 10-08 16:16 | +5 | ETH | DOWN | 0.55 | 0.65 | 0.66 |
| 10-08 16:16 | +10 stop | ZEC | UP | 0.59 | 0.41 | -2.14 |
| 10-08 16:16 | +20 | ZEC | UP | 0.59 | 0.83 | 2.13 |
| 10-08 16:16 | +15 | ZEC | UP | 0.59 | 0.74 | 1.19 |
| 10-08 16:16 | +10 | ZEC | UP | 0.59 | 0.72 | 0.98 |
| 10-08 16:16 | +5 | ZEC | UP | 0.59 | 0.65 | 0.27 |
| 10-08 16:16 | +10 stop | NEAR | UP | 0.59 | 0.73 | 1.09 |
| 10-08 16:16 | +20 | NEAR | UP | 0.59 | 0.79 | 1.71 |
| 10-08 16:16 | +15 | NEAR | UP | 0.58 | 0.73 | 1.18 |
| 10-08 16:16 | +10 | NEAR | UP | 0.58 | 0.73 | 1.18 |
| 10-08 16:16 | +5 | NEAR | UP | 0.59 | 0.73 | 1.09 |
| 10-08 16:16 | +10 stop | SOL | DOWN | 0.59 | 0.30 | -3.22 |
