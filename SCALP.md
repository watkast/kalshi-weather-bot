# Range-Scalp Bot

*Updated Sun Oct 18 02:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21923 | 19101 | 2822 (29) | 6 | $-6274.85 | -4.5% |
| **+10¢** | 16498 | 13232 | 3266 (41) | 5 | $-5607.36 | -5.4% |
| **+15¢** | 13813 | 10288 | 3525 (61) | 2 | $-5097.74 | -5.9% |
| **+20¢** | 12226 | 8532 | 3694 (80) | 1 | $-4553.18 | -5.9% |
| **+10¢ (15¢ stop)** | 26971 | 26921 | 50 (29) | 0 | $-10283.95 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 02:22 | +10 stop | BNB | UP | 0.70 | 0.85 | 1.26 |
| 10-18 02:22 | +20 | BNB | UP | 0.70 | 0.91 | 1.89 |
| 10-18 02:22 | +10 stop | BTC | UP | 0.71 | 0.81 | 0.74 |
| 10-18 02:21 | +10 stop | HYPE | UP | 0.67 | 0.83 | 1.34 |
| 10-18 02:20 | +10 stop | ZEC | UP | 0.70 | 0.82 | 0.94 |
| 10-18 02:20 | +20 | ZEC | UP | 0.70 | 0.91 | 1.90 |
| 10-18 02:20 | +15 | ZEC | UP | 0.70 | 0.87 | 1.47 |
| 10-18 02:20 | +10 | ZEC | UP | 0.70 | 0.82 | 0.94 |
| 10-18 02:20 | +5 | ZEC | UP | 0.70 | 0.82 | 0.94 |
| 10-18 02:20 | +10 stop | NEAR | UP | 0.65 | 0.75 | 0.70 |
| 10-18 02:20 | +15 | NEAR | UP | 0.65 | 0.82 | 1.43 |
| 10-18 02:20 | +10 | NEAR | UP | 0.65 | 0.75 | 0.70 |
| 10-18 02:20 | +5 | NEAR | UP | 0.65 | 0.75 | 0.70 |
| 10-18 02:19 | +20 | HYPE | UP | 0.70 | 0.90 | 1.79 |
| 10-18 02:19 | +10 stop | BNB | UP | 0.56 | 0.67 | 0.76 |
| 10-18 02:19 | +15 | BNB | UP | 0.56 | 0.72 | 1.27 |
| 10-18 02:19 | +10 stop | SOL | UP | 0.61 | 0.76 | 1.20 |
| 10-18 02:19 | +10 stop | DOGE | UP | 0.60 | 0.72 | 0.88 |
| 10-18 02:19 | +10 | DOGE | UP | 0.60 | 0.72 | 0.88 |
| 10-18 02:19 | +10 stop | XRP | UP | 0.58 | 0.70 | 0.87 |
| 10-18 02:19 | +15 | XRP | UP | 0.58 | 0.77 | 1.59 |
| 10-18 02:19 | +10 stop | ETH | UP | 0.67 | 0.80 | 1.02 |
| 10-18 02:19 | +15 | ETH | UP | 0.67 | 0.82 | 1.23 |
| 10-18 02:19 | +10 | ETH | UP | 0.67 | 0.80 | 1.02 |
| 10-18 02:19 | +15 | HYPE | UP | 0.69 | 0.90 | 1.85 |
| 10-18 02:19 | +10 stop | BTC | UP | 0.63 | 0.74 | 0.79 |
| 10-18 02:19 | +5 | ETH | UP | 0.68 | 0.75 | 0.40 |
| 10-18 02:19 | +10 stop | HYPE | UP | 0.70 | 0.54 | -1.94 |
| 10-18 02:18 | +10 stop | DOGE | DOWN | 0.56 | 0.37 | -2.25 |
| 10-18 02:18 | +5 | SOL | DOWN | 0.62 | open |  |
| 10-18 02:18 | +5 | DOGE | DOWN | 0.65 | open |  |
| 10-18 02:18 | +5 | BNB | DOWN | 0.58 | open |  |
| 10-18 02:17 | +10 stop | HYPE | DOWN | 0.63 | 0.48 | -1.85 |
| 10-18 02:17 | +10 | HYPE | DOWN | 0.63 | open |  |
| 10-18 02:17 | +5 | HYPE | DOWN | 0.63 | open |  |
| 10-18 02:17 | +10 stop | BNB | DOWN | 0.55 | 0.39 | -1.95 |
| 10-18 02:17 | +10 | BNB | DOWN | 0.55 | open |  |
| 10-18 02:17 | +5 | BNB | DOWN | 0.55 | 0.61 | 0.25 |
| 10-18 02:17 | +10 stop | BTC | DOWN | 0.59 | 0.43 | -1.95 |
| 10-18 02:17 | +20 | BTC | DOWN | 0.59 | open |  |
