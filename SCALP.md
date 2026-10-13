# Range-Scalp Bot

*Updated Tue Oct 13 09:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14458 | 12501 | 1957 (27) | 0 | $-4690.19 | -5.1% |
| **+10¢** | 10939 | 8666 | 2273 (39) | 0 | $-4409.81 | -6.4% |
| **+15¢** | 9193 | 6762 | 2431 (57) | 0 | $-3925.73 | -6.8% |
| **+20¢** | 8182 | 5650 | 2532 (72) | 0 | $-3378.03 | -6.6% |
| **+10¢ (15¢ stop)** | 17731 | 17682 | 49 (29) | 0 | $-6874.81 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 09:24 | +5 | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-13 09:24 | +10 stop | SOL | DOWN | 0.64 | 0.86 | 1.94 |
| 10-13 09:24 | +15 | SOL | DOWN | 0.64 | 0.86 | 1.94 |
| 10-13 09:24 | +5 | SOL | DOWN | 0.62 | 0.71 | 0.58 |
| 10-13 09:23 | +10 stop | ETH | DOWN | 0.70 | 0.86 | 1.36 |
| 10-13 09:23 | +5 | ETH | DOWN | 0.70 | 0.76 | 0.32 |
| 10-13 09:21 | +10 stop | ETH | DOWN | 0.60 | 0.74 | 1.09 |
| 10-13 09:21 | +10 stop | NEAR | DOWN | 0.48 | 0.62 | 1.09 |
| 10-13 09:21 | +10 stop | NEAR | UP | 0.43 | 0.58 | 1.14 |
| 10-13 09:20 | +10 stop | SOL | UP | 0.61 | 0.42 | -2.25 |
| 10-13 09:20 | +10 stop | ETH | DOWN | 0.57 | 0.68 | 0.76 |
| 10-13 09:20 | +10 stop | BTC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-13 09:20 | +10 | BTC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-13 09:20 | +5 | BTC | DOWN | 0.65 | 0.71 | 0.29 |
| 10-13 09:19 | +10 stop | SOL | DOWN | 0.70 | 0.46 | -2.73 |
| 10-13 09:19 | +10 | SOL | DOWN | 0.70 | 0.86 | 1.36 |
| 10-13 09:18 | +5 | SOL | DOWN | 0.68 | 0.73 | 0.20 |
| 10-13 09:17 | +10 stop | NEAR | DOWN | 0.60 | 0.44 | -1.95 |
| 10-13 09:17 | +20 | NEAR | DOWN | 0.60 | 0.82 | 1.92 |
| 10-13 09:17 | +15 | NEAR | DOWN | 0.60 | 0.75 | 1.19 |
| 10-13 09:17 | +10 | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
| 10-13 09:17 | +5 | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
| 10-13 09:16 | +10 stop | XRP | DOWN | 0.62 | 0.73 | 0.79 |
| 10-13 09:16 | +20 | XRP | DOWN | 0.62 | 0.82 | 1.72 |
| 10-13 09:16 | +15 | XRP | DOWN | 0.62 | 0.80 | 1.51 |
| 10-13 09:16 | +10 | XRP | DOWN | 0.62 | 0.73 | 0.79 |
| 10-13 09:16 | +5 | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-13 09:16 | +10 stop | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-13 09:16 | +20 | BTC | DOWN | 0.65 | 0.85 | 1.75 |
| 10-13 09:16 | +15 | BTC | DOWN | 0.65 | 0.85 | 1.75 |
| 10-13 09:16 | +10 | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-13 09:16 | +5 | BTC | DOWN | 0.65 | 0.71 | 0.29 |
| 10-13 09:16 | +10 stop | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-13 09:16 | +20 | ZEC | DOWN | 0.70 | 0.95 | 2.30 |
| 10-13 09:16 | +15 | ZEC | DOWN | 0.70 | 0.88 | 1.57 |
| 10-13 09:16 | +10 | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-13 09:16 | +5 | ZEC | DOWN | 0.70 | 0.75 | 0.21 |
| 10-13 09:16 | +10 stop | BNB | DOWN | 0.70 | 0.81 | 0.84 |
| 10-13 09:16 | +20 | BNB | DOWN | 0.70 | 0.94 | 2.19 |
| 10-13 09:16 | +15 | BNB | DOWN | 0.70 | 0.86 | 1.36 |
