# Range-Scalp Bot

*Updated Fri Oct 16 16:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19502 | 16944 | 2558 (29) | 2 | $-5900.08 | -4.8% |
| **+10¢** | 14699 | 11744 | 2955 (41) | 2 | $-5312.70 | -5.7% |
| **+15¢** | 12302 | 9124 | 3178 (60) | 4 | $-4805.77 | -6.2% |
| **+20¢** | 10914 | 7584 | 3330 (79) | 5 | $-4273.53 | -6.2% |
| **+10¢ (15¢ stop)** | 23978 | 23928 | 50 (29) | 1 | $-9181.99 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 16:21 | +10 stop | BTC | UP | 0.70 | open |  |
| 10-16 16:21 | +5 | DOGE | UP | 0.68 | 0.74 | 0.30 |
| 10-16 16:21 | +10 stop | SOL | UP | 0.56 | 0.75 | 1.58 |
| 10-16 16:21 | +10 stop | BTC | UP | 0.53 | 0.69 | 1.27 |
| 10-16 16:21 | +10 stop | XRP | UP | 0.62 | 0.74 | 0.89 |
| 10-16 16:21 | +5 | XRP | UP | 0.62 | 0.74 | 0.89 |
| 10-16 16:20 | +10 stop | ETH | UP | 0.71 | 0.85 | 1.16 |
| 10-16 16:20 | +10 stop | DOGE | UP | 0.68 | 0.81 | 1.03 |
| 10-16 16:20 | +10 stop | HYPE | UP | 0.62 | 0.74 | 0.89 |
| 10-16 16:20 | +10 stop | BNB | UP | 0.64 | 0.81 | 1.42 |
| 10-16 16:19 | +5 | NEAR | UP | 0.68 | 0.77 | 0.61 |
| 10-16 16:19 | +5 | BTC | DOWN | 0.68 | open |  |
| 10-16 16:19 | +10 stop | XRP | DOWN | 0.57 | 0.40 | -2.05 |
| 10-16 16:18 | +10 stop | ETH | DOWN | 0.55 | 0.35 | -2.34 |
| 10-16 16:18 | +10 stop | SOL | DOWN | 0.63 | 0.38 | -2.84 |
| 10-16 16:18 | +10 stop | BTC | DOWN | 0.63 | 0.42 | -2.45 |
| 10-16 16:18 | +20 | BTC | DOWN | 0.63 | open |  |
| 10-16 16:18 | +15 | BTC | DOWN | 0.63 | open |  |
| 10-16 16:18 | +10 | BTC | DOWN | 0.63 | open |  |
| 10-16 16:18 | +5 | BTC | DOWN | 0.63 | 0.71 | 0.48 |
| 10-16 16:17 | +5 | DOGE | UP | 0.61 | 0.66 | 0.17 |
| 10-16 16:17 | +5 | NEAR | UP | 0.60 | 0.70 | 0.68 |
| 10-16 16:17 | +5 | BNB | UP | 0.62 | 0.70 | 0.49 |
| 10-16 16:17 | +5 | XRP | UP | 0.51 | 0.59 | 0.45 |
| 10-16 16:17 | +10 stop | ZEC | DOWN | 0.63 | 0.77 | 1.10 |
| 10-16 16:16 | +10 stop | NEAR | UP | 0.61 | 0.77 | 1.30 |
| 10-16 16:16 | +20 | NEAR | UP | 0.61 | 0.83 | 1.93 |
| 10-16 16:16 | +15 | NEAR | UP | 0.61 | 0.77 | 1.30 |
| 10-16 16:16 | +10 | NEAR | UP | 0.61 | 0.77 | 1.30 |
| 10-16 16:16 | +5 | NEAR | UP | 0.62 | 0.68 | 0.28 |
| 10-16 16:16 | +10 stop | DOGE | UP | 0.63 | 0.42 | -2.45 |
| 10-16 16:16 | +20 | DOGE | UP | 0.63 | 0.83 | 1.73 |
| 10-16 16:16 | +15 | DOGE | UP | 0.63 | 0.81 | 1.52 |
| 10-16 16:16 | +10 | DOGE | UP | 0.63 | 0.74 | 0.79 |
| 10-16 16:16 | +5 | DOGE | UP | 0.63 | 0.72 | 0.58 |
| 10-16 16:16 | +10 stop | ETH | UP | 0.60 | 0.44 | -1.95 |
| 10-16 16:16 | +20 | ETH | UP | 0.60 | 0.85 | 2.24 |
| 10-16 16:16 | +15 | ETH | UP | 0.60 | 0.85 | 2.24 |
| 10-16 16:16 | +10 | ETH | UP | 0.60 | 0.70 | 0.68 |
| 10-16 16:16 | +5 | ETH | UP | 0.60 | 0.69 | 0.58 |
