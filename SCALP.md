# Range-Scalp Bot

*Updated Fri Oct 23 18:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30785 | 26822 | 3963 (39) | 0 | $-8948.38 | -4.6% |
| **+10¢** | 23032 | 18453 | 4579 (56) | 0 | $-7965.95 | -5.5% |
| **+15¢** | 19267 | 14337 | 4930 (79) | 0 | $-7216.87 | -6.0% |
| **+20¢** | 17065 | 11904 | 5161 (102) | 0 | $-6448.46 | -6.0% |
| **+10¢ (15¢ stop)** | 37767 | 37708 | 59 (32) | 0 | $-14380.57 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 18:39 | +10 stop | ETH | DOWN | 0.66 | 0.80 | 1.12 |
| 10-23 18:38 | +5 | SOL | DOWN | 0.67 | 0.72 | 0.19 |
| 10-23 18:38 | +10 stop | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 10-23 18:38 | +5 | NEAR | DOWN | 0.60 | 0.76 | 1.30 |
| 10-23 18:37 | +10 stop | XRP | DOWN | 0.56 | 0.78 | 1.89 |
| 10-23 18:37 | +5 | BNB | DOWN | 0.66 | 0.72 | 0.29 |
| 10-23 18:37 | +10 stop | HYPE | DOWN | 0.62 | 0.83 | 1.83 |
| 10-23 18:36 | +10 stop | NEAR | DOWN | 0.53 | 0.76 | 1.99 |
| 10-23 18:36 | +10 | NEAR | DOWN | 0.53 | 0.76 | 1.99 |
| 10-23 18:36 | +5 | NEAR | DOWN | 0.53 | 0.58 | 0.14 |
| 10-23 18:36 | +5 | DOGE | DOWN | 0.71 | 0.83 | 0.95 |
| 10-23 18:35 | +10 stop | ETH | UP | 0.58 | 0.36 | -2.55 |
| 10-23 18:35 | +5 | BNB | DOWN | 0.59 | 0.67 | 0.47 |
| 10-23 18:35 | +10 stop | DOGE | DOWN | 0.64 | 0.83 | 1.63 |
| 10-23 18:35 | +10 | DOGE | DOWN | 0.64 | 0.83 | 1.63 |
| 10-23 18:35 | +5 | DOGE | DOWN | 0.64 | 0.69 | 0.18 |
| 10-23 18:35 | +5 | BNB | DOWN | 0.55 | 0.64 | 0.55 |
| 10-23 18:35 | +10 stop | NEAR | DOWN | 0.48 | 0.63 | 1.15 |
| 10-23 18:35 | +10 | NEAR | DOWN | 0.46 | 0.63 | 1.35 |
| 10-23 18:35 | +5 | NEAR | DOWN | 0.46 | 0.63 | 1.35 |
| 10-23 18:34 | +10 stop | XRP | DOWN | 0.64 | 0.46 | -2.15 |
| 10-23 18:34 | +5 | XRP | DOWN | 0.64 | 0.78 | 1.10 |
| 10-23 18:34 | +10 stop | HYPE | UP | 0.57 | 0.40 | -2.05 |
| 10-23 18:33 | +10 stop | DOGE | DOWN | 0.59 | 0.72 | 0.98 |
| 10-23 18:33 | +10 | DOGE | DOWN | 0.59 | 0.72 | 0.98 |
| 10-23 18:33 | +5 | DOGE | DOWN | 0.54 | 0.62 | 0.45 |
| 10-23 18:33 | +10 stop | SOL | UP | 0.66 | 0.37 | -3.23 |
| 10-23 18:33 | +10 stop | ZEC | DOWN | 0.62 | 0.73 | 0.79 |
| 10-23 18:33 | +20 | ZEC | DOWN | 0.62 | 0.84 | 1.93 |
| 10-23 18:33 | +15 | ZEC | DOWN | 0.62 | 0.77 | 1.20 |
| 10-23 18:33 | +10 | ZEC | DOWN | 0.62 | 0.73 | 0.79 |
| 10-23 18:33 | +5 | ZEC | DOWN | 0.62 | 0.73 | 0.79 |
| 10-23 18:33 | +5 | XRP | DOWN | 0.46 | 0.54 | 0.44 |
| 10-23 18:33 | +10 stop | XRP | DOWN | 0.63 | 0.46 | -2.05 |
| 10-23 18:33 | +5 | XRP | DOWN | 0.63 | 0.68 | 0.17 |
| 10-23 18:33 | +10 stop | HYPE | DOWN | 0.58 | 0.36 | -2.55 |
| 10-23 18:33 | +10 | HYPE | DOWN | 0.57 | 0.70 | 0.97 |
| 10-23 18:33 | +5 | HYPE | DOWN | 0.57 | 0.65 | 0.46 |
| 10-23 18:32 | +5 | NEAR | DOWN | 0.55 | 0.65 | 0.66 |
| 10-23 18:31 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
