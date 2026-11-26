# Range-Scalp Bot

*Updated Thu Nov 26 22:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73008 | 63722 | 9286 (158) | 0 | $-19460.78 | -4.2% |
| **+10¢** | 54426 | 43586 | 10840 (203) | 0 | $-18048.27 | -5.3% |
| **+15¢** | 45581 | 33903 | 11678 (261) | 0 | $-16140.39 | -5.6% |
| **+20¢** | 40562 | 28267 | 12295 (327) | 0 | $-14524.56 | -5.7% |
| **+10¢ (15¢ stop)** | 88898 | 88689 | 209 (128) | 0 | $-32779.21 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 22:43 | +10 stop | SOL | DOWN | 0.69 | 0.95 | 2.44 |
| 11-26 22:43 | +20 | SOL | DOWN | 0.69 | 0.95 | 2.44 |
| 11-26 22:43 | +15 | SOL | DOWN | 0.69 | 0.95 | 2.44 |
| 11-26 22:43 | +10 | SOL | DOWN | 0.69 | 0.95 | 2.44 |
| 11-26 22:43 | +5 | SOL | DOWN | 0.69 | 0.95 | 2.44 |
| 11-26 22:41 | +5 | ZEC | DOWN | 0.67 | yes | -6.81 |
| 11-26 22:41 | +10 stop | ZEC | DOWN | 0.68 | 0.52 | -1.94 |
| 11-26 22:39 | +10 stop | ZEC | DOWN | 0.59 | 0.41 | -2.14 |
| 11-26 22:39 | +15 | ZEC | DOWN | 0.59 | yes | -6.07 |
| 11-26 22:39 | +5 | ZEC | DOWN | 0.59 | 0.68 | 0.57 |
| 11-26 22:37 | +10 stop | HYPE | UP | 0.50 | 0.21 | -3.20 |
| 11-26 22:35 | +10 stop | ZEC | DOWN | 0.67 | 0.82 | 1.23 |
| 11-26 22:35 | +20 | ZEC | DOWN | 0.67 | yes | -6.86 |
| 11-26 22:35 | +15 | ZEC | DOWN | 0.67 | 0.82 | 1.23 |
| 11-26 22:35 | +5 | ZEC | DOWN | 0.67 | 0.75 | 0.50 |
| 11-26 22:33 | +5 | ZEC | DOWN | 0.67 | 0.73 | 0.30 |
| 11-26 22:33 | +10 stop | HYPE | DOWN | 0.62 | 0.43 | -2.25 |
| 11-26 22:33 | +5 | NEAR | DOWN | 0.71 | 0.77 | 0.32 |
| 11-26 22:32 | +5 | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 11-26 22:32 | +10 stop | BTC | DOWN | 0.63 | 0.77 | 1.10 |
| 11-26 22:32 | +10 | BTC | DOWN | 0.63 | 0.77 | 1.10 |
| 11-26 22:32 | +5 | BTC | DOWN | 0.63 | 0.72 | 0.58 |
| 11-26 22:32 | +10 stop | SOL | DOWN | 0.58 | 0.69 | 0.77 |
| 11-26 22:32 | +20 | SOL | DOWN | 0.57 | 0.81 | 2.11 |
| 11-26 22:32 | +15 | SOL | DOWN | 0.57 | 0.73 | 1.28 |
| 11-26 22:32 | +10 | SOL | DOWN | 0.57 | 0.69 | 0.87 |
| 11-26 22:32 | +5 | SOL | DOWN | 0.57 | 0.64 | 0.35 |
| 11-26 22:31 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-26 22:31 | +20 | ETH | DOWN | 0.65 | 0.85 | 1.75 |
| 11-26 22:31 | +15 | ETH | DOWN | 0.65 | 0.80 | 1.22 |
| 11-26 22:31 | +10 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-26 22:31 | +5 | ETH | DOWN | 0.66 | 0.72 | 0.29 |
| 11-26 22:31 | +10 stop | XRP | DOWN | 0.69 | 0.80 | 0.83 |
| 11-26 22:31 | +20 | XRP | DOWN | 0.69 | 0.89 | 1.78 |
| 11-26 22:31 | +15 | XRP | DOWN | 0.69 | 0.87 | 1.57 |
| 11-26 22:31 | +10 | XRP | DOWN | 0.69 | 0.80 | 0.83 |
| 11-26 22:31 | +5 | XRP | DOWN | 0.69 | 0.80 | 0.83 |
| 11-26 22:31 | +10 stop | ZEC | UP | 0.51 | 0.33 | -2.14 |
| 11-26 22:31 | +10 | ZEC | UP | 0.51 | 0.61 | 0.65 |
| 11-26 22:31 | +5 | ZEC | UP | 0.51 | 0.56 | 0.14 |
