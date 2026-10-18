# Range-Scalp Bot

*Updated Sun Oct 18 09:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22327 | 19433 | 2894 (29) | 0 | $-6520.46 | -4.6% |
| **+10¢** | 16814 | 13469 | 3345 (43) | 0 | $-5809.64 | -5.5% |
| **+15¢** | 14081 | 10472 | 3609 (63) | 0 | $-5316.97 | -6.0% |
| **+20¢** | 12459 | 8679 | 3780 (81) | 0 | $-4766.48 | -6.1% |
| **+10¢ (15¢ stop)** | 27481 | 27431 | 50 (29) | 0 | $-10514.67 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 08:58 | +5 | ETH | DOWN | 0.65 | 0.70 | 0.19 |
| 10-18 08:57 | +10 stop | BTC | UP | 0.67 | 0.79 | 0.92 |
| 10-18 08:55 | +10 stop | ETH | DOWN | 0.67 | 0.34 | -3.62 |
| 10-18 08:55 | +20 | ETH | DOWN | 0.67 | no | 3.14 |
| 10-18 08:55 | +15 | ETH | DOWN | 0.67 | no | 3.14 |
| 10-18 08:55 | +10 | ETH | DOWN | 0.67 | no | 3.14 |
| 10-18 08:55 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 10-18 08:54 | +10 stop | BNB | UP | 0.61 | 0.30 | -3.42 |
| 10-18 08:54 | +10 stop | BTC | DOWN | 0.62 | 0.43 | -2.25 |
| 10-18 08:54 | +20 | BTC | DOWN | 0.62 | yes | -6.37 |
| 10-18 08:54 | +15 | BTC | DOWN | 0.62 | yes | -6.37 |
| 10-18 08:54 | +10 | BTC | DOWN | 0.62 | yes | -6.37 |
| 10-18 08:54 | +5 | BTC | DOWN | 0.62 | yes | -6.37 |
| 10-18 08:53 | +10 stop | BNB | DOWN | 0.68 | 0.46 | -2.58 |
| 10-18 08:53 | +15 | DOGE | UP | 0.67 | 0.82 | 1.23 |
| 10-18 08:53 | +5 | DOGE | UP | 0.67 | 0.82 | 1.23 |
| 10-18 08:53 | +10 stop | HYPE | DOWN | 0.66 | 0.38 | -3.17 |
| 10-18 08:52 | +10 stop | XRP | UP | 0.58 | 0.83 | 2.22 |
| 10-18 08:52 | +10 | DOGE | UP | 0.63 | 0.82 | 1.62 |
| 10-18 08:52 | +5 | DOGE | UP | 0.62 | 0.70 | 0.48 |
| 10-18 08:52 | +10 stop | SOL | UP | 0.56 | 0.76 | 1.69 |
| 10-18 08:52 | +10 stop | DOGE | UP | 0.62 | 0.82 | 1.72 |
| 10-18 08:52 | +5 | SOL | UP | 0.57 | 0.76 | 1.59 |
| 10-18 08:51 | +10 stop | NEAR | UP | 0.71 | 0.84 | 1.05 |
| 10-18 08:51 | +10 stop | XRP | DOWN | 0.68 | 0.42 | -2.94 |
| 10-18 08:51 | +10 | XRP | DOWN | 0.68 | yes | -6.96 |
| 10-18 08:51 | +5 | XRP | DOWN | 0.68 | yes | -6.96 |
| 10-18 08:49 | +10 stop | NEAR | UP | 0.54 | 0.71 | 1.33 |
| 10-18 08:49 | +10 stop | DOGE | DOWN | 0.62 | 0.47 | -1.85 |
| 10-18 08:49 | +10 stop | SOL | DOWN | 0.67 | 0.43 | -2.74 |
| 10-18 08:49 | +10 | SOL | DOWN | 0.67 | yes | -6.86 |
| 10-18 08:48 | +10 stop | BNB | DOWN | 0.60 | 0.45 | -1.85 |
| 10-18 08:48 | +5 | SOL | DOWN | 0.65 | 0.70 | 0.23 |
| 10-18 08:48 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-18 08:48 | +20 | ETH | DOWN | 0.71 | 0.93 | 1.99 |
| 10-18 08:48 | +15 | ETH | DOWN | 0.71 | 0.89 | 1.58 |
| 10-18 08:48 | +10 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-18 08:48 | +5 | ETH | DOWN | 0.71 | 0.80 | 0.63 |
| 10-18 08:48 | +10 stop | HYPE | DOWN | 0.63 | 0.48 | -1.85 |
| 10-18 08:48 | +20 | HYPE | DOWN | 0.63 | yes | -6.47 |
