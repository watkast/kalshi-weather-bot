# Range-Scalp Bot

*Updated Wed Oct 07 00:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5685 | 4922 | 763 (9) | 0 | $-1777.76 | -5.0% |
| **+10¢** | 4332 | 3434 | 898 (15) | 1 | $-1707.18 | -6.3% |
| **+15¢** | 3635 | 2683 | 952 (19) | 1 | $-1501.62 | -6.6% |
| **+20¢** | 3247 | 2256 | 991 (26) | 1 | $-1241.66 | -6.1% |
| **+10¢ (15¢ stop)** | 6919 | 6904 | 15 (9) | 0 | $-2499.97 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 00:13 | +10 stop | HYPE | UP | 0.45 | 0.56 | 0.74 |
| 10-07 00:13 | +20 | HYPE | UP | 0.47 | open |  |
| 10-07 00:13 | +15 | HYPE | UP | 0.48 | open |  |
| 10-07 00:13 | +10 | HYPE | UP | 0.49 | open |  |
| 10-07 00:13 | +5 | HYPE | UP | 0.47 | 0.56 | 0.54 |
| 10-07 00:11 | +10 stop | ZEC | DOWN | 0.71 | 0.89 | 1.58 |
| 10-07 00:11 | +20 | ZEC | DOWN | 0.71 | 0.95 | 2.26 |
| 10-07 00:11 | +15 | ZEC | DOWN | 0.71 | 0.89 | 1.58 |
| 10-07 00:11 | +10 | ZEC | DOWN | 0.71 | 0.89 | 1.58 |
| 10-07 00:11 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-07 00:10 | +10 stop | HYPE | DOWN | 0.60 | 0.79 | 1.61 |
| 10-07 00:10 | +20 | HYPE | DOWN | 0.60 | 0.91 | 2.85 |
| 10-07 00:10 | +15 | HYPE | DOWN | 0.60 | 0.79 | 1.61 |
| 10-07 00:10 | +10 | HYPE | DOWN | 0.60 | 0.79 | 1.61 |
| 10-07 00:10 | +5 | HYPE | DOWN | 0.60 | 0.79 | 1.61 |
| 10-07 00:10 | +10 stop | ETH | UP | 0.67 | 0.79 | 0.92 |
| 10-07 00:10 | +20 | ETH | UP | 0.67 | 0.88 | 1.86 |
| 10-07 00:10 | +15 | ETH | UP | 0.68 | 0.88 | 1.76 |
| 10-07 00:10 | +10 | ETH | UP | 0.67 | 0.79 | 0.92 |
| 10-07 00:10 | +5 | ETH | UP | 0.67 | 0.79 | 0.92 |
| 10-07 00:10 | +10 stop | BTC | UP | 0.71 | 0.82 | 0.84 |
| 10-07 00:10 | +10 stop | ETH | DOWN | 0.33 | 0.68 | 3.18 |
| 10-07 00:10 | +20 | ETH | DOWN | 0.33 | 0.68 | 3.18 |
| 10-07 00:10 | +15 | ETH | DOWN | 0.33 | 0.68 | 3.18 |
| 10-07 00:10 | +10 | ETH | DOWN | 0.33 | 0.68 | 3.18 |
| 10-07 00:10 | +5 | ETH | DOWN | 0.33 | 0.68 | 3.18 |
| 10-07 00:08 | +5 | BTC | DOWN | 0.65 | yes | -6.66 |
| 10-07 00:08 | +10 stop | XRP | DOWN | 0.63 | 0.47 | -1.94 |
| 10-07 00:08 | +5 | XRP | DOWN | 0.63 | yes | -6.46 |
| 10-07 00:06 | +5 | BTC | DOWN | 0.62 | 0.68 | 0.27 |
| 10-07 00:06 | +10 stop | NEAR | DOWN | 0.59 | 0.38 | -2.44 |
| 10-07 00:05 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 10-07 00:04 | +10 stop | HYPE | DOWN | 0.69 | 0.81 | 0.90 |
| 10-07 00:04 | +10 | HYPE | DOWN | 0.69 | 0.81 | 0.90 |
| 10-07 00:04 | +5 | HYPE | DOWN | 0.68 | 0.76 | 0.51 |
| 10-07 00:04 | +5 | XRP | DOWN | 0.67 | 0.74 | 0.40 |
| 10-07 00:04 | +10 stop | NEAR | UP | 0.62 | 0.44 | -2.15 |
| 10-07 00:02 | +10 stop | NEAR | DOWN | 0.62 | 0.34 | -3.13 |
| 10-07 00:02 | +20 | NEAR | DOWN | 0.62 | yes | -6.37 |
| 10-07 00:02 | +15 | NEAR | DOWN | 0.62 | yes | -6.36 |
