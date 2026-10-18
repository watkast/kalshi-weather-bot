# Range-Scalp Bot

*Updated Sun Oct 18 00:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21791 | 18986 | 2805 (29) | 2 | $-6241.67 | -4.5% |
| **+10¢** | 16393 | 13147 | 3246 (41) | 3 | $-5580.44 | -5.4% |
| **+15¢** | 13711 | 10207 | 3504 (61) | 3 | $-5093.94 | -5.9% |
| **+20¢** | 12140 | 8467 | 3673 (80) | 2 | $-4558.03 | -6.0% |
| **+10¢ (15¢ stop)** | 26788 | 26738 | 50 (29) | 1 | $-10214.73 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 00:26 | +10 stop | ZEC | UP | 0.51 | 0.22 | -3.21 |
| 10-18 00:26 | +10 stop | SOL | UP | 0.62 | 0.81 | 1.62 |
| 10-18 00:26 | +5 | SOL | UP | 0.62 | 0.71 | 0.58 |
| 10-18 00:25 | +10 stop | BNB | UP | 0.57 | 0.70 | 0.96 |
| 10-18 00:25 | +10 | BNB | UP | 0.57 | 0.70 | 0.96 |
| 10-18 00:25 | +5 | BNB | UP | 0.57 | 0.70 | 0.96 |
| 10-18 00:25 | +5 | ZEC | UP | 0.59 | open |  |
| 10-18 00:23 | +10 stop | XRP | UP | 0.59 | 0.70 | 0.75 |
| 10-18 00:22 | +5 | NEAR | DOWN | 0.65 | 0.72 | 0.39 |
| 10-18 00:22 | +10 stop | BNB | UP | 0.62 | 0.72 | 0.68 |
| 10-18 00:22 | +10 | BNB | UP | 0.62 | 0.72 | 0.68 |
| 10-18 00:22 | +5 | BNB | UP | 0.62 | 0.72 | 0.68 |
| 10-18 00:22 | +10 stop | ZEC | UP | 0.69 | 0.53 | -1.93 |
| 10-18 00:22 | +15 | ZEC | UP | 0.69 | open |  |
| 10-18 00:22 | +10 | ZEC | UP | 0.68 | open |  |
| 10-18 00:22 | +5 | ZEC | UP | 0.67 | 0.72 | 0.19 |
| 10-18 00:22 | +10 stop | XRP | UP | 0.66 | 0.46 | -2.34 |
| 10-18 00:22 | +5 | XRP | UP | 0.66 | 0.71 | 0.19 |
| 10-18 00:22 | +10 stop | NEAR | DOWN | 0.57 | 0.72 | 1.17 |
| 10-18 00:22 | +15 | NEAR | DOWN | 0.57 | 0.72 | 1.17 |
| 10-18 00:22 | +10 | NEAR | DOWN | 0.57 | 0.72 | 1.17 |
| 10-18 00:22 | +5 | NEAR | DOWN | 0.57 | 0.66 | 0.56 |
| 10-18 00:22 | +10 stop | DOGE | DOWN | 0.51 | 0.33 | -2.14 |
| 10-18 00:21 | +10 stop | ZEC | DOWN | 0.46 | 0.63 | 1.35 |
| 10-18 00:21 | +15 | ZEC | DOWN | 0.48 | 0.63 | 1.15 |
| 10-18 00:21 | +10 | ZEC | DOWN | 0.48 | 0.63 | 1.15 |
| 10-18 00:21 | +5 | ZEC | DOWN | 0.42 | 0.63 | 1.75 |
| 10-18 00:21 | +10 stop | DOGE | DOWN | 0.57 | 0.68 | 0.76 |
| 10-18 00:20 | +10 stop | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-18 00:20 | +10 stop | ETH | UP | 0.56 | 0.69 | 0.97 |
| 10-18 00:20 | +20 | ETH | UP | 0.56 | 0.79 | 2.00 |
| 10-18 00:20 | +15 | ETH | UP | 0.56 | 0.73 | 1.38 |
| 10-18 00:20 | +10 | ETH | UP | 0.56 | 0.69 | 0.97 |
| 10-18 00:20 | +5 | ETH | UP | 0.56 | 0.69 | 0.97 |
| 10-18 00:19 | +10 stop | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-18 00:19 | +5 | NEAR | DOWN | 0.71 | 0.77 | 0.32 |
| 10-18 00:18 | +10 stop | ZEC | DOWN | 0.51 | 0.63 | 0.85 |
| 10-18 00:18 | +20 | ZEC | DOWN | 0.51 | 0.77 | 2.29 |
| 10-18 00:18 | +15 | ZEC | DOWN | 0.51 | 0.68 | 1.36 |
| 10-18 00:18 | +10 | ZEC | DOWN | 0.51 | 0.63 | 0.85 |
