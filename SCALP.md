# Range-Scalp Bot

*Updated Tue Nov 03 15:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46146 | 40180 | 5966 (70) | 2 | $-13309.86 | -4.6% |
| **+10¢** | 34440 | 27528 | 6912 (92) | 4 | $-12187.09 | -5.6% |
| **+15¢** | 28827 | 21397 | 7430 (120) | 4 | $-11111.64 | -6.1% |
| **+20¢** | 25604 | 17818 | 7786 (157) | 7 | $-9865.81 | -6.1% |
| **+10¢ (15¢ stop)** | 56300 | 56211 | 89 (53) | 4 | $-21141.35 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 15:37 | +10 stop | NEAR | UP | 0.65 | open |  |
| 11-03 15:37 | +5 | NEAR | UP | 0.65 | open |  |
| 11-03 15:37 | +10 stop | ZEC | UP | 0.69 | open |  |
| 11-03 15:37 | +5 | ZEC | UP | 0.68 | 0.76 | 0.51 |
| 11-03 15:36 | +10 stop | HYPE | UP | 0.51 | open |  |
| 11-03 15:36 | +5 | HYPE | UP | 0.51 | 0.56 | 0.14 |
| 11-03 15:36 | +10 stop | NEAR | UP | 0.63 | 0.48 | -1.85 |
| 11-03 15:36 | +10 | NEAR | UP | 0.63 | open |  |
| 11-03 15:36 | +5 | NEAR | UP | 0.63 | 0.69 | 0.28 |
| 11-03 15:35 | +10 stop | NEAR | UP | 0.53 | 0.66 | 0.96 |
| 11-03 15:35 | +20 | NEAR | UP | 0.54 | open |  |
| 11-03 15:35 | +15 | NEAR | UP | 0.56 | open |  |
| 11-03 15:35 | +10 | NEAR | UP | 0.56 | 0.66 | 0.66 |
| 11-03 15:35 | +5 | NEAR | UP | 0.56 | 0.66 | 0.66 |
| 11-03 15:34 | +10 stop | ETH | UP | 0.68 | 0.81 | 1.03 |
| 11-03 15:34 | +10 stop | XRP | UP | 0.59 | 0.70 | 0.81 |
| 11-03 15:34 | +10 stop | BNB | UP | 0.66 | 0.83 | 1.44 |
| 11-03 15:33 | +10 stop | BTC | DOWN | 0.47 | open |  |
| 11-03 15:33 | +10 stop | ZEC | DOWN | 0.47 | 0.59 | 0.85 |
| 11-03 15:33 | +5 | BNB | UP | 0.65 | 0.73 | 0.50 |
| 11-03 15:33 | +10 stop | HYPE | UP | 0.54 | 0.65 | 0.73 |
| 11-03 15:32 | +10 stop | XRP | UP | 0.69 | 0.53 | -1.93 |
| 11-03 15:32 | +20 | XRP | UP | 0.68 | 0.92 | 2.14 |
| 11-03 15:32 | +15 | XRP | UP | 0.68 | 0.83 | 1.24 |
| 11-03 15:32 | +10 | XRP | UP | 0.68 | 0.83 | 1.24 |
| 11-03 15:32 | +5 | XRP | UP | 0.68 | 0.83 | 1.24 |
| 11-03 15:31 | +10 | BNB | UP | 0.67 | 0.83 | 1.34 |
| 11-03 15:31 | +5 | BNB | UP | 0.67 | 0.72 | 0.19 |
| 11-03 15:31 | +10 stop | DOGE | UP | 0.71 | 0.53 | -2.13 |
| 11-03 15:31 | +20 | DOGE | UP | 0.71 | open |  |
| 11-03 15:31 | +15 | DOGE | UP | 0.71 | 0.87 | 1.37 |
| 11-03 15:31 | +10 | DOGE | UP | 0.70 | 0.83 | 1.05 |
| 11-03 15:31 | +5 | DOGE | UP | 0.70 | 0.75 | 0.21 |
| 11-03 15:31 | +10 stop | ETH | UP | 0.68 | 0.53 | -1.84 |
| 11-03 15:31 | +20 | ETH | UP | 0.68 | open |  |
| 11-03 15:31 | +15 | ETH | UP | 0.68 | 0.83 | 1.24 |
| 11-03 15:31 | +10 | ETH | UP | 0.68 | 0.81 | 1.03 |
| 11-03 15:31 | +5 | ETH | UP | 0.68 | 0.77 | 0.61 |
| 11-03 15:31 | +10 stop | BNB | UP | 0.71 | 0.56 | -1.83 |
| 11-03 15:31 | +20 | BNB | UP | 0.71 | open |  |
