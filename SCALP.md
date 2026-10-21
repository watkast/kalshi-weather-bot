# Range-Scalp Bot

*Updated Wed Oct 21 12:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27241 | 23725 | 3516 (39) | 2 | $-7899.50 | -4.6% |
| **+10¢** | 20480 | 16415 | 4065 (55) | 1 | $-6989.46 | -5.4% |
| **+15¢** | 17148 | 12774 | 4374 (78) | 1 | $-6246.90 | -5.8% |
| **+20¢** | 15179 | 10594 | 4585 (98) | 1 | $-5616.57 | -5.9% |
| **+10¢ (15¢ stop)** | 33428 | 33369 | 59 (32) | 0 | $-12400.04 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 12:42 | +10 stop | ETH | DOWN | 0.69 | 0.83 | 1.15 |
| 10-21 12:42 | +10 stop | BNB | UP | 0.56 | 0.25 | -3.42 |
| 10-21 12:42 | +5 | BNB | UP | 0.58 | 0.65 | 0.36 |
| 10-21 12:42 | +10 stop | ETH | UP | 0.37 | 0.60 | 1.96 |
| 10-21 12:40 | +10 stop | BNB | UP | 0.58 | 0.74 | 1.28 |
| 10-21 12:40 | +5 | BNB | UP | 0.58 | 0.74 | 1.28 |
| 10-21 12:40 | +10 stop | ETH | UP | 0.51 | 0.76 | 2.19 |
| 10-21 12:40 | +10 stop | XRP | UP | 0.53 | 0.37 | -1.95 |
| 10-21 12:39 | +5 | DOGE | DOWN | 0.52 | 0.57 | 0.14 |
| 10-21 12:39 | +10 stop | NEAR | UP | 0.56 | 0.31 | -2.83 |
| 10-21 12:38 | +10 stop | XRP | DOWN | 0.55 | 0.37 | -2.15 |
| 10-21 12:38 | +15 | XRP | DOWN | 0.55 | 0.74 | 1.58 |
| 10-21 12:38 | +10 | XRP | DOWN | 0.55 | 0.74 | 1.58 |
| 10-21 12:38 | +5 | XRP | DOWN | 0.56 | 0.61 | 0.15 |
| 10-21 12:38 | +5 | BNB | UP | 0.62 | 0.71 | 0.60 |
| 10-21 12:38 | +10 stop | BNB | UP | 0.61 | 0.71 | 0.68 |
| 10-21 12:38 | +5 | SOL | DOWN | 0.56 | 0.61 | 0.15 |
| 10-21 12:38 | +10 stop | ZEC | UP | 0.64 | 0.43 | -2.45 |
| 10-21 12:38 | +10 stop | SOL | DOWN | 0.51 | 0.61 | 0.65 |
| 10-21 12:38 | +15 | SOL | DOWN | 0.51 | 0.82 | 2.81 |
| 10-21 12:38 | +10 | SOL | DOWN | 0.51 | 0.61 | 0.65 |
| 10-21 12:38 | +5 | SOL | DOWN | 0.51 | 0.57 | 0.24 |
| 10-21 12:38 | +10 stop | DOGE | DOWN | 0.56 | 0.71 | 1.17 |
| 10-21 12:38 | +15 | DOGE | DOWN | 0.56 | 0.71 | 1.17 |
| 10-21 12:38 | +10 | DOGE | DOWN | 0.56 | 0.71 | 1.17 |
| 10-21 12:38 | +5 | DOGE | DOWN | 0.56 | 0.64 | 0.45 |
| 10-21 12:38 | +10 stop | BTC | DOWN | 0.48 | 0.58 | 0.64 |
| 10-21 12:38 | +20 | BTC | DOWN | 0.50 | 0.87 | 3.44 |
| 10-21 12:38 | +15 | BTC | DOWN | 0.58 | 0.87 | 2.64 |
| 10-21 12:38 | +10 | BTC | DOWN | 0.58 | 0.87 | 2.64 |
| 10-21 12:38 | +5 | BTC | DOWN | 0.58 | 0.63 | 0.15 |
| 10-21 12:38 | +10 stop | NEAR | DOWN | 0.67 | 0.34 | -3.62 |
| 10-21 12:38 | +20 | NEAR | DOWN | 0.67 | 0.88 | 1.86 |
| 10-21 12:38 | +15 | NEAR | DOWN | 0.67 | 0.88 | 1.86 |
| 10-21 12:38 | +10 | NEAR | DOWN | 0.67 | 0.80 | 1.02 |
| 10-21 12:38 | +5 | NEAR | DOWN | 0.67 | 0.76 | 0.61 |
| 10-21 12:38 | +10 stop | ETH | DOWN | 0.55 | 0.40 | -1.85 |
| 10-21 12:38 | +15 | ETH | DOWN | 0.55 | 0.83 | 2.52 |
| 10-21 12:38 | +10 | ETH | DOWN | 0.55 | 0.83 | 2.52 |
| 10-21 12:38 | +5 | ETH | DOWN | 0.55 | 0.63 | 0.45 |
