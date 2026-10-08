# Range-Scalp Bot

*Updated Thu Oct 08 03:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7245 | 6283 | 962 (13) | 2 | $-2212.95 | -4.8% |
| **+10¢** | 5494 | 4361 | 1133 (20) | 3 | $-2161.76 | -6.2% |
| **+15¢** | 4606 | 3410 | 1196 (29) | 3 | $-1800.70 | -6.2% |
| **+20¢** | 4112 | 2869 | 1243 (36) | 3 | $-1439.47 | -5.6% |
| **+10¢ (15¢ stop)** | 8768 | 8746 | 22 (14) | 1 | $-3156.60 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 03:31 | +10 stop | BNB | UP | 0.67 | open |  |
| 10-08 03:31 | +20 | BNB | UP | 0.67 | open |  |
| 10-08 03:31 | +15 | BNB | UP | 0.67 | open |  |
| 10-08 03:31 | +10 | BNB | UP | 0.67 | open |  |
| 10-08 03:31 | +5 | BNB | UP | 0.67 | open |  |
| 10-08 03:30 | +10 stop | SOL | DOWN | 0.49 | 0.29 | -2.33 |
| 10-08 03:30 | +20 | SOL | DOWN | 0.49 | open |  |
| 10-08 03:30 | +15 | SOL | DOWN | 0.49 | open |  |
| 10-08 03:30 | +10 | SOL | DOWN | 0.49 | open |  |
| 10-08 03:30 | +5 | SOL | DOWN | 0.49 | 0.54 | 0.14 |
| 10-08 03:30 | +10 stop | NEAR | DOWN | 0.63 | 0.42 | -2.45 |
| 10-08 03:30 | +20 | NEAR | DOWN | 0.63 | open |  |
| 10-08 03:30 | +15 | NEAR | DOWN | 0.63 | open |  |
| 10-08 03:30 | +10 | NEAR | DOWN | 0.63 | open |  |
| 10-08 03:30 | +5 | NEAR | DOWN | 0.63 | open |  |
| 10-08 03:27 | +10 stop | ZEC | DOWN | 0.65 | 0.82 | 1.44 |
| 10-08 03:26 | +10 stop | XRP | DOWN | 0.47 | 0.64 | 1.35 |
| 10-08 03:26 | +15 | XRP | DOWN | 0.47 | 0.64 | 1.35 |
| 10-08 03:26 | +10 | XRP | DOWN | 0.47 | 0.64 | 1.35 |
| 10-08 03:26 | +5 | XRP | DOWN | 0.47 | 0.64 | 1.35 |
| 10-08 03:26 | +10 stop | DOGE | DOWN | 0.67 | 0.41 | -2.93 |
| 10-08 03:26 | +10 stop | SOL | UP | 0.68 | 0.90 | 1.93 |
| 10-08 03:25 | +5 | BTC | UP | 0.55 | 0.62 | 0.35 |
| 10-08 03:25 | +10 stop | ETH | UP | 0.64 | 0.85 | 1.84 |
| 10-08 03:25 | +10 stop | DOGE | UP | 0.61 | 0.39 | -2.54 |
| 10-08 03:25 | +10 | DOGE | UP | 0.61 | 0.79 | 1.51 |
| 10-08 03:25 | +5 | DOGE | UP | 0.61 | 0.79 | 1.51 |
| 10-08 03:24 | +10 stop | BTC | UP | 0.67 | 0.41 | -2.93 |
| 10-08 03:24 | +20 | BTC | UP | 0.67 | 0.94 | 2.45 |
| 10-08 03:24 | +15 | BTC | UP | 0.67 | 0.86 | 1.65 |
| 10-08 03:24 | +10 | BTC | UP | 0.67 | 0.86 | 1.65 |
| 10-08 03:24 | +5 | BTC | UP | 0.65 | 0.73 | 0.50 |
| 10-08 03:24 | +5 | ETH | UP | 0.66 | 0.72 | 0.29 |
| 10-08 03:24 | +10 stop | ZEC | UP | 0.67 | 0.48 | -2.24 |
| 10-08 03:24 | +20 | ZEC | UP | 0.67 | no | -6.86 |
| 10-08 03:24 | +15 | ZEC | UP | 0.67 | no | -6.86 |
| 10-08 03:24 | +10 | ZEC | UP | 0.67 | no | -6.86 |
| 10-08 03:24 | +5 | ZEC | UP | 0.67 | no | -6.86 |
| 10-08 03:23 | +10 stop | XRP | UP | 0.70 | 0.83 | 1.05 |
| 10-08 03:23 | +10 | XRP | UP | 0.70 | 0.83 | 1.05 |
