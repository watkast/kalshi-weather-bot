# Range-Scalp Bot

*Updated Fri Nov 13 05:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57936 | 50543 | 7393 (101) | 3 | $-15706.43 | -4.3% |
| **+10¢** | 43285 | 34648 | 8637 (133) | 5 | $-14657.01 | -5.4% |
| **+15¢** | 36284 | 26986 | 9298 (167) | 5 | $-13214.08 | -5.8% |
| **+20¢** | 32321 | 22561 | 9760 (217) | 6 | $-11605.34 | -5.7% |
| **+10¢ (15¢ stop)** | 70612 | 70484 | 128 (78) | 1 | $-25991.62 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 05:42 | +5 | BTC | DOWN | 0.66 | open |  |
| 11-13 05:41 | +5 | BTC | DOWN | 0.56 | 0.63 | 0.35 |
| 11-13 05:41 | +5 | ETH | UP | 0.66 | 0.81 | 1.23 |
| 11-13 05:40 | +10 stop | BTC | DOWN | 0.55 | open |  |
| 11-13 05:40 | +20 | BTC | DOWN | 0.55 | open |  |
| 11-13 05:40 | +15 | BTC | DOWN | 0.55 | open |  |
| 11-13 05:40 | +10 | BTC | DOWN | 0.55 | open |  |
| 11-13 05:40 | +5 | BTC | DOWN | 0.55 | 0.64 | 0.55 |
| 11-13 05:40 | +10 stop | ETH | UP | 0.64 | 0.81 | 1.42 |
| 11-13 05:40 | +20 | ETH | UP | 0.64 | open |  |
| 11-13 05:40 | +15 | ETH | UP | 0.66 | 0.81 | 1.23 |
| 11-13 05:40 | +10 | ETH | UP | 0.67 | 0.81 | 1.13 |
| 11-13 05:40 | +5 | ETH | UP | 0.67 | 0.73 | 0.30 |
| 11-13 05:39 | +10 stop | XRP | UP | 0.67 | 0.81 | 1.18 |
| 11-13 05:38 | +5 | ZEC | UP | 0.67 | 0.80 | 0.98 |
| 11-13 05:38 | +10 stop | NEAR | UP | 0.64 | 0.81 | 1.42 |
| 11-13 05:38 | +5 | XRP | DOWN | 0.57 | open |  |
| 11-13 05:38 | +10 stop | XRP | DOWN | 0.50 | 0.34 | -1.94 |
| 11-13 05:38 | +10 stop | SOL | DOWN | 0.62 | 0.46 | -1.95 |
| 11-13 05:38 | +10 | HYPE | DOWN | 0.51 | open |  |
| 11-13 05:38 | +5 | HYPE | DOWN | 0.51 | 0.58 | 0.34 |
| 11-13 05:37 | +10 stop | HYPE | DOWN | 0.66 | 0.39 | -3.03 |
| 11-13 05:37 | +10 stop | NEAR | UP | 0.58 | 0.38 | -2.35 |
| 11-13 05:37 | +10 | NEAR | UP | 0.58 | 0.71 | 0.97 |
| 11-13 05:37 | +5 | NEAR | UP | 0.57 | 0.71 | 1.07 |
| 11-13 05:36 | +10 stop | XRP | UP | 0.55 | 0.38 | -2.06 |
| 11-13 05:36 | +10 stop | SOL | UP | 0.49 | 0.32 | -2.04 |
| 11-13 05:36 | +10 stop | ZEC | UP | 0.57 | 0.70 | 0.97 |
| 11-13 05:35 | +10 stop | SOL | DOWN | 0.60 | 0.36 | -2.74 |
| 11-13 05:35 | +10 stop | SOL | DOWN | 0.54 | 0.64 | 0.65 |
| 11-13 05:35 | +10 stop | DOGE | DOWN | 0.51 | 0.66 | 1.16 |
| 11-13 05:35 | +10 stop | HYPE | DOWN | 0.61 | 0.45 | -1.95 |
| 11-13 05:35 | +5 | HYPE | DOWN | 0.61 | 0.66 | 0.17 |
| 11-13 05:34 | +10 stop | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 11-13 05:34 | +10 | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 11-13 05:34 | +5 | NEAR | UP | 0.61 | 0.70 | 0.58 |
| 11-13 05:34 | +10 stop | XRP | UP | 0.46 | 0.62 | 1.25 |
| 11-13 05:34 | +10 stop | ZEC | UP | 0.59 | 0.41 | -2.14 |
| 11-13 05:34 | +5 | ZEC | UP | 0.59 | 0.64 | 0.16 |
| 11-13 05:34 | +10 stop | HYPE | UP | 0.54 | 0.37 | -2.04 |
