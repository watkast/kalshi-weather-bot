# Range-Scalp Bot

*Updated Thu Oct 08 21:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8026 | 6951 | 1075 (13) | 4 | $-2549.52 | -5.0% |
| **+10¢** | 6077 | 4803 | 1274 (25) | 5 | $-2526.49 | -6.6% |
| **+15¢** | 5113 | 3774 | 1339 (37) | 5 | $-2035.47 | -6.3% |
| **+20¢** | 4566 | 3177 | 1389 (45) | 5 | $-1616.81 | -5.6% |
| **+10¢ (15¢ stop)** | 9753 | 9723 | 30 (19) | 1 | $-3596.52 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 21:39 | +5 | HYPE | UP | 0.68 | 0.83 | 1.24 |
| 10-08 21:39 | +10 stop | XRP | DOWN | 0.65 | open |  |
| 10-08 21:37 | +5 | HYPE | UP | 0.63 | 0.69 | 0.28 |
| 10-08 21:36 | +5 | HYPE | UP | 0.52 | 0.63 | 0.75 |
| 10-08 21:36 | +10 stop | BTC | UP | 0.61 | 0.74 | 0.99 |
| 10-08 21:36 | +10 stop | ETH | UP | 0.55 | 0.73 | 1.48 |
| 10-08 21:36 | +10 stop | HYPE | UP | 0.58 | 0.69 | 0.81 |
| 10-08 21:36 | +5 | HYPE | UP | 0.58 | 0.65 | 0.40 |
| 10-08 21:35 | +10 stop | SOL | UP | 0.71 | 0.83 | 0.95 |
| 10-08 21:35 | +10 stop | XRP | DOWN | 0.66 | 0.46 | -2.34 |
| 10-08 21:35 | +15 | XRP | DOWN | 0.66 | open |  |
| 10-08 21:35 | +10 | XRP | DOWN | 0.66 | open |  |
| 10-08 21:35 | +5 | XRP | DOWN | 0.66 | open |  |
| 10-08 21:35 | +10 stop | ZEC | UP | 0.65 | 0.79 | 1.12 |
| 10-08 21:34 | +5 | BTC | DOWN | 0.58 | open |  |
| 10-08 21:34 | +10 stop | SOL | DOWN | 0.66 | 0.36 | -3.33 |
| 10-08 21:34 | +10 | SOL | DOWN | 0.66 | open |  |
| 10-08 21:34 | +5 | SOL | DOWN | 0.66 | open |  |
| 10-08 21:34 | +10 stop | BNB | UP | 0.52 | 0.62 | 0.65 |
| 10-08 21:34 | +20 | BNB | UP | 0.52 | 0.73 | 1.78 |
| 10-08 21:34 | +15 | BNB | UP | 0.52 | 0.70 | 1.47 |
| 10-08 21:34 | +10 | BNB | UP | 0.54 | 0.70 | 1.27 |
| 10-08 21:34 | +5 | BNB | UP | 0.55 | 0.62 | 0.35 |
| 10-08 21:33 | +5 | ETH | DOWN | 0.69 | open |  |
| 10-08 21:33 | +5 | SOL | DOWN | 0.62 | 0.68 | 0.27 |
| 10-08 21:33 | +5 | XRP | DOWN | 0.67 | 0.74 | 0.40 |
| 10-08 21:33 | +10 stop | BTC | DOWN | 0.54 | 0.36 | -2.15 |
| 10-08 21:33 | +20 | BTC | DOWN | 0.54 | open |  |
| 10-08 21:33 | +15 | BTC | DOWN | 0.54 | open |  |
| 10-08 21:33 | +10 | BTC | DOWN | 0.54 | open |  |
| 10-08 21:33 | +5 | BTC | DOWN | 0.54 | 0.59 | 0.15 |
| 10-08 21:31 | +10 stop | ETH | DOWN | 0.61 | 0.39 | -2.54 |
| 10-08 21:31 | +20 | ETH | DOWN | 0.61 | open |  |
| 10-08 21:31 | +15 | ETH | DOWN | 0.61 | open |  |
| 10-08 21:31 | +10 | ETH | DOWN | 0.61 | open |  |
| 10-08 21:31 | +5 | ETH | DOWN | 0.61 | 0.67 | 0.27 |
| 10-08 21:31 | +10 stop | NEAR | UP | 0.59 | 0.70 | 0.78 |
| 10-08 21:31 | +20 | NEAR | UP | 0.59 | 0.79 | 1.71 |
| 10-08 21:31 | +15 | NEAR | UP | 0.59 | 0.77 | 1.50 |
| 10-08 21:31 | +10 | NEAR | UP | 0.60 | 0.70 | 0.69 |
