# Range-Scalp Bot

*Updated Mon Nov 09 03:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53245 | 46425 | 6820 (85) | 0 | $-14714.53 | -4.4% |
| **+10¢** | 39764 | 31809 | 7955 (110) | 0 | $-13714.28 | -5.5% |
| **+15¢** | 33318 | 24747 | 8571 (141) | 0 | $-12527.30 | -6.0% |
| **+20¢** | 29639 | 20652 | 8987 (186) | 0 | $-11035.47 | -5.9% |
| **+10¢ (15¢ stop)** | 64873 | 64767 | 106 (63) | 0 | $-24072.66 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 03:41 | +10 stop | SOL | DOWN | 0.69 | 0.24 | -4.78 |
| 11-09 03:41 | +10 stop | BTC | DOWN | 0.59 | 0.42 | -2.05 |
| 11-09 03:40 | +10 stop | ZEC | DOWN | 0.58 | 0.31 | -3.03 |
| 11-09 03:38 | +10 stop | BNB | DOWN | 0.70 | 0.52 | -2.13 |
| 11-09 03:38 | +10 stop | ZEC | UP | 0.62 | 0.46 | -1.95 |
| 11-09 03:38 | +20 | ZEC | UP | 0.62 | 0.88 | 2.35 |
| 11-09 03:38 | +15 | ZEC | UP | 0.62 | 0.79 | 1.41 |
| 11-09 03:38 | +10 | ZEC | UP | 0.62 | 0.79 | 1.41 |
| 11-09 03:38 | +5 | ZEC | UP | 0.62 | 0.68 | 0.27 |
| 11-09 03:38 | +10 stop | SOL | DOWN | 0.69 | 0.80 | 0.83 |
| 11-09 03:37 | +10 stop | NEAR | DOWN | 0.66 | 0.76 | 0.71 |
| 11-09 03:37 | +5 | NEAR | DOWN | 0.67 | 0.76 | 0.61 |
| 11-09 03:37 | +10 stop | DOGE | UP | 0.56 | 0.40 | -1.95 |
| 11-09 03:37 | +15 | DOGE | UP | 0.56 | 0.72 | 1.27 |
| 11-09 03:37 | +10 | DOGE | UP | 0.56 | 0.70 | 1.07 |
| 11-09 03:37 | +5 | DOGE | UP | 0.56 | 0.70 | 1.07 |
| 11-09 03:37 | +5 | BNB | UP | 0.60 | 0.71 | 0.81 |
| 11-09 03:37 | +10 stop | SOL | UP | 0.57 | 0.42 | -1.86 |
| 11-09 03:37 | +10 | SOL | UP | 0.57 | 0.75 | 1.48 |
| 11-09 03:37 | +5 | SOL | UP | 0.57 | 0.75 | 1.48 |
| 11-09 03:35 | +10 stop | BNB | UP | 0.66 | 0.48 | -2.14 |
| 11-09 03:35 | +10 | BNB | UP | 0.66 | 0.84 | 1.54 |
| 11-09 03:35 | +5 | BNB | UP | 0.66 | 0.74 | 0.50 |
| 11-09 03:35 | +10 stop | HYPE | DOWN | 0.67 | 0.79 | 0.92 |
| 11-09 03:35 | +10 | HYPE | DOWN | 0.67 | 0.79 | 0.92 |
| 11-09 03:35 | +10 stop | SOL | UP | 0.60 | 0.73 | 0.99 |
| 11-09 03:35 | +10 | SOL | UP | 0.60 | 0.73 | 0.99 |
| 11-09 03:35 | +5 | SOL | UP | 0.61 | 0.73 | 0.89 |
| 11-09 03:35 | +10 stop | BTC | DOWN | 0.58 | 0.69 | 0.77 |
| 11-09 03:35 | +10 stop | NEAR | UP | 0.69 | 0.51 | -2.13 |
| 11-09 03:35 | +10 | NEAR | UP | 0.69 | 0.88 | 1.67 |
| 11-09 03:35 | +5 | NEAR | UP | 0.69 | 0.74 | 0.21 |
| 11-09 03:34 | +10 stop | ETH | UP | 0.53 | 0.32 | -2.44 |
| 11-09 03:34 | +10 | ETH | UP | 0.53 | 0.82 | 2.61 |
| 11-09 03:34 | +5 | ETH | UP | 0.65 | 0.82 | 1.43 |
| 11-09 03:33 | +10 stop | BTC | DOWN | 0.56 | 0.66 | 0.66 |
| 11-09 03:33 | +10 stop | HYPE | DOWN | 0.52 | 0.37 | -1.85 |
| 11-09 03:33 | +15 | HYPE | DOWN | 0.52 | 0.72 | 1.67 |
| 11-09 03:33 | +10 | HYPE | DOWN | 0.52 | 0.66 | 1.06 |
| 11-09 03:33 | +10 stop | DOGE | UP | 0.69 | 0.80 | 0.83 |
