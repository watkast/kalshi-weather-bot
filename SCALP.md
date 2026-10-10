# Range-Scalp Bot

*Updated Sat Oct 10 02:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9831 | 8482 | 1349 (18) | 0 | $-3330.91 | -5.4% |
| **+10¢** | 7428 | 5853 | 1575 (30) | 0 | $-3212.37 | -6.9% |
| **+15¢** | 6265 | 4604 | 1661 (43) | 0 | $-2676.62 | -6.8% |
| **+20¢** | 5570 | 3843 | 1727 (55) | 0 | $-2254.63 | -6.4% |
| **+10¢ (15¢ stop)** | 12068 | 12033 | 35 (22) | 0 | $-4695.07 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 02:27 | +10 stop | DOGE | UP | 0.69 | 0.79 | 0.74 |
| 10-10 02:26 | +10 stop | XRP | UP | 0.60 | 0.36 | -2.74 |
| 10-10 02:24 | +10 stop | DOGE | UP | 0.58 | 0.70 | 0.87 |
| 10-10 02:24 | +5 | XRP | UP | 0.55 | no | -5.71 |
| 10-10 02:23 | +5 | XRP | UP | 0.54 | 0.61 | 0.35 |
| 10-10 02:23 | +10 stop | XRP | UP | 0.57 | 0.38 | -2.25 |
| 10-10 02:23 | +15 | XRP | UP | 0.57 | no | -5.88 |
| 10-10 02:23 | +10 | XRP | UP | 0.57 | no | -5.88 |
| 10-10 02:23 | +5 | XRP | UP | 0.57 | 0.65 | 0.46 |
| 10-10 02:22 | +10 stop | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 10-10 02:22 | +10 | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 10-10 02:22 | +5 | HYPE | DOWN | 0.71 | 0.80 | 0.63 |
| 10-10 02:22 | +10 stop | BNB | DOWN | 0.59 | 0.71 | 0.85 |
| 10-10 02:22 | +5 | BNB | DOWN | 0.59 | 0.71 | 0.85 |
| 10-10 02:21 | +10 stop | HYPE | DOWN | 0.69 | 0.80 | 0.83 |
| 10-10 02:21 | +10 stop | DOGE | UP | 0.71 | 0.51 | -2.29 |
| 10-10 02:21 | +15 | DOGE | UP | 0.71 | 0.97 | 2.46 |
| 10-10 02:21 | +10 | DOGE | UP | 0.71 | 0.82 | 0.88 |
| 10-10 02:21 | +5 | DOGE | UP | 0.71 | 0.76 | 0.26 |
| 10-10 02:21 | +10 stop | SOL | DOWN | 0.66 | 0.79 | 0.98 |
| 10-10 02:21 | +10 stop | BNB | DOWN | 0.60 | 0.73 | 0.99 |
| 10-10 02:20 | +10 stop | ETH | DOWN | 0.60 | 0.77 | 1.40 |
| 10-10 02:20 | +10 stop | ZEC | DOWN | 0.64 | 0.74 | 0.70 |
| 10-10 02:20 | +10 | ZEC | DOWN | 0.65 | 0.83 | 1.54 |
| 10-10 02:20 | +5 | ZEC | DOWN | 0.65 | 0.74 | 0.60 |
| 10-10 02:20 | +5 | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-10 02:19 | +10 stop | SOL | DOWN | 0.64 | 0.46 | -2.15 |
| 10-10 02:19 | +10 stop | DOGE | UP | 0.60 | 0.77 | 1.42 |
| 10-10 02:19 | +20 | DOGE | UP | 0.60 | 0.82 | 1.94 |
| 10-10 02:19 | +15 | DOGE | UP | 0.59 | 0.77 | 1.54 |
| 10-10 02:19 | +10 | DOGE | UP | 0.58 | 0.77 | 1.55 |
| 10-10 02:19 | +5 | DOGE | UP | 0.58 | 0.68 | 0.62 |
| 10-10 02:19 | +10 stop | XRP | DOWN | 0.66 | 0.43 | -2.64 |
| 10-10 02:19 | +10 stop | HYPE | DOWN | 0.66 | 0.48 | -2.14 |
| 10-10 02:19 | +10 stop | BNB | DOWN | 0.67 | 0.52 | -1.88 |
| 10-10 02:18 | +10 stop | SOL | UP | 0.45 | 0.56 | 0.76 |
| 10-10 02:16 | +10 stop | SOL | DOWN | 0.60 | 0.43 | -2.05 |
| 10-10 02:16 | +20 | SOL | DOWN | 0.60 | 0.83 | 2.03 |
| 10-10 02:16 | +15 | SOL | DOWN | 0.60 | 0.79 | 1.61 |
| 10-10 02:16 | +10 | SOL | DOWN | 0.60 | 0.79 | 1.61 |
