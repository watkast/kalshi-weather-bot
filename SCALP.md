# Range-Scalp Bot

*Updated Sun Oct 04 08:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 1991 | 1721 | 270 (3) | 2 | $-637.50 | -5.0% |
| **+10¢** | 1550 | 1250 | 300 (4) | 2 | $-452.10 | -4.6% |
| **+15¢** | 1303 | 985 | 318 (5) | 2 | $-377.63 | -4.6% |
| **+20¢** | 1152 | 816 | 336 (7) | 2 | $-348.04 | -4.8% |
| **+10¢ (15¢ stop)** | 2485 | 2484 | 1 (1) | 0 | $-968.32 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 08:08 | +10 stop | BTC | UP | 0.65 | 0.49 | -1.94 |
| 10-04 08:08 | +15 | BTC | UP | 0.65 | 0.91 | 2.32 |
| 10-04 08:08 | +10 | BTC | UP | 0.65 | 0.91 | 2.32 |
| 10-04 08:08 | +5 | BTC | UP | 0.65 | 0.91 | 2.32 |
| 10-04 08:06 | +10 stop | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 10-04 08:06 | +10 | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 10-04 08:06 | +5 | ETH | DOWN | 0.66 | 0.72 | 0.29 |
| 10-04 08:06 | +10 stop | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 10-04 08:06 | +5 | NEAR | UP | 0.68 | 0.74 | 0.30 |
| 10-04 08:06 | +5 | XRP | DOWN | 0.56 | 0.68 | 0.86 |
| 10-04 08:05 | +15 | XRP | DOWN | 0.51 | 0.68 | 1.36 |
| 10-04 08:05 | +5 | XRP | DOWN | 0.51 | 0.59 | 0.45 |
| 10-04 08:04 | +10 stop | SOL | UP | 0.51 | 0.35 | -1.94 |
| 10-04 08:04 | +5 | SOL | UP | 0.51 | open |  |
| 10-04 08:04 | +10 stop | NEAR | UP | 0.71 | 0.87 | 1.38 |
| 10-04 08:04 | +20 | NEAR | UP | 0.71 | 0.92 | 1.90 |
| 10-04 08:04 | +15 | NEAR | UP | 0.71 | 0.87 | 1.38 |
| 10-04 08:04 | +10 | NEAR | UP | 0.71 | 0.87 | 1.38 |
| 10-04 08:04 | +5 | NEAR | UP | 0.71 | 0.78 | 0.43 |
| 10-04 08:04 | +10 stop | BTC | UP | 0.70 | 0.86 | 1.36 |
| 10-04 08:04 | +10 | BTC | UP | 0.70 | 0.86 | 1.36 |
| 10-04 08:04 | +5 | BTC | UP | 0.70 | 0.77 | 0.42 |
| 10-04 08:04 | +10 stop | XRP | DOWN | 0.53 | 0.68 | 1.16 |
| 10-04 08:04 | +10 | XRP | DOWN | 0.53 | 0.68 | 1.16 |
| 10-04 08:04 | +5 | XRP | DOWN | 0.53 | 0.62 | 0.55 |
| 10-04 08:03 | +10 stop | XRP | UP | 0.47 | 0.66 | 1.56 |
| 10-04 08:03 | +10 | XRP | UP | 0.47 | 0.66 | 1.56 |
| 10-04 08:03 | +5 | XRP | UP | 0.47 | 0.66 | 1.56 |
| 10-04 08:03 | +10 stop | HYPE | UP | 0.60 | 0.76 | 1.30 |
| 10-04 08:03 | +20 | HYPE | UP | 0.60 | 0.86 | 2.34 |
| 10-04 08:03 | +15 | HYPE | UP | 0.60 | 0.76 | 1.30 |
| 10-04 08:03 | +10 | HYPE | UP | 0.60 | 0.76 | 1.30 |
| 10-04 08:03 | +5 | HYPE | UP | 0.60 | 0.67 | 0.37 |
| 10-04 08:02 | +10 stop | ZEC | DOWN | 0.70 | 0.55 | -1.83 |
| 10-04 08:02 | +10 stop | SOL | UP | 0.70 | 0.52 | -2.13 |
| 10-04 08:02 | +20 | SOL | UP | 0.69 | open |  |
| 10-04 08:02 | +15 | SOL | UP | 0.69 | open |  |
| 10-04 08:02 | +10 | SOL | UP | 0.69 | open |  |
| 10-04 08:02 | +5 | SOL | UP | 0.69 | 0.75 | 0.31 |
| 10-04 08:02 | +10 stop | ETH | DOWN | 0.64 | 0.74 | 0.69 |
