# Range-Scalp Bot

*Updated Sun Oct 18 03:49 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22005 | 19162 | 2843 (29) | 0 | $-6362.90 | -4.6% |
| **+10¢** | 16560 | 13276 | 3284 (41) | 0 | $-5659.18 | -5.4% |
| **+15¢** | 13869 | 10328 | 3541 (61) | 0 | $-5129.97 | -5.9% |
| **+20¢** | 12272 | 8562 | 3710 (80) | 1 | $-4579.43 | -5.9% |
| **+10¢ (15¢ stop)** | 27075 | 27025 | 50 (29) | 0 | $-10353.02 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 03:46 | +10 stop | BTC | UP | 0.68 | 0.78 | 0.71 |
| 10-18 03:46 | +20 | BTC | UP | 0.68 | open |  |
| 10-18 03:46 | +15 | BTC | UP | 0.68 | 0.85 | 1.45 |
| 10-18 03:46 | +10 | BTC | UP | 0.67 | 0.78 | 0.81 |
| 10-18 03:46 | +5 | BTC | UP | 0.67 | 0.74 | 0.40 |
| 10-18 03:46 | +10 stop | ZEC | UP | 0.67 | 0.87 | 1.76 |
| 10-18 03:46 | +20 | ZEC | UP | 0.67 | 0.87 | 1.76 |
| 10-18 03:46 | +15 | ZEC | UP | 0.67 | 0.87 | 1.76 |
| 10-18 03:46 | +10 | ZEC | UP | 0.67 | 0.87 | 1.76 |
| 10-18 03:46 | +5 | ZEC | UP | 0.67 | 0.72 | 0.19 |
| 10-18 03:46 | +10 stop | BNB | UP | 0.68 | 0.83 | 1.24 |
| 10-18 03:46 | +20 | BNB | UP | 0.68 | 0.89 | 1.87 |
| 10-18 03:46 | +15 | BNB | UP | 0.68 | 0.83 | 1.24 |
| 10-18 03:46 | +10 | BNB | UP | 0.68 | 0.83 | 1.24 |
| 10-18 03:46 | +5 | BNB | UP | 0.68 | 0.75 | 0.40 |
| 10-18 03:39 | +10 stop | ETH | UP | 0.61 | 0.87 | 2.35 |
| 10-18 03:39 | +10 stop | HYPE | UP | 0.66 | 0.80 | 1.12 |
| 10-18 03:37 | +10 stop | BTC | UP | 0.67 | 0.79 | 0.92 |
| 10-18 03:36 | +10 stop | NEAR | DOWN | 0.64 | 0.47 | -2.05 |
| 10-18 03:35 | +10 stop | ETH | DOWN | 0.52 | 0.33 | -2.24 |
| 10-18 03:34 | +10 stop | DOGE | UP | 0.56 | 0.71 | 1.17 |
| 10-18 03:33 | +5 | HYPE | DOWN | 0.66 | yes | -6.76 |
| 10-18 03:33 | +10 stop | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 10-18 03:33 | +10 stop | SOL | UP | 0.67 | 0.77 | 0.71 |
| 10-18 03:33 | +15 | SOL | UP | 0.67 | 0.82 | 1.23 |
| 10-18 03:33 | +10 | SOL | UP | 0.67 | 0.77 | 0.71 |
| 10-18 03:33 | +5 | SOL | UP | 0.67 | 0.73 | 0.30 |
| 10-18 03:33 | +10 stop | BTC | DOWN | 0.62 | 0.47 | -1.85 |
| 10-18 03:33 | +10 stop | NEAR | UP | 0.45 | 0.28 | -2.03 |
| 10-18 03:33 | +10 stop | XRP | UP | 0.60 | 0.72 | 0.88 |
| 10-18 03:33 | +5 | HYPE | DOWN | 0.53 | 0.60 | 0.35 |
| 10-18 03:32 | +10 stop | BNB | DOWN | 0.56 | 0.28 | -3.13 |
| 10-18 03:32 | +20 | BNB | DOWN | 0.56 | yes | -5.78 |
| 10-18 03:32 | +15 | BNB | DOWN | 0.56 | yes | -5.78 |
| 10-18 03:32 | +10 | BNB | DOWN | 0.56 | yes | -5.78 |
| 10-18 03:32 | +5 | BNB | DOWN | 0.57 | yes | -5.88 |
| 10-18 03:32 | +10 stop | HYPE | DOWN | 0.61 | 0.39 | -2.54 |
| 10-18 03:32 | +20 | HYPE | DOWN | 0.61 | yes | -6.27 |
| 10-18 03:32 | +15 | HYPE | DOWN | 0.61 | yes | -6.27 |
| 10-18 03:32 | +10 | HYPE | DOWN | 0.61 | yes | -6.27 |
