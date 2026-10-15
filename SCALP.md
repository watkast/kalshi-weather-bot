# Range-Scalp Bot

*Updated Thu Oct 15 00:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16796 | 14569 | 2227 (28) | 2 | $-5205.98 | -4.9% |
| **+10¢** | 12696 | 10115 | 2581 (40) | 3 | $-4750.64 | -5.9% |
| **+15¢** | 10661 | 7889 | 2772 (59) | 3 | $-4257.95 | -6.4% |
| **+20¢** | 9470 | 6566 | 2904 (76) | 3 | $-3757.08 | -6.3% |
| **+10¢ (15¢ stop)** | 20670 | 20620 | 50 (29) | 0 | $-7961.13 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 00:27 | +10 stop | DOGE | DOWN | 0.70 | 0.93 | 2.10 |
| 10-15 00:26 | +10 stop | XRP | DOWN | 0.64 | 0.78 | 1.10 |
| 10-15 00:26 | +5 | XRP | DOWN | 0.64 | 0.78 | 1.10 |
| 10-15 00:25 | +10 stop | DOGE | DOWN | 0.63 | 0.44 | -2.25 |
| 10-15 00:25 | +10 | DOGE | DOWN | 0.63 | 0.76 | 1.00 |
| 10-15 00:25 | +5 | DOGE | DOWN | 0.63 | 0.76 | 1.00 |
| 10-15 00:25 | +10 stop | ETH | UP | 0.68 | 0.79 | 0.82 |
| 10-15 00:25 | +10 | ETH | UP | 0.68 | 0.79 | 0.82 |
| 10-15 00:25 | +5 | ETH | UP | 0.68 | 0.79 | 0.82 |
| 10-15 00:25 | +10 stop | ZEC | UP | 0.64 | 0.46 | -2.15 |
| 10-15 00:25 | +10 | ZEC | UP | 0.64 | open |  |
| 10-15 00:25 | +5 | DOGE | UP | 0.44 | 0.65 | 1.76 |
| 10-15 00:24 | +5 | SOL | UP | 0.59 | 0.67 | 0.47 |
| 10-15 00:24 | +5 | HYPE | UP | 0.53 | 0.58 | 0.14 |
| 10-15 00:23 | +5 | SOL | UP | 0.60 | 0.67 | 0.37 |
| 10-15 00:23 | +10 stop | HYPE | UP | 0.56 | 0.27 | -3.21 |
| 10-15 00:23 | +15 | HYPE | UP | 0.56 | open |  |
| 10-15 00:23 | +10 | HYPE | UP | 0.56 | open |  |
| 10-15 00:23 | +5 | HYPE | UP | 0.56 | 0.62 | 0.26 |
| 10-15 00:22 | +5 | BTC | DOWN | 0.64 | 0.76 | 0.90 |
| 10-15 00:22 | +10 stop | ETH | UP | 0.71 | 0.81 | 0.74 |
| 10-15 00:22 | +20 | ETH | UP | 0.71 | 0.97 | 2.41 |
| 10-15 00:22 | +15 | ETH | UP | 0.71 | 0.97 | 2.41 |
| 10-15 00:22 | +10 | ETH | UP | 0.71 | 0.81 | 0.74 |
| 10-15 00:22 | +5 | ETH | UP | 0.71 | 0.81 | 0.74 |
| 10-15 00:22 | +10 stop | DOGE | UP | 0.71 | 0.36 | -3.82 |
| 10-15 00:22 | +5 | DOGE | UP | 0.71 | 0.76 | 0.22 |
| 10-15 00:22 | +10 stop | BNB | UP | 0.67 | 0.78 | 0.81 |
| 10-15 00:22 | +10 stop | XRP | UP | 0.63 | 0.26 | -4.01 |
| 10-15 00:22 | +10 stop | NEAR | DOWN | 0.67 | 0.82 | 1.23 |
| 10-15 00:22 | +20 | NEAR | DOWN | 0.67 | 0.91 | 2.12 |
| 10-15 00:22 | +15 | NEAR | DOWN | 0.67 | 0.82 | 1.23 |
| 10-15 00:22 | +10 | NEAR | DOWN | 0.67 | 0.82 | 1.23 |
| 10-15 00:22 | +5 | NEAR | DOWN | 0.67 | 0.74 | 0.40 |
| 10-15 00:22 | +10 stop | ZEC | UP | 0.62 | 0.45 | -2.05 |
| 10-15 00:22 | +10 stop | SOL | UP | 0.65 | 0.46 | -2.24 |
| 10-15 00:22 | +10 stop | BTC | DOWN | 0.58 | 0.76 | 1.49 |
| 10-15 00:22 | +15 | BTC | DOWN | 0.58 | 0.76 | 1.49 |
| 10-15 00:22 | +10 | BTC | DOWN | 0.58 | 0.76 | 1.49 |
| 10-15 00:22 | +5 | BTC | DOWN | 0.58 | 0.64 | 0.25 |
