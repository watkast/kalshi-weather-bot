# Range-Scalp Bot

*Updated Tue Oct 06 19:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5339 | 4625 | 714 (7) | 3 | $-1671.75 | -5.0% |
| **+10¢** | 4074 | 3238 | 836 (12) | 3 | $-1577.78 | -6.2% |
| **+15¢** | 3416 | 2531 | 885 (15) | 3 | $-1372.29 | -6.4% |
| **+20¢** | 3060 | 2141 | 919 (22) | 5 | $-1089.01 | -5.7% |
| **+10¢ (15¢ stop)** | 6519 | 6504 | 15 (9) | 1 | $-2371.66 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 19:08 | +5 | BTC | DOWN | 0.66 | open |  |
| 10-06 19:08 | +10 stop | ZEC | DOWN | 0.68 | open |  |
| 10-06 19:08 | +10 stop | BTC | UP | 0.53 | 0.35 | -2.14 |
| 10-06 19:08 | +20 | BTC | UP | 0.53 | open |  |
| 10-06 19:08 | +15 | BTC | UP | 0.53 | open |  |
| 10-06 19:08 | +10 | BTC | UP | 0.53 | open |  |
| 10-06 19:08 | +5 | BTC | UP | 0.53 | 0.59 | 0.25 |
| 10-06 19:08 | +5 | ETH | DOWN | 0.62 | 0.77 | 1.20 |
| 10-06 19:07 | +10 stop | ZEC | DOWN | 0.46 | 0.59 | 0.95 |
| 10-06 19:07 | +5 | ETH | DOWN | 0.63 | 0.68 | 0.17 |
| 10-06 19:07 | +10 stop | ETH | DOWN | 0.68 | 0.87 | 1.66 |
| 10-06 19:06 | +10 stop | ZEC | UP | 0.69 | 0.43 | -2.93 |
| 10-06 19:06 | +10 stop | ETH | UP | 0.67 | 0.44 | -2.64 |
| 10-06 19:06 | +10 stop | SOL | UP | 0.71 | 0.48 | -2.63 |
| 10-06 19:05 | +10 stop | BTC | UP | 0.66 | 0.76 | 0.71 |
| 10-06 19:05 | +10 | BTC | UP | 0.66 | 0.76 | 0.71 |
| 10-06 19:05 | +5 | BTC | UP | 0.65 | 0.75 | 0.70 |
| 10-06 19:04 | +5 | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 10-06 19:04 | +10 stop | HYPE | DOWN | 0.64 | 0.88 | 2.15 |
| 10-06 19:04 | +10 stop | BTC | UP | 0.55 | 0.65 | 0.66 |
| 10-06 19:04 | +20 | BTC | UP | 0.55 | 0.75 | 1.68 |
| 10-06 19:04 | +15 | BTC | UP | 0.55 | 0.75 | 1.68 |
| 10-06 19:04 | +10 | BTC | UP | 0.55 | 0.65 | 0.66 |
| 10-06 19:04 | +5 | BTC | UP | 0.55 | 0.65 | 0.66 |
| 10-06 19:03 | +10 stop | ZEC | UP | 0.56 | 0.66 | 0.66 |
| 10-06 19:03 | +10 stop | SOL | DOWN | 0.68 | 0.49 | -2.24 |
| 10-06 19:03 | +20 | SOL | DOWN | 0.68 | open |  |
| 10-06 19:03 | +15 | SOL | DOWN | 0.68 | 0.84 | 1.34 |
| 10-06 19:03 | +10 | SOL | DOWN | 0.68 | 0.82 | 1.13 |
| 10-06 19:03 | +5 | SOL | DOWN | 0.68 | 0.73 | 0.20 |
| 10-06 19:02 | +5 | HYPE | UP | 0.47 | open |  |
| 10-06 19:02 | +10 stop | NEAR | DOWN | 0.71 | 0.51 | -2.33 |
| 10-06 19:02 | +20 | NEAR | DOWN | 0.71 | open |  |
| 10-06 19:02 | +15 | NEAR | DOWN | 0.71 | 0.87 | 1.37 |
| 10-06 19:02 | +10 | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-06 19:02 | +5 | NEAR | DOWN | 0.71 | 0.78 | 0.43 |
| 10-06 19:02 | +10 stop | ETH | DOWN | 0.61 | 0.45 | -1.95 |
| 10-06 19:02 | +20 | ETH | DOWN | 0.61 | 0.87 | 2.35 |
| 10-06 19:02 | +15 | ETH | DOWN | 0.61 | 0.77 | 1.30 |
| 10-06 19:02 | +10 | ETH | DOWN | 0.61 | 0.77 | 1.30 |
