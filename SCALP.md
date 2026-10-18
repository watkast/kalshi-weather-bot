# Range-Scalp Bot

*Updated Sun Oct 18 06:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22128 | 19259 | 2869 (29) | 0 | $-6475.34 | -4.6% |
| **+10¢** | 16656 | 13343 | 3313 (42) | 0 | $-5757.18 | -5.5% |
| **+15¢** | 13948 | 10377 | 3571 (62) | 0 | $-5231.77 | -6.0% |
| **+20¢** | 12344 | 8604 | 3740 (80) | 0 | $-4679.60 | -6.0% |
| **+10¢ (15¢ stop)** | 27230 | 27180 | 50 (29) | 0 | $-10435.09 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 05:59 | +10 stop | NEAR | UP | 0.70 | 0.83 | 1.05 |
| 10-18 05:58 | +10 stop | NEAR | DOWN | 0.63 | 0.44 | -2.25 |
| 10-18 05:56 | +10 stop | BTC | UP | 0.61 | 0.97 | 3.43 |
| 10-18 05:55 | +10 stop | NEAR | DOWN | 0.49 | 0.59 | 0.65 |
| 10-18 05:55 | +10 stop | BNB | UP | 0.56 | 0.32 | -2.74 |
| 10-18 05:55 | +10 stop | BTC | UP | 0.53 | 0.63 | 0.65 |
| 10-18 05:55 | +10 stop | ZEC | UP | 0.64 | 0.44 | -2.35 |
| 10-18 05:54 | +10 stop | DOGE | DOWN | 0.44 | 0.69 | 2.17 |
| 10-18 05:54 | +15 | DOGE | DOWN | 0.44 | 0.69 | 2.17 |
| 10-18 05:54 | +10 | DOGE | DOWN | 0.44 | 0.69 | 2.17 |
| 10-18 05:54 | +5 | DOGE | DOWN | 0.44 | 0.69 | 2.17 |
| 10-18 05:54 | +10 stop | ZEC | DOWN | 0.59 | 0.41 | -2.14 |
| 10-18 05:53 | +10 stop | BTC | DOWN | 0.61 | 0.46 | -1.85 |
| 10-18 05:53 | +10 stop | SOL | DOWN | 0.53 | 0.33 | -2.34 |
| 10-18 05:53 | +10 stop | XRP | DOWN | 0.54 | 0.35 | -2.24 |
| 10-18 05:53 | +10 stop | HYPE | DOWN | 0.70 | 0.47 | -2.67 |
| 10-18 05:52 | +10 stop | BNB | DOWN | 0.66 | 0.49 | -2.04 |
| 10-18 05:52 | +20 | BTC | UP | 0.71 | 0.97 | 2.45 |
| 10-18 05:52 | +10 stop | DOGE | DOWN | 0.62 | 0.75 | 0.99 |
| 10-18 05:51 | +10 stop | ZEC | UP | 0.48 | 0.29 | -2.23 |
| 10-18 05:51 | +10 stop | HYPE | UP | 0.54 | 0.39 | -1.85 |
| 10-18 05:51 | +5 | SOL | UP | 0.66 | 0.72 | 0.27 |
| 10-18 05:51 | +10 | XRP | UP | 0.70 | 0.85 | 1.30 |
| 10-18 05:51 | +5 | XRP | UP | 0.70 | 0.77 | 0.46 |
| 10-18 05:51 | +10 stop | XRP | UP | 0.69 | 0.54 | -1.83 |
| 10-18 05:50 | +10 stop | SOL | UP | 0.67 | 0.42 | -2.84 |
| 10-18 05:50 | +10 stop | BTC | UP | 0.68 | 0.41 | -3.03 |
| 10-18 05:50 | +15 | BTC | UP | 0.68 | 0.97 | 2.74 |
| 10-18 05:50 | +10 stop | DOGE | DOWN | 0.66 | 0.50 | -1.94 |
| 10-18 05:50 | +20 | DOGE | DOWN | 0.66 | yes | -6.76 |
| 10-18 05:50 | +15 | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-18 05:50 | +10 | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-18 05:50 | +5 | DOGE | DOWN | 0.66 | 0.75 | 0.60 |
| 10-18 05:50 | +10 | BTC | UP | 0.67 | 0.97 | 2.84 |
| 10-18 05:50 | +10 stop | HYPE | DOWN | 0.66 | 0.42 | -2.74 |
| 10-18 05:50 | +10 | HYPE | DOWN | 0.66 | yes | -6.76 |
| 10-18 05:50 | +5 | HYPE | DOWN | 0.66 | yes | -6.76 |
| 10-18 05:50 | +10 stop | ZEC | DOWN | 0.66 | 0.51 | -1.84 |
| 10-18 05:50 | +15 | BNB | DOWN | 0.70 | no | 2.85 |
| 10-18 05:50 | +10 stop | ETH | UP | 0.68 | 0.79 | 0.82 |
