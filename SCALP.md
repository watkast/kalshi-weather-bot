# Range-Scalp Bot

*Updated Sat Nov 07 02:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50343 | 43885 | 6458 (76) | 1 | $-14148.19 | -4.5% |
| **+10¢** | 37564 | 30046 | 7518 (102) | 1 | $-13073.68 | -5.5% |
| **+15¢** | 31457 | 23356 | 8101 (131) | 1 | $-11980.45 | -6.1% |
| **+20¢** | 27965 | 19470 | 8495 (173) | 1 | $-10606.23 | -6.0% |
| **+10¢ (15¢ stop)** | 61298 | 61199 | 99 (58) | 0 | $-22713.84 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 02:25 | +10 stop | HYPE | DOWN | 0.68 | 0.33 | -3.82 |
| 11-07 02:24 | +10 stop | HYPE | DOWN | 0.48 | 0.80 | 2.90 |
| 11-07 02:22 | +10 stop | HYPE | UP | 0.59 | 0.43 | -1.95 |
| 11-07 02:22 | +15 | HYPE | UP | 0.59 | 0.85 | 2.34 |
| 11-07 02:22 | +10 | HYPE | UP | 0.59 | 0.85 | 2.34 |
| 11-07 02:22 | +5 | HYPE | UP | 0.59 | 0.85 | 2.34 |
| 11-07 02:21 | +10 stop | NEAR | UP | 0.43 | 0.13 | -3.26 |
| 11-07 02:20 | +5 | ETH | DOWN | 0.63 | 0.70 | 0.38 |
| 11-07 02:20 | +5 | HYPE | UP | 0.63 | 0.72 | 0.58 |
| 11-07 02:20 | +5 | ETH | DOWN | 0.59 | 0.68 | 0.57 |
| 11-07 02:20 | +5 | BTC | DOWN | 0.65 | 0.78 | 1.01 |
| 11-07 02:19 | +5 | NEAR | UP | 0.61 | open |  |
| 11-07 02:19 | +5 | ETH | DOWN | 0.61 | 0.66 | 0.17 |
| 11-07 02:19 | +5 | BTC | DOWN | 0.57 | 0.63 | 0.25 |
| 11-07 02:18 | +5 | SOL | DOWN | 0.59 | 0.67 | 0.47 |
| 11-07 02:18 | +10 stop | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-07 02:18 | +20 | ZEC | DOWN | 0.71 | 0.92 | 1.89 |
| 11-07 02:18 | +15 | ZEC | DOWN | 0.71 | 0.86 | 1.26 |
| 11-07 02:18 | +10 | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-07 02:18 | +5 | ZEC | DOWN | 0.71 | 0.79 | 0.53 |
| 11-07 02:17 | +10 stop | ETH | DOWN | 0.71 | 0.87 | 1.37 |
| 11-07 02:17 | +20 | ETH | DOWN | 0.71 | 0.92 | 1.87 |
| 11-07 02:17 | +15 | ETH | DOWN | 0.71 | 0.87 | 1.37 |
| 11-07 02:17 | +10 | ETH | DOWN | 0.71 | 0.87 | 1.37 |
| 11-07 02:17 | +5 | ETH | DOWN | 0.71 | 0.80 | 0.63 |
| 11-07 02:17 | +10 stop | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-07 02:17 | +20 | BTC | DOWN | 0.70 | 0.91 | 1.86 |
| 11-07 02:17 | +15 | BTC | DOWN | 0.70 | 0.87 | 1.47 |
| 11-07 02:17 | +10 | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-07 02:17 | +5 | BTC | DOWN | 0.70 | 0.78 | 0.52 |
| 11-07 02:17 | +10 stop | HYPE | UP | 0.56 | 0.66 | 0.66 |
| 11-07 02:17 | +20 | HYPE | UP | 0.56 | 0.85 | 2.63 |
| 11-07 02:17 | +15 | HYPE | UP | 0.56 | 0.72 | 1.27 |
| 11-07 02:17 | +10 | HYPE | UP | 0.56 | 0.66 | 0.66 |
| 11-07 02:17 | +5 | HYPE | UP | 0.56 | 0.64 | 0.45 |
| 11-07 02:16 | +10 stop | DOGE | DOWN | 0.68 | 0.81 | 1.03 |
| 11-07 02:16 | +20 | DOGE | DOWN | 0.68 | 0.95 | 2.47 |
| 11-07 02:16 | +15 | DOGE | DOWN | 0.68 | 0.83 | 1.24 |
| 11-07 02:16 | +10 | DOGE | DOWN | 0.68 | 0.81 | 1.03 |
| 11-07 02:16 | +5 | DOGE | DOWN | 0.68 | 0.81 | 1.03 |
