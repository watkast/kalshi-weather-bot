# Range-Scalp Bot

*Updated Fri Nov 06 13:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49522 | 43156 | 6366 (76) | 0 | $-14002.20 | -4.5% |
| **+10¢** | 36974 | 29574 | 7400 (101) | 0 | $-12857.99 | -5.5% |
| **+15¢** | 30967 | 22996 | 7971 (130) | 0 | $-11754.11 | -6.0% |
| **+20¢** | 27528 | 19174 | 8354 (171) | 0 | $-10378.08 | -6.0% |
| **+10¢ (15¢ stop)** | 60363 | 60266 | 97 (57) | 0 | $-22342.44 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 13:27 | +10 stop | BNB | UP | 0.66 | 0.44 | -2.54 |
| 11-06 13:26 | +15 | BNB | UP | 0.59 | 0.83 | 2.13 |
| 11-06 13:26 | +10 | BNB | UP | 0.59 | 0.83 | 2.13 |
| 11-06 13:26 | +10 stop | BNB | UP | 0.51 | 0.68 | 1.36 |
| 11-06 13:25 | +10 stop | XRP | UP | 0.70 | 0.92 | 1.90 |
| 11-06 13:25 | +20 | XRP | UP | 0.70 | 0.92 | 1.95 |
| 11-06 13:25 | +15 | XRP | UP | 0.70 | 0.92 | 1.95 |
| 11-06 13:25 | +10 | XRP | UP | 0.70 | 0.92 | 1.95 |
| 11-06 13:25 | +5 | XRP | UP | 0.70 | 0.79 | 0.63 |
| 11-06 13:25 | +10 stop | DOGE | UP | 0.70 | 0.87 | 1.47 |
| 11-06 13:25 | +10 stop | HYPE | UP | 0.63 | 0.79 | 1.31 |
| 11-06 13:25 | +10 stop | BTC | UP | 0.59 | 0.74 | 1.19 |
| 11-06 13:25 | +10 | BTC | UP | 0.59 | 0.74 | 1.19 |
| 11-06 13:25 | +5 | BTC | UP | 0.59 | 0.74 | 1.19 |
| 11-06 13:25 | +10 stop | BNB | UP | 0.50 | 0.60 | 0.65 |
| 11-06 13:25 | +20 | BNB | UP | 0.51 | 0.83 | 2.92 |
| 11-06 13:25 | +15 | BNB | UP | 0.52 | 0.68 | 1.30 |
| 11-06 13:25 | +10 | BNB | UP | 0.52 | 0.68 | 1.30 |
| 11-06 13:25 | +10 stop | ETH | UP | 0.46 | 0.58 | 0.84 |
| 11-06 13:25 | +10 | ETH | UP | 0.46 | 0.58 | 0.84 |
| 11-06 13:25 | +5 | ETH | UP | 0.46 | 0.58 | 0.84 |
| 11-06 13:22 | +10 stop | NEAR | UP | 0.63 | 0.77 | 1.10 |
| 11-06 13:20 | +10 stop | DOGE | UP | 0.64 | 0.74 | 0.69 |
| 11-06 13:20 | +10 stop | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 11-06 13:20 | +10 stop | XRP | UP | 0.59 | 0.69 | 0.68 |
| 11-06 13:19 | +15 | NEAR | DOWN | 0.63 | yes | -6.47 |
| 11-06 13:19 | +5 | NEAR | DOWN | 0.63 | yes | -6.47 |
| 11-06 13:19 | +10 stop | DOGE | DOWN | 0.56 | 0.37 | -2.25 |
| 11-06 13:19 | +10 | DOGE | DOWN | 0.56 | yes | -5.78 |
| 11-06 13:19 | +10 stop | HYPE | DOWN | 0.59 | 0.35 | -2.73 |
| 11-06 13:19 | +10 stop | SOL | UP | 0.60 | 0.73 | 0.99 |
| 11-06 13:19 | +10 | SOL | UP | 0.60 | 0.73 | 0.99 |
| 11-06 13:19 | +5 | SOL | UP | 0.60 | 0.67 | 0.37 |
| 11-06 13:19 | +5 | BTC | UP | 0.58 | 0.66 | 0.46 |
| 11-06 13:19 | +5 | DOGE | DOWN | 0.60 | yes | -6.17 |
| 11-06 13:19 | +10 stop | ZEC | DOWN | 0.59 | 0.39 | -2.34 |
| 11-06 13:19 | +10 stop | ETH | UP | 0.52 | 0.63 | 0.75 |
| 11-06 13:19 | +10 | ETH | UP | 0.51 | 0.61 | 0.65 |
| 11-06 13:19 | +5 | ETH | UP | 0.51 | 0.61 | 0.65 |
| 11-06 13:18 | +10 stop | NEAR | DOWN | 0.54 | 0.36 | -2.15 |
