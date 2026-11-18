# Range-Scalp Bot

*Updated Wed Nov 18 06:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63771 | 55620 | 8151 (119) | 4 | $-17424.15 | -4.3% |
| **+10¢** | 47644 | 38104 | 9540 (160) | 6 | $-16339.21 | -5.5% |
| **+15¢** | 39940 | 29653 | 10287 (205) | 6 | $-14820.96 | -5.9% |
| **+20¢** | 35569 | 24772 | 10797 (260) | 6 | $-13106.11 | -5.9% |
| **+10¢ (15¢ stop)** | 77588 | 77430 | 158 (93) | 0 | $-28527.49 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 06:57 | +10 stop | BTC | UP | 0.69 | 0.53 | -1.93 |
| 11-18 06:56 | +10 stop | DOGE | DOWN | 0.61 | 0.45 | -1.95 |
| 11-18 06:56 | +10 | DOGE | DOWN | 0.61 | 0.94 | 3.13 |
| 11-18 06:56 | +5 | DOGE | DOWN | 0.61 | 0.69 | 0.48 |
| 11-18 06:56 | +10 stop | DOGE | DOWN | 0.58 | 0.69 | 0.77 |
| 11-18 06:56 | +10 | DOGE | DOWN | 0.58 | 0.69 | 0.77 |
| 11-18 06:56 | +5 | DOGE | DOWN | 0.58 | 0.69 | 0.77 |
| 11-18 06:55 | +10 stop | BTC | UP | 0.58 | 0.69 | 0.77 |
| 11-18 06:54 | +10 stop | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-18 06:54 | +10 stop | BNB | DOWN | 0.61 | 0.43 | -2.15 |
| 11-18 06:54 | +10 | BNB | DOWN | 0.62 | open |  |
| 11-18 06:54 | +5 | BNB | DOWN | 0.62 | 0.68 | 0.27 |
| 11-18 06:51 | +10 stop | BNB | DOWN | 0.67 | 0.90 | 2.07 |
| 11-18 06:51 | +10 | BNB | DOWN | 0.67 | 0.90 | 2.07 |
| 11-18 06:51 | +5 | BNB | DOWN | 0.67 | 0.73 | 0.30 |
| 11-18 06:51 | +10 stop | DOGE | DOWN | 0.60 | 0.73 | 0.99 |
| 11-18 06:51 | +10 | DOGE | DOWN | 0.60 | 0.73 | 0.99 |
| 11-18 06:51 | +5 | DOGE | DOWN | 0.60 | 0.67 | 0.37 |
| 11-18 06:50 | +10 stop | ETH | DOWN | 0.69 | 0.82 | 1.04 |
| 11-18 06:50 | +5 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 11-18 06:50 | +10 stop | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 11-18 06:50 | +10 stop | DOGE | UP | 0.50 | 0.68 | 1.46 |
| 11-18 06:50 | +10 | DOGE | UP | 0.51 | 0.68 | 1.36 |
| 11-18 06:50 | +5 | DOGE | UP | 0.52 | 0.68 | 1.26 |
| 11-18 06:50 | +5 | NEAR | DOWN | 0.71 | 0.78 | 0.42 |
| 11-18 06:49 | +10 | HYPE | UP | 0.55 | open |  |
| 11-18 06:49 | +10 stop | BNB | UP | 0.48 | 0.58 | 0.64 |
| 11-18 06:49 | +15 | BNB | UP | 0.48 | 0.74 | 2.28 |
| 11-18 06:49 | +10 | BNB | UP | 0.48 | 0.58 | 0.64 |
| 11-18 06:49 | +5 | BNB | UP | 0.47 | 0.58 | 0.72 |
| 11-18 06:49 | +5 | ETH | UP | 0.55 | 0.60 | 0.15 |
| 11-18 06:48 | +5 | ETH | UP | 0.60 | 0.65 | 0.17 |
| 11-18 06:48 | +10 stop | BTC | UP | 0.70 | 0.51 | -2.23 |
| 11-18 06:48 | +10 | BTC | UP | 0.70 | open |  |
| 11-18 06:48 | +5 | BTC | UP | 0.70 | open |  |
| 11-18 06:48 | +15 | XRP | UP | 0.59 | 0.79 | 1.71 |
| 11-18 06:47 | +10 stop | XRP | UP | 0.66 | 0.51 | -1.84 |
| 11-18 06:47 | +10 | XRP | UP | 0.66 | 0.79 | 1.02 |
| 11-18 06:47 | +5 | ZEC | UP | 0.55 | open |  |
| 11-18 06:47 | +5 | XRP | UP | 0.66 | 0.72 | 0.29 |
