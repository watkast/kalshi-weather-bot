# Range-Scalp Bot

*Updated Sun Nov 01 09:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43420 | 37839 | 5581 (63) | 3 | $-12387.37 | -4.5% |
| **+10¢** | 32391 | 25948 | 6443 (85) | 3 | $-11067.81 | -5.4% |
| **+15¢** | 27108 | 20169 | 6939 (112) | 3 | $-10097.90 | -5.9% |
| **+20¢** | 24074 | 16806 | 7268 (146) | 3 | $-8897.36 | -5.9% |
| **+10¢ (15¢ stop)** | 52956 | 52871 | 85 (50) | 0 | $-19992.31 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 09:21 | +10 stop | BTC | UP | 0.50 | 0.33 | -2.04 |
| 11-01 09:21 | +10 stop | DOGE | DOWN | 0.66 | 0.79 | 1.02 |
| 11-01 09:21 | +15 | DOGE | DOWN | 0.66 | 0.89 | 2.07 |
| 11-01 09:21 | +10 | DOGE | DOWN | 0.66 | 0.79 | 1.02 |
| 11-01 09:21 | +5 | DOGE | DOWN | 0.66 | 0.74 | 0.50 |
| 11-01 09:21 | +10 stop | ETH | DOWN | 0.70 | 0.85 | 1.26 |
| 11-01 09:20 | +10 stop | BTC | DOWN | 0.58 | 0.40 | -2.15 |
| 11-01 09:20 | +10 stop | XRP | DOWN | 0.59 | 0.72 | 0.98 |
| 11-01 09:19 | +10 stop | ETH | DOWN | 0.59 | 0.75 | 1.29 |
| 11-01 09:18 | +10 stop | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-01 09:18 | +20 | DOGE | DOWN | 0.62 | 0.89 | 2.46 |
| 11-01 09:18 | +15 | DOGE | DOWN | 0.62 | 0.77 | 1.20 |
| 11-01 09:18 | +10 | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-01 09:18 | +5 | DOGE | DOWN | 0.61 | 0.72 | 0.78 |
| 11-01 09:18 | +10 stop | BNB | DOWN | 0.65 | 0.79 | 1.12 |
| 11-01 09:17 | +10 stop | BTC | UP | 0.57 | 0.41 | -1.95 |
| 11-01 09:17 | +10 stop | ETH | UP | 0.57 | 0.42 | -1.86 |
| 11-01 09:17 | +20 | ETH | UP | 0.57 | open |  |
| 11-01 09:17 | +15 | ETH | UP | 0.57 | open |  |
| 11-01 09:17 | +10 | ETH | UP | 0.57 | open |  |
| 11-01 09:17 | +5 | ETH | UP | 0.57 | open |  |
| 11-01 09:17 | +10 stop | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-01 09:17 | +20 | ZEC | DOWN | 0.67 | 0.87 | 1.76 |
| 11-01 09:17 | +15 | ZEC | DOWN | 0.67 | 0.85 | 1.55 |
| 11-01 09:17 | +10 | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-01 09:17 | +5 | ZEC | DOWN | 0.67 | 0.74 | 0.40 |
| 11-01 09:17 | +10 stop | XRP | DOWN | 0.60 | 0.43 | -2.05 |
| 11-01 09:17 | +20 | XRP | DOWN | 0.60 | 0.80 | 1.71 |
| 11-01 09:17 | +15 | XRP | DOWN | 0.60 | 0.80 | 1.71 |
| 11-01 09:17 | +10 | XRP | DOWN | 0.60 | 0.72 | 0.88 |
| 11-01 09:17 | +5 | XRP | DOWN | 0.60 | 0.68 | 0.47 |
| 11-01 09:17 | +10 stop | SOL | DOWN | 0.56 | 0.76 | 1.69 |
| 11-01 09:17 | +20 | SOL | DOWN | 0.55 | 0.76 | 1.79 |
| 11-01 09:17 | +15 | SOL | DOWN | 0.55 | 0.76 | 1.79 |
| 11-01 09:17 | +10 | SOL | DOWN | 0.55 | 0.76 | 1.79 |
| 11-01 09:17 | +5 | SOL | DOWN | 0.55 | 0.60 | 0.15 |
| 11-01 09:16 | +5 | NEAR | UP | 0.58 | open |  |
| 11-01 09:16 | +10 stop | BNB | UP | 0.58 | 0.42 | -1.96 |
| 11-01 09:16 | +20 | BNB | UP | 0.58 | open |  |
| 11-01 09:16 | +15 | BNB | UP | 0.58 | open |  |
