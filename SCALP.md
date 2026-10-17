# Range-Scalp Bot

*Updated Sat Oct 17 15:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21178 | 18436 | 2742 (29) | 2 | $-6155.13 | -4.6% |
| **+10¢** | 15937 | 12772 | 3165 (41) | 5 | $-5474.90 | -5.5% |
| **+15¢** | 13321 | 9912 | 3409 (61) | 6 | $-4968.06 | -5.9% |
| **+20¢** | 11808 | 8237 | 3571 (80) | 6 | $-4395.21 | -5.9% |
| **+10¢ (15¢ stop)** | 26016 | 25966 | 50 (29) | 0 | $-9903.11 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 15:41 | +10 | XRP | UP | 0.66 | 0.93 | 2.45 |
| 10-17 15:41 | +5 | XRP | UP | 0.66 | 0.74 | 0.50 |
| 10-17 15:41 | +10 stop | DOGE | DOWN | 0.71 | 0.52 | -2.23 |
| 10-17 15:41 | +10 stop | SOL | UP | 0.52 | 0.64 | 0.85 |
| 10-17 15:41 | +10 | SOL | UP | 0.52 | 0.64 | 0.85 |
| 10-17 15:41 | +5 | SOL | UP | 0.52 | 0.64 | 0.85 |
| 10-17 15:40 | +10 stop | XRP | UP | 0.66 | 0.93 | 2.46 |
| 10-17 15:40 | +10 stop | SOL | DOWN | 0.48 | 0.58 | 0.64 |
| 10-17 15:40 | +15 | SOL | DOWN | 0.47 | open |  |
| 10-17 15:40 | +10 | SOL | DOWN | 0.47 | 0.58 | 0.74 |
| 10-17 15:40 | +5 | SOL | DOWN | 0.47 | 0.58 | 0.74 |
| 10-17 15:40 | +10 stop | DOGE | DOWN | 0.71 | 0.54 | -2.03 |
| 10-17 15:40 | +20 | DOGE | DOWN | 0.71 | open |  |
| 10-17 15:40 | +15 | DOGE | DOWN | 0.71 | open |  |
| 10-17 15:40 | +10 | DOGE | DOWN | 0.71 | open |  |
| 10-17 15:40 | +5 | DOGE | DOWN | 0.71 | open |  |
| 10-17 15:39 | +10 stop | ETH | DOWN | 0.60 | 0.78 | 1.50 |
| 10-17 15:38 | +10 stop | XRP | UP | 0.42 | 0.52 | 0.64 |
| 10-17 15:37 | +10 stop | SOL | DOWN | 0.65 | 0.79 | 1.12 |
| 10-17 15:37 | +20 | SOL | DOWN | 0.66 | open |  |
| 10-17 15:37 | +15 | SOL | DOWN | 0.61 | 0.79 | 1.47 |
| 10-17 15:37 | +10 | SOL | DOWN | 0.60 | 0.71 | 0.78 |
| 10-17 15:37 | +5 | SOL | DOWN | 0.60 | 0.67 | 0.37 |
| 10-17 15:37 | +10 stop | BTC | DOWN | 0.71 | 0.84 | 1.05 |
| 10-17 15:37 | +10 stop | XRP | DOWN | 0.64 | 0.42 | -2.55 |
| 10-17 15:37 | +5 | BTC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-17 15:36 | +10 stop | ZEC | DOWN | 0.62 | 0.76 | 1.10 |
| 10-17 15:36 | +5 | ZEC | DOWN | 0.62 | 0.71 | 0.58 |
| 10-17 15:36 | +10 stop | XRP | UP | 0.48 | 0.58 | 0.64 |
| 10-17 15:36 | +10 stop | BTC | DOWN | 0.50 | 0.67 | 1.36 |
| 10-17 15:36 | +5 | BTC | DOWN | 0.50 | 0.55 | 0.14 |
| 10-17 15:36 | +10 stop | NEAR | DOWN | 0.71 | 0.49 | -2.53 |
| 10-17 15:36 | +5 | NEAR | DOWN | 0.71 | 0.86 | 1.26 |
| 10-17 15:35 | +10 stop | XRP | UP | 0.60 | 0.41 | -2.24 |
| 10-17 15:35 | +20 | XRP | UP | 0.60 | 0.93 | 3.04 |
| 10-17 15:35 | +15 | XRP | UP | 0.60 | 0.93 | 3.04 |
| 10-17 15:35 | +10 | XRP | UP | 0.60 | 0.72 | 0.88 |
| 10-17 15:35 | +5 | XRP | UP | 0.60 | 0.72 | 0.88 |
| 10-17 15:35 | +10 stop | ETH | UP | 0.61 | 0.35 | -2.93 |
| 10-17 15:35 | +20 | ETH | UP | 0.61 | open |  |
