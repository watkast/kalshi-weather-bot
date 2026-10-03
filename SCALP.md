# Range-Scalp Bot

*Updated Sat Oct 03 11:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 696 | 602 | 94 (1) | 1 | $-227.04 | -5.1% |
| **+10¢** | 532 | 428 | 104 (2) | 1 | $-170.19 | -5.1% |
| **+15¢** | 453 | 342 | 111 (3) | 1 | $-149.45 | -5.3% |
| **+20¢** | 393 | 279 | 114 (3) | 2 | $-130.72 | -5.3% |
| **+10¢ (15¢ stop)** | 903 | 902 | 1 (1) | 1 | $-483.47 | -8.5% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 11:36 | +10 stop | BTC | UP | 0.66 | open |  |
| 10-03 11:36 | +15 | BTC | UP | 0.66 | open |  |
| 10-03 11:36 | +10 | BTC | UP | 0.66 | open |  |
| 10-03 11:36 | +5 | BTC | UP | 0.66 | open |  |
| 10-03 11:35 | +10 stop | BNB | UP | 0.56 | 0.40 | -1.95 |
| 10-03 11:34 | +10 stop | BNB | DOWN | 0.61 | 0.45 | -2.00 |
| 10-03 11:34 | +20 | BNB | DOWN | 0.64 | open |  |
| 10-03 11:34 | +15 | BNB | DOWN | 0.63 | 0.80 | 1.39 |
| 10-03 11:34 | +10 | BNB | DOWN | 0.63 | 0.80 | 1.39 |
| 10-03 11:34 | +5 | BNB | DOWN | 0.63 | 0.80 | 1.39 |
| 10-03 11:34 | +10 stop | BTC | UP | 0.57 | 0.70 | 0.97 |
| 10-03 11:34 | +20 | BTC | UP | 0.57 | open |  |
| 10-03 11:34 | +15 | BTC | UP | 0.57 | 0.73 | 1.28 |
| 10-03 11:34 | +10 | BTC | UP | 0.57 | 0.70 | 0.97 |
| 10-03 11:34 | +5 | BTC | UP | 0.57 | 0.70 | 0.97 |
| 10-03 11:34 | +10 stop | SOL | DOWN | 0.63 | 0.41 | -2.54 |
| 10-03 11:32 | +10 stop | HYPE | UP | 0.65 | 0.80 | 1.22 |
| 10-03 11:32 | +20 | HYPE | UP | 0.65 | 0.85 | 1.75 |
| 10-03 11:32 | +15 | HYPE | UP | 0.65 | 0.80 | 1.22 |
| 10-03 11:32 | +10 | HYPE | UP | 0.65 | 0.80 | 1.22 |
| 10-03 11:32 | +5 | HYPE | UP | 0.65 | 0.72 | 0.39 |
| 10-03 11:31 | +10 stop | SOL | UP | 0.57 | 0.41 | -1.95 |
| 10-03 11:31 | +20 | SOL | UP | 0.57 | 0.83 | 2.32 |
| 10-03 11:31 | +15 | SOL | UP | 0.57 | 0.74 | 1.38 |
| 10-03 11:31 | +10 | SOL | UP | 0.57 | 0.74 | 1.38 |
| 10-03 11:31 | +5 | SOL | UP | 0.57 | 0.64 | 0.35 |
| 10-03 11:31 | +10 stop | DOGE | UP | 0.70 | 0.81 | 0.84 |
| 10-03 11:31 | +20 | DOGE | UP | 0.70 | 0.93 | 2.13 |
| 10-03 11:31 | +15 | DOGE | UP | 0.70 | 0.88 | 1.57 |
| 10-03 11:31 | +10 | DOGE | UP | 0.70 | 0.81 | 0.84 |
| 10-03 11:31 | +5 | DOGE | UP | 0.70 | 0.76 | 0.32 |
| 10-03 11:31 | +10 stop | ETH | UP | 0.62 | 0.72 | 0.68 |
| 10-03 11:31 | +20 | ETH | UP | 0.62 | 0.84 | 1.93 |
| 10-03 11:31 | +15 | ETH | UP | 0.62 | 0.79 | 1.41 |
| 10-03 11:31 | +10 | ETH | UP | 0.62 | 0.72 | 0.68 |
| 10-03 11:31 | +5 | ETH | UP | 0.62 | 0.71 | 0.58 |
| 10-03 11:31 | +10 stop | NEAR | UP | 0.69 | 0.84 | 1.25 |
| 10-03 11:31 | +20 | NEAR | UP | 0.69 | 0.89 | 1.78 |
| 10-03 11:31 | +15 | NEAR | UP | 0.69 | 0.84 | 1.25 |
| 10-03 11:31 | +10 | NEAR | UP | 0.69 | 0.84 | 1.25 |
