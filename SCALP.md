# Range-Scalp Bot

*Updated Thu Oct 22 02:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28132 | 24516 | 3616 (39) | 0 | $-8059.95 | -4.5% |
| **+10¢** | 21135 | 16956 | 4179 (55) | 1 | $-7108.67 | -5.3% |
| **+15¢** | 17702 | 13207 | 4495 (78) | 1 | $-6321.45 | -5.7% |
| **+20¢** | 15664 | 10952 | 4712 (98) | 2 | $-5672.91 | -5.8% |
| **+10¢ (15¢ stop)** | 34526 | 34467 | 59 (32) | 0 | $-12889.39 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 02:43 | +10 stop | NEAR | DOWN | 0.33 | 0.52 | 1.56 |
| 10-22 02:43 | +10 | NEAR | DOWN | 0.33 | 0.52 | 1.56 |
| 10-22 02:43 | +5 | NEAR | DOWN | 0.33 | 0.52 | 1.56 |
| 10-22 02:42 | +10 stop | XRP | DOWN | 0.71 | 0.27 | -4.69 |
| 10-22 02:42 | +10 | XRP | DOWN | 0.71 | 0.98 | 2.54 |
| 10-22 02:42 | +5 | XRP | DOWN | 0.71 | 0.98 | 2.54 |
| 10-22 02:42 | +10 stop | BTC | UP | 0.58 | 0.75 | 1.38 |
| 10-22 02:42 | +15 | BTC | UP | 0.59 | 0.75 | 1.29 |
| 10-22 02:42 | +10 | BTC | UP | 0.59 | 0.75 | 1.29 |
| 10-22 02:42 | +5 | BTC | UP | 0.59 | 0.66 | 0.37 |
| 10-22 02:42 | +10 stop | XRP | DOWN | 0.56 | 0.68 | 0.86 |
| 10-22 02:42 | +10 | XRP | DOWN | 0.56 | 0.68 | 0.86 |
| 10-22 02:42 | +5 | XRP | DOWN | 0.56 | 0.68 | 0.86 |
| 10-22 02:41 | +10 stop | ETH | UP | 0.60 | 0.12 | -5.03 |
| 10-22 02:41 | +20 | ETH | UP | 0.59 | open |  |
| 10-22 02:41 | +15 | ETH | UP | 0.59 | open |  |
| 10-22 02:41 | +10 | ETH | UP | 0.59 | open |  |
| 10-22 02:41 | +5 | ETH | UP | 0.58 | 0.68 | 0.66 |
| 10-22 02:41 | +10 stop | XRP | UP | 0.49 | 0.63 | 1.05 |
| 10-22 02:41 | +15 | XRP | UP | 0.49 | 0.70 | 1.77 |
| 10-22 02:41 | +10 | XRP | UP | 0.50 | 0.63 | 0.95 |
| 10-22 02:41 | +5 | XRP | UP | 0.49 | 0.63 | 1.05 |
| 10-22 02:41 | +10 stop | NEAR | UP | 0.53 | 0.67 | 1.06 |
| 10-22 02:41 | +10 | NEAR | UP | 0.53 | 0.67 | 1.06 |
| 10-22 02:39 | +5 | ETH | UP | 0.66 | 0.72 | 0.29 |
| 10-22 02:39 | +5 | BTC | UP | 0.69 | 0.76 | 0.42 |
| 10-22 02:38 | +10 stop | XRP | UP | 0.68 | 0.85 | 1.45 |
| 10-22 02:38 | +15 | XRP | UP | 0.68 | 0.85 | 1.45 |
| 10-22 02:38 | +10 | XRP | UP | 0.70 | 0.85 | 1.26 |
| 10-22 02:38 | +10 stop | NEAR | DOWN | 0.64 | 0.43 | -2.45 |
| 10-22 02:36 | +10 stop | ETH | UP | 0.64 | 0.85 | 1.84 |
| 10-22 02:36 | +10 | ETH | UP | 0.64 | 0.85 | 1.84 |
| 10-22 02:36 | +5 | ETH | UP | 0.64 | 0.70 | 0.28 |
| 10-22 02:36 | +5 | NEAR | DOWN | 0.56 | 0.81 | 2.21 |
| 10-22 02:36 | +15 | SOL | UP | 0.61 | 0.76 | 1.20 |
| 10-22 02:36 | +5 | SOL | UP | 0.61 | 0.73 | 0.89 |
| 10-22 02:36 | +5 | DOGE | UP | 0.65 | 0.70 | 0.19 |
| 10-22 02:36 | +10 stop | BTC | UP | 0.67 | 0.88 | 1.86 |
| 10-22 02:35 | +10 stop | NEAR | DOWN | 0.47 | 0.59 | 0.85 |
| 10-22 02:34 | +10 stop | DOGE | UP | 0.70 | 0.81 | 0.85 |
