# Range-Scalp Bot

*Updated Sun Oct 04 07:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 1909 | 1645 | 264 (3) | 2 | $-644.46 | -5.3% |
| **+10¢** | 1480 | 1187 | 293 (4) | 2 | $-472.70 | -5.1% |
| **+15¢** | 1248 | 937 | 311 (5) | 2 | $-407.10 | -5.2% |
| **+20¢** | 1102 | 773 | 329 (7) | 2 | $-389.20 | -5.6% |
| **+10¢ (15¢ stop)** | 2398 | 2397 | 1 (1) | 0 | $-969.77 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 06:52 | +10 stop | HYPE | UP | 0.67 | 0.84 | 1.44 |
| 10-04 06:51 | +10 stop | ZEC | DOWN | 0.47 | 0.29 | -2.13 |
| 10-04 06:48 | +10 stop | SOL | UP | 0.66 | 0.78 | 0.91 |
| 10-04 06:48 | +5 | HYPE | DOWN | 0.68 | 0.80 | 0.92 |
| 10-04 06:47 | +10 stop | NEAR | UP | 0.68 | 0.78 | 0.72 |
| 10-04 06:47 | +5 | NEAR | UP | 0.68 | 0.75 | 0.41 |
| 10-04 06:47 | +10 stop | ZEC | DOWN | 0.66 | 0.50 | -1.90 |
| 10-04 06:47 | +10 stop | ETH | UP | 0.68 | 0.79 | 0.82 |
| 10-04 06:47 | +20 | ETH | UP | 0.68 | 0.89 | 1.87 |
| 10-04 06:47 | +15 | ETH | UP | 0.68 | 0.86 | 1.55 |
| 10-04 06:47 | +10 | ETH | UP | 0.68 | 0.79 | 0.82 |
| 10-04 06:47 | +5 | ETH | UP | 0.68 | 0.74 | 0.30 |
| 10-04 06:46 | +10 stop | SOL | DOWN | 0.51 | 0.35 | -1.89 |
| 10-04 06:46 | +10 stop | XRP | UP | 0.69 | 0.80 | 0.83 |
| 10-04 06:46 | +5 | BNB | UP | 0.71 | 0.78 | 0.42 |
| 10-04 06:46 | +10 stop | NEAR | UP | 0.67 | 0.52 | -1.84 |
| 10-04 06:46 | +20 | NEAR | UP | 0.67 | 0.88 | 1.86 |
| 10-04 06:46 | +15 | NEAR | UP | 0.67 | 0.82 | 1.23 |
| 10-04 06:46 | +10 | NEAR | UP | 0.65 | 0.75 | 0.70 |
| 10-04 06:46 | +5 | NEAR | UP | 0.65 | 0.70 | 0.19 |
| 10-04 06:46 | +10 stop | DOGE | UP | 0.66 | 0.77 | 0.82 |
| 10-04 06:46 | +20 | DOGE | UP | 0.66 | 0.88 | 1.97 |
| 10-04 06:46 | +15 | DOGE | UP | 0.61 | 0.77 | 1.30 |
| 10-04 06:46 | +10 | DOGE | UP | 0.61 | 0.71 | 0.68 |
| 10-04 06:46 | +5 | DOGE | UP | 0.61 | 0.71 | 0.68 |
| 10-04 06:46 | +10 | ZEC | DOWN | 0.62 | 0.79 | 1.41 |
| 10-04 06:46 | +10 stop | ZEC | DOWN | 0.69 | 0.52 | -2.03 |
| 10-04 06:46 | +20 | ZEC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-04 06:46 | +15 | ZEC | DOWN | 0.71 | 0.89 | 1.61 |
| 10-04 06:46 | +5 | ZEC | DOWN | 0.71 | 0.79 | 0.56 |
| 10-04 06:46 | +10 stop | BTC | UP | 0.57 | 0.73 | 1.28 |
| 10-04 06:46 | +20 | BTC | UP | 0.57 | 0.77 | 1.69 |
| 10-04 06:46 | +15 | BTC | UP | 0.57 | 0.73 | 1.28 |
| 10-04 06:46 | +10 | BTC | UP | 0.57 | 0.73 | 1.28 |
| 10-04 06:46 | +5 | BTC | UP | 0.57 | 0.73 | 1.28 |
| 10-04 06:45 | +10 stop | HYPE | DOWN | 0.66 | 0.39 | -2.98 |
| 10-04 06:45 | +20 | HYPE | DOWN | 0.66 | 0.88 | 2.00 |
| 10-04 06:45 | +15 | HYPE | DOWN | 0.66 | 0.88 | 2.00 |
| 10-04 06:45 | +10 | HYPE | DOWN | 0.66 | 0.80 | 1.17 |
| 10-04 06:45 | +5 | HYPE | DOWN | 0.66 | 0.72 | 0.33 |
