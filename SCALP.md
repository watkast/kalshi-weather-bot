# Range-Scalp Bot

*Updated Wed Oct 14 03:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15362 | 13300 | 2062 (27) | 0 | $-4886.44 | -5.0% |
| **+10¢** | 11620 | 9228 | 2392 (39) | 2 | $-4546.37 | -6.2% |
| **+15¢** | 9764 | 7200 | 2564 (58) | 2 | $-4052.57 | -6.6% |
| **+20¢** | 8677 | 5995 | 2682 (75) | 4 | $-3559.78 | -6.5% |
| **+10¢ (15¢ stop)** | 18827 | 18777 | 50 (29) | 1 | $-7228.45 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 03:12 | +10 stop | NEAR | DOWN | 0.71 | open |  |
| 10-14 03:12 | +10 | NEAR | DOWN | 0.69 | open |  |
| 10-14 03:12 | +5 | NEAR | DOWN | 0.69 | 0.77 | 0.49 |
| 10-14 03:10 | +10 stop | BTC | UP | 0.70 | 0.82 | 0.94 |
| 10-14 03:10 | +10 | BTC | UP | 0.70 | 0.82 | 0.94 |
| 10-14 03:10 | +5 | BTC | UP | 0.70 | 0.76 | 0.32 |
| 10-14 03:10 | +10 stop | ZEC | DOWN | 0.71 | 0.84 | 1.05 |
| 10-14 03:10 | +10 stop | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 10-14 03:10 | +20 | BNB | DOWN | 0.65 | 0.89 | 2.17 |
| 10-14 03:10 | +15 | BNB | DOWN | 0.65 | 0.82 | 1.43 |
| 10-14 03:10 | +10 | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 10-14 03:10 | +5 | BNB | DOWN | 0.66 | 0.74 | 0.51 |
| 10-14 03:10 | +5 | ETH | DOWN | 0.62 | 0.72 | 0.68 |
| 10-14 03:10 | +10 stop | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 10-14 03:10 | +10 | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 10-14 03:10 | +5 | XRP | DOWN | 0.65 | 0.72 | 0.39 |
| 10-14 03:09 | +10 stop | SOL | DOWN | 0.59 | 0.74 | 1.19 |
| 10-14 03:09 | +10 | SOL | DOWN | 0.59 | 0.74 | 1.19 |
| 10-14 03:09 | +5 | SOL | DOWN | 0.59 | 0.74 | 1.19 |
| 10-14 03:09 | +10 stop | ZEC | DOWN | 0.55 | 0.66 | 0.76 |
| 10-14 03:09 | +10 stop | DOGE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-14 03:09 | +15 | DOGE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-14 03:09 | +5 | DOGE | DOWN | 0.70 | 0.79 | 0.63 |
| 10-14 03:09 | +10 stop | NEAR | DOWN | 0.64 | 0.79 | 1.21 |
| 10-14 03:09 | +5 | NEAR | DOWN | 0.64 | 0.79 | 1.21 |
| 10-14 03:09 | +10 stop | BTC | UP | 0.68 | 0.79 | 0.82 |
| 10-14 03:09 | +20 | BTC | UP | 0.67 | open |  |
| 10-14 03:09 | +15 | BTC | UP | 0.68 | open |  |
| 10-14 03:09 | +10 | BTC | UP | 0.68 | 0.79 | 0.82 |
| 10-14 03:09 | +5 | BTC | UP | 0.68 | 0.77 | 0.61 |
| 10-14 03:09 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-14 03:08 | +10 stop | ZEC | UP | 0.48 | 0.60 | 0.85 |
| 10-14 03:07 | +10 stop | DOGE | UP | 0.54 | 0.64 | 0.65 |
| 10-14 03:07 | +5 | DOGE | UP | 0.57 | 0.64 | 0.35 |
| 10-14 03:07 | +10 stop | ETH | UP | 0.53 | 0.38 | -1.85 |
| 10-14 03:07 | +10 stop | HYPE | DOWN | 0.47 | 0.57 | 0.64 |
| 10-14 03:07 | +5 | HYPE | DOWN | 0.47 | 0.54 | 0.30 |
| 10-14 03:06 | +10 stop | BNB | UP | 0.64 | 0.43 | -2.40 |
| 10-14 03:06 | +5 | BNB | UP | 0.64 | 0.72 | 0.53 |
| 10-14 03:06 | +10 stop | SOL | UP | 0.53 | 0.30 | -2.63 |
