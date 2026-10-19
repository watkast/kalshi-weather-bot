# Range-Scalp Bot

*Updated Mon Oct 19 15:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24162 | 21014 | 3148 (31) | 2 | $-7176.82 | -4.7% |
| **+10¢** | 18172 | 14540 | 3632 (46) | 3 | $-6404.92 | -5.6% |
| **+15¢** | 15228 | 11316 | 3912 (69) | 3 | $-5788.57 | -6.1% |
| **+20¢** | 13479 | 9384 | 4095 (87) | 4 | $-5179.62 | -6.1% |
| **+10¢ (15¢ stop)** | 29751 | 29699 | 52 (30) | 0 | $-11317.03 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 15:11 | +10 stop | SOL | UP | 0.69 | 0.52 | -2.03 |
| 10-19 15:11 | +5 | ETH | DOWN | 0.60 | 0.67 | 0.37 |
| 10-19 15:11 | +10 stop | HYPE | UP | 0.46 | 0.58 | 0.84 |
| 10-19 15:11 | +5 | HYPE | UP | 0.46 | 0.58 | 0.84 |
| 10-19 15:10 | +10 stop | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-19 15:10 | +10 stop | ETH | DOWN | 0.60 | 0.74 | 1.09 |
| 10-19 15:10 | +5 | ETH | DOWN | 0.60 | 0.69 | 0.58 |
| 10-19 15:10 | +10 stop | ETH | UP | 0.51 | 0.66 | 1.16 |
| 10-19 15:10 | +5 | ETH | UP | 0.51 | 0.66 | 1.16 |
| 10-19 15:09 | +10 stop | BTC | UP | 0.68 | 0.48 | -2.34 |
| 10-19 15:09 | +10 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 10-19 15:09 | +5 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 10-19 15:08 | +10 stop | XRP | UP | 0.67 | 0.79 | 0.92 |
| 10-19 15:08 | +5 | ETH | DOWN | 0.51 | 0.56 | 0.14 |
| 10-19 15:08 | +10 stop | DOGE | DOWN | 0.55 | 0.66 | 0.76 |
| 10-19 15:08 | +5 | HYPE | DOWN | 0.59 | 0.66 | 0.37 |
| 10-19 15:08 | +10 stop | BTC | DOWN | 0.59 | 0.44 | -1.85 |
| 10-19 15:08 | +10 stop | HYPE | DOWN | 0.70 | 0.44 | -2.97 |
| 10-19 15:08 | +10 stop | ETH | DOWN | 0.71 | 0.56 | -1.83 |
| 10-19 15:08 | +5 | BTC | DOWN | 0.66 | 0.78 | 0.91 |
| 10-19 15:07 | +5 | BTC | UP | 0.47 | 0.54 | 0.34 |
| 10-19 15:07 | +5 | ZEC | DOWN | 0.68 | 0.77 | 0.61 |
| 10-19 15:07 | +5 | NEAR | DOWN | 0.64 | 0.70 | 0.28 |
| 10-19 15:07 | +10 stop | ETH | DOWN | 0.48 | 0.63 | 1.15 |
| 10-19 15:06 | +10 stop | NEAR | DOWN | 0.71 | 0.55 | -1.93 |
| 10-19 15:06 | +10 stop | SOL | UP | 0.66 | 0.83 | 1.44 |
| 10-19 15:06 | +10 stop | ETH | UP | 0.54 | 0.35 | -2.24 |
| 10-19 15:05 | +5 | BNB | DOWN | 0.66 | 0.74 | 0.50 |
| 10-19 15:05 | +5 | ZEC | DOWN | 0.67 | 0.73 | 0.30 |
| 10-19 15:05 | +10 stop | DOGE | UP | 0.52 | 0.36 | -1.95 |
| 10-19 15:05 | +5 | BTC | UP | 0.51 | 0.56 | 0.14 |
| 10-19 15:05 | +10 stop | SOL | UP | 0.58 | 0.68 | 0.66 |
| 10-19 15:04 | +10 stop | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 10-19 15:03 | +10 stop | BTC | UP | 0.57 | 0.38 | -2.25 |
| 10-19 15:03 | +10 stop | HYPE | UP | 0.54 | 0.38 | -1.99 |
| 10-19 15:03 | +10 stop | BNB | DOWN | 0.62 | 0.74 | 0.85 |
| 10-19 15:03 | +10 stop | DOGE | UP | 0.54 | 0.64 | 0.66 |
| 10-19 15:03 | +5 | BTC | UP | 0.56 | 0.63 | 0.35 |
| 10-19 15:03 | +10 stop | XRP | UP | 0.63 | 0.46 | -2.05 |
| 10-19 15:03 | +10 stop | SOL | UP | 0.53 | 0.65 | 0.86 |
