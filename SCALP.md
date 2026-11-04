# Range-Scalp Bot

*Updated Wed Nov 04 11:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47179 | 41089 | 6090 (72) | 4 | $-13550.95 | -4.6% |
| **+10¢** | 35242 | 28177 | 7065 (97) | 4 | $-12376.07 | -5.6% |
| **+15¢** | 29509 | 21901 | 7608 (125) | 4 | $-11353.36 | -6.1% |
| **+20¢** | 26213 | 18244 | 7969 (165) | 5 | $-10020.91 | -6.1% |
| **+10¢ (15¢ stop)** | 57499 | 57406 | 93 (56) | 0 | $-21433.29 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 11:25 | +10 stop | HYPE | DOWN | 0.65 | 0.78 | 0.98 |
| 11-04 11:24 | +10 stop | NEAR | DOWN | 0.67 | 0.79 | 0.92 |
| 11-04 11:24 | +15 | NEAR | DOWN | 0.67 | 0.84 | 1.44 |
| 11-04 11:24 | +10 | NEAR | DOWN | 0.67 | 0.79 | 0.92 |
| 11-04 11:24 | +5 | NEAR | DOWN | 0.67 | 0.79 | 0.92 |
| 11-04 11:24 | +10 stop | HYPE | DOWN | 0.69 | 0.54 | -1.88 |
| 11-04 11:24 | +10 stop | BNB | DOWN | 0.70 | 0.47 | -2.63 |
| 11-04 11:24 | +10 | BNB | DOWN | 0.70 | open |  |
| 11-04 11:24 | +5 | BNB | DOWN | 0.70 | open |  |
| 11-04 11:24 | +10 stop | DOGE | DOWN | 0.69 | 0.51 | -2.13 |
| 11-04 11:23 | +10 stop | ETH | UP | 0.71 | 0.84 | 1.05 |
| 11-04 11:23 | +20 | ETH | UP | 0.70 | open |  |
| 11-04 11:23 | +15 | ETH | UP | 0.70 | 0.87 | 1.45 |
| 11-04 11:23 | +10 | ETH | UP | 0.70 | 0.84 | 1.13 |
| 11-04 11:23 | +5 | ETH | UP | 0.70 | 0.84 | 1.13 |
| 11-04 11:23 | +5 | BTC | DOWN | 0.51 | 0.64 | 0.95 |
| 11-04 11:23 | +5 | SOL | UP | 0.55 | 0.61 | 0.25 |
| 11-04 11:22 | +10 stop | BTC | UP | 0.50 | 0.35 | -1.84 |
| 11-04 11:22 | +15 | BTC | UP | 0.50 | 0.73 | 1.98 |
| 11-04 11:22 | +5 | BTC | UP | 0.50 | 0.55 | 0.14 |
| 11-04 11:22 | +10 stop | BNB | DOWN | 0.61 | 0.73 | 0.89 |
| 11-04 11:22 | +10 stop | NEAR | DOWN | 0.62 | 0.83 | 1.83 |
| 11-04 11:22 | +10 stop | DOGE | DOWN | 0.61 | 0.42 | -2.25 |
| 11-04 11:22 | +10 stop | SOL | UP | 0.64 | 0.48 | -1.95 |
| 11-04 11:22 | +20 | SOL | UP | 0.64 | 0.90 | 2.39 |
| 11-04 11:22 | +10 | SOL | UP | 0.64 | 0.77 | 1.00 |
| 11-04 11:22 | +5 | SOL | UP | 0.64 | 0.73 | 0.59 |
| 11-04 11:21 | +5 | HYPE | UP | 0.59 | open |  |
| 11-04 11:20 | +10 stop | ZEC | DOWN | 0.66 | 0.76 | 0.71 |
| 11-04 11:20 | +10 | ZEC | DOWN | 0.66 | 0.76 | 0.71 |
| 11-04 11:20 | +10 stop | XRP | DOWN | 0.70 | 0.85 | 1.31 |
| 11-04 11:20 | +5 | ZEC | DOWN | 0.64 | 0.73 | 0.59 |
| 11-04 11:20 | +5 | BTC | UP | 0.58 | 0.64 | 0.25 |
| 11-04 11:20 | +5 | ETH | UP | 0.53 | 0.59 | 0.25 |
| 11-04 11:19 | +5 | BTC | UP | 0.62 | 0.67 | 0.17 |
| 11-04 11:19 | +10 stop | NEAR | UP | 0.56 | 0.39 | -2.04 |
| 11-04 11:19 | +5 | ZEC | DOWN | 0.53 | 0.58 | 0.14 |
| 11-04 11:19 | +10 stop | DOGE | UP | 0.67 | 0.50 | -2.04 |
| 11-04 11:19 | +10 | DOGE | UP | 0.67 | open |  |
| 11-04 11:18 | +5 | XRP | UP | 0.56 | open |  |
