# Range-Scalp Bot

*Updated Mon Nov 23 21:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70140 | 61209 | 8931 (147) | 5 | $-18857.88 | -4.3% |
| **+10¢** | 52331 | 41901 | 10430 (190) | 5 | $-17497.83 | -5.3% |
| **+15¢** | 43850 | 32616 | 11234 (246) | 5 | $-15592.52 | -5.7% |
| **+20¢** | 39040 | 27218 | 11822 (311) | 5 | $-13955.09 | -5.7% |
| **+10¢ (15¢ stop)** | 85430 | 85234 | 196 (118) | 3 | $-31426.74 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 21:38 | +10 stop | BNB | DOWN | 0.67 | open |  |
| 11-23 21:38 | +10 stop | XRP | DOWN | 0.70 | open |  |
| 11-23 21:38 | +10 stop | HYPE | DOWN | 0.65 | open |  |
| 11-23 21:37 | +5 | NEAR | DOWN | 0.71 | 0.78 | 0.42 |
| 11-23 21:36 | +10 stop | SOL | UP | 0.69 | 0.53 | -1.93 |
| 11-23 21:36 | +10 | SOL | UP | 0.69 | open |  |
| 11-23 21:36 | +5 | SOL | UP | 0.69 | open |  |
| 11-23 21:36 | +10 stop | DOGE | UP | 0.61 | 0.38 | -2.64 |
| 11-23 21:36 | +15 | DOGE | UP | 0.61 | open |  |
| 11-23 21:36 | +10 | DOGE | UP | 0.61 | open |  |
| 11-23 21:36 | +5 | DOGE | UP | 0.61 | open |  |
| 11-23 21:36 | +10 stop | HYPE | UP | 0.53 | 0.36 | -2.05 |
| 11-23 21:36 | +10 | HYPE | UP | 0.53 | open |  |
| 11-23 21:36 | +5 | HYPE | UP | 0.53 | open |  |
| 11-23 21:36 | +5 | BNB | UP | 0.61 | open |  |
| 11-23 21:36 | +10 stop | BTC | DOWN | 0.63 | 0.78 | 1.20 |
| 11-23 21:36 | +10 stop | XRP | UP | 0.56 | 0.35 | -2.41 |
| 11-23 21:36 | +20 | XRP | UP | 0.55 | open |  |
| 11-23 21:36 | +15 | XRP | UP | 0.56 | open |  |
| 11-23 21:36 | +10 | XRP | UP | 0.55 | open |  |
| 11-23 21:36 | +5 | XRP | UP | 0.56 | open |  |
| 11-23 21:36 | +5 | BNB | UP | 0.58 | 0.66 | 0.46 |
| 11-23 21:36 | +5 | NEAR | DOWN | 0.55 | 0.62 | 0.31 |
| 11-23 21:36 | +10 stop | ETH | UP | 0.48 | 0.30 | -2.13 |
| 11-23 21:35 | +10 stop | BNB | UP | 0.67 | 0.38 | -3.23 |
| 11-23 21:35 | +10 stop | SOL | UP | 0.65 | 0.78 | 1.01 |
| 11-23 21:35 | +20 | SOL | UP | 0.65 | open |  |
| 11-23 21:35 | +15 | SOL | UP | 0.65 | open |  |
| 11-23 21:35 | +10 | SOL | UP | 0.65 | 0.78 | 1.01 |
| 11-23 21:35 | +5 | SOL | UP | 0.65 | 0.78 | 1.01 |
| 11-23 21:35 | +5 | ZEC | DOWN | 0.65 | 0.72 | 0.39 |
| 11-23 21:34 | +10 stop | XRP | UP | 0.62 | 0.73 | 0.79 |
| 11-23 21:34 | +15 | XRP | UP | 0.62 | 0.78 | 1.30 |
| 11-23 21:34 | +10 | XRP | UP | 0.61 | 0.73 | 0.89 |
| 11-23 21:34 | +5 | XRP | UP | 0.61 | 0.69 | 0.48 |
| 11-23 21:33 | +10 stop | BTC | DOWN | 0.64 | 0.48 | -1.95 |
| 11-23 21:33 | +10 | BTC | DOWN | 0.64 | 0.78 | 1.12 |
| 11-23 21:33 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-23 21:33 | +10 stop | BNB | DOWN | 0.60 | 0.39 | -2.44 |
| 11-23 21:33 | +10 stop | ETH | DOWN | 0.64 | 0.45 | -2.25 |
