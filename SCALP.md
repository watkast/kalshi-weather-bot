# Range-Scalp Bot

*Updated Sun Oct 04 09:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2073 | 1788 | 285 (3) | 0 | $-698.41 | -5.3% |
| **+10¢** | 1613 | 1297 | 316 (4) | 0 | $-507.24 | -5.0% |
| **+15¢** | 1357 | 1022 | 335 (5) | 1 | $-431.26 | -5.0% |
| **+20¢** | 1197 | 845 | 352 (7) | 1 | $-385.83 | -5.1% |
| **+10¢ (15¢ stop)** | 2578 | 2577 | 1 (1) | 0 | $-984.05 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 09:30 | +10 stop | XRP | UP | 0.43 | 0.54 | 0.74 |
| 10-04 09:30 | +20 | XRP | UP | 0.43 | open |  |
| 10-04 09:30 | +15 | XRP | UP | 0.44 | open |  |
| 10-04 09:30 | +10 | XRP | UP | 0.44 | 0.54 | 0.64 |
| 10-04 09:30 | +5 | XRP | UP | 0.45 | 0.54 | 0.54 |
| 10-04 09:23 | +10 stop | ZEC | UP | 0.61 | 0.77 | 1.30 |
| 10-04 09:21 | +10 stop | HYPE | UP | 0.62 | 0.76 | 1.10 |
| 10-04 09:21 | +5 | ZEC | DOWN | 0.69 | yes | -7.05 |
| 10-04 09:21 | +10 stop | HYPE | DOWN | 0.36 | 0.68 | 2.87 |
| 10-04 09:20 | +10 stop | XRP | UP | 0.68 | 0.82 | 1.14 |
| 10-04 09:20 | +20 | XRP | UP | 0.68 | 0.90 | 2.02 |
| 10-04 09:20 | +15 | XRP | UP | 0.68 | 0.85 | 1.46 |
| 10-04 09:20 | +10 | XRP | UP | 0.68 | 0.82 | 1.14 |
| 10-04 09:20 | +5 | XRP | UP | 0.68 | 0.77 | 0.62 |
| 10-04 09:20 | +10 stop | NEAR | UP | 0.49 | 0.61 | 0.85 |
| 10-04 09:20 | +10 stop | SOL | UP | 0.65 | 0.77 | 0.91 |
| 10-04 09:20 | +5 | ZEC | DOWN | 0.49 | 0.56 | 0.34 |
| 10-04 09:19 | +10 stop | SOL | UP | 0.53 | 0.65 | 0.85 |
| 10-04 09:19 | +5 | ETH | UP | 0.66 | 0.73 | 0.40 |
| 10-04 09:18 | +10 stop | DOGE | UP | 0.61 | 0.80 | 1.61 |
| 10-04 09:18 | +10 stop | NEAR | DOWN | 0.64 | 0.43 | -2.45 |
| 10-04 09:18 | +5 | DOGE | UP | 0.60 | 0.70 | 0.68 |
| 10-04 09:18 | +10 stop | ETH | UP | 0.62 | 0.73 | 0.79 |
| 10-04 09:18 | +20 | ETH | UP | 0.59 | 0.84 | 2.23 |
| 10-04 09:18 | +15 | ETH | UP | 0.59 | 0.74 | 1.19 |
| 10-04 09:18 | +10 | ETH | UP | 0.59 | 0.70 | 0.78 |
| 10-04 09:18 | +5 | ETH | UP | 0.59 | 0.68 | 0.57 |
| 10-04 09:18 | +5 | DOGE | DOWN | 0.61 | 0.68 | 0.37 |
| 10-04 09:17 | +5 | XRP | UP | 0.61 | 0.74 | 0.98 |
| 10-04 09:17 | +10 stop | HYPE | DOWN | 0.63 | 0.76 | 1.00 |
| 10-04 09:17 | +10 stop | SOL | DOWN | 0.61 | 0.40 | -2.44 |
| 10-04 09:17 | +20 | SOL | DOWN | 0.61 | yes | -6.27 |
| 10-04 09:17 | +15 | SOL | DOWN | 0.61 | yes | -6.27 |
| 10-04 09:17 | +10 | SOL | DOWN | 0.61 | yes | -6.27 |
| 10-04 09:17 | +5 | SOL | DOWN | 0.61 | yes | -6.27 |
| 10-04 09:17 | +5 | BTC | UP | 0.67 | 0.72 | 0.19 |
| 10-04 09:17 | +10 stop | NEAR | UP | 0.70 | 0.51 | -2.22 |
| 10-04 09:17 | +20 | NEAR | UP | 0.70 | 0.91 | 1.89 |
| 10-04 09:17 | +15 | NEAR | UP | 0.70 | 0.86 | 1.37 |
| 10-04 09:17 | +10 | NEAR | UP | 0.70 | 0.83 | 1.06 |
