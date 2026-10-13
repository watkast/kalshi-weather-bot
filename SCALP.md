# Range-Scalp Bot

*Updated Tue Oct 13 23:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15113 | 13075 | 2038 (27) | 0 | $-4878.04 | -5.1% |
| **+10¢** | 11427 | 9059 | 2368 (39) | 0 | $-4579.66 | -6.4% |
| **+15¢** | 9606 | 7073 | 2533 (58) | 0 | $-4062.35 | -6.7% |
| **+20¢** | 8541 | 5896 | 2645 (74) | 0 | $-3551.65 | -6.6% |
| **+10¢ (15¢ stop)** | 18532 | 18482 | 50 (29) | 0 | $-7151.84 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 23:00 | +10 stop | BTC | DOWN | 0.65 | 0.82 | 1.43 |
| 10-13 23:00 | +20 | BTC | DOWN | 0.65 | 0.87 | 1.96 |
| 10-13 23:00 | +15 | BTC | DOWN | 0.65 | 0.82 | 1.43 |
| 10-13 23:00 | +10 | BTC | DOWN | 0.65 | 0.82 | 1.43 |
| 10-13 23:00 | +5 | BTC | DOWN | 0.65 | 0.70 | 0.19 |
| 10-13 22:58 | +10 stop | XRP | DOWN | 0.37 | 0.62 | 2.16 |
| 10-13 22:58 | +5 | XRP | DOWN | 0.37 | 0.62 | 2.16 |
| 10-13 22:57 | +10 stop | ETH | UP | 0.47 | 0.64 | 1.35 |
| 10-13 22:57 | +10 stop | NEAR | DOWN | 0.60 | 0.77 | 1.40 |
| 10-13 22:54 | +10 stop | NEAR | UP | 0.56 | 0.41 | -1.85 |
| 10-13 22:54 | +10 stop | ETH | DOWN | 0.51 | 0.35 | -1.94 |
| 10-13 22:54 | +10 stop | BNB | UP | 0.52 | 0.70 | 1.45 |
| 10-13 22:53 | +10 stop | NEAR | DOWN | 0.46 | 0.56 | 0.64 |
| 10-13 22:53 | +10 stop | XRP | DOWN | 0.56 | 0.71 | 1.17 |
| 10-13 22:52 | +10 stop | ETH | UP | 0.65 | 0.47 | -2.14 |
| 10-13 22:51 | +10 stop | XRP | UP | 0.64 | 0.48 | -1.95 |
| 10-13 22:51 | +10 stop | BTC | UP | 0.58 | 0.69 | 0.77 |
| 10-13 22:51 | +10 stop | HYPE | DOWN | 0.57 | 0.69 | 0.87 |
| 10-13 22:51 | +10 | HYPE | DOWN | 0.57 | 0.69 | 0.87 |
| 10-13 22:51 | +5 | HYPE | DOWN | 0.57 | 0.66 | 0.52 |
| 10-13 22:50 | +5 | BTC | UP | 0.69 | 0.74 | 0.21 |
| 10-13 22:50 | +10 stop | NEAR | UP | 0.71 | 0.52 | -2.23 |
| 10-13 22:50 | +10 stop | ETH | UP | 0.58 | 0.71 | 0.97 |
| 10-13 22:50 | +10 stop | XRP | UP | 0.50 | 0.67 | 1.36 |
| 10-13 22:49 | +20 | SOL | UP | 0.68 | 0.91 | 1.99 |
| 10-13 22:49 | +15 | SOL | UP | 0.68 | 0.84 | 1.31 |
| 10-13 22:49 | +5 | SOL | UP | 0.68 | 0.77 | 0.58 |
| 10-13 22:49 | +10 stop | XRP | DOWN | 0.59 | 0.44 | -1.85 |
| 10-13 22:48 | +10 stop | ETH | UP | 0.53 | 0.63 | 0.65 |
| 10-13 22:48 | +10 stop | BTC | UP | 0.55 | 0.68 | 0.96 |
| 10-13 22:48 | +10 stop | SOL | UP | 0.67 | 0.77 | 0.71 |
| 10-13 22:48 | +10 | SOL | UP | 0.67 | 0.77 | 0.71 |
| 10-13 22:48 | +10 stop | ZEC | UP | 0.63 | 0.73 | 0.69 |
| 10-13 22:48 | +20 | ZEC | UP | 0.63 | 0.83 | 1.73 |
| 10-13 22:48 | +15 | ZEC | UP | 0.63 | 0.82 | 1.62 |
| 10-13 22:48 | +10 | ZEC | UP | 0.63 | 0.73 | 0.69 |
| 10-13 22:48 | +5 | ZEC | UP | 0.63 | 0.73 | 0.69 |
| 10-13 22:48 | +5 | BTC | UP | 0.57 | 0.62 | 0.15 |
| 10-13 22:48 | +5 | HYPE | DOWN | 0.67 | 0.75 | 0.50 |
| 10-13 22:47 | +10 stop | BNB | UP | 0.62 | 0.77 | 1.16 |
