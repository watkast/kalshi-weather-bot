# Range-Scalp Bot

*Updated Sun Oct 11 19:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12372 | 10674 | 1698 (25) | 1 | $-4113.33 | -5.3% |
| **+10¢** | 9397 | 7432 | 1965 (37) | 2 | $-3859.77 | -6.5% |
| **+15¢** | 7914 | 5828 | 2086 (54) | 3 | $-3291.76 | -6.6% |
| **+20¢** | 7052 | 4880 | 2172 (68) | 5 | $-2769.07 | -6.3% |
| **+10¢ (15¢ stop)** | 15249 | 15208 | 41 (25) | 2 | $-6017.10 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 19:26 | +10 stop | XRP | UP | 0.49 | 0.65 | 1.26 |
| 10-11 19:26 | +20 | XRP | UP | 0.49 | open |  |
| 10-11 19:26 | +15 | XRP | UP | 0.49 | 0.65 | 1.26 |
| 10-11 19:26 | +10 | XRP | UP | 0.49 | 0.65 | 1.26 |
| 10-11 19:26 | +5 | XRP | UP | 0.49 | 0.65 | 1.26 |
| 10-11 19:26 | +10 stop | BTC | DOWN | 0.71 | open |  |
| 10-11 19:26 | +20 | BTC | DOWN | 0.71 | open |  |
| 10-11 19:26 | +10 | BTC | DOWN | 0.71 | open |  |
| 10-11 19:26 | +5 | BTC | DOWN | 0.71 | open |  |
| 10-11 19:25 | +10 stop | SOL | DOWN | 0.65 | open |  |
| 10-11 19:24 | +10 stop | ZEC | UP | 0.54 | 0.29 | -2.83 |
| 10-11 19:22 | +10 stop | ZEC | DOWN | 0.61 | 0.46 | -1.85 |
| 10-11 19:22 | +10 | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-11 19:22 | +5 | ZEC | DOWN | 0.65 | 0.72 | 0.39 |
| 10-11 19:21 | +10 stop | BTC | UP | 0.67 | 0.77 | 0.71 |
| 10-11 19:21 | +15 | BTC | UP | 0.67 | open |  |
| 10-11 19:21 | +10 | BTC | UP | 0.67 | 0.77 | 0.71 |
| 10-11 19:21 | +5 | BTC | UP | 0.66 | 0.74 | 0.50 |
| 10-11 19:21 | +10 | ZEC | UP | 0.35 | 0.60 | 2.18 |
| 10-11 19:21 | +10 stop | SOL | UP | 0.58 | 0.37 | -2.45 |
| 10-11 19:21 | +5 | ZEC | UP | 0.63 | 0.69 | 0.31 |
| 10-11 19:21 | +10 stop | ETH | UP | 0.61 | 0.73 | 0.89 |
| 10-11 19:21 | +10 stop | ZEC | UP | 0.70 | 0.32 | -4.11 |
| 10-11 19:19 | +10 stop | ZEC | UP | 0.46 | 0.56 | 0.64 |
| 10-11 19:19 | +5 | SOL | DOWN | 0.64 | 0.71 | 0.38 |
| 10-11 19:19 | +10 stop | ETH | UP | 0.59 | 0.43 | -2.00 |
| 10-11 19:18 | +10 stop | SOL | DOWN | 0.62 | 0.45 | -2.05 |
| 10-11 19:18 | +5 | SOL | DOWN | 0.61 | 0.67 | 0.27 |
| 10-11 19:18 | +10 stop | ZEC | DOWN | 0.66 | 0.44 | -2.54 |
| 10-11 19:18 | +10 stop | BTC | UP | 0.60 | 0.71 | 0.78 |
| 10-11 19:18 | +10 | BTC | UP | 0.60 | 0.71 | 0.78 |
| 10-11 19:17 | +10 stop | HYPE | UP | 0.54 | 0.67 | 0.96 |
| 10-11 19:17 | +20 | HYPE | UP | 0.54 | 0.84 | 2.72 |
| 10-11 19:17 | +15 | HYPE | UP | 0.54 | 0.72 | 1.47 |
| 10-11 19:17 | +10 | HYPE | UP | 0.54 | 0.67 | 0.96 |
| 10-11 19:17 | +5 | HYPE | UP | 0.54 | 0.67 | 0.96 |
| 10-11 19:17 | +5 | BTC | UP | 0.64 | 0.71 | 0.38 |
| 10-11 19:17 | +5 | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 10-11 19:17 | +5 | BNB | UP | 0.67 | 0.75 | 0.50 |
| 10-11 19:17 | +10 | BNB | UP | 0.66 | 0.78 | 0.93 |
