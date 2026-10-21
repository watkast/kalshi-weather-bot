# Range-Scalp Bot

*Updated Wed Oct 21 12:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27190 | 23677 | 3513 (39) | 2 | $-7903.41 | -4.6% |
| **+10¢** | 20445 | 16386 | 4059 (55) | 4 | $-6988.59 | -5.4% |
| **+15¢** | 17119 | 12749 | 4370 (78) | 3 | $-6267.30 | -5.8% |
| **+20¢** | 15154 | 10575 | 4579 (98) | 4 | $-5624.17 | -5.9% |
| **+10¢ (15¢ stop)** | 33362 | 33303 | 59 (32) | 0 | $-12350.69 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 12:12 | +10 stop | NEAR | UP | 0.64 | 0.91 | 2.46 |
| 10-21 12:12 | +5 | NEAR | UP | 0.64 | 0.91 | 2.46 |
| 10-21 12:10 | +10 | XRP | UP | 0.64 | 0.74 | 0.69 |
| 10-21 12:10 | +5 | XRP | UP | 0.64 | 0.71 | 0.38 |
| 10-21 12:10 | +10 stop | SOL | UP | 0.66 | 0.76 | 0.71 |
| 10-21 12:10 | +10 | SOL | UP | 0.66 | 0.76 | 0.71 |
| 10-21 12:10 | +5 | SOL | UP | 0.66 | 0.76 | 0.71 |
| 10-21 12:10 | +10 stop | ETH | DOWN | 0.67 | 0.52 | -1.84 |
| 10-21 12:09 | +10 stop | DOGE | DOWN | 0.59 | 0.69 | 0.69 |
| 10-21 12:09 | +10 stop | ZEC | DOWN | 0.54 | 0.25 | -3.22 |
| 10-21 12:09 | +15 | ZEC | DOWN | 0.54 | 0.82 | 2.51 |
| 10-21 12:09 | +10 | ZEC | DOWN | 0.54 | 0.82 | 2.51 |
| 10-21 12:09 | +5 | ZEC | DOWN | 0.54 | 0.82 | 2.51 |
| 10-21 12:09 | +10 stop | BTC | UP | 0.71 | 0.89 | 1.58 |
| 10-21 12:09 | +15 | NEAR | DOWN | 0.56 | open |  |
| 10-21 12:09 | +5 | NEAR | DOWN | 0.56 | 0.65 | 0.56 |
| 10-21 12:09 | +10 stop | XRP | UP | 0.69 | 0.93 | 2.19 |
| 10-21 12:08 | +10 stop | ETH | DOWN | 0.66 | 0.50 | -1.94 |
| 10-21 12:08 | +10 stop | SOL | UP | 0.62 | 0.72 | 0.68 |
| 10-21 12:08 | +15 | SOL | UP | 0.62 | 0.79 | 1.41 |
| 10-21 12:08 | +10 | SOL | UP | 0.62 | 0.72 | 0.68 |
| 10-21 12:08 | +5 | SOL | UP | 0.62 | 0.72 | 0.68 |
| 10-21 12:08 | +5 | ZEC | DOWN | 0.70 | 0.75 | 0.21 |
| 10-21 12:07 | +10 stop | DOGE | UP | 0.52 | 0.37 | -1.85 |
| 10-21 12:07 | +10 | DOGE | UP | 0.52 | open |  |
| 10-21 12:07 | +5 | DOGE | UP | 0.52 | open |  |
| 10-21 12:07 | +10 stop | ETH | UP | 0.62 | 0.45 | -2.05 |
| 10-21 12:07 | +10 stop | BTC | UP | 0.67 | 0.50 | -2.04 |
| 10-21 12:07 | +5 | BTC | UP | 0.67 | 0.75 | 0.50 |
| 10-21 12:07 | +10 stop | BNB | DOWN | 0.70 | 0.85 | 1.26 |
| 10-21 12:07 | +20 | BNB | DOWN | 0.70 | 0.92 | 1.94 |
| 10-21 12:07 | +15 | BNB | DOWN | 0.70 | 0.85 | 1.26 |
| 10-21 12:07 | +10 | BNB | DOWN | 0.70 | 0.85 | 1.26 |
| 10-21 12:07 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 10-21 12:07 | +10 stop | XRP | UP | 0.71 | 0.56 | -1.83 |
| 10-21 12:07 | +5 | XRP | UP | 0.71 | 0.76 | 0.22 |
| 10-21 12:07 | +10 stop | DOGE | DOWN | 0.42 | 0.56 | 1.04 |
| 10-21 12:07 | +10 | DOGE | DOWN | 0.41 | 0.56 | 1.15 |
| 10-21 12:07 | +5 | DOGE | DOWN | 0.41 | 0.56 | 1.15 |
| 10-21 12:07 | +10 stop | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
