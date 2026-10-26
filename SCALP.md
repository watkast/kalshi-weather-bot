# Range-Scalp Bot

*Updated Mon Oct 26 22:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35531 | 31004 | 4527 (43) | 0 | $-9973.64 | -4.5% |
| **+10¢** | 26570 | 21335 | 5235 (65) | 0 | $-8808.79 | -5.3% |
| **+15¢** | 22234 | 16604 | 5630 (89) | 1 | $-7883.16 | -5.6% |
| **+20¢** | 19715 | 13814 | 5901 (112) | 1 | $-6951.52 | -5.6% |
| **+10¢ (15¢ stop)** | 43565 | 43503 | 62 (33) | 0 | $-16600.41 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 22:30 | +10 stop | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 10-26 22:30 | +20 | BNB | DOWN | 0.66 | open |  |
| 10-26 22:30 | +15 | BNB | DOWN | 0.66 | open |  |
| 10-26 22:30 | +10 | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 10-26 22:30 | +5 | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 10-26 22:29 | +10 stop | ZEC | UP | 0.51 | 0.72 | 1.77 |
| 10-26 22:29 | +20 | ZEC | UP | 0.51 | 0.72 | 1.77 |
| 10-26 22:29 | +15 | ZEC | UP | 0.51 | 0.72 | 1.77 |
| 10-26 22:29 | +10 | ZEC | UP | 0.53 | 0.72 | 1.57 |
| 10-26 22:29 | +5 | ZEC | UP | 0.51 | 0.56 | 0.14 |
| 10-26 22:27 | +10 stop | BTC | UP | 0.57 | 0.11 | -4.85 |
| 10-26 22:27 | +10 | XRP | DOWN | 0.59 | 0.87 | 2.55 |
| 10-26 22:27 | +5 | XRP | DOWN | 0.59 | 0.87 | 2.55 |
| 10-26 22:26 | +10 stop | XRP | DOWN | 0.69 | 0.87 | 1.57 |
| 10-26 22:26 | +10 stop | SOL | DOWN | 0.65 | 0.91 | 2.41 |
| 10-26 22:26 | +10 stop | BTC | DOWN | 0.64 | 0.38 | -2.94 |
| 10-26 22:26 | +10 | BTC | DOWN | 0.64 | 0.88 | 2.15 |
| 10-26 22:26 | +10 stop | ZEC | UP | 0.60 | 0.74 | 1.09 |
| 10-26 22:26 | +20 | ZEC | UP | 0.60 | 0.92 | 2.97 |
| 10-26 22:26 | +15 | ZEC | UP | 0.60 | 0.92 | 2.97 |
| 10-26 22:26 | +10 | ZEC | UP | 0.60 | 0.74 | 1.09 |
| 10-26 22:26 | +5 | ZEC | UP | 0.60 | 0.74 | 1.09 |
| 10-26 22:24 | +10 stop | BTC | UP | 0.58 | 0.36 | -2.55 |
| 10-26 22:24 | +5 | BTC | UP | 0.58 | no | -5.98 |
| 10-26 22:24 | +10 stop | XRP | UP | 0.71 | 0.51 | -2.33 |
| 10-26 22:23 | +10 stop | SOL | UP | 0.62 | 0.39 | -2.64 |
| 10-26 22:23 | +10 | SOL | UP | 0.62 | no | -6.37 |
| 10-26 22:23 | +5 | SOL | UP | 0.62 | no | -6.37 |
| 10-26 22:22 | +10 stop | XRP | UP | 0.57 | 0.72 | 1.17 |
| 10-26 22:22 | +10 stop | BNB | UP | 0.58 | 0.68 | 0.66 |
| 10-26 22:22 | +10 stop | BTC | DOWN | 0.46 | 0.29 | -2.03 |
| 10-26 22:22 | +10 | BTC | DOWN | 0.46 | 0.63 | 1.35 |
| 10-26 22:22 | +5 | BTC | DOWN | 0.46 | 0.52 | 0.24 |
| 10-26 22:20 | +5 | SOL | UP | 0.64 | 0.71 | 0.38 |
| 10-26 22:20 | +10 stop | XRP | UP | 0.56 | 0.71 | 1.17 |
| 10-26 22:20 | +10 stop | BNB | UP | 0.65 | 0.48 | -2.04 |
| 10-26 22:20 | +5 | NEAR | UP | 0.70 | 0.79 | 0.63 |
| 10-26 22:20 | +10 stop | HYPE | UP | 0.70 | 0.83 | 1.01 |
| 10-26 22:20 | +10 | HYPE | UP | 0.70 | 0.83 | 1.01 |
| 10-26 22:20 | +5 | HYPE | UP | 0.70 | 0.79 | 0.59 |
