# Range-Scalp Bot

*Updated Tue Oct 27 04:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35983 | 31414 | 4569 (43) | 2 | $-9997.24 | -4.4% |
| **+10¢** | 26901 | 21613 | 5288 (65) | 4 | $-8846.17 | -5.2% |
| **+15¢** | 22507 | 16823 | 5684 (89) | 4 | $-7874.39 | -5.6% |
| **+20¢** | 19950 | 13995 | 5955 (112) | 4 | $-6916.16 | -5.5% |
| **+10¢ (15¢ stop)** | 44124 | 44061 | 63 (33) | 0 | $-16803.49 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 04:24 | +10 stop | XRP | UP | 0.51 | 0.65 | 1.06 |
| 10-27 04:24 | +10 stop | ETH | UP | 0.29 | 0.54 | 2.17 |
| 10-27 04:23 | +10 stop | BNB | DOWN | 0.59 | 0.82 | 2.02 |
| 10-27 04:23 | +10 | BNB | DOWN | 0.59 | 0.82 | 2.02 |
| 10-27 04:23 | +5 | BNB | DOWN | 0.59 | 0.82 | 2.02 |
| 10-27 04:23 | +10 stop | ZEC | UP | 0.68 | 0.47 | -2.44 |
| 10-27 04:23 | +10 stop | HYPE | DOWN | 0.67 | 0.80 | 1.02 |
| 10-27 04:23 | +10 | HYPE | DOWN | 0.67 | 0.80 | 1.02 |
| 10-27 04:23 | +5 | HYPE | DOWN | 0.67 | 0.80 | 1.02 |
| 10-27 04:23 | +10 stop | DOGE | DOWN | 0.63 | 0.79 | 1.31 |
| 10-27 04:23 | +10 | DOGE | DOWN | 0.63 | 0.79 | 1.31 |
| 10-27 04:23 | +5 | DOGE | DOWN | 0.63 | 0.79 | 1.31 |
| 10-27 04:23 | +10 stop | ETH | DOWN | 0.56 | 0.41 | -1.85 |
| 10-27 04:22 | +10 stop | XRP | UP | 0.57 | 0.67 | 0.66 |
| 10-27 04:22 | +10 stop | NEAR | UP | 0.54 | 0.70 | 1.27 |
| 10-27 04:22 | +10 stop | SOL | UP | 0.64 | 0.74 | 0.69 |
| 10-27 04:21 | +10 stop | SOL | UP | 0.56 | 0.66 | 0.66 |
| 10-27 04:21 | +5 | BNB | DOWN | 0.66 | 0.72 | 0.29 |
| 10-27 04:20 | +10 stop | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 10-27 04:20 | +10 stop | XRP | DOWN | 0.56 | 0.33 | -2.64 |
| 10-27 04:20 | +10 stop | HYPE | DOWN | 0.60 | 0.77 | 1.40 |
| 10-27 04:20 | +10 stop | NEAR | DOWN | 0.55 | 0.37 | -2.15 |
| 10-27 04:20 | +10 stop | ZEC | UP | 0.56 | 0.40 | -1.95 |
| 10-27 04:19 | +10 stop | SOL | UP | 0.65 | 0.49 | -1.94 |
| 10-27 04:18 | +10 stop | ZEC | DOWN | 0.55 | 0.37 | -2.15 |
| 10-27 04:18 | +5 | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-27 04:17 | +10 stop | SOL | DOWN | 0.65 | 0.50 | -1.84 |
| 10-27 04:17 | +20 | SOL | DOWN | 0.65 | open |  |
| 10-27 04:17 | +15 | SOL | DOWN | 0.65 | open |  |
| 10-27 04:17 | +10 | SOL | DOWN | 0.65 | open |  |
| 10-27 04:17 | +5 | SOL | DOWN | 0.65 | open |  |
| 10-27 04:16 | +10 stop | HYPE | DOWN | 0.70 | 0.47 | -2.67 |
| 10-27 04:16 | +20 | HYPE | DOWN | 0.70 | 0.90 | 1.78 |
| 10-27 04:16 | +15 | HYPE | DOWN | 0.70 | 0.90 | 1.74 |
| 10-27 04:16 | +10 | HYPE | DOWN | 0.70 | 0.83 | 1.01 |
| 10-27 04:16 | +5 | HYPE | DOWN | 0.70 | 0.77 | 0.38 |
| 10-27 04:16 | +10 stop | BTC | DOWN | 0.69 | 0.54 | -1.83 |
| 10-27 04:16 | +20 | BTC | DOWN | 0.69 | 0.90 | 1.91 |
| 10-27 04:16 | +15 | BTC | DOWN | 0.69 | 0.90 | 1.91 |
| 10-27 04:16 | +10 | BTC | DOWN | 0.69 | 0.90 | 1.91 |
