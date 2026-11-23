# Range-Scalp Bot

*Updated Mon Nov 23 08:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69689 | 60811 | 8878 (146) | 3 | $-18741.88 | -4.3% |
| **+10¢** | 52001 | 41630 | 10371 (189) | 3 | $-17422.81 | -5.3% |
| **+15¢** | 43569 | 32396 | 11173 (244) | 4 | $-15580.55 | -5.7% |
| **+20¢** | 38797 | 27045 | 11752 (309) | 7 | $-13908.41 | -5.7% |
| **+10¢ (15¢ stop)** | 84854 | 84664 | 190 (118) | 0 | $-31190.77 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 08:28 | +10 stop | BNB | UP | 0.46 | 0.66 | 1.67 |
| 11-23 08:28 | +10 | BNB | UP | 0.44 | 0.66 | 1.86 |
| 11-23 08:28 | +5 | BNB | UP | 0.44 | 0.66 | 1.86 |
| 11-23 08:28 | +10 stop | BTC | DOWN | 0.29 | 0.57 | 2.47 |
| 11-23 08:26 | +10 stop | BNB | DOWN | 0.65 | 0.77 | 0.91 |
| 11-23 08:26 | +10 | BNB | DOWN | 0.65 | 0.77 | 0.91 |
| 11-23 08:26 | +5 | BNB | DOWN | 0.65 | 0.73 | 0.50 |
| 11-23 08:26 | +10 stop | DOGE | DOWN | 0.56 | 0.67 | 0.76 |
| 11-23 08:26 | +10 | DOGE | DOWN | 0.56 | 0.67 | 0.76 |
| 11-23 08:26 | +5 | DOGE | DOWN | 0.56 | 0.64 | 0.45 |
| 11-23 08:26 | +10 stop | HYPE | DOWN | 0.37 | 0.65 | 2.47 |
| 11-23 08:26 | +20 | HYPE | DOWN | 0.37 | 0.65 | 2.46 |
| 11-23 08:26 | +15 | HYPE | DOWN | 0.37 | 0.65 | 2.46 |
| 11-23 08:26 | +10 | HYPE | DOWN | 0.40 | 0.65 | 2.17 |
| 11-23 08:26 | +5 | HYPE | DOWN | 0.40 | 0.65 | 2.17 |
| 11-23 08:24 | +10 stop | ZEC | UP | 0.67 | 0.82 | 1.23 |
| 11-23 08:24 | +10 stop | SOL | UP | 0.65 | 0.76 | 0.81 |
| 11-23 08:24 | +5 | BNB | DOWN | 0.67 | 0.72 | 0.19 |
| 11-23 08:24 | +10 stop | NEAR | DOWN | 0.60 | 0.38 | -2.54 |
| 11-23 08:24 | +15 | NEAR | DOWN | 0.61 | 0.83 | 1.93 |
| 11-23 08:24 | +10 | NEAR | DOWN | 0.61 | 0.72 | 0.78 |
| 11-23 08:24 | +5 | NEAR | DOWN | 0.61 | 0.72 | 0.78 |
| 11-23 08:24 | +10 stop | XRP | DOWN | 0.71 | 0.46 | -2.82 |
| 11-23 08:24 | +10 | XRP | DOWN | 0.71 | open |  |
| 11-23 08:24 | +5 | XRP | DOWN | 0.70 | open |  |
| 11-23 08:23 | +10 stop | BTC | DOWN | 0.51 | 0.61 | 0.65 |
| 11-23 08:23 | +5 | SOL | DOWN | 0.65 | open |  |
| 11-23 08:23 | +10 stop | SOL | DOWN | 0.67 | 0.36 | -3.43 |
| 11-23 08:23 | +10 stop | ZEC | DOWN | 0.65 | 0.37 | -3.13 |
| 11-23 08:23 | +10 stop | ETH | UP | 0.48 | 0.77 | 2.59 |
| 11-23 08:23 | +10 | ETH | UP | 0.48 | 0.77 | 2.59 |
| 11-23 08:22 | +5 | ETH | UP | 0.70 | 0.77 | 0.42 |
| 11-23 08:22 | +10 stop | BTC | UP | 0.63 | 0.48 | -1.85 |
| 11-23 08:22 | +20 | BTC | UP | 0.63 | open |  |
| 11-23 08:22 | +15 | BTC | UP | 0.62 | 0.81 | 1.62 |
| 11-23 08:22 | +10 | BTC | UP | 0.61 | 0.72 | 0.78 |
| 11-23 08:22 | +5 | BTC | UP | 0.61 | 0.72 | 0.78 |
| 11-23 08:21 | +10 stop | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 11-23 08:21 | +10 | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 11-23 08:21 | +5 | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
