# Range-Scalp Bot

*Updated Thu Oct 15 16:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17821 | 15466 | 2355 (28) | 2 | $-5490.54 | -4.9% |
| **+10¢** | 13457 | 10730 | 2727 (40) | 4 | $-4989.76 | -5.9% |
| **+15¢** | 11289 | 8358 | 2931 (59) | 4 | $-4483.25 | -6.3% |
| **+20¢** | 10037 | 6970 | 3067 (77) | 4 | $-3910.66 | -6.2% |
| **+10¢ (15¢ stop)** | 21952 | 21902 | 50 (29) | 0 | $-8495.28 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 16:42 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-15 16:41 | +10 stop | BTC | DOWN | 0.66 | 0.47 | -2.24 |
| 10-15 16:41 | +5 | BTC | DOWN | 0.66 | 0.72 | 0.29 |
| 10-15 16:40 | +10 stop | BTC | DOWN | 0.53 | 0.64 | 0.75 |
| 10-15 16:40 | +5 | BTC | DOWN | 0.56 | 0.64 | 0.45 |
| 10-15 16:39 | +5 | BTC | UP | 0.41 | 0.60 | 1.56 |
| 10-15 16:39 | +10 stop | ZEC | UP | 0.58 | 0.79 | 1.80 |
| 10-15 16:39 | +10 stop | SOL | UP | 0.51 | 0.63 | 0.85 |
| 10-15 16:39 | +10 stop | ETH | UP | 0.58 | 0.81 | 2.03 |
| 10-15 16:39 | +10 stop | BTC | UP | 0.55 | 0.37 | -2.15 |
| 10-15 16:39 | +10 stop | XRP | UP | 0.66 | 0.78 | 0.91 |
| 10-15 16:39 | +10 stop | NEAR | UP | 0.59 | 0.40 | -2.29 |
| 10-15 16:38 | +5 | BTC | UP | 0.59 | 0.64 | 0.16 |
| 10-15 16:37 | +10 stop | ZEC | DOWN | 0.59 | 0.43 | -1.95 |
| 10-15 16:37 | +10 stop | XRP | UP | 0.68 | 0.53 | -1.84 |
| 10-15 16:37 | +10 stop | NEAR | UP | 0.51 | 0.62 | 0.75 |
| 10-15 16:37 | +5 | XRP | UP | 0.71 | 0.78 | 0.42 |
| 10-15 16:36 | +10 stop | ZEC | UP | 0.58 | 0.39 | -2.25 |
| 10-15 16:36 | +15 | ZEC | UP | 0.58 | 0.79 | 1.80 |
| 10-15 16:36 | +10 | ZEC | UP | 0.58 | 0.79 | 1.80 |
| 10-15 16:36 | +10 stop | ETH | UP | 0.66 | 0.51 | -1.84 |
| 10-15 16:36 | +5 | ETH | UP | 0.66 | 0.81 | 1.23 |
| 10-15 16:36 | +10 stop | BTC | UP | 0.64 | 0.47 | -2.05 |
| 10-15 16:36 | +5 | BTC | UP | 0.64 | 0.69 | 0.18 |
| 10-15 16:36 | +10 stop | SOL | UP | 0.63 | 0.47 | -1.95 |
| 10-15 16:36 | +5 | SOL | UP | 0.63 | 0.68 | 0.17 |
| 10-15 16:35 | +10 stop | BNB | UP | 0.62 | 0.74 | 0.89 |
| 10-15 16:35 | +10 stop | XRP | UP | 0.56 | 0.72 | 1.27 |
| 10-15 16:35 | +5 | XRP | UP | 0.56 | 0.64 | 0.45 |
| 10-15 16:35 | +10 stop | DOGE | UP | 0.68 | 0.82 | 1.14 |
| 10-15 16:35 | +15 | DOGE | UP | 0.67 | 0.82 | 1.23 |
| 10-15 16:35 | +10 | DOGE | UP | 0.67 | 0.82 | 1.23 |
| 10-15 16:35 | +5 | DOGE | UP | 0.67 | 0.74 | 0.40 |
| 10-15 16:35 | +10 stop | ZEC | UP | 0.61 | 0.71 | 0.68 |
| 10-15 16:35 | +10 | ZEC | UP | 0.61 | 0.71 | 0.68 |
| 10-15 16:34 | +10 stop | HYPE | UP | 0.70 | 0.82 | 0.94 |
| 10-15 16:34 | +5 | ETH | DOWN | 0.47 | 0.57 | 0.64 |
| 10-15 16:34 | +5 | BTC | DOWN | 0.52 | 0.60 | 0.45 |
| 10-15 16:33 | +10 stop | SOL | DOWN | 0.71 | 0.54 | -2.03 |
| 10-15 16:33 | +10 | SOL | DOWN | 0.71 | open |  |
