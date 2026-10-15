# Range-Scalp Bot

*Updated Thu Oct 15 00:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16814 | 14585 | 2229 (28) | 3 | $-5211.86 | -4.9% |
| **+10¢** | 12707 | 10123 | 2584 (40) | 5 | $-4760.94 | -6.0% |
| **+15¢** | 10671 | 7896 | 2775 (59) | 5 | $-4264.56 | -6.4% |
| **+20¢** | 9480 | 6573 | 2907 (76) | 5 | $-3762.30 | -6.3% |
| **+10¢ (15¢ stop)** | 20699 | 20649 | 50 (29) | 0 | $-7993.41 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 00:38 | +10 stop | SOL | UP | 0.65 | 0.43 | -2.54 |
| 10-15 00:38 | +20 | SOL | UP | 0.65 | open |  |
| 10-15 00:38 | +15 | SOL | UP | 0.65 | open |  |
| 10-15 00:38 | +10 | SOL | UP | 0.65 | open |  |
| 10-15 00:38 | +5 | SOL | UP | 0.65 | open |  |
| 10-15 00:37 | +10 stop | BTC | DOWN | 0.60 | 0.77 | 1.40 |
| 10-15 00:36 | +10 stop | ETH | DOWN | 0.62 | 0.72 | 0.68 |
| 10-15 00:36 | +10 stop | NEAR | UP | 0.65 | 0.47 | -2.14 |
| 10-15 00:36 | +10 stop | ZEC | DOWN | 0.56 | 0.73 | 1.38 |
| 10-15 00:36 | +10 stop | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-15 00:35 | +10 stop | HYPE | DOWN | 0.63 | 0.77 | 1.10 |
| 10-15 00:35 | +20 | HYPE | DOWN | 0.63 | 0.87 | 2.15 |
| 10-15 00:35 | +15 | HYPE | DOWN | 0.63 | 0.87 | 2.15 |
| 10-15 00:35 | +10 | HYPE | DOWN | 0.63 | 0.77 | 1.10 |
| 10-15 00:35 | +5 | HYPE | DOWN | 0.63 | 0.71 | 0.48 |
| 10-15 00:35 | +10 stop | ETH | DOWN | 0.50 | 0.63 | 0.95 |
| 10-15 00:35 | +10 stop | XRP | DOWN | 0.56 | 0.74 | 1.48 |
| 10-15 00:34 | +10 stop | BNB | UP | 0.56 | 0.35 | -2.43 |
| 10-15 00:34 | +10 stop | ZEC | UP | 0.64 | 0.36 | -3.17 |
| 10-15 00:34 | +10 stop | BTC | UP | 0.64 | 0.43 | -2.45 |
| 10-15 00:34 | +10 stop | DOGE | UP | 0.67 | 0.43 | -2.74 |
| 10-15 00:34 | +5 | DOGE | UP | 0.67 | open |  |
| 10-15 00:34 | +10 stop | DOGE | DOWN | 0.42 | 0.54 | 0.84 |
| 10-15 00:34 | +20 | DOGE | DOWN | 0.44 | 0.70 | 2.27 |
| 10-15 00:34 | +15 | DOGE | DOWN | 0.46 | 0.70 | 2.07 |
| 10-15 00:34 | +10 | DOGE | DOWN | 0.48 | 0.70 | 1.87 |
| 10-15 00:34 | +5 | DOGE | DOWN | 0.48 | 0.54 | 0.24 |
| 10-15 00:34 | +5 | SOL | UP | 0.69 | 0.80 | 0.83 |
| 10-15 00:34 | +20 | XRP | DOWN | 0.68 | 0.89 | 1.87 |
| 10-15 00:34 | +15 | XRP | DOWN | 0.68 | 0.85 | 1.45 |
| 10-15 00:34 | +10 | XRP | DOWN | 0.68 | 0.85 | 1.45 |
| 10-15 00:34 | +5 | XRP | DOWN | 0.68 | 0.74 | 0.30 |
| 10-15 00:33 | +10 stop | ETH | DOWN | 0.67 | 0.48 | -2.24 |
| 10-15 00:33 | +5 | ETH | DOWN | 0.67 | 0.72 | 0.19 |
| 10-15 00:33 | +10 stop | SOL | UP | 0.66 | 0.80 | 1.12 |
| 10-15 00:33 | +10 stop | BNB | DOWN | 0.62 | 0.39 | -2.64 |
| 10-15 00:33 | +10 stop | NEAR | DOWN | 0.66 | 0.44 | -2.54 |
| 10-15 00:33 | +10 | NEAR | DOWN | 0.66 | open |  |
| 10-15 00:33 | +5 | NEAR | DOWN | 0.66 | 0.75 | 0.60 |
| 10-15 00:33 | +5 | ZEC | DOWN | 0.63 | 0.73 | 0.69 |
