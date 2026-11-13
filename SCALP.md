# Range-Scalp Bot

*Updated Fri Nov 13 09:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58082 | 50678 | 7404 (102) | 0 | $-15690.34 | -4.3% |
| **+10¢** | 43395 | 34740 | 8655 (134) | 1 | $-14649.47 | -5.4% |
| **+15¢** | 36382 | 27065 | 9317 (168) | 2 | $-13196.11 | -5.8% |
| **+20¢** | 32417 | 22636 | 9781 (219) | 2 | $-11561.92 | -5.7% |
| **+10¢ (15¢ stop)** | 70768 | 70639 | 129 (79) | 0 | $-26020.14 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 09:42 | +10 stop | ZEC | UP | 0.61 | 0.89 | 2.52 |
| 11-13 09:41 | +10 stop | ZEC | UP | 0.67 | 0.50 | -2.04 |
| 11-13 09:41 | +15 | ZEC | UP | 0.61 | 0.89 | 2.56 |
| 11-13 09:41 | +10 | ZEC | UP | 0.61 | 0.89 | 2.56 |
| 11-13 09:41 | +5 | ZEC | UP | 0.61 | 0.89 | 2.56 |
| 11-13 09:38 | +10 stop | NEAR | DOWN | 0.63 | 0.74 | 0.79 |
| 11-13 09:35 | +10 stop | NEAR | DOWN | 0.58 | 0.43 | -1.86 |
| 11-13 09:35 | +10 | NEAR | DOWN | 0.58 | 0.68 | 0.66 |
| 11-13 09:35 | +5 | NEAR | DOWN | 0.58 | 0.68 | 0.66 |
| 11-13 09:34 | +10 stop | ZEC | UP | 0.69 | 0.85 | 1.36 |
| 11-13 09:34 | +20 | ZEC | UP | 0.69 | 0.89 | 1.78 |
| 11-13 09:34 | +15 | ZEC | UP | 0.71 | 0.86 | 1.26 |
| 11-13 09:34 | +10 | ZEC | UP | 0.71 | 0.85 | 1.16 |
| 11-13 09:34 | +5 | ZEC | UP | 0.71 | 0.85 | 1.16 |
| 11-13 09:34 | +10 stop | NEAR | DOWN | 0.48 | 0.59 | 0.75 |
| 11-13 09:34 | +10 | NEAR | DOWN | 0.46 | 0.59 | 0.95 |
| 11-13 09:34 | +5 | NEAR | DOWN | 0.46 | 0.59 | 0.95 |
| 11-13 09:33 | +10 stop | ETH | UP | 0.68 | 0.81 | 1.03 |
| 11-13 09:33 | +20 | ETH | UP | 0.68 | 0.89 | 1.87 |
| 11-13 09:33 | +15 | ETH | UP | 0.68 | 0.83 | 1.24 |
| 11-13 09:33 | +10 | ETH | UP | 0.68 | 0.81 | 1.03 |
| 11-13 09:33 | +5 | ETH | UP | 0.68 | 0.75 | 0.40 |
| 11-13 09:33 | +5 | NEAR | UP | 0.65 | 0.76 | 0.81 |
| 11-13 09:31 | +10 stop | BTC | UP | 0.68 | 0.78 | 0.71 |
| 11-13 09:31 | +20 | BTC | UP | 0.68 | 0.88 | 1.76 |
| 11-13 09:31 | +15 | BTC | UP | 0.68 | 0.88 | 1.76 |
| 11-13 09:31 | +10 | BTC | UP | 0.68 | 0.78 | 0.71 |
| 11-13 09:31 | +5 | BTC | UP | 0.68 | 0.78 | 0.71 |
| 11-13 09:31 | +10 stop | NEAR | UP | 0.65 | 0.76 | 0.81 |
| 11-13 09:31 | +20 | NEAR | UP | 0.65 | open |  |
| 11-13 09:31 | +15 | NEAR | UP | 0.65 | open |  |
| 11-13 09:31 | +10 | NEAR | UP | 0.65 | 0.76 | 0.81 |
| 11-13 09:31 | +5 | NEAR | UP | 0.65 | 0.72 | 0.39 |
| 11-13 09:31 | +10 stop | HYPE | DOWN | 0.49 | 0.27 | -2.52 |
| 11-13 09:31 | +20 | HYPE | DOWN | 0.49 | open |  |
| 11-13 09:31 | +15 | HYPE | DOWN | 0.49 | open |  |
| 11-13 09:31 | +10 | HYPE | DOWN | 0.49 | open |  |
| 11-13 09:31 | +5 | HYPE | DOWN | 0.49 | 0.55 | 0.24 |
| 11-13 09:30 | +10 stop | SOL | UP | 0.65 | 0.75 | 0.70 |
| 11-13 09:30 | +20 | SOL | UP | 0.65 | 0.87 | 1.96 |
