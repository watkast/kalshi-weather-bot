# Range-Scalp Bot

*Updated Tue Oct 27 08:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36249 | 31651 | 4598 (43) | 0 | $-10030.08 | -4.4% |
| **+10¢** | 27105 | 21787 | 5318 (65) | 0 | $-8853.08 | -5.2% |
| **+15¢** | 22678 | 16967 | 5711 (89) | 1 | $-7814.35 | -5.5% |
| **+20¢** | 20097 | 14113 | 5984 (112) | 1 | $-6853.04 | -5.4% |
| **+10¢ (15¢ stop)** | 44463 | 44400 | 63 (33) | 0 | $-16934.29 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 08:25 | +10 stop | SOL | DOWN | 0.69 | 0.52 | -2.03 |
| 10-27 08:25 | +10 stop | BTC | DOWN | 0.62 | 0.77 | 1.20 |
| 10-27 08:24 | +10 stop | ZEC | DOWN | 0.67 | 0.39 | -3.13 |
| 10-27 08:24 | +10 stop | DOGE | DOWN | 0.56 | 0.70 | 1.07 |
| 10-27 08:24 | +10 stop | SOL | UP | 0.49 | 0.59 | 0.65 |
| 10-27 08:23 | +10 stop | BNB | UP | 0.61 | 0.41 | -2.34 |
| 10-27 08:23 | +10 stop | BTC | UP | 0.57 | 0.40 | -2.05 |
| 10-27 08:23 | +10 stop | ZEC | UP | 0.61 | 0.42 | -2.25 |
| 10-27 08:23 | +10 stop | BNB | DOWN | 0.42 | 0.53 | 0.74 |
| 10-27 08:22 | +10 stop | DOGE | DOWN | 0.66 | 0.46 | -2.34 |
| 10-27 08:22 | +10 | DOGE | DOWN | 0.67 | 0.90 | 2.08 |
| 10-27 08:22 | +5 | DOGE | DOWN | 0.67 | 0.72 | 0.19 |
| 10-27 08:22 | +10 stop | BTC | DOWN | 0.58 | 0.41 | -2.05 |
| 10-27 08:21 | +10 stop | ETH | UP | 0.61 | 0.73 | 0.89 |
| 10-27 08:21 | +10 stop | BNB | DOWN | 0.62 | 0.47 | -1.85 |
| 10-27 08:20 | +10 stop | BTC | DOWN | 0.51 | 0.65 | 1.06 |
| 10-27 08:20 | +10 stop | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 10-27 08:20 | +5 | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 10-27 08:20 | +10 stop | ZEC | DOWN | 0.67 | 0.52 | -1.84 |
| 10-27 08:20 | +10 | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-27 08:20 | +5 | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-27 08:20 | +10 stop | XRP | DOWN | 0.58 | 0.30 | -3.13 |
| 10-27 08:20 | +10 stop | SOL | DOWN | 0.62 | 0.43 | -2.25 |
| 10-27 08:20 | +10 stop | BTC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-27 08:19 | +10 stop | DOGE | DOWN | 0.54 | 0.70 | 1.27 |
| 10-27 08:19 | +15 | XRP | UP | 0.48 | 0.69 | 1.77 |
| 10-27 08:19 | +10 | XRP | UP | 0.48 | 0.69 | 1.77 |
| 10-27 08:19 | +5 | ZEC | DOWN | 0.64 | 0.72 | 0.48 |
| 10-27 08:19 | +10 stop | NEAR | DOWN | 0.62 | 0.80 | 1.51 |
| 10-27 08:19 | +10 | NEAR | DOWN | 0.62 | 0.80 | 1.51 |
| 10-27 08:19 | +5 | NEAR | DOWN | 0.62 | 0.70 | 0.48 |
| 10-27 08:19 | +10 stop | BNB | UP | 0.50 | 0.35 | -1.84 |
| 10-27 08:19 | +10 stop | XRP | UP | 0.64 | 0.47 | -2.05 |
| 10-27 08:19 | +5 | XRP | UP | 0.65 | 0.75 | 0.70 |
| 10-27 08:19 | +10 stop | ETH | UP | 0.69 | 0.44 | -2.83 |
| 10-27 08:19 | +10 stop | DOGE | UP | 0.60 | 0.44 | -1.95 |
| 10-27 08:19 | +10 stop | BTC | UP | 0.66 | 0.40 | -2.93 |
| 10-27 08:19 | +10 stop | HYPE | DOWN | 0.66 | 0.76 | 0.71 |
| 10-27 08:19 | +20 | HYPE | DOWN | 0.66 | 0.87 | 1.86 |
| 10-27 08:19 | +15 | HYPE | DOWN | 0.66 | 0.82 | 1.33 |
